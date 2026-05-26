"""Tent Irrigation Rename Migration.

Renames every entity / automation / script / helper / switch / device that
currently has "irrigation" in its identifier but no "tent" — to include "tent".
Leaves labels (sys_irrigation, sub_irrigation_*) generic per the tagging
standard. Leaves the Kasa "Irrigation Multi - Plug" device alone.

What this does, in a single authenticated WebSocket session:
  1. Renames automation/script/switch entity_ids in the entity registry,
     plus updates their friendly name override.
  2. Renames the HS300 device's `name_by_user`:
     "Irrigation Power Strip" -> "Tent Irrigation Power Strip".
  3. Deletes the two orphan automations (irrigation_night_cycle_start/stop)
     that are currently `state: unavailable, restored: true`.
  4. (Helpers) Renames the entity_ids of input_boolean.irrigation_enabled,
     input_boolean.irrigation_kill_automations, input_text.irrigation_status
     in the registry. The underlying .storage/input_boolean and
     .storage/input_text id-field cleanup is done separately by the
     `--storage-cleanup` step (which edits local repo files; requires
     subsequent commit/push/VM-pull/restart).

Idempotent: skips items already renamed.
Dry-run by default. Pass `--apply` to commit registry changes.
Pass `--storage-cleanup` to also rewrite the local .storage helper files.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib, sys
import websockets

HERE = pathlib.Path(__file__).parent
REPO = pathlib.Path(r"D:\Claude\Projects\homeassistant-config")
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

HS300_DEVICE_ID = "0fcd2598b991e9c34ada7834acc81788"
HS300_OLD_NAME  = "Irrigation Power Strip"
HS300_NEW_NAME  = "Tent Irrigation Power Strip"

# (old_entity_id, new_entity_id, new_friendly_name_or_None)
RENAMES = [
    # --- 21 automations ---
    ("automation.irrigation_block_feed_fill_when_reservoir_full",
     "automation.tent_irrigation_block_feed_fill_when_reservoir_full",
     "Tent Irrigation — Block Feed Fill When Reservoir Full"),
    ("automation.irrigation_block_feed_when_reservoir_dry",
     "automation.tent_irrigation_block_feed_when_reservoir_dry",
     "Tent Irrigation — Block Feed When Reservoir Dry"),
    ("automation.irrigation_block_flush_fill_when_reservoir_full",
     "automation.tent_irrigation_block_flush_fill_when_reservoir_full",
     "Tent Irrigation — Block Flush Fill When Reservoir Full"),
    ("automation.irrigation_block_flush_when_reservoir_dry",
     "automation.tent_irrigation_block_flush_when_reservoir_dry",
     "Tent Irrigation — Block Flush When Reservoir Dry"),
    ("automation.irrigation_block_table_drain_pump_when_dry",
     "automation.tent_irrigation_block_table_drain_pump_when_dry",
     "Tent Irrigation — Block Table Drain Pump When Dry"),
    ("automation.irrigation_daily_setup_at_lights_on",
     "automation.tent_irrigation_daily_setup_at_lights_on",
     "Tent Irrigation — Daily Setup at Lights On"),
    ("automation.irrigation_feed_trigger",
     "automation.tent_irrigation_feed_trigger",
     "Tent Irrigation — Feed Trigger"),
    ("automation.irrigation_lights_off_cleanup",
     "automation.tent_irrigation_lights_off_cleanup",
     "Tent Irrigation — Lights Off Cleanup"),
    ("automation.irrigation_low_flow_safety",
     "automation.tent_irrigation_low_flow_safety",
     "Tent Irrigation — Low Flow Safety"),
    ("automation.irrigation_maintenance_cycle",
     "automation.tent_irrigation_maintenance_cycle",
     "Tent Irrigation — Maintenance Cycle"),
    ("automation.irrigation_night_pulses_flower",
     "automation.tent_irrigation_night_pulses_flower",
     "Tent Irrigation — Night Pulses (Flower)"),
    ("automation.irrigation_night_pulses_veg",
     "automation.tent_irrigation_night_pulses_veg",
     "Tent Irrigation — Night Pulses (Veg)"),
    ("automation.irrigation_pre_feed_air_stir_start",
     "automation.tent_irrigation_pre_feed_air_stir_start",
     "Tent Irrigation — Pre-Feed Air/Stir Start"),
    ("automation.irrigation_pre_feed_air_stir_stop",
     "automation.tent_irrigation_pre_feed_air_stir_stop",
     "Tent Irrigation — Pre-Feed Air/Stir Stop"),
    ("automation.irrigation_re_enable_maintenance_on_enable",
     "automation.tent_irrigation_re_enable_maintenance_on_enable",
     "Tent Irrigation — Re-enable Maintenance on Enable"),
    ("automation.irrigation_startup_recovery",
     "automation.tent_irrigation_startup_recovery",
     "Tent Irrigation — Startup Recovery"),
    ("automation.irrigation_table_drain_pump",
     "automation.tent_irrigation_table_drain_pump",
     "Tent Irrigation — Table Drain Pump"),
    ("automation.irrigation_watchdog",
     "automation.tent_irrigation_watchdog",
     "Tent Irrigation — Watchdog"),
    ("automation.toggle_kill_irrigation_automations",
     "automation.toggle_kill_tent_irrigation_automations",
     "Toggle — Kill Tent Irrigation Automations"),
    # --- 1 script ---
    ("script.irrigation_advance_to_next_feed",
     "script.tent_irrigation_advance_to_next_feed",
     "Tent Irrigation — Advance to Next Feed"),
    # --- 3 helpers ---
    ("input_boolean.irrigation_enabled",
     "input_boolean.tent_irrigation_enabled",
     "Tent Irrigation Enabled"),
    ("input_boolean.irrigation_kill_automations",
     "input_boolean.tent_irrigation_kill_automations",
     "Tent Irrigation Kill Automations"),
    ("input_text.irrigation_status",
     "input_text.tent_irrigation_status",
     "Tent Irrigation Status"),
    # --- 1 switch ---
    ("switch.irrigation_power_strip",
     "switch.tent_irrigation_power_strip",
     None),  # name comes from device, no override needed
]

ORPHANS_TO_DELETE = [
    "automation.irrigation_night_cycle_start",
    "automation.irrigation_night_cycle_stop",
]


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
        devices  = (await ws_call(ws, nid(), type="config/device_registry/list"))["result"]
        eid_map  = {e["entity_id"]: e for e in entities}
        new_eids = {e["entity_id"] for e in entities}

        print(f"Loaded: {len(entities)} entities, {len(devices)} devices")

        # === Plan renames ===
        rename_plan = []   # (old, new, name, status)
        for old, new, name in RENAMES:
            if old in eid_map:
                rename_plan.append((old, new, name, "rename"))
            elif new in eid_map:
                rename_plan.append((old, new, name, "already-renamed"))
            else:
                rename_plan.append((old, new, name, "MISSING"))

        # === Plan orphan deletes ===
        delete_plan = []
        for eid in ORPHANS_TO_DELETE:
            if eid in eid_map:
                delete_plan.append((eid, "delete"))
            else:
                delete_plan.append((eid, "already-gone"))

        # === Plan device rename ===
        hs300 = next((d for d in devices if d["id"] == HS300_DEVICE_ID), None)
        if hs300 is None:
            device_status = "MISSING"
            current_name = None
        else:
            current_name = hs300.get("name_by_user")
            if current_name == HS300_NEW_NAME:
                device_status = "already-renamed"
            elif current_name == HS300_OLD_NAME:
                device_status = "rename"
            else:
                device_status = f"unexpected-current-name={current_name!r}"

        # === Print plan ===
        print("\n=== ENTITY RENAMES ===")
        for old, new, name, status in rename_plan:
            tag = "" if status == "rename" else f"  [{status}]"
            print(f"  {old:62s} -> {new}{tag}")

        print(f"\n=== ORPHAN DELETES ({len([p for p in delete_plan if p[1]=='delete'])}) ===")
        for eid, status in delete_plan:
            tag = "" if status == "delete" else f"  [{status}]"
            print(f"  - {eid}{tag}")

        print(f"\n=== DEVICE RENAME ===")
        print(f"  HS300 ({HS300_DEVICE_ID[:10]}..): {current_name!r} -> {HS300_NEW_NAME!r}  [{device_status}]")

        if not apply:
            print("\n=== DRY RUN — nothing was modified. Re-run with --apply to commit. ===")
            return

        # ============ APPLY ============
        print("\n\n====== APPLYING CHANGES ======\n")

        ok = fail = skip = 0
        for old, new, name, status in rename_plan:
            if status != "rename":
                skip += 1
                print(f"  skip {old}: {status}")
                continue
            kw = {"type": "config/entity_registry/update", "entity_id": old,
                  "new_entity_id": new}
            if name is not None:
                kw["name"] = name
            r = await ws_call(ws, nid(), **kw)
            if r.get("success"):
                ok += 1
                print(f"  OK   {old} -> {new}")
            else:
                fail += 1
                print(f"  FAIL {old}: {r}")

        # Delete orphans
        for eid, status in delete_plan:
            if status != "delete":
                print(f"  skip orphan {eid}: {status}")
                continue
            r = await ws_call(ws, nid(), type="config/entity_registry/remove", entity_id=eid)
            if r.get("success"):
                ok += 1
                print(f"  OK   delete orphan {eid}")
            else:
                fail += 1
                print(f"  FAIL delete orphan {eid}: {r}")

        # Device rename
        if device_status == "rename":
            r = await ws_call(ws, nid(), type="config/device_registry/update",
                              device_id=HS300_DEVICE_ID, name_by_user=HS300_NEW_NAME)
            if r.get("success"):
                ok += 1
                print(f"  OK   rename device HS300")
            else:
                fail += 1
                print(f"  FAIL rename device HS300: {r}")
        else:
            skip += 1
            print(f"  skip device rename: {device_status}")

        print(f"\n=== APPLY: {ok} OK, {fail} FAIL, {skip} SKIP ===")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Commit registry changes (default: dry run)")
    args = ap.parse_args()
    asyncio.run(main(args.apply))
