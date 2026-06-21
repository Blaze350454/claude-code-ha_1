import asyncio, json, re, pathlib, datetime, websockets

env = dict(re.findall(r'^(\w+)=(.*)$', pathlib.Path('.env').read_text(), re.M))
TOKEN = env['HA_TOKEN']
URL = "ws://192.168.2.151:8123/api/websocket"

md = r"""{% macro rel(ts, future=false) -%}
{%- set t = state_attr(ts, 'timestamp') -%}
{%- if t is none -%}—
{%- else -%}
{%- set d = t - now().timestamp() -%}
{%- set a = (d | abs) | int -%}
{%- if d >= 0 -%}in {{ (a//3600) }}h {{ '%02d' | format((a%3600)//60) }}m
{%- elif future -%}overdue
{%- else -%}{{ (a//3600) }}h {{ '%02d' | format((a%3600)//60) }}m ago
{%- endif -%}
{%- endif -%}
{%- endmacro -%}
{%- set on = states('input_datetime.veg_lights_on_time') -%}
{%- set off = states('input_datetime.veg_lights_off_time') -%}
{%- set feeds = states('input_number.feeds_per_day_2') | int(0) -%}
{%- set on_t = (on[0:2]|int)*60 + (on[3:5]|int) -%}
{%- set off_t = (off[0:2]|int)*60 + (off[3:5]|int) -%}
{%- set dur = (off_t - on_t) if off_t > on_t else (1440 - on_t + off_t) -%}
{%- set iv = (((dur-35)/(feeds-1))|round(0)|int) if feeds > 1 else dur -%}
{%- set ns = namespace(t=[]) -%}
{%- for n in range(1, feeds+1) -%}
  {%- set tot = on_t + 5 + (n-1)*iv -%}
  {%- set ns.t = ns.t + ['%02d:%02d' | format((tot//60)%24, tot%60)] -%}
{%- endfor -%}
### \U0001F331 Irrigation

**Status:** {{ states('input_text.tent_irrigation_status') }}

**Last feed:** {{ rel('input_datetime.last_feed_time') }} ({{ state_attr('input_datetime.last_feed_time','timestamp') | timestamp_custom('%-I:%M %p', true, '—') }})

**Next feed:** {{ rel('input_datetime.next_feed_time', true) }} ({{ state_attr('input_datetime.next_feed_time','timestamp') | timestamp_custom('%-I:%M %p', true, '—') }}) — feed {{ states('input_number.current_feed_number')|int }} of {{ feeds }}

**Today's feeds:** {{ ns.t | join(', ') }}

**Feed** {{ states('input_number.feed_duration_minutes')|int }}m · **Clear** {{ states('input_number.line_clear_minutes')|float }}m · **Lights** {{ on[0:5] }}–{{ off[0:5] }} · **Flush** every {{ states('input_number.flush_day_interval')|int }}d
"""

def level_gauge(ent, name, severity=None):
    # Small semicircular gauge; fill color follows level. Default >=75 green, >=50 yellow, else red.
    # grid_options columns:4 = one third of the section width, so all three sit in a single row.
    return {"type": "gauge", "entity": ent, "name": name, "min": 0, "max": 100,
            "severity": severity or {"green": 75, "yellow": 50, "red": 0},
            "grid_options": {"columns": 4}}

def float_tile(ent, name):
    style = ("ha-card {\n  --tile-color: {% if is_state('" + ent + "','on') %} #43a047 "
             "{% else %} #757575 {% endif %};\n}")
    return {"type": "tile", "entity": ent, "name": name, "card_mod": {"style": style}}

def gauge(ent, name, mx, sev):
    # columns:4 = one third width, matching the reservoir level gauges (three per row).
    # No needle: the fill color follows the value's severity band.
    return {"type": "gauge", "entity": ent, "name": name, "min": 0, "max": mx,
            "severity": sev, "grid_options": {"columns": 4}}

stats = {"type": "grid", "column_span": 1, "cards": [
    {"type": "heading", "heading": "Irrigation"},
    {"show_name": True, "show_icon": True, "type": "button", "name": "Feed Now", "icon": "mdi:watering-can", "color": "green",
     "tap_action": {"action": "perform-action", "perform_action": "script.run_feed_cycle",
       "confirmation": {"text": "Run a manual feed cycle now? Standard pump timing (~8 min); if it's the last feed of the day it also runs the line-clear flush."}}},
    {"show_name": True, "show_icon": True, "show_state": False, "type": "button", "name": "STOP ALL",
     "icon": "mdi:hand-back-right", "entity": "input_boolean.irrigation_tent_kill",
     "tap_action": {"action": "toggle",
       "confirmation": {"text": "Toggle STOP ALL? Engaging halts ALL tent irrigation immediately; disengaging resumes automation."}},
     "card_mod": {"style":
       "ha-card {\n"
       "  color: #ffffff;\n"
       "  {% if is_state('input_boolean.irrigation_tent_kill','on') %}\n"
       "  background: #b71c1c; border: 2px solid #ff5252;\n"
       "  {% else %}\n"
       "  background: #1b5e20; border: 1px solid #66bb6a;\n"
       "  {% endif %}\n"
       "}\n"
       "ha-state-icon, ha-icon {\n"
       "  {% if is_state('input_boolean.irrigation_tent_kill','on') %}\n"
       "  animation: kill-pulse 1s ease-in-out infinite;\n"
       "  {% else %}\n"
       "  color: #d32f2f !important; --mdc-icon-color: #d32f2f !important;\n"
       "  {% endif %}\n"
       "}\n"
       "@keyframes kill-pulse {\n"
       "  0%, 100% { color: #ff1744; }\n"
       "  50% { color: #000000; }\n"
       "}\n"}},
    {"type": "markdown", "card_mod": {"style": {"ha-markdown$": "h3 { text-align:center; margin-top:0; }\n"}}, "content": md},
    {"type": "heading", "heading": "Reservoirs", "heading_style": "subtitle"},
    level_gauge("sensor.feed_level_irrigation_tent", "Feed"),
    level_gauge("sensor.flush_level_irrigation_tent", "Flush"),
    level_gauge("sensor.table_drain_level_irrigation_tent", "Table Drain", {"green": 0, "red": 100}),
    {"type": "heading", "heading": "Pressure & flow (last feed)", "heading_style": "subtitle"},
    gauge("sensor.last_feed_flow", "Feed Flow", 5, {"green": 0.5, "yellow": 0.2, "red": 0}),
    gauge("sensor.last_feed_pressure_post", "Post-Reg", 30, {"green": 10, "yellow": 5, "red": 0}),
    gauge("sensor.last_feed_pressure_pre", "Pre-Reg", 60, {"green": 20, "yellow": 10, "red": 0}),
]}

