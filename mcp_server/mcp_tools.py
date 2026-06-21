import sys
from typing import List, Dict, Union

from mcp_server.app import mcp_server
from mcp_server.data_loader import (
    load_and_chunk_documents,
    get_available_documents,
    get_document_headings as _get_headings_from_loader,
    get_all_chunks,
)
from mcp_server.search import search_chunks

_docs_loaded = False


def _ensure_docs_loaded():
    global _docs_loaded
    if not _docs_loaded:
        load_and_chunk_documents()
        _docs_loaded = True

# --- Tool Implementations (using decorators) ---


@mcp_server.tool()
def list_documents() -> List[str]:
    """MCP Tool: Lists available documentation markdown files."""
    _ensure_docs_loaded()
    return get_available_documents()


@mcp_server.tool()
def get_document_headings(filename: str) -> List[Dict[str, Union[int, str]]]:
    """MCP Tool: Retrieves the heading structure for a specified file.

    Args:
        filename: The exact filename from list_documents.
    """
    _ensure_docs_loaded()
    available_docs = get_available_documents()
    if filename not in available_docs:
        print(f"Warning: get_document_headings called for non-existent file: {filename}", file=sys.stderr)
        return []
    return _get_headings_from_loader(filename)


@mcp_server.tool()
def search_documentation(
    query: str, filename: str = "", max_results: int = 5
) -> List[Dict[str, Union[str, float]]]:
    """MCP Tool: Searches documentation chunks based on a query.

    Args:
        query: The natural language question or search query.
        filename: Optional filename from list_documents to restrict search scope.
        max_results: Maximum sections to return (default 5, max 20).
    """
    _ensure_docs_loaded()
    max_results = max(1, min(max_results, 20))
    effective_filename = filename if filename else None
    results = search_chunks(query, effective_filename, max_results)
    return [
        {
            "filename": r["filename"],
            "heading": r["heading"],
            "content": r["content"],
            "score": float(r["score"]),
            "source_url": r.get("source_url", ""),
        }
        for r in results
    ]
