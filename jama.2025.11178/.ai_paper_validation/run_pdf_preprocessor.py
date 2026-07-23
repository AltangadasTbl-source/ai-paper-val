from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import pdfplumber
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PDFTOPPM = r"C:\Users\juliz\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe"

DOCS = {
    "DOC-001-MAIN": {
        "source": "jama_debar_2025_oi_250046_1755300121.13587.pdf",
        "selected": list(range(1, 15)),
        "render": [5, 6, 7, 8, 9, 10, 11],
        "ocr": [9, 10, 11],
        "scope": "Main article pages 1-14",
    },
    "DOC-005-RESULTS": {
        "source": "joi250046supp4_prod_1755300121.15587.pdf",
        "selected": list(range(2, 19)),
        "render": [3, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18],
        "ocr": [3],
        "scope": "Results supplement pages 3-18; page 2 context only",
    },
}

def normalize(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return text.strip() + "\n" if text.strip() else ""

def quality(text: str) -> tuple[str, list[str]]:
    compact = re.sub(r"\s+", "", text)
    chars = len(compact)
    printable = sum(c.isprintable() for c in compact)
    alpha = sum(c.isalpha() for c in compact)
    reasons = []
    if chars < 250:
        reasons.append("sparse native text")
    if chars and printable / chars < 0.96:
        reasons.append("nonprintable characters")
    if chars and alpha / chars < 0.08:
        reasons.append("very low alphabetic content")
    return ("weak" if reasons else "usable"), reasons

def reconstruct_rotated_native(page) -> str:
    """Restore the readable table order for 90-degree rotated native glyph runs."""
    words = [w for w in page.extract_words(x_tolerance=1, y_tolerance=3) if w["x0"] >= 70]
    words.sort(key=lambda w: (w["x0"], w["top"]))
    rows, anchor = [], None
    for word in words:
        if anchor is None or word["x0"] - anchor > 2.0:
            rows.append([])
            anchor = word["x0"]
        rows[-1].append(word)
    return normalize("\n".join(
        " ".join(word["text"][::-1] for word in sorted(row, key=lambda w: w["top"], reverse=True))
        for row in rows
    ))

def render_page(pdf: Path, page_number: int, image: Path) -> None:
    image.parent.mkdir(parents=True, exist_ok=True)
    prefix = image.with_suffix("")
    subprocess.run([
        PDFTOPPM, "-f", str(page_number), "-l", str(page_number), "-r", "300",
        "-png", "-singlefile", str(pdf), str(prefix)
    ], check=True)

def ocr_image(image: Path, rotate_ccw: bool = False) -> str:
    target = image
    temporary = None
    if rotate_ccw:
        temporary = image.with_name(image.stem + ".ocr-rotated.png")
        with Image.open(image) as source:
            source.rotate(-90, expand=True).save(temporary)
        target = temporary
    r = subprocess.run(
        ["tesseract", str(target), "stdout", "-l", "eng", "--psm", "6"],
        check=False, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if temporary:
        temporary.unlink(missing_ok=True)
    return normalize(r.stdout)

def write_document(docid: str, cfg: dict) -> None:
    source = ROOT / cfg["source"]
    out = ROOT / ".ai_paper_validation" / "document_outputs" / docid
    text_dir = out / "normalized_text"
    image_dir = out / "page_images"
    text_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    with pdfplumber.open(source) as pdf:
        for p in cfg["selected"]:
            native = normalize(pdf.pages[p - 1].extract_text(x_tolerance=1, y_tolerance=3) or "")
            status, reasons = quality(native)
            corrupt_rotated_native = docid == "DOC-001-MAIN" and p in {9, 10, 11}
            if corrupt_rotated_native:
                status = "corrupted"
                reasons.append("native text is reversed/rotated on the table page")
            image_rel = None
            ocr = ""
            if p in cfg["render"]:
                image = image_dir / f"page_{p:03d}.png"
                if not image.exists():
                    render_page(source, p, image)
                image_rel = image.relative_to(ROOT / ".ai_paper_validation").as_posix()
            if p in cfg["ocr"]:
                if image_rel is None:
                    image = image_dir / f"page_{p:03d}.png"
                    if not image.exists():
                        render_page(source, p, image)
                    image_rel = image.relative_to(ROOT / ".ai_paper_validation").as_posix()
                else:
                    image = image_dir / f"page_{p:03d}.png"
                existing_ocr = text_dir / f"page_{p:03d}.ocr.txt"
                ocr = existing_ocr.read_text(encoding="utf-8") if existing_ocr.exists() else ocr_image(image, rotate_ccw=corrupt_rotated_native)
            # OCR is retained as supplemental text; it becomes canonical only where native table text is corrupt.
            canonical = native
            method = "native"
            if p in cfg["ocr"]:
                (text_dir / f"page_{p:03d}.ocr.txt").write_text(ocr, encoding="utf-8")
                method = "native+ocr"
            if corrupt_rotated_native:
                (text_dir / f"page_{p:03d}.native.txt").write_text(native, encoding="utf-8")
                canonical = reconstruct_rotated_native(pdf.pages[p - 1])
                method = "native coordinate reconstruction+ocr check"
            (text_dir / f"page_{p:03d}.txt").write_text(canonical, encoding="utf-8")
            notes = reasons[:]
            if p in cfg["render"]:
                notes.append("rendered because it contains a result-relevant table, figure, or flow diagram")
            if p in cfg["ocr"]:
                notes.append("native coordinate reconstruction selected as canonical normalized text; raw native and OCR check text retained" if corrupt_rotated_native else "OCR retained as supplemental recovery/check text")
            if docid == "DOC-005-RESULTS" and p == 2:
                notes.append("context-only page; excluded from scientific result checks unless needed")
            manifest.append({
                "source_pdf": cfg["source"], "source_page": p, "selected_scope": True,
                "native_characters": len(re.sub(r"\s+", "", native)), "native_quality": status,
                "native_quality_notes": reasons, "extraction_method": method,
                "normalized_text": f"document_outputs/{docid}/normalized_text/page_{p:03d}.txt",
                "native_text": (f"document_outputs/{docid}/normalized_text/page_{p:03d}.native.txt" if corrupt_rotated_native else None),
                "ocr_text": (f"document_outputs/{docid}/normalized_text/page_{p:03d}.ocr.txt" if p in cfg["ocr"] else None),
                "image": image_rel, "notes": notes,
            })
    (out / "page_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    lines = ["# Page-Level Extraction Manifest", "", f"- Document ID: {docid}", f"- Source PDF: `{cfg['source']}`", f"- Selected scope: {cfg['scope']}", "", "| PDF page | Native quality | Method | Normalized text | Image | Notes |", "|---:|---|---|---|---|---|"]
    for m in manifest:
        notes = "; ".join(m["notes"]) if m["notes"] else "-"
        lines.append(f"| {m['source_page']} | {m['native_quality']} ({m['native_characters']} nonspace chars) | {m['extraction_method']} | `{m['normalized_text']}` | {('`' + m['image'] + '`') if m['image'] else '-'} | {notes} |")
    (out / "page_manifest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    record = f"""# PDF Preprocessing Record

- Document ID: {docid}
- Source PDF: `{cfg['source']}` (read only; unchanged)
- Selected extraction scope: {cfg['scope']}
- Native extraction: completed for every selected page before rendering/OCR.
- Rendering: selective, limited to pages containing result-relevant tables, figures, or flow diagrams.
- OCR: selective, limited to pages with corrupted, sparse, or visually required text; supplemental OCR text is retained beside canonical native extraction.
- Page-level source references, quality assessment, and derived artifact paths: `page_manifest.md` and `page_manifest.json`.
- Processing status: Complete.
"""
    (out / "preprocessing_record.md").write_text(record, encoding="utf-8")

def write_not_audited(docid: str, source: str, classification: str, scope: str) -> None:
    out = ROOT / ".ai_paper_validation" / "document_outputs" / docid
    record = f"""# PDF Preprocessing Record

- Document ID: {docid}
- Source PDF: `{source}` (read only; unchanged)
- Classification: {classification}
- Extraction/OCR scope: Not Audited by Design.
- Processing status: No scientific-content extraction, rendering, or OCR performed. This document may be opened only for a specific parent-requested comparison.
- Rights-screen status: retained separately in `rights_record.md`.
"""
    (out / "preprocessing_record.md").write_text(record, encoding="utf-8")

for ident, settings in DOCS.items():
    write_document(ident, settings)
# Page 12 of the results supplement contains only the repeating rights footer; no image/OCR is retained.
for stale in [
    ROOT / ".ai_paper_validation" / "document_outputs" / "DOC-005-RESULTS" / "page_images" / "page_012.png",
    ROOT / ".ai_paper_validation" / "document_outputs" / "DOC-005-RESULTS" / "normalized_text" / "page_012.ocr.txt",
]:
    stale.unlink(missing_ok=True)
write_not_audited("DOC-002-PROTOCOL", "joi250046supp1_prod_1755300121.14087.pdf", "Protocol", "Not Audited by Design")
write_not_audited("DOC-003-SAP", "joi250046supp2_prod_1755300121.15087.pdf", "Statistical analysis plan", "Not Audited by Design")
write_not_audited("DOC-004-INTERVENTION", "joi250046supp3_prod_1755300121.15087.pdf", "Intervention description / TIDieR", "Not Audited by Design")

out = ROOT / ".ai_paper_validation" / "document_outputs" / "DOC-006-XLSX"
(out / "preprocessing_record.md").write_text("""# Preprocessing Record

- Document ID: DOC-006-XLSX
- Source artifact: `joi250046supp5_prod_1755300121.16087.xlsx` (read only; unchanged)
- Processing status: Not a PDF; no PDF preprocessing performed. Native workbook cells are reserved for the results-supplement extractor and downstream checkers.
""", encoding="utf-8")
