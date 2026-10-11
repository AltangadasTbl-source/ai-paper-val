#!/usr/bin/env python3
"""Selective native-PDF text extraction with page-level provenance."""
from __future__ import annotations

import json
import re
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".ai_paper_validation" / "document_outputs"
SPECS = [
    ("DOC-001", "jama_bot_2019_oi_190007.pdf", range(1, 12), "main article; full scientific audit scope"),
    ("DOC-004", "joi190007supp3_prod.pdf", [1, 2, *range(16, 24)], "results supplement; priority results pages"),
]

def normalize(text: str) -> str:
    text = text.replace("\u00a0", " ").replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n"))
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

def quality(text: str) -> dict[str, object]:
    nonspace = len(re.sub(r"\s", "", text))
    readable = len(re.findall(r"[A-Za-z0-9]", text))
    replacement = text.count("\ufffd")
    control = len(re.findall(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text))
    if nonspace < 80 or readable < 40:
        assessment = "sparse"
    elif replacement or control:
        assessment = "corrupted"
    else:
        assessment = "usable"
    return {"assessment": assessment, "non_whitespace_characters": nonspace,
            "readable_alphanumeric_characters": readable, "replacement_characters": replacement,
            "control_characters": control}

for document_id, filename, pages, scope in SPECS:
    pdf = ROOT / filename
    doc = fitz.open(pdf)
    selected = list(pages)
    ddir = OUT / document_id
    tdir = ddir / "normalized_text"
    tdir.mkdir(parents=True, exist_ok=True)
    records = []
    combined = []
    for page_number in selected:
        page = doc[page_number - 1]
        text = normalize(page.get_text("text", sort=True))
        rel = f"normalized_text/page_{page_number:03d}.txt"
        (ddir / rel).write_text(text, encoding="utf-8")
        q = quality(text)
        drawings = page.get_drawings()
        images = page.get_images(full=True)
        record = {
            "source_pdf": filename, "source_pdf_page": page_number,
            "source_page_reference": f"{document_id}:{filename}:PDF p {page_number}",
            "selected_for_audit": True, "native_text_path": rel,
            "native_extraction": q, "extraction_method": "native", "ocr_required": False,
            "rendered_image_path": None, "ocr_text_path": None, "ocr_metadata_path": None,
            "vector_drawing_count": len(drawings), "embedded_image_count": len(images),
            "required_visual_for_downstream_check": "pending manual classification"
        }
        records.append(record)
        combined.append(f"\n\n===== PDF PAGE {page_number} =====\n{text}")
    (ddir / "normalized_text.txt").write_text("".join(combined).lstrip(), encoding="utf-8")
    manifest = {"schema_version": 1, "document_id": document_id, "source_pdf": filename,
                "source_pdf_page_count": len(doc), "audit_scope": scope,
                "selected_pdf_pages": selected, "excluded_pdf_pages": [i for i in range(1, len(doc)+1) if i not in selected],
                "page_records": records, "extraction_status": "native extraction complete; visual-page classification pending"}
    (ddir / "page_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    doc.close()
