#!/usr/bin/env python3
"""Re-point a Home Assistant ESPHome config entry at a new IP address.

WHY THIS EXISTS
---------------
When an ESPHome device's `manual_ip: static_ip:` changes and you reflash it, the
device comes up on the new address but **Home Assistant keeps dialling the old
one** and every entity for that device goes `unavailable`. Zeroconf does not fix
this on its own -- observed 2026-08-07, even though the entries were originally
created by zeroconf discovery.

The supported fix is the ESPHome integration's *reconfigure* flow, which runs in
two steps:

    1. `user`            -> host + port
    2. `encryption_key`  -> noise_psk

Step 2 asks for a key Home Assistant is already storing for that device, so this
script reads it back out of `.storage/core.config_entries` and posts it straight
back. That means the key never has to be typed, copied, or moved off the box --
which is why this is designed to RUN ON THE HA VM and talk to localhost only.

    FINAL: type=abort reason=already_configured_updates

is the SUCCESS result. That abort reason means "an entry already matched and its
data was updated", which is exactly the intent. Entities come back in ~10 s.

USAGE (on the HA VM, e.g. homeadmin@192.168.2.151)
--------------------------------------------------
    python3 ha_repoint_esphome.py <entry_id> <new_host>

Find <entry_id> with:
    GET /api/config/config_entries/entry   (admin token; filter domain == esphome)

Needs a long-lived token at ~/.ha_token (chmod 600) -- the same one pull-ha.sh uses.
"""

import json
import sys
import urllib.request

BASE = "http://localhost:8123"
TOKEN_FILE = "/home/homeadmin/.ha_token"
ENTRIES = "/home/homeadmin/homeassistant/.config/.storage/core.config_entries"


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    entry_id, new_host = sys.argv[1], sys.argv[2]

    token = open(TOKEN_FILE).read().strip()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    def post(url, payload):
        req = urllib.request.Request(
            url, data=json.dumps(payload).encode(), headers=headers, method="POST"
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.load(resp)

    # Reuse the noise_psk HA already stores for this device.
    psk = None
    for entry in json.load(open(ENTRIES))["data"]["entries"]:
        if entry["entry_id"] == entry_id:
            psk = entry["data"].get("noise_psk")
            print(f"  entry: {entry.get('title')}  "
                  f"old host={entry['data'].get('host')} -> {new_host}")
    if psk is None:
        sys.exit(f"  no esphome entry {entry_id} with a stored noise_psk")

    flow = post(f"{BASE}/api/config/config_entries/flow",
                {"handler": "esphome",
                 "context": {"source": "reconfigure", "entry_id": entry_id}})
    fid = flow["flow_id"]

    res = post(f"{BASE}/api/config/config_entries/flow/{fid}",
               {"host": new_host, "port": 6053})
    print(f"  host step: type={res['type']} step={res.get('step_id')} "
          f"errors={res.get('errors')}")

    if res["type"] == "form" and res.get("step_id") == "encryption_key":
        res = post(f"{BASE}/api/config/config_entries/flow/{fid}", {"noise_psk": psk})
        print(f"  key  step: type={res['type']} reason={res.get('reason')}")

    ok = res.get("reason") == "already_configured_updates"
    print(f"  FINAL: type={res['type']} reason={res.get('reason', '')}  "
          f"{'<- SUCCESS' if ok else '<- CHECK THIS'}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
