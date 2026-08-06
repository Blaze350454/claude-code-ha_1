---
name: update-homelab
description: >
  Update the grow-tent homelab stack: Home Assistant Core (Docker), HACS/Lovelace
  card integrations, VM 101 Ubuntu OS packages, the ESPHome dashboard tool, and
  OTA-reflash the ESP32 devices (tent-irrigation-controller, grow-tent-one,
  grow-tent-two, grow-tower). Use when the user says "update ha", "update esphome",
  "update devices", "update homelab", "full update", or asks to check for / apply
  updates across the grow tent stack.
---

Runbook for a full homelab update pass. Access paths, credentials, and box layout
are in memory `project-homelab-topology` (and `project-ha-config-deploy` /
`project-esphome-deploy`) — read those first if anything here seems stale, since
IPs/paths can drift.

## Order of operations

Work through these in order. Each stage is roughly independent, but do OS/tool
upgrades before device reflashing so devices get the newest ESPHome core in one pass.

### 1. Survey — find out what's actually outdated before touching anything

- **HA update entities**: `ha_list_entities(domain="update")`, then check each
  entity's state (`"on"` = update available). Most of these are HACS-managed
  Lovelace cards/integrations; several are known-dead "Blank" ghost plugs that
  report `"unavailable"` — ignore those (see `project-tent-system-audit` /
  `reference-reservoir-prime-pump-dead-matter-plug`).
- **HA Core itself**: check `binary_sensor.ha_core_update_available` (has
  `running_version` / `latest_version` attributes) — there's no `update.home_assistant_core`
  entity because this install is a plain Docker container, not Supervised/HAOS.
- **VM 101 OS packages**: SSH `homeadmin@192.168.2.151`, then
  `sudo -S -E apt-get update -qq && sudo -S -E apt list --upgradable`. Look for any
  `linux-image-*` package — if present, a reboot will actually be needed; otherwise skip
  the reboot. Also read `/var/run/reboot-required.pkgs`, which can list a reboot pending
  from an *earlier* pass. Some packages (apport, alsa-ucm-conf) sit unupgraded because of
  Ubuntu's **phased rollout** — `apt-get -s full-upgrade` says "deferred due to phasing".
  That is normal, not a failure; leave them.
  **The NIC-hang caveat (`project-ha-down-20260709`) does NOT apply to rebooting VM 101** —
  that e1000e/I219-LM fault is the *Proxmox host's* physical NIC; VM 101 is `virtio_net`.
  A guest reboot is cheap and safe: measured ~30 s end to end on 2026-08-06, both
  containers return on their own (`restart: unless-stopped`), and the ESPs are untouched.
  Only rebooting the **host** carries the e1000e risk.
- **ESPHome tool**: on LXC 100 via Proxmox host (`pct exec 100 -- ...`), run
  `VIRTUAL_ENV=/opt/esphome/.venv /usr/local/bin/uv pip install --dry-run --upgrade esphome`
  to see the version delta without applying it.
- **LXC 100 free disk** — `pct exec 100 -- df -h /`. **Do this before any reflash.**
  ESPHome ≥2026.7 installs its own ESP-IDF toolchain under `/root/.cache/esphome/idf/`
  (several GB). On 2026-08-06 this filled the then-16 GB rootfs and the flash died with
  `RuntimeError: ESP-IDF 5.5.5 framework installation failure` — an error that names the
  framework but actually means **no disk**. Resized to 40 GB (`pct resize 100 rootfs +24G`;
  the `local-lvm` thin pool has ~650 GB spare). Want ≥10 GB free before flashing.
- **Device firmware**: `esphome_list_configs` for the current device list. Check each
  device is actually online first (its `wifi_signal`/`uptime` sensor in HA — if
  `unavailable`, OTA will just fail, so skip and report it rather than attempting).

### 2. Check for breaking changes before touching HA Core

If HA Core has jumped a full monthly release (not just a patch), fetch that month's
release notes (`https://www.home-assistant.io/blog/<year>/<month>/01/release-<yymm>/`)
and check the breaking-changes section against this repo's YAML — grep both
`grow_tent_automation/` in this repo and the separate `homeassistant-config` repo
(`D:\Claude\Projects\homeassistant-config`) for anything renamed/removed. Report what
you found before proceeding, even if nothing matched.

### 3. Confirm scope with the user before applying anything system-level

