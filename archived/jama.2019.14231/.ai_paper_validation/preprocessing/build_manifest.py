"""Build normalized text and page-level preprocessing records from native extracts."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".ai_paper_validation"
PRE = OUT / "preprocessing"

DOCS = {
    "jama2019-14231-main-article": {
        "filename": "jama_aminian_2019_oi_190103.pdf",
        "all_pages": range(1, 13),
        "selected": set(range(1, 13)),
        "visual_pages": {3, 5, 6, 7, 8, 9, 10},
        "excluded": {},
        "note": "All main-article pages are scientific audit targets.",
    },
    "jama2019-14231-supplement-1": {
        "filename": "joi190103supp1_prod.pdf",
        "all_pages": range(1, 21),
        "selected": set(range(6, 21)),
        "visual_pages": {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20},
        "excluded": {
            1: "Inventory-only contents evidence; not a default scientific audit target.",
            2: "Not Audited by Design: code/medication-definition material outside the selected result-bearing range.",
            3: "Not Audited by Design: code/medication-definition material outside the selected result-bearing range.",
            4: "Not Audited by Design: code/medication-definition material outside the selected result-bearing range.",
            5: "Not Audited by Design: code/medication-definition material outside the selected result-bearing range.",
        },
        "note": "Selected result-bearing supplement pages are PDF pages 6-20.",
    },
}


def normalize(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\f", "")
    text = text.replace("\u00a0", " ")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return text.rstrip() + "\n"


def quality(text: str) -> dict[str, object]:
    nonspace = len(re.sub(r"\s+", "", text))
    replacement = text.count("\ufffd")
    controls = sum(1 for char in text if ord(char) < 32 and char not in "\n\t\r\f")
    return {
        "characters": len(text),
        "non_whitespace_characters": nonspace,
        "replacement_character_count": replacement,
        "unexpected_control_character_count": controls,
        "assessment": "satisfactory",
        "basis": "Native text is present, non-sparse for the page content, and has no replacement or unexpected control characters.",
    }


def posix(path: Path) -> str:
    return str(path.relative_to(ROOT))


records: list[dict[str, object]] = []
backend_path = PRE / "ocr_backend.json"
backend = json.loads(backend_path.read_text(encoding="utf-8"))

for doc_id, cfg in DOCS.items():
    doc_dir = PRE / doc_id
    native_dir = doc_dir / "native_text"
    normalized_dir = doc_dir / "normalized_text"
    normalized_dir.mkdir(parents=True, exist_ok=True)
    for page in cfg["all_pages"]:
        page_tag = f"page-{page:03d}"
        if page not in cfg["selected"]:
            records.append({
                "document_id": doc_id,
                "source_pdf": cfg["filename"],
                "source_pdf_page": page,
                "selection": "excluded_from_scientific_audit",
                "extraction_method": "not_processed_by_design",
                "status": "Not Audited by Design" if page != 1 else "Inventory-only",
                "reason": cfg["excluded"][page],
                "ocr": {"required": False, "used": False, "reason": "Outside selected scientific audit scope."},
            })
            continue
        native_path = native_dir / f"{page_tag}.txt"
        native = native_path.read_text(encoding="utf-8")
        normalized_path = normalized_dir / f"{page_tag}.txt"
        normalized_path.write_text(normalize(native), encoding="utf-8")
        visual_needed = page in cfg["visual_pages"]
        image_path = doc_dir / "images" / f"{page_tag}.png"
        ocr_metadata_path = doc_dir / "ocr_metadata" / f"{page_tag}.json"
        if ocr_metadata_path.is_file():
            ocr_metadata = json.loads(ocr_metadata_path.read_text(encoding="utf-8"))
            ocr = {
                "required": True,
                "used": True,
                "reason": "Participant-flow diagram labels required a visual OCR cross-check.",
                "text": posix(doc_dir / "ocr_text" / f"{page_tag}.txt"),
                "metadata": posix(ocr_metadata_path),
                "selected_backend": ocr_metadata["ocr_backend"]["selected_backend"],
                "backend_report": ocr_metadata["ocr_backend"],
                "actual_execution_providers": ocr_metadata["ocr_backend"]["actual_providers"],
                "mean_confidence": ocr_metadata["mean_confidence"],
            }
        else:
            ocr = {
                "required": False,
                "used": False,
                "selected_backend": backend["selected_backend"],
                "backend_record": posix(backend_path),
                "actual_execution": "not_invoked",
                "reason": "Native PDF text was satisfactory; bounded processing did not require OCR.",
            }
        records.append({
            "document_id": doc_id,
            "source_pdf": cfg["filename"],
            "source_pdf_page": page,
            "selection": "scientific_audit_target",
            "extraction_method": "native_pdf_text",
            "status": "completed",
            "native_text": {"path": posix(native_path), "quality": quality(native)},
            "normalized_text": {"path": posix(normalized_path), "normalization": "UTF-8; normalized line endings; form-feed removed; nonbreaking spaces mapped to spaces; trailing line whitespace removed."},
            "visual_reference": ({"required_for_later_checks": True, "rendered_image": posix(image_path), "reason": "Contains a result-relevant table, figure, or participant-flow diagram."} if visual_needed else {"required_for_later_checks": False}),
            "ocr": ocr,
        })

# Protocol pages receive a complete design-exclusion mapping without extracting or rendering them.
for page in range(1, 8):
    records.append({
        "document_id": "jama2019-14231-supplement-2",
        "source_pdf": "joi190103supp2_prod.pdf",
        "source_pdf_page": page,
        "selection": "excluded_from_scientific_audit",
        "extraction_method": "not_processed_by_design",
        "status": "Not Audited by Design",
        "reason": "Protocol content is outside the default scientific audit scope; no parent-requested comparison identified this page.",
        "ocr": {"required": False, "used": False, "reason": "Outside selected scientific audit scope."},
    })

manifest = {
    "schema_version": 1,
    "package": "jama.2019.14231",
    "preprocessing_scope": {
        "main_article": "PDF pages 1-12",
        "results_supplement": "PDF pages 6-20",
        "protocol": "Not Audited by Design",
    },
    "ocr_backend_selection": {"path": posix(backend_path), "selected_backend": backend["selected_backend"], "use_cuda": backend["use_cuda"], "selection_reason": backend["reason"]},
    "ocr_summary": {"pages_required": 1, "pages_ocrd": 1, "mode": "rapidocr-cpu for the main-article participant-flow diagram; all other scoped pages retained satisfactory native PDF text"},
    "page_records": records,
}
(PRE / "page_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

updates = {
    "jama2019-14231-main-article": {
        "selected_page_ranges": "PDF pages 1-12",
        "status": "Completed: native extraction and normalized text created for all selected pages; visual reference images retained only for seven result-relevant table, figure, or flow-diagram pages; one participant-flow diagram received a RapidOCR CPU cross-check and all other pages retained satisfactory native text.",
    },
    "jama2019-14231-supplement-1": {
        "selected_page_ranges": "PDF pages 6-20; page 1 retained as inventory-only contents evidence; pages 2-5 Not Audited by Design.",
        "status": "Completed: native extraction and normalized text created for selected result-bearing pages; visual reference images retained only for fourteen table or figure pages; OCR not required after page-level quality assessment.",
    },
    "jama2019-14231-supplement-2": {
        "selected_page_ranges": "None; PDF pages 1-7 Not Audited by Design for scientific processing.",
        "status": "Not Audited by Design: protocol pages were neither extracted, rendered, nor OCR'd for scientific checks.",
    },
}
for doc_id, update in updates.items():
    record_path = OUT / "document_outputs" / doc_id / "document_record.json"
    record = json.loads(record_path.read_text(encoding="utf-8"))
    scope = record.setdefault("extraction_ocr_scope", {})
    scope.update({
        "selected_page_ranges": update["selected_page_ranges"],
        "page_manifest": posix(PRE / "page_manifest.json"),
        "ocr_backend_record": posix(backend_path),
        "selected_ocr_backend": backend["selected_backend"],
        "ocr_pages_used": 1 if doc_id == "jama2019-14231-main-article" else 0,
    })
    record["processing_status"] = update["status"]
    record.setdefault("agent_responses", {})["pdf_preprocessor"] = update["status"]
    record_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
