"""Extract and normalize text from explicitly scoped PDF pages."""
from __future__ import annotations

import json
import re
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[2]
SPECS = (
    ("D01", "jama_brenner_2019_oi_190039.pdf", range(1, 8)),
    ("D04", "joi190039supp3_prod.pdf", range(4, 9)),
)


def normalized(text: str) -> str:
    lines = [re.sub(r"[ \\t]+", " ", line).strip() for line in text.replace("\\r\\n", "\\n").replace("\\r", "\\n").split("\\n")]
    return "\\n".join(lines).strip() + "\\n"


def assess(text: str) -> dict[str, object]:
    nonspace = [c for c in text if not c.isspace()]
    words = re.findall(r"[A-Za-z0-9]+", text)
    bad = text.count("\\ufffd") + sum(1 for c in text if ord(c) < 32 and c not in "\\n\\t\\r")
    character_count = len(nonspace)
    bad_ratio = bad / max(character_count, 1)
    status = "adequate" if character_count >= 100 and len(words) >= 20 and bad_ratio <= 0.01 else "needs_ocr_review"
    return {
        "extraction_quality": status,
        "nonwhitespace_characters": character_count,
        "alphanumeric_tokens": len(words),
        "corrupt_character_count": bad,
        "corrupt_character_ratio": round(bad_ratio, 6),
    }


records: list[dict[str, object]] = []
for doc_id, filename, pages in SPECS:
    source = ROOT / filename
    output_dir = ROOT / ".ai_paper_validation" / "document_outputs" / doc_id / "native_pages"
    output_dir.mkdir(parents=True, exist_ok=True)
    with fitz.open(source) as pdf:
        for pdf_page in pages:
            raw = pdf[pdf_page - 1].get_text("text", sort=True)
            text = normalized(raw)
            output = output_dir / f"page-{pdf_page}.txt"
            output.write_text(text, encoding="utf-8")
            records.append({
                "document_id": doc_id,
                "source_pdf": filename,
                "source_pdf_page": pdf_page,
                "native_text_path": str(output.relative_to(ROOT)),
                "native_text_characters": len(text),
                **assess(text),
            })

(ROOT / ".ai_paper_validation" / "preprocessing" / "native_extraction_quality.json").write_text(
    json.dumps({"schema_version": 1, "pages": records}, indent=2) + "\\n", encoding="utf-8"
)
