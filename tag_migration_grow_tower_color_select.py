"""Grow Tower — rename + label the "Medium Alert Color" select entity (2026-07-16).

Background:
  Replaced the 3 separate yellow R/G/B `number` sliders with a single `select`
  entity offering named color presets (Yellow/Orange/Green/Blue) for the MEDIUM
  alert. On reflash it landed with the usual `front_sunroom_` area-prefix quirk:

    select.front_sunroom_grow_tower_medium_alert_color

This script (idempotent, dry-run by default):
  1. Renames the entity_id, stripping the `front_sunroom_` prefix.
  2. Applies the same tagging-standard labels used for the other LED-tuning
     entities: `sys_lighting` + `sev_info` + `grow` (no `fn_` — pure dashboard
     tuning value, same carve-out as the number entities in
     tag_migration_grow_tower_led_numbers.py).

Run `python registry_export.py --label pre-grow-tower-color-select` first for a snapshot.

Dry-run by default. Pass `--apply` to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

OLD_EID = "select.front_sunroom_grow_tower_medium_alert_color"
NEW_EID = "select.grow_tower_medium_alert_color"
TARGET_LABELS = ["sys_lighting", "sev_info", "grow"]


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

        labels = (await ws_call(ws, mid, type="config/label_registry/list"))["result"]; mid += 1
        existing = {l["label_id"] for l in labels}
        missing = set(TARGET_LABELS) - existing
        if missing:
            print(f"ABORT: missing labels in registry: {sorted(missing)}")
            return

        entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
        ent_by_id = {e["entity_id"]: e for e in entities}

        # 1. Rename
        if OLD_EID not in ent_by_id and NEW_EID in ent_by_id:
            print(f"  noop (already renamed): {NEW_EID}")
        elif OLD_EID not in ent_by_id:
            print(f"  MISSING: {OLD_EID} (and no {NEW_EID})")
            return
        else:
            print(f"  {'WOULD RENAME' if not do else 'RENAME'}: {OLD_EID} -> {NEW_EID}")
            if do:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                  entity_id=OLD_EID, new_entity_id=NEW_EID); mid += 1
                if not r.get("success"):
                    print(f"    FAIL: {r}")
                    return

        if do:
            entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
            ent_by_id = {e["entity_id"]: e for e in entities}

        # 2. Label
        e = ent_by_id.get(NEW_EID)
        if not e:
            print(f"  MISSING entity (rename not applied yet?): {NEW_EID}")
            return
        cur = set(e.get("labels") or [])
        if cur == set(TARGET_LABELS):
            print(f"  noop (already labeled): {NEW_EID}")
        else:
            print(f"  {'WOULD LABEL' if not do else 'LABEL'}: {NEW_EID} -> {sorted(TARGET_LABELS)}")
            if do:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                  entity_id=NEW_EID, labels=sorted(TARGET_LABELS)); mid += 1
                if not r.get("success"):
                    print(f"    FAIL: {r}")

        if not do:
            print("DRY-RUN — re-run with --apply to commit.")


if __name__ == "__main__":
    asyncio.run(main())
