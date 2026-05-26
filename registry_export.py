"""Pre-migration snapshot: dump HA entity/area/device/label registries as JSON.

Writes to ./migration_snapshots/<UTC-timestamp>/ so they're diff-able and can be
cherry-pick reverted entity-by-entity if a migration step goes sideways.

Usage:
    python registry_export.py
    python registry_export.py --label pre-tagging-migration

Output:
    migration_snapshots/<timestamp>[_label]/
        entity_registry.json
        area_registry.json
        device_registry.json
        label_registry.json
        manifest.json   (counts + HA version + timestamp)
"""
import argparse, asyncio, json, pathlib, sys
from datetime import datetime, timezone
import websockets
import aiohttp

HERE = pathlib.Path(__file__).parent
MCP_JSON = HERE / ".cursor" / "mcp.json"
cfg = json.loads(MCP_JSON.read_text())["mcpServers"]["home-assistant"]["env"]
HA_URL = cfg["HA_URL"]
HA_TOKEN = cfg["HA_TOKEN"]
WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://") + "/api/websocket"

REGISTRIES = [
    ("entity_registry", "config/entity_registry/list"),
    ("area_registry", "config/area_registry/list"),
    ("device_registry", "config/device_registry/list"),
    ("label_registry", "config/label_registry/list"),
]


async def ws_call(ws, msg_id, **kwargs):
    await ws.send(json.dumps({"id": msg_id, **kwargs}))
    while True:
        reply = json.loads(await ws.recv())
        if reply.get("id") == msg_id:
            return reply


async def fetch_version():
    async with aiohttp.ClientSession() as s:
        async with s.get(f"{HA_URL}/api/config", headers={"Authorization": f"Bearer {HA_TOKEN}"}) as r:
            r.raise_for_status()
            data = await r.json()
            return data.get("version")


async def main(label: str | None):
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%SZ")
    folder = ts + (f"_{label}" if label else "")
    out_dir = HERE / "migration_snapshots" / folder
    out_dir.mkdir(parents=True, exist_ok=True)

    version = await fetch_version()
    counts = {}

    async with websockets.connect(WS_URL, max_size=None) as ws:
        hello = json.loads(await ws.recv())
        assert hello["type"] == "auth_required", hello
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        auth = json.loads(await ws.recv())
        assert auth["type"] == "auth_ok", auth

        mid = 0
        for name, ws_type in REGISTRIES:
            mid += 1
            reply = await ws_call(ws, mid, type=ws_type)
            if not reply.get("success", True) and "result" not in reply:
                print(f"  FAIL {name}: {reply}", file=sys.stderr)
                sys.exit(2)
            records = reply["result"]
            counts[name] = len(records) if isinstance(records, list) else "n/a"
            path = out_dir / f"{name}.json"
            path.write_text(json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False))
            print(f"  wrote {path.name}  ({counts[name]} records)")

    manifest = {
        "timestamp_utc": ts,
        "label": label,
        "ha_url": HA_URL,
        "ha_version": version,
        "counts": counts,
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(f"\nSnapshot complete: {out_dir}")
    return out_dir


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default=None, help="Suffix appended to folder name (e.g. pre-tagging-migration)")
    args = ap.parse_args()
    asyncio.run(main(args.label))
