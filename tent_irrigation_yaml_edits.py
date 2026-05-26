"""Apply tent-irrigation rename to YAML files in homeassistant-config repo.

Replacements:
  - alias: Irrigation —                   -> alias: Tent Irrigation —
  - alias: Toggle — Kill Irrigation ...   -> alias: Toggle — Kill Tent Irrigation ...
  - automation.irrigation_*               -> automation.tent_irrigation_*  (for renamed list only)
  - automation.toggle_kill_irrigation_... -> automation.toggle_kill_tent_irrigation_...
  - script.irrigation_advance_to_next_feed -> script.tent_irrigation_advance_to_next_feed
  - input_boolean.irrigation_enabled       -> input_boolean.tent_irrigation_enabled
  - input_boolean.irrigation_kill_automations -> input_boolean.tent_irrigation_kill_automations
  - input_text.irrigation_status           -> input_text.tent_irrigation_status
  - switch.irrigation_power_strip          -> switch.tent_irrigation_power_strip

Idempotent: running twice is a no-op (the second pass finds no matches).
Dry-run by default. Pass --apply to write changes to disk.
"""
from __future__ import annotations
import argparse, pathlib, sys
import re

REPO = pathlib.Path(r"D:\Claude\Projects\homeassistant-config")

# Files that contain irrigation references (from earlier grep)
TARGET_FILES = [
    REPO / "scripts.yaml",
    REPO / "packages" / "tent" / "control" / "safety.yaml",
    REPO / "packages" / "tent" / "irrigation" / "drainage.yaml",
    REPO / "packages" / "tent" / "irrigation" / "feed_cycle.yaml",
    REPO / "packages" / "tent" / "irrigation" / "night_pulses.yaml",
    REPO / "packages" / "tent" / "irrigation" / "reservoirs.yaml",
    REPO / "packages" / "tent" / "irrigation" / "safety.yaml",
    REPO / "packages" / "tent" / "irrigation" / "schedule.yaml",
]

# 19 automations to rename (kept the ones that exist in YAML; orphans not in YAML)
RENAMED_AUTOMATIONS = [
    "block_feed_fill_when_reservoir_full",
    "block_feed_when_reservoir_dry",
    "block_flush_fill_when_reservoir_full",
    "block_flush_when_reservoir_dry",
    "block_table_drain_pump_when_dry",
    "daily_setup_at_lights_on",
    "daily_setup",  # this is the unique_id used in YAML `id:` field for daily_setup_at_lights_on
    "feed_trigger",
    "lights_off_cleanup",
    "lights_off_stop",  # YAML `id` for lights_off_cleanup
    "low_flow_safety",
    "maintenance_cycle",
    "night_pulses_flower",
    "night_pulses_veg",
    "pre_feed_air_stir_start",
    "pre_feed_start",  # YAML `id` for pre_feed_air_stir_start
    "pre_feed_air_stir_stop",
    "pre_feed_stop",  # YAML `id` for pre_feed_air_stir_stop
    "re_enable_maintenance_on_enable",
    "enabled_resync",  # YAML `id` for re_enable_maintenance
    "startup_recovery",
    "table_drain_pump",
    "watchdog",
    "feed_empty_block",  # YAML `id` for block_feed_when_reservoir_dry
    "flush_empty_block",  # YAML `id` for block_flush_when_reservoir_dry
    "table_drain_empty_block",  # YAML `id` for block_table_drain_pump_when_dry
]


