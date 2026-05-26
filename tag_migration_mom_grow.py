"""Mom Grow onboarding — new grow operation on a Kasa EP40M 2-outlet strip.

Creates:
  - Floor:  Main (if missing)
  - Area:   Mom Grow (on Main floor)

Reconfigures the EP40M strip (parent + 2 outlet sub-devices, 16 entities):
  - Renames plug-2 sub-device: "Mom Grow 2" -> "Mom Grow Lights"
  - Renames every entity_id from `unnamed_ep40m_*` to `mom_grow_*` convention
  - Moves all 3 devices into the new area
  - Applies full sys_lighting + grow taxonomy labels

Plug 1 currently has nothing plugged in (reserve). Whole strip tagged sys_lighting
for now since the only active load is the lights on plug 2; plug 1 will be re-tagged
if something else lands on it later.

Dry-run by default. Pass `--apply` to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

FLOOR_NAME = "Main"
AREA_NAME = "Mom Grow"
AREA_ID = "mom_grow"

# Device IDs (from pre-mom-grow snapshot)
DEV_PARENT = "ed25779a"  # Unnamed EP40M (user-renamed: "Mom Grow")
DEV_PLUG1  = "578b0e50"  # Mom Grow 1
DEV_PLUG2  = "76a64941"  # Mom Grow 2 -> rename to "Mom Grow Lights"

PLUG2_NEW_NAME = "Mom Grow Lights"

# (old_entity_id, new_entity_id, [labels...])  — additive (no existing labels to merge)
RENAMES: list[tuple[str, str, list[str]]] = [
    # --- Parent device (strip-level diagnostics) ---
    ("switch.unnamed_ep40m_auto_update_enabled",
     "switch.mom_grow_auto_update_enabled",
     ["sys_lighting", "grow", "fn_controller", "sev_info"]),
    ("switch.unnamed_ep40m_led",
     "switch.mom_grow_led",
     ["sys_lighting", "grow", "fn_controller", "sev_info"]),
    ("binary_sensor.unnamed_ep40m_cloud_connection",
     "binary_sensor.mom_grow_cloud_connection",
     ["sys_lighting", "grow", "fn_sensor_status", "sev_warning"]),
    ("button.unnamed_ep40m_restart",
     "button.mom_grow_restart",
     ["sys_lighting", "grow", "fn_controller", "sev_warning"]),
    ("sensor.unnamed_ep40m_signal_level",
     "sensor.mom_grow_signal_level",
     ["sys_lighting", "grow", "fn_sensor_signal", "sev_info"]),
    ("sensor.unnamed_ep40m_signal_strength",
     "sensor.mom_grow_signal_strength",
     ["sys_lighting", "grow", "fn_sensor_signal", "sev_info"]),
    ("sensor.unnamed_ep40m_ssid",
     "sensor.mom_grow_ssid",
     ["sys_lighting", "grow", "fn_sensor_status", "sev_info"]),
    ("sensor.unnamed_ep40m_device_time",
     "sensor.mom_grow_device_time",
     ["sys_lighting", "grow", "fn_sensor_status", "sev_info"]),

    # --- Plug 1 (reserve / empty) ---
    ("switch.unnamed_ep40m_kasa_smart_plug_1",
     "switch.mom_grow_1",
     ["sys_lighting", "grow", "fn_controller", "sev_info"]),
    ("binary_sensor.unnamed_ep40m_kasa_smart_plug_1_overheated",
     "binary_sensor.mom_grow_1_overheated",
     ["sys_lighting", "grow", "fn_sensor_status", "sev_critical"]),
    ("button.unnamed_ep40m_kasa_smart_plug_1_restart",
     "button.mom_grow_1_restart",
     ["sys_lighting", "grow", "fn_controller", "sev_warning"]),
    ("sensor.unnamed_ep40m_kasa_smart_plug_1_on_since",
     "sensor.mom_grow_1_on_since",
     ["sys_lighting", "grow", "fn_sensor_status", "sev_info"]),

    # --- Plug 2 / Lights ---
    ("switch.unnamed_ep40m_kasa_smart_plug_2",
     "switch.mom_grow_lights",
     ["sys_lighting", "grow", "fn_controller", "sev_critical"]),
    ("binary_sensor.unnamed_ep40m_kasa_smart_plug_2_overheated",
     "binary_sensor.mom_grow_lights_overheated",
     ["sys_lighting", "grow", "fn_sensor_status", "sev_critical"]),
    ("button.unnamed_ep40m_kasa_smart_plug_2_restart",
     "button.mom_grow_lights_restart",
     ["sys_lighting", "grow", "fn_controller", "sev_warning"]),
    ("sensor.unnamed_ep40m_kasa_smart_plug_2_on_since",
     "sensor.mom_grow_lights_on_since",
     ["sys_lighting", "grow", "fn_sensor_status", "sev_info"]),
]


async def ws_call(ws, mid, **kw):
    await ws.send(json.dumps({"id": mid, **kw}))
    while True:
        r = json.loads(await ws.recv())
        if r.get("id") == mid:
            return r


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    do = args.apply

    async with websockets.connect(WS_URL, max_size=None) as ws:
        assert json.loads(await ws.recv())["type"] == "auth_required"
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        assert json.loads(await ws.recv())["type"] == "auth_ok"

        mid = 1

        # 1. Ensure Main floor exists
        floors = (await ws_call(ws, mid, type="config/floor_registry/list"))["result"]; mid += 1
        floor = next((f for f in floors if f.get("name") == FLOOR_NAME), None)
        if floor:
            floor_id = floor["floor_id"]
            print(f"[floor] exists: {FLOOR_NAME} (id={floor_id})")
        else:
            print(f"[floor] {'WOULD CREATE' if not do else 'CREATE'}: {FLOOR_NAME}")
            if do:
                r = await ws_call(ws, mid, type="config/floor_registry/create",
                                   name=FLOOR_NAME); mid += 1
                floor_id = r["result"]["floor_id"]
                print(f"  -> floor_id={floor_id}")
            else:
                floor_id = "<new>"

        # 2. Ensure Mom Grow area exists on Main floor
        areas = (await ws_call(ws, mid, type="config/area_registry/list"))["result"]; mid += 1
        area = next((a for a in areas if a.get("area_id") == AREA_ID), None)
        if area:
            print(f"[area] exists: {AREA_ID}")
            if do and area.get("floor_id") != floor_id:
                r = await ws_call(ws, mid, type="config/area_registry/update",
                                   area_id=AREA_ID, floor_id=floor_id); mid += 1
                print(f"  -> updated floor_id={floor_id}")
        else:
            print(f"[area] {'WOULD CREATE' if not do else 'CREATE'}: {AREA_NAME} (floor={FLOOR_NAME})")
            if do:
                r = await ws_call(ws, mid, type="config/area_registry/create",
                                   name=AREA_NAME, floor_id=floor_id); mid += 1
                print(f"  -> area_id={r['result']['area_id']}")

        # 3. Fetch device + entity registries
        devs = (await ws_call(ws, mid, type="config/device_registry/list"))["result"]; mid += 1
        dev_by_id = {d["id"]: d for d in devs}
        entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
        ent_by_id = {e["entity_id"]: e for e in entities}

        # Resolve partial device IDs to full IDs
        def resolve_dev(prefix8: str) -> str:
            match = [d["id"] for d in devs if d["id"].startswith(prefix8)]
            if len(match) != 1:
                raise RuntimeError(f"ambiguous/missing device prefix {prefix8}: {match}")
            return match[0]

        dev_parent = resolve_dev(DEV_PARENT)
        dev_plug1  = resolve_dev(DEV_PLUG1)
        dev_plug2  = resolve_dev(DEV_PLUG2)

        # 4. Rename plug-2 device to "Mom Grow Lights"
        p2 = dev_by_id[dev_plug2]
        if p2.get("name_by_user") != PLUG2_NEW_NAME:
            print(f"[device] {'WOULD RENAME' if not do else 'RENAME'}: {p2.get('name_by_user')} -> {PLUG2_NEW_NAME}")
            if do:
                await ws_call(ws, mid, type="config/device_registry/update",
                               device_id=dev_plug2, name_by_user=PLUG2_NEW_NAME); mid += 1
        else:
            print(f"[device] plug2 already named {PLUG2_NEW_NAME}")

        # 5. Move all 3 devices into Mom Grow area
        for did, label in [(dev_parent, "parent"), (dev_plug1, "plug1"), (dev_plug2, "plug2")]:
            d = dev_by_id[did]
            if d.get("area_id") == AREA_ID:
                print(f"[device] {label} already in area")
                continue
            print(f"[device] {'WOULD MOVE' if not do else 'MOVE'} {label} -> area {AREA_ID}")
            if do:
                await ws_call(ws, mid, type="config/device_registry/update",
                               device_id=did, area_id=AREA_ID); mid += 1

        # 6. Rename entity_ids + apply labels (one update per entity)
        ok = fail = 0
        for old_eid, new_eid, labels in RENAMES:
            e = ent_by_id.get(old_eid)
            if not e:
                # Maybe already renamed (idempotent)
                e = ent_by_id.get(new_eid)
                if e:
                    cur = set(e.get("labels") or [])
                    if cur == set(labels):
                        print(f"  noop (already renamed+labeled): {new_eid}")
                        ok += 1
                        continue
                    print(f"  {'WOULD RELABEL' if not do else 'RELABEL'}: {new_eid}  -> {sorted(labels)}")
                    if do:
                        r = await ws_call(ws, mid, type="config/entity_registry/update",
                                           entity_id=new_eid, labels=sorted(labels)); mid += 1
                        if r.get("success"): ok += 1
                        else: fail += 1; print(f"    FAIL: {r}")
                    else:
                        ok += 1
                    continue
                print(f"  MISSING: {old_eid} (and no {new_eid})")
                fail += 1
                continue
            print(f"  {'WOULD RENAME+LABEL' if not do else 'RENAME+LABEL'}: {old_eid} -> {new_eid}  {sorted(labels)}")
            if do:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                   entity_id=old_eid,
                                   new_entity_id=new_eid,
                                   labels=sorted(labels)); mid += 1
                if r.get("success"): ok += 1
                else: fail += 1; print(f"    FAIL: {r}")
            else:
                ok += 1

        print(f"\nResult: {ok} OK, {fail} FAIL (of {len(RENAMES)} entity plans)")
        if not do:
            print("DRY-RUN — re-run with --apply to commit.")


if __name__ == "__main__":
    asyncio.run(main())
