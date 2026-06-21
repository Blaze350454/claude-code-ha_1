import asyncio, json, re, pathlib, datetime, websockets

env = dict(re.findall(r'^(\w+)=(.*)$', pathlib.Path('.env').read_text(), re.M))
TOKEN = env['HA_TOKEN']
URL = "ws://192.168.2.151:8123/api/websocket"

stage_card = {"type": "entities", "title": "Feed Stage",
              "entities": [{"entity": "input_select.feed_stage", "name": "Plant stage"}]}

durs = [("Seedling", "seedling"), ("Early Veg", "early_veg"), ("Medium Veg", "medium_veg"),
        ("Late Veg", "late_veg"), ("Early Flower", "early_flower"), ("Mid Flower", "mid_flower"),
        ("Late Flower", "late_flower")]
profile_entities = [{"entity": "input_select.feed_stage", "name": "Current stage"},
                    {"type": "section", "label": "Feed duration (min) per stage"}]
profile_entities += [{"entity": "input_number.feed_dur_" + s, "name": n} for n, s in durs]
profile_entities += [{"type": "section", "label": "Feeds per day per stage"}]
profile_entities += [{"entity": "input_number.feeds_" + s, "name": n} for n, s in durs]
profiles_card = {"type": "entities", "title": "Feed Stage Profiles", "entities": profile_entities}


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
        secs = cfg["views"][0]["sections"]
        stats, settings = secs[0], secs[1]
        # guard against duplicates
        if not any(c.get("title") == "Feed Stage" for c in stats["cards"]):
            mi = next(i for i, c in enumerate(stats["cards"]) if c.get("type") == "markdown")
            stats["cards"].insert(mi + 1, stage_card)
        if not any(c.get("title") == "Feed Stage Profiles" for c in settings["cards"]):
            settings["cards"].insert(1, profiles_card)
        save = await req(ws, {"type": "lovelace/config/save", "url_path": "dashboard-tent", "config": cfg}, 2)
        print("save success:", save.get("success"), save.get("error", ""))
        chk = (await req(ws, {"type": "lovelace/config", "url_path": "dashboard-tent"}, 3))["result"]["views"][0]["sections"]
        print("stats cards:", [c.get("title") or c.get("heading") or c.get("type") for c in chk[0]["cards"]])
        print("settings cards:", [c.get("title") or c.get("heading") or c.get("type") for c in chk[1]["cards"]])

asyncio.run(main())
