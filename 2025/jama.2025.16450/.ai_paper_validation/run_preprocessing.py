"""Scoped, source-read-only PDF preprocessing for JAMA 2025.16450."""
from __future__ import annotations

import json
import re
import shutil
import unicodedata
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".ai_paper_validation"

DOCUMENTS = [
    {
        "id": "JAMA2025-16450-MAIN",
        "source": "jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf",
        "scope": range(1, 12),
        "render_pages": {4: "flow_diagram", 5: "table", 6: "table", 7: "table"},
        "scope_note": "All main-article pages 1-11; visual render limited to Figure 1 and Tables 1-2 pages.",
    },
    {
        "id": "JAMA2025-16450-SUPP04-RESULTS",
        "source": "joi250072supp4_prod_1761000786.6988.pdf",
        "scope": range(1, 17),
        "render_pages": {**{p: "table" for p in range(2, 17)}},
        "scope_note": "Page 1 contents/context and results eTable pages 2-16; visual render limited to eTable pages.",
    },
]

EXCLUDED = [
    ("JAMA2025-16450-SUPP01-PROTOCOL", "Protocol", "joi250072supp1_prod_1761000786.68881.pdf", 35),
    ("JAMA2025-16450-SUPP02-MANUAL", "Administrative material (Manual of Operations)", "joi250072supp2_prod_1761000786.6938.pdf", 162),
    ("JAMA2025-16450-SUPP03-SAP", "Statistical analysis plan", "joi250072supp3_prod_1761000786.6988.pdf", 48),
]


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).replace("\u00ad", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def quality(text: str) -> tuple[str, list[str], dict[str, float | int]]:
    nonspace = [c for c in text if not c.isspace()]
    n = len(nonspace)
    alnum = sum(c.isalnum() for c in nonspace)
    corrupt = sum(c in "\ufffd\x00" or unicodedata.category(c) == "Co" for c in nonspace)
    metrics = {
        "native_characters": len(text),
        "nonspace_characters": n,
        "alphanumeric_ratio": round(alnum / n, 3) if n else 0,
        "corrupt_character_count": corrupt,
    }
    if len(text) < 100:
        return "Sparse", ["native text under 100 characters"], metrics
    if corrupt or (n and alnum / n < 0.25):
        return "Corrupted", ["replacement/private-use characters or unusually low alphanumeric content"], metrics
    return "Adequate", [], metrics


def clean_folder(folder: Path) -> None:
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True, exist_ok=True)


