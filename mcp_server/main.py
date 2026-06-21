import traceback
import sys  # Import sys for stderr usage

# Import the shared FastMCP instance
from mcp_server.app import mcp_server as mcp_app_instance

# Import the data loading function and chunk access function
from mcp_server.data_loader import load_and_chunk_documents, get_all_chunks

# Import the tools modules to ensure decorators run and register tools
import mcp_server.mcp_tools  # noqa: F401
import mcp_server.ha_tools  # noqa: F401
import mcp_server.proxmox_tools  # noqa: F401

# --- Main Execution (for direct run `python -m mcp_server.main`) ---
if __name__ == "__main__":
    try:
        print("Starting MCP server on STDIO...", file=sys.stderr)
        # Call run directly on the imported instance
        mcp_app_instance.run(transport="stdio")
    except KeyboardInterrupt:
        print("\nServer stopped by user.", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        # Print the full traceback to see the sub-exception details
        traceback.print_exc()  # Prints to stderr by default
