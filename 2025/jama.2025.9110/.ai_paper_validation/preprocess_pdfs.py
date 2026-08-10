from __future__ import annotations

import re
import subprocess
import unicodedata
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".ai_paper_validation" / "document_outputs"
POPPLER_EXE = Path(r"C:\Users\juliz\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")

DOCUMENTS = (
    {
        "id": "JAMA2025_9110_D01_MAIN",
        "source": "jama_summers_2025_oi_250040_1753124024.36498.pdf",
        "pages": range(1, 11),
        "visual": {3: "flow diagram (Figure 1)", 5: "table (Table 1)", 6: "figure (Figure 2)", 7: "table (Table 2)", 8: "figure (Figure 3)"},
        "ocr_required": {3, 5, 6, 7, 8},
        "scope": "Audited: source PDF pp. 1-10. Native text retained for every page; rendered/OCR visual-review artifacts retained only for Figure 1, Table 1, Figure 2, Table 2, and Figure 3 pages.",
    },
    {
        "id": "JAMA2025_9110_D04_RESULTS_SUPP",
        "source": "joi250040supp3_prod_1753124024.38098.pdf",
        "pages": range(1, 33),
        "visual": {
            **{page: "result-relevant table" for page in range(7, 23)},
            **{page: "result-relevant figure" for page in range(23, 29)},
            **{page: "ICEMAN result-relevant visual/table material" for page in range(29, 33)},
        },
        "ocr_required": set(range(7, 33)) | {6},
        "scope": "Audited: source PDF pp. 1-32. Native text retained for every page. Rendering/OCR is restricted to p. 6 (corrupted native character), eTables pp. 7-22, eFigures pp. 23-28, and ICEMAN material pp. 29-32. References pp. 33-34 are Not Audited by Design.",
    },
)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n"))
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def native_quality(text: str) -> tuple[str, str]:
    visible = len(re.sub(r"\s", "", text))
    bad = text.count("\ufffd") + text.count("\x00")
    if bad:
        return "corrupted", f"{bad} replacement/control character(s) detected; OCR used for the normalized review text."
    if visible < 250:
        return "sparse", "Sparse native layer; OCR used for the normalized review text."
    return "acceptable", "Substantive, readable native text; retained as the normalized review text."


def write_text(path: Path, document_id: str, source: str, page: int, method: str, quality: str, content: str) -> None:
    header = (
        f"Source document ID: {document_id}\n"
        f"Source PDF: {source}\n"
        f"Source PDF page: {page}\n"
        f"Extraction method: {method}\n"
        f"Native extraction quality: {quality}\n"
        "---\n"
    )
    path.write_text(header + normalize(content), encoding="utf-8")


def render_page(pdf: Path, page: int, image: Path) -> None:
    image.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [str(POPPLER_EXE), "-f", str(page), "-l", str(page), "-r", "170", "-png", "-singlefile", str(pdf), str(image.with_suffix(""))],
        check=True,
        capture_output=True,
    )


def ocr_image(image: Path) -> str:
    result = subprocess.run(
        ["tesseract.exe", str(image), "stdout", "--psm", "6"], check=True, capture_output=True
    )
    return result.stdout.decode("utf-8", errors="replace")


