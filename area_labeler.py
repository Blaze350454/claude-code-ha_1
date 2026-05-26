"""One-shot: assign `tent` / `tent_irrigation` areas to grow-tent entities in HA.

Uses the websocket config/entity_registry/update API. Dry-run by default; pass --apply to commit.
"""
import asyncio, json, re, sys, pathlib
import websockets

MCP_JSON = pathlib.Path(__file__).parent / ".cursor" / "mcp.json"
cfg = json.loads(MCP_JSON.read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]
HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

TENT_IRR = "tent_irrigation"
TENT = "tent"


def endswith(*suffixes): return lambda eid: eid.endswith(suffixes)
def oneof(*ids):
    s = set(ids); return lambda eid: eid in s
def regex(pat):
    r = re.compile(pat); return lambda eid: bool(r.match(eid))


RULES = [
    (TENT_IRR, endswith("_irrigation_tent")),
    (TENT_IRR, oneof(
        "switch.reservoir_prime_pump_tent",
        "switch.irrigation_power_strip",
        "sensor.air_pump_current",
        "script.irrigation_advance_to_next_feed",
        "input_boolean.irrigation_enabled",
        "input_boolean.irrigation_kill_automations",
        "input_boolean.irrigation_tent_kill",
        "input_boolean.tent_irrigation_start",
        "input_number.tent_feed_duration",
        "input_number.tent_flush_duration",
        "input_number.air_on_duration_minutes",
        "input_number.stir_on_duration_minutes",
        "input_text.irrigation_status",
        "input_datetime.grow_tent_watering_time",
        "sensor.tent_irrigation_controller_pressure_pre_reg_raw_voltage",
    )),
    (TENT_IRR, oneof("switch.irrigation_controller_tent")),
    (TENT_IRR, regex(r"^[a-z_]+\.tp_link_power_strip_c074")),
    (TENT_IRR, regex(r"^[a-z_]+\.sonoff_10017ff9b7")),
    (TENT_IRR, regex(r"^update\.reservoir_prime_pump_tent")),
    (TENT_IRR, regex(r"^automation\.(fill_feed_reservoir|fill_flush_reservoir|alert_feed_reservoir|alert_flush_reservoir|irrigation_|toggle_irrigation|toggle_kill_irrigation)")),

    (TENT, endswith("_air_conditioner_tent", "_camera_tent")),
    (TENT, oneof(
        "climate.air_conditioner_tent",
        "switch.air_conditioner_tent",
        "switch.frost_protect_air_onditioner_tent",
        "update.firmware_3_air_conditioner_tent",
        "camera.tent",
        "binary_sensor.tent_camera_armed",
        "fan.circulation_fans_tent",
        "humidifier.dehumidifier_tent",
        "sensor.humidifier_reservoir_temperature",
        "switch.grow_tent_one_extra_relay",
        "switch.controller_tent",
        "sensor.current_tent_controller",
        "sensor.power_tent_controller",
        "sensor.voltage_tent_controller",
        "sensor.tent_average_humidity",
        "sensor.tent_average_pressure",
        "sensor.tent_average_temperature",
        "automation.alert_tplink_service_down",
        "automation.safety_flower_night_humidifier_shutoff",
        "automation.safety_flower_night_humidity_high_warning",
        "automation.tent_lights_auto",
        "automation.tent_lights_transition",
        "input_boolean.flower_night_humidifier_block",
        "input_boolean.grow_tent_automation_enabled",
        "input_boolean.grow_tent_vacation_mode",
        "input_datetime.flower_lights_off_time",
        "input_datetime.flower_lights_on_time",
        "input_datetime.grow_tent_lights_on",
        "input_number.grow_tent_light_duration",
        "input_number.grow_tent_target_humidity",
        "input_number.grow_tent_target_temp",
        "input_number.tent_day_temp_target",
        "input_number.tent_night_temp_target",
        "input_select.grow_tent_growth_stage",
        "input_select.growth_stage",
        "input_select.tent_humidity_mode",
    )),
    (TENT, regex(r"^[a-z_]+\.sonoff_10017fee1e")),
    (TENT, regex(r"^sensor\.(canopy|flower)_(temperature|humidity|pressure)_tent$")),
    (TENT, regex(r"^sensor\.(co2_concentration|corrected_co2_voltage|raw_adc_reading)_tent$")),
    (TENT, regex(r"^sensor\.grow_tent_(dli|status|vpd)$")),
    (TENT, regex(r"^sensor\.grow_tent_two_.*_(moisture|volts)$")),
]

