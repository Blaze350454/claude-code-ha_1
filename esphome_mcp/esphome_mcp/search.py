from typing import List, Dict, Optional, Union
import numpy as np

from sentence_transformers.util import dot_score

from esphome_mcp.app import embedding_model
from esphome_mcp.data_loader import get_all_chunks


def search_chunks(
    query: str, filename: Optional[str] = None, max_results: int = 5
) -> List[Dict[str, Union[str, float]]]:
    """
    Performs semantic search over the loaded document chunks using embeddings.
    """
    if not query:
        return []
    all_chunks = get_all_chunks()
    if not all_chunks:
        return []

    # Generate embedding for the query
    try:
        query_embedding = embedding_model.encode(query)
    except Exception as e:
        return []

    results_with_scores = []

    for idx, chunk in enumerate(all_chunks):
        # Filter by filename if provided
        if filename and chunk["filename"] != filename:
            continue

        # Check if chunk has an embedding
        chunk_embedding = chunk.get("embedding")
        if chunk_embedding is None or not isinstance(chunk_embedding, np.ndarray):
            continue

        # Calculate dot product similarity
        try:
            similarity = dot_score(query_embedding, chunk_embedding)[0][0].item()
        except Exception as e:
            similarity = -float("inf")

        # Store results with scores
        results_with_scores.append(
            {
                "filename": chunk["filename"],
                "heading": chunk["heading"],
                "content": chunk["content"],
                "score": similarity,
                "source_url": chunk.get("source_url", ""),
            }
        )

    # Sort results by score (descending)
    results_with_scores.sort(key=lambda x: x["score"], reverse=True)

    return results_with_scores[:max_results]
