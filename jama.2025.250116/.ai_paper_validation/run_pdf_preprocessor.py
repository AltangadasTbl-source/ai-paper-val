from __future__ import annotations

import json
import re
import shutil
import subprocess
import unicodedata
from datetime import date
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".ai_paper_validation" / "document_outputs"
PDFTOPPM = str(Path(r"C:\Users\juliz\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe"))
TESSERACT = shutil.which("tesseract.exe") or shutil.which("tesseract")

DOCS = [
    {
        "id": "DOC-001-MAIN",
        "source": "jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf",
        "pages": list(range(1, 10)),
        "visual_pages": {3: "Figure 1 participant flow", 4: "Table 1", 5: "Table 1 continued", 6: "Table 2", 7: "Figure 2", 8: "Table 3"},
        "excluded": "Pages 10-12 were not extracted, rendered, or OCR processed: context only unless specifically needed.",
    },
    {
        "id": "DOC-003-RESULTS-SUPP",
        "source": "joi250116supp2_prod_1771885794.27755.pdf",
        "pages": list(range(6, 9)) + list(range(14, 54)),
        "visual_pages": {**{p: "eTable 1" for p in range(6, 9)}, **{p: "eTables 5-15" for p in range(14, 45)}, **{p: "eFigures 1-9" for p in range(45, 54)}},
        "excluded": "Pages 1-5, 9-13, and 54 were not extracted, rendered, or OCR processed: context/nonroutine targets by design.",
    },
]


def normalized(text: str) -> str:
    """Preserve source wording while normalizing unicode form and line endings."""
    text = unicodedata.normalize("NFKC", text).replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")).strip() + "\n"


