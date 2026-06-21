"""Hydro Tower diagnostics — entity_id cleanup.

The 6 diagnostic entities created on the post-secretize reflash came in with a
`front_sunroom_` prefix (this HA instance bakes the device's AREA name into new
entity_ids at creation — same mechanism that gave the original 3 a `mom_grow_`
prefix). Friendly names are already correct ("Hydro Tower ..."). This strips the
area prefix to match the `hydro_tower_*` convention.

Run `python registry_export.py --label pre-hydro-tower-diag-naming` first.
Dry-run by default. Pass `--apply` to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

RENAMES: list[tuple[str, str]] = [
    ("sensor.front_sunroom_hydro_tower_wifi_signal",    "sensor.hydro_tower_wifi_signal"),
    ("sensor.front_sunroom_hydro_tower_uptime",         "sensor.hydro_tower_uptime"),
    ("sensor.front_sunroom_hydro_tower_ip_address",     "sensor.hydro_tower_ip_address"),
    ("sensor.front_sunroom_hydro_tower_connected_ssid", "sensor.hydro_tower_connected_ssid"),
    ("sensor.front_sunroom_hydro_tower_mac_address",    "sensor.hydro_tower_mac_address"),
    ("sensor.front_sunroom_hydro_tower_esphome_version","sensor.hydro_tower_esphome_version"),
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
        entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
        ent = {e["entity_id"] for e in entities}

        ok = fail = 0
        for old_eid, new_eid in RENAMES:
            if old_eid not in ent and new_eid in ent:
                print(f"  noop (already renamed): {new_eid}")
                ok += 1
                continue
            if old_eid not in ent:
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

        print(f"\nResult: {ok} OK, {fail} FAIL (of {len(RENAMES)} renames)")
        if not do:
            print("DRY-RUN — re-run with --apply to commit.")


if __name__ == "__main__":
    asyncio.run(main())
