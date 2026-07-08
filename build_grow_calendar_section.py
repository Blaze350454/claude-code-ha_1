# Adds the "Grow Calendar" section to the Tent dashboard (storage dashboard
# "dashboard-tent"). Backend entities come from
# homeassistant-config/packages/tent/control/grow_calendar.yaml.
#
# Statistical only: date pickers + stat markdown. No control cards — when the
# advance automation is uncommented later, add the grow_calendar_linked toggle
# row here and rerun.
#
# Idempotent: no-op if a "Grow Calendar" section already exists (delete the
# section on the dashboard first to force a rebuild). Inserted after
# "Stage & Light Schedule". Note build_tent_irrigation.py reorders sections on
# rerun (its managed set first, everything else appended in order) — this
# section survives but may move below the managed ones.

import asyncio, json, re, pathlib, datetime, websockets

env = dict(re.findall(r'^(\w+)=(.*)$', pathlib.Path('.env').read_text(), re.M))
TOKEN = env['HA_TOKEN']
URL = "ws://192.168.2.151:8123/api/websocket"

md = r"""{% set stage = states('sensor.grow_scheduled_stage') %}
{% if is_state('input_boolean.grow_active', 'off') %}
**Grow inactive** — set the seedling date and turn on *Grow active*.
{% elif stage == 'Not started' %}
**Not started** — seedling date unset or in the future.
{% elif stage == 'Harvest' %}
# 🌾 HARVEST
**Day {{ states('sensor.grow_day') }}** of grow — {{ states('sensor.grow_stage_day') }} day(s) since harvest date.
{% else %}
## Day {{ states('sensor.grow_day') }} — {{ stage }}
**Stage day {{ states('sensor.grow_stage_day') }}**
{%- set nxt = states('sensor.grow_days_to_next_stage') %}
{%- if nxt not in ['unknown', 'unavailable'] %}
Next: **{{ state_attr('sensor.grow_days_to_next_stage', 'next_stage') }}** in {{ nxt }} day{{ 's' if nxt | int(0) != 1 }}
{%- endif %}
{%- set h = states('sensor.grow_days_to_harvest') %}
{%- if h not in ['unknown', 'unavailable'] %}
Harvest in **{{ h }}** day{{ 's' if h | int(0) != 1 }}
{%- endif %}
{% endif %}

*Display only — stage dates don't change any settings yet.*"""

grow_cal_section = {"type": "grid", "column_span": 1, "cards": [
    {"type": "heading", "heading": "Grow Calendar"},
    {"type": "markdown", "content": md},
    {"type": "entities", "entities": [
        {"entity": "input_boolean.grow_active", "name": "Grow active"},
        {"type": "section", "label": "Stage start dates"},
        {"entity": "input_datetime.grow_stage_seedling_date", "name": "Seedling (grow start)"},
        {"entity": "input_datetime.grow_stage_early_veg_date", "name": "Early Veg"},
        {"entity": "input_datetime.grow_stage_medium_veg_date", "name": "Medium Veg"},
        {"entity": "input_datetime.grow_stage_late_veg_date", "name": "Late Veg"},
        {"entity": "input_datetime.grow_stage_early_flower_date", "name": "Early Flower"},
        {"entity": "input_datetime.grow_stage_mid_flower_date", "name": "Mid Flower"},
        {"entity": "input_datetime.grow_stage_late_flower_date", "name": "Late Flower"},
        {"entity": "input_datetime.grow_harvest_date", "name": "Harvest"},
    ]},
    {"show_name": True, "show_icon": True, "show_state": False, "type": "button",
     "name": "Fill dates from seedling start", "icon": "mdi:calendar-refresh",
     "tap_action": {"action": "perform-action",
       "perform_action": "script.grow_calendar_fill_defaults",
       "confirmation": {"text": "Fill all stage dates from the seedling start "
         "date using default stage lengths? This overwrites the other 7 dates."}}},
]}


def first_heading(sec):
    for c in sec.get("cards", []):
        if c.get("type") == "heading":
            return c.get("heading")
    return None


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
        print("backup:", f"dashboard_tent_backup_{ts}.json")
        secs = cfg["views"][0]["sections"]
        # Safety: make sure we're looking at the right dashboard before we touch it.
        assert any(first_heading(s) == "Irrigation" for s in secs), \
            "no 'Irrigation' section found — wrong dashboard or unexpected layout?"
        if any(first_heading(s) == "Grow Calendar" for s in secs):
            print("Grow Calendar section already present — nothing to do.")
            return
        idx = next((i for i, s in enumerate(secs)
                    if first_heading(s) == "Stage & Light Schedule"), None)
        pos = idx + 1 if idx is not None else len(secs)
        secs.insert(pos, grow_cal_section)
        save = await req(ws, {"type": "lovelace/config/save", "url_path": "dashboard-tent", "config": cfg}, 2)
        print("save success:", save.get("success"), save.get("error", ""))
        chk = (await req(ws, {"type": "lovelace/config", "url_path": "dashboard-tent"}, 3))["result"]["views"][0]["sections"]
        print("section count:", len(chk))
        print("headings:", [first_heading(s) for s in chk])

asyncio.run(main())