Surface the survey results (table of component → current → new version) and get an
explicit go-ahead before running anything that restarts a live service or reboots a
box — this stack controls physical irrigation/climate hardware. Low-risk items
(a single HACS card update via `update.install`) can be applied without asking;
HA Core restart, OS full-upgrade, and device reflashing should be confirmed as a
batch (they usually all get approved together, but ask).

### 4. Apply, in this order

1. **Trivial HA update entities** (HACS cards etc.): `ha_call_service(domain="update",
   service="install", entity_id=...)` per entity that's `"on"`.
2. **HA Core**: SSH to VM 101, `cd ~/homeassistant && docker compose pull && docker compose
   up -d`. Poll `http://192.168.2.151:8123/` until it responds (usually back in
   10-30s), then `ha_check_connection` to confirm the new version.
3. **VM 101 OS packages**: `sudo -S -E apt-get -y -o Dpkg::Options::=--force-confold
   full-upgrade`, then `sudo -S -E apt-get -y autoremove --purge`. Check
   `/var/run/reboot-required` — only reboot if it's actually required (kernel bump);
   otherwise leave it running and note that a reboot is pending for next time.
4. **ESPHome tool** (LXC 100 via Proxmox pct exec): `VIRTUAL_ENV=/opt/esphome/.venv
   /usr/local/bin/uv pip install --upgrade esphome && systemctl restart
   esphomeDashboard.service`.
   **⚠ ESPHome 2026.7 REMOVED the built-in dashboard.** `esphome dashboard` now exits 1
   with "The built-in dashboard has been removed from ESPHome" and the service fails.
   It is a separate package now — already migrated on 2026-08-06:
   `uv pip install esphome-device-builder` into the same venv, and the unit's ExecStart
   repointed to `/opt/esphome/.venv/bin/esphome-device-builder /root/config/` (same port
   6052, same positional config-dir arg; original unit backed up at
   `/root/esphomeDashboard.service.bak-20260806`). If the `mcp__esphome__*` tools go dead
   after an ESPHome upgrade, check this service first — it backs them.
5. **Device reflash** — for each *online* device: first verify no feed/flush cycle is
   running (`script.run_feed_now` / `script.run_flush_now` state `"off"`) and no
   stir/air burst is mid-cycle (`script.tent_stir_burst` / `script.tent_air_burst`
   `current: 0`) — a flash reboots the ESP and all GPIO outputs default OFF on boot
   (valves close), which is safe when idle but would interrupt an active cycle.
   Then: `pct exec 100 -- bash -c 'cd /root/config && /opt/esphome/.venv/bin/esphome
   run <config>.yaml --device <STATIC-IP> --no-logs'`. Watch for
   `INFO OTA successful` + exit 0.
   **⚠ Do NOT use `<name>.local` — mDNS does not resolve** from the LXC 100 or VM 101
   shells (no `nss-mdns`); you get "Name or service not known" even though the devices are
   perfectly healthy and device-builder's own mDNS browser sees them. Flash by static IP,
   taken from each config's `manual_ip:` block:
   `grow-tent-climate` **.236** · `grow-tent-one` **.96** · `grow-tent-two` **.39** ·
   `tent-irrigation-controller` **.55** · `grow-tower` **.248** · `test-esp32` **.53**
   A core-version bump busts the build cache, so expect a **full** recompile per device
   (~2-3 min each once ESP-IDF is installed; the first one also downloads the toolchain).
   **Windows console gotcha**: pipe/print the SSH stdout through
   `.encode("ascii", "replace").decode("ascii")` before printing — raw build output has
   box-drawing characters that crash a cp1252 terminal.

### 5. Verify

After each device flash, check its `wifi_signal` or `uptime` sensor in HA came back
(uptime near-zero confirms it actually rebooted onto new firmware, not just stayed
connected). A device briefly showing `unavailable` right after a flash before
recovering is normal — recheck once before treating it as a real failure. Check
`sensor.tent_error_list` / `binary_sensor.tent_alert_banner` afterward and confirm
any flagged issue predates the update (cross-reference memory) rather than being
caused by it.

### Credentials

`.env` at repo root has `PROXMOX_PASSWORD`, `HA_URL`, `HA_TOKEN`. SSH to VM 101 uses
key auth (no password) for the user account; `sudo` there needs `PROXMOX_PASSWORD`.
The Proxmox host itself has no SSH key set up — use `paramiko` with password auth
(`root` / `PROXMOX_PASSWORD`), e.g. `uv run --with paramiko --with python-dotenv
python <script>`. Write throwaway scripts to the scratchpad dir, not `/tmp` (Windows
`uv run` on this box doesn't resolve Git-Bash's `/tmp`).
