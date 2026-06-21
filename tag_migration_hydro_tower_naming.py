"""Hydro Tower — naming + zoning fix (steps 1 & 2 of tower onboarding).

Background:
  The Hydro Tower ESP32 was originally adopted while the device sat in the
  "Mom Grow" area, so HA baked a `mom_grow_` prefix into its entity_ids even
  though the friendly names are correct ("Hydro Tower ..."). The user now wants
  the device in its own room area.

This script (idempotent, dry-run by default):
  1. Ensures the "Main" floor exists (created previously for Mom Grow).
  2. Ensures area "Front Sunroom" exists on the Main floor (creates if missing).
  3. Finds the Hydro Tower device (via its entities' device_id) and moves it
     from "Mom Grow" into "Front Sunroom".
  4. Renames the 3 entity_ids, stripping the stray `mom_grow_` prefix:
       switch.mom_grow_hydro_tower_water_pump   -> switch.hydro_tower_water_pump
       binary_sensor.mom_grow_hydro_tower_water_level
                                                -> binary_sensor.hydro_tower_water_level
       light.mom_grow_hydro_tower_led           -> light.hydro_tower_led

NOT in scope here (deliberately): labels / sys_/sub_/fn_/sev_ taxonomy. That's
step 3 and will be a separate pass once naming + zoning are confirmed.

Run `python registry_export.py --label pre-hydro-tower-naming` first for a snapshot.

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
AREA_NAME = "Front Sunroom"
AREA_ID = "front_sunroom"

# (old_entity_id, new_entity_id) — strip the mom_grow_ prefix. No labels (step 3).
RENAMES: list[tuple[str, str]] = [
    ("switch.mom_grow_hydro_tower_water_pump",        "switch.hydro_tower_water_pump"),
    ("binary_sensor.mom_grow_hydro_tower_water_level", "binary_sensor.hydro_tower_water_level"),
    ("light.mom_grow_hydro_tower_led",                "light.hydro_tower_led"),
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

        # 2. Ensure Front Sunroom area exists on Main floor
        areas = (await ws_call(ws, mid, type="config/area_registry/list"))["result"]; mid += 1
        area = next((a for a in areas
                     if a.get("area_id") == AREA_ID or a.get("name") == AREA_NAME), None)
        if area:
            AREA_ID_RESOLVED = area["area_id"]
            print(f"[area] exists: {AREA_ID_RESOLVED} ({area.get('name')})")
            if do and area.get("floor_id") != floor_id:
                await ws_call(ws, mid, type="config/area_registry/update",
                              area_id=AREA_ID_RESOLVED, floor_id=floor_id); mid += 1
                print(f"  -> updated floor_id={floor_id}")
        else:
            print(f"[area] {'WOULD CREATE' if not do else 'CREATE'}: {AREA_NAME} (floor={FLOOR_NAME})")
            AREA_ID_RESOLVED = AREA_ID
            if do:
                r = await ws_call(ws, mid, type="config/area_registry/create",
                                   name=AREA_NAME, floor_id=floor_id); mid += 1
                AREA_ID_RESOLVED = r["result"]["area_id"]
                print(f"  -> area_id={AREA_ID_RESOLVED}")

        # 3. Fetch registries; locate the Hydro Tower device via its entities
        devs = (await ws_call(ws, mid, type="config/device_registry/list"))["result"]; mid += 1
        dev_by_id = {d["id"]: d for d in devs}
        entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
        ent_by_id = {e["entity_id"]: e for e in entities}

        device_ids = set()
        for old_eid, new_eid in RENAMES:
            e = ent_by_id.get(old_eid) or ent_by_id.get(new_eid)
            if e and e.get("device_id"):
                device_ids.add(e["device_id"])
        if len(device_ids) != 1:
            print(f"[device] WARNING: expected exactly 1 Hydro Tower device, found {device_ids}")
        for did in device_ids:
            d = dev_by_id.get(did, {})
            cur_area = d.get("area_id")
            dname = d.get("name_by_user") or d.get("name")
            if cur_area == AREA_ID_RESOLVED:
                print(f"[device] '{dname}' already in {AREA_ID_RESOLVED}")
                continue
            print(f"[device] {'WOULD MOVE' if not do else 'MOVE'} '{dname}': {cur_area} -> {AREA_ID_RESOLVED}")
            if do:
                await ws_call(ws, mid, type="config/device_registry/update",
                              device_id=did, area_id=AREA_ID_RESOLVED); mid += 1

        # 4. Rename entity_ids (strip mom_grow_ prefix)
        ok = fail = 0
        for old_eid, new_eid in RENAMES:
            if old_eid not in ent_by_id and new_eid in ent_by_id:
                print(f"  noop (already renamed): {new_eid}")
                ok += 1
                continue
            if old_eid not in ent_by_id:
                print(f"  MISSING: {old_eid} (and no {new_eid})")
                fail += 1
                continue
            print(f"  {'WOULD RENAME' if not do else 'RENAME'}: {old_eid} -> {new_eid}")
            if do:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                  entity_id=old_eid, new_entity_id=new_eid); mid += 1
                if r.get("success"): ok += 1
                else: fail += 1; print(f"    FAIL: {r}")
            else:
                ok += 1

        print(f"\nResult: {ok} OK, {fail} FAIL (of {len(RENAMES)} entity renames)")
        if not do:
            print("DRY-RUN — re-run with --apply to commit.")


if __name__ == "__main__":
    asyncio.run(main())
