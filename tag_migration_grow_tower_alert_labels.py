"""Grow Tower — alert banner + notification labels.

Applies the v1 tagging taxonomy to the new tower alert-banner backend
(packages/tower/control/alert_banner.yaml) and the 2 new notification
automations in packages/tower/irrigation/reservoir.yaml. Labels-only — no
renames, no area changes: these are all YAML-defined helpers/template
entities/script/automations with explicit id/unique_id, not ESPHome-
synthesized, so there's no area-prefix quirk to correct.

automation.tower_irrigation_block_pump_when_dry is intentionally NOT in
PLANS — only its actions changed (added the LOW-dry push +
persistent_notification), not its role/severity, so its existing labels
from the earlier pump-automation labeling pass are left untouched.

Run `python registry_export.py --label pre-tower-alert-banner-labels` first.

Dry-run by default. Pass `--apply` to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

PLANS: list[tuple[str, list[str]]] = [
    ("input_boolean.tower_alert_details_open",   ["sys_irrigation", "sev_info", "grow"]),
    ("input_datetime.tower_alert_snooze_until",  ["sys_irrigation", "sev_info", "grow"]),
    ("input_text.tower_alert_snoozed_keys",      ["sys_irrigation", "sev_info", "grow"]),
    ("input_select.tower_alert_snooze_duration", ["sys_irrigation", "sev_info", "grow"]),
    ("sensor.tower_error_list",                  ["sys_irrigation", "sev_info", "grow"]),
    ("binary_sensor.tower_alert_banner",         ["sys_irrigation", "sev_warning", "grow"]),
    ("script.tower_alert_snooze",                ["sys_irrigation", "sev_info", "grow"]),
    ("automation.alert_tower_reservoir_medium_dry",
     ["sys_irrigation", "sub_irrigation_reservoir", "sev_warning", "grow"]),
    ("automation.alert_tower_reservoir_low_dry_repeat",
     ["sys_irrigation", "sub_irrigation_reservoir", "sev_critical", "grow"]),
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
