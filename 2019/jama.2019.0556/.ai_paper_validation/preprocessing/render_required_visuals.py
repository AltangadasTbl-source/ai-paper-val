#!/usr/bin/env python3
"""Render only result-relevant tables, figures, and participant flow pages."""
from __future__ import annotations

import json
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[2]
OUTPUTS = ROOT / ".ai_paper_validation" / "document_outputs"
SPECS = {
    "DOC-001": {
        "pdf": "jama_bot_2019_oi_190007.pdf",
        "pages": {
            3: "Figure 1 participant-flow diagram",
            5: "Table 1 baseline characteristics",
            6: "Table 2 primary outcome and Figure 1 continuation",
            7: "Figure 2 secondary-outcome plots",
            8: "Table 3 secondary outcomes",
        },
    },
    "DOC-004": {
        "pdf": "joi190007supp3_prod.pdf",
        "pages": {
            16: "eAppendix 6 results table",
            17: "eAppendix 7 results display",
            18: "eAppendix 8 results table",
            19: "eAppendix 9 interaction display",
            20: "eAppendix 10 results table",
            21: "eAppendix 11 results table",
            22: "eAppendix 12 CACE results table",
            23: "eAppendix 13 concealment results display",
        },
    },
}

for did, spec in SPECS.items():
    ddir = OUTPUTS / did
    manifest_path = ddir / "page_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    doc = fitz.open(ROOT / spec["pdf"])
    rdir = ddir / "rendered_pages"
    rdir.mkdir(parents=True, exist_ok=True)
    records = {record["source_pdf_page"]: record for record in manifest["page_records"]}
    for page_number, label in spec["pages"].items():
        rel = f"rendered_pages/page_{page_number:03d}.png"
        pixmap = doc[page_number - 1].get_pixmap(matrix=fitz.Matrix(2.5, 2.5), alpha=False)
        pixmap.save(ddir / rel)
        record = records[page_number]
        record["required_visual_for_downstream_check"] = label
        record["rendered_image_path"] = rel
        record["ocr_required"] = True
        record["extraction_method"] = "native+ocr"
    manifest["extraction_status"] = "native extraction complete; required visual pages rendered and awaiting OCR"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    doc.close()
