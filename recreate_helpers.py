"""
Delete mismatched helpers and recreate with correct entity IDs.
HA WebSocket API uses the entity name slug as the ID, but we can try
explicitly passing an id field during creation.
"""
import asyncio
import json
import os
import websockets

HA_WS_URL = "ws://192.168.2.151:8123/api/websocket"
HA_TOKEN = os.environ["HA_TOKEN"]

# Entities to delete (wrong IDs) and their replacement definitions
# Format: (domain, current_slug, desired_slug, full_config)
RECREATIONS = [
    # input_number
    ("input_number", "feed_duration", "feed_duration_minutes", {
        "type": "input_number/create",
        "id": "feed_duration_minutes",
        "name": "Feed Duration",
        "min": 0.5, "max": 30, "step": 0.5, "initial": 3,
        "unit_of_measurement": "min", "icon": "mdi:timer", "mode": "box"
    }),
    ("input_number", "flush_duration", "flush_duration_minutes", {
        "type": "input_number/create",
        "id": "flush_duration_minutes",
        "name": "Flush Duration",
        "min": 0.5, "max": 10, "step": 0.5, "initial": 1.5,
        "unit_of_measurement": "min", "icon": "mdi:timer-outline", "mode": "box"
    }),
    ("input_number", "air_stir_lead_time", "air_stir_lead_minutes", {
        "type": "input_number/create",
        "id": "air_stir_lead_minutes",
        "name": "Air/Stir Lead Time",
        "min": 5, "max": 120, "step": 5, "initial": 45,
        "unit_of_measurement": "min", "icon": "mdi:clock-start", "mode": "box"
    }),
    ("input_number", "air_pump_on_duration", "air_on_duration_minutes", {
        "type": "input_number/create",
        "id": "air_on_duration_minutes",
        "name": "Air Pump On Duration",
        "min": 5, "max": 60, "step": 5, "initial": 20,
        "unit_of_measurement": "min", "icon": "mdi:air-purifier", "mode": "box"
    }),
    ("input_number", "stir_pump_on_duration", "stir_on_duration_minutes", {
        "type": "input_number/create",
        "id": "stir_on_duration_minutes",
        "name": "Stir Pump On Duration",
        "min": 5, "max": 60, "step": 5, "initial": 20,
        "unit_of_measurement": "min", "icon": "mdi:rotate-3d-variant", "mode": "box"
    }),
    ("input_number", "night_cycle_delay_after_lights_off", "night_delay_minutes", {
        "type": "input_number/create",
        "id": "night_delay_minutes",
        "name": "Night Cycle Delay After Lights Off",
        "min": 0, "max": 120, "step": 5, "initial": 60,
        "unit_of_measurement": "min", "icon": "mdi:weather-night", "mode": "box"
    }),
    ("input_number", "flush_cycle_drain_duration", "flush_cycle_drain_minutes", {
        "type": "input_number/create",
        "id": "flush_cycle_drain_minutes",
        "name": "Flush Cycle Drain Duration",
        "min": 1, "max": 30, "step": 1, "initial": 5,
        "unit_of_measurement": "min", "icon": "mdi:pipe-valve", "mode": "box"
    }),
    ("input_number", "flush_cycle_plant_duration", "flush_cycle_plant_minutes", {
        "type": "input_number/create",
        "id": "flush_cycle_plant_minutes",
        "name": "Flush Cycle Plant Duration",
        "min": 1, "max": 30, "step": 1, "initial": 5,
        "unit_of_measurement": "min", "icon": "mdi:flower-outline", "mode": "box"
    }),
    # input_datetime
    ("input_datetime", "pre_feed_air_stir_start", "next_pre_feed_start", {
        "type": "input_datetime/create",
        "id": "next_pre_feed_start",
        "name": "Pre-Feed Air/Stir Start",
        "has_date": True, "has_time": True
    }),
    ("input_datetime", "pre_feed_air_stir_stop", "next_pre_feed_stop", {
        "type": "input_datetime/create",
        "id": "next_pre_feed_stop",
        "name": "Pre-Feed Air/Stir Stop",
        "has_date": True, "has_time": True
    }),
    ("input_datetime", "night_cycle_start_time", "night_cycle_start", {
        "type": "input_datetime/create",
        "id": "night_cycle_start",
        "name": "Night Cycle Start Time",
        "has_date": True, "has_time": True
    }),
    # input_boolean
    ("input_boolean", "air_stir_alternating_active", "alternating_active", {
        "type": "input_boolean/create",
        "id": "alternating_active",
        "name": "Air/Stir Alternating Active",
        "icon": "mdi:sync"
    }),
]

# Also delete the duplicate feeds_per_day created by the virtual state
# Note: feeds_per_day_2 from virtual states might not be in storage


async def recreate():
    results = {"deleted": [], "created": [], "failed": []}
    msg_id = 1

    async with websockets.connect(HA_WS_URL) as ws:
        msg = json.loads(await ws.recv())
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        msg = json.loads(await ws.recv())
        if msg["type"] != "auth_ok":
            print(f"Auth failed: {msg}")
            return results
        print(f"[WS] Authenticated OK")

        async def send_cmd(cmd):
            nonlocal msg_id
            cmd["id"] = msg_id
            msg_id += 1
            await ws.send(json.dumps(cmd))
            resp = json.loads(await ws.recv())
            return resp

        for domain, old_id, new_id, create_config in RECREATIONS:
            print(f"\n--- Processing {domain}: {old_id} -> {new_id} ---")

            # Step 1: Delete old entity
            del_key = f"{domain}_id"
            del_resp = await send_cmd({"type": f"{domain}/delete", del_key: old_id})
            if del_resp.get("success"):
                print(f"  [OK] Deleted {domain}.{old_id}")
                results["deleted"].append(f"{domain}.{old_id}")
            else:
                err = del_resp.get("error", {})
                print(f"  [FAIL] Delete {domain}.{old_id}: {err.get('code')} - {err.get('message')}")
                results["failed"].append(f"delete {domain}.{old_id}: {err}")
                # Still try to create the new one

            # Step 2: Create with desired ID (explicitly passing "id" field)
            resp = await send_cmd(create_config)
            if resp.get("success"):
                result_id = resp.get("result", {}).get("id", "unknown")
                entity_id = f"{domain}.{result_id}"
                print(f"  [OK] Created {entity_id} (requested: {domain}.{new_id})")
                if result_id == new_id:
                    print(f"       ID matches requested!")
                else:
                    print(f"       WARNING: ID mismatch! Got {result_id}, wanted {new_id}")
                results["created"].append(f"{domain}.{result_id} (wanted: {domain}.{new_id})")
            else:
                err = resp.get("error", {})
                print(f"  [FAIL] Create {domain}.{new_id}: {err.get('code')} - {err.get('message')}")
                results["failed"].append(f"create {domain}.{new_id}: {err}")

    return results


async def main():
    results = await recreate()
    print(f"\n\n=== SUMMARY ===")
    print(f"Deleted: {len(results['deleted'])}")
    for d in results["deleted"]:
        print(f"  {d}")
    print(f"\nCreated: {len(results['created'])}")
    for c in results["created"]:
        print(f"  {c}")
    print(f"\nFailed: {len(results['failed'])}")
    for f in results["failed"]:
        print(f"  {f}")


if __name__ == "__main__":
    asyncio.run(main())
