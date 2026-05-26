"""Verify which entities the flood-stop automation's 4 targets will hit.

Each target is an intersection of 3 labels. Confirm they resolve to exactly
the expected entities before deploying.
"""
from __future__ import annotations
import asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

TARGETS = [
    ("valve.close_valve  feed-loop valves",
     ["sys_irrigation","fn_valve","sub_irrigation_feed_loop"]),
    ("valve.close_valve  flush-loop valves",
     ["sys_irrigation","fn_valve","sub_irrigation_flush_loop"]),
    ("switch.turn_off    feed-loop pumps",
     ["sys_irrigation","fn_pump","sub_irrigation_feed_loop"]),
    ("switch.turn_off    flush-loop pumps",
     ["sys_irrigation","fn_pump","sub_irrigation_flush_loop"]),
]


async def ws_call(ws, mid, **kw):
    await ws.send(json.dumps({"id": mid, **kw}))
    while True:
        r = json.loads(await ws.recv())
        if r.get("id") == mid:
            return r


async def main():
    async with websockets.connect(WS_URL, max_size=None) as ws:
        assert json.loads(await ws.recv())["type"] == "auth_required"
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        assert json.loads(await ws.recv())["type"] == "auth_ok"

        entities = (await ws_call(ws, 1, type="config/entity_registry/list"))["result"]

    for name, label_ids in TARGETS:
        matched = []
        for e in entities:
            labels = set(e.get("labels") or [])
            if all(L in labels for L in label_ids):
                matched.append(e["entity_id"])
        print(f"\n[{name}]  labels={label_ids}")
        print(f"  matches: {len(matched)}")
        for eid in sorted(matched):
            print(f"    - {eid}")


if __name__ == "__main__":
    asyncio.run(main())
