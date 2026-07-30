#!/usr/bin/env python3
"""Build page-linked normalized text and a preprocessing manifest."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def normalize(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def main() -> None:
    document_id, source_pdf, selected_pages, ocr_pages, audit_reason = sys.argv[1:6]
    selected = {int(value) for value in selected_pages.split(",")}
    rendered_ocr = {int(value) for value in ocr_pages.split(",") if value}
    base = Path(".ai_paper_validation/document_outputs") / document_id / "preprocessing"
    native_dir = base / "native_text"
    normalized_dir = base / "normalized_text"
    normalized_dir.mkdir(parents=True, exist_ok=True)
    quality = json.loads((native_dir / "native_extraction_quality.json").read_text(encoding="utf-8"))
    page_entries: list[dict[str, object]] = []
    for measured in quality["pages"]:
        page_number = int(measured["pdf_page"])
        if page_number not in selected:
            continue
        native_path = Path(str(measured["native_text_file"]))
        native_text = native_path.read_text(encoding="utf-8")
        page: dict[str, object] = {
            "pdf_page": page_number,
            "source_page_reference": f"{source_pdf}, PDF page {page_number}",
            "native_extraction": {
                "status": "completed",
                "text_file": str(native_path),
                "quality_measurements": {key: measured[key] for key in (
                    "native_text_characters", "native_alphanumeric_characters",
                    "native_text_blocks", "native_words", "embedded_images",
                    "vector_drawings", "replacement_characters",
                )},
            },
        }
        final_text = native_text
        if page_number in rendered_ocr:
            metadata_path = base / "ocr_metadata" / f"page-{page_number:03d}.json"
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            ocr_path = Path(metadata["output_text"])
            ocr_text = ocr_path.read_text(encoding="utf-8")
            final_text = native_text + "\n\n[OCR transcription of rendered page]\n" + ocr_text
            page["ocr"] = {
                "status": metadata["status"],
                "trigger": audit_reason,
                "rendered_image": metadata["input_image"],
                "ocr_text_file": str(ocr_path),
                "metadata_file": str(metadata_path),
                "backend": metadata["ocr_backend"]["selected_backend"],
                "actual_execution_providers": metadata["ocr_backend"]["actual_providers"],
                "mean_confidence": metadata["mean_confidence"],
                "backend_report": metadata["ocr_backend"],
            }
            page["extraction_method"] = "native_text_plus_selective_ocr"
            page["quality_assessment"] = "Native extraction retained; " + audit_reason
        else:
            page["extraction_method"] = "native_text"
            page["quality_assessment"] = (
                "Native extraction was nonempty and contained no replacement characters; no visual "
                "content requiring downstream OCR was selected."
            )
        normalized_path = normalized_dir / f"page-{page_number:03d}.txt"
        normalized_path.write_text(normalize(final_text), encoding="utf-8")
        page["normalized_text_file"] = str(normalized_path)
        page_entries.append(page)
    manifest = {
        "document_id": document_id,
        "source_pdf": source_pdf,
        "audit_scope": f"PDF pages {min(selected)}-{max(selected)}",
        "source_pdf_modified": False,
        "ocr_backend_selection": ".ai_paper_validation/preprocessing/ocr_backend.json",
        "pages": page_entries,
    }
    (base / "page_level_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
