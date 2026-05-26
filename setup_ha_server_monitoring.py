"""Bootstrap HA host-health monitoring.

- Creates area 'HA Server' if missing.
- Creates label 'sys_infrastructure' if missing.
- Enables the 5 systemmonitor sensors we care about.
- Tags each enabled sensor with area + sys_infrastructure + grow (NO — grow is
  grow-scope) + sev_* per the tagging standard.

Note: systemmonitor sensors are simple system-telemetry percentages — they
don't map cleanly to any existing `fn_sensor_*` bucket, so `fn_` is omitted
(same exception used for aggregated template sensors like VPD/DLI).

Idempotent. Dry-run by default; pass --apply to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

NEW_AREA_ID = "ha_server"
NEW_AREA_NAME = "HA Server"

NEW_LABEL_ID = "sys_infrastructure"
NEW_LABEL_NAME = "sys_infrastructure"

# systemmonitor naming: `_usage` = percent, `_use` = absolute (GiB/MiB) —
# EXCEPT `processor_use` which is %. Inconsistent in the integration.
# entity_id -> sev label
SENSORS: dict[str, str] = {
    "sensor.system_monitor_disk_usage_config": "sev_critical",
    "sensor.system_monitor_memory_usage":      "sev_critical",
    "sensor.system_monitor_swap_usage":        "sev_warning",
    "sensor.system_monitor_processor_use":     "sev_warning",
    "sensor.system_monitor_load_15_min":       "sev_warning",
    # command_line sensor declared in packages/system/host_health.yaml
    "sensor.ha_database_size":                 "sev_warning",
    # version + template-binary sensors declared in packages/system/updates.yaml
    "sensor.ha_core_running":                  "sev_info",
    "sensor.ha_core_latest":                   "sev_warning",
    "binary_sensor.ha_core_update_available":  "sev_warning",
}

# Mistakenly enabled in an earlier pass — these are absolute (GiB/MiB), not %.
# Re-disable so the entity list stays tidy.
SENSORS_TO_DISABLE = [
    "sensor.system_monitor_disk_use_config",
    "sensor.system_monitor_memory_use",
    "sensor.system_monitor_swap_use",
]


async def ws_call(ws, mid, **kw):
    await ws.send(json.dumps({"id": mid, **kw}))
    while True:
        r = json.loads(await ws.recv())
        if r.get("id") == mid:
            return r


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    async with websockets.connect(WS_URL, max_size=None) as ws:
        assert json.loads(await ws.recv())["type"] == "auth_required"
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        assert json.loads(await ws.recv())["type"] == "auth_ok"

        mid = 1

        # --- AREA ---
        areas = (await ws_call(ws, mid, type="config/area_registry/list"))["result"]; mid += 1
        area_ids = {a["area_id"] for a in areas}
        if NEW_AREA_ID in area_ids:
            print(f"area: {NEW_AREA_ID!r} exists")
        else:
            print(f"area: {'WOULD CREATE' if not args.apply else 'CREATE'} {NEW_AREA_ID!r} ({NEW_AREA_NAME!r})")
            if args.apply:
                r = await ws_call(ws, mid, type="config/area_registry/create",
                                  name=NEW_AREA_NAME); mid += 1
                if not r.get("success"):
                    print(f"  FAIL: {r}"); return 1
                # Re-fetch in case HA generated a different area_id from the name
                areas = (await ws_call(ws, mid, type="config/area_registry/list"))["result"]; mid += 1
                created = next((a for a in areas if a["name"] == NEW_AREA_NAME), None)
                if created and created["area_id"] != NEW_AREA_ID:
                    print(f"  note: HA assigned area_id {created['area_id']!r} (not {NEW_AREA_ID!r}); using its value")

        # Refresh and resolve effective area_id
        areas = (await ws_call(ws, mid, type="config/area_registry/list"))["result"]; mid += 1
        target_area = next((a for a in areas if a["name"] == NEW_AREA_NAME), None)
        target_area_id = target_area["area_id"] if target_area else (NEW_AREA_ID if not args.apply else None)
        if args.apply and target_area_id is None:
            print(f"FAIL: could not resolve area for {NEW_AREA_NAME!r}"); return 1

        # --- LABEL ---
        labels = (await ws_call(ws, mid, type="config/label_registry/list"))["result"]; mid += 1
        label_ids = {l["label_id"] for l in labels}
        if NEW_LABEL_ID in label_ids:
            print(f"label: {NEW_LABEL_ID!r} exists")
        else:
            print(f"label: {'WOULD CREATE' if not args.apply else 'CREATE'} {NEW_LABEL_ID!r}")
            if args.apply:
                r = await ws_call(ws, mid, type="config/label_registry/create",
                                  name=NEW_LABEL_NAME); mid += 1
                if not r.get("success"):
                    print(f"  FAIL: {r}"); return 1

        # --- SENSORS: enable + tag ---
        entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
        ent_map = {e["entity_id"]: e for e in entities}

        for eid, sev in SENSORS.items():
            e = ent_map.get(eid)
            if not e:
                print(f"  MISSING: {eid}"); continue

            updates: dict = {}
            if e.get("disabled_by") is not None:
                updates["disabled_by"] = None
            target_labels = sorted(set(e.get("labels") or []) | {NEW_LABEL_ID, sev})
            if target_labels != sorted(e.get("labels") or []):
                updates["labels"] = target_labels
            if e.get("area_id") != target_area_id:
                updates["area_id"] = target_area_id

            if not updates:
                print(f"  noop: {eid}")
                continue

            print(f"  {'WOULD UPDATE' if not args.apply else 'UPDATE'}: {eid}")
            for k, v in updates.items():
                print(f"    {k}: {e.get(k)!r} -> {v!r}")

            if args.apply:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                  entity_id=eid, **updates); mid += 1
                if not r.get("success"):
                    print(f"    FAIL: {r}")

        # --- DISABLE wrong-pass sensors ---
        for eid in SENSORS_TO_DISABLE:
            e = ent_map.get(eid)
            if not e:
                continue
            if e.get("disabled_by") is not None:
                print(f"  noop (already disabled): {eid}")
                continue
            # Strip tags too — they don't belong on a disabled sensor we're
            # walking back.
            updates = {"disabled_by": "user", "labels": [], "area_id": None}
            print(f"  {'WOULD DISABLE' if not args.apply else 'DISABLE'}: {eid}")
            if args.apply:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                  entity_id=eid, **updates); mid += 1
                if not r.get("success"):
                    print(f"    FAIL: {r}")

        if not args.apply:
            print("\nDRY-RUN — re-run with --apply to commit.")
        return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
