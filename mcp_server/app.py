import mcp.types as types
from fastmcp import FastMCP

mcp_server = FastMCP(
    name="doc-query-server",
    version="0.1.0",
    capabilities=types.ServerCapabilities(
        tools=types.ToolsCapability(listChanged=False)
    ),
)
