#!/usr/bin/env python3
"""Create native-text artifacts and the selectively required OCR renders."""
from __future__ import annotations

import json
import re
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".ai_paper_validation"
DOCS = {
    "DOC-001": {
        "filename": "jama_kotecha_2020_oi_200126_1607962892.52158.pdf",
        "scope": "all pages 1-12 (main article)",
        "ocr_pages": {
            3: "Figure 1 participant flow diagram required for later participant-flow checks",
            5: "Table 1 required for later table-arithmetic checks",
            6: "Table 2 required for later table-arithmetic and statistical-reporting checks",
            7: "Table 3 required for later table-arithmetic and statistical-reporting checks",
            8: "Figure 2 required for later figure/flow checks",
            9: "Table 4 required for later table-arithmetic checks",
        },
    },
    "DOC-004": {
        "filename": "joi200126supp3_prod_1607962892.5372.pdf",
        "scope": "all pages 1-20 (results-relevant supplement)",
        "ocr_pages": {
            8: "eFigure 1 participant flow diagram required for later participant-flow checks",
            9: "eFigure 2 required for later figure checks",
            10: "eFigure 3 required for later figure/statistical-reporting checks",
            11: "eFigure 4 required for later figure/statistical-reporting checks",
            12: "eFigure 5 required for later figure checks",
            13: "eTable 1 required for later table-arithmetic checks",
            14: "eTable 2 required for later table-arithmetic and statistical-reporting checks",
            15: "eTable 3 required for later table-arithmetic and statistical-reporting checks",
            16: "eTable 4 required for later table-arithmetic and statistical-reporting checks",
            17: "eTable 5 required for later table-arithmetic checks",
            18: "eTable 6 required for later cross-document context checks",
        },
    },
}


def normalize(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u00ad", "").replace("\ufb01", "fi").replace("\ufb02", "fl")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text + "\n" if text else ""


def quality(text: str) -> tuple[str, list[str]]:
    visible = sum(not c.isspace() for c in text)
    replacement = text.count("\ufffd")
    controls = sum(ord(c) < 32 and c not in "\n\t\r" for c in text)
    issues: list[str] = []
    if visible < 180:
        issues.append("sparse_native_text")
    if replacement or controls:
        issues.append("corrupted_characters")
    return ("acceptable" if not issues else "limited"), issues


def main() -> None:
    manifests: dict[str, dict] = {}
    for doc_id, cfg in DOCS.items():
        source = ROOT / cfg["filename"]
        native_dir = OUT / "normalized_text" / doc_id
        image_dir = OUT / "preprocessing" / "rendered_pages" / doc_id
        native_dir.mkdir(parents=True, exist_ok=True)
        image_dir.mkdir(parents=True, exist_ok=True)
        pdf = fitz.open(source)
        document_text: list[str] = []
        pages: list[dict] = []
        for index, page in enumerate(pdf, 1):
            native = normalize(page.get_text("text", sort=True))
            text_file = native_dir / f"page-{index:03d}.txt"
            text_file.write_text(native, encoding="utf-8")
            document_text.append(f"\f\n[Source: {doc_id}, {cfg['filename']}, PDF page {index}]\n{native}")
            extraction_quality, quality_flags = quality(native)
            needs_ocr = index in cfg["ocr_pages"]
            item = {
                "pdf_page": index,
                "source_pdf": cfg["filename"],
                "source_page_reference": f"{doc_id}, {cfg['filename']}, PDF page {index}",
                "native_text_file": str(text_file.relative_to(OUT)),
                "native_text_characters": len(native),
                "native_extraction_quality": extraction_quality,
                "native_quality_flags": quality_flags,
                "extraction_method": "native_pdf_text",
                "ocr_required": needs_ocr,
            }
            if needs_ocr:
                image_file = image_dir / f"page-{index:03d}.png"
                pix = page.get_pixmap(dpi=220, alpha=False)
                pix.save(image_file)
                item.update({
                    "ocr_reason": cfg["ocr_pages"][index],
                    "rendered_image": str(image_file.relative_to(OUT)),
                    "ocr_text_file": str((OUT / "normalized_text" / doc_id / f"page-{index:03d}.ocr.txt").relative_to(OUT)),
                    "ocr_metadata_file": str((OUT / "preprocessing" / "page_ocr_metadata" / doc_id / f"page-{index:03d}.json").relative_to(OUT)),
                    "extraction_method": "native_pdf_text_plus_ocr_for_visual_structure",
                })
            pages.append(item)
        (native_dir / "document-native-normalized.txt").write_text("\n".join(document_text), encoding="utf-8")
        manifests[doc_id] = {
            "document_id": doc_id,
            "source_pdf": cfg["filename"],
            "source_page_count": len(pdf),
            "selected_page_range": cfg["scope"],
            "processing_status": "native extraction complete; OCR render set prepared",
            "pages": pages,
        }
        pdf.close()
    manifest_dir = OUT / "preprocessing" / "page_manifests"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    for doc_id, data in manifests.items():
        (manifest_dir / f"{doc_id}.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
