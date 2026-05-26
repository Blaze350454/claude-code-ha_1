"""
Fix entity IDs to match the requested IDs.
Uses WebSocket API to list items and update their IDs.
"""
import asyncio
import json
import os
import websockets

HA_WS_URL = "ws://192.168.2.151:8123/api/websocket"
HA_TOKEN = os.environ["HA_TOKEN"]

# Mapping: current_id (as returned by HA) -> desired_id
# HA returns just the slug part after input_number.
ID_RENAMES = {
    "input_number": {
        # current_slug -> desired_slug
        "feed_duration": "feed_duration_minutes",
        "flush_duration": "flush_duration_minutes",
        "air_stir_lead_time": "air_stir_lead_minutes",
        "air_pump_on_duration": "air_on_duration_minutes",
        "stir_pump_on_duration": "stir_on_duration_minutes",
        "night_cycle_delay_after_lights_off": "night_delay_minutes",
        "flush_cycle_drain_duration": "flush_cycle_drain_minutes",
        "flush_cycle_plant_duration": "flush_cycle_plant_minutes",
    },
    "input_datetime": {
        "pre_feed_air_stir_start": "next_pre_feed_start",
        "pre_feed_air_stir_stop": "next_pre_feed_stop",
        "night_cycle_start_time": "night_cycle_start",
    },
    "input_boolean": {
        "air_stir_alternating_active": "alternating_active",
    },
    "input_text": {},
}

# Also need to delete the duplicate feeds_per_day_2
TO_DELETE = {
    "input_number": ["feeds_per_day_2"],
}


async def fix_ids():
    results = {"renamed": [], "deleted": [], "failed": []}
    msg_id = 1

    async with websockets.connect(HA_WS_URL) as ws:
        msg = json.loads(await ws.recv())
        print(f"[WS] Connected: {msg['type']}")

        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        msg = json.loads(await ws.recv())
        if msg["type"] != "auth_ok":
            print(f"[WS] Auth failed: {msg}")
            return results
        print(f"[WS] Authenticated OK")

        async def send_command(cmd):
            nonlocal msg_id
            cmd["id"] = msg_id
            msg_id += 1
            await ws.send(json.dumps(cmd))
            response = json.loads(await ws.recv())
            return response

        # First, list all items to get their internal IDs
        for domain in ["input_number", "input_datetime", "input_boolean", "input_text"]:
            if not ID_RENAMES.get(domain) and not TO_DELETE.get(domain):
                continue

            print(f"\n--- Listing {domain} items ---")
            list_resp = await send_command({"type": f"{domain}/list"})
            if not list_resp.get("success"):
                print(f"  [FAIL] Cannot list {domain}: {list_resp}")
                continue

            items = list_resp.get("result", [])
            print(f"  Found {len(items)} items")

            # Build a map of slug -> item
            items_by_id = {item["id"]: item for item in items}
            print(f"  IDs: {list(items_by_id.keys())}")

            # Handle renames
            renames = ID_RENAMES.get(domain, {})
            for current_id, desired_id in renames.items():
                if current_id not in items_by_id:
                    print(f"  [SKIP] {domain}.{current_id} not found in list")
                    continue

                item = items_by_id[current_id]
                print(f"  Renaming {domain}.{current_id} -> {domain}.{desired_id}")
                
                update_cmd = {"type": f"{domain}/update", "input_number_id": current_id if domain == "input_number" else None}
                
                # Different domains use different field names for the item ID
                if domain == "input_number":
                    update_cmd = {"type": "input_number/update", "input_number_id": current_id}
                elif domain == "input_datetime":
                    update_cmd = {"type": "input_datetime/update", "input_datetime_id": current_id}
                elif domain == "input_boolean":
                    update_cmd = {"type": "input_boolean/update", "input_boolean_id": current_id}
                elif domain == "input_text":
                    update_cmd = {"type": "input_text/update", "input_text_id": current_id}

                # Copy over all existing fields
                for key in ["name", "min", "max", "step", "initial", "unit_of_measurement", "icon", "mode", "has_date", "has_time"]:
                    if key in item:
                        update_cmd[key] = item[key]
                
                resp = await send_command(update_cmd)
                if resp.get("success"):
                    print(f"    [OK] Updated (but note: HA may not support ID rename via update)")
                    # Check what actually happened
                    result = resp.get("result", {})
                    print(f"    Result ID: {result.get('id', 'unknown')}")
                    results["renamed"].append(f"{domain}.{current_id} -> {domain}.{desired_id}")
                else:
                    err = resp.get("error", {})
                    print(f"    [FAIL] {err.get('code')} - {err.get('message')}")
                    results["failed"].append(f"rename {domain}.{current_id}: {err}")

            # Handle deletions
            to_del = TO_DELETE.get(domain, [])
            for del_id in to_del:
                if del_id not in items_by_id:
                    print(f"  [SKIP] {domain}.{del_id} not found for deletion")
                    continue

                print(f"  Deleting {domain}.{del_id}")
                if domain == "input_number":
                    del_cmd = {"type": "input_number/delete", "input_number_id": del_id}
                elif domain == "input_boolean":
                    del_cmd = {"type": "input_boolean/delete", "input_boolean_id": del_id}
                
                resp = await send_command(del_cmd)
                if resp.get("success"):
                    print(f"    [OK] Deleted {domain}.{del_id}")
                    results["deleted"].append(f"{domain}.{del_id}")
                else:
                    err = resp.get("error", {})
                    print(f"    [FAIL] {err.get('code')} - {err.get('message')}")
                    results["failed"].append(f"delete {domain}.{del_id}: {err}")

    return results


async def main():
    results = await fix_ids()
    print(f"\n\n=== SUMMARY ===")
    print(f"Renamed: {len(results['renamed'])}")
    for r in results["renamed"]:
        print(f"  {r}")
    print(f"\nDeleted: {len(results['deleted'])}")
    for d in results["deleted"]:
        print(f"  {d}")
    print(f"\nFailed: {len(results['failed'])}")
    for f in results["failed"]:
        print(f"  {f}")


if __name__ == "__main__":
    asyncio.run(main())
