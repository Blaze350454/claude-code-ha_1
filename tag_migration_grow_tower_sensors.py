"""Grow Tower — rename + label the 3 water-level XKC-Y25 sensors (2026-07-16).

Background:
  Firmware added HIGH (GPIO32) + MEDIUM (GPIO33) XKC-Y25 sensors and moved the
  existing LOW sensor GPIO34 -> GPIO14 (see memory `project_grow_tower`). On
  reflash, HA created 3 new entities with the device's area name baked into the
  entity_id (a known quirk of this HA instance - same thing happened to the
  original hydro-tower entities when they were first created):

    binary_sensor.front_sunroom_grow_tower_water_level_low
    binary_sensor.front_sunroom_grow_tower_water_level_high
    binary_sensor.front_sunroom_grow_tower_water_level_medium

This script (idempotent, dry-run by default):
  1. Renames the 3 entity_ids, stripping the `front_sunroom_` prefix.
  2. Applies tagging-standard labels (all `sys_irrigation` + `sub_irrigation_reservoir`
     + `fn_sensor_level` + `grow`), severity per role per the standard's worked
     examples (feed-tank empty -> sev_critical, half-full -> sev_info):
       LOW (near pump intake, critical alert + future pump lockout)      -> sev_critical
       MEDIUM (early "refill soon" notify-only nudge, recoverable)       -> sev_warning
       HIGH (full mark, status indicator, not actionable on its own)     -> sev_info

Run `python registry_export.py --label pre-grow-tower-sensors` first for a snapshot.

Dry-run by default. Pass `--apply` to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

# (old_entity_id, new_entity_id) — strip the front_sunroom_ prefix.
RENAMES: list[tuple[str, str]] = [
    ("binary_sensor.front_sunroom_grow_tower_water_level_low",
     "binary_sensor.grow_tower_water_level_low"),
    ("binary_sensor.front_sunroom_grow_tower_water_level_high",
     "binary_sensor.grow_tower_water_level_high"),
    ("binary_sensor.front_sunroom_grow_tower_water_level_medium",
     "binary_sensor.grow_tower_water_level_medium"),
]

# (final entity_id, [target labels])
PLANS: list[tuple[str, list[str]]] = [
    ("binary_sensor.grow_tower_water_level_low",
     ["sys_irrigation", "sub_irrigation_reservoir", "fn_sensor_level", "sev_critical", "grow"]),
    ("binary_sensor.grow_tower_water_level_medium",
     ["sys_irrigation", "sub_irrigation_reservoir", "fn_sensor_level", "sev_warning", "grow"]),
    ("binary_sensor.grow_tower_water_level_high",
     ["sys_irrigation", "sub_irrigation_reservoir", "fn_sensor_level", "sev_info", "grow"]),
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

        # Confirm all referenced labels exist
        labels = (await ws_call(ws, mid, type="config/label_registry/list"))["result"]; mid += 1
        existing = {l["label_id"] for l in labels}
        wanted = {lab for _, labs in PLANS for lab in labs}
        missing = wanted - existing
        if missing:
            print(f"ABORT: missing labels in registry: {sorted(missing)}")
            return

        entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
        ent_by_id = {e["entity_id"]: e for e in entities}

        # 1. Rename entity_ids (strip front_sunroom_ prefix)
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

        print(f"\nRename result: {ok} OK, {fail} FAIL (of {len(RENAMES)})")

        # Re-fetch registry after renames so label step sees final entity_ids
        if do:
            entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
            ent_by_id = {e["entity_id"]: e for e in entities}

        # 2. Apply labels
        ok = fail = 0
        for eid, target in PLANS:
            e = ent_by_id.get(eid)
            if not e:
                print(f"  MISSING entity (rename not applied yet?): {eid}")
                fail += 1
                continue
            cur = set(e.get("labels") or [])
            if cur == set(target):
                print(f"  noop (already labeled): {eid}")
                ok += 1
                continue
            print(f"  {'WOULD LABEL' if not do else 'LABEL'}: {eid} -> {sorted(target)}")
            if do:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                  entity_id=eid, labels=sorted(target)); mid += 1
                if r.get("success"): ok += 1
                else: fail += 1; print(f"    FAIL: {r}")
            else:
                ok += 1

        print(f"\nLabel result: {ok} OK, {fail} FAIL (of {len(PLANS)})")
        if not do:
            print("DRY-RUN — re-run with --apply to commit.")


if __name__ == "__main__":
    asyncio.run(main())
