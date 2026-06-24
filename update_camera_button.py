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

        # Find the "Take Photo" button (in the Tent Camera section) and repoint it
        changed = 0
        for sec in cfg["views"][0]["sections"]:
            for c in sec.get("cards", []):
                if c.get("type") == "button" and c.get("name") == "Take Photo":
                    c["tap_action"] = {
                        "action": "perform-action",
                        "perform_action": "script.tent_camera_snapshot",
                    }
                    changed += 1
        print("buttons updated:", changed)

        save = await req(ws, {"type": "lovelace/config/save", "url_path": "dashboard-tent", "config": cfg}, 2)
        print("save success:", save.get("success"), save.get("error", ""))

        chk = (await req(ws, {"type": "lovelace/config", "url_path": "dashboard-tent"}, 3))["result"]
        for sec in chk["views"][0]["sections"]:
            for c in sec.get("cards", []):
                if c.get("type") == "button" and c.get("name") == "Take Photo":
                    print("verify tap_action:", json.dumps(c["tap_action"]))


asyncio.run(main())
