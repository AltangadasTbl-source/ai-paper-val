from __future__ import annotations

"""Native-first, page-linked preprocessing for the assigned audit scope."""

import json
import re
import subprocess
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import fitz  # PyMuPDF
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".ai_paper_validation" / "document_outputs"

DOCS = {
    "JAMA2025-4390-MAIN": {
        "source": "jama_garrison_2025_oi_250019_1749674951.29054.pdf",
        "classification": "main article",
        "audited": set(range(1, 13)),
        "context": set(),
        "visual": {4, 5, 7, 8, 9},
        "ocr": set(),
        "excluded": "none",
    },
    "JAMA2025-4390-SUPP1-PROTOCOL": {
        "source": "joi250019supp1_prod_1749674951.29554.pdf",
        "classification": "protocol",
        "audited": set(),
        "context": set(),
        "visual": set(),
        "ocr": set(),
        "excluded": "all 18 pages; Not Audited by Design except a specifically requested protocol-to-report comparison",
    },
    "JAMA2025-4390-SUPP2-SAP": {
        "source": "joi250019supp2_prod_1749674951.30054.pdf",
        "classification": "statistical analysis plan",
        "audited": set(),
        "context": set(),
        "visual": set(),
        "ocr": set(),
        "excluded": "all 7 pages; Not Audited by Design except a specifically requested SAP-to-report comparison",
    },
    "JAMA2025-4390-SUPP3-RESULTS": {
        "source": "joi250019supp3_prod_1749674951.30054.pdf",
        "classification": "results supplement",
        "audited": {11, 12, 19, *range(22, 50)},
        "context": {20, 21},
        "visual": {11, 12, 19, *range(22, 50)},
        "ocr": {11, 12, 19, 22, 23, 24, 26},
        "excluded": "pp. 2-10; Not Audited by Design (administrative/methods content)",
    },
}


