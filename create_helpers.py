"""
Create Home Assistant helper entities via WebSocket API.

Strategy for getting exact entity IDs:
- HA generates storage id from the name via slugify (lowercase, spaces->underscores)
- So to get id=feed_duration_minutes, we create with name="Feed Duration Minutes"
- Then update with the actual display name e.g. "Feed Duration"
- The id and entity_id never change after creation.

Each entry has:
  slug_name: used at creation time to generate the right id
  display_name: set after creation via update (this is the friendly_name shown in UI)
  id: the expected storage id (= entity_id suffix)
"""
import asyncio
import json
import os
import websockets

HA_WS = 'ws://192.168.2.151:8123/api/websocket'
TOKEN = os.environ['HA_TOKEN']

# slug_name -> HA will create id by slugifying this
# After creation, we update 'name' to display_name
INPUT_NUMBERS = [
    {
        "id": "feeds_per_day",
        "slug_name": "Feeds Per Day",
        "display_name": "Feeds Per Day",
        "min": 2, "max": 12, "step": 1, "initial": 4,
        "unit_of_measurement": "feeds", "icon": "mdi:counter", "mode": "box",
    },
    {
        "id": "feed_duration_minutes",
        "slug_name": "Feed Duration Minutes",
        "display_name": "Feed Duration",
        "min": 0.5, "max": 30, "step": 0.5, "initial": 3,
        "unit_of_measurement": "min", "icon": "mdi:timer", "mode": "box",
    },
    {
        "id": "flush_duration_minutes",
        "slug_name": "Flush Duration Minutes",
        "display_name": "Flush Duration",
        "min": 0.5, "max": 10, "step": 0.5, "initial": 1.5,
        "unit_of_measurement": "min", "icon": "mdi:timer-outline", "mode": "box",
    },
    {
        "id": "air_stir_lead_minutes",
        "slug_name": "Air Stir Lead Minutes",
        "display_name": "Air/Stir Lead Time",
        "min": 5, "max": 120, "step": 5, "initial": 45,
        "unit_of_measurement": "min", "icon": "mdi:clock-start", "mode": "box",
    },
    {
        "id": "air_on_duration_minutes",
        "slug_name": "Air On Duration Minutes",
        "display_name": "Air Pump On Duration",
        "min": 5, "max": 60, "step": 5, "initial": 20,
        "unit_of_measurement": "min", "icon": "mdi:air-purifier", "mode": "box",
    },
    {
        "id": "stir_on_duration_minutes",
        "slug_name": "Stir On Duration Minutes",
        "display_name": "Stir Pump On Duration",
        "min": 5, "max": 60, "step": 5, "initial": 20,
        "unit_of_measurement": "min", "icon": "mdi:rotate-3d-variant", "mode": "box",
    },
    {
        "id": "night_delay_minutes",
        "slug_name": "Night Delay Minutes",
        "display_name": "Night Cycle Delay After Lights Off",
        "min": 0, "max": 120, "step": 5, "initial": 60,
        "unit_of_measurement": "min", "icon": "mdi:weather-night", "mode": "box",
    },
    {
        "id": "flush_cycle_drain_minutes",
        "slug_name": "Flush Cycle Drain Minutes",
        "display_name": "Flush Cycle Drain Duration",
        "min": 1, "max": 30, "step": 1, "initial": 5,
        "unit_of_measurement": "min", "icon": "mdi:pipe-valve", "mode": "box",
    },
    {
        "id": "flush_cycle_plant_minutes",
        "slug_name": "Flush Cycle Plant Minutes",
        "display_name": "Flush Cycle Plant Duration",
        "min": 1, "max": 30, "step": 1, "initial": 5,
        "unit_of_measurement": "min", "icon": "mdi:flower-outline", "mode": "box",
    },
    {
        "id": "flush_day_counter",
        "slug_name": "Flush Day Counter",
        "display_name": "Flush Day Counter",
        "min": 1, "max": 3, "step": 1, "initial": 1,
        "icon": "mdi:calendar-clock", "mode": "box",
    },
    {
        "id": "current_feed_number",
        "slug_name": "Current Feed Number",
        "display_name": "Current Feed Number",
        "min": 0, "max": 12, "step": 1, "initial": 0,
        "icon": "mdi:numeric", "mode": "box",
    },
]

INPUT_DATETIMES = [
    {
        "id": "next_feed_time",
        "slug_name": "Next Feed Time",
        "display_name": "Next Feed Time",
        "has_date": True, "has_time": True,
    },
    {
        "id": "next_pre_feed_start",
        "slug_name": "Next Pre Feed Start",
        "display_name": "Pre-Feed Air/Stir Start",
        "has_date": True, "has_time": True,
    },
    {
        "id": "next_pre_feed_stop",
        "slug_name": "Next Pre Feed Stop",
        "display_name": "Pre-Feed Air/Stir Stop",
        "has_date": True, "has_time": True,
    },
    {
        "id": "night_cycle_start",
        "slug_name": "Night Cycle Start",
        "display_name": "Night Cycle Start Time",
        "has_date": True, "has_time": True,
    },
]