def native_quality(text: str, visual: bool) -> tuple[str, str]:
    chars = len(text.strip())
    replacement = text.count("\ufffd")
    if chars == 0:
        return "Missing", "No native text returned; OCR required."
    if replacement or chars < 250:
        return "Sparse/corrupted", "Native text is insufficient for reliable standalone review; OCR retained."
    if visual and chars < 900:
        return "Sparse for visual page", "Native text is present but cannot fully represent the required graphical/table layout; rendered image and OCR retained."
    if visual:
        return "Usable with layout limitation", "Native text is readable; rendered image and OCR retained for table/figure/flow verification."
    return "Usable", "Native text is readable and sufficient for the scoped narrative page."


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def main() -> None:
    if not PDFTOPPM or not TESSERACT:
        raise RuntimeError("Required Poppler renderer or Tesseract executable was not found.")
    package_pages = []
    for doc in DOCS:
        docdir = OUT / doc["id"]
        textdir = docdir / "normalized_text"
        images = docdir / "page_images"
        ocrdir = docdir / "ocr_text"
        for d in (textdir, images, ocrdir):
            d.mkdir(parents=True, exist_ok=True)
        source_path = ROOT / doc["source"]
        reader = PdfReader(str(source_path))
        combined = []
        rows = []
        for page_no in doc["pages"]:
            raw = reader.pages[page_no - 1].extract_text() or ""
            text = normalized(raw)
            visual_label = doc["visual_pages"].get(page_no)
            quality, note = native_quality(raw, bool(visual_label))
            page_text_rel = f"normalized_text/page-{page_no:03d}.txt"
            (docdir / page_text_rel).write_text(
                f"Source PDF: {doc['source']}\nSource page: {page_no}\nExtraction: native PDF text\n\n{text}", encoding="utf-8"
            )
            combined.append(f"\n===== SOURCE PDF {doc['source']} | PAGE {page_no} | NATIVE TEXT =====\n\n{text}")
            page = {
                "document_id": doc["id"], "source_pdf": doc["source"], "source_page": page_no,
                "scope": "Scientific audit", "native_text_file": page_text_rel,
                "native_text_characters": len(raw.strip()), "native_text_quality": quality,
                "quality_note": note, "extraction_method": "native",
                "rendered_image": None, "ocr_text_file": None, "ocr_characters": None,
                "visual_reason": visual_label,
            }
            if visual_label:
                prefix = images / f"page-{page_no:03d}"
                image_path = images / f"page-{page_no:03d}.png"
                if not image_path.exists():
                    print(f"Rendering {doc['id']} page {page_no}", flush=True)
                    run([PDFTOPPM, "-png", "-r", "220", "-f", str(page_no), "-l", str(page_no), str(source_path), str(prefix)])
                    generated_candidates = sorted(images.glob(f"page-{page_no:03d}-*.png"))
                    if len(generated_candidates) != 1:
                        raise RuntimeError(f"Expected one rendered image for source page {page_no}; found {generated_candidates}")
                    generated_candidates[0].replace(image_path)
                ocr_base = ocrdir / f"page-{page_no:03d}"
                ocr_path = ocrdir / f"page-{page_no:03d}.txt"
                if not ocr_path.exists():
                    print(f"OCR {doc['id']} page {page_no}", flush=True)
                    run([TESSERACT, str(image_path), str(ocr_base), "--psm", "6"])
                    ocr = normalized(ocr_path.read_text(encoding="utf-8", errors="replace"))
                    ocr_path.write_text(
                        f"Source PDF: {doc['source']}\nSource page: {page_no}\nExtraction: OCR from rendered page image (220 dpi; tesseract --psm 6)\nVisual target: {visual_label}\n\n{ocr}",
                        encoding="utf-8",
                    )
                else:
                    ocr = normalized(ocr_path.read_text(encoding="utf-8", errors="replace"))
                page.update({
                    "extraction_method": "native + rendered image + OCR",
                    "rendered_image": f"page_images/{image_path.name}",
                    "ocr_text_file": f"ocr_text/{ocr_path.name}", "ocr_characters": len(ocr.strip()),
                })
            rows.append(page)
            package_pages.append(page)
        (textdir / "all_selected_pages_native.txt").write_text("".join(combined).lstrip(), encoding="utf-8")
        manifest = {
            "document_id": doc["id"], "source_pdf": doc["source"], "selected_pages": doc["pages"],
            "excluded_content": doc["excluded"], "pages": rows,
        }
        (docdir / "page_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        md = [f"# PDF Preprocessing Record - {doc['id']}", "", f"Source PDF: `{doc['source']}`", "", "## Scope", "", f"Selected pages: {', '.join(map(str, doc['pages']))}.", "", doc["excluded"], "", "## Extraction summary", "", "Native PDF text was extracted first for every selected page. Rendered PNG and OCR derivatives were retained only for pages containing a required table, figure, or participant-flow diagram.", "", "| Page | Native quality | Method | Visual target |", "|---:|---|---|---|"]
        for p in rows:
            md.append(f"| {p['source_page']} | {p['native_text_quality']} | {p['extraction_method']} | {p['visual_reason'] or '-'} |")
        md.extend(["", "## Source-page linkage", "", "Every normalized-text, OCR-text, and image artifact above embeds or is named with its source PDF and exact source page. No source PDF was modified."])
        (docdir / "pdf_preprocessing.md").write_text("\n".join(md) + "\n", encoding="utf-8")
        status = [f"# Processing Status - {doc['id']}", "", "- Inventory classification: " + ("Main article" if doc["id"] == "DOC-001-MAIN" else "Results supplement"), "- AI Training Restriction Record: retained separately in `rights_record.md`.", "- Human Compliance Review: authorized 2026-07-21 for this scoped scientific processing.", "- Extraction/OCR scope: selected scientific-audit pages processed as documented in `page_manifest.json` and `pdf_preprocessing.md`.", "- Excluded content: " + doc["excluded"], "- Source PDF integrity: source was read only; no modification, rename, move, or overwrite performed."]
        (docdir / "processing_status.md").write_text("\n".join(status) + "\n", encoding="utf-8")
        with (docdir / "agent_responses.md").open("a", encoding="utf-8") as f:
            f.write(f"\n\n## pdf_preprocessor - {date.today().isoformat()}\n\nCompleted scoped native-text extraction and selective rendered-image/OCR preprocessing. See `pdf_preprocessing.md` and `page_manifest.json`.\n")
    package_manifest = {"generated_by": "pdf_preprocessor", "documents": [d["id"] for d in DOCS], "pages": package_pages}
    (ROOT / ".ai_paper_validation" / "page_level_extraction_manifest.json").write_text(json.dumps(package_manifest, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
