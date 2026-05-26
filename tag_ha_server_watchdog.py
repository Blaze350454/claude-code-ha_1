"""Tag HA host watchdog automations.

Applies area + labels per the tagging standard:
  area_id: ha_server
  labels:  sys_infrastructure, sev_critical

Watchdog automations get sev_critical per the standard
(Watchdog / safety-lock / emergency-kill → sev_critical).

Idempotent. Dry-run by default; pass --apply to commit.

Prereq: packages/system/host_health.yaml deployed + HA reloaded.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

TARGET_AREA = "ha_server"
# automation_entity_id -> sev label (severity per the tagging standard:
# Watchdog/safety/emergency-kill = sev_critical; informational digest = sev_warning).
TARGET_AUTOMATIONS: dict[str, str] = {
    "automation.watchdog_ha_host_resource_pressure":     "sev_critical",
    "automation.watchdog_ha_backup_database_health":     "sev_critical",
    "automation.watchdog_ha_updates_daily_digest":       "sev_warning",
    "automation.watchdog_ha_started":                    "sev_warning",
    "automation.watchdog_external_heartbeat_healthchecks_io": "sev_warning",
}


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

        any_missing = False
        for target, sev in TARGET_AUTOMATIONS.items():
            e = ent_map.get(target)
            if not e:
                print(f"MISSING: {target} not in entity registry.")
                for eid in sorted(ent_map):
                    if "watchdog_ha" in eid:
                        print(f"  candidate: {eid}")
                any_missing = True
                continue

            target_labels = {"sys_infrastructure", sev}
            cur_area = e.get("area_id")
            cur_labels = set(e.get("labels") or [])
            new_labels = sorted(cur_labels | target_labels)

            updates: dict = {}
            if cur_area != TARGET_AREA:
                updates["area_id"] = TARGET_AREA
            if sorted(cur_labels) != new_labels:
                updates["labels"] = new_labels

            if not updates:
                print(f"noop: {target} already has area={cur_area}, labels={sorted(cur_labels)}")
                continue

            print(f"{'WOULD SET' if not args.apply else 'SET'}: {target}")
            if "area_id" in updates:
                print(f"  area_id: {cur_area!r} -> {updates['area_id']!r}")
            if "labels" in updates:
                print(f"  labels:  {sorted(cur_labels)} -> {updates['labels']}")

            if args.apply:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                  entity_id=target, **updates); mid += 1
                if not r.get("success"):
                    print(f"  FAIL: {r}")

        if not args.apply:
            print("\nDRY-RUN — re-run with --apply to commit.")
        return 1 if any_missing else 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
