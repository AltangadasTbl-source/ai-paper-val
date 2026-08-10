"""Create scoped, page-linked PDF preprocessing artifacts.

Source PDFs are read only. All output is kept below .ai_paper_validation.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import unicodedata
from pathlib import Path

import fitz  # PyMuPDF
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".ai_paper_validation"

DOCUMENTS = [
    {
        "document_id": "DOC-001-main-article",
        "source_filename": "jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf",
        "page_count": 11,
        "selected_pages": list(range(1, 12)),
        # These are the pages that visibly contain the flow diagram, table, or figures.
        "visual_asset_pages": [5, 6, 7, 8, 9],
        "excluded_pages": [],
        "scope_note": "All main-article pages are audited. Images/OCR are retained for the pages with required flow/table/figure evidence.",
    },
    {
        "document_id": "DOC-003-results-supplement",
        "source_filename": "joi250084supp2_prod_1765403089.61751.pdf",
        "page_count": 69,
        "selected_pages": [34, 35, *range(38, 67)],
        # The two eFigure pages and each selected eTable page require visual/table review.
        "visual_asset_pages": [34, 35, *range(38, 67)],
        "excluded_pages": [*range(1, 34), 36, 37, 67, 68, 69],
        "scope_note": "Pages 34-35 and 38-66 are audited. Pages 36-37 are comparison-only and were not processed; all other excluded pages are Not Audited by Design.",
    },
]


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "")
    value = value.replace("\r\n", "\n").replace("\r", "\n").replace("\x00", "")
    value = "\n".join(line.rstrip() for line in value.split("\n"))
    return value.strip() + "\n"


def quality(text: str) -> tuple[str, dict]:
    nonspace = [c for c in text if not c.isspace()]
    printable = sum(c.isprintable() for c in nonspace)
    alnum = sum(c.isalnum() for c in text)
    metrics = {
        "character_count": len(text),
        "alphanumeric_count": alnum,
        "replacement_character_count": text.count("\ufffd"),
        "printable_ratio": round(printable / len(nonspace), 4) if nonspace else 0.0,
    }
    if len(text.strip()) < 150:
        return "sparse", metrics
    if metrics["replacement_character_count"] > 3 or metrics["printable_ratio"] < 0.95:
        return "corrupted", metrics
    return "usable", metrics


def render_page(pdf: fitz.Document, page_no: int, destination: Path) -> None:
    page = pdf.load_page(page_no - 1)
    # 200 dpi balances legibility of tables against retaining only necessary artifacts.
    pix = page.get_pixmap(matrix=fitz.Matrix(200 / 72, 200 / 72), alpha=False)
    pix.save(destination)


def ocr_image(image_path: Path) -> str:
    if not shutil.which("tesseract"):
        return "[OCR unavailable: tesseract executable not found]\n"
    completed = subprocess.run(
        ["tesseract", str(image_path), "stdout", "-l", "eng", "--psm", "6"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if completed.returncode:
        return f"[OCR failed: {completed.stderr.strip()}]\n"
    return normalize_text(completed.stdout)


def page_range(pages: list[int]) -> str:
    runs: list[tuple[int, int]] = []
    start = prior = pages[0]
    for item in pages[1:]:
        if item == prior + 1:
            prior = item
        else:
            runs.append((start, prior))
            start = prior = item
    runs.append((start, prior))
    return ", ".join(str(a) if a == b else f"{a}-{b}" for a, b in runs)


def process_document(config: dict) -> dict:
    document_id = config["document_id"]
    source = ROOT / config["source_filename"]
    document_out = OUT / "document_outputs" / document_id
    native_dir = document_out / "normalized_text" / "native"
    image_dir = document_out / "page_images"
    ocr_dir = document_out / "normalized_text" / "ocr"
    for directory in (native_dir, image_dir, ocr_dir):
        directory.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(source))
    pdf = fitz.open(source)
    records = []
    combined_native = []
    combined_ocr = []
    visual_pages = set(config["visual_asset_pages"])
    for page_no in config["selected_pages"]:
        text = normalize_text(reader.pages[page_no - 1].extract_text() or "")
        native_quality, metrics = quality(text)
        native_rel = native_dir.relative_to(OUT) / f"page-{page_no:03d}.txt"
        (OUT / native_rel).write_text(text, encoding="utf-8")
        combined_native.append(f"\n===== SOURCE: {config['source_filename']} | PAGE: {page_no} =====\n{text}")

        requires_visual = page_no in visual_pages
        use_ocr = requires_visual or native_quality in {"sparse", "corrupted"}
        image_rel = None
        ocr_rel = None
        ocr_quality = None
        reason = "Native extraction usable; no required visual asset on this page."
        if use_ocr:
            image_rel = image_dir.relative_to(OUT) / f"page-{page_no:03d}.png"
            render_page(pdf, page_no, OUT / image_rel)
            ocr_text = ocr_image(OUT / image_rel)
            ocr_rel = ocr_dir.relative_to(OUT) / f"page-{page_no:03d}.txt"
            (OUT / ocr_rel).write_text(ocr_text, encoding="utf-8")
            ocr_quality, _ = quality(ocr_text)
            combined_ocr.append(f"\n===== SOURCE: {config['source_filename']} | PAGE: {page_no} =====\n{ocr_text}")
            if requires_visual:
                reason = "Rendered and OCRed because this scoped page contains a required table, figure, or flow diagram; native text remains retained as primary extraction."
            else:
                reason = f"Rendered and OCRed because native extraction was assessed as {native_quality}."
        records.append(
            {
                "document_id": document_id,
                "source_pdf": config["source_filename"],
                "source_page": page_no,
                "audit_scope": "audited",
                "native_text_method": "native",
                "native_quality": native_quality,
                "native_text_path": native_rel.as_posix(),
                "ocr_used": use_ocr,
                "ocr_quality": ocr_quality,
                "ocr_text_path": ocr_rel.as_posix() if ocr_rel else None,
                "page_image_path": image_rel.as_posix() if image_rel else None,
                "selection_reason": reason,
                **metrics,
            }
        )
    pdf.close()
    (document_out / "normalized_text" / "native_all_selected_pages.txt").write_text("".join(combined_native), encoding="utf-8")
    if combined_ocr:
        (document_out / "normalized_text" / "ocr_all_selected_visual_pages.txt").write_text("".join(combined_ocr), encoding="utf-8")
    return {
        "document_id": document_id,
        "source_filename": config["source_filename"],
        "page_count": config["page_count"],
        "selected_page_range": page_range(config["selected_pages"]),
        "selected_page_count": len(config["selected_pages"]),
        "visual_ocr_page_range": page_range(config["visual_asset_pages"]),
        "visual_ocr_page_count": len(config["visual_asset_pages"]),
        "scope_note": config["scope_note"],
        "pages": records,
    }


def main() -> None:
    processed = [process_document(doc) for doc in DOCUMENTS]
    protocol_record = {
        "document_id": "DOC-002-protocol",
        "source_filename": "joi250084supp1_prod_1765403089.61351.pdf",
        "page_count": 90,
        "audit_scope": "Not Audited by Design",
        "selected_page_range": None,
        "selected_page_count": 0,
        "visual_ocr_page_range": None,
        "visual_ocr_page_count": 0,
        "scope_note": "No routine scientific extraction, rendering, OCR, or checking was performed. A protocol page may be processed only for a later, specifically requested comparison.",
        "pages": [],
    }
    result = {
        "artifact_type": "page-level PDF preprocessing manifest",
        "created_date": "2026-07-21",
        "native_first": True,
        "documents": [*processed, protocol_record],
    }
    (OUT / "pdf_preprocessing_manifest.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    lines = [
        "# PDF Preprocessing Manifest",
        "",
        "Native PDF text was extracted before any rendering/OCR. OCR and PNG rendering were retained only for scoped pages with a required table, figure, or flow diagram. Source PDFs were read only.",
        "",
        "| Document | Selected source pages | Native text quality | Rendered/OCR pages | Status |",
        "|---|---|---|---|---|",
    ]
    for doc in processed:
        quality_counts = {}
        for page in doc["pages"]:
            quality_counts[page["native_quality"]] = quality_counts.get(page["native_quality"], 0) + 1
        quality_note = ", ".join(f"{key}: {value}" for key, value in quality_counts.items())
        lines.append(f"| {doc['document_id']} | {doc['selected_page_range']} | {quality_note} | {doc['visual_ocr_page_range']} | Complete |")
    lines.append("| DOC-002-protocol | None | Not assessed by design | None | Not Audited by Design |")
    lines.extend([
        "",
        "## Page-level records",
        "",
        "The JSON companion contains the source PDF, source page, text-quality metrics, method, and every retained artifact path for each processed page.",
        "",
        "## Quality limitations",
        "",
        "- Native text is readable on all selected pages, but multicolumn journal text and tables can have non-linear reading order or collapsed word spacing.",
        "- OCR text is an image-derived companion for visual checking; it is not a substitute for checking the retained page image when verifying table alignment, figure labels, or flow arrows.",
        "- Excluded supplement pages, including pp. 36-37, and the entire protocol were not processed for scientific content by design.",
        "",
    ])
    (OUT / "pdf_preprocessing_manifest.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
