"""Add tent + tower alert banners to the Mom dashboard, and fix the broken
tower water-level tile card.

Storage-mode dashboard (dashboard-mom) — no YAML file, edited live via the
WS API. Mirrors add_res_dry_banner.py's backup-then-save workflow (used for
dashboard-tent), applied here to dashboard-mom instead.

Steps:
  1. Fetch current dashboard-mom config, write a timestamped backup JSON.
  2. Insert a new first section ("Alerts") containing:
       - a byte-identical copy of tent's own alert-banner card (still
         pointed at binary_sensor.tent_alert_banner etc. — tent keeps its
         own dashboard-tent copy too; this is additive, not a move).
       - the new tower alert-banner card (binary_sensor.tower_alert_banner,
         sensor.tower_error_list, script.tower_alert_snooze).
  3. In the existing tower section, replace the broken
       {"type": "tile", "entity": "binary_sensor.grow_tower_water_level"}
     with 3 tile cards for the real low/medium/high entities.
  4. Save via lovelace/config/save.

Idempotent: re-running after a successful --apply is a no-op (detects the
banners/tiles are already present). Dry-run by default; --apply to write.
"""
from __future__ import annotations
import argparse, asyncio, json, pathlib, datetime
import websockets

HERE = pathlib.Path(__file__).parent
cfg = json.loads((HERE / ".cursor" / "mcp.json").read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]; HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

URL_PATH = "dashboard-mom"

TENT_ALERT_BANNER = {
    "type": "conditional",
    "conditions": [
        {"condition": "state", "entity": "binary_sensor.tent_alert_banner", "state": "on"}
    ],
    "grid_options": {"columns": "full"},
    "card": {
        "type": "vertical-stack",
        "cards": [
            {
                "type": "markdown",
                "content": "# ERROR !!\n###### {{ (state_attr('sensor.tent_error_list','errors') or []) | count }} active",
                "card_mod": {
                    "style": {
                        ".": "ha-card {\n  border: none;\n  min-height: 130px;\n  position: relative;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  animation: errbg 1.8s ease-in-out infinite;\n}\n@keyframes errbg {0%,100%{background:#c00000;}50%{background:#000000;}}\n",
                        "ha-markdown$": "h1 {\n  text-align: center;\n  font-size: 4em;\n  font-weight: 900;\n  letter-spacing: 6px;\n  margin: 0;\n  animation: errtx 1.8s ease-in-out infinite;\n}\nh6 {\n  position: absolute;\n  left: 16px;\n  bottom: 8px;\n  margin: 0;\n  font-size: 1em;\n  font-weight: 700;\n  animation: errtx 1.8s ease-in-out infinite;\n}\n@keyframes errtx {0%,100%{color:#000000;}50%{color:#ff3030;}}\n",
                    }
                },
            },
            {
                "type": "markdown",
                "content": "{% for e in (state_attr('sensor.tent_error_list','errors') or []) %}\n- **{{ e.msg }}**\n{% endfor %}",
            },
            {
                "type": "horizontal-stack",
                "cards": [
                    {
                        "type": "entities",
                        "entities": [{"entity": "input_select.tent_alert_snooze_duration", "name": "Snooze"}],
                        "card_mod": {"style": "ha-card{box-shadow:none;background:none;border:none;}\n#states{padding:0 8px;}\n.card-content{padding:4px 8px !important;}\n"},
                    },
                    {
                        "type": "button",
                        "name": "DISABLE",
                        "show_icon": False,
                        "show_state": False,
                        "tap_action": {"action": "perform-action", "perform_action": "script.tent_alert_snooze"},
                        "card_mod": {"style": "ha-card{min-height:0;height:100%;display:flex;align-items:center;justify-content:center;font-weight:700;}\n.button{padding:6px !important;}\n"},
                    },
                ],
            },
        ],
    },
}

