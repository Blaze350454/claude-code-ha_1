"""Grow Tower — pump/irrigation package labels.

Applies the v1 tagging taxonomy to the new pump-cycle package entities
(packages/grow_tower_package.yaml + packages/tower/irrigation/{pump,safety}.yaml
in the homeassistant-config repo). Unlike tag_migration_grow_tower_sensors.py,
NO rename step is needed here: every entity below is defined directly in HA
config YAML (automation `id:`, script mapping key, input_number/input_boolean
keys, template unique_id) — HA uses that literal value as the entity_id, so
there is no "area baked into entity_id" quirk to correct (that quirk is
specific to entities an integration synthesizes from a device, e.g. ESPHome
API discovery combining area + device name; it cannot happen for
config-defined entities).

Run `python registry_export.py --label pre-grow-tower-pump-labels` first.

Dry-run by default. Pass `--apply` to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

CRITICAL = ["sys_irrigation", "sub_irrigation_feed_loop", "sev_critical", "grow"]
INFO = ["sys_irrigation", "sub_irrigation_feed_loop", "sev_info", "grow"]

PLANS: list[tuple[str, list[str]]] = [
    # NOTE: automation entity_id is slugified from `alias:`, NOT the `id:` field
    # in the YAML (that's just an internal editor key) - these two differ from
    # what you'd guess from the source file's `id:` values.
    ("automation.tower_irrigation_block_pump_when_reservoir_dry", CRITICAL),
    ("script.tower_irrigation_pump_cycle", CRITICAL),
    ("automation.tower_irrigation_master_enable_toggle", INFO),
    ("automation.tower_irrigation_startup_recovery", INFO),
    ("automation.tower_irrigation_seed_default_slider_values", INFO),
    ("binary_sensor.tower_night_mode", INFO),
    ("input_boolean.tower_pump_automation_enabled", INFO),
    ("input_boolean.tower_pump_defaults_seeded", INFO),
    ("input_number.tower_day_on_seconds", INFO),
    ("input_number.tower_day_off_minutes", INFO),
    ("input_number.tower_night_on_seconds", INFO),
    ("input_number.tower_night_off_minutes", INFO),
    ("input_number.tower_sunset_delay_minutes", INFO),
    ("input_number.tower_sunrise_delay_minutes", INFO),
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
