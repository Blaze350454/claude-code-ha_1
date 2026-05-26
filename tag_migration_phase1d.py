"""Phase 1d — patch AC/dehumidifier sub-controls with proper fn_ labels.

Phase 1b tagged the main AC entity but skipped the dozens of sub-controls
(eco mode, swing, airflow selects, etc.). These all need sys_climate + sub_climate_*
+ sev_info + fn_{climate|fan} + grow.

3 aggregated template sensors (grow_tent_vpd/dli/status) are intentionally left
with only sys_ + sev_info — documented as "aggregated/template sensor" exceptions
in tagging_standard.md.

1 camera entity (binary_sensor.tent_camera_armed) is phase-2 scope, left untagged.

Dry-run by default. Pass `--apply` to commit.
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


# Each entry is DESIRED full label set. Script is additive (merges with existing).
AC = ["sys_climate","sub_climate_ac","sev_info","grow"]
DEHUM = ["sys_climate","sub_climate_dehumidifier","sev_info","grow"]

PATCHES: list[Patch] = [
    # AC — airflow direction (fan-function)
    Patch("number.fan_speed_percent_air_conditioner_tent",     AC + ["fn_fan"]),
    Patch("select.airflow_horizontal_air_conditioner_tent",    AC + ["fn_fan"]),
    Patch("select.airflow_vertical_air_conditioner_tent",      AC + ["fn_fan"]),
    Patch("switch.indirect_wind_air_conditioner_tent",         AC + ["fn_fan"]),
    Patch("switch.natural_wind_air_conditioner_tent",          AC + ["fn_fan"]),
    Patch("switch.swing_horizontal_air_conditioner_tent",      AC + ["fn_fan"]),
    Patch("switch.swing_vertical_air_conditioner_tent",        AC + ["fn_fan"]),

    # AC — mode switches (climate-function)
    Patch("switch.aux_heating_air_conditioner_tent",           AC + ["fn_climate"]),
    Patch("switch.boost_mode_air_conditioner_tent",            AC + ["fn_climate"]),
    Patch("switch.breezeless_air_conditioner_tent",            AC + ["fn_climate"]),
    Patch("switch.comfort_mode_air_conditioner_tent",          AC + ["fn_climate"]),
    Patch("switch.dehumidifier_air_conditioner_tent",          AC + ["fn_climate"]),  # dry-mode switch on the AC
    Patch("switch.eco_mode_air_conditioner_tent",              AC + ["fn_climate"]),
    Patch("switch.frost_protect_air_onditioner_tent",          AC + ["fn_climate"]),
    Patch("switch.sleep_mode_air_conditioner_tent",            AC + ["fn_climate"]),
    Patch("switch.smart_eye_air_conditioner_tent",             AC + ["fn_climate"]),

    # AC — device UI / diagnostic (climate-function, no better bucket)
    Patch("switch.prompt_tone_air_conditioner_tent",           AC + ["fn_climate"]),
    Patch("switch.screen_display_air_conditioner_tent",        AC + ["fn_climate"]),
    Patch("switch.screen_display_alternate_air_conditioner_tent", AC + ["fn_climate"]),
    # full_dust already has sev_warning (filter-needs-cleaning alert) — keep that, only add fn_
    Patch("binary_sensor.full_dust_air_conditioner_tent",
          ["sys_climate","sub_climate_ac","grow","fn_climate"]),

    # Dehumidifier — sub-controls
    Patch("select.water_level_set_dehumidifier",               DEHUM + ["fn_climate"]),
    Patch("switch.anion_dehumidifier",                         DEHUM + ["fn_climate"]),
    Patch("switch.prompt_tone_dehumidifier",                   DEHUM + ["fn_climate"]),
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

        plan = []
        missing = []
        no_change = []

        for p in PATCHES:
            if p.entity_id not in by_id:
                missing.append(p.entity_id); continue
            cur = list(by_id[p.entity_id].get("labels") or [])
            new = list(cur)
            for L in p.labels:
                if L not in new:
                    new.append(L)
            if sorted(new) == sorted(cur):
                no_change.append(p.entity_id)
            else:
                plan.append((p.entity_id, cur, new))

        print(f"=== PHASE 1D PLAN ===")
        print(f"  patches requested: {len(PATCHES)}")
        print(f"  will update:       {len(plan)}")
        print(f"  already correct:   {len(no_change)}")
        print(f"  missing from reg:  {len(missing)}")

        if missing:
            print(f"\n--- MISSING ---")
            for eid in missing: print(f"  ? {eid}")

        if plan:
            print(f"\n--- CHANGES ---")
            for eid, cl, nl in plan:
                added = [L for L in nl if L not in cl]
                print(f"  {eid:58s}  +{added}  (was: {cl})")

        if not apply:
            print("\n=== DRY RUN — re-run with --apply to commit. ===")
            return

        print("\n====== APPLYING ======")
        ok = fail = 0
        for eid, cl, nl in plan:
            r = await ws_call(ws, nid(), type="config/entity_registry/update",
                              entity_id=eid, labels=nl)
            if r.get("success"): ok += 1
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
