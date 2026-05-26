"""Tag the irrigation critical-offline watchdog automation.

Applies area + labels to `automation.watchdog_irrigation_critical_offline`
per the v1 tagging standard:
  area_id: tent
  labels:  sys_irrigation, sev_critical, grow

Idempotent. Dry-run by default; pass `--apply` to commit.

Prereq: the YAML at grow_tent_automation/automations/watchdog_critical_offline.yaml
must be deployed and HA must have reloaded automations so the entity exists in
the registry. The script verifies presence before attempting any update.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

TARGET_ENTITY = "automation.watchdog_irrigation_critical_device_offline"
TARGET_AREA = "tent"
TARGET_LABELS = {"sys_irrigation", "sev_critical", "grow"}


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
        entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
        ent_map = {e["entity_id"]: e for e in entities}

        e = ent_map.get(TARGET_ENTITY)
        if not e:
            print(f"MISSING: {TARGET_ENTITY} not in entity registry.")
            print("  Deploy the YAML and reload automations first.")
            return 1

        areas = (await ws_call(ws, mid, type="config/area_registry/list"))["result"]; mid += 1
        area_ids = {a["area_id"] for a in areas}
        if TARGET_AREA not in area_ids:
            print(f"MISSING: area '{TARGET_AREA}' not in area registry.")
            return 1

        labels = (await ws_call(ws, mid, type="config/label_registry/list"))["result"]; mid += 1
        label_ids = {l["label_id"] for l in labels}
        missing_labels = TARGET_LABELS - label_ids
        if missing_labels:
            print(f"MISSING labels: {sorted(missing_labels)}")
            print("  These should already exist from phase 1a/1b. Re-check tagging_standard.md.")
            return 1

        cur_area = e.get("area_id")
        cur_labels = set(e.get("labels") or [])
        new_labels = sorted(cur_labels | TARGET_LABELS)

        updates: dict = {}
        if cur_area != TARGET_AREA:
            updates["area_id"] = TARGET_AREA
        if sorted(cur_labels) != new_labels:
            updates["labels"] = new_labels

        if not updates:
            print(f"noop: {TARGET_ENTITY} already has area={cur_area}, labels={sorted(cur_labels)}")
            return 0

        print(f"{'WOULD SET' if not args.apply else 'SET'}: {TARGET_ENTITY}")
        if "area_id" in updates:
            print(f"  area_id: {cur_area!r} -> {updates['area_id']!r}")
        if "labels" in updates:
            print(f"  labels:  {sorted(cur_labels)} -> {updates['labels']}")

        if args.apply:
            r = await ws_call(ws, mid, type="config/entity_registry/update",
                              entity_id=TARGET_ENTITY, **updates); mid += 1
            if not r.get("success"):
                print(f"FAIL: {r}")
                return 1
            print("OK")
        else:
            print("DRY-RUN — re-run with --apply to commit.")
        return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