def build_replacements() -> list[tuple[str, str]]:
    repls: list[tuple[str, str]] = []

    # Aliases (friendly names). Toggle is more specific so do it first.
    repls.append(("alias: Toggle — Kill Irrigation Automations",
                  "alias: Toggle — Kill Tent Irrigation Automations"))
    repls.append(("alias: Irrigation —", "alias: Tent Irrigation —"))

    # Toggle automation entity_id (NOT the unique_id `id:` field — leaving that
    # alone preserves the registry match).
    repls.append(("automation.toggle_kill_irrigation_automations",
                  "automation.toggle_kill_tent_irrigation_automations"))

    # All renamed automations: only update entity_id REFERENCES (e.g. inside
    # `entity_id:` keys, target lists, comments). The YAML `id:` (unique_id)
    # field must stay unchanged so HA can match the existing registry entries
    # we're about to rename. To avoid touching `id:` lines, we anchor on
    # `automation.irrigation_<name>` only when not preceded by `id: `.
    # The simple `str.replace` here would match those too, so we use regex.
    for name in sorted(RENAMED_AUTOMATIONS, key=len, reverse=True):
        repls.append((f"automation.irrigation_{name}",
                      f"automation.tent_irrigation_{name}"))

    # Script
    repls.append(("script.irrigation_advance_to_next_feed",
                  "script.tent_irrigation_advance_to_next_feed"))

    # Helpers
    repls.append(("input_boolean.irrigation_enabled",
                  "input_boolean.tent_irrigation_enabled"))
    repls.append(("input_boolean.irrigation_kill_automations",
                  "input_boolean.tent_irrigation_kill_automations"))
    repls.append(("input_text.irrigation_status",
                  "input_text.tent_irrigation_status"))

    # Switch
    repls.append(("switch.irrigation_power_strip",
                  "switch.tent_irrigation_power_strip"))

    return repls


def is_id_line(line: str) -> bool:
    """True if this YAML line is a unique_id assignment (`id:` or `- id:`).
    We must NOT rewrite entity_id-shaped strings on these lines, because the
    `id:` field is the unique_id and renaming it would orphan the registry
    entry on next HA reload."""
    stripped = line.lstrip()
    if stripped.startswith("- id:") or stripped.startswith("id:"):
        return True
    return False


def apply_to_file(path: pathlib.Path, replacements: list[tuple[str, str]],
                  apply: bool) -> tuple[int, list[tuple[str, str, int]]]:
    """Returns (total_changes, [(old, new, count), ...])."""
    if not path.exists():
        return 0, []
    text = path.read_text(encoding="utf-8")
    original = text
    per_repl_counts: dict[tuple[str, str], int] = {}

    new_lines = []
    for line in text.splitlines(keepends=True):
        skip_entity_subs = is_id_line(line)
        for old, new in replacements:
            if old == new:
                continue
            # Skip entity_id-style replacements on `id:` lines (those are unique_ids).
            # Aliases (`alias: ...`) are always safe.
            if skip_entity_subs and not old.startswith("alias:"):
                continue
            if old in line:
                count = line.count(old)
                line = line.replace(old, new)
                per_repl_counts[(old, new)] = per_repl_counts.get((old, new), 0) + count
        new_lines.append(line)
    text = "".join(new_lines)

    if text != original and apply:
        path.write_text(text, encoding="utf-8")
    per_repl = [(o, n, c) for (o, n), c in per_repl_counts.items()]
    total = sum(c for _, _, c in per_repl)
    return total, per_repl


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Write changes to disk (default: dry run)")
    args = ap.parse_args()

    replacements = build_replacements()

    grand_total = 0
    for path in TARGET_FILES:
        total, per_repl = apply_to_file(path, replacements, args.apply)
        if total == 0:
            print(f"  {path.relative_to(REPO)}: no changes")
            continue
        grand_total += total
        print(f"\n  {path.relative_to(REPO)}: {total} changes")
        for old, new, count in per_repl:
            short_old = old if len(old) <= 60 else old[:57] + "..."
            short_new = new if len(new) <= 60 else new[:57] + "..."
            print(f"    [{count:3d}] {short_old}\n          -> {short_new}")

    if not args.apply:
        print(f"\n=== DRY RUN — {grand_total} total replacements would be made. Re-run with --apply. ===")
    else:
        print(f"\n=== APPLIED {grand_total} replacements ===")


if __name__ == "__main__":
    main()
