# mcp_server/

Internals of the FastMCP server (semantic doc search + live Home Assistant
control over stdio). Moved out of the root `CLAUDE.md` so it loads only when
working in this package.

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
