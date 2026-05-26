import torch
import mcp.types as types
from fastmcp import FastMCP
from sentence_transformers import SentenceTransformer

# --- Determine Device ---
if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

# --- Embedding Model ---
try:
    model_name = "multi-qa-mpnet-base-dot-v1"
    embedding_model = SentenceTransformer(model_name, device=device)
    import sys
    print(
        f"Embedding model '{model_name}' loaded on device: {device}",
        file=sys.stderr,
    )
except Exception as e:
    import sys
    print(
        f"FATAL: Failed to load embedding model on device '{device}': {e}",
        file=sys.stderr,
    )
    raise RuntimeError("Failed to load embedding model") from e


# --- MCP Server Instance ---
mcp_server = FastMCP(
    name="esphome-docs",
    version="0.1.0",
    capabilities=types.ServerCapabilities(
        tools=types.ToolsCapability(listChanged=False)
    ),
)
