from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".ai_paper_validation"

DOCUMENTS = {
    "DOC-001": {
        "source": "jama_zahid_2025_oi_250093_1768590553.08463.pdf",
        "scope": range(1, 10),
        # Visual evidence required by later table/figure/flow checks.
        "render": {4, 5, 6, 7},
        # Page 4 contains a locally corrupted word run in the native layer.
        "ocr": {4},
    },
    "DOC-003": {
        "source": "joi250093supp2_prod_1768590553.09463.pdf",
        "scope": range(3, 17),
        # eTables 1-10 (including continuation pages) and the eFigure.
        "render": set(range(3, 17)),
        # Page 7 has sparse native text because plot labels are graphical; pages 14
        # and 16 are sparse continuation/notes pages, so all are supplemented with OCR.
        "ocr": {7, 14, 16},
    },
}


def normalize(text: str) -> str:
    """Retain line/page structure while removing extraction-only whitespace noise."""
    lines = []
    for line in text.replace("\u00a0", " ").splitlines():
        line = re.sub(r"[ \t]+", " ", line).strip()
        if line:
            lines.append(line)
    return "\n".join(lines) + ("\n" if lines else "")


def native_quality(text: str, page_no: int, doc_id: str) -> tuple[str, list[str]]:
    chars = len(text.strip())
    words = len(re.findall(r"\S+", text))
    replacement = text.count("\ufffd")
    notes: list[str] = []
    if replacement:
        notes.append(f"{replacement} Unicode replacement character(s)")
    if chars < 500:
        notes.append("sparse native text")
    if doc_id == "DOC-001" and page_no == 4:
        notes.append("locally joined word run near participant-flow narrative")
    if replacement or chars < 500 or (doc_id == "DOC-001" and page_no == 4):
        return "moderate", notes
    return "high", notes


def render_page(page: fitz.Page, target: Path) -> None:
    # 300 dpi supports later visual checking of table cells and plot labels.
    pix = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72), alpha=False)
    pix.save(target)


def ocr_image(image: Path, target: Path, psm: int) -> str:
    result = subprocess.run(
        ["tesseract", str(image), "stdout", "-l", "eng", "--psm", str(psm)],
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    text = normalize(result.stdout)
    target.write_text(text, encoding="utf-8")
    return text


for doc_id, config in DOCUMENTS.items():
    source = ROOT / config["source"]
    doc_out = OUT / "document_outputs" / doc_id
    text_dir = doc_out / "normalized_text"
    image_dir = doc_out / "page_images"
    ocr_dir = doc_out / "ocr_text"
    for folder in (text_dir, image_dir, ocr_dir):
        folder.mkdir(parents=True, exist_ok=True)

    pdf = fitz.open(source)
    page_records = []
    combined = []
    for page_no in config["scope"]:
        page = pdf[page_no - 1]
        native = normalize(page.get_text("text"))
        native_path = text_dir / f"page-{page_no:03d}.txt"
        native_path.write_text(native, encoding="utf-8")
        quality, quality_notes = native_quality(native, page_no, doc_id)

        rendered_path = None
        if page_no in config["render"] or page_no in config["ocr"]:
            rendered_path = image_dir / f"page-{page_no:03d}.png"
            render_page(page, rendered_path)

        ocr_path = None
        ocr_words = 0
        if page_no in config["ocr"]:
            ocr_path = ocr_dir / f"page-{page_no:03d}.txt"
            ocr_text = ocr_image(rendered_path, ocr_path, 11 if (doc_id, page_no) == ("DOC-003", 7) else 6)
            ocr_words = len(re.findall(r"\S+", ocr_text))

        mode = "native" if ocr_path is None else "native_plus_ocr"
        rec = {
            "source_pdf": config["source"],
            "source_page": page_no,
            "in_audit_scope": True,
            "extraction_mode": mode,
            "native_text_path": str(native_path.relative_to(OUT)).replace("\\", "/"),
            "native_character_count": len(native.strip()),
            "native_word_count": len(re.findall(r"\S+", native)),
            "native_quality": quality,
            "quality_notes": quality_notes,
            "rendered_image_path": str(rendered_path.relative_to(OUT)).replace("\\", "/") if rendered_path else None,
            "ocr_text_path": str(ocr_path.relative_to(OUT)).replace("\\", "/") if ocr_path else None,
            "ocr_word_count": ocr_words if ocr_path else None,
            "visual_evidence": "required" if page_no in config["render"] else "not required",
        }
        page_records.append(rec)
        combined.append(f"\f\n[Source: {config['source']}, PDF page {page_no}; extraction: {mode}]\n{native}")

    (text_dir / "document-normalized.txt").write_text("\n".join(combined), encoding="utf-8")
    manifest = {
        "document_id": doc_id,
        "source_pdf": config["source"],
        "source_page_count": len(pdf),
        "selected_page_range": f"{min(config['scope'])}-{max(config['scope'])}",
        "excluded_pages": ([1, 2] if doc_id == "DOC-003" else []),
        "excluded_content_status": "Not Audited by Design" if doc_id == "DOC-003" else "None; entire main article selected",
        "native_extraction_first": True,
        "preprocessing_status": "complete",
        "pages": page_records,
    }
    (doc_out / "preprocessing_page_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    md = [
        f"# {doc_id} Preprocessing Record",
        "",
        f"- Source PDF: `{config['source']}`",
        f"- Selected source pages: {manifest['selected_page_range']}",
        "- Native PDF extraction was performed before any OCR.",
        f"- Excluded content: {manifest['excluded_content_status']}.",
        "- Page images were retained only for later-required tables, figures, or flow diagrams; OCR was limited to pages with sparse or locally corrupted native text.",
        "",
        "| PDF page | Native quality | Mode | Visual image | OCR supplement | Source-linked normalized text |",
        "|---:|---|---|---|---|---|",
    ]
    for r in page_records:
        md.append(
            f"| {r['source_page']} | {r['native_quality']} | {r['extraction_mode']} | "
            f"{r['rendered_image_path'] or '-'} | {r['ocr_text_path'] or '-'} | {r['native_text_path']} |"
        )
    (doc_out / "preprocessing_record.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    pdf.close()
