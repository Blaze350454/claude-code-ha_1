import re
import pickle
import os
import sys

from typing import List, Dict, Union, Any

import numpy as np

from esphome_mcp.config import STORAGE_DIR, CACHE_FILE_PATH
from esphome_mcp.app import embedding_model

# Simple regex to find markdown headings (##, ###, etc.)
HEADING_RE = re.compile(r"^(#{2,4})\s+(.*)")
# Simple regex to find Source: URL lines
SOURCE_RE = re.compile(r"Source:\s*(https?://\S+)")

# In-memory storage for chunks
document_chunks: List[Dict[str, Union[str, np.ndarray]]] = []


def parse_markdown_to_chunks(filename: str, content: str) -> List[Dict[str, str]]:
    """
    Parses markdown content into chunks based on headings (## and deeper).

    Each chunk includes the heading, the content following it, and any
    detected Source: URL immediately after the heading.
    """
    chunks = []
    lines = content.splitlines()
    current_heading = "Introduction"
    current_content: List[str] = []
    current_source_url: Union[str, None] = None
    heading_level = 1

    for i, line in enumerate(lines):
        heading_match = HEADING_RE.match(line)
        source_match = SOURCE_RE.match(line)

        if heading_match:
            # Save previous chunk
            if current_content:
                content_str = "\n".join(current_content).strip()
                if content_str:
                    chunks.append(
                        {
                            "filename": filename,
                            "heading": current_heading,
                            "content": content_str,
                            "content_lower": content_str.lower(),
                            "heading_lower": current_heading.lower(),
                            "source_url": current_source_url or "",
                            "level": str(heading_level),
                        }
                    )

            # Start new chunk
            heading_level = len(heading_match.group(1))
            current_heading = heading_match.group(2).strip()
            current_content = []
            current_source_url = None

            # Check next line for Source: URL
            if i + 1 < len(lines):
                next_line_source_match = SOURCE_RE.match(lines[i + 1])
                if next_line_source_match:
                    current_source_url = next_line_source_match.group(1)

        elif source_match and current_heading == "Introduction":
            current_source_url = source_match.group(1)
        elif not source_match:
            current_content.append(line)

    # Add last chunk
    if current_content:
        content_str = "\n".join(current_content).strip()
        if content_str:
            chunks.append(
                {
                    "filename": filename,
                    "heading": current_heading,
                    "content": content_str,
                    "content_lower": content_str.lower(),
                    "heading_lower": current_heading.lower(),
                    "source_url": current_source_url or "",
                    "level": str(heading_level),
                }
            )

    return chunks


def load_and_chunk_documents():
    """
    Scans the STORAGE_DIR, reads .md files, parses them into chunks,
    generates embeddings, and stores them in the global document_chunks list.
    Uses a cache file to speed up subsequent loads.
    """
    global document_chunks

    # Get current state of markdown files
    current_file_metadata = {}
    if STORAGE_DIR.exists() and STORAGE_DIR.is_dir():
        for file_path in STORAGE_DIR.glob("*.md"):
            try:
                mtime = os.path.getmtime(file_path)
                current_file_metadata[file_path.name] = mtime
            except OSError as e:
                print(
                    f"Warning: Could not get metadata for {file_path.name}: {e}",
                    file=sys.stderr,
                )
                current_file_metadata = None
                break
    else:
        current_file_metadata = None

    # Try loading from cache and validate metadata
    cache_valid = False
    if current_file_metadata is not None and CACHE_FILE_PATH.exists():
        try:
            with open(CACHE_FILE_PATH, "rb") as f_cache:
                cached_metadata, cached_chunks = pickle.load(f_cache)

                if isinstance(cached_metadata, dict) and isinstance(
                    cached_chunks, list
                ):
                    if cached_metadata == current_file_metadata:
                        document_chunks = cached_chunks
                        cache_valid = True
                    else:
                        print(
                            "Cache metadata mismatch. Source files changed. "
                            "Regenerating cache.",
                            file=sys.stderr,
                        )
                else:
                    print(
                        "Warning: Cache file format is invalid. Regenerating cache.",
                        file=sys.stderr,
                    )
        except Exception as e:
            print(
                f"Warning: Failed to load or validate cache ({e}). "
                "Regenerating cache.",
                file=sys.stderr,
            )

        # Delete invalid/outdated cache file
        if not cache_valid and CACHE_FILE_PATH.exists():
            try:
                CACHE_FILE_PATH.unlink(missing_ok=True)
            except OSError as unlink_e:
                print(
                    f"Warning: Could not delete cache file: {unlink_e}",
                    file=sys.stderr,
                )

    # If cache was invalid or didn't exist, process files
    if not cache_valid:
        print(
            "Processing documents and generating embeddings...",
            file=sys.stderr,
        )
        if not STORAGE_DIR.exists() or not STORAGE_DIR.is_dir():
            print(
                f"Error: Storage directory '{STORAGE_DIR}' not found or is "
                "not a directory.",
                file=sys.stderr,
            )
            document_chunks = []
            return

        loaded_chunks = []
        for file_path in STORAGE_DIR.glob("*.md"):
            try:
                content = file_path.read_text(encoding="utf-8")
                file_chunks = parse_markdown_to_chunks(file_path.name, content)
                loaded_chunks.extend(file_chunks)
            except Exception as e:
                print(
                    f"Error processing file {file_path.name}: {e}",
                    file=sys.stderr,
                )

        # Generate Embeddings
        if loaded_chunks:
            texts_to_embed = [chunk["content"] for chunk in loaded_chunks]
            try:
                print(
                    f"Generating embeddings for {len(texts_to_embed)} chunks...",
                    file=sys.stderr,
                )
                embeddings = embedding_model.encode(
                    texts_to_embed,
                    show_progress_bar=True,
                )
                for i, chunk in enumerate(loaded_chunks):
                    chunk["embedding"] = embeddings[i]
            except Exception as e:
                print(f"Error generating embeddings: {e}", file=sys.stderr)
                for chunk in loaded_chunks:
                    chunk["embedding"] = None

        document_chunks = loaded_chunks

        # Save to cache
        if document_chunks and current_file_metadata is not None:
            print(
                f"Saving {len(document_chunks)} chunks and embeddings to "
                f"cache: {CACHE_FILE_PATH}",
                file=sys.stderr,
            )
            try:
                CACHE_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
                data_to_cache: tuple[Dict[str, float], List[Dict[str, Any]]] = (
                    current_file_metadata,
                    document_chunks,
                )
                with open(CACHE_FILE_PATH, "wb") as f_cache:
                    pickle.dump(data_to_cache, f_cache)
            except Exception as e:
                print(
                    f"Warning: Failed to save cache to {CACHE_FILE_PATH}: {e}",
                    file=sys.stderr,
                )


def get_available_documents() -> List[str]:
    """Returns a list of unique filenames that have been loaded."""
    return sorted(list(set(chunk["filename"] for chunk in document_chunks)))


def get_document_headings(filename: str) -> List[Dict[str, Union[int, str]]]:
    """Returns the heading structure for a specific document."""
    headings = []
    seen_headings = set()
    for chunk in document_chunks:
        if chunk["filename"] == filename:
            heading_key = (chunk["heading"], chunk["level"])
            if heading_key not in seen_headings:
                headings.append(
                    {
                        "level": int(chunk["level"]),
                        "title": chunk["heading"],
                    }
                )
                seen_headings.add(heading_key)
    return headings


def get_all_chunks() -> List[Dict[str, Union[str, np.ndarray]]]:
    return document_chunks
