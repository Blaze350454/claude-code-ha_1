import traceback
import sys

from esphome_mcp.app import mcp_server as mcp_app_instance
from esphome_mcp.data_loader import load_and_chunk_documents, get_all_chunks

# Import tools module to ensure decorators run
import esphome_mcp.mcp_tools  # noqa: F401

if __name__ == "__main__":
    # Load documents synchronously before starting the server
    print("Loading ESPHome documentation...", file=sys.stderr)
    load_and_chunk_documents()
    num_chunks = len(get_all_chunks())
    print(f"Document loading complete. {num_chunks} chunks loaded.", file=sys.stderr)

    try:
        print("Starting ESPHome MCP server on STDIO...", file=sys.stderr)
        mcp_app_instance.run(transport="stdio")
    except KeyboardInterrupt:
        print("\nServer stopped by user.", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        traceback.print_exc()
