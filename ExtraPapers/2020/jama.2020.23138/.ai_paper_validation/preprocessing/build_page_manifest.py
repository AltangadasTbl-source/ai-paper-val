"""Generate the preprocessing page manifest from already-created local artifacts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / ".ai_paper_validation"
PRE = BASE / "preprocessing"

DOCS = {
    "JAMA2020-23138-MAIN": {
        "document_output_id": "DOC-001",
        "source_filename": "jama_kotecha_2020_oi_200126_1607962892.52158.pdf",
        "pages": range(1, 13),
        "page_scope": lambda p: "Main-article scientific audit target",
    },
    "JAMA2020-23138-SUPP03-RESULTS": {
        "document_output_id": "DOC-004",
        "source_filename": "joi200126supp3_prod_1607962892.5372.pdf",
        "pages": range(1, 21),
        "page_scope": lambda p: (
            "Primary results audit target" if 8 <= p <= 18 else
            "Results-supplement contextual material" if p <= 7 else
            "Results-supplement references; extracted for traceability, not a primary results check target"
        ),
    },
}

RENDERED = {
    "JAMA2020-23138-MAIN": {3, 5, 6, 7, 8, 9},
    "JAMA2020-23138-SUPP03-RESULTS": set(range(8, 19)),
}
OCR_REQUIRED = {
    "JAMA2020-23138-MAIN": {3, 8},
    "JAMA2020-23138-SUPP03-RESULTS": {8, 9, 10, 11, 12},
}
SPARSE = {"JAMA2020-23138-SUPP03-RESULTS": {8, 9, 10, 11, 12}}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def page_record(doc_id: str, spec: dict, page: int, backend: dict) -> dict:
    native = PRE / "native_text" / doc_id / f"page-{page:03d}.txt"
    normalized = PRE / "normalized_text" / doc_id / f"page-{page:03d}.txt"
    image = PRE / "page_images" / doc_id / f"page-{page:02d}.png"
    rendered = page in RENDERED[doc_id]
    ocr_required = page in OCR_REQUIRED[doc_id]
    quality = "sparse" if page in SPARSE.get(doc_id, set()) else "adequate"
    entry = {
        "document_id": doc_id,
        "document_output_id": spec["document_output_id"],
        "source_pdf": spec["source_filename"],
        "source_page": page,
        "source_page_reference": f"{spec['source_filename']}, PDF page {page}",
        "audit_scope": spec["page_scope"](page),
        "native_extraction": {
            "status": "completed",
            "quality": quality,
            "characters": len(native.read_text(encoding="utf-8")),
            "artifact": rel(native),
        },
        "normalized_text": {
            "status": "completed_from_native_extraction",
            "artifact": rel(normalized),
        },
        "rendering": {"status": "not_required"},
    }
    if rendered:
        entry["rendering"] = {
            "status": "completed",
            "artifact": rel(image),
            "resolution_dpi": 200,
            "reason": (
                "Table/figure/flow-diagram visual content retained for downstream checking"
                if not ocr_required else
                "Figure or flow-diagram visual text is incomplete in native extraction"
            ),
        }
    if ocr_required:
        entry["ocr"] = {
            "status": "failed_backend_unavailable",
            "attempted": True,
            "command": "scripts/ocr_page.py <rendered-image> <ocr-text-output> --mode auto --metadata <page-ocr-metadata>",
            "selected_backend": backend["selected_backend"],
            "backend_report": rel(PRE / "ocr_backend.json"),
            "actual_execution_providers": {
                "detector": [], "classifier": [], "recognizer": [],
                "note": "No OCR stage initialized because backend selection was unavailable.",
            },
            "mean_confidence": None,
            "error": backend["reason"],
            "ocr_text_artifact": None,
            "page_ocr_metadata_artifact": None,
        }
    else:
        entry["ocr"] = {
            "status": "not_required_native_text_adequate",
            "attempted": False,
            "selected_backend": backend["selected_backend"],
            "mean_confidence": None,
        }
    return entry


def update_record(path: Path, preprocessing: dict, status: str) -> None:
    record = json.loads(path.read_text(encoding="utf-8"))
    record["preprocessing"] = preprocessing
    record["processing_status"] = status
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    backend = json.loads((PRE / "ocr_backend.json").read_text(encoding="utf-8"))
    pages = [page_record(doc_id, spec, p, backend) for doc_id, spec in DOCS.items() for p in spec["pages"]]
    manifest = {
        "schema_version": 1,
        "artifact_root": ".ai_paper_validation/",
        "source_pdf_policy": "Source PDFs were read only and were not modified, moved, renamed, or overwritten.",
        "ocr_backend_selection": {
            "interpreter": backend["python"],
            "report": rel(PRE / "ocr_backend.json"),
            "selected_backend": backend["selected_backend"],
            "use_cuda": backend["use_cuda"],
            "reason": backend["reason"],
            "provider_validation": {
                "onnxruntime_available_providers": backend["onnxruntime_available_providers"],
                "gpu_ocr_used": False,
                "cpu_ocr_used": False,
            },
        },
        "summary": {
            "native_text_pages_completed": len(pages),
            "normalized_text_pages_completed": len(pages),
            "rendered_pages_completed": sum(p in RENDERED[d] for d, spec in DOCS.items() for p in spec["pages"]),
            "ocr_pages_required": sum(p in OCR_REQUIRED[d] for d, spec in DOCS.items() for p in spec["pages"]),
            "ocr_pages_completed": 0,
            "ocr_pages_failed": sum(p in OCR_REQUIRED[d] for d, spec in DOCS.items() for p in spec["pages"]),
            "overall_status": "native_extraction_completed__required_ocr_blocked_backend_unavailable",
        },
        "pages": pages,
    }
    (PRE / "page_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    update_record(
        BASE / "document_outputs/DOC-001/document_record.json",
        {
            "selected_pages": "PDF pages 1-12",
            "native_extraction": "Completed for all 12 pages",
            "normalized_text_root": ".ai_paper_validation/preprocessing/normalized_text/JAMA2020-23138-MAIN/",
            "rendered_pages": [3, 5, 6, 7, 8, 9],
            "ocr_required_pages": [3, 8],
            "ocr_status": "Blocked: selected backend unavailable; every required OCR invocation failed before provider initialization.",
            "page_manifest": rel(PRE / "page_manifest.json"),
        },
        "Preprocessing: native extraction and selected rendering completed; required figure/flow OCR blocked because no supported OCR backend is available.",
    )
    update_record(
        BASE / "document_outputs/DOC-004/document_record.json",
        {
            "selected_pages": "PDF pages 1-20; primary results pages 8-18",
            "native_extraction": "Completed for all 20 pages",
            "normalized_text_root": ".ai_paper_validation/preprocessing/normalized_text/JAMA2020-23138-SUPP03-RESULTS/",
            "rendered_pages": list(range(8, 19)),
            "ocr_required_pages": [8, 9, 10, 11, 12],
            "ocr_status": "Blocked: selected backend unavailable; every required OCR invocation failed before provider initialization.",
            "page_manifest": rel(PRE / "page_manifest.json"),
        },
        "Preprocessing: native extraction and selected rendering completed; required eFigure OCR blocked because no supported OCR backend is available.",
    )
    for doc, kind in (("DOC-002", "protocol"), ("DOC-003", "statistical analysis plan"), ("DOC-005", "data-sharing administrative statement")):
        update_record(
            BASE / f"document_outputs/{doc}/document_record.json",
            {
                "selected_pages": [],
                "extraction_status": "Not Audited by Design",
                "rendering_status": "Not Audited by Design",
                "ocr_status": "Not Audited by Design",
                "reason": f"{kind.capitalize()} is outside the routine scientific-audit scope; no preprocessing was performed.",
            },
            "Inventory and AI Training Restriction screen complete — Not Audited by Design; no routine extraction, OCR, rendering, or checking performed.",
        )
    provenance = {
        "source_pdf_sha256": {
            spec["source_filename"]: sha256(ROOT / spec["source_filename"])
            for spec in DOCS.values()
        },
        "page_manifest": rel(PRE / "page_manifest.json"),
        "ocr_backend_report": rel(PRE / "ocr_backend.json"),
    }
    (PRE / "preprocessing_provenance.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
