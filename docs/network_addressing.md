# Network addressing — static IPs, the DHCP pool, and what breaks

How the grow-system devices get their addresses on `192.168.2.0/24`, why the ESP32s
pin theirs in firmware, and the two failure modes that come out of that.

Written 2026-08-07 after moving three ESP statics above the DHCP pool.

---

## Why the ESPs use in-firmware static IPs

**The router refuses DHCP reservations.** That leaves no way to guarantee a device
keeps its address, and Home Assistant's ESPHome integration dials a *stored host*, not
a name — `<device>.local` does not resolve from the LXC 100 or VM 101 shells (no
`nss-mdns`). So each ESP pins its own address with a `manual_ip:` block in its ESPHome
YAML, on **both** network entries (grow AP and router fallback).

## Current assignments

| device | address | notes |
|---|---|---|
| `tent-irrigation-controller` | **192.168.2.240** | moved from `.55` 2026-08-07 |
| `grow-tent-one` | **192.168.2.241** | moved from `.96` 2026-08-07 |
| `grow-tent-two` | **192.168.2.242** | moved from `.39` 2026-08-07 |
| `grow-tent-climate` | **192.168.2.236** | already above the pool |
| `grow-tower` | **192.168.2.248** | already above the pool — **committed but NOT flashed**, node is offline on July firmware |
| `test-esp32` | **192.168.2.53** | Windows bench board, normally powered off |

Infrastructure: Proxmox host `.100` · HA VM 101 `.151` · ESPHome LXC 100 `.14` ·
Brentons grow-area AP (GT784WN bridge) `.250` · HS300 irrigation strip `.182`.

## Where the DHCP pool actually is

Not read from the router — its web UI at `.1` returns HTTP 200 but an empty page and
was not authenticated against. The boundary below is **inferred from observed
occupancy**, which is good enough to act on but is not a config readout:

- DHCP demonstrably hands out **into the .180s** — live leases seen at `.14`, `.16–.28`,
  `.33–.42`, `.45`, `.52`, `.57`, `.58`, `.77`, `.84`, `.143`, `.165`, `.183`.
- **`.200–.254` is essentially empty** — a sweep found only `.204`, `.228`, `.236`,
  `.250`, all deliberate statics.

**So: put statics at `.200+`.** `.39`, `.55` and `.96` sat inside the range the router
actively leases from, which left them exposed to a collision; that is why they moved.

> Note on scope: moving them removed a real exposure, but a collision was **never
> observed**. The 2026-08-07 controller outage that prompted the move is still
> unexplained — see the incident memory. Do not treat the renumber as its fix.

## ⚠ Changing a static IP requires re-pointing Home Assistant by hand

**Zeroconf does not follow the device.** Verified across all three moves on
2026-08-07 — and these entries were *originally created* by zeroconf discovery, so
"it was auto-discovered" is not evidence it will re-discover. HA keeps dialling the
old address and every entity for that device goes `unavailable` and stays there.

Order of operations:

1. Edit `manual_ip:` in the **LXC copy** (`/root/config/<name>.yaml` on LXC 100) —
   that is the copy that gets flashed.
2. Flash with `--device <OLD-ip>`; that is still how you reach it. The device reboots
   onto the new address.
3. Re-point HA with **`tools/ha_repoint_esphome.py`** (run it on the VM; it reads the
   `noise_psk` HA already stores and posts it back to localhost, so the key never
   moves). `abort / already_configured_updates` is **success**.
4. Mirror the change into `esphome-config` and `C:\esphome-test`.

Full runbook: the `flash-esp32` skill.

## TP-Link/Kasa devices: "pings fine, integration dead"

Separate failure mode, same subnet. When a TP-Link device answers ping but its HA
entities are `unavailable` — or its config entry sits `not_loaded` — **and the log
shows zero kasa/tplink retry lines**, the break is on the cloud/device side, not HA's.

**Fix: Tapo app → device → Third-Party Services / Cloud Service → toggle OFF, then ON.**

An HA config-entry reload does *not* fix it. Confirmed again 2026-08-07 on four
`KP125M` plugs (`.84`, `.143`, `.202`, `.139`): reload returned
`{"require_restart": false}` and every entry stayed `not_loaded`, with no retry lines
logged. Same signature previously documented for the HS300 strip.

## Diagnosing from the right box

- **Sweep from the HA VM, never the Windows PC** — the PC is on a different segment and
  cannot reach grow devices even when they are healthy.
- `ip neigh show <ip>` beats ping: `FAILED`/`INCOMPLETE` means the MAC will not even
  resolve, i.e. the device is off the LAN entirely rather than merely refusing a port.
- An ESPHome device's own MAC is in HA's device registry — check it before concluding
  someone else has taken an address. (On 2026-08-07 `.55` resolving to
  `44:1d:64:f1:48:90` looked like a squatter; it was the controller's own MAC.)
