#!/usr/bin/env python3
"""Finalize selective extraction manifests and document-level scope records."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / ".ai_paper_validation" / "document_outputs"
BACKEND = ".ai_paper_validation/preprocessing/ocr_backend.json"

VISUAL_PAGES = {"DOC-001": [3, 5, 6, 7, 8], "DOC-004": list(range(16, 24))}
for did, pages in VISUAL_PAGES.items():
    ddir = OUTPUT / did
    mp = ddir / "page_manifest.json"
    manifest = json.loads(mp.read_text(encoding="utf-8"))
    by_page = {r["source_pdf_page"]: r for r in manifest["page_records"]}
    for page in pages:
        record = by_page[page]
        text_path = f"ocr_text/page_{page:03d}.txt"
        metadata_path = f"ocr_metadata/page_{page:03d}.json"
        metadata = json.loads((ddir / metadata_path).read_text(encoding="utf-8"))
        report = metadata["ocr_backend"]
        record["ocr_text_path"] = text_path
        record["ocr_metadata_path"] = metadata_path
        record["ocr_execution"] = {
            "status": metadata["status"], "selected_backend": report["selected_backend"],
            "actual_providers": report["actual_providers"],
            "mean_confidence": metadata["mean_confidence"], "backend_type": "CPU",
        }
    manifest["ocr_backend_selection_record"] = BACKEND
    manifest["extraction_status"] = "complete"
    mp.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

records = {
    "DOC-001": {
        "filename": "jama_bot_2019_oi_190007.pdf", "classification": "main article",
        "source_pdf_pages": 11, "selected_pdf_pages": list(range(1, 12)), "excluded_pdf_pages": [],
        "scope": "Full scientific audit scope.", "preprocessing_status": "Complete",
        "native_text_pages": list(range(1, 12)), "ocr_pages": [3, 5, 6, 7, 8],
        "not_audited_by_design": None,
    },
    "DOC-002": {
        "filename": "joi190007supp1_prod.pdf", "classification": "protocol",
        "source_pdf_pages": None, "selected_pdf_pages": [], "excluded_pdf_pages": "all pages",
        "scope": "Not Audited by Design: protocol excluded from scientific checks absent a parent-requested comparison.",
        "preprocessing_status": "Not Audited by Design", "native_text_pages": [], "ocr_pages": [],
        "not_audited_by_design": "Protocol; no scientific extraction, rendering, or OCR performed.",
    },
    "DOC-003": {
        "filename": "joi190007supp2_prod.pdf", "classification": "statistical analysis plan",
        "source_pdf_pages": None, "selected_pdf_pages": [], "excluded_pdf_pages": "all pages",
        "scope": "Not Audited by Design: SAP excluded from scientific checks absent a parent-requested comparison.",
        "preprocessing_status": "Not Audited by Design", "native_text_pages": [], "ocr_pages": [],
        "not_audited_by_design": "SAP; no scientific extraction, rendering, or OCR performed.",
    },
    "DOC-004": {
        "filename": "joi190007supp3_prod.pdf", "classification": "results supplement",
        "source_pdf_pages": 25, "selected_pdf_pages": [1, 2, *range(16, 24)],
        "excluded_pdf_pages": [*range(3, 16), 24, 25],
        "scope": "Priority results pages 1-2 and 16-23; excluded pages are not result-audit targets under the package manifest.",
        "preprocessing_status": "Complete", "native_text_pages": [1, 2, *range(16, 24)],
        "ocr_pages": list(range(16, 24)),
        "not_audited_by_design": "PDF pages 3-15 and 24-25 excluded from result-audit scope.",
    },
    "DOC-005": {
        "filename": "joi190007supp4_prod.pdf", "classification": "administrative",
        "source_pdf_pages": None, "selected_pdf_pages": [], "excluded_pdf_pages": "all pages",
        "scope": "Not Audited by Design: administrative/data-sharing content excluded from scientific checks.",
        "preprocessing_status": "Not Audited by Design", "native_text_pages": [], "ocr_pages": [],
        "not_audited_by_design": "Administrative supplement; no scientific extraction, rendering, or OCR performed.",
    },
}
for did, record in records.items():
    record.update({
        "document_id": did,
        "source_pdf_unchanged": True,
        "rights_processing_authorization": "Coordinator confirmed rights screen complete and processing authorized.",
        "ocr_backend_selection_record": BACKEND if record["ocr_pages"] else None,
        "ocr_execution_type": "rapidocr-cpu; detector/classifier/recognizer all CPUExecutionProvider" if record["ocr_pages"] else None,
        "page_manifest": "page_manifest.json" if (OUTPUT / did / "page_manifest.json").exists() else None,
        "agent_response": "pdf_preprocessor completed selective extraction and scope recording.",
    })
    (OUTPUT / did / "document_status.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
