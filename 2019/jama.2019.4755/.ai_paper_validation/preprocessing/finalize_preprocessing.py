#!/usr/bin/env python3
"""Finalize the scoped native-text preprocessing record without further OCR."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARTIFACTS = ROOT / ".ai_paper_validation"
MANIFEST_PATH = ARTIFACTS / "preprocessing" / "page_manifest.json"
BACKEND_PATH = ARTIFACTS / "preprocessing" / "ocr_backend.json"
QUALITY_PATH = ARTIFACTS / "preprocessing" / "native_layout_quality_report.json"
SUMMARY_PATH = ARTIFACTS / "preprocessing" / "preprocessing_summary.json"

RENDERED = {
    ("doc-799606a72443", 4): "flow diagram and Table 1 required for later visual/flow checks",
    ("doc-799606a72443", 5): "Tables 2-3 required for later table/statistical checks",
    ("doc-b45e07a04d82", 4): "eTable 2 required for later table checks",
    ("doc-b45e07a04d82", 5): "eTable 3 required for later table/statistical checks",
    ("doc-b45e07a04d82", 6): "eTable 4 required for later table/statistical checks",
    ("doc-b45e07a04d82", 7): "eTable 5 required for later table/statistical checks",
    ("doc-b45e07a04d82", 8): "eTable 6 required for later table/statistical checks",
}


def dump(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


backend = json.loads(BACKEND_PATH.read_text(encoding="utf-8"))
if backend.get("selected_backend") != "rapidocr-cpu" or backend.get("use_cuda") is not False:
    raise RuntimeError(f"Expected recorded CPU RapidOCR selection, got {backend!r}")

manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
manifest["ocr_backend"] = backend
manifest["preprocessing_status"] = "completed_native_with_rendered_audit_pages"
manifest["ocr_completion_note"] = (
    "Native extraction was adequate on every scoped page. Per coordinator direction, no further OCR "
    "was required; the seven audit-critical visual pages were rendered and retained for downstream review."
)

for page in manifest["pages"]:
    key = (page["document_id"], page["source_pdf_page"])
    page["ocr_backend_report"] = str(BACKEND_PATH.relative_to(ROOT))
    page["ocr_backend_selected"] = "rapidocr-cpu"
    page["ocr_required"] = False
    page["ocr_status"] = "not_required_by_final_scope"
    page["ocr_reason"] = (
        "Native layout extraction passed all page-level completeness and corruption checks; "
        "no further OCR was required by the final scoped preprocessing direction."
    )
    if key in RENDERED:
        image = ROOT / ".ai_paper_validation" / "document_outputs" / page["document_id"] / "ocr_pages" / f"page-{page['source_pdf_page']}.png"
        if not image.is_file():
            raise RuntimeError(f"Expected rendered audit page is missing: {image}")
        page["rendered_audit_image"] = str(image.relative_to(ROOT))
        page["render_reason"] = RENDERED[key]
        page["render_status"] = "completed"

for document in manifest.get("documents", []):
    if document["document_id"] in {"doc-799606a72443", "doc-b45e07a04d82"}:
        document.update({
            "native_extraction_status": "completed; all scoped pages adequate",
            "ocr_status": "not required by final scope; CPU backend selection recorded",
            "extraction_status": "completed_native_with_rendered_audit_pages",
            "ocr_backend_report": str(BACKEND_PATH.relative_to(ROOT)),
        })

dump(MANIFEST_PATH, manifest)

for document_id in ("doc-799606a72443", "doc-b45e07a04d82"):
    path = ARTIFACTS / "document_outputs" / document_id / "document_record.json"
    record = json.loads(path.read_text(encoding="utf-8"))
    selected = "1-7" if document_id == "doc-799606a72443" else "4-8"
    record["pdf_preprocessing"] = {
        "selected_pdf_pages": selected,
        "native_extraction_status": "completed; all scoped pages adequate",
        "ocr_status": "not required by final scope; CPU backend selection recorded",
        "extraction_status": "completed_native_with_rendered_audit_pages",
        "page_manifest": str(MANIFEST_PATH.relative_to(ROOT)),
        "native_layout_quality_report": str(QUALITY_PATH.relative_to(ROOT)),
        "ocr_backend_report": str(BACKEND_PATH.relative_to(ROOT)),
        "rendered_audit_pages": [
            str((ARTIFACTS / "document_outputs" / document_id / "ocr_pages" / f"page-{page}.png").relative_to(ROOT))
            for ident, page in RENDERED if ident == document_id
        ],
        "source_pdf_unchanged": True,
    }
    dump(path, record)

summary = {
    "scope": {
        "doc-799606a72443": "PDF pages 1-7",
        "doc-b45e07a04d82": "PDF pages 4-8",
        "excluded": {
            "doc-5143f7e4da1a": "Not Audited by Design (protocol)",
            "doc-5704a644014e": "Not Audited by Design (statistical analysis plan)",
            "doc-ded78f53da7b": "Not Audited by Design (administrative material)",
        },
    },
    "ocr_backend": {
        "report": str(BACKEND_PATH.relative_to(ROOT)),
        "selected_backend": "rapidocr-cpu",
        "use_cuda": False,
    },
    "native_extraction_quality": "adequate for all 12 scoped pages",
    "rendered_audit_pages": [
        str((ARTIFACTS / "document_outputs" / identifier / "ocr_pages" / f"page-{page}.png").relative_to(ROOT))
        for identifier, page in RENDERED
    ],
    "ocr": "No additional OCR performed by final scoped preprocessing direction.",
    "source_pdfs_modified": False,
}
dump(SUMMARY_PATH, summary)