SKIP = {
    "sensor.sm_a166w_diastolic_blood_pressure",
    "sensor.sm_a166w_pressure_sensor",
    "sensor.sm_a166w_systolic_blood_pressure",
    "sensor.weather_antigonish_barometric_pressure",
    "switch.opengrowbox_pre_release",
    "update.opengrowbox_update",
}
SKIP_PATTERNS = [re.compile(r"^[a-z_]+\.tp_link_power_strip_53db")]


def target_area_for(eid):
    if eid in SKIP or any(p.match(eid) for p in SKIP_PATTERNS):
        return None
    for area, match in RULES:
        if match(eid):
            return area
    return None


async def ws_call(ws, msg_id, **kwargs):
    await ws.send(json.dumps({"id": msg_id, **kwargs}))
    while True:
        reply = json.loads(await ws.recv())
        if reply.get("id") == msg_id:
            return reply


async def main(apply: bool):
    async with websockets.connect(WS_URL, max_size=None) as ws:
        hello = json.loads(await ws.recv())
        assert hello["type"] == "auth_required", hello
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        auth = json.loads(await ws.recv())
        assert auth["type"] == "auth_ok", auth

        mid = 1
        reg = await ws_call(ws, mid, type="config/entity_registry/list"); mid += 1
        entities = reg["result"]

        plan = []
        already_ok = 0
        matched = set()
        for e in entities:
            eid = e["entity_id"]
            tgt = target_area_for(eid)
            if tgt is None:
                continue
            matched.add(eid)
            cur = e.get("area_id")
            if cur == tgt:
                already_ok += 1
            else:
                plan.append((eid, cur, tgt))

        kw = re.compile(r"(tent|irrigat|pump|valve|solenoid|flow|pressure|reservoir|float|hs300|kp303|tp_link|tplink|grow|sonoff.*fee1e|sonoff.*ff9b7|air_conditioner|controller_tent)", re.I)
        orphans = []
        for e in entities:
            eid = e["entity_id"]
            if eid in matched or eid in SKIP or any(p.match(eid) for p in SKIP_PATTERNS):
                continue
            name = e.get("name") or e.get("original_name") or ""
            if kw.search(eid) or kw.search(name):
                orphans.append((eid, e.get("area_id"), name))

        print(f"=== PLAN: {len(plan)} changes, {already_ok} already correct ===\n")
        for eid, cur, tgt in sorted(plan, key=lambda x: (x[2], x[0])):
            print(f"  {(cur or '(none)'):16s} -> {tgt:16s}  {eid}")

        if orphans:
            print(f"\n=== ORPHANS ({len(orphans)}) — candidates not matched by any rule, PLEASE REVIEW ===")
            for eid, cur, nm in sorted(orphans):
                print(f"  [{cur or '(none)'}]  {eid}   name={nm!r}")

        if not apply:
            print("\nDRY RUN. Re-run with --apply to commit.")
            return

        print(f"\n=== APPLYING {len(plan)} changes ===")
        ok = fail = 0
        for eid, cur, tgt in plan:
            mid += 1
            r = await ws_call(ws, mid, type="config/entity_registry/update", entity_id=eid, area_id=tgt)
            if r.get("success"):
                ok += 1
            else:
                fail += 1
                print(f"  FAIL {eid}: {r}")
        print(f"\nApplied: {ok} ok, {fail} failed")


if __name__ == "__main__":
    asyncio.run(main(apply="--apply" in sys.argv))
