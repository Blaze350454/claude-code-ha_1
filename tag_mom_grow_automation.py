"""Tag + area the Mom Grow Lights helpers + automations post-reload.

Adds sys_lighting + grow + sev_ labels to the 8 new entities and moves them
into the mom_grow area. Dry-run by default; --apply to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

AREA_ID = "mom_grow"

# (entity_id, [labels...])  — helpers + automations, no fn_
PLANS: list[tuple[str, list[str]]] = [
    # Helpers
    ("input_datetime.mom_grow_lights_on_time",
     ["sys_lighting", "grow", "sev_info"]),
    ("input_datetime.mom_grow_lights_off_time",
     ["sys_lighting", "grow", "sev_info"]),
    ("input_boolean.mom_grow_lights_automation_enabled",
     ["sys_lighting", "grow", "sev_info"]),
    ("input_boolean.mom_grow_lights_enforce_fail",
     ["sys_lighting", "grow", "sev_warning"]),

    # Automations
    ("automation.mom_grow_lights_scheduler",
     ["sys_lighting", "grow", "sev_critical"]),
    ("automation.mom_grow_lights_offline_alert",
     ["sys_lighting", "grow", "sev_warning"]),
    ("automation.mom_grow_lights_back_online",
     ["sys_lighting", "grow", "sev_info"]),
    ("automation.mom_grow_lights_plug_overheated",
     ["sys_lighting", "grow", "sev_critical"]),
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
    do = args.apply

    async with websockets.connect(WS_URL, max_size=None) as ws:
        assert json.loads(await ws.recv())["type"] == "auth_required"
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        assert json.loads(await ws.recv())["type"] == "auth_ok"

        mid = 1
        entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
        ent = {e["entity_id"]: e for e in entities}

        ok = fail = 0
        for eid, labels in PLANS:
            e = ent.get(eid)
            if not e:
                print(f"  MISSING: {eid}")
                fail += 1
                continue
            cur_labels = sorted(e.get("labels") or [])
            cur_area = e.get("area_id")
            want_labels = sorted(labels)
            needs_label = cur_labels != want_labels
            needs_area = cur_area != AREA_ID
            if not (needs_label or needs_area):
                print(f"  noop: {eid}")
                ok += 1
                continue

            change = []
            if needs_label: change.append(f"labels {cur_labels} -> {want_labels}")
            if needs_area:  change.append(f"area '{cur_area}' -> '{AREA_ID}'")
            print(f"  {'WOULD' if not do else 'APPLY'}: {eid}  ::  {'; '.join(change)}")

            if do:
                payload = {"type": "config/entity_registry/update", "entity_id": eid}
                if needs_label: payload["labels"] = want_labels
                if needs_area:  payload["area_id"] = AREA_ID
                r = await ws_call(ws, mid, **payload); mid += 1
                if r.get("success"):
                    ok += 1
                else:
                    fail += 1
                    print(f"    FAIL: {r}")
            else:
                ok += 1

        print(f"\nResult: {ok} OK, {fail} FAIL (of {len(PLANS)} plans)")
        if not do:
            print("DRY-RUN — re-run with --apply to commit.")


if __name__ == "__main__":
    asyncio.run(main())
