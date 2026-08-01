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
  the reboot (this box has a history of a NIC hardware hang, see `project-ha-down-20260709`,
  so don't reboot it speculatively).
- **ESPHome tool**: on LXC 100 via Proxmox host (`pct exec 100 -- ...`), run
  `VIRTUAL_ENV=/opt/esphome/.venv /usr/local/bin/uv pip install --dry-run --upgrade esphome`
  to see the version delta without applying it.
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
5. **Device reflash** — for each *online* device: first verify no feed/flush cycle is
   running (`script.run_feed_now` / `script.run_flush_now` state `"off"`) and no
   stir/air burst is mid-cycle (`script.tent_stir_burst` / `script.tent_air_burst`
   `current: 0`) — a flash reboots the ESP and all GPIO outputs default OFF on boot
   (valves close), which is safe when idle but would interrupt an active cycle.
   Then: `pct exec 100 -- bash -c 'cd /root/config && /opt/esphome/.venv/bin/esphome
   run <config>.yaml --device <esphome-name>.local --no-logs'`. Watch for
   `INFO OTA successful` + exit 0. **Windows console gotcha**: pipe/print the SSH
   stdout through `.encode("ascii", "replace").decode("ascii")` before printing —
   raw PlatformIO output has box-drawing characters that crash a cp1252 terminal.

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