def clean(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Controls embedded by PDF character maps are corruption, not page structure.
    text = "".join(ch for ch in text if ch in "\n\t" or ord(ch) >= 32)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text + ("\n" if text else "")


def quality(text: str) -> tuple[str, dict]:
    compact = " ".join(text.split())
    visible = [ch for ch in compact if not ch.isspace()]
    bad = sum(ch in "\ufffd\u25a1" or ord(ch) < 32 for ch in compact)
    control = sum(ord(ch) < 32 and not ch.isspace() for ch in text)
    stats = {
        "normalized_characters": len(compact),
        "replacement_or_box_characters": bad,
        "embedded_control_characters": control,
        "printable_fraction": round(sum(ch.isprintable() for ch in visible) / len(visible), 4) if visible else 0,
    }
    if len(compact) < 750:
        return "sparse", stats
    if bad > max(8, len(compact) * 0.01) or control > max(8, len(compact) * 0.01):
        return "corrupted", stats
    return "adequate", stats


def visual_cues(text: str) -> list[str]:
    lower = text.lower()
    cues = []
    if "table" in lower or "etable" in lower:
        cues.append("table")
    if "figure" in lower or "fig." in lower or "efigure" in lower:
        cues.append("figure")
    if "flow diagram" in lower or "consort" in lower:
        cues.append("flow diagram")
    return cues


def render_page(pdf: fitz.Document, page_no: int, destination: Path, dpi: int) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    scale = dpi / 72
    pix = pdf.load_page(page_no - 1).get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    pix.save(str(destination))


def do_ocr(image: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["tesseract", str(image), "stdout", "--psm", "11"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    destination.write_text(clean(result.stdout), encoding="utf-8")


def page_range(pages: set[int]) -> str:
    if not pages:
        return "none"
    values = sorted(pages)
    groups, start, previous = [], values[0], values[0]
    for value in values[1:]:
        if value == previous + 1:
            previous = value
        else:
            groups.append((start, previous))
            start = previous = value
    groups.append((start, previous))
    return ", ".join(str(a) if a == b else f"{a}-{b}" for a, b in groups)


def main() -> None:
    generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    package_pages = []
    summaries = []
    for doc_id, spec in DOCS.items():
        source = ROOT / spec["source"]
        reader = PdfReader(str(source))
        pdf = fitz.open(source)
        doc_dir = OUT / doc_id
        prep = doc_dir / "preprocessing"
        pages_dir = prep / "normalized_pages"
        images_dir = prep / "page_images"
        ocr_dir = prep / "ocr"
        pages_dir.mkdir(parents=True, exist_ok=True)
        records = []
        combined = [
            f"# Normalized Native Text: {doc_id}",
            "",
            f"- Source PDF: `{spec['source']}`",
            "- Extraction method: native PDF text layer first; OCR text is retained separately only for selected sparse visual pages.",
            "",
        ]
        for page_no, page in enumerate(reader.pages, 1):
            raw = page.extract_text() or ""
            normalized = clean(raw)
            assessment, metrics = quality(normalized)
            scope = "audited" if page_no in spec["audited"] else "targeted_context_only" if page_no in spec["context"] else "not_audited_by_design"
            cues = visual_cues(normalized)
            image_rel = None
            ocr_rel = None
            extraction_method = "native"
            if page_no in spec["audited"]:
                page_file = pages_dir / f"page-{page_no:03d}.txt"
                page_file.write_text(
                    f"Source PDF: {spec['source']}\nSource PDF page: {page_no}\nDocument ID: {doc_id}\nExtraction: native PDF text layer\n\n{normalized}",
                    encoding="utf-8",
                )
                combined += [f"## Source PDF page {page_no}", "", normalized.rstrip(), ""]
            if page_no in spec["visual"]:
                dpi = 300 if page_no in spec["ocr"] else 200
                image_path = images_dir / f"page-{page_no:03d}.png"
                render_page(pdf, page_no, image_path, dpi)
                image_rel = image_path.relative_to(doc_dir).as_posix()
            if page_no in spec["ocr"]:
                ocr_path = ocr_dir / f"page-{page_no:03d}.txt"
                do_ocr(image_path, ocr_path)
                ocr_rel = ocr_path.relative_to(doc_dir).as_posix()
                extraction_method = "native_plus_selective_ocr"
            record = {
                "document_id": doc_id,
                "source_pdf": spec["source"],
                "source_pdf_page": page_no,
                "audit_scope": scope,
                "native_extraction_quality": assessment,
                "quality_metrics": metrics,
                "visual_cues_in_native_text": cues,
                "extraction_method": extraction_method,
                "normalized_native_text": (pages_dir / f"page-{page_no:03d}.txt").relative_to(doc_dir).as_posix() if page_no in spec["audited"] else None,
                "rendered_page_image": image_rel,
                "ocr_text": ocr_rel,
                "reason_for_render_or_ocr": (
                    "Required figure/table/flow-diagram review page; native text adequate." if image_rel and not ocr_rel else
                    "Sparse native text on a required visual page; rendered at 300 dpi and OCR retained alongside native text." if ocr_rel else
                    "Native text assessed but excluded from scientific audit by design."
                ),
            }
            records.append(record)
            package_pages.append(record)
        if spec["audited"]:
            (prep / "normalized_native_text.md").write_text("\n".join(combined), encoding="utf-8")
        page_manifest = {
            "document_id": doc_id,
            "source_pdf": spec["source"],
            "classification": spec["classification"],
            "generated_at_utc": generated,
            "native_text_first": True,
            "audited_pages": page_range(spec["audited"]),
            "targeted_context_only_pages": page_range(spec["context"]),
            "not_audited_by_design": spec["excluded"],
            "pages": records,
        }
        (prep / "page_manifest.json").write_text(json.dumps(page_manifest, indent=2), encoding="utf-8")
        status = [
            f"# PDF Preprocessing Record: {doc_id}",
            "",
            f"- Source PDF: `{spec['source']}` (unchanged)",
            f"- Classification: {spec['classification']}",
            "- Native PDF text was extracted before any rendering or OCR.",
            f"- Scientific audit pages processed: {page_range(spec['audited'])}.",
            f"- Targeted-context-only pages: {page_range(spec['context'])}.",
            f"- Excluded content: {spec['excluded']}.",
            f"- Rendered page images: {len(spec['visual'])}; OCR pages: {page_range(spec['ocr'])}.",
            f"- Page-level source references, quality assessments, methods, and artifact paths: `preprocessing/page_manifest.json`.",
            "- Processing status: preprocessing completed; downstream extraction/checking may use retained artifacts within the stated scope.",
        ]
        (doc_dir / "preprocessing_record.md").write_text("\n".join(status) + "\n", encoding="utf-8")
        summaries.append({
            "document_id": doc_id,
            "source_pdf": spec["source"],
            "classification": spec["classification"],
            "audit_pages": page_range(spec["audited"]),
            "context_pages": page_range(spec["context"]),
            "rendered_pages": page_range(spec["visual"]),
            "ocr_pages": page_range(spec["ocr"]),
            "not_audited_by_design": spec["excluded"],
        })
        pdf.close()
    root_prep = ROOT / ".ai_paper_validation" / "preprocessing"
    root_prep.mkdir(parents=True, exist_ok=True)
    (root_prep / "page_level_manifest.json").write_text(json.dumps({
        "package_id": "jama.2025.4390",
        "generated_at_utc": generated,
        "native_text_first": True,
        "pages": package_pages,
    }, indent=2), encoding="utf-8")
    (root_prep / "extraction_summary.json").write_text(json.dumps({
        "package_id": "jama.2025.4390",
        "generated_at_utc": generated,
        "documents": summaries,
    }, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
