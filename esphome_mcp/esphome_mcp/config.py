import os
import pickle
from pathlib import Path

# Directory where the crawled markdown files are stored
STORAGE_DIR = Path("./storage")

# Path for caching the processed chunks and embeddings
CACHE_FILE_PATH = STORAGE_DIR / "document_chunks_cache.pkl"

# ESPHome dashboard HTTP API
ESPHOME_DASHBOARD_URL = os.environ.get("ESPHOME_DASHBOARD_URL", "http://192.168.2.14:6052")
