import os
import pickle
from pathlib import Path

# Directory where the crawled markdown files are stored
STORAGE_DIR = Path("./storage")

# Path for caching the processed chunks and embeddings
# Store it alongside the storage dir for simplicity
CACHE_FILE_PATH = STORAGE_DIR / "document_chunks_cache.pkl"

# Home Assistant configuration
# These can be overridden via environment variables: HA_URL and HA_TOKEN
HA_URL = os.getenv("HA_URL", "")
HA_TOKEN = os.getenv("HA_TOKEN", "")

# Flag to enable/disable Home Assistant integration
# Auto-enabled if both HA_URL and HA_TOKEN are provided
HA_ENABLED = bool(HA_URL and HA_TOKEN)
