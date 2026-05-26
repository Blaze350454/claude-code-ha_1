"""Phase 2 — Blink camera tagging (12 cams + 2 sync modules + bambu wifi retrofit).

Creates: sys_camera, blink, sub_camera_indoor, sub_camera_outdoor,
         fn_sensor_motion, fn_sensor_battery, fn_sensor_signal.
Applies: 86 Blink entities + 2 housekeeping fixes (bambu wifi +fn_sensor_signal,
         flow_rate stray wi_fi strip).
Strips:  loose labels `camera`, `wi_fi` from every holder.
Deletes: `camera` and `wi_fi` labels (verified 0 holders post-strip).
         `battery` label LEFT ALIVE — still used by 2 phone entities (phase 3 scope).

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

LABELS_TO_ENSURE = [
    ("sys_camera",          "sys_camera",          "red",         "mdi:cctv"),
    ("blink",               "blink",               "blue",        "mdi:video-wireless"),
    ("sub_camera_indoor",   "sub_camera_indoor",   "light-green", "mdi:home"),
    ("sub_camera_outdoor",  "sub_camera_outdoor",  "brown",       "mdi:tree"),
    ("fn_sensor_motion",    "fn_sensor_motion",    "amber",       "mdi:motion-sensor"),
    ("fn_sensor_battery",   "fn_sensor_battery",   "green",       "mdi:battery-medium"),
    ("fn_sensor_signal",    "fn_sensor_signal",    "teal",        "mdi:wifi"),
]

INDOOR_CAMS  = ["bath_room", "bedroom", "hall", "kitchen"]       # blink_<name>_ naming
OUTDOOR_CAMS = ["back_door", "front", "front_door", "front_driveway",
                "garage", "garden", "water_side"]

# Tent cam uses its own naming — 7 entities, device 5ae513c6. Treated as indoor + grow.
TENT_CAM_ENTITIES: dict[str, list[str]] = {
    "camera.tent":                              ["fn_camera",        "sev_info"],
    "binary_sensor.motion_camera_tent":         ["fn_sensor_motion", "sev_info"],
    "binary_sensor.battery_camera_tent":        ["fn_sensor_battery","sev_warning"],
    "binary_sensor.tent_camera_armed":          ["fn_sensor_status", "sev_info"],
    "switch.motion_detection_camera_tent":      ["fn_controller",    "sev_info"],
    "sensor.temperature_camera_tent":           ["fn_sensor_temp",   "sev_info"],
    "sensor.wi_fi_signal_strength_camera_tent": ["fn_sensor_signal", "sev_info"],
}

# Security cam per-field rules (applied to both indoor + outdoor names)
SECURITY_FIELD_RULES: dict[str, list[str]] = {
    "camera":                        ["fn_camera",        "sev_warning"],
    "motion":                        ["fn_sensor_motion", "sev_warning"],
    "battery":                       ["fn_sensor_battery","sev_warning"],
    "camera_armed":                  ["fn_sensor_status", "sev_info"],
    "camera_motion_detection":       ["fn_controller",    "sev_warning"],
    "temperature":                   ["fn_sensor_temp",   "sev_info"],
    "wi_fi_signal_strength":         ["fn_sensor_signal", "sev_info"],
}

# Sync-module alarm panels
SYNC_MODULES: dict[str, str] = {
    "alarm_control_panel.blink_indoor":  "sub_camera_indoor",
    "alarm_control_panel.blink_outdoor": "sub_camera_outdoor",
}

# Housekeeping: retrofit fn_sensor_signal onto bambu wifi (was fn_sensor_status in phase 3d).
#               Strip stray `wi_fi` from irrigation flow_rate (mis-tag from phase 1a era).
BAMBU_WIFI_ENTITY = "sensor.wi_fi_signal_bambu"
FLOW_RATE_STRAY = "sensor.flow_rate_irrigation_tent"

LOOSE_LABELS_TO_STRIP = {"camera", "wi_fi", "battery"}
LOOSE_LABELS_TO_DELETE = {"camera", "wi_fi"}  # `battery` stays alive for phase-3 phone entities


def build_security_cam_entity_map(cam_name: str, sub_label: str) -> dict[str, list[str]]:
    """For a given cam <name>, produce entity_id -> [fn_, sev_] map."""
    # Entity ID patterns Blink uses for non-tent cams:
    #   camera.<name>
    #   binary_sensor.<name>_motion
    #   binary_sensor.<name>_battery
    #   binary_sensor.<name>_camera_armed
    #   switch.<name>_camera_motion_detection
    #   sensor.blink_<name>_temperature
    #   sensor.blink_<name>_wi_fi_signal_strength
    return {
        f"camera.{cam_name}":                              SECURITY_FIELD_RULES["camera"],
        f"binary_sensor.{cam_name}_motion":                SECURITY_FIELD_RULES["motion"],
        f"binary_sensor.{cam_name}_battery":               SECURITY_FIELD_RULES["battery"],
        f"binary_sensor.{cam_name}_camera_armed":          SECURITY_FIELD_RULES["camera_armed"],
        f"switch.{cam_name}_camera_motion_detection":      SECURITY_FIELD_RULES["camera_motion_detection"],
        f"sensor.blink_{cam_name}_temperature":            SECURITY_FIELD_RULES["temperature"],
        f"sensor.blink_{cam_name}_wi_fi_signal_strength":  SECURITY_FIELD_RULES["wi_fi_signal_strength"],
    }


@dataclass
class Plan:
    entity_id: str
    target_labels: list[str]


def compute_plans() -> list[Plan]:
    plans: list[Plan] = []
    # --- Tent cam (indoor + grow) ---
    for eid, rules in TENT_CAM_ENTITIES.items():
        plans.append(Plan(eid, sorted({
            "sys_camera", "sub_camera_indoor", "blink", "grow", *rules,
        })))
    # --- Indoor security cams ---
    for cam in INDOOR_CAMS:
        emap = build_security_cam_entity_map(cam, "sub_camera_indoor")
        for eid, rules in emap.items():
            plans.append(Plan(eid, sorted({
                "sys_camera", "sub_camera_indoor", "blink", *rules,
            })))
    # --- Outdoor security cams ---
    for cam in OUTDOOR_CAMS:
        emap = build_security_cam_entity_map(cam, "sub_camera_outdoor")
        for eid, rules in emap.items():
            plans.append(Plan(eid, sorted({
                "sys_camera", "sub_camera_outdoor", "blink", *rules,
            })))
    # --- Sync module alarm panels ---
    for eid, sub in SYNC_MODULES.items():
        plans.append(Plan(eid, sorted({
            "sys_camera", sub, "blink", "fn_controller", "sev_warning",
        })))
    return plans


async def ws_call(ws, mid, **kw):
    await ws.send(json.dumps({"id": mid, **kw}))
    while True:
        r = json.loads(await ws.recv())
        if r.get("id") == mid:
            return r


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="commit (default: dry-run)")
    args = ap.parse_args()

    plans = compute_plans()

    async with websockets.connect(WS_URL, max_size=None) as ws:
        assert json.loads(await ws.recv())["type"] == "auth_required"
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        assert json.loads(await ws.recv())["type"] == "auth_ok"

        mid = 1
        # 1. Ensure labels exist
        labels_resp = await ws_call(ws, mid, type="config/label_registry/list"); mid += 1
        existing = {l["label_id"]: l for l in labels_resp["result"]}
        for lid, name, color, icon in LABELS_TO_ENSURE:
            if lid in existing:
                print(f"[label] exists: {lid}")
                continue
            print(f"[label] {'WOULD CREATE' if not args.apply else 'CREATE'}: {lid}")
            if args.apply:
                r = await ws_call(ws, mid, type="config/label_registry/create",
                                   name=name, color=color, icon=icon); mid += 1
                if not r.get("success"):
                    print(f"  FAIL: {r}")

        # Refresh labels
        labels_resp = await ws_call(ws, mid, type="config/label_registry/list"); mid += 1
        existing = {l["label_id"]: l for l in labels_resp["result"]}

        # 2. Fetch entity registry
        entities_resp = await ws_call(ws, mid, type="config/entity_registry/list"); mid += 1
        entities = {e["entity_id"]: e for e in entities_resp["result"]}

        # 3. Apply plans (additive merge, strip LOOSE_LABELS_TO_STRIP)
        ok = fail = 0
        for p in plans:
            e = entities.get(p.entity_id)
            if not e:
                print(f"  MISSING: {p.entity_id}")
                fail += 1
                continue
            current = set(e.get("labels") or [])
            # Strip loose labels + any prior sys_/sub_/fn_/sev_ (will be replaced)
            cleaned = {l for l in current
                       if l not in LOOSE_LABELS_TO_STRIP
                       and not l.startswith(("sys_", "sub_", "fn_", "sev_"))}
            new_labels = sorted(cleaned | set(p.target_labels))
            if new_labels == sorted(current):
                print(f"  noop: {p.entity_id}")
                ok += 1
                continue
            print(f"  {'WOULD SET' if not args.apply else 'SET'}: {p.entity_id}  -> {new_labels}")
            if args.apply:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                   entity_id=p.entity_id, labels=new_labels)
                if r.get("success"):
                    ok += 1
                else:
                    print(f"    FAIL: {r}")
                    fail += 1
                mid += 1
            else:
                ok += 1

        # 4. Housekeeping: bambu wifi — add fn_sensor_signal, drop fn_sensor_status, strip wi_fi
        for eid in (BAMBU_WIFI_ENTITY, FLOW_RATE_STRAY):
            e = entities.get(eid)
            if not e:
                print(f"  MISSING housekeeping: {eid}")
                continue
            cur = set(e.get("labels") or [])
            new = set(cur)
            new.discard("wi_fi")
            if eid == BAMBU_WIFI_ENTITY:
                new.discard("fn_sensor_status")
                new.add("fn_sensor_signal")
            new_sorted = sorted(new)
            if new_sorted == sorted(cur):
                print(f"  housekeeping noop: {eid}")
                continue
            print(f"  {'WOULD SET' if not args.apply else 'SET'} housekeeping: {eid}  -> {new_sorted}")
            if args.apply:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                   entity_id=eid, labels=new_sorted)
                if not r.get("success"):
                    print(f"    FAIL: {r}")
                    fail += 1
                else:
                    ok += 1
                mid += 1

        # 5. Delete loose labels (verify 0 holders first)
        if args.apply:
            entities_resp = await ws_call(ws, mid, type="config/entity_registry/list"); mid += 1
            entities_latest = entities_resp["result"]
        else:
            entities_latest = list(entities.values())
        for stale in LOOSE_LABELS_TO_DELETE:
            holders = [e["entity_id"] for e in entities_latest if stale in (e.get("labels") or [])]
            if holders:
                print(f"[label] SKIP delete {stale}: still held by {len(holders)} -> {holders[:5]}")
                continue
            print(f"[label] {'WOULD DELETE' if not args.apply else 'DELETE'}: {stale}")
            if args.apply and stale in existing:
                r = await ws_call(ws, mid, type="config/label_registry/delete", label_id=stale)
                if not r.get("success"):
                    print(f"  FAIL: {r}")
                mid += 1

        print(f"\nResult: {ok} OK, {fail} FAIL, {len(plans)} plans + 2 housekeeping")
        if not args.apply:
            print("DRY-RUN — re-run with --apply to commit.")


if __name__ == "__main__":
    asyncio.run(main())
