---
name: flash-esp32
description: >
  Edit one ESP32's ESPHome YAML and OTA-flash it in the tight dev loop
  (write -> flash -> verify), outside a full stack update. Use when the user says
  "flash <device>", "reflash the esp", "install the code on the esp32", "push the
  firmware", "change the esp code and flash it", or is iterating on a single ESP32's
  config (grow-tent-env, tent-irrigation-controller, test-esp32, etc.). For a full
  homelab update pass (HA Core + OS + all devices) use `update-homelab` instead.
---

Tight single-device edit/flash/verify loop. Credentials, IPs and box layout live in
memory `project-homelab-topology`, `project-esphome-deploy`,
`reference-esphome-windows-bench` — read those if anything here looks stale.

## The one thing that trips people up
**The ESPHome-dashboard MCP `esphome_compile` / `esphome_validate` tools return HTTP 405
(known-broken on this dashboard).** So you can WRITE configs via MCP but you CANNOT
compile/flash through it. Flashing happens from the Windows PC (or the LXC). Don't waste
a turn retrying the MCP compile.

## Step 1 — write the config (keep BOTH copies in sync)
There are two config copies and they drift; update both when you change one:
- **LXC dashboard copy**: `esphome_write_config(configuration="<name>.yaml", content=...)`
  (this is what the dashboard/`esphome_read_config` sees).
