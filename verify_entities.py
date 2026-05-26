"""Verify all created entities against requested entity IDs."""
import json
import os
import subprocess
import sys

HA_TOKEN = os.environ["HA_TOKEN"]
HA_URL = "http://192.168.2.151:8123"

result = subprocess.run(
    ["curl", "-s", f"{HA_URL}/api/states",
     "-H", f"Authorization: Bearer {HA_TOKEN}"],
    capture_output=True, text=True
)
data = json.loads(result.stdout)

entities = {}
for e in data:
    if e["entity_id"].startswith("input_"):
        entities[e["entity_id"]] = e

# (requested_id, actual_id_in_ha)
MAPPING = [
    ("input_number.feeds_per_day",              "input_number.feeds_per_day"),
    ("input_number.feed_duration_minutes",      "input_number.feed_duration"),
    ("input_number.flush_duration_minutes",     "input_number.flush_duration"),
    ("input_number.air_stir_lead_minutes",      "input_number.air_stir_lead_time"),
    ("input_number.air_on_duration_minutes",    "input_number.air_pump_on_duration"),
    ("input_number.stir_on_duration_minutes",   "input_number.stir_pump_on_duration"),
    ("input_number.night_delay_minutes",        "input_number.night_cycle_delay_after_lights_off"),
    ("input_number.flush_cycle_drain_minutes",  "input_number.flush_cycle_drain_duration"),
    ("input_number.flush_cycle_plant_minutes",  "input_number.flush_cycle_plant_duration"),
    ("input_number.flush_day_counter",          "input_number.flush_day_counter"),
    ("input_number.current_feed_number",        "input_number.current_feed_number"),
    ("input_datetime.next_feed_time",           "input_datetime.next_feed_time"),
    ("input_datetime.next_pre_feed_start",      "input_datetime.pre_feed_air_stir_start"),
    ("input_datetime.next_pre_feed_stop",       "input_datetime.pre_feed_air_stir_stop"),
    ("input_datetime.night_cycle_start",        "input_datetime.night_cycle_start_time"),
    ("input_datetime.last_flush_date",          "input_datetime.last_flush_date"),
    ("input_boolean.alternating_active",        "input_boolean.air_stir_alternating_active"),
    ("input_boolean.irrigation_enabled",        "input_boolean.irrigation_enabled"),
    ("input_text.irrigation_status",            "input_text.irrigation_status"),
]

exact_match = []
id_mismatch = []
missing = []

print(f"\n{'Requested ID':<45} {'Status':<12} {'Actual ID in HA':<50} {'State'}")
print("-" * 130)

for req_id, actual_id in MAPPING:
    if req_id == actual_id:
        # Should be exact match
        if req_id in entities:
            e = entities[req_id]
            print(f"{req_id:<45} {'EXACT MATCH':<12} {req_id:<50} {e['state']}")
            exact_match.append(req_id)
        else:
            print(f"{req_id:<45} {'MISSING':<12} {req_id:<50} N/A")
            missing.append(req_id)
    else:
        # Check if it exists with the actual ID
        if actual_id in entities:
            e = entities[actual_id]
            fname = e["attributes"].get("friendly_name", "")
            print(f"{req_id:<45} {'ID MISMATCH':<12} {actual_id:<50} {e['state']} ({fname})")
            id_mismatch.append((req_id, actual_id))
        else:
            print(f"{req_id:<45} {'MISSING':<12} {'NOT FOUND':<50} N/A")
            missing.append(req_id)

print(f"\n\n=== SUMMARY ===")
print(f"Exact matches (entity_id correct): {len(exact_match)}")
for e in exact_match:
    print(f"  [OK] {e}")
print(f"\nID mismatches (entity exists but wrong ID): {len(id_mismatch)}")
for req, actual in id_mismatch:
    print(f"  [~] Requested: {req}")
    print(f"       Actual:   {actual}")
print(f"\nMissing: {len(missing)}")
for m in missing:
    print(f"  [X] {m}")
