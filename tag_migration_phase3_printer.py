"""Phase 3 (3D printer sub-phase) — tag Bambu P1S + related Kasa/integration/spool.

Creates: sys_printer, fn_camera, fn_sensor_status (new home-wide labels).
Keeps:   bambu (brand cross-cutter), camera (still needed by phase-2 tent-cam entities).
Strips:  3d_printer from every entity; camera from the 3 printer cam entities.
Deletes: 3d_printer label (redundant with sys_printer).
Areas:   moves printer devices into area_id='3d_printer' ('3D Printer').

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

AREA_ID = "3d_printer"

LABELS_TO_ENSURE = [
    ("sys_printer",       "sys_printer",       "deep-purple", "mdi:printer-3d"),
    ("fn_camera",         "fn_camera",         "indigo",      "mdi:cctv"),
    ("fn_sensor_status",  "fn_sensor_status",  "grey",        "mdi:information-outline"),
    ("prusa",             "prusa",             "orange",      "mdi:printer-3d-nozzle-alert"),
]

# Entity IDs belonging to the Prusa printer (currently just the Kasa plug — Prusa not yet wired)
PRUSA_ENTITIES = {
    "switch.prusa", "sensor.current_prusa", "sensor.power_prusa", "sensor.voltage_prusa",
}

# Devices whose entire entity set should end up in area "3D Printer"
PRINTER_DEVICE_NAME_PREFIXES = [
    "P1S_",                 # P1S_01P09C470802548 and its ExternalSpool sibling
    "Bambu Lab",            # integration device
]
# Individual Kasa plug powering the printer (identified by entity on the device)
KASA_BAMBU_ENTITIES = {"switch.bambu", "update.firmware_2_p1s"}

OLD_LABELS_TO_STRIP_GLOBAL = {"3d_printer"}   # from every entity that has it
# `camera` label stripped ONLY from these 3 printer entities (leave it on tent-cam entities for phase 2)
CAMERA_LABEL_STRIP_FROM = {
    "camera.camera_p1s", "switch.enable_camera_p1s", "switch.use_image_sensor_camera_p1s",
}

BAMBU_BASE = ["sys_printer", "bambu"]
PRUSA_BASE = ["sys_printer", "prusa"]


@dataclass
class Rule:
    eids: set[str]
    extra: list[str]  # fn_* + sev_* (BASE added automatically)


# First match wins. Any printer entity not hit by a rule falls through to STATUS_DEFAULT.
RULES: list[Rule] = [
    # --- Prusa (Kasa outlet — printer not yet wired, but outlet is live) ---
    Rule({"switch.prusa"}, ["fn_controller", "sev_critical"]),
    Rule({"sensor.current_prusa", "sensor.power_prusa", "sensor.voltage_prusa"},
         ["fn_power_meter", "sev_info"]),
    # --- Print controls (critical safety) ---
    Rule({"button.pause_printing_p1s", "button.resume_printing_p1s", "button.stop_printing_p1s"},
         ["fn_controller", "sev_critical"]),
    Rule({"switch.bambu"}, ["fn_controller", "sev_critical"]),  # main power outlet

    # --- Error/diagnostic binary sensors (critical) ---
    Rule({"binary_sensor.hms_errors_p1s", "binary_sensor.print_error_p1s"},
         ["fn_sensor_status", "sev_critical"]),

    # --- Temperatures ---
    Rule({"sensor.bed_temperature_p1s", "sensor.nozzle_temperature_p1s"},
         ["fn_sensor_temp", "sev_warning"]),  # runaway = fire risk
    Rule({"sensor.bed_target_temperature_p1s", "sensor.nozzle_target_temperature_p1s"},
         ["fn_sensor_temp", "sev_info"]),
    Rule({"number.bed_target_temperature_p1s", "number.nozzle_target_temperature_p1s"},
         ["fn_controller", "sev_warning"]),  # wrong setpoint = damage

    # --- Fans ---
    Rule({"sensor.heatbreak_fan_speed_p1s"},
         ["fn_fan", "sev_warning"]),  # heatbreak fan failure → nozzle damage
    Rule({"fan.cooling_fan_p1s", "sensor.cooling_fan_speed_p1s"},
         ["fn_fan", "sev_info"]),

    # --- Light ---
    Rule({"light.chamber_light_p1s"}, ["fn_light", "sev_info"]),

    # --- Camera ---
    Rule({"camera.camera_p1s"}, ["fn_camera", "sev_info"]),
    Rule({"switch.enable_camera_p1s", "switch.use_image_sensor_camera_p1s"},
         ["fn_camera", "sev_info"]),

    # --- Misc controllers ---
    Rule({"button.force_refresh_data_p1s", "select.printing_speed_p1s",
          "switch.bambu_lab_pre_release"},
         ["fn_controller", "sev_info"]),

    # --- Status binary sensors (non-critical flags) ---
    Rule({"binary_sensor.online_p1s"},
         ["fn_sensor_status", "sev_warning"]),
    Rule({"binary_sensor.firmware_update_p1s"},
         ["fn_sensor_status", "sev_warning"]),
    Rule({"binary_sensor.developer_lan_mode_p1s",
          "binary_sensor.extruder_filament_state_p1s",
          "binary_sensor.hybrid_mqtt_blocks_control_p1s",
          "binary_sensor.mqtt_encryption_firmware_p1s",
          "binary_sensor.recording_timelapse_p1s",
          "binary_sensor.externalspool_active_p1s"},
         ["fn_sensor_status", "sev_info"]),

    # --- Update entities ---
    Rule({"update.firmware_2_p1s"}, ["fn_sensor_status", "sev_warning"]),
    Rule({"update.bambu_lab_update"}, ["fn_sensor_status", "sev_info"]),

    # --- Wi-Fi signal ---
    Rule({"sensor.wi_fi_signal_bambu"}, ["fn_sensor_status", "sev_info"]),

    # --- Automations (no fn_) ---
    Rule({"automation.bambu_light_on_power", "automation.bambu_turn_off_after_print"},
         ["sev_info"]),
]

# Fallback for any printer-scoped entity not covered above — catch-all telemetry.
STATUS_DEFAULT = ["fn_sensor_status", "sev_info"]


async def ws_call(ws, mid, **kw):
    await ws.send(json.dumps({"id": mid, **kw}))
    while True:
        r = json.loads(await ws.recv())
        if r.get("id") == mid:
            return r


def in_scope(entity, device_by_id) -> bool:
    eid = entity["entity_id"]
    if eid in KASA_BAMBU_ENTITIES or eid in PRUSA_ENTITIES:
        return True
    if eid in {"automation.bambu_light_on_power", "automation.bambu_turn_off_after_print"}:
        return True
    did = entity.get("device_id")
    if did and did in device_by_id:
        dname = device_by_id[did].get("name") or ""
        if any(dname.startswith(p) for p in PRINTER_DEVICE_NAME_PREFIXES):
            return True
    # Already-labeled printer entities (belt-and-suspenders — catch anything with 3d_printer/bambu)
    labels = entity.get("labels") or []
    if "3d_printer" in labels or ("bambu" in labels and not eid.startswith("binary_sensor.sm_")):
        return True
    return False


def labels_for(eid: str) -> list[str] | None:
    for r in RULES:
        if eid in r.eids:
            return r.extra
    return None


async def main(apply: bool):
    async with websockets.connect(WS_URL, max_size=None) as ws:
        assert json.loads(await ws.recv())["type"] == "auth_required"
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        assert json.loads(await ws.recv())["type"] == "auth_ok"

        mid = 0
        def nid(): nonlocal mid; mid += 1; return mid

        ents   = (await ws_call(ws, nid(), type="config/entity_registry/list"))["result"]
        labels = (await ws_call(ws, nid(), type="config/label_registry/list"))["result"]
        devs   = (await ws_call(ws, nid(), type="config/device_registry/list"))["result"]
        areas  = (await ws_call(ws, nid(), type="config/area_registry/list"))["result"]

        existing_labels = {l["label_id"] for l in labels}
        dev_by_id = {d["id"]: d for d in devs}
        area_ids = {a["area_id"] for a in areas}
        assert AREA_ID in area_ids, f"area {AREA_ID!r} missing"

        # === 1. Label creation plan ===
        to_create = [L for L in LABELS_TO_ENSURE if L[0] not in existing_labels]
        print(f"=== LABELS TO CREATE: {len(to_create)} ===")
        for lid, nm, col, ic in to_create:
            print(f"  + {lid:22s}  {col}  {ic}")

        # === 2. In-scope entities and their plans ===
        scope_ents = [e for e in ents if in_scope(e, dev_by_id)]
        entity_plan = []          # (eid, cur, new)
        unmatched = []            # no rule → fell through to STATUS_DEFAULT
        for e in scope_ents:
            eid = e["entity_id"]
            cur = list(e.get("labels") or [])
            new = list(cur)

            # strip legacy labels
            new = [L for L in new if L not in OLD_LABELS_TO_STRIP_GLOBAL]
            if eid in CAMERA_LABEL_STRIP_FROM:
                new = [L for L in new if L != "camera"]
            # Prusa entities were historically mis-labeled `bambu` — strip it
            if eid in PRUSA_ENTITIES:
                new = [L for L in new if L != "bambu"]

            # Add base + rule labels
            rule = labels_for(eid)
            if rule is None:
                rule = STATUS_DEFAULT
                unmatched.append(eid)
            base = PRUSA_BASE if eid in PRUSA_ENTITIES else BAMBU_BASE
            for L in base + rule:
                if L not in new:
                    new.append(L)

            if sorted(new) != sorted(cur):
                entity_plan.append((eid, cur, new))

        print(f"\n=== ENTITY PLANS (in-scope: {len(scope_ents)}, changing: {len(entity_plan)}) ===")
        for eid, cl, nl in sorted(entity_plan):
            added = [L for L in nl if L not in cl]
            removed = [L for L in cl if L not in nl]
            parts = []
            if added: parts.append(f"+{added}")
            if removed: parts.append(f"-{removed}")
            print(f"  {eid:60s}  {' '.join(parts)}")

        if unmatched:
            print(f"\n=== UNMATCHED (got STATUS_DEFAULT fallback): {len(unmatched)} ===")
            for eid in sorted(unmatched):
                print(f"  ? {eid}")

        # === 3. Device area moves ===
        device_moves = []
        for d in devs:
            dname = d.get("name") or ""
            if any(dname.startswith(p) for p in PRINTER_DEVICE_NAME_PREFIXES):
                if d.get("area_id") != AREA_ID:
                    device_moves.append((d["id"], dname, d.get("area_id"), AREA_ID))
        # Kasa plugs powering printers — identify by checking which device owns bambu/prusa entities
        kasa_dev_ids = {e.get("device_id") for e in ents
                        if (e["entity_id"] in KASA_BAMBU_ENTITIES or e["entity_id"] in PRUSA_ENTITIES)
                        and e.get("device_id")}
        for did in kasa_dev_ids:
            d = dev_by_id.get(did)
            if d and d.get("area_id") != AREA_ID:
                device_moves.append((did, d.get("name") or "(kasa plug)", d.get("area_id"), AREA_ID))

        print(f"\n=== DEVICE AREA MOVES: {len(device_moves)} ===")
        for did, dn, old, new in device_moves:
            print(f"  {dn:45s}  area: {old!r:12s} -> {new!r}")

        # === 4. Label deletions ===
        to_delete = [L for L in OLD_LABELS_TO_STRIP_GLOBAL if L in existing_labels]
        print(f"\n=== LABELS TO DELETE: {len(to_delete)} ===")
        for L in to_delete:
            print(f"  - {L}")

        if not apply:
            print("\n=== DRY RUN — re-run with --apply to commit. ===")
            return

        print("\n====== APPLYING ======\n")
        for lid, nm, col, ic in to_create:
            r = await ws_call(ws, nid(), type="config/label_registry/create",
                              name=nm, color=col, icon=ic)
            print(f"  create label {lid}: {'OK' if r.get('success') else r}")

        for did, dn, old, new in device_moves:
            r = await ws_call(ws, nid(), type="config/device_registry/update",
                              device_id=did, area_id=new)
            print(f"  move device {dn}: {'OK' if r.get('success') else r}")

        ok = fail = 0
        for eid, cl, nl in entity_plan:
            r = await ws_call(ws, nid(), type="config/entity_registry/update",
                              entity_id=eid, labels=nl)
            if r.get("success"): ok += 1
            else:
                fail += 1
                print(f"  FAIL {eid}: {r}")
        print(f"\n  entity updates: {ok} OK, {fail} FAIL")

        for L in to_delete:
            r = await ws_call(ws, nid(), type="config/label_registry/delete", label_id=L)
            print(f"  delete label '{L}': {'OK' if r.get('success') else r}")

        print("\n=== APPLY COMPLETE ===")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    asyncio.run(main(args.apply))
