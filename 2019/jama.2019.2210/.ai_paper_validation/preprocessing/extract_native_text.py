#!/usr/bin/env python3
"""Extract page-linked native text and record transparent quality metrics."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

import fitz


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text).replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip() for line in text.split("\n")).strip() + "\n"


def quality(text: str) -> tuple[str, dict[str, int | float]]:
    stripped = text.strip()
    non_whitespace = sum(not char.isspace() for char in text)
    replacement = text.count("\ufffd")
    control = sum(ord(char) < 32 and char not in "\n\t\r" for char in text)
    replacement_ratio = replacement / non_whitespace if non_whitespace else 0.0
    if not stripped:
        status = "missing"
    elif non_whitespace < 80:
        status = "sparse"
    elif replacement_ratio > 0.01 or control > 2:
        status = "corrupted"
    else:
        status = "acceptable"
    return status, {
        "characters": len(text),
        "non_whitespace_characters": non_whitespace,
        "replacement_characters": replacement,
        "control_characters": control,
        "replacement_ratio": replacement_ratio,
    }


def visual_flags(text: str) -> dict[str, bool]:
    return {
        "table": bool(re.search(r"\b(?:e?table)\s+\d+\b", text, re.IGNORECASE)),
        "figure": bool(re.search(r"\b(?:e?figure|fig\.)\s*\d+\b", text, re.IGNORECASE)),
        "flow_diagram": bool(re.search(r"\b(?:flow\s*(?:diagram|chart)|consort)\b", text, re.IGNORECASE)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_pdf", type=Path)
    parser.add_argument("--document-id", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    source = args.source_pdf.resolve()
    output = args.output_dir
    page_dir = output / "native_text_pages"
    page_dir.mkdir(parents=True, exist_ok=True)
    pdf = fitz.open(source)
    pages: list[dict[str, object]] = []
    whole_text: list[str] = []
    for index, page in enumerate(pdf, start=1):
        text = normalize(page.get_text("text"))
        text_path = page_dir / f"page-{index:03d}.txt"
        text_path.write_text(text, encoding="utf-8")
        extraction_quality, metrics = quality(text)
        flags = visual_flags(text)
        whole_text.append(f"\n\f\n[PDF page {index}]\n{text}")
        pages.append(
            {
                "document_id": args.document_id,
                "source_pdf": source.name,
                "source_pdf_path": str(source),
                "source_page": index,
                "source_page_reference": f"{args.document_id}:{source.name}:PDF page {index}",
                "text_path": str(text_path),
                "extraction_method": "native_pdf_text",
                "extraction_quality": extraction_quality,
                "quality_metrics": metrics,
                "visual_content_flags": flags,
                "ocr_status": "not_required_pending_visual_scope",
            }
        )
    normalized = output / "normalized_text.txt"
    normalized.write_text("".join(whole_text).lstrip(), encoding="utf-8")
    result = {
        "document_id": args.document_id,
        "source_pdf": source.name,
        "source_pdf_path": str(source),
        "page_count": len(pages),
        "normalized_text_path": str(normalized),
        "pages": pages,
    }
    (output / "native_extraction_manifest.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({"document_id": args.document_id, "pages": len(pages)}, sort_keys=True))


if __name__ == "__main__":
    main()
