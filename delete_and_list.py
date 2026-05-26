"""
List all input_* items and delete the duplicate feeds_per_day_2.
Also get the internal storage IDs for all entities.
"""
import asyncio
import json
import os
import websockets

HA_WS_URL = "ws://192.168.2.151:8123/api/websocket"
HA_TOKEN = os.environ["HA_TOKEN"]


async def list_and_fix():
    msg_id = 1

    async with websockets.connect(HA_WS_URL) as ws:
        msg = json.loads(await ws.recv())
        await ws.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        msg = json.loads(await ws.recv())
        print(f"Auth: {msg['type']}")

        async def send_cmd(cmd):
            nonlocal msg_id
            cmd["id"] = msg_id
            msg_id += 1
            await ws.send(json.dumps(cmd))
            resp = json.loads(await ws.recv())
            return resp

        # List all input_* entities
        for domain in ["input_number", "input_datetime", "input_boolean", "input_text"]:
            resp = await send_cmd({"type": f"{domain}/list"})
            if resp.get("success"):
                items = resp["result"]
                print(f"\n=== {domain} ({len(items)} items) ===")
                for item in items:
                    print(f"  id={item['id']!r:45} name={item['name']!r}")
            else:
                print(f"\n=== {domain} LIST FAILED: {resp} ===")

        # Delete the duplicate feeds_per_day_2
        print("\n--- Deleting feeds_per_day_2 ---")
        resp = await send_cmd({"type": "input_number/delete", "input_number_id": "feeds_per_day_2"})
        if resp.get("success"):
            print("  [OK] Deleted feeds_per_day_2")
        else:
            print(f"  [INFO] {resp.get('error', {}).get('message', resp)}")

asyncio.run(list_and_fix())
