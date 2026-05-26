"""Phase 1c — cleanup patch for 21 tent-scope helpers/automations missed by 1a+1b.

These are automations/helpers that had no matching rule in phase 1a/1b and ended up with
empty label sets. All are tent-scope grow-related.

Dry-run by default. Pass `--apply` to commit.

Invariants per tagging_standard.md (v1):
  - Exactly one sys_, at most one sub_, exactly one sev_ per helper/automation.
  - No fn_ on automations/helpers.
  - All get `grow`.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
from dataclasses import dataclass
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"


@dataclass
class Patch:
    entity_id: str
    labels: list[str]


# All 21 stragglers. bambu_light_on_power is intentionally excluded (3D printer, not grow).
PATCHES: list[Patch] = [
    # ============================================================
    # IRRIGATION HELPERS (11) — sys_irrigation + sub_ + sev_info + grow
    # ============================================================
    # Feed loop
    Patch("input_datetime.next_feed_time",               ["sys_irrigation","sub_irrigation_feed_loop","sev_info","grow"]),
    Patch("input_datetime.next_pre_feed_start",          ["sys_irrigation","sub_irrigation_feed_loop","sev_info","grow"]),
    Patch("input_datetime.next_pre_feed_stop",           ["sys_irrigation","sub_irrigation_feed_loop","sev_info","grow"]),
    Patch("input_number.current_feed_number",            ["sys_irrigation","sub_irrigation_feed_loop","sev_info","grow"]),
    Patch("input_number.feed_duration_minutes",          ["sys_irrigation","sub_irrigation_feed_loop","sev_info","grow"]),
    Patch("input_number.feeds_per_day_2",                ["sys_irrigation","sub_irrigation_feed_loop","sev_info","grow"]),
    # Flush loop
    Patch("input_datetime.last_flush_date",              ["sys_irrigation","sub_irrigation_flush_loop","sev_info","grow"]),
    Patch("input_number.flush_cycle_plant_minutes",      ["sys_irrigation","sub_irrigation_flush_loop","sev_info","grow"]),
    Patch("input_number.flush_day_counter",              ["sys_irrigation","sub_irrigation_flush_loop","sev_info","grow"]),
    Patch("input_number.flush_duration_minutes",         ["sys_irrigation","sub_irrigation_flush_loop","sev_info","grow"]),
    # Drain loop
    Patch("input_number.flush_cycle_drain_minutes",      ["sys_irrigation","sub_irrigation_drain_loop","sev_info","grow"]),

    # ============================================================
    # CLIMATE — AC "lights" automations (stage transitions; sub_ac)
    # ============================================================
    Patch("automation.ac_lights_off_night_mode",         ["sys_climate","sub_climate_ac","sev_info","grow"]),
    Patch("automation.ac_lights_on_day_mode",            ["sys_climate","sub_climate_ac","sev_info","grow"]),

    # ============================================================
    # CLIMATE — Fans "lights" automations (circulation stage transitions)
    # ============================================================
    Patch("automation.fans_lights_off_night_mode",       ["sys_climate","sub_climate_circulation","sev_info","grow"]),
    Patch("automation.fans_lights_on_day_mode",          ["sys_climate","sub_climate_circulation","sev_info","grow"]),

    # ============================================================
    # CLIMATE — Humidity automations + day-target helper
    # ============================================================
    Patch("automation.humidity_lights_off_night_target", ["sys_climate","sub_climate_humidifier","sev_info","grow"]),
    Patch("automation.humidity_lights_on_day_target",    ["sys_climate","sub_climate_humidifier","sev_info","grow"]),
    Patch("automation.humidity_mode_changed",            ["sys_climate","sub_climate_humidifier","sev_info","grow"]),
    Patch("input_number.humidity_day_target",            ["sys_climate","sub_climate_humidifier","sev_info","grow"]),

    # ============================================================
    # LIGHTING — Veg schedule helpers (no sub_)
    # ============================================================
    Patch("input_datetime.veg_lights_off_time",          ["sys_lighting","sev_info","grow"]),
    Patch("input_datetime.veg_lights_on_time",           ["sys_lighting","sev_info","grow"]),
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

        plan = []       # (eid, current, new)
        missing = []    # eid not in registry
        no_change = []  # already correct

        for p in PATCHES:
            if p.entity_id not in by_id:
                missing.append(p.entity_id)
                continue
            cur = list(by_id[p.entity_id].get("labels") or [])
            # Additive: keep whatever is already there, union with desired
            new = list(cur)
            for L in p.labels:
                if L not in new:
                    new.append(L)
            if sorted(new) == sorted(cur):
                no_change.append(p.entity_id)
            else:
                plan.append((p.entity_id, cur, new))

        print(f"=== PHASE 1C PLAN ===")
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
            for eid, cl, nl in plan:
                added = [L for L in nl if L not in cl]
                print(f"  {eid:55s}  +{added}  (was: {cl})")

        if not apply:
            print("\n=== DRY RUN — re-run with --apply to commit. ===")
            return

        print("\n====== APPLYING ======")
        ok = fail = 0
        for eid, cl, nl in plan:
            r = await ws_call(ws, nid(), type="config/entity_registry/update",
                              entity_id=eid, labels=nl)
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
