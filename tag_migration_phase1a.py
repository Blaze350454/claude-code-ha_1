"""Phase 1a tagging migration — irrigation subsystem (Tent garden).

What this does, in a single authenticated WebSocket session:
  1. Ensure the new phase-1a labels exist (creates missing ones).
  2. Move every entity+device currently in area `tent_irrigation` -> area `tent`.
  3. Compute new label set per entity (existing_labels - {irrigation_tent}) | per-rule new labels.
     Write updated labels (and area) via config/entity_registry/update.
  4. Delete the `tent_irrigation` area (after reassignments).
  5. Delete the `irrigation_tent` label (after removals).

Dry-run by default. Pass `--apply` to commit.

Invariants per tagging_standard.md (v1):
  - Every matched entity gets exactly one sys_, at most one sub_, one-or-more fn_, exactly one sev_.
  - Automations/scripts/helpers get sys_/sub_/sev_ (no fn_).
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib, re, sys
from dataclasses import dataclass, field
from typing import Callable
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

OLD_AREA = "tent_irrigation"
NEW_AREA = "tent"
OLD_LABEL = "irrigation_tent"

# ---------- Label specs: (label_id, name, color, icon) ----------
LABELS_TO_ENSURE = [
    # System
    ("sys_irrigation",            "sys_irrigation",            "light-blue", "mdi:sprinkler"),
    # Subsystems (irrigation-scoped)
    ("sub_irrigation_feed_loop",  "sub_irrigation_feed_loop",  "green",      "mdi:watering-can"),
    ("sub_irrigation_flush_loop", "sub_irrigation_flush_loop", "cyan",       "mdi:water-sync"),
    ("sub_irrigation_drain_loop", "sub_irrigation_drain_loop", "teal",       "mdi:pipe-disconnected"),
    ("sub_irrigation_reservoir",  "sub_irrigation_reservoir",  "blue",       "mdi:cup-water"),
    # Function
    ("fn_pump",            "fn_pump",            "indigo",     "mdi:pump"),
    ("fn_valve",           "fn_valve",           "deep-purple","mdi:valve"),
    ("fn_controller",      "fn_controller",      "purple",     "mdi:chip"),
    ("fn_power_meter",     "fn_power_meter",     "orange",     "mdi:flash"),
    ("fn_sensor_level",    "fn_sensor_level",    "light-blue", "mdi:waves-arrow-up"),
    ("fn_sensor_pressure", "fn_sensor_pressure", "red",        "mdi:gauge"),
    ("fn_sensor_flow",     "fn_sensor_flow",     "teal",       "mdi:waves-arrow-right"),
    ("fn_sensor_temp",     "fn_sensor_temp",     "yellow",     "mdi:thermometer"),
    # Severity
    ("sev_critical", "sev_critical", "red",        "mdi:alert-octagon"),
    ("sev_warning",  "sev_warning",  "amber",      "mdi:alert"),
    ("sev_info",     "sev_info",     "light-grey", "mdi:information-outline"),
]

# ---------- Mapping helpers ----------
def regex(pat: str) -> Callable[[str], bool]:
    r = re.compile(pat); return lambda eid: bool(r.match(eid))
def oneof(*ids: str) -> Callable[[str], bool]:
    s = set(ids); return lambda eid: eid in s

@dataclass
class Rule:
    match: Callable[[str], bool]
    labels: list[str]           # sys_ + sub_ (optional) + fn_ (zero or more) + sev_
    note: str = ""

# ---------- Rules (first match wins) ----------
# Severity assignments per plan §Tent Garden Entity -> Label Mapping.
RULES: list[Rule] = [
    # --- Pumps (feed loop) ---
    Rule(oneof("switch.air_pump_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_pump","sev_critical"],
         "air pump: critical for root O2"),
    Rule(oneof("switch.feed_pump_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_pump","sev_critical"],
         "feed pump: waters plants"),
    Rule(oneof("switch.feed_stir_pump_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_pump","sev_warning"],
         "feed stir pump: mixes nutes (non-critical)"),
    # --- Pumps (flush loop) ---
    Rule(oneof("switch.flush_pump_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_flush_loop","fn_pump","sev_critical"]),
    Rule(oneof("switch.flush_stir_pump_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_flush_loop","fn_pump","sev_warning"]),
    # --- Pumps (drain + reservoir) ---
    Rule(oneof("switch.table_drain_pump_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_drain_loop","fn_pump","sev_critical"]),
    Rule(oneof("switch.reservoir_prime_pump_tent"),
         ["sys_irrigation","sub_irrigation_reservoir","fn_pump","sev_warning"]),
    # --- Valves ---
    Rule(oneof("valve.feed_valve_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_valve","sev_critical"]),
    Rule(oneof("valve.feed_fill_valve_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_valve","sev_warning"]),
    Rule(oneof("valve.flush_valve_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_flush_loop","fn_valve","sev_critical"]),
    Rule(oneof("valve.flush_fill_valve_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_flush_loop","fn_valve","sev_warning"]),
    Rule(oneof("valve.flush_drain_valve_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_drain_loop","fn_valve","sev_warning"]),
    # --- Controllers ---
    Rule(oneof("switch.irrigation_controller_tent"),
         ["sys_irrigation","fn_controller","sev_critical"],
         "ESP32 irrigation controller"),
    Rule(oneof("switch.irrigation_power_strip","switch.s1","switch.s2","switch.s3","switch.s123"),
         ["sys_irrigation","fn_controller","sev_critical"],
         "KP303/HS300 power strip outlets driving irrigation"),
    # --- Sensors: feed loop ---
    Rule(oneof("sensor.feed_level_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_sensor_level","sev_warning"]),
    Rule(oneof("sensor.feed_temperature_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_sensor_temp","sev_info"]),
    Rule(oneof("sensor.flow_rate_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_sensor_flow","sev_warning"]),
    Rule(oneof("sensor.flow_total_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_sensor_flow","sev_info"]),
    Rule(oneof("sensor.pressure_post_regulator_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_sensor_pressure","sev_critical"]),
    Rule(oneof("sensor.tent_irrigation_controller_pressure_pre_reg_raw_voltage"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_sensor_pressure","sev_info"]),
    Rule(oneof("sensor.air_pump_current"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_power_meter","sev_info"]),
    # --- Sensors: flush loop ---
    Rule(oneof("sensor.flush_level_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_flush_loop","fn_sensor_level","sev_warning"]),
    Rule(oneof("sensor.flush_temperature_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_flush_loop","fn_sensor_temp","sev_info"]),
    # --- Sensors: drain loop ---
    Rule(oneof("sensor.table_drain_level_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_drain_loop","fn_sensor_level","sev_warning"]),
    # --- Binary sensors (feed tank discrete levels) ---
    Rule(oneof("binary_sensor.feed_empty_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_sensor_level","sev_critical"]),
    Rule(regex(r"^binary_sensor\.feed_(half|three_quarter|full)_irrigation_tent$"),
         ["sys_irrigation","sub_irrigation_feed_loop","fn_sensor_level","sev_info"]),
    # --- Binary sensors (flush tank discrete levels) ---
    Rule(oneof("binary_sensor.flush_empty_irrigation_tent"),
         ["sys_irrigation","sub_irrigation_flush_loop","fn_sensor_level","sev_critical"]),
    Rule(regex(r"^binary_sensor\.flush_(half|full)_irrigation_tent$"),
         ["sys_irrigation","sub_irrigation_flush_loop","fn_sensor_level","sev_info"]),
    # --- Binary sensors (table drain) ---
    Rule(oneof("binary_sensor.table_drain_empty"),
         ["sys_irrigation","sub_irrigation_drain_loop","fn_sensor_level","sev_warning"]),
    Rule(oneof("binary_sensor.table_drain_full"),
         ["sys_irrigation","sub_irrigation_drain_loop","fn_sensor_level","sev_critical"]),

    # --- Power telemetry: HS300 (tp_link_power_strip_c074) — all plug-level and strip-level sensors ---
    Rule(regex(r"^sensor\.tp_link_power_strip_c074(_plug_\d+)?_(current|voltage|current_consumption|this_month_s_consumption|today_s_consumption|total_consumption)$"),
         ["sys_irrigation","fn_power_meter","sev_info"]),
    Rule(regex(r"^sensor\.tp_link_power_strip_c074(_plug_\d+)?_(on_since|signal_strength)$"),
         ["sys_irrigation","fn_power_meter","sev_info"]),
    Rule(oneof("binary_sensor.tp_link_power_strip_c074_cloud_connection"),
         ["sys_irrigation","fn_power_meter","sev_warning"]),
    Rule(oneof("switch.tp_link_power_strip_c074_led", "button.tp_link_power_strip_c074_restart"),
         ["sys_irrigation","fn_controller","sev_info"]),
    # --- Power telemetry: Sonoff 10017ff9b7 ---
    # DEFERRED: this plug's device is named "AC Circulation Fan" (area=tent), but its
    # entities are currently filed under tent_irrigation area. Ambiguous. Phase 1b will
    # sort it out once we know whether the plug drives irrigation or climate.

    # --- Update entities / firmware ---
    Rule(regex(r"^update\.reservoir_prime_pump_tent_firmware"),
         ["sys_irrigation","sub_irrigation_reservoir","sev_info"]),

    # --- Automations (irrigation; no fn_, no sub_ unless loop-specific) ---
    # Safety / watchdog / alerts -> critical
    Rule(oneof("automation.irrigation_watchdog",
               "automation.irrigation_startup_recovery",
               "automation.irrigation_maintenance_cycle"),
         ["sys_irrigation","sev_critical"]),
    Rule(oneof("automation.irrigation_block_feed_when_reservoir_dry",
               "automation.alert_feed_reservoir_dry","automation.alert_feed_reservoir_dry_repeat"),
         ["sys_irrigation","sub_irrigation_feed_loop","sev_critical"]),
    Rule(oneof("automation.irrigation_block_flush_when_reservoir_dry",
               "automation.alert_flush_reservoir_dry","automation.alert_flush_reservoir_dry_repeat"),
         ["sys_irrigation","sub_irrigation_flush_loop","sev_critical"]),
    Rule(oneof("automation.irrigation_block_table_drain_pump_when_dry",
               "automation.irrigation_table_drain_pump"),
         ["sys_irrigation","sub_irrigation_drain_loop","sev_critical"]),
    Rule(oneof("automation.fill_feed_reservoir"),
         ["sys_irrigation","sub_irrigation_feed_loop","sev_warning"]),
    Rule(oneof("automation.fill_flush_reservoir"),
         ["sys_irrigation","sub_irrigation_flush_loop","sev_warning"]),
    Rule(oneof("automation.irrigation_feed_trigger"),
         ["sys_irrigation","sub_irrigation_feed_loop","sev_critical"]),
    Rule(oneof("automation.irrigation_daily_setup_at_lights_on",
               "automation.irrigation_lights_off_cleanup",
               "automation.irrigation_night_cycle_start","automation.irrigation_night_cycle_stop",
               "automation.irrigation_pre_feed_air_stir_start","automation.irrigation_pre_feed_air_stir_stop"),
         ["sys_irrigation","sev_info"]),
    Rule(oneof("automation.toggle_irrigation_tent_all_off",
               "automation.toggle_kill_irrigation_automations"),
         ["sys_irrigation","sev_critical"], "emergency kill toggles"),

    # --- Scripts ---
    Rule(oneof("script.run_feed_cycle"),
         ["sys_irrigation","sub_irrigation_feed_loop","sev_info"]),
    Rule(oneof("script.run_normal_flush","script.run_day3_flush"),
         ["sys_irrigation","sub_irrigation_flush_loop","sev_info"]),
    Rule(oneof("script.run_alternating","script.stop_alternating",
               "script.irrigation_advance_to_next_feed"),
         ["sys_irrigation","sev_info"]),

    # --- Input helpers ---
    Rule(oneof("input_boolean.irrigation_enabled","input_boolean.irrigation_kill_automations",
               "input_boolean.irrigation_tent_kill","input_boolean.tent_irrigation_start"),
         ["sys_irrigation","sev_critical"], "kill/enable toggles"),
    Rule(oneof("input_number.tent_feed_duration","input_number.air_on_duration_minutes",
               "input_number.stir_on_duration_minutes"),
         ["sys_irrigation","sub_irrigation_feed_loop","sev_info"]),
    Rule(oneof("input_number.tent_flush_duration"),
         ["sys_irrigation","sub_irrigation_flush_loop","sev_info"]),
    Rule(oneof("input_datetime.grow_tent_watering_time"),
         ["sys_irrigation","sev_info"]),
    Rule(oneof("input_text.irrigation_status"),
         ["sys_irrigation","sev_info"]),
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

        # === 1. Load current state ===
        entities = (await ws_call(ws, nid(), type="config/entity_registry/list"))["result"]
        devices  = (await ws_call(ws, nid(), type="config/device_registry/list"))["result"]
        areas    = (await ws_call(ws, nid(), type="config/area_registry/list"))["result"]
        labels   = (await ws_call(ws, nid(), type="config/label_registry/list"))["result"]
        existing_label_ids = {l["label_id"] for l in labels}
        existing_area_ids  = {a["area_id"] for a in areas}

        print(f"Loaded: {len(entities)} entities, {len(devices)} devices, {len(areas)} areas, {len(labels)} labels")

        # === 2. Plan label creation ===
        to_create = [L for L in LABELS_TO_ENSURE if L[0] not in existing_label_ids]
        print(f"\n=== LABELS TO CREATE: {len(to_create)} ===")
        for lid, nm, col, ic in to_create:
            print(f"  + {lid:28s}  name={nm!r}  color={col}  icon={ic}")

        # === 3. Plan device area migration ===
        # Move any device where: (a) its area_id is OLD_AREA, OR
        # (b) at least one of its entities is matched by our rules AND the device
        #     currently lacks an area. Avoids disturbing devices already correctly placed elsewhere.
        matched_device_ids = {e["device_id"] for e in entities
                              if e.get("device_id") and labels_for(e["entity_id"])}
        dev_moves = []
        for d in devices:
            did = d["id"]
            cur = d.get("area_id")
            if cur == OLD_AREA:
                dev_moves.append((did, d.get("name_by_user") or d.get("name") or "(unnamed)", cur))
            elif did in matched_device_ids and not cur:
                dev_moves.append((did, d.get("name_by_user") or d.get("name") or "(unnamed)", cur))
        print(f"\n=== DEVICES: move -> area '{NEW_AREA}' ({len(dev_moves)}) ===")
        for did, nm, cur in dev_moves:
            print(f"  ~ device {did[:10]}..  area={cur or '(none)'} -> {NEW_AREA}   name={nm!r}")

        # === 4. Plan entity changes ===
        entity_plan = []    # list of (eid, current_area, new_area, current_labels, new_labels, matched_by_rule)
        unmatched_in_old_area = []
        for e in entities:
            eid = e["entity_id"]
            cur_area = e.get("area_id")
            cur_labels = list(e.get("labels") or [])
            in_old_area = cur_area == OLD_AREA

            desired_labels_from_rule = labels_for(eid)
            # Start with current labels, strip OLD_LABEL if present
            new_labels = [L for L in cur_labels if L != OLD_LABEL]
            # Union with rule-derived labels
            matched = desired_labels_from_rule is not None
            if matched:
                for L in desired_labels_from_rule:
                    if L not in new_labels:
                        new_labels.append(L)

            # Area: if in OLD_AREA, move to NEW_AREA.
            # If rule-matched and has no area at all, also set NEW_AREA.
            if in_old_area:
                new_area = NEW_AREA
            elif matched and not cur_area:
                new_area = NEW_AREA
            else:
                new_area = cur_area

            labels_changed = sorted(new_labels) != sorted(cur_labels)
            area_changed = new_area != cur_area

            if labels_changed or area_changed:
                entity_plan.append((eid, cur_area, new_area, cur_labels, new_labels, matched))
            if in_old_area and not matched:
                unmatched_in_old_area.append(eid)

        changed_labels = sum(1 for p in entity_plan if sorted(p[3]) != sorted(p[4]))
        changed_area   = sum(1 for p in entity_plan if p[1] != p[2])

        print(f"\n=== ENTITY CHANGES: {len(entity_plan)} total "
              f"(labels: {changed_labels}, area: {changed_area}) ===")
        for eid, ca, na, cl, nl, matched in sorted(entity_plan):
            parts = []
            if ca != na:
                parts.append(f"area {ca or '(none)'} -> {na or '(none)'}")
            if sorted(cl) != sorted(nl):
                added   = [L for L in nl if L not in cl]
                removed = [L for L in cl if L not in nl]
                if added:   parts.append(f"+labels={added}")
                if removed: parts.append(f"-labels={removed}")
            tag = "" if matched else "  [NO RULE — area-only move]"
            print(f"  {eid:60s}  {' | '.join(parts)}{tag}")

        if unmatched_in_old_area:
            print(f"\n=== UNMATCHED in '{OLD_AREA}' (area moves only, no labels applied): {len(unmatched_in_old_area)} ===")
            for eid in sorted(unmatched_in_old_area):
                print(f"  {eid}")

        # === 5. Plan area deletion ===
        print(f"\n=== AREA TO DELETE: '{OLD_AREA}' ({'exists' if OLD_AREA in existing_area_ids else 'NOT FOUND'}) ===")

        # === 6. Plan label deletion ===
        print(f"\n=== LABEL TO DELETE: '{OLD_LABEL}' ({'exists' if OLD_LABEL in existing_label_ids else 'NOT FOUND'}) ===")

        if not apply:
            print("\n=== DRY RUN — nothing was modified. Re-run with --apply to commit. ===")
            return

        # ============ APPLY ============
        print("\n\n====== APPLYING CHANGES ======\n")

        # Create labels (label_id auto-derived from name by HA)
        for lid, nm, col, ic in to_create:
            r = await ws_call(ws, nid(), type="config/label_registry/create",
                              name=nm, color=col, icon=ic)
            print(f"  create label {lid}: {'OK' if r.get('success') else r}")

        # Move devices
        for did, nm, _cur in dev_moves:
            r = await ws_call(ws, nid(), type="config/device_registry/update",
                              device_id=did, area_id=NEW_AREA)
            print(f"  move device {did[:10]}..: {'OK' if r.get('success') else r}")

        # Update entities
        ok = fail = 0
        for eid, ca, na, cl, nl, matched in entity_plan:
            kw = {"type": "config/entity_registry/update", "entity_id": eid, "labels": nl}
            if ca != na:
                kw["area_id"] = na
            r = await ws_call(ws, nid(), **kw)
            if r.get("success"):
                ok += 1
            else:
                fail += 1
                print(f"  FAIL {eid}: {r}")
        print(f"  entity updates: {ok} OK, {fail} FAIL")

        # Delete old area
        if OLD_AREA in existing_area_ids:
            r = await ws_call(ws, nid(), type="config/area_registry/delete", area_id=OLD_AREA)
            print(f"  delete area '{OLD_AREA}': {'OK' if r.get('success') else r}")

        # Delete old label
        if OLD_LABEL in existing_label_ids:
            r = await ws_call(ws, nid(), type="config/label_registry/delete", label_id=OLD_LABEL)
            print(f"  delete label '{OLD_LABEL}': {'OK' if r.get('success') else r}")

        print("\n=== APPLY COMPLETE ===")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Commit changes (default: dry run)")
    args = ap.parse_args()
    asyncio.run(main(args.apply))
