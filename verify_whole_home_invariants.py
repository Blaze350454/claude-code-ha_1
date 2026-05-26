"""Verify tagging_standard.md invariants across every tagged system, whole-home.

Covers:
  - Tent grow (sys_irrigation, sys_climate, sys_lighting)
  - 3D printer  (sys_printer + bambu/prusa brands)
  - Cameras     (sys_camera + blink brand + sub_camera_{indoor,outdoor})

Reports 5 core invariants + 3 cross-cutting checks + per-system breakdown.
"""
from __future__ import annotations
import asyncio, json, pathlib
from collections import defaultdict
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

ALL_SYS_LABELS = {
    "sys_irrigation", "sys_climate", "sys_lighting", "sys_power",
    "sys_printer", "sys_camera",
}
GROW_SYS_LABELS = {"sys_irrigation", "sys_climate", "sys_lighting"}
SEV_LABELS = {"sev_critical", "sev_warning", "sev_info"}

HELPER_DOMAINS = {
    "input_boolean", "input_datetime", "input_number", "input_select",
    "input_text", "input_button", "automation", "script", "scene",
    "timer", "counter",
}
ENTITY_DOMAINS = {
    "switch", "sensor", "binary_sensor", "light", "fan", "valve", "climate",
    "button", "number", "select", "camera", "update", "alarm_control_panel",
}

# Tent entities explicitly deferred (not in use / future hw) — skip scope
DEFERRED = {
    "switch.blank_2", "switch.humidifier_2", "switch.grow_tent_one_extra_relay",
    "switch.kasa_smart_outdoor_plug_switch_1", "switch.kasa_smart_outdoor_plug_switch_2",
}
def is_future_hw(eid: str) -> bool:
    return "grow_tent_two_plant_" in eid or "grow_tent_two_flood_" in eid

# Aggregated template sensors — documented exception to fn_ requirement
AGGREGATE_SENSORS = {
    "sensor.grow_tent_vpd", "sensor.grow_tent_dli", "sensor.grow_tent_status",
}


async def ws_call(ws, mid, **kw):
    await ws.send(json.dumps({"id": mid, **kw}))
    while True:
        r = json.loads(await ws.recv())
        if r.get("id") == mid:
            return r


