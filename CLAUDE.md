# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Two independent but related sub-projects live here:

1. **MCP Server** (`mcp_server/`) — A FastMCP server that combines semantic search over crawled documentation with live Home Assistant control via REST API. Consumed by AI agents (Claude Code, Cursor) over stdio.
2. **ESPHome MCP** (`esphome_mcp/`) — A separate, self-contained MCP server specifically for ESPHome documentation. Has its own `pyproject.toml` and `uv` environment.
3. **Grow Tent Automation** (`grow_tent_automation/`) — HA YAML configs for the irrigation system. `grow_tent_package.yaml` is the main HA package. Hardware/entity documentation is in `docs/tent_irrigation_esphome.md`.

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

### MCP Server Startup Sequence

`main.py` → imports `app.py` (loads `SentenceTransformer` model, creates `FastMCP` instance) → calls `load_and_chunk_documents()` → imports `mcp_tools` and `ha_tools` (tool decorators self-register on the `FastMCP` instance) → `mcp_app_instance.run(transport="stdio")`.

**Critical:** Tool registration happens via `@mcp_server.tool()` decorators at import time. The imports in `main.py` (`import mcp_server.mcp_tools` and `import mcp_server.ha_tools`) must happen before `mcp_app_instance.run()`.

### Document Chunking and Embedding

`data_loader.py` parses `.md` files in `storage/` by splitting on `##`/`###`/`####` headings. Each chunk stores `filename`, `heading`, `content`, `source_url`, `level`, and a `numpy` embedding vector. The cache (`storage/document_chunks_cache.pkl`) stores `(file_metadata_dict, chunks_list)` as a pickle tuple and is invalidated when any `.md` file's mtime changes.

Embedding model: `multi-qa-mpnet-base-dot-v1`. Search uses dot-product similarity (not cosine) — this is intentional for this model.

### Home Assistant Integration

`ha_client.py` is a thin async `aiohttp` wrapper around the HA REST API. `ha_tools.py` registers MCP tools and creates one `HomeAssistantClient` instance at module import time if `HA_URL` and `HA_TOKEN` env vars are set. If either is missing, all `ha_*` tools raise `RuntimeError` when called.

HA credentials are passed via environment variables only — never hardcoded. For Cursor, set them in `.cursor/mcp.json` under `env`.

### Configuration

`mcp_server/config.py` reads `HA_URL` and `HA_TOKEN` from env and sets `STORAGE_DIR = Path("./storage")`. The server must be launched from the project root so relative paths resolve correctly.

## Tagging Standard (READ BEFORE ADDING ENTITIES)

Every HA entity/device/automation/script/helper follows the v1 tagging taxonomy documented at **`D:\Claude\Projects\homeassistant-config\docs\tagging_standard.md`**. Consult it before creating or migrating anything in HA — it defines the `sys_` / `sub_` / `fn_` / `sev_` label prefixes, required labels per entity, area vs label rules, and severity triage.

Migration tooling lives in this repo:
- `tag_migration_phase1a.py` — idempotent migrator (dry-run default, `--apply` commits)
- `registry_export.py` — pre/post-migration JSON snapshots under `migration_snapshots/<timestamp>[_label]/`

## Home Assistant / Grow Tent Context

- HA instance: `http://192.168.2.151:8123`
- HS300 power strip pumps are controlled via a custom cloud-API service running on the Ubuntu VM (port 8765), not via the native TP-Link integration (firmware broke local auth).
- KP303 (`192.168.2.182`, MAC suffix `53db`, HA name "Power Strip Tent") is currently an unplugged spare — integration kept for future use; outlets renamed `Blank 4/5/6`. Works via native TP-Link integration when powered.
- ESP32 device `tent-irrigation-controller` exposes float switches, solenoid valves, and DS18B20 sensors to HA via ESPHome.
- Full irrigation entity IDs and HS300 outlet mappings: see `MEMORY.md` and `grow_tent_automation/docs/tent_irrigation_esphome.md`.
- HA config on host VM: `/home/homeadmin/homeassistant/.config/configuration.yaml`
