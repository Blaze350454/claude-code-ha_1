"""Hydro Tower diagnostics — labels / taxonomy.

Labels the 6 device-level diagnostic entities (entity_ids already cleaned to
hydro_tower_* in tag_migration_hydro_tower_diag_naming.py).

Per user decision (2026-06-14): device-level diagnostics go under sys_irrigation
(the pump is the device's critical role). All get grow + sev_info.
  WiFi Signal                -> fn_sensor_signal
  Uptime/IP/SSID/MAC/Version -> fn_sensor_status

Run `python registry_export.py --label pre-hydro-tower-diag-labels` first.
Dry-run by default. Pass `--apply` to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

BASE = ["sys_irrigation", "sev_info", "grow"]
PLANS: list[tuple[str, list[str]]] = [
    ("sensor.hydro_tower_wifi_signal",     BASE + ["fn_sensor_signal"]),
    ("sensor.hydro_tower_uptime",          BASE + ["fn_sensor_status"]),
    ("sensor.hydro_tower_ip_address",      BASE + ["fn_sensor_status"]),
    ("sensor.hydro_tower_connected_ssid",  BASE + ["fn_sensor_status"]),
    ("sensor.hydro_tower_mac_address",     BASE + ["fn_sensor_status"]),
    ("sensor.hydro_tower_esphome_version", BASE + ["fn_sensor_status"]),
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