async def main():
    async with websockets.connect(WS_URL, max_size=None) as ws:
        assert json.loads(await ws.recv())["type"] == "auth_required"
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        assert json.loads(await ws.recv())["type"] == "auth_ok"
        entities = (await ws_call(ws, 1, type="config/entity_registry/list"))["result"]

    # Scope: any entity carrying a known sys_ label. Deferred/future-hw excluded.
    scope = []
    for e in entities:
        eid = e["entity_id"]
        labels = set(e.get("labels") or [])
        if not (labels & ALL_SYS_LABELS):
            continue
        if eid in DEFERRED or is_future_hw(eid):
            continue
        scope.append(e)

    # Per-system bucket (first matching sys_ label wins for bucket display)
    buckets = defaultdict(list)
    for e in scope:
        labels = set(e.get("labels") or [])
        sys_hits = labels & ALL_SYS_LABELS
        # Put into each sys_ bucket it belongs to (multi-sys violations show everywhere)
        for s in sys_hits:
            buckets[s].append(e)

    print(f"=== WHOLE-HOME TAG INVARIANT CHECK ===")
    print(f"In-scope entities (have any sys_, excl. deferred/future-hw): {len(scope)}\n")
    print("Per-system entity counts:")
    for s in sorted(buckets):
        print(f"  {s:18s} {len(buckets[s]):4d}")
    print()

    # ---- Core invariants ----

    # [1] exactly one sys_ per entity
    missing_sys, multi_sys = [], []
    for e in scope:
        labels = set(e.get("labels") or [])
        n = len(labels & ALL_SYS_LABELS)
        if n == 0: missing_sys.append(e["entity_id"])
        elif n > 1: multi_sys.append((e["entity_id"], sorted(labels & ALL_SYS_LABELS)))
    print("[1] exactly one sys_ per entity")
    print(f"    missing: {len(missing_sys)}   multiple: {len(multi_sys)}")
    for eid in sorted(missing_sys)[:20]: print(f"      - {eid}")
    for eid, sl in sorted(multi_sys)[:20]: print(f"      - {eid}  {sl}")

    # [2] exactly one sev_ per entity
    missing_sev, multi_sev = [], []
    for e in scope:
        labels = set(e.get("labels") or [])
        n = len(labels & SEV_LABELS)
        if n == 0: missing_sev.append(e["entity_id"])
        elif n > 1: multi_sev.append((e["entity_id"], sorted(labels & SEV_LABELS)))
    print(f"\n[2] exactly one sev_ per entity")
    print(f"    missing: {len(missing_sev)}   multiple: {len(multi_sev)}")
    for eid in sorted(missing_sev)[:20]: print(f"      - {eid}")
    for eid, sl in sorted(multi_sev)[:20]: print(f"      - {eid}  {sl}")

    # [3] no fn_ on helpers/automations/scripts/etc.
    helper_with_fn = []
    for e in scope:
        eid = e["entity_id"]
        dom = eid.split(".", 1)[0]
        if dom not in HELPER_DOMAINS: continue
        fns = [L for L in (e.get("labels") or []) if L.startswith("fn_")]
        if fns: helper_with_fn.append((eid, fns))
    print(f"\n[3] no fn_ on helpers / automations / scripts")
    print(f"    violations: {len(helper_with_fn)}")
    for eid, fns in helper_with_fn[:20]: print(f"      - {eid}  {fns}")

    # [4] at least one fn_ on non-helper entity domains (except aggregates)
    missing_fn = []
    for e in scope:
        eid = e["entity_id"]
        dom = eid.split(".", 1)[0]
        if dom not in ENTITY_DOMAINS: continue
        if eid in AGGREGATE_SENSORS: continue
        fns = [L for L in (e.get("labels") or []) if L.startswith("fn_")]
        if not fns: missing_fn.append(eid)
    print(f"\n[4] at least one fn_ on non-helper entities (aggregates excepted)")
    print(f"    missing: {len(missing_fn)}")
    for eid in sorted(missing_fn)[:20]: print(f"      - {eid}")

    # [5] exactly one sub_camera_* on every sys_camera entity
    cam_sub_bad = []
    for e in buckets.get("sys_camera", []):
        labels = set(e.get("labels") or [])
        subs = [L for L in labels if L.startswith("sub_camera_")]
        if len(subs) != 1:
            cam_sub_bad.append((e["entity_id"], subs))
    print(f"\n[5] exactly one sub_camera_* on every sys_camera entity")
    print(f"    violations: {len(cam_sub_bad)}")
    for eid, subs in cam_sub_bad[:20]: print(f"      - {eid}  {subs}")

    # ---- Cross-cutting brand / grow checks ----

    # [6] `grow` on every tent-grow entity
    no_grow = []
    for e in scope:
        labels = set(e.get("labels") or [])
        if labels & GROW_SYS_LABELS and "grow" not in labels:
            no_grow.append(e["entity_id"])
    print(f"\n[6] `grow` on every tent-grow (sys_irrigation/climate/lighting) entity")
    print(f"    missing: {len(no_grow)}")
    for eid in sorted(no_grow)[:20]: print(f"      - {eid}")

    # [7] `blink` on every sys_camera entity (whole-home rule for now)
    no_blink = []
    for e in buckets.get("sys_camera", []):
        labels = set(e.get("labels") or [])
        if "blink" not in labels:
            no_blink.append(e["entity_id"])
    print(f"\n[7] `blink` on every sys_camera entity")
    print(f"    missing: {len(no_blink)}")
    for eid in sorted(no_blink)[:20]: print(f"      - {eid}")

    # [8] sys_printer entity must carry `bambu` or `prusa`
    no_brand = []
    for e in buckets.get("sys_printer", []):
        labels = set(e.get("labels") or [])
        if not (labels & {"bambu", "prusa"}):
            no_brand.append(e["entity_id"])
    print(f"\n[8] sys_printer entity carries a brand (`bambu` or `prusa`)")
    print(f"    missing: {len(no_brand)}")
    for eid in sorted(no_brand)[:20]: print(f"      - {eid}")

    # ---- Summary ----
    all_ok = not (
        missing_sys or multi_sys or missing_sev or multi_sev or helper_with_fn
        or missing_fn or cam_sub_bad or no_grow or no_blink or no_brand
    )
    print(f"\n=== SUMMARY ===")
    print(f"  scope entities: {len(scope)}")
    print(f"  ALL INVARIANTS HOLD: {all_ok}")


if __name__ == "__main__":
    asyncio.run(main())