def settings_section(title, entities):
    # Each settings group is its own grid section: a heading card + one entities card.
    return {"type": "grid", "column_span": 1, "cards": [
        {"type": "heading", "heading": title},
        {"type": "entities", "entities": entities},
    ]}

settings_sections = [
    settings_section("Stage & Light Schedule", [
        {"entity": "input_select.grow_tent_growth_stage", "name": "Growth stage"},
        {"entity": "input_datetime.veg_lights_on_time", "name": "Veg lights on"},
        {"entity": "input_datetime.veg_lights_off_time", "name": "Veg lights off"},
        {"entity": "input_datetime.flower_lights_on_time", "name": "Flower lights on"},
        {"entity": "input_datetime.flower_lights_off_time", "name": "Flower lights off"},
        {"entity": "input_datetime.daily_setup_time", "name": "Daily setup time"},
    ]),
    settings_section("Feed & Flush", [
        {"entity": "input_boolean.tent_irrigation_enabled", "name": "Automation enabled"},
        {"entity": "input_number.feeds_per_day_2", "name": "Feeds per day"},
        {"entity": "input_number.feed_duration_minutes", "name": "Feed duration (min)"},
        {"entity": "input_number.line_clear_minutes", "name": "Line clear (min)"},
        {"entity": "input_number.flush_duration_minutes", "name": "Flush duration (min)"},
        {"entity": "input_number.flush_day_interval", "name": "Flush every (days)"},
        {"entity": "input_number.air_stir_lead_minutes", "name": "Pre-feed air/stir lead (min)"},
    ]),
    settings_section("Maintenance & Timeouts", [
        {"entity": "input_number.maintenance_interval_minutes", "name": "Maintenance interval (min)"},
        {"entity": "input_number.maintenance_stir_minutes", "name": "Maintenance stir (min)"},
        {"entity": "input_number.maintenance_air_minutes", "name": "Maintenance air (min)"},
        {"entity": "input_number.air_on_duration_minutes", "name": "Air on duration (min)"},
        {"entity": "input_number.stir_on_duration_minutes", "name": "Stir on duration (min)"},
        {"entity": "input_number.feed_fill_timeout_seconds", "name": "Feed fill timeout (s)"},
        {"entity": "input_number.flush_fill_timeout_seconds", "name": "Flush fill timeout (s)"},
    ]),
    settings_section("Night Pulses", [
        {"entity": "input_number.night_pulse_air_minutes", "name": "Air (min)"},
        {"entity": "input_number.night_pulse_stir_pre_minutes", "name": "Stir pre (min)"},
        {"entity": "input_number.night_pulse_stir_post_minutes", "name": "Stir post (min)"},
        {"entity": "input_datetime.night_pulse_veg_1", "name": "Veg pulse 1"},
        {"entity": "input_datetime.night_pulse_veg_2", "name": "Veg pulse 2"},
        {"entity": "input_datetime.night_pulse_flower_1", "name": "Flower pulse 1"},
        {"entity": "input_datetime.night_pulse_flower_2", "name": "Flower pulse 2"},
        {"entity": "input_datetime.night_pulse_flower_3", "name": "Flower pulse 3"},
        {"entity": "input_datetime.night_pulse_flower_4", "name": "Flower pulse 4"},
        {"entity": "input_datetime.night_pulse_flower_5", "name": "Flower pulse 5"},
    ]),
]

# Headings of the sections this script owns and rebuilds every run. Every other section on
# the dashboard is preserved untouched. "Irrigation Settings" is the legacy single settings
# section we split apart — listed so the migration run drops it instead of orphaning it.
MANAGED_HEADINGS = {
    "Irrigation", "Irrigation Settings",
    "Stage & Light Schedule", "Feed & Flush",
    "Maintenance & Timeouts", "Night Pulses",
}

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
        # Rebuild every managed section; keep all other (manually-built) sections as-is.
        managed = [stats] + settings_sections
        manual = [s for s in secs if first_heading(s) not in MANAGED_HEADINGS]
        cfg["views"][0]["sections"] = managed + manual
        save = await req(ws, {"type": "lovelace/config/save", "url_path": "dashboard-tent", "config": cfg}, 2)
        print("save success:", save.get("success"), save.get("error", ""))
        chk = (await req(ws, {"type": "lovelace/config", "url_path": "dashboard-tent"}, 3))["result"]["views"][0]["sections"]
        print("section count:", len(chk))
        print("sec0:", chk[0]["cards"][0].get("heading"), "cards:", len(chk[0]["cards"]))
        print("sec1:", chk[1]["cards"][0].get("heading"), "cards:", len(chk[1]["cards"]))

asyncio.run(main())
