import asyncio, json, re, pathlib, datetime, websockets

env = dict(re.findall(r'^(\w+)=(.*)$', pathlib.Path('.env').read_text(), re.M))
TOKEN = env['HA_TOKEN']
URL = "ws://192.168.2.151:8123/api/websocket"

# Reservoir-dry banner: same flashing style as the ERROR banner above it,
# baby blue (#89CFF0) <-> black. Keys off the shared dry flags
# (binary_sensor.feed/flush_reservoir_dry in templates/irrigation_templates.yaml)
# so the banner, safety automations and error list all use one "dry" definition.
DRY_TEXT = (
    "# {% set f = is_state('binary_sensor.feed_reservoir_dry','on') %}"
    "{% set l = is_state('binary_sensor.flush_reservoir_dry','on') %}"
    "{% if f and l %}FEED & Flush Res DRY"
    "{% elif f %}Feed Res DRY"
    "{% else %}Flush Res DRY{% endif %}"
)

DRY_BANNER = {
    "type": "conditional",
    "conditions": [
        {
            "condition": "or",
            "conditions": [
                {"condition": "state",
                 "entity": "binary_sensor.feed_reservoir_dry", "state": "on"},
                {"condition": "state",
                 "entity": "binary_sensor.flush_reservoir_dry", "state": "on"},
            ],
        }
    ],
    "grid_options": {"columns": "full"},
    "card": {
        "type": "markdown",
        "content": DRY_TEXT,
        "card_mod": {
            "style": {
                ".": "ha-card {\n  border: none;\n  min-height: 130px;\n  position: relative;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  animation: drybg 1.8s ease-in-out infinite;\n}\n@keyframes drybg {0%,100%{background:#89CFF0;}50%{background:#000000;}}\n",
                "ha-markdown$": "h1 {\n  text-align: center;\n  font-size: 4em;\n  font-weight: 900;\n  letter-spacing: 6px;\n  margin: 0;\n  animation: drytx 1.8s ease-in-out infinite;\n}\n@keyframes drytx {0%,100%{color:#000000;}50%{color:#89CFF0;}}\n",
            }
        },
    },
}


async def req(ws, msg, _id):
    msg = dict(msg); msg["id"] = _id
    await ws.send(json.dumps(msg))
    while True:
        m = json.loads(await ws.recv())
        if m.get("id") == _id:
            return m


def is_dry_banner(card):
    return "Res DRY" in json.dumps(card)


def is_error_banner(card):
    return (card.get("type") == "conditional"
            and any(c.get("entity") == "binary_sensor.tent_alert_banner"
                    for c in card.get("conditions", [])))


async def main():
    async with websockets.connect(URL, max_size=None) as ws:
        await ws.recv()
        await ws.send(json.dumps({"type": "auth", "access_token": TOKEN}))
        await ws.recv()
        cfg = (await req(ws, {"type": "lovelace/config", "url_path": "dashboard-tent"}, 1))["result"]
        ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d-%H%M%SZ")
        pathlib.Path(f"dashboard_tent_backup_{ts}.json").write_text(json.dumps(cfg, indent=1))

        sec = cfg["views"][0]["sections"][0]
        if not any(is_error_banner(c) for c in sec["cards"]):
            print("ERROR: alert banner section not found"); return

        sec["cards"] = [c for c in sec["cards"] if not is_dry_banner(c)]
        idx = next(i for i, c in enumerate(sec["cards"]) if is_error_banner(c))
        sec["cards"].insert(idx + 1, DRY_BANNER)

        save = await req(ws, {"type": "lovelace/config/save", "url_path": "dashboard-tent", "config": cfg}, 2)
        print("save success:", save.get("success"), save.get("error", ""))

asyncio.run(main())
