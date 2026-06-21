from typing import List, Dict, Optional, Union
import numpy as np

from mcp_server.data_loader import get_all_chunks
from mcp_server.model import get_model


def search_chunks(
    query: str, filename: Optional[str] = None, max_results: int = 5
) -> List[Dict[str, Union[str, float]]]:
    """Semantic search over loaded document chunks."""
    if not query:
        return []
    all_chunks = get_all_chunks()
    if not all_chunks:
        return []

    try:
        from sentence_transformers.util import dot_score
        query_embedding = get_model().encode(query)
    except Exception:
        return []

    results_with_scores = []

    for chunk in all_chunks:
        if filename and chunk["filename"] != filename:
            continue

        chunk_embedding = chunk.get("embedding")
        if chunk_embedding is None or not isinstance(chunk_embedding, np.ndarray):
            continue

        try:
            similarity = dot_score(query_embedding, chunk_embedding)[0][0].item()
        except Exception:
            similarity = -float("inf")

        results_with_scores.append(
            {
                "filename": chunk["filename"],
                "heading": chunk["heading"],
                "content": chunk["content"],
                "score": similarity,
                "source_url": chunk.get("source_url", ""),
            }
        )

    results_with_scores.sort(key=lambda x: x["score"], reverse=True)
    return results_with_scores[:max_results]
