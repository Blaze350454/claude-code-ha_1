import asyncio, json, re, pathlib, datetime, websockets

env = dict(re.findall(r'^(\w+)=(.*)$', pathlib.Path('.env').read_text(), re.M))
TOKEN = env['HA_TOKEN']
URL = "ws://192.168.2.151:8123/api/websocket"


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

        # whole-word replace camera.tent -> camera.tent_1 anywhere in the config
        raw = json.dumps(cfg)
        new = re.sub(r'camera\.tent(?!_)', 'camera.tent_1', raw)
        print("occurrences replaced:", raw.count('"camera.tent"') ,
              "| total camera.tent (pre):", len(re.findall(r'camera\.tent(?!_)', raw)))
        cfg = json.loads(new)

        save = await req(ws, {"type": "lovelace/config/save", "url_path": "dashboard-tent", "config": cfg}, 2)
        print("save success:", save.get("success"), save.get("error", ""))

        chk = json.dumps((await req(ws, {"type": "lovelace/config", "url_path": "dashboard-tent"}, 3))["result"])
        print("remaining bare camera.tent:", len(re.findall(r'camera\.tent(?!_)', chk)))
        print("camera.tent_1 refs:", chk.count("camera.tent_1"))


asyncio.run(main())
