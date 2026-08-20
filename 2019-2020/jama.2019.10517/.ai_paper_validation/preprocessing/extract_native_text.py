#!/usr/bin/env python3
"""Extract per-page native PDF text with lightweight quality measurements."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import fitz


def main() -> None:
    pdf = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    document = fitz.open(pdf)
    pages: list[dict[str, object]] = []
    for index, page in enumerate(document, start=1):
        text = page.get_text("text", sort=True)
        text_path = out_dir / f"page-{index:03d}.txt"
        text_path.write_text(text, encoding="utf-8")
        blocks = page.get_text("blocks", sort=True)
        words = page.get_text("words", sort=True)
        images = page.get_images(full=True)
        drawings = page.get_drawings()
        alphanumeric = sum(character.isalnum() for character in text)
        replacement_chars = text.count("\ufffd")
        pages.append(
            {
                "pdf_page": index,
                "source_pdf": pdf.name,
                "native_text_file": str(text_path),
                "native_text_characters": len(text),
                "native_alphanumeric_characters": alphanumeric,
                "native_text_blocks": len(blocks),
                "native_words": len(words),
                "embedded_images": len(images),
                "vector_drawings": len(drawings),
                "replacement_characters": replacement_chars,
            }
        )
    (out_dir / "native_extraction_quality.json").write_text(
        json.dumps({"source_pdf": pdf.name, "pages": pages}, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