def process(doc: dict) -> None:
    document_id = doc["id"]
    source_name = doc["source"]
    pdf = ROOT / source_name
    directory = OUT / document_id
    prep = directory / "derived" / "preprocessing"
    native_dir = prep / "native_text_pages"
    normalized_dir = prep / "normalized_text_pages"
    ocr_dir = prep / "ocr_text_pages"
    image_dir = prep / "page_images"
    for d in (native_dir, normalized_dir):
        d.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(pdf))
    records = []
    for page in doc["pages"]:
        raw = reader.pages[page - 1].extract_text() or ""
        quality, quality_note = native_quality(raw)
        visual_kind = doc["visual"].get(page)
        if visual_kind and "table" in visual_kind and quality == "acceptable":
            quality = "acceptable with table-layout fragmentation"
            quality_note = "Substantive native text, but table cell ordering/layout is fragmented; OCR and the rendered source page are retained for review."
        page_name = f"page-{page:03d}"
        native_path = native_dir / f"{page_name}.native.txt"
        write_text(native_path, document_id, source_name, page, "native", quality, raw)

        needs_ocr = page in doc["ocr_required"]
        image_rel = "Not rendered"
        ocr_rel = "Not produced"
        if visual_kind or needs_ocr:
            image_path = image_dir / f"{page_name}.png"
            render_page(pdf, page, image_path)
            image_rel = image_path.relative_to(directory).as_posix()
        if needs_ocr:
            ocr_dir.mkdir(parents=True, exist_ok=True)
            ocr = ocr_image(image_path)
            ocr_path = ocr_dir / f"{page_name}.ocr.txt"
            write_text(ocr_path, document_id, source_name, page, "OCR (rendered at 170 dpi)", quality, ocr)
            ocr_rel = ocr_path.relative_to(directory).as_posix()

        normalized_path = normalized_dir / f"{page_name}.txt"
        if quality in {"corrupted", "sparse"} and needs_ocr:
            final_method, final_content = "OCR (native retained separately)", ocr
        else:
            final_method, final_content = "native (OCR retained as visual aid where applicable)", raw
        write_text(normalized_path, document_id, source_name, page, final_method, quality, final_content)
        normalized_rel = normalized_path.relative_to(directory).as_posix()
        native_rel = native_path.relative_to(directory).as_posix()
        method = "native + rendered visual review + OCR" if needs_ocr else ("native + rendered visual review" if visual_kind else "native")
        notes = quality_note
        if visual_kind:
            notes += f" Visual target: {visual_kind}."
        records.append((page, len(raw), quality, method, native_rel, normalized_rel, image_rel, ocr_rel, notes))

    lines = [
        f"# Page-level preprocessing manifest - {document_id}",
        "",
        f"Source PDF: `{source_name}` (source files were read only)",
        f"Source-page scope: {min(doc['pages'])}-{max(doc['pages'])}",
        "",
        "| Source PDF page | Native characters | Native quality | Page method | Native text artifact | Normalized text artifact | Rendered image | OCR text artifact | Assessment / reason |",
        "|---:|---:|---|---|---|---|---|---|---|",
    ]
    for record in records:
        lines.append("| " + " | ".join(str(value) for value in record) + " |")
    (prep / "page_manifest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    processing = [
        f"# Preprocessing record - {document_id}",
        "",
        f"Source PDF: `{source_name}` (unchanged; all derived artifacts are beneath this document output directory).",
        "",
        "## Extraction and OCR scope",
        "",
        doc["scope"],
        "",
        "Native extraction was performed before any rendering/OCR. Each text artifact embeds the document ID, exact source filename, and source PDF page. OCR output is a visual-review aid and does not replace retained native extraction.",
        "",
        "## Artifact index",
        "",
        "- `derived/preprocessing/page_manifest.md` - page-level method, quality, and source-linked artifact index",
        "- `derived/preprocessing/native_text_pages/` - native text from every scoped page",
        "- `derived/preprocessing/normalized_text_pages/` - normalized downstream review text",
        "- `derived/preprocessing/page_images/` - only selected visual or native-quality exception pages",
        "- `derived/preprocessing/ocr_text_pages/` - only selected visual or native-quality exception pages",
    ]
    (directory / "preprocessing_record.md").write_text("\n".join(processing) + "\n", encoding="utf-8")


def write_not_audited(document_id: str, source_name: str, classification: str) -> None:
    directory = OUT / document_id
    record = [
        f"# Preprocessing record - {document_id}",
        "",
        f"Source PDF: `{source_name}` (unchanged).",
        "",
        "## Extraction and OCR scope",
        "",
        f"**Not Audited by Design.** This {classification} is outside the default scientific audit scope. No pages were natively extracted, rendered, or OCR processed by preprocessing. It may be opened only for a specific parent-requested protocol-to-report comparison.",
        "",
        "No derived page images or text artifacts were created for this document.",
    ]
    (directory / "preprocessing_record.md").write_text("\n".join(record) + "\n", encoding="utf-8")


for document in DOCUMENTS:
    process(document)
write_not_audited("JAMA2025_9110_D02_PROTOCOL", "joi250040supp1_prod_1753124024.37199.pdf", "protocol")
write_not_audited("JAMA2025_9110_D03_SAP", "joi250040supp2_prod_1753124024.37799.pdf", "statistical analysis plan")
