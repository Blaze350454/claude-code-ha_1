import asyncio, json, re, pathlib, datetime, websockets

env = dict(re.findall(r'^(\w+)=(.*)$', pathlib.Path('.env').read_text(), re.M))
TOKEN = env['HA_TOKEN']
URL = "ws://192.168.2.151:8123/api/websocket"

BUTTON = {
    "type": "custom:button-card",
    "entity": "input_select.tent_timelapse",
    "name": "Timelapse",
    "show_state": True,
    "show_icon": True,
    "size": "22px",
    "tap_action": {"action": "more-info"},
    "state": [
        {"operator": "==", "value": "Off", "icon": "mdi:camera-off",
         "color": "var(--error-color)"},
        {"operator": "default", "icon": "mdi:camera-timer",
         "color": "var(--success-color)"},
    ],
    "styles": {
        "card": [
            {"padding": "8px 12px"},
            {"border-radius": "12px"},
            {"box-shadow": "none"},
            {"border": "[[[ return '1px solid ' + (entity.state === 'Off' ? "
                       "'var(--error-color)' : 'var(--success-color)') ]]]"},
            {"background": "[[[ return entity.state === 'Off' ? "
                          "'rgba(244,67,54,0.14)' : 'rgba(76,175,80,0.14)' ]]]"},
        ],
        "grid": [
            {"grid-template-areas": '"i n" "i s"'},
            {"grid-template-columns": "min-content 1fr"},
            {"gap": "0px 10px"},
        ],
        "img_cell": [{"justify-self": "start"}, {"align-self": "center"}],
        "name": [{"justify-self": "start"}, {"font-weight": "bold"},
                 {"font-size": "13px"}],
        "state": [{"justify-self": "start"}, {"font-size": "12px"},
                  {"opacity": "0.85"}],
    },
}


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

        target = None
        for sec in cfg["views"][0]["sections"]:
            if any(c.get("type") == "heading" and c.get("heading") == "Tent Camera"
                   for c in sec.get("cards", [])):
                target = sec
                break
        if target is None:
            print("ERROR: Tent Camera section not found"); return

        # idempotent: drop any existing timelapse button-card first
        target["cards"] = [c for c in target["cards"]
                           if not (c.get("type") == "custom:button-card"
                                   and c.get("entity") == "input_select.tent_timelapse")]
        target["cards"].append(BUTTON)

        save = await req(ws, {"type": "lovelace/config/save", "url_path": "dashboard-tent", "config": cfg}, 2)
        print("save success:", save.get("success"), save.get("error", ""))

        chk = (await req(ws, {"type": "lovelace/config", "url_path": "dashboard-tent"}, 3))["result"]
        for sec in chk["views"][0]["sections"]:
            if any(c.get("type") == "heading" and c.get("heading") == "Tent Camera"
                   for c in sec.get("cards", [])):
                print("Tent Camera cards:",
                      [c.get("name") or c.get("heading") or c.get("type") for c in sec["cards"]])


asyncio.run(main())
