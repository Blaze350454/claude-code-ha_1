import asyncio, json, re, pathlib, websockets

env = dict(re.findall(r'^(\w+)=(.*)$', pathlib.Path('.env').read_text(), re.M))
TOKEN = env['HA_TOKEN']
URL = "ws://192.168.2.151:8123/api/websocket"

DEVICE_ID = "5ae513c6adc21392f807171b42513eba"
NEW_DEVICE_NAME = "Camera Tent 1"

# current entity_id -> new entity_id (append _1); name override cleared so each
# entity inherits the device prefix ("Camera Tent 1 <Temperature>" etc).
RENAMES = {
    "camera.tent": "camera.tent_1",
    "binary_sensor.tent_camera_armed": "binary_sensor.tent_camera_armed_1",
    "binary_sensor.motion_camera_tent": "binary_sensor.motion_camera_tent_1",
    "switch.motion_detection_camera_tent": "switch.motion_detection_camera_tent_1",
    "sensor.temperature_camera_tent": "sensor.temperature_camera_tent_1",
    "binary_sensor.battery_camera_tent": "binary_sensor.battery_camera_tent_1",
    "sensor.wi_fi_signal_strength_camera_tent": "sensor.wi_fi_signal_strength_camera_tent_1",
}


async def req(ws, msg, _id):
    msg = dict(msg); msg["id"] = _id
    await ws.send(json.dumps(msg))
    while True:
        m = json.loads(await ws.recv())
        if m.get("id") == _id:
            return m


async def main():
    async with websockets.connect(URL, max_size=None) as ws:
        await ws.recv()
        await ws.send(json.dumps({"type": "auth", "access_token": TOKEN}))
        await ws.recv()

        i = 0
        # 1) rename the device -> entities with has_entity_name inherit the prefix
        i += 1
        r = await req(ws, {"type": "config/device_registry/update",
                           "device_id": DEVICE_ID,
                           "name_by_user": NEW_DEVICE_NAME}, i)
        print("device rename success:", r.get("success"), r.get("error", ""))

        # 2) rename each entity_id and clear the name override
        for old, new in RENAMES.items():
            i += 1
            r = await req(ws, {"type": "config/entity_registry/update",
                               "entity_id": old,
                               "new_entity_id": new,
                               "name": None}, i)
            ok = r.get("success")
            print(f"{old} -> {new}: {ok} {r.get('error','') if not ok else ''}")


asyncio.run(main())
