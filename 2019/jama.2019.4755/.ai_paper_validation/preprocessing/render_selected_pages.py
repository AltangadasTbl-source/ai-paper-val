"""Render only pages identified for OCR from the scoped documents."""
from __future__ import annotations

from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[2]
SPECS = (
    ("D01", "jama_brenner_2019_oi_190039.pdf", (1, 2, 3, 4, 5, 7)),
    ("D04", "joi190039supp3_prod.pdf", (4, 5, 6, 7, 8)),
)

for doc_id, filename, pages in SPECS:
    output_dir = ROOT / ".ai_paper_validation" / "document_outputs" / doc_id / "ocr_pages"
    output_dir.mkdir(parents=True, exist_ok=True)
    with fitz.open(ROOT / filename) as pdf:
        for pdf_page in pages:
            pixmap = pdf[pdf_page - 1].get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72), alpha=False)
            pixmap.save(output_dir / f"page-{pdf_page}.png")
