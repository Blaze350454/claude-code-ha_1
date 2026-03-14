#!/usr/bin/env python3
import asyncio
import sys
import os
import json
import time

creds_file = "/config/scripts/.tplink_creds"
token_file = "/config/scripts/.tplink_tokens"
device_cache_file = "/config/scripts/.tplink_device_cache"
CACHE_TTL = 300  # seconds (5 minutes)

# Force IPv4 - IPv6 not routable in container
import socket
_orig_getaddrinfo = socket.getaddrinfo
def _ipv4_only(host, port, family=0, type=0, proto=0, flags=0):
    return _orig_getaddrinfo(host, port, socket.AF_INET, type, proto, flags)
socket.getaddrinfo = _ipv4_only

if os.path.exists(creds_file):
    with open(creds_file) as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                os.environ[k.strip()] = v.strip()

USERNAME = os.environ.get("TPLINK_USER", "")
PASSWORD = os.environ.get("TPLINK_PASS", "")

def load_tokens():
    if os.path.exists(token_file):
        try:
            return json.load(open(token_file))
        except Exception:
            pass
    return None

def save_tokens(manager):
    try:
        tokens = {
            "token": manager.get_token(),
            "refresh_token": manager.get_refresh_token()
        }
        with open(token_file, "w") as f:
            json.dump(tokens, f)
        os.chmod(token_file, 0o600)
    except Exception:
        pass

async def get_manager_and_target(outlet_name):
    from tplinkcloud import TPLinkDeviceManager

    # Try token + device cache first (fastest path)
    tokens = load_tokens()
    if tokens and os.path.exists(device_cache_file):
        try:
            cache = json.load(open(device_cache_file))
            if time.time() - cache.get("ts", 0) < CACHE_TTL:
                manager = TPLinkDeviceManager(prefetch=False)
                manager.set_auth_token(tokens["token"])
                manager.set_refresh_token(tokens["refresh_token"])
                devices = await manager.get_devices()
                if devices:
                    for device in devices:
                        if device.get_alias().lower() == outlet_name.lower():
                            return device
        except Exception:
            pass

    # Full login + device fetch
    if tokens:
        try:
            manager = TPLinkDeviceManager(prefetch=False)
            manager.set_auth_token(tokens["token"])
            manager.set_refresh_token(tokens["refresh_token"])
            devices = await manager.get_devices()
            if not devices:
                raise Exception("empty")
        except Exception:
            manager = TPLinkDeviceManager(USERNAME, PASSWORD)
            save_tokens(manager)
            devices = await manager.get_devices()
    else:
        manager = TPLinkDeviceManager(USERNAME, PASSWORD)
        save_tokens(manager)
        devices = await manager.get_devices()

    # Cache device list timestamp
    try:
        with open(device_cache_file, "w") as f:
            json.dump({"ts": time.time()}, f)
    except Exception:
        pass

    for device in devices:
        if device.get_alias().lower() == outlet_name.lower():
            return device
    return None

async def main():
    if len(sys.argv) < 3:
        print("off")
        sys.exit(1)

    action = sys.argv[1]
    outlet_name = sys.argv[2]

    target = await get_manager_and_target(outlet_name)

    if not target:
        print("off")
        sys.exit(1)

    if action == "on":
        await target.power_on()
        print("on")
    elif action == "off":
        await target.power_off()
        print("off")

asyncio.run(main())