- **Windows flash copy**: `C:\esphome-test\<name>.yaml` (Read it first, then Write — this
  is the copy that actually gets compiled + flashed by Step 2's primary path).

## Step 2 — flash (primary: Windows-direct OTA, proven fast)
esphome is not on PATH and not in a venv here — it runs via **uv's cache with `uvx`**.
Secrets live in `C:\esphome-test\secrets.yaml`.

```powershell
Set-Location C:\esphome-test
uvx esphome@2026.6.5 run <name>.yaml --device <device-ip> --no-logs 2>&1 | Select-Object -Last 40
```

- Pin `esphome@<ver>` to the version the device currently runs (**2026.7.4** as of
  2026-08-06 — all four tent ESPs were reflashed onto it; check the device's
  `esphome_version` sensor or the dashboard) so you don't silently bump the firmware core.
- **Crossing the 2026.6 → 2026.7 boundary is not a normal bump.** 2026.7 replaced
  PlatformIO with a native ESP-IDF toolchain, so the first build downloads several GB and
  the cache is invalidated (full recompile, not incremental). `~/.platformio` becomes dead
  weight for every `esp-idf` config — only `grow-tower.yaml` is still `framework: arduino`.
- `--device <device-ip>` forces OTA to that address (e.g. `192.168.2.54`). Boards with a
  dead USB bootloader flash fine this way as long as they're online.
- `| Select-Object -Last 40` is REQUIRED: raw PlatformIO output has box-drawing chars that
  crash the cp1252 console. Success = `INFO OTA successful` + `Successfully uploaded program.`
- Compile is incremental (build cache in `.esphome\build\<name>`), usually well under a
  minute after the first build; give the tool a long timeout anyway.
- **The api encryption `key:` in `secrets.yaml` MUST match what HA already stored** for the
  device, or HA loses the connection after the flash. The existing `C:\esphome-test\secrets.yaml`
  is already correct for grow-* devices — reuse it, don't regenerate keys.
- **PowerShell, not git-bash** (MSYS breaks the esp-idf toolchain).

### Step 2 alt — flash from the LXC (when the Windows copy/secrets aren't handy)
Per `update-homelab`: paramiko `root`/`PROXMOX_PASSWORD` to the Proxmox host, then
`pct exec 100 -- bash -c 'cd /root/config && /opt/esphome/.venv/bin/esphome run <name>.yaml
--device <STATIC-IP> --no-logs'`. Config lives in LXC `/root/config`. The Proxmox host has
no SSH key (password auth only); VM 101 `homeadmin@192.168.2.151` uses key auth.

**⚠ `<name>.local` does NOT resolve** from the LXC 100 or VM 101 shells (no `nss-mdns`) —
you get "Name or service not known" on perfectly healthy devices. Use the static IP from
the config's `manual_ip:` block: `grow-tent-climate` **.236** · `grow-tent-one` **.241** ·
`grow-tent-two` **.242** · `tent-irrigation-controller` **.240** · `grow-tower` **.248** ·
`test-esp32` **.53**.
**Renumbered 2026-08-07** — irrigation `.55`→`.240`, tent-one `.96`→`.241`,
tent-two `.39`→`.242`, to lift every static above the DHCP pool (the router refuses
reservations, and DHCP demonstrably hands out into the .180s, so statics down there
were exposed to a lease collision). `.236`/`.248` were already high and did not move.
**Changing a device's static IP also requires re-pointing HA**, which does NOT happen
by itself — see "Step 2b" below.

Check `pct exec 100 -- df -h /` first — the ESP-IDF toolchain needs GB of free space and
reports exhaustion as a misleading
`RuntimeError: ESP-IDF 5.5.5 framework installation failure`.

## Step 2b — if you changed the static IP, re-point HA (it will NOT self-heal)
Flash with `--device <OLD-ip>` (that is how you still reach it); the device reboots onto
the new one. HA keeps dialling the old address and every entity goes `unavailable` —
**zeroconf did not update it** in practice (2026-08-07), even though all the ESPHome
entries were originally created by zeroconf discovery.

Drive the reconfigure flow. It is two steps: `user` (host/port) then `encryption_key`,
which asks for the `noise_psk` HA *already has* — so read it back out of
`.storage/core.config_entries` and post it straight back. Run it ON THE VM so the key
never leaves the box. `tools/ha_repoint_esphome.py` in this repo does exactly that:

```bash
scp tools/ha_repoint_esphome.py homeadmin@192.168.2.151:/tmp/
ssh homeadmin@192.168.2.151 'python3 /tmp/ha_repoint_esphome.py <entry_id> <new-ip>'
# <entry_id> from: GET /api/config/config_entries/entry  (filter domain == esphome)
```

`FINAL: type=abort reason=already_configured_updates` is **success** — that abort reason
means "entry matched and its data was updated". Entities return within ~10 s.

## Step 3 — verify (HA is the fastest check)
- `ha_get_entity_state` on the device's sensors: `..._wifi_signal`/`uptime` back = it
  rebooted onto new firmware; new entities reporting values = success. `unknown` right after
  boot can be normal for a cycle (SCD41 CO2 needs ~30-60s warmup); recheck once.
- **Boot I2C scan** (definitive for sensor wiring): `uvx esphome@<ver> logs <name>.yaml`
  and power-cycle / reflash to catch boot — look for `Results from bus scan: Found device at
  address 0x..` per bus. (Run this in the background with a timeout; `logs` streams forever.)

## Safety before flashing an irrigation board
Before reflashing `tent-irrigation-controller`, confirm no feed/flush/stir/air cycle is
mid-run (`script.run_feed_now`/`run_flush_now` = `off`, `tent_stir_burst`/`tent_air_burst`
`current: 0`). A flash reboots the ESP and all GPIO outputs default OFF on boot (valves
close) — safe when idle, disruptive mid-cycle.

## Device quick-map
- **grow-tent-env** @ `192.168.2.54` — SCD41 CO2 + 4x BME280 (two I2C buses). Dead USB → OTA only.
- **test-esp32** @ `192.168.2.53` — Windows bench board (`reference-esphome-windows-bench`).
- tent-irrigation-controller / grow-tent-one / grow-tent-two / grow-tower — see memory.
  (grow-tower @ `192.168.2.248` was named hydro-tower until 2026-07-15.)

## I2C sensor-bring-up cheatsheet (hard-won on grow-tent-env)
- Each device shows in the boot scan when it ACKs its address; role = **bus + SDO strap**,
  not any label. On one bus, two BME280/BMP280 must be strapped **opposite**: one SDO->GND
  (0x76), one SDO->3.3V (0x77). Four of them need both buses (two per bus).
- **SDO must be tied SOLIDLY** to GND or 3.3V. Floating/loose SDO = undefined address = the
  device won't ACK (shows as "found no devices" / a bus that won't enumerate).
- `bme280.sensor: Wrong chip ID or no response` while the scan DID find the address = the
  module is a **BMP280 (chip 0x58, temp+pressure, no humidity), not a BME280 (0x60)** — very
  common mislabeled modules. Fix = `platform: bmp280_i2c` (drop humidity) or swap in a real BME280.
- Power/ground good but a bus dark = suspect **SDA/SCL swapped** on that bus's GPIO pair.
