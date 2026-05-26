import sys
from typing import List, Dict, Union

from esphome_mcp.app import mcp_server
from esphome_mcp.data_loader import (
    get_available_documents,
    get_document_headings as _get_headings_from_loader,
)
from esphome_mcp.search import search_chunks


@mcp_server.tool()
def list_documents() -> List[str]:
    """MCP Tool: Lists available ESPHome documentation markdown files."""
    return get_available_documents()


@mcp_server.tool()
def get_document_headings(filename: str) -> List[Dict[str, Union[int, str]]]:
    """MCP Tool: Retrieves the heading structure for a specified file.

    Args:
        filename: The exact filename from list_documents.
    """
    available_docs = get_available_documents()
    if filename not in available_docs:
        print(
            f"Warning: get_document_headings called for non-existent file: {filename}",
            file=sys.stderr,
        )
        return []
    return _get_headings_from_loader(filename)


@mcp_server.tool()
def search_documentation(
    query: str, filename: str = "", max_results: int = 5
) -> List[Dict[str, Union[str, float]]]:
    """
    MCP Tool: Searches ESPHome documentation chunks based on a query.

    Returns a list of dicts with filename, heading, content snippet, score,
    and source_url.

    Args:
        query: The natural language question or search query.
        filename: Optional. The specific filename (from list_documents) to
                  search within. If empty, searches all documents.
        max_results: Optional. Maximum number of relevant sections to return
                     (default 5, max 20).
    """
    if max_results < 1:
        max_results = 1
    if max_results > 20:
        max_results = 20

    effective_filename = filename if filename else None

    search_results = search_chunks(query, effective_filename, max_results)

    formatted_results = []
    for res in search_results:
        formatted_results.append(
            {
                "filename": res["filename"],
                "heading": res["heading"],
                "content": res["content"],
                "score": float(res["score"]),
                "source_url": res.get("source_url", ""),
            }
        )

    return formatted_results