TOWER_ALERT_BANNER = {
    "type": "conditional",
    "conditions": [
        {"condition": "state", "entity": "binary_sensor.tower_alert_banner", "state": "on"}
    ],
    "grid_options": {"columns": "full"},
    "card": {
        "type": "vertical-stack",
        "cards": [
            {
                "type": "markdown",
                "content": "# ERROR !!\n###### {{ (state_attr('sensor.tower_error_list','errors') or []) | count }} active",
                "card_mod": {
                    "style": {
                        ".": "ha-card {\n  border: none;\n  min-height: 130px;\n  position: relative;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  animation: errbg 1.8s ease-in-out infinite;\n}\n@keyframes errbg {0%,100%{background:#c00000;}50%{background:#000000;}}\n",
                        "ha-markdown$": "h1 {\n  text-align: center;\n  font-size: 4em;\n  font-weight: 900;\n  letter-spacing: 6px;\n  margin: 0;\n  animation: errtx 1.8s ease-in-out infinite;\n}\nh6 {\n  position: absolute;\n  left: 16px;\n  bottom: 8px;\n  margin: 0;\n  font-size: 1em;\n  font-weight: 700;\n  animation: errtx 1.8s ease-in-out infinite;\n}\n@keyframes errtx {0%,100%{color:#000000;}50%{color:#ff3030;}}\n",
                    }
                },
            },
            {
                "type": "markdown",
                "content": "{% for e in (state_attr('sensor.tower_error_list','errors') or []) %}\n- **{{ e.msg }}**\n{% endfor %}",
            },
            {
                "type": "horizontal-stack",
                "cards": [
                    {
                        "type": "entities",
                        "entities": [{"entity": "input_select.tower_alert_snooze_duration", "name": "Snooze"}],
                        "card_mod": {"style": "ha-card{box-shadow:none;background:none;border:none;}\n#states{padding:0 8px;}\n.card-content{padding:4px 8px !important;}\n"},
                    },
                    {
                        "type": "button",
                        "name": "DISABLE",
                        "show_icon": False,
                        "show_state": False,
                        "tap_action": {"action": "perform-action", "perform_action": "script.tower_alert_snooze"},
                        "card_mod": {"style": "ha-card{min-height:0;height:100%;display:flex;align-items:center;justify-content:center;font-weight:700;}\n.button{padding:6px !important;}\n"},
                    },
                ],
            },
        ],
    },
}

BROKEN_TILE_ENTITY = "binary_sensor.grow_tower_water_level"
REPLACEMENT_TILES = [
    {"type": "tile", "entity": "binary_sensor.grow_tower_water_level_low", "name": "Tower Water — Low (Critical)"},
    {"type": "tile", "entity": "binary_sensor.grow_tower_water_level_medium", "name": "Tower Water — Medium"},
    {"type": "tile", "entity": "binary_sensor.grow_tower_water_level_high", "name": "Tower Water — High"},
]


async def ws_call(ws, mid, **kw):
    await ws.send(json.dumps({"id": mid, **kw}))
    while True:
        r = json.loads(await ws.recv())
        if r.get("id") == mid:
            return r


def is_broken_tile(card):
    return card.get("type") == "tile" and card.get("entity") == BROKEN_TILE_ENTITY


def has_alerts_section(sections):
    return any(
        any("tower_alert_banner" in json.dumps(c) or "tent_alert_banner" in json.dumps(c)
            for c in s.get("cards", []))
        for s in sections
    )


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    async with websockets.connect(WS_URL, max_size=None) as ws:
        assert json.loads(await ws.recv())["type"] == "auth_required"
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        assert json.loads(await ws.recv())["type"] == "auth_ok"

        mid = 1
        dash = (await ws_call(ws, mid, type="lovelace/config", url_path=URL_PATH))["result"]; mid += 1

        ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d-%H%M%SZ")
        backup_path = HERE / f"dashboard_mom_backup_{ts}.json"
        backup_path.write_text(json.dumps(dash, indent=1))
        print(f"Backup written: {backup_path}")

        sections = dash["views"][0]["sections"]

        if not has_alerts_section(sections):
            sections.insert(0, {
                "type": "grid",
                "cards": [
                    {"type": "heading", "heading": "Alerts"},
                    TENT_ALERT_BANNER,
                    TOWER_ALERT_BANNER,
                ],
            })
            print("Inserted new Alerts section at index 0.")
        else:
            print("Alerts section already present — skipping insert.")

        fixed = False
        for s in sections:
            cards = s.get("cards", [])
            idxs = [i for i, c in enumerate(cards) if is_broken_tile(c)]
            for i in idxs:
                cards[i:i + 1] = REPLACEMENT_TILES
                fixed = True
        print("Replaced broken tile." if fixed else "No broken tile found — skipping.")

        if not args.apply:
            print("\nDRY RUN — not saved. Re-run with --apply to write to dashboard-mom.")
            return

        save = await ws_call(ws, mid, type="lovelace/config/save", url_path=URL_PATH, config=dash); mid += 1
        print("save success:", save.get("success"), save.get("error", ""))


if __name__ == "__main__":
    asyncio.run(main())
