# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## ⚠ THIS REPO IS PUBLIC

The remote is **`https://github.com/Blaze350454/claude-code-ha_1` — a public repo.**
Everything pushed here is world-readable immediately.

- **Never commit a credential value.** All secrets live in gitignored files only —
  see **`docs/secrets_and_credentials.md`** for the full list, the HA token rotation
  runbook, and the history-audit recipe.
- `.gitignore` does not untrack an already-committed file, and does nothing about
  history. Use `git rm --cached <path>` (keeps the local file) plus an ignore rule.
- If a secret does get pushed, **rotate it first**. A revoked credential in public
  history is inert; a history rewrite is disruptive and un-publishes nothing.
- This applies to CAD, logs and dashboards too — large binaries and stray debug
  output have no business in a public repo. STEP exports are gitignored (`*.step`)
  and kept on the build machine.

## Project Overview

**Grow Home** is the umbrella repo for all of the home garden/grow automation projects — a single home for tooling and configs that grows as new grow systems (tent, tower, future builds) are added over time. It currently holds these independent but related sub-projects:

1. **MCP Server** (`mcp_server/`) — A FastMCP server that combines semantic search over crawled documentation with live Home Assistant control via REST API. Consumed by AI agents (Claude Code, Cursor) over stdio.
2. **ESPHome MCP** (`esphome_mcp/`) — A separate, self-contained MCP server specifically for ESPHome documentation. Has its own `pyproject.toml` and `uv` environment.
3. **Grow Tent Automation** (`grow_tent_automation/`) — HA YAML configs for the tent irrigation system. Hardware/entity documentation is in `docs/tent_irrigation_esphome.md`.

   ⚠ **`grow_tent_automation/grow_tent_package.yaml` is NOT the live package** —
   it is a 374-line snapshot untouched since the initial commit (1cab613,
   2026-05-26). The package Home Assistant actually loads is
   **`packages/grow_tent_package.yaml` in the `homeassistant-config` repo**
   (796 lines, checked out on the HA VM at `~/homeassistant/.config`). The two
   have diverged hard: the local copy has none of the tent-average / VPD /
   dewpoint / divergence templates and still references
   `sensor.temperature_camera_tent`, an entity that does not exist. **Edit the
   `homeassistant-config` copy; never deploy this one.** (Corrected 2026-08-05,
   after this file's "main HA package" claim sent a session to the wrong file.)

New grow projects (e.g. the hydro tower, plant scales, CO2 sensor builds tracked in `MEMORY.md`) are added here as additional sub-directories rather than as separate repos.

## Commands

```bash
# Install/sync all dependencies
uv sync

# Run the MCP server (loads docs, generates embeddings, runs on stdio)
uv run python -m mcp_server.main

# Crawl documentation into storage/
uv run python crawl.py https://www.home-assistant.io/docs/ --max-depth 3 --include-pattern "*docs*"
```

For the ESPHome MCP sub-project:
```bash
cd esphome_mcp
uv sync
uv run python crawl.py https://esphome.io/components/
python -m esphome_mcp.main
```

## Architecture

MCP-server internals (startup/import order, chunk cache format, HA client
lifecycle, `config.py` paths) live in `mcp_server/CLAUDE.md` — it loads
automatically when working in that package.

## Tagging Standard (READ BEFORE ADDING ENTITIES)

Every HA entity/device/automation/script/helper follows the v1 tagging taxonomy documented at **`D:\Claude\Projects\homeassistant-config\docs\tagging_standard.md`**. Consult it before creating or migrating anything in HA — it defines the `sys_` / `sub_` / `fn_` / `sev_` label prefixes, required labels per entity, area vs label rules, and severity triage.

Migration tooling lives in this repo:
- `tag_migration_phase1a.py` — idempotent migrator (dry-run default, `--apply` commits)
- `registry_export.py` — pre/post-migration JSON snapshots under `migration_snapshots/<timestamp>[_label]/`
- `tag_migration_grow_tower_*.py` — seven per-concern Grow Tower migrators (sensors,
  led_numbers, color_select, color_text, led_testing_controls, pump_labels,
  alert_labels), same idempotent dry-run-by-default pattern

**Workflow:** always `python registry_export.py --label <pre-something>` first, then
run the migrator dry, read the diff, then `--apply`. These scripts read `HA_URL` /
`HA_TOKEN` from `.cursor/mcp.json` at runtime — that file is gitignored and holds a
real token, so never commit it (see `docs/secrets_and_credentials.md`).

**Entity-ID gotcha:** HA prefixes the *area name* onto entity IDs created on an
area-assigned device, so a freshly flashed ESP produces e.g.
`binary_sensor.front_sunroom_grow_tower_water_level_low`. The migrators strip that
prefix — expect to re-run one after any reflash that adds entities.

## Home Assistant / Grow System Context

- HA instance: `http://192.168.2.151:8123`
- **HS300 "Tent Irrigation Power Strip"** — `192.168.2.182`, MAC suffix `c074`,
  model **HS300**, 6 sockets. This is the **live feed/flush strip**. Its six sockets,
  verified against the registry 2026-08-07, are exactly: `air_pump`, `feed_pump`,
  `feed_stir_pump`, `flush_pump`, `flush_stir_pump`, `irrigation_controller`
  (plus the strip master and its LED, which are not sockets).
  (MAC verified 2026-06-16 — an earlier `53db` here was wrong; don't "correct" it back.)
  - **⚠ Corrected 2026-08-07: the irrigation ESP32 is NOT on this strip — it is not
    on a smart plug at all.** `switch.irrigation_controller_tent` is a real HS300
    socket (platform `tplink`, on the `c074` strip) and it is named after the ESP,
    but **it does not power it** — confirmed by the user, who has eyes on the wiring.
    What that socket actually feeds is **unrecorded**; fill this in when known.
    **Consequence: you cannot power-cycle the irrigation ESP32 from Home Assistant.**
    Recovery from a wedged controller is a physical unplug, or a reflash. This file
    previously claimed the socket powered the ESP, which sent a session (2026-08-07)
    to recommend a power-cycle that would have done nothing.
  - **Corrected 2026-08-07: the table-drain pump is NOT on this strip.**
    `switch.table_drain_pump_irrigation_tent` is an **ESPHome** switch on
    **grow-tent-one** (esp32-c3-devkitm-1), as are `binary_sensor.table_drain_empty`
    / `_full`. This entry used to list it among the strip's loads; it never was one.
  - **Corrected 2026-08-05:** this entry previously described `.182`/`c074` as an
    *unplugged KP303 spare*. That was wrong — it is the live HS300, and **no KP303
    exists in the device registry at all**. Verified against
    `.storage/core.device_registry` (model `HS300`, sockets `Socket for HS300(US)`).
  - **Corrected 2026-08-05:** the pumps are **NOT** driven by a custom cloud-API
    service on port 8765. That service is gone — nothing listens on 8765 and no
    unit exists. Every pump switch is `platform=tplink`, i.e. the **native TP-Link
    integration**. Don't go looking for the 8765 service.
  - **Recovery when the strip goes `unavailable` but still pings:** Tapo app →
    toggle **Third-Party Services OFF then ON**. An HA reload does *not* fix it.
    Zero kasa retries in the log alongside a pingable strip is the signature.
- ESP32 device `tent-irrigation-controller` exposes float switches, solenoid valves, and DS18B20 sensors to HA via ESPHome.
- Full irrigation entity IDs and HS300 outlet mappings: see `MEMORY.md` and `grow_tent_automation/docs/tent_irrigation_esphome.md`.
- HA config on host VM: `/home/homeadmin/homeassistant/.config/configuration.yaml`
- **Proxmox host (`192.168.2.100`) — storage, VM backups, backup monitoring, guest agent
  and the "rebooting VM 101" checklist: see `docs/proxmox_host.md`.** Read it before
  touching `local` storage or debugging a backup — `vzdump`'s `Broken pipe` error means
  *out of disk*, and the backup-listing API returns an empty list rather than a 403 when
  the token lacks `Datastore.AllocateSpace` + `VM.Backup`.

### Power topology (matters for every "everything is offline" diagnosis)

- **On UPS:** the Proxmox host / HA VM, both PCs + displays, the **Brentons WiFi
  router**, and both 3D printers. HA therefore *survives* a house power cut and can
  observe it. WiFi survives too, by design.
- **During an area outage** the house runs a generator feeding only a few isolated
  outlets — **no grow equipment is on them**, so the tent stays dark for the duration.
- **A mass simultaneous `unavailable` across the grow gear is the EXPECTED signature
  of a normal area outage.** It is not a fault, not a GFCI trip, and not a network
  failure. Don't chase it as one.
- `binary_sensor.house_power_outage` detects this — see
  `docs/power_outage_detection.md` in the **homeassistant-config** repo.
- **Diagnosing power vs network:** `switch.pc` / `switch.prusa` are Sonoff plugs fed
  *from the UPS*; the other six Sonoff plugs are on mains. Six dead while those two
  still report cannot be Sonoff and cannot be the network — it is power. The
  battery+cloud Blink tent cams are the second reference (and a live tent
  thermometer when everything else is dark).
- **`ping` from the Windows PC is useless here** — it sits on a different segment and
  cannot reach the grow devices even when they are healthy. Sweep from the HA VM.
- **After an HA restart every entity carries `last_changed` = restart time.** So any
  "offline since HH:MM" is the *restart*, not the outage, and simultaneity across
  entities is meaningless. Get true onset from the **recorder history API**.
