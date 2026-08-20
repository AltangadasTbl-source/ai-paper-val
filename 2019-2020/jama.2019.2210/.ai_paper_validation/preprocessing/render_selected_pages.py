#!/usr/bin/env python3
"""Render an explicit PDF-page list to PNG without modifying the source PDF."""

from __future__ import annotations

import argparse
from pathlib import Path

import fitz


def parse_pages(value: str) -> list[int]:
    values: list[int] = []
    for part in value.split(","):
        part = part.strip()
        if "-" in part:
            start, end = (int(item) for item in part.split("-", 1))
            values.extend(range(start, end + 1))
        elif part:
            values.append(int(part))
    return sorted(set(values))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_pdf", type=Path)
    parser.add_argument("--pages", required=True, help="Comma-separated pages/ranges, one-based.")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--scale", type=float, default=2.0)
    args = parser.parse_args()
    pdf = fitz.open(args.source_pdf)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    matrix = fitz.Matrix(args.scale, args.scale)
    for page_number in parse_pages(args.pages):
        if not 1 <= page_number <= len(pdf):
            parser.error(f"Page {page_number} outside document range 1-{len(pdf)}")
        pixmap = pdf[page_number - 1].get_pixmap(matrix=matrix, alpha=False)
        pixmap.save(args.output_dir / f"page-{page_number:03d}.png")


if __name__ == "__main__":
    main()
