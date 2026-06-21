import traceback
import sys

from esphome_mcp.app import mcp_server as mcp_app_instance
import esphome_mcp.mcp_tools  # noqa: F401

if __name__ == "__main__":
    try:
        print("Starting ESPHome MCP server on STDIO...", file=sys.stderr)
        mcp_app_instance.run(transport="stdio")
    except KeyboardInterrupt:
        print("\nServer stopped by user.", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        traceback.print_exc()
