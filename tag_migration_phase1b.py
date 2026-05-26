"""Phase 1b tagging migration - tent climate / lighting / residual-irrigation ancillaries.

What this does, in a single authenticated WebSocket session:
  1. Ensure new phase-1b labels exist (sys_climate/lighting, sub_climate_*, fn_fan/light/climate/
     sensor_humidity/sensor_co2, grow).
  2. Apply per-rule labels to every matched entity. Also adds `grow` to all sys_irrigation
     entities (retroactive phase 1a touch-up so the master grow dashboard works).
  3. Strip the superseded labels from every entity: tent, fans_tent, lights_tent, ac_tent,
     humidifier_tent, air_quality_tent, controller.
  4. Delete those 7 superseded labels from the registry.

Dry-run by default. Pass `--apply` to commit.

Deferred (will show up in UNMATCHED list, untouched):
  - Camera Tent device (camera.tent + *_camera_tent entities)   -> phase 2 (sys_camera/security)
  - switch.blank_2, switch.humidifier_2, switch.grow_tent_one_extra_relay (unknown loads)
  - sensor.grow_tent_two_plant_{1..9}_* and flood_{1..4}_* (reserved/future irrigation hardware)

Invariants per tagging_standard.md (v1):
  - Exactly one sys_, at most one sub_, one+ fn_ (for entities), exactly one sev_.
  - Automations / scripts / helpers: sys_/sub_/sev_ only, no fn_.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib, re
from dataclasses import dataclass
from typing import Callable
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

# Labels to strip from every entity (superseded by the new taxonomy)
OLD_LABELS_TO_STRIP = {
    "tent", "fans_tent", "lights_tent", "ac_tent",
    "humidifier_tent", "air_quality_tent", "controller",
}

# ---------- Label specs: (label_id, name, color, icon) ----------
LABELS_TO_ENSURE = [
    # System
    ("sys_climate",              "sys_climate",              "light-green", "mdi:thermometer-lines"),
    ("sys_lighting",             "sys_lighting",             "yellow",      "mdi:lightbulb-on"),
    # Climate subsystems (system-scoped)
    ("sub_climate_ac",           "sub_climate_ac",           "blue",        "mdi:air-conditioner"),
    ("sub_climate_humidifier",   "sub_climate_humidifier",   "cyan",        "mdi:air-humidifier"),
    ("sub_climate_dehumidifier", "sub_climate_dehumidifier", "light-blue",  "mdi:air-humidifier-off"),
    ("sub_climate_circulation",  "sub_climate_circulation",  "teal",        "mdi:fan"),
    ("sub_climate_exhaust",      "sub_climate_exhaust",      "blue-grey",   "mdi:fan-chevron-up"),
    ("sub_climate_canopy",       "sub_climate_canopy",       "light-green", "mdi:leaf"),
    ("sub_climate_flower",       "sub_climate_flower",       "pink",        "mdi:flower"),
    ("sub_climate_co2",          "sub_climate_co2",          "deep-purple", "mdi:molecule-co2"),
    # Function (new)
    ("fn_fan",              "fn_fan",              "blue-grey",   "mdi:fan"),
    ("fn_light",            "fn_light",            "amber",       "mdi:lightbulb"),
    ("fn_climate",          "fn_climate",          "green",       "mdi:thermostat"),
    ("fn_sensor_humidity",  "fn_sensor_humidity",  "light-blue",  "mdi:water-percent"),
    ("fn_sensor_co2",       "fn_sensor_co2",       "deep-purple", "mdi:molecule-co2"),
    # Cross-cutting
    ("grow",                "grow",                "green",       "mdi:cannabis"),
]


def regex(pat: str) -> Callable[[str], bool]:
    r = re.compile(pat); return lambda eid: bool(r.match(eid))
def oneof(*ids: str) -> Callable[[str], bool]:
    s = set(ids); return lambda eid: eid in s


@dataclass
class Rule:
    match: Callable[[str], bool]
    labels: list[str]
    note: str = ""


# ---------- Rules (first match wins). All grow-related entities also get `grow`. ----------
RULES: list[Rule] = [
    # ============================================================
    # RESIDUAL IRRIGATION ANCILLARIES (missed by phase 1a)
    # ============================================================
    # Tent Controller Sonoff (10017fee1e) powers the ESP32 irrigation controller
    Rule(oneof("switch.controller_tent"),
         ["sys_irrigation","fn_controller","sev_critical"],
         "Sonoff that powers the irrigation ESP32"),
    Rule(oneof("switch.sonoff_10017fee1e_led"),
         ["sys_irrigation","fn_controller","sev_info"]),
    Rule(regex(r"^sensor\.sonoff_10017fee1e_(rssi|energy|connection)$"),
         ["sys_irrigation","fn_power_meter","sev_info"]),
    Rule(regex(r"^sensor\.(current|power|voltage)_tent_controller$"),
         ["sys_irrigation","fn_power_meter","sev_info"]),

    # KP303 "Power Strip Tent" (53db) — phase 1a tagged the s1/s2/s3/s123 switches; mop up ancillaries
    Rule(oneof("binary_sensor.tp_link_power_strip_53db_cloud_connection"),
         ["sys_irrigation","fn_power_meter","sev_warning"]),
    Rule(oneof("button.tp_link_power_strip_53db_restart",
               "switch.tp_link_power_strip_53db_led"),
         ["sys_irrigation","fn_controller","sev_info"]),
    Rule(oneof("sensor.tp_link_power_strip_53db_signal_strength",
               "sensor.tp_link_power_strip_53db_on_since"),
         ["sys_irrigation","fn_power_meter","sev_info"]),

    # Kasa "Irrigation Multi - Plug" outdoor 2-plug
    Rule(oneof("switch.kasa_smart_outdoor_plug_switch_1",
               "switch.kasa_smart_outdoor_plug_switch_2"),
         ["sys_irrigation","fn_controller","sev_warning"],
         "Outdoor irrigation plug outlets; severity flagged for review"),
    Rule(oneof("update.kasa_smart_outdoor_plug_firmware"),
         ["sys_irrigation","sev_info"]),

    # automation.alert_tplink_service_down — monitors HS300 cloud-API service
    Rule(oneof("automation.alert_tplink_service_down"),
         ["sys_irrigation","sev_critical"]),

    # ============================================================
    # CLIMATE — AC
    # ============================================================
    Rule(oneof("climate.air_conditioner_tent"),
         ["sys_climate","sub_climate_ac","fn_climate","sev_critical"]),
    Rule(oneof("switch.air_conditioner_tent",
               "switch.power_air_conditioner_tent"),
         ["sys_climate","sub_climate_ac","fn_controller","sev_critical"]),
    Rule(oneof("fan.fresh_air_air_conditioner_tent"),
         ["sys_climate","sub_climate_ac","fn_fan","sev_warning"]),
    Rule(oneof("number.fan_speed_percent_air_conditioner_tent"),
         ["sys_climate","sub_climate_ac","sev_info"]),
    Rule(regex(r"^select\.airflow_(horizontal|vertical)_air_conditioner_tent$"),
         ["sys_climate","sub_climate_ac","sev_info"]),
    Rule(oneof("sensor.current_energy_consumption_air_conditioner_tent",
               "sensor.realtime_power_air_conditioner_tent",
               "sensor.total_energy_consumption_air_conditioner_tent"),
         ["sys_climate","sub_climate_ac","fn_power_meter","sev_info"]),
    Rule(oneof("sensor.indoor_humidity_air_conditioner_tent"),
         ["sys_climate","sub_climate_ac","fn_sensor_humidity","sev_warning"]),
    Rule(oneof("sensor.indoor_temperature_air_conditioner_tent"),
         ["sys_climate","sub_climate_ac","fn_sensor_temp","sev_warning"]),
    Rule(oneof("sensor.outdoor_temperature_air_conditioner_tent"),
         ["sys_climate","sub_climate_ac","fn_sensor_temp","sev_info"]),
    Rule(oneof("binary_sensor.full_dust_air_conditioner_tent"),
         ["sys_climate","sub_climate_ac","sev_warning"]),
    Rule(regex(r"^switch\.(aux_heating|boost_mode|breezeless|comfort_mode|dehumidifier|eco_mode|"
               r"frost_protect|indirect_wind|natural_wind|prompt_tone|screen_display|"
               r"screen_display_alternate|sleep_mode|smart_eye|swing_horizontal|swing_vertical)"
               r"_air_conditioner_tent$"),
         ["sys_climate","sub_climate_ac","sev_info"]),
    # frost_protect: entity id actually "frost_protect_air_onditioner_tent" (typo in HA)
    Rule(oneof("switch.frost_protect_air_onditioner_tent"),
         ["sys_climate","sub_climate_ac","sev_info"]),
    Rule(regex(r"^update\.firmware_3_air_conditioner_tent$"),
         ["sys_climate","sub_climate_ac","sev_info"]),

    # ============================================================
    # CLIMATE — Dehumidifier
    # ============================================================
    Rule(oneof("humidifier.dehumidifier_tent"),
         ["sys_climate","sub_climate_dehumidifier","fn_climate","sev_critical"]),
    Rule(oneof("switch.power_dehumidifier"),
         ["sys_climate","sub_climate_dehumidifier","fn_controller","sev_critical"]),
    Rule(oneof("switch.anion_dehumidifier","switch.prompt_tone_dehumidifier"),
         ["sys_climate","sub_climate_dehumidifier","sev_info"]),
    Rule(oneof("switch.fan_swing_dehumidifier"),
         ["sys_climate","sub_climate_dehumidifier","fn_fan","sev_info"]),
    Rule(oneof("binary_sensor.tank_full_dehumidifier"),
         ["sys_climate","sub_climate_dehumidifier","fn_sensor_level","sev_warning"]),
    Rule(oneof("sensor.tank_dehumidifier"),
         ["sys_climate","sub_climate_dehumidifier","fn_sensor_level","sev_warning"]),
    Rule(oneof("sensor.current_humidity_dehumidifier"),
         ["sys_climate","sub_climate_dehumidifier","fn_sensor_humidity","sev_warning"]),
    Rule(oneof("sensor.current_temperature_dehumidifier"),
         ["sys_climate","sub_climate_dehumidifier","fn_sensor_temp","sev_info"]),
    Rule(oneof("select.fan_speed_dehumidifier"),
         ["sys_climate","sub_climate_dehumidifier","fn_fan","sev_info"]),
    Rule(oneof("select.water_level_set_dehumidifier"),
         ["sys_climate","sub_climate_dehumidifier","sev_info"]),
    Rule(oneof("lock.child_lock_dehumidifier"),
         ["sys_climate","sub_climate_dehumidifier","sev_info"]),

    # ============================================================
    # CLIMATE — Humidifier
    # ============================================================
    Rule(oneof("switch.humidifier"),
         ["sys_climate","sub_climate_humidifier","fn_controller","sev_critical"]),
    Rule(oneof("update.firmware_2_humidifier","update.humidifier_firmware"),
         ["sys_climate","sub_climate_humidifier","sev_info"]),
    # grow-tent-one ESP32 — humidifier PWM fan + reservoir temp
    Rule(oneof("fan.humidifier_fan_pwm"),
         ["sys_climate","sub_climate_humidifier","fn_fan","sev_warning"]),
    Rule(oneof("sensor.humidifier_fan_rpm"),
         ["sys_climate","sub_climate_humidifier","fn_fan","sev_info"]),
    Rule(oneof("sensor.humidifier_reservoir_temperature"),
         ["sys_climate","sub_climate_humidifier","fn_sensor_temp","sev_info"]),

    # ============================================================
    # CLIMATE — Circulation (interior air movement)
    # ============================================================
    Rule(oneof("fan.circulation_fans_tent"),
         ["sys_climate","sub_climate_circulation","fn_fan","sev_warning"]),
    Rule(oneof("switch.circulation_fans"),
         ["sys_climate","sub_climate_circulation","fn_controller","sev_warning"]),
    Rule(oneof("switch.sonoff_10017fff91_led"),
         ["sys_climate","sub_climate_circulation","fn_controller","sev_info"]),
    Rule(regex(r"^sensor\.sonoff_10017fff91_(rssi|energy|connection)$"),
         ["sys_climate","sub_climate_circulation","fn_power_meter","sev_info"]),
    Rule(regex(r"^sensor\.(current|power|voltage)_circulation_fans$"),
         ["sys_climate","sub_climate_circulation","fn_power_meter","sev_info"]),
    # AC Circulation Fan (Sonoff 10017ff9b7)
    Rule(oneof("fan.ac_circulation_fan"),
         ["sys_climate","sub_climate_circulation","fn_fan","sev_warning"]),
    Rule(oneof("switch.ac_circulation_fan"),
         ["sys_climate","sub_climate_circulation","fn_controller","sev_warning"]),
    Rule(oneof("switch.sonoff_10017ff9b7_led"),
         ["sys_climate","sub_climate_circulation","fn_controller","sev_info"]),
    Rule(regex(r"^sensor\.sonoff_10017ff9b7_(rssi|energy|connection)$"),
         ["sys_climate","sub_climate_circulation","fn_power_meter","sev_info"]),
    Rule(regex(r"^sensor\.(current|power|voltage)_ac_circulation_fan$"),
         ["sys_climate","sub_climate_circulation","fn_power_meter","sev_info"]),

    # ============================================================
    # CLIMATE — Exhaust (duct fan)
    # ============================================================
    Rule(oneof("fan.duct_fan"),
         ["sys_climate","sub_climate_exhaust","fn_fan","sev_warning"]),
    Rule(oneof("switch.duct_fan"),
         ["sys_climate","sub_climate_exhaust","fn_controller","sev_warning"]),
    Rule(oneof("switch.sonoff_1001804756_led"),
         ["sys_climate","sub_climate_exhaust","fn_controller","sev_info"]),
    Rule(regex(r"^sensor\.sonoff_1001804756_(rssi|energy|connection)$"),
         ["sys_climate","sub_climate_exhaust","fn_power_meter","sev_info"]),
    Rule(regex(r"^sensor\.(current|power|voltage)_duct_fan$"),
         ["sys_climate","sub_climate_exhaust","fn_power_meter","sev_info"]),

    # ============================================================
    # CLIMATE — Canopy BME280 sensors (Grow Tent Two ESP32)
    # ============================================================
    Rule(oneof("sensor.canopy_temperature_tent"),
         ["sys_climate","sub_climate_canopy","fn_sensor_temp","sev_warning"]),
    Rule(oneof("sensor.canopy_humidity_tent"),
         ["sys_climate","sub_climate_canopy","fn_sensor_humidity","sev_warning"]),
    Rule(oneof("sensor.canopy_pressure_tent"),
         ["sys_climate","sub_climate_canopy","fn_sensor_pressure","sev_info"]),

    # ============================================================
    # CLIMATE — Flower BME280 sensors
    # ============================================================
    Rule(oneof("sensor.flower_temperature_tent"),
         ["sys_climate","sub_climate_flower","fn_sensor_temp","sev_warning"]),
    Rule(oneof("sensor.flower_humidity_tent"),
         ["sys_climate","sub_climate_flower","fn_sensor_humidity","sev_warning"]),
    Rule(oneof("sensor.flower_pressure_tent"),
         ["sys_climate","sub_climate_flower","fn_sensor_pressure","sev_info"]),

    # ============================================================
    # CLIMATE — CO2
    # ============================================================
    Rule(oneof("sensor.co2_concentration_tent"),
         ["sys_climate","sub_climate_co2","fn_sensor_co2","sev_warning"]),
    Rule(oneof("sensor.corrected_co2_voltage_tent","sensor.raw_adc_reading_tent"),
         ["sys_climate","sub_climate_co2","fn_sensor_co2","sev_info"]),

    # ============================================================
    # CLIMATE — Aggregated / template sensors (no sub_)
    # ============================================================
    Rule(oneof("sensor.tent_average_temperature"),
         ["sys_climate","fn_sensor_temp","sev_warning"]),
    Rule(oneof("sensor.tent_average_humidity"),
         ["sys_climate","fn_sensor_humidity","sev_warning"]),
    Rule(oneof("sensor.tent_average_pressure"),
         ["sys_climate","fn_sensor_pressure","sev_info"]),
    Rule(oneof("sensor.grow_tent_vpd"),
         ["sys_climate","sev_info"]),
    Rule(oneof("sensor.grow_tent_status"),
         ["sys_climate","sev_info"]),

    # ============================================================
    # LIGHTING — HLG
    # ============================================================
    Rule(oneof("light.hlg"),
         ["sys_lighting","fn_light","sev_critical"]),
    Rule(oneof("switch.hlg"),
         ["sys_lighting","fn_controller","sev_critical"]),
    Rule(oneof("switch.sonoff_10017fe92a_led"),
         ["sys_lighting","fn_controller","sev_info"]),
    Rule(regex(r"^sensor\.sonoff_10017fe92a_(rssi|energy|connection)$"),
         ["sys_lighting","fn_power_meter","sev_info"]),
    Rule(regex(r"^sensor\.(current|power|voltage)_hlg$"),
         ["sys_lighting","fn_power_meter","sev_info"]),

    # ============================================================
    # LIGHTING — Chilled
    # ============================================================
    Rule(oneof("light.chilled"),
         ["sys_lighting","fn_light","sev_critical"]),
    Rule(oneof("switch.chilled"),
         ["sys_lighting","fn_controller","sev_critical"]),
    Rule(oneof("switch.sonoff_1001801377_led"),
         ["sys_lighting","fn_controller","sev_info"]),
    Rule(regex(r"^sensor\.sonoff_1001801377_(rssi|energy|connection)$"),
         ["sys_lighting","fn_power_meter","sev_info"]),
    Rule(regex(r"^sensor\.(current|power|voltage)_chilled$"),
         ["sys_lighting","fn_power_meter","sev_info"]),

    # DLI — lighting-scoped derived telemetry
    Rule(oneof("sensor.grow_tent_dli"),
         ["sys_lighting","sev_info"]),

    # ============================================================
    # AUTOMATIONS (climate/lighting)
    # ============================================================
    Rule(oneof("automation.tent_lights_transition","automation.tent_lights_auto"),
         ["sys_lighting","sev_info"]),
    Rule(oneof("automation.humidity_stage_change_defaults"),
         ["sys_climate","sub_climate_humidifier","sev_info"]),
    Rule(oneof("automation.safety_flower_night_humidifier_shutoff"),
         ["sys_climate","sub_climate_humidifier","sev_critical"]),
    Rule(oneof("automation.safety_flower_night_humidity_high_warning"),
         ["sys_climate","sub_climate_humidifier","sev_warning"]),

    # ============================================================
    # INPUT HELPERS
    # ============================================================
    # Lighting
    Rule(oneof("input_datetime.flower_lights_on_time","input_datetime.flower_lights_off_time",
               "input_datetime.grow_tent_lights_on",
               "input_number.grow_tent_light_duration"),
         ["sys_lighting","sev_info"]),
    # Climate — temp
    Rule(oneof("input_number.grow_tent_target_temp",
               "input_number.tent_day_temp_target","input_number.tent_night_temp_target"),
         ["sys_climate","sev_info"]),
    # Climate — humidity
    Rule(oneof("input_number.grow_tent_target_humidity",
               "input_number.humidity_night_target",
               "input_boolean.flower_night_humidifier_block",
               "input_select.tent_humidity_mode"),
         ["sys_climate","sub_climate_humidifier","sev_info"]),
    # Climate — growth stage / master toggles
    Rule(oneof("input_select.growth_stage","input_select.grow_tent_growth_stage"),
         ["sys_climate","sev_info"]),
    Rule(oneof("input_boolean.grow_tent_automation_enabled"),
         ["sys_climate","sev_critical"],
         "master grow automations kill switch"),
    Rule(oneof("input_boolean.grow_tent_vacation_mode"),
         ["sys_climate","sev_warning"]),
]


def labels_for(eid: str) -> list[str] | None:
    for r in RULES:
        if r.match(eid):
            return list(r.labels)
    return None


# ---------- WebSocket helpers ----------
async def ws_call(ws, mid, **kw):
    await ws.send(json.dumps({"id": mid, **kw}))
    while True:
        r = json.loads(await ws.recv())
        if r.get("id") == mid:
            return r


async def main(apply: bool):
    async with websockets.connect(WS_URL, max_size=None) as ws:
        assert json.loads(await ws.recv())["type"] == "auth_required"
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        assert json.loads(await ws.recv())["type"] == "auth_ok"

        mid = 0
        def nid(): nonlocal mid; mid += 1; return mid

        entities = (await ws_call(ws, nid(), type="config/entity_registry/list"))["result"]
        labels   = (await ws_call(ws, nid(), type="config/label_registry/list"))["result"]
        areas    = (await ws_call(ws, nid(), type="config/area_registry/list"))["result"]
        existing_label_ids = {l["label_id"] for l in labels}

        print(f"Loaded: {len(entities)} entities, {len(labels)} labels, {len(areas)} areas")

        # === 1. Plan label creation ===
        to_create = [L for L in LABELS_TO_ENSURE if L[0] not in existing_label_ids]
        print(f"\n=== LABELS TO CREATE: {len(to_create)} ===")
        for lid, nm, col, ic in to_create:
            print(f"  + {lid:28s}  color={col}  icon={ic}")

        # === 2. Plan entity label changes ===
        entity_plan = []  # (eid, current, new)
        unmatched_tent = []  # entities in tent area without rule or existing sys_*
        for e in entities:
            eid = e["entity_id"]
            cur_labels = list(e.get("labels") or [])
            new_labels = list(cur_labels)

            # a) Strip superseded labels
            new_labels = [L for L in new_labels if L not in OLD_LABELS_TO_STRIP]

            # b) Apply rule-derived labels (phase 1b)
            rule = labels_for(eid)
            if rule:
                for L in rule:
                    if L not in new_labels:
                        new_labels.append(L)
                # c) cross-cutting `grow` for every rule-matched grow entity
                if "grow" not in new_labels:
                    new_labels.append("grow")

            # d) Retroactive: any entity already tagged sys_irrigation gets `grow`
            if "sys_irrigation" in new_labels and "grow" not in new_labels:
                new_labels.append("grow")

            if sorted(new_labels) != sorted(cur_labels):
                entity_plan.append((eid, cur_labels, new_labels))

            # Track tent-area entities with no sys_ (post-strip view, ignoring area)
            ent_area = e.get("area_id")
            if ent_area == "tent" and not rule:
                has_sys = any(L.startswith("sys_") for L in new_labels)
                if not has_sys:
                    unmatched_tent.append((eid, cur_labels))

        print(f"\n=== ENTITY CHANGES: {len(entity_plan)} ===")
        for eid, cl, nl in sorted(entity_plan):
            added = [L for L in nl if L not in cl]
            removed = [L for L in cl if L not in nl]
            parts = []
            if added: parts.append(f"+{added}")
            if removed: parts.append(f"-{removed}")
            print(f"  {eid:62s}  {' '.join(parts)}")

        if unmatched_tent:
            print(f"\n=== UNMATCHED tent-area entities (no rule, no sys_ label) — DEFERRED: {len(unmatched_tent)} ===")
            for eid, cl in sorted(unmatched_tent):
                print(f"  {eid:62s}  current_labels={cl}")

        # === 3. Plan label deletions ===
        to_delete = [L for L in OLD_LABELS_TO_STRIP if L in existing_label_ids]
        print(f"\n=== LABELS TO DELETE (post-migration): {len(to_delete)} ===")
        for L in to_delete:
            print(f"  - {L}")

        if not apply:
            print("\n=== DRY RUN - nothing was modified. Re-run with --apply to commit. ===")
            return

        # ============ APPLY ============
        print("\n\n====== APPLYING CHANGES ======\n")

        for lid, nm, col, ic in to_create:
            r = await ws_call(ws, nid(), type="config/label_registry/create",
                              name=nm, color=col, icon=ic)
            print(f"  create label {lid}: {'OK' if r.get('success') else r}")

        ok = fail = 0
        for eid, cl, nl in entity_plan:
            r = await ws_call(ws, nid(), type="config/entity_registry/update",
                              entity_id=eid, labels=nl)
            if r.get("success"):
                ok += 1
            else:
                fail += 1
                print(f"  FAIL {eid}: {r}")
        print(f"  entity updates: {ok} OK, {fail} FAIL")

        for L in to_delete:
            r = await ws_call(ws, nid(), type="config/label_registry/delete", label_id=L)
            print(f"  delete label '{L}': {'OK' if r.get('success') else r}")

        print("\n=== APPLY COMPLETE ===")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Commit changes (default: dry run)")
    args = ap.parse_args()
    asyncio.run(main(args.apply))
