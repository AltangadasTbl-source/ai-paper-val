#!/usr/bin/env python3
"""Render specified 1-based PDF pages as PNG images for selective OCR."""

from __future__ import annotations

import sys
from pathlib import Path

import fitz


def main() -> None:
    pdf = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    page_numbers = [int(value) for value in sys.argv[3].split(",")]
    out_dir.mkdir(parents=True, exist_ok=True)
    document = fitz.open(pdf)
    matrix = fitz.Matrix(300 / 72, 300 / 72)
    for number in page_numbers:
        page = document[number - 1]
        pixmap = page.get_pixmap(matrix=matrix, alpha=False)
        pixmap.save(out_dir / f"page-{number:03d}.png")


if __name__ == "__main__":
    main()