INPUT_BOOLEANS = [
    {
        "id": "alternating_active",
        "slug_name": "Alternating Active",
        "display_name": "Air/Stir Alternating Active",
        "icon": "mdi:sync",
    },
    {
        "id": "irrigation_enabled",
        "slug_name": "Irrigation Enabled",
        "display_name": "Irrigation Enabled",
        "icon": "mdi:sprinkler-variant",
    },
]

INPUT_TEXTS = [
    {
        "id": "irrigation_status",
        "slug_name": "Irrigation Status",
        "display_name": "Irrigation Status",
        "initial": "Idle",
        "icon": "mdi:information-outline",
    },
]


async def ws_send(ws, payload):
    await ws.send(json.dumps(payload))
    return json.loads(await ws.recv())


async def create_helpers():
    results = []
    msg_id = [1]

    def nid():
        i = msg_id[0]
        msg_id[0] += 1
        return i

    async with websockets.connect(HA_WS) as ws:
        await ws.recv()
        await ws.send(json.dumps({'type': 'auth', 'access_token': TOKEN}))
        auth = json.loads(await ws.recv())
        if auth.get('type') != 'auth_ok':
            print(f"Auth failed: {auth}")
            return
        print("WebSocket authenticated OK\n")

        # Get existing editable items for each domain
        nr_list = await ws_send(ws, {'id': nid(), 'type': 'input_number/list'})
        existing_numbers = {item['id']: item for item in (nr_list.get('result') or [])}

        dt_list = await ws_send(ws, {'id': nid(), 'type': 'input_datetime/list'})
        existing_datetimes = {item['id']: item for item in (dt_list.get('result') or [])}

        bl_list = await ws_send(ws, {'id': nid(), 'type': 'input_boolean/list'})
        existing_booleans = {item['id']: item for item in (bl_list.get('result') or [])}

        tx_list = await ws_send(ws, {'id': nid(), 'type': 'input_text/list'})
        existing_texts = {item['id']: item for item in (tx_list.get('result') or [])}

        # ========================
        # INPUT_NUMBERS
        # ========================
        print("=== INPUT_NUMBER ===")
        for cfg in INPUT_NUMBERS:
            entity_id = f"input_number.{cfg['id']}"
            item_id = cfg['id']

            if item_id in existing_numbers:
                # Update - correct all fields including display name
                payload = {
                    "id": nid(),
                    "type": "input_number/update",
                    "input_number_id": item_id,
                    "name": cfg["display_name"],
                    "min": cfg["min"],
                    "max": cfg["max"],
                    "step": cfg["step"],
                    "mode": cfg.get("mode", "box"),
                }
                if "initial" in cfg:
                    payload["initial"] = cfg["initial"]
                if "unit_of_measurement" in cfg:
                    payload["unit_of_measurement"] = cfg["unit_of_measurement"]
                if "icon" in cfg:
                    payload["icon"] = cfg["icon"]
                resp = await ws_send(ws, payload)
                ok = resp.get('success', False)
                detail = "" if ok else str(resp.get('error', ''))
                results.append(("UPDATE", entity_id, ok, detail))
                print(f"  UPDATE {entity_id}: {'OK' if ok else 'FAIL: ' + detail}")
            else:
                # Create with slug_name to get the right id
                payload = {
                    "id": nid(),
                    "type": "input_number/create",
                    "name": cfg["slug_name"],
                    "min": cfg["min"],
                    "max": cfg["max"],
                    "step": cfg["step"],
                    "mode": cfg.get("mode", "box"),
                }
                if "initial" in cfg:
                    payload["initial"] = cfg["initial"]
                if "unit_of_measurement" in cfg:
                    payload["unit_of_measurement"] = cfg["unit_of_measurement"]
                if "icon" in cfg:
                    payload["icon"] = cfg["icon"]
                resp = await ws_send(ws, payload)
                ok = resp.get('success', False)
                created_id = resp.get('result', {}).get('id', '') if ok else ''

                if ok and created_id != item_id:
                    print(f"  CREATE {entity_id}: WARNING - got id={created_id} expected={item_id}")
                    results.append(("CREATE", entity_id, False, f"Wrong id: got {created_id}"))
                elif ok:
                    # Now update display name if different from slug_name
                    if cfg['slug_name'] != cfg['display_name']:
                        upd = {
                            "id": nid(),
                            "type": "input_number/update",
                            "input_number_id": created_id,
                            "name": cfg["display_name"],
                            "min": cfg["min"],
                            "max": cfg["max"],
                            "step": cfg["step"],
                            "mode": cfg.get("mode", "box"),
                        }
                        if "initial" in cfg:
                            upd["initial"] = cfg["initial"]
                        if "unit_of_measurement" in cfg:
                            upd["unit_of_measurement"] = cfg["unit_of_measurement"]
                        if "icon" in cfg:
                            upd["icon"] = cfg["icon"]
                        upd_resp = await ws_send(ws, upd)
                        upd_ok = upd_resp.get('success', False)
                        print(f"  CREATE {entity_id}: OK (id={created_id}) | rename to '{cfg['display_name']}': {'OK' if upd_ok else 'FAIL'}")
                        results.append(("CREATE", entity_id, True, f"id={created_id}, renamed={upd_ok}"))
                    else:
                        results.append(("CREATE", entity_id, True, f"id={created_id}"))
                        print(f"  CREATE {entity_id}: OK (id={created_id})")
                else:
                    detail = str(resp.get('error', ''))
                    results.append(("CREATE", entity_id, False, detail))
                    print(f"  CREATE {entity_id}: FAIL: {detail}")

        # ========================
        # INPUT_DATETIMES
        # ========================
        print("\n=== INPUT_DATETIME ===")
        for cfg in INPUT_DATETIMES:
            entity_id = f"input_datetime.{cfg['id']}"
            item_id = cfg['id']

            if item_id in existing_datetimes:
                payload = {
                    "id": nid(),
                    "type": "input_datetime/update",
                    "input_datetime_id": item_id,
                    "name": cfg["display_name"],
                    "has_date": cfg["has_date"],
                    "has_time": cfg["has_time"],
                }
                resp = await ws_send(ws, payload)
                ok = resp.get('success', False)
                detail = "" if ok else str(resp.get('error', ''))
                results.append(("UPDATE", entity_id, ok, detail))
                print(f"  UPDATE {entity_id}: {'OK' if ok else 'FAIL: ' + detail}")
            else:
                payload = {
                    "id": nid(),
                    "type": "input_datetime/create",
                    "name": cfg["slug_name"],
                    "has_date": cfg["has_date"],
                    "has_time": cfg["has_time"],
                }
                resp = await ws_send(ws, payload)
                ok = resp.get('success', False)
                created_id = resp.get('result', {}).get('id', '') if ok else ''

                if ok and created_id != item_id:
                    print(f"  CREATE {entity_id}: WARNING - got id={created_id} expected={item_id}")
                    results.append(("CREATE", entity_id, False, f"Wrong id: got {created_id}"))
                elif ok:
                    if cfg['slug_name'] != cfg['display_name']:
                        upd = {
                            "id": nid(),
                            "type": "input_datetime/update",
                            "input_datetime_id": created_id,
                            "name": cfg["display_name"],
                            "has_date": cfg["has_date"],
                            "has_time": cfg["has_time"],
                        }
                        upd_resp = await ws_send(ws, upd)
                        upd_ok = upd_resp.get('success', False)
                        print(f"  CREATE {entity_id}: OK (id={created_id}) | rename: {'OK' if upd_ok else 'FAIL'}")
                        results.append(("CREATE", entity_id, True, f"id={created_id}, renamed={upd_ok}"))
                    else:
                        results.append(("CREATE", entity_id, True, f"id={created_id}"))
                        print(f"  CREATE {entity_id}: OK (id={created_id})")
                else:
                    detail = str(resp.get('error', ''))
                    results.append(("CREATE", entity_id, False, detail))
                    print(f"  CREATE {entity_id}: FAIL: {detail}")

        # ========================
        # INPUT_BOOLEANS
        # ========================
        print("\n=== INPUT_BOOLEAN ===")
        for cfg in INPUT_BOOLEANS:
            entity_id = f"input_boolean.{cfg['id']}"
            item_id = cfg['id']

            if item_id in existing_booleans:
                payload = {
                    "id": nid(),
                    "type": "input_boolean/update",
                    "input_boolean_id": item_id,
                    "name": cfg["display_name"],
                    "icon": cfg.get("icon"),
                }
                payload = {k: v for k, v in payload.items() if v is not None}
                resp = await ws_send(ws, payload)
                ok = resp.get('success', False)
                detail = "" if ok else str(resp.get('error', ''))
                results.append(("UPDATE", entity_id, ok, detail))
                print(f"  UPDATE {entity_id}: {'OK' if ok else 'FAIL: ' + detail}")
            else:
                payload = {
                    "id": nid(),
                    "type": "input_boolean/create",
                    "name": cfg["slug_name"],
                }
                if "icon" in cfg:
                    payload["icon"] = cfg["icon"]
                resp = await ws_send(ws, payload)
                ok = resp.get('success', False)
                created_id = resp.get('result', {}).get('id', '') if ok else ''

                if ok and created_id != item_id:
                    print(f"  CREATE {entity_id}: WARNING - got id={created_id} expected={item_id}")
                    results.append(("CREATE", entity_id, False, f"Wrong id: got {created_id}"))
                elif ok:
                    if cfg['slug_name'] != cfg['display_name']:
                        upd = {
                            "id": nid(),
                            "type": "input_boolean/update",
                            "input_boolean_id": created_id,
                            "name": cfg["display_name"],
                            "icon": cfg.get("icon"),
                        }
                        upd = {k: v for k, v in upd.items() if v is not None}
                        upd_resp = await ws_send(ws, upd)
                        upd_ok = upd_resp.get('success', False)
                        print(f"  CREATE {entity_id}: OK (id={created_id}) | rename: {'OK' if upd_ok else 'FAIL'}")
                        results.append(("CREATE", entity_id, True, f"id={created_id}, renamed={upd_ok}"))
                    else:
                        results.append(("CREATE", entity_id, True, f"id={created_id}"))
                        print(f"  CREATE {entity_id}: OK (id={created_id})")
                else:
                    detail = str(resp.get('error', ''))
                    results.append(("CREATE", entity_id, False, detail))
                    print(f"  CREATE {entity_id}: FAIL: {detail}")

        # ========================
        # INPUT_TEXTS
        # ========================
        print("\n=== INPUT_TEXT ===")
        for cfg in INPUT_TEXTS:
            entity_id = f"input_text.{cfg['id']}"
            item_id = cfg['id']

            if item_id in existing_texts:
                payload = {
                    "id": nid(),
                    "type": "input_text/update",
                    "input_text_id": item_id,
                    "name": cfg["display_name"],
                    "initial": cfg.get("initial", ""),
                    "icon": cfg.get("icon"),
                }
                payload = {k: v for k, v in payload.items() if v is not None}
                resp = await ws_send(ws, payload)
                ok = resp.get('success', False)
                detail = "" if ok else str(resp.get('error', ''))
                results.append(("UPDATE", entity_id, ok, detail))
                print(f"  UPDATE {entity_id}: {'OK' if ok else 'FAIL: ' + detail}")
            else:
                payload = {
                    "id": nid(),
                    "type": "input_text/create",
                    "name": cfg["slug_name"],
                    "initial": cfg.get("initial", ""),
                    "icon": cfg.get("icon"),
                }
                resp = await ws_send(ws, payload)
                ok = resp.get('success', False)
                created_id = resp.get('result', {}).get('id', '') if ok else ''

                if ok and created_id != item_id:
                    print(f"  CREATE {entity_id}: WARNING - got id={created_id} expected={item_id}")
                    results.append(("CREATE", entity_id, False, f"Wrong id: got {created_id}"))
                elif ok:
                    if cfg['slug_name'] != cfg['display_name']:
                        upd = {
                            "id": nid(),
                            "type": "input_text/update",
                            "input_text_id": created_id,
                            "name": cfg["display_name"],
                            "initial": cfg.get("initial", ""),
                            "icon": cfg.get("icon"),
                        }
                        upd = {k: v for k, v in upd.items() if v is not None}
                        upd_resp = await ws_send(ws, upd)
                        upd_ok = upd_resp.get('success', False)
                        print(f"  CREATE {entity_id}: OK (id={created_id}) | rename: {'OK' if upd_ok else 'FAIL'}")
                        results.append(("CREATE", entity_id, True, f"id={created_id}, renamed={upd_ok}"))
                    else:
                        results.append(("CREATE", entity_id, True, f"id={created_id}"))
                        print(f"  CREATE {entity_id}: OK (id={created_id})")
                else:
                    detail = str(resp.get('error', ''))
                    results.append(("CREATE", entity_id, False, detail))
                    print(f"  CREATE {entity_id}: FAIL: {detail}")

        # SUMMARY
        print("\n" + "=" * 60)
        print("FINAL SUMMARY")
        print("=" * 60)
        ok_count = sum(1 for _, _, ok, _ in results if ok)
        fail_count = sum(1 for _, _, ok, _ in results if not ok)
        print(f"Total: {len(results)} | OK: {ok_count} | FAIL: {fail_count}\n")
        for action, eid, ok, detail in results:
            status = "OK  " if ok else "FAIL"
            print(f"  [{status}] {action:6s} {eid}")
            if detail:
                prefix = "         "
                print(f"{prefix} {detail}")


asyncio.run(create_helpers())
