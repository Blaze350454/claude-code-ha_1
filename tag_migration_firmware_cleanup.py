"""Follow-up: tag 6 `update.*_firmware` entities missed in phase 1a/1b/1c/1d.

Applies `fn_sensor_status` (same pattern as phase 3d firmware updates).
Strips stray `firmware` loose label from its one holder (update.firmware_2_humidifier)
and deletes the `firmware` label (zero holders post-strip).

Dry-run by default. Pass `--apply` to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

FIRMWARE_UPDATE_ENTITIES = {
    "update.reservoir_prime_pump_tent_firmware",
    "update.reservoir_prime_pump_tent_firmware_2",
    "update.kasa_smart_outdoor_plug_firmware",
    "update.firmware_3_air_conditioner_tent",
    "update.firmware_2_humidifier",
    "update.humidifier_firmware",
}
LOOSE_FIRMWARE_LABEL = "firmware"


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

    async with websockets.connect(WS_URL, max_size=None) as ws:
        assert json.loads(await ws.recv())["type"] == "auth_required"
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        assert json.loads(await ws.recv())["type"] == "auth_ok"

        mid = 1
        entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
        ent_map = {e["entity_id"]: e for e in entities}

        ok = 0
        for eid in FIRMWARE_UPDATE_ENTITIES:
            e = ent_map.get(eid)
            if not e:
                print(f"  MISSING: {eid}")
                continue
            cur = set(e.get("labels") or [])
            new = set(cur)
            new.add("fn_sensor_status")
            new.discard(LOOSE_FIRMWARE_LABEL)
            new_sorted = sorted(new)
            if new_sorted == sorted(cur):
                print(f"  noop: {eid}")
                ok += 1
                continue
            print(f"  {'WOULD SET' if not args.apply else 'SET'}: {eid}  -> {new_sorted}")
            if args.apply:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                   entity_id=eid, labels=new_sorted); mid += 1
                if r.get("success"):
                    ok += 1
                else:
                    print(f"    FAIL: {r}")
            else:
                ok += 1

        # Delete the `firmware` label if now empty
        if args.apply:
            entities_latest = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
        else:
            entities_latest = entities
        holders = [e["entity_id"] for e in entities_latest if LOOSE_FIRMWARE_LABEL in (e.get("labels") or [])]
        if holders:
            print(f"[label] SKIP delete {LOOSE_FIRMWARE_LABEL}: still held by {holders}")
        else:
            print(f"[label] {'WOULD DELETE' if not args.apply else 'DELETE'}: {LOOSE_FIRMWARE_LABEL}")
            if args.apply:
                r = await ws_call(ws, mid, type="config/label_registry/delete",
                                   label_id=LOOSE_FIRMWARE_LABEL); mid += 1
                if not r.get("success"):
                    print(f"  FAIL: {r}")

        print(f"\nResult: {ok}/{len(FIRMWARE_UPDATE_ENTITIES)} OK")
        if not args.apply:
            print("DRY-RUN — re-run with --apply to commit.")


if __name__ == "__main__":
    asyncio.run(main())
