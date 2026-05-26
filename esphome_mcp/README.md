# ESPHome MCP Server

This project provides an MCP server for searching ESPHome documentation, designed for integration with Claude Code and other MCP clients.

## Features

- **Web Crawler**: Crawls ESPHome documentation from https://esphome.io/components/
- **MCP Server**: Provides semantic search over ESPHome component documentation
- **Vector Embeddings**: Uses sentence-transformers for accurate semantic search
- **Caching**: Fast startup times with intelligent caching

## Setup

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency management.

1. **Install dependencies:**

   ```bash
   cd "/d/Claude/Projects/Container Home/esphome_mcp"
   uv sync
   ```

## Usage

### 1. Crawl ESPHome Documentation

```bash
uv run python crawl.py https://esphome.io/components/
```

This will crawl the ESPHome component documentation and save it to `./storage/esphome.io.md`.

### 2. Run the MCP Server

The MCP server is designed to run via `stdio` transport for use with Claude Code:

```bash
python -m esphome_mcp.main
```

### 3. Configure Claude Code

Add this to your `.claude.json`:

```json
{
  "mcpServers": {
    "esphome": {
      "command": "uv",
      "args": [
        "--directory",
        "D:\\Claude\\Projects\\Container Home\\esphome_mcp",
        "run",
        "python",
        "-m",
        "esphome_mcp.main"
      ],
      "env": {}
    }
  }
}
```

## MCP Tools

The server exposes these tools:

- `list_documents`: List available ESPHome documentation files
- `get_document_headings`: Get the heading structure of a document
- `search_documentation`: Semantic search across ESPHome documentation

## Dependencies

- `crawl4ai`: Web crawling
- `fastmcp`: MCP server implementation
- `sentence-transformers`: Text embeddings
- `torch`: Required by sentence-transformers
- `typer`: CLI tool
- `uv`: Project management

## License

MIT License
