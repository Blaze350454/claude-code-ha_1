"""Tag the night-pulse subsystem entities added 2026-05-07.

Adds 13 new entities under sys_irrigation:
  - 7 input_datetime helpers (night_pulse_veg_1/2 + flower_1..5)
  - 3 input_number helpers (stir_pre / air / stir_post minutes)
  - 1 script (run_night_pulse) — analogue of script.run_alternating
  - 2 automations (irrigation_night_pulses_veg/_flower) — analogues of
    automation.irrigation_maintenance_cycle (interval scheduler firing pumps)

Dry-run by default. Pass `--apply` to commit.

Invariants per tagging_standard.md (v1):
  - Exactly one sys_, at most one sub_, exactly one sev_ per helper/automation.
  - No fn_ on automations/scripts/helpers.
  - All get `grow`.
  - No sub_ — operation spans both feed and flush loops, mirrors run_alternating
    and irrigation_maintenance_cycle (neither carries a sub_).

Severity:
  - Helpers + script: sev_info (matches script.run_alternating + helper convention)
  - Automations: sev_critical (matches automation.irrigation_maintenance_cycle —
    pump-firing scheduler whose failure cascades into reservoir health)

Area: tent (matches every other irrigation grow entity).
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
from dataclasses import dataclass
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

AREA = "tent"


@dataclass
class Patch:
    entity_id: str
    labels: list[str]


HELPER_LABELS = ["sys_irrigation", "sev_info", "grow"]
SCRIPT_LABELS = ["sys_irrigation", "sev_info", "grow"]
AUTOMATION_LABELS = ["sys_irrigation", "sev_critical", "grow"]
TRANSITION_AUTOMATION_LABELS = ["sys_irrigation", "sev_info", "grow"]

PATCHES: list[Patch] = [
    # input_datetime — when daily_setup runs (defaults to 17:00 = 1 hour before
    # veg_lights_on, so that pre-feed datetimes computed there land in the future)
    Patch("input_datetime.daily_setup_time",      HELPER_LABELS),

    # input_datetime helpers (UI-editable pulse start times)
    Patch("input_datetime.night_pulse_veg_1",     HELPER_LABELS),
    Patch("input_datetime.night_pulse_veg_2",     HELPER_LABELS),
    Patch("input_datetime.night_pulse_flower_1",  HELPER_LABELS),
    Patch("input_datetime.night_pulse_flower_2",  HELPER_LABELS),
    Patch("input_datetime.night_pulse_flower_3",  HELPER_LABELS),
    Patch("input_datetime.night_pulse_flower_4",  HELPER_LABELS),
    Patch("input_datetime.night_pulse_flower_5",  HELPER_LABELS),

    # input_number helpers (per-phase durations)
    Patch("input_number.night_pulse_stir_pre_minutes",  HELPER_LABELS),
    Patch("input_number.night_pulse_air_minutes",       HELPER_LABELS),
    Patch("input_number.night_pulse_stir_post_minutes", HELPER_LABELS),

    # input_number helpers (fill timeouts — replace hardcoded 3:50/2:50)
    Patch("input_number.feed_fill_timeout_seconds",     HELPER_LABELS),
    Patch("input_number.flush_fill_timeout_seconds",    HELPER_LABELS),

    # Script (sequence orchestrator)
    Patch("script.run_night_pulse", SCRIPT_LABELS),

    # Automations (stage-gated time triggers calling the script)
    Patch("automation.irrigation_night_pulses_veg",    AUTOMATION_LABELS),
    Patch("automation.irrigation_night_pulses_flower", AUTOMATION_LABELS),

    # Transition handler — re-enables maintenance on irrigation_enabled off->on
    # Slug derived from alias "Irrigation — Re-enable Maintenance on Enable"
    Patch("automation.irrigation_re_enable_maintenance_on_enable", TRANSITION_AUTOMATION_LABELS),
]


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
        by_id = {e["entity_id"]: e for e in entities}

        plan = []       # (eid, current_labels, new_labels, current_area, set_area)
        missing = []
        no_change = []

        for p in PATCHES:
            if p.entity_id not in by_id:
                missing.append(p.entity_id)
                continue
            cur_labels = list(by_id[p.entity_id].get("labels") or [])
            new_labels = list(cur_labels)
            for L in p.labels:
                if L not in new_labels:
                    new_labels.append(L)

            cur_area = by_id[p.entity_id].get("area_id")
            set_area = cur_area != AREA

            if sorted(new_labels) == sorted(cur_labels) and not set_area:
                no_change.append(p.entity_id)
            else:
                plan.append((p.entity_id, cur_labels, new_labels, cur_area, set_area))

        print(f"=== NIGHT PULSE TAG PLAN ===")
        print(f"  patches requested:  {len(PATCHES)}")
        print(f"  will update:        {len(plan)}")
        print(f"  already correct:    {len(no_change)}")
        print(f"  missing from reg:   {len(missing)}")

        if missing:
            print(f"\n--- MISSING entities (skipping) ---")
            for eid in missing:
                print(f"  ? {eid}")

        if plan:
            print(f"\n--- CHANGES ---")
            for eid, cl, nl, ca, sa in plan:
                added = [L for L in nl if L not in cl]
                area_note = f"  area: {ca!r} -> {AREA!r}" if sa else ""
                print(f"  {eid:55s}  +{added}{area_note}")

        if not apply:
            print("\n=== DRY RUN — re-run with --apply to commit. ===")
            return

        print("\n====== APPLYING ======")
        ok = fail = 0
        for eid, cl, nl, ca, sa in plan:
            kwargs = {"type": "config/entity_registry/update",
                      "entity_id": eid, "labels": nl}
            if sa:
                kwargs["area_id"] = AREA
            r = await ws_call(ws, nid(), **kwargs)
            if r.get("success"):
                ok += 1
            else:
                fail += 1
                print(f"  FAIL {eid}: {r}")
        print(f"\n  updates: {ok} OK, {fail} FAIL")
        print("=== APPLY COMPLETE ===")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    asyncio.run(main(args.apply))
