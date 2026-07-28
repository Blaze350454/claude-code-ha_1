# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Grow Home** is the umbrella repo for all of the home garden/grow automation projects — a single home for tooling and configs that grows as new grow systems (tent, tower, future builds) are added over time. It currently holds these independent but related sub-projects:

1. **MCP Server** (`mcp_server/`) — A FastMCP server that combines semantic search over crawled documentation with live Home Assistant control via REST API. Consumed by AI agents (Claude Code, Cursor) over stdio.
2. **ESPHome MCP** (`esphome_mcp/`) — A separate, self-contained MCP server specifically for ESPHome documentation. Has its own `pyproject.toml` and `uv` environment.
3. **Grow Tent Automation** (`grow_tent_automation/`) — HA YAML configs for the tent irrigation system. `grow_tent_package.yaml` is the main HA package. Hardware/entity documentation is in `docs/tent_irrigation_esphome.md`.

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

## Home Assistant / Grow System Context

- HA instance: `http://192.168.2.151:8123`
- HS300 power strip pumps are controlled via a custom cloud-API service running on the Ubuntu VM (port 8765), not via the native TP-Link integration (firmware broke local auth).
- KP303 (`192.168.2.182`, MAC suffix `c074`, HA name "Power Strip Tent") is currently an unplugged spare — integration kept for future use; outlets renamed `Blank 4/5/6`. Works via native TP-Link integration when powered. (MAC verified 2026-06-16 — an earlier `53db` here was wrong; don't "correct" it back.)
- ESP32 device `tent-irrigation-controller` exposes float switches, solenoid valves, and DS18B20 sensors to HA via ESPHome.
- Full irrigation entity IDs and HS300 outlet mappings: see `MEMORY.md` and `grow_tent_automation/docs/tent_irrigation_esphome.md`.
- HA config on host VM: `/home/homeadmin/homeassistant/.config/configuration.yaml`
