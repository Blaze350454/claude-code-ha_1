"""Grow Tower — rename + label the LED testing controls (2026-07-16).

Background:
  Added a master "Aesthetic Enabled" switch (disables the automatic idle
  breathe/restore so manual test presses aren't fought) and 4 "Preview <Color>"
  buttons (force the LED to a named color right now, for eyeballing/tuning the
  Color* text values). On reflash they landed with the usual `front_sunroom_`
  area-prefix quirk:

    switch.front_sunroom_grow_tower_aesthetic_enabled
    button.front_sunroom_grow_tower_preview_yellow
    button.front_sunroom_grow_tower_preview_orange
    button.front_sunroom_grow_tower_preview_green
    button.front_sunroom_grow_tower_preview_blue

This script (idempotent, dry-run by default):
  1. Renames the 5 entity_ids, stripping the `front_sunroom_` prefix.
  2. Applies the same tagging-standard labels used for the other LED-tuning
     entities: `sys_lighting` + `sev_info` + `grow` (no `fn_` — testing/config
     controls, not a physical device function, same carve-out as the
     number/select/text LED-tuning entities).

Run `python registry_export.py --label pre-grow-tower-led-testing-controls` first.

Dry-run by default. Pass `--apply` to commit.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

RENAMES: list[tuple[str, str]] = [
    ("switch.front_sunroom_grow_tower_aesthetic_enabled", "switch.grow_tower_aesthetic_enabled"),
    ("button.front_sunroom_grow_tower_preview_yellow", "button.grow_tower_preview_yellow"),
    ("button.front_sunroom_grow_tower_preview_orange", "button.grow_tower_preview_orange"),
    ("button.front_sunroom_grow_tower_preview_green", "button.grow_tower_preview_green"),
    ("button.front_sunroom_grow_tower_preview_blue", "button.grow_tower_preview_blue"),
]

TARGET_LABELS = ["sys_lighting", "sev_info", "grow"]
PLANS: list[tuple[str, list[str]]] = [(new, TARGET_LABELS) for _, new in RENAMES]


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

        ok = fail = 0
        for old_eid, new_eid in RENAMES:
            if old_eid not in ent_by_id and new_eid in ent_by_id:
                print(f"  noop (already renamed): {new_eid}")
                ok += 1
                continue
            if old_eid not in ent_by_id:
                print(f"  MISSING: {old_eid} (and no {new_eid})")
                fail += 1
                continue
            print(f"  {'WOULD RENAME' if not do else 'RENAME'}: {old_eid} -> {new_eid}")
            if do:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                  entity_id=old_eid, new_entity_id=new_eid); mid += 1
                if r.get("success"): ok += 1
                else: fail += 1; print(f"    FAIL: {r}")
            else:
                ok += 1

        print(f"\nRename result: {ok} OK, {fail} FAIL (of {len(RENAMES)})")

        if do:
            entities = (await ws_call(ws, mid, type="config/entity_registry/list"))["result"]; mid += 1
            ent_by_id = {e["entity_id"]: e for e in entities}

        ok = fail = 0
        for eid, target in PLANS:
            e = ent_by_id.get(eid)
            if not e:
                print(f"  MISSING entity (rename not applied yet?): {eid}")
                fail += 1
                continue
            cur = set(e.get("labels") or [])
            if cur == set(target):
                print(f"  noop (already labeled): {eid}")
                ok += 1
                continue
            print(f"  {'WOULD LABEL' if not do else 'LABEL'}: {eid} -> {sorted(target)}")
            if do:
                r = await ws_call(ws, mid, type="config/entity_registry/update",
                                  entity_id=eid, labels=sorted(target)); mid += 1
                if r.get("success"): ok += 1
                else: fail += 1; print(f"    FAIL: {r}")
            else:
                ok += 1

        print(f"\nLabel result: {ok} OK, {fail} FAIL (of {len(PLANS)})")
        if not do:
            print("DRY-RUN — re-run with --apply to commit.")


if __name__ == "__main__":
    asyncio.run(main())
