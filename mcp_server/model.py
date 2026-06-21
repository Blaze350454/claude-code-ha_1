import sys

_embedding_model = None


def get_model():
    global _embedding_model
    if _embedding_model is None:
        import torch
        from sentence_transformers import SentenceTransformer
        device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Loading embedding model on {device}...", file=sys.stderr)
        _embedding_model = SentenceTransformer("multi-qa-mpnet-base-dot-v1", device=device)
        print("Embedding model ready.", file=sys.stderr)
    return _embedding_model
