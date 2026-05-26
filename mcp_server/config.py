import os
import pickle
from pathlib import Path

# Directory where the crawled markdown files are stored
STORAGE_DIR = Path("./storage")

# Path for caching the processed chunks and embeddings
# Store it alongside the storage dir for simplicity
CACHE_FILE_PATH = STORAGE_DIR / "document_chunks_cache.pkl"

# Home Assistant configuration
HA_URL = os.getenv("HA_URL", "")
HA_TOKEN = os.getenv("HA_TOKEN", "")
HA_ENABLED = bool(HA_URL and HA_TOKEN)

# Proxmox configuration
PROXMOX_URL = os.getenv("PROXMOX_URL", "")
PROXMOX_USER = os.getenv("PROXMOX_USER", "root@pam")
PROXMOX_PASSWORD = os.getenv("PROXMOX_PASSWORD", "")
PROXMOX_NODE = os.getenv("PROXMOX_NODE", "proxmox")
PROXMOX_ENABLED = bool(PROXMOX_URL and PROXMOX_PASSWORD)
