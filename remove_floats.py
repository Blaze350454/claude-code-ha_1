import asyncio, json, re, pathlib, datetime, websockets

env = dict(re.findall(r'^(\w+)=(.*)$', pathlib.Path('.env').read_text(), re.M))
TOKEN = env['HA_TOKEN']
URL = "ws://192.168.2.151:8123/api/websocket"

DROP_HEADINGS = {"Feed floats", "Flush floats", "Table drain floats"}


def keep(card):
    # drop the float-group heading cards
    if card.get("type") == "heading" and card.get("heading") in DROP_HEADINGS:
        return False
    # drop the float tiles (tiles bound to binary_sensors)
    if card.get("type") == "tile" and str(card.get("entity", "")).startswith("binary_sensor."):
        return False
    return True


async def req(ws, msg, _id):
    msg = dict(msg); msg["id"] = _id
    await ws.send(json.dumps(msg))
    while True:
        m = json.loads(await ws.recv())
        if m.get("id") == _id:
            return m


async def main():
    async with websockets.connect(URL, max_size=None) as ws:
        await ws.recv()
        await ws.send(json.dumps({"type": "auth", "access_token": TOKEN}))
        await ws.recv()
        cfg = (await req(ws, {"type": "lovelace/config", "url_path": "dashboard-tent"}, 1))["result"]
        ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d-%H%M%SZ")
        pathlib.Path(f"dashboard_tent_backup_{ts}.json").write_text(json.dumps(cfg, indent=1))
        sec0 = cfg["views"][0]["sections"][0]
        before = len(sec0["cards"])
        sec0["cards"] = [c for c in sec0["cards"] if keep(c)]
        after = len(sec0["cards"])
        print("stats section cards:", before, "->", after, "(removed %d)" % (before - after))
        save = await req(ws, {"type": "lovelace/config/save", "url_path": "dashboard-tent", "config": cfg}, 2)
        print("save success:", save.get("success"), save.get("error", ""))
        chk = (await req(ws, {"type": "lovelace/config", "url_path": "dashboard-tent"}, 3))["result"]
        remaining = [c.get("heading") or c.get("entity") or c.get("type") for c in chk["views"][0]["sections"][0]["cards"]]
        print("remaining stats cards:", remaining)

asyncio.run(main())
