"""Hydro Tower — labels / taxonomy (step 3 of tower onboarding).

Applies the v1 tagging taxonomy to the 3 Hydro Tower entities (naming + zoning
already done in tag_migration_hydro_tower_naming.py). All required label_ids
already exist in the registry (verified against the pre-naming snapshot).

Plan (every entity also carries `grow`):
  switch.hydro_tower_water_pump        sys_irrigation + sub_irrigation_feed_loop + fn_pump        + sev_critical
  binary_sensor.hydro_tower_water_level sys_irrigation + sub_irrigation_reservoir + fn_sensor_level + sev_critical
  light.hydro_tower_led                sys_lighting   +                           fn_light         + sev_info

Severity rationale (per tagging_standard worked examples):
  - pump  -> sev_critical (pump failure = plants dry out)
  - water level (reservoir empty/low) -> sev_critical (must block feed cycle)
  - LED is an accent/status light, not the grow light -> sev_info

Entities are freshly created (no prior labels), so this SETS the target label set
rather than merging. Idempotent: skips entities already at the target set.

Run `python registry_export.py --label pre-hydro-tower-labels` first for a snapshot.

Dry-run by default. Pass `--apply` to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

# (entity_id, [target labels])
PLANS: list[tuple[str, list[str]]] = [
    ("switch.hydro_tower_water_pump",
     ["sys_irrigation", "sub_irrigation_feed_loop", "fn_pump", "sev_critical", "grow"]),
    ("binary_sensor.hydro_tower_water_level",
     ["sys_irrigation", "sub_irrigation_reservoir", "fn_sensor_level", "sev_critical", "grow"]),
    ("light.hydro_tower_led",
     ["sys_lighting", "fn_light", "sev_info", "grow"]),
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

        ok = fail = 0
        for eid, target in PLANS:
            e = ent_by_id.get(eid)
            if not e:
                print(f"  MISSING entity: {eid}")
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

        print(f"\nResult: {ok} OK, {fail} FAIL (of {len(PLANS)} entities)")
        if not do:
            print("DRY-RUN — re-run with --apply to commit.")


if __name__ == "__main__":
    asyncio.run(main())
