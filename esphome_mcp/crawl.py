#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple crawler script for ESPHome documentation.
Crawls https://esphome.io/components/ and saves to storage/esphome.io.md
"""

import asyncio
from pathlib import Path
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode


async def crawl_esphome_docs():
    """Crawl ESPHome documentation and save to markdown."""

    storage_path = Path(__file__).parent / "storage"
    storage_path.mkdir(exist_ok=True)

    output_file = storage_path / "esphome.io.md"

    # Configure browser and crawler
    browser_config = BrowserConfig(
        headless=True,
        verbose=True,
    )

    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        markdown_generator="Default",
        wait_until="networkidle",
    )

    print("Starting ESPHome documentation crawl...")
    print(f"Target URL: https://esphome.io/components/")
    print(f"Output file: {output_file}")

    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Crawl the main components page
        result = await crawler.arun(
            url="https://esphome.io/components/",
            config=crawler_config,
        )

        if result.success:
            # Write markdown to file
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"# ESPHome Components Documentation\n\n")
                f.write(f"Source: https://esphome.io/components/\n\n")
                f.write(result.markdown_v2.raw_markdown)

            print(f"✓ Successfully crawled ESPHome documentation")
            print(f"  Saved to: {output_file}")
            print(f"  Size: {len(result.markdown_v2.raw_markdown)} characters")
        else:
            print(f"✗ Failed to crawl: {result.error_message}")
            return False

    return True


if __name__ == "__main__":
    asyncio.run(crawl_esphome_docs())