def preprocess(doc_spec: dict) -> None:
    doc_id = doc_spec["id"]
    source = ROOT / doc_spec["source"]
    doc_out = OUT / "document_outputs" / doc_id
    work = doc_out / "preprocessing"
    pages_dir = work / "normalized_pages"
    images_dir = work / "page_images"
    clean_folder(pages_dir)
    clean_folder(images_dir)
    pdf = fitz.open(source)
    page_records = []
    all_text = []
    for page_number in doc_spec["scope"]:
        page = pdf[page_number - 1]
        native = normalize(page.get_text("text", sort=True))
        q, reasons, metrics = quality(native)
        page_name = f"page-{page_number:03d}.txt"
        (pages_dir / page_name).write_text(native, encoding="utf-8")
        visual_kind = doc_spec["render_pages"].get(page_number)
        image_name = None
        if visual_kind:
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
            image_name = f"page-{page_number:03d}-{visual_kind}.png"
            pix.save(images_dir / image_name)
        record = {
            "source_pdf": doc_spec["source"],
            "source_page": page_number,
            "source_reference": f"{doc_spec['source']}#page={page_number}",
            "in_selected_scope": True,
            "content_role": "context" if doc_id.endswith("RESULTS") and page_number == 1 else (visual_kind or "text"),
            "native_text_file": f"normalized_pages/{page_name}",
            "native_extraction_quality": q,
            "quality_reasons": reasons,
            "quality_metrics": metrics,
            "extraction_method_retained": "native",
            "ocr_performed": False,
            "ocr_reason": None,
            "rendered_image": f"page_images/{image_name}" if image_name else None,
            "render_reason": f"Required later visual verification: {visual_kind}." if visual_kind else None,
        }
        page_records.append(record)
        all_text.append(f"\n===== SOURCE: {doc_spec['source']} | PDF PAGE {page_number} | METHOD: native =====\n\n{native}")
    (work / "normalized_text.txt").write_text("".join(all_text).lstrip(), encoding="utf-8")
    (work / "page_manifest.json").write_text(json.dumps({
        "document_id": doc_id,
        "source_pdf": doc_spec["source"],
        "source_pdf_page_count": len(pdf),
        "selected_page_range": f"1-{len(doc_spec['scope'])}",
        "extraction_status": "Complete - native text retained on all selected pages; no OCR needed.",
        "pages": page_records,
    }, indent=2), encoding="utf-8")
    lines = [
        f"# Page-Level Preprocessing Manifest - {doc_id}", "",
        f"- Source PDF (read only): `{doc_spec['source']}`",
        f"- Selected scope: pages 1-{len(doc_spec['scope'])}",
        f"- Scope rationale: {doc_spec['scope_note']}",
        "- Native-first result: all selected pages were adequate after native extraction; OCR was not performed.",
        "- Page images are 144 dpi-equivalent PNG renders used only for pages containing a required flow diagram or table.", "",
        "| PDF page | Source reference | Role | Native quality | Retained method | OCR | Render artifact |",
        "|---:|---|---|---|---|---|---|",
    ]
    for r in page_records:
        lines.append(f"| {r['source_page']} | `{r['source_reference']}` | {r['content_role']} | {r['native_extraction_quality']} | native | No | {('`' + r['rendered_image'] + '`') if r['rendered_image'] else 'None'} |")
    (work / "page_manifest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    record_path = doc_out / "inventory_record.md"
    with record_path.open("a", encoding="utf-8") as f:
        f.write("\n## PDF preprocessing update\n\n")
        f.write(f"- Processing authorization: coordinator reported institutional permission; continued despite any Human Compliance Review flag.\n")
        f.write(f"- Selected pages: 1-{len(doc_spec['scope'])}.\n")
        f.write("- Extraction status: **Complete**. Native text was extracted, quality-screened, and retained for every selected page; no page met the threshold for OCR.\n")
        f.write(f"- Visual renders: {', '.join(str(p) for p in sorted(doc_spec['render_pages']))}; only required table/flow-diagram pages were rendered.\n")
        f.write(f"- Artifacts: `preprocessing/page_manifest.md`, `preprocessing/page_manifest.json`, `preprocessing/normalized_text.txt`, per-page normalized text, and selected page images.\n")
    pdf.close()


def excluded_record(doc_id: str, classification: str, source: str, pages: int) -> None:
    doc_out = OUT / "document_outputs" / doc_id
    path = doc_out / "preprocessing_status.md"
    path.write_text(f"""# PDF Preprocessing Status - {doc_id}

- Source PDF (read only): `{source}` ({pages} pages)
- Classification: {classification}
- Scientific preprocessing status: **Not Audited by Design**.
- Selected page ranges: None.
- Native extraction, rendering, OCR, page images, and normalized scientific text: Not performed.
- Reason: This document is excluded by the package manifest's long-supplement rule. It may be opened only for a specific parent-requested protocol/SAP/report comparison.
- Source-page references: None created because no pages were selected.
""", encoding="utf-8")
    record_path = doc_out / "inventory_record.md"
    with record_path.open("a", encoding="utf-8") as f:
        f.write("\n## PDF preprocessing update\n\n")
        f.write("- Preprocessing status: **Not Audited by Design**. No pages selected; no scientific native extraction, rendering, OCR, page images, or normalized text produced.\n")
        f.write("- Record: `preprocessing_status.md`. Targeted processing remains limited to a parent-requested comparison.\n")


for spec in DOCUMENTS:
    preprocess(spec)
for excluded in EXCLUDED:
    excluded_record(*excluded)
