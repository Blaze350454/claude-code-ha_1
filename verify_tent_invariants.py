"""Verify tagging_standard.md invariants across the full tent-scope registry post-phase1c."""
from __future__ import annotations
import asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

SYS_LABELS = {"sys_irrigation","sys_climate","sys_lighting","sys_power"}
SEV_LABELS = {"sev_critical","sev_warning","sev_info"}
HELPER_DOMAINS = {"input_boolean","input_datetime","input_number","input_select","input_text","automation","script","scene","timer","counter"}

DEFERRED = {
    "switch.blank_2","switch.humidifier_2","switch.grow_tent_one_extra_relay",
    "switch.kasa_smart_outdoor_plug_switch_1","switch.kasa_smart_outdoor_plug_switch_2",
}
# Camera tent entities (phase 2)
def is_camera(eid): return "camera_tent" in eid or "tent_camera" in eid or eid == "camera.tent"

AGGREGATE_SENSORS = {"sensor.grow_tent_vpd","sensor.grow_tent_dli","sensor.grow_tent_status"}
# Future-hardware entities on grow_tent_two ESP32
def is_future_hw(eid):
    return ("grow_tent_two_plant_" in eid) or ("grow_tent_two_flood_" in eid)


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

        mid = 0
        def nid(): nonlocal mid; mid += 1; return mid

        entities = (await ws_call(ws, nid(), type="config/entity_registry/list"))["result"]

    # Scope: anything in `tent` area OR tagged with any sys_/grow label OR matching deferred patterns
    tent_area_ents = []
    grow_tagged = []
    for e in entities:
        eid = e["entity_id"]
        labels = set(e.get("labels") or [])
        area = e.get("area_id")
        in_scope = (
            area == "tent"
            or (SYS_LABELS & labels)
            or "grow" in labels
        )
        if not in_scope:
            continue
        if eid in DEFERRED or is_camera(eid) or is_future_hw(eid):
            continue
        tent_area_ents.append(e)
        if "grow" in labels:
            grow_tagged.append(e)

    total = len(tent_area_ents)
    print(f"=== TENT-SCOPE ENTITIES (excl. deferred/camera/future-hw): {total} ===\n")

    # Invariant 1: exactly one sys_
    missing_sys = []
    multi_sys = []
    for e in tent_area_ents:
        labels = set(e.get("labels") or [])
        sys_count = len(labels & SYS_LABELS)
        if sys_count == 0:
            missing_sys.append(e["entity_id"])
        elif sys_count > 1:
            multi_sys.append((e["entity_id"], sorted(labels & SYS_LABELS)))

    print(f"[1] exactly one sys_ per entity")
    print(f"    missing sys_: {len(missing_sys)}")
    for eid in sorted(missing_sys)[:30]:
        print(f"      - {eid}")
    if len(missing_sys) > 30:
        print(f"      ... +{len(missing_sys)-30} more")
    print(f"    multiple sys_: {len(multi_sys)}")
    for eid, sl in sorted(multi_sys):
        print(f"      - {eid}  {sl}")

    # Invariant 2: exactly one sev_
    missing_sev = []
    multi_sev = []
    for e in tent_area_ents:
        labels = set(e.get("labels") or [])
        sev_count = len(labels & SEV_LABELS)
        if sev_count == 0:
            missing_sev.append(e["entity_id"])
        elif sev_count > 1:
            multi_sev.append((e["entity_id"], sorted(labels & SEV_LABELS)))

    print(f"\n[2] exactly one sev_ per entity")
    print(f"    missing sev_: {len(missing_sev)}")
    for eid in sorted(missing_sev)[:30]:
        print(f"      - {eid}")
    print(f"    multiple sev_: {len(multi_sev)}")
    for eid, sl in sorted(multi_sev):
        print(f"      - {eid}  {sl}")

    # Invariant 3: no fn_ on helpers/automations/scripts
    helper_with_fn = []
    for e in tent_area_ents:
        eid = e["entity_id"]
        dom = eid.split(".", 1)[0]
        if dom not in HELPER_DOMAINS:
            continue
        fns = [L for L in (e.get("labels") or []) if L.startswith("fn_")]
        if fns:
            helper_with_fn.append((eid, fns))

    print(f"\n[3] no fn_ on helpers/automations/scripts")
    print(f"    violations: {len(helper_with_fn)}")
    for eid, fns in helper_with_fn:
        print(f"      - {eid}  {fns}")

    # Invariant 4: grow label on every tent-scope grow entity
    no_grow = []
    for e in tent_area_ents:
        labels = set(e.get("labels") or [])
        if "grow" not in labels:
            no_grow.append(e["entity_id"])
    print(f"\n[4] `grow` label on every tent-scope entity")
    print(f"    missing grow: {len(no_grow)}")
    for eid in sorted(no_grow)[:20]:
        print(f"      - {eid}")

    # Invariant 5: at least one fn_ on non-helper entities
    ent_domains = {"switch","sensor","binary_sensor","light","fan","valve","climate","button","number","select"}
    no_fn = []
    for e in tent_area_ents:
        eid = e["entity_id"]
        dom = eid.split(".", 1)[0]
        if dom not in ent_domains:
            continue
        if eid in AGGREGATE_SENSORS:
            continue  # documented exception per tagging_standard.md
        fns = [L for L in (e.get("labels") or []) if L.startswith("fn_")]
        if not fns:
            no_fn.append(eid)
    print(f"\n[5] at least one fn_ on entities (non-helper)")
    print(f"    missing fn_: {len(no_fn)}")
    for eid in sorted(no_fn):
        print(f"      - {eid}")

    # Summary
    all_ok = not (missing_sys or multi_sys or missing_sev or multi_sev or helper_with_fn or no_grow or no_fn)
    print(f"\n=== SUMMARY ===")
    print(f"  in-scope entities: {total}")
    print(f"  grow-tagged:       {len(grow_tagged)}")
    print(f"  ALL INVARIANTS HOLD: {all_ok}")


if __name__ == "__main__":
    asyncio.run(main())
