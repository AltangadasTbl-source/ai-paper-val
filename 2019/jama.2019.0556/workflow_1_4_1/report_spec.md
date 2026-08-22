# Workflow 1.4.1 Artifact and Report Specification

## Canonical artifacts

Write new artifacts only below `.ai_paper_validation/review_1_4_1/`, except for the two versioned
reports stored directly below `.ai_paper_validation/`:

```text
.ai_paper_validation/
├── final_report_1_4_1.md
├── final_report_1_4_1.html
└── review_1_4_1/
    ├── run_state.md
    ├── source_inventory.md
    ├── source_hashes_before.sha256
    ├── reused_artifact_hashes_before.sha256
    ├── evidence_asset_inventory.md
    ├── source_coverage.md
    ├── coverage_manifest.md
    ├── extraction/main_quantitative_evidence.md
    ├── extraction/support_quantitative_evidence.md
    ├── relationships/numeric_relationship_inventory.md
    ├── statistics/relationship_inventory.md
    ├── checkers/numeric_consistency.md
    ├── checkers/statistical_pass_1.md
    ├── checkers/cross_source_consistency.md
    ├── checkers/statistical_pass_2.md
    ├── candidate_ledger.md
    ├── verification/evidence_recheck.md
    ├── quality/evidence_quality_audit.md
    ├── limitations.md
    └── review_validation.json
```

Stage-specific shard parts may live in `parts/` subdirectories. Every part must be listed in
`coverage_manifest.md` and merged without loss into the canonical artifact.

## Candidate identity

Use `## C001 — ...`, `## C002 — ...`, and so on in the candidate ledger, evidence recheck, quality
audit, and final report. These four ID sets must be identical. There is no review queue and no count
cap. If complete coverage produces no candidates, all four files must explicitly state that the stable
candidate set is empty.

Each final report card contains these exact bold labels:

- **Candidate statement:**
- **Category:**
- **Exact source locations:**
- **Source evidence:**
- **Reported-versus-comparator:**
- **Reasoning procedure:**
- **Calculation:**
- **Alternative source-grounded interpretations:**
- **Mechanical evidence recheck:**
- **Quality-control relevance:**
- **Potential downstream evidence impact:**
- **Human verification steps:**
- **Human adjudication fields:**

The final field contains blank entries for validity, importance, action, initials, and notes. Do not
fill them. `Potential downstream evidence impact` must be bounded: identify what a systematic review,
meta-analysis, guideline, or data extractor could copy if the candidate is confirmed; do not claim
that propagation or conclusion change has occurred.

## Final report order

1. Title framed as a quantitative quality-control consistency review.
2. Prominent `Pending Human Adjudication` notice.
3. Executive Quality-Control Summary with the actual candidate count and no severity language.
4. Package and Reused-Evidence Provenance.
5. Scope, Complete Coverage, and Exclusions.
6. Quantitative and Statistical Relationship Coverage, including both statistical passes.
7. Candidate Index containing every stable ID.
8. Candidate Evidence Cards containing every stable ID.
9. Downstream Evidence-Chain Considerations, stated generically and without assumed harm.
10. Limitations and Missing Definitions.
11. Human Adjudication Checklist.
12. Reproducibility, Source-Integrity, and Performance Metadata, including target, observed elapsed
    minutes, target status, and any bounded exceedance causes from `run_state.md`.

Do not reproduce old AI dispositions, a top-10 list, a severity ranking, or a deferred-by-cap section.

## Evidence links

From a report stored directly in `.ai_paper_validation/`:

- source PDF: `[main.pdf — PDF p. 8](<../main.pdf#page=8>)`;
- reused rendered/OCR derivative: name it as provenance, then link the source PDF page as evidence;
- converted Office PDF inside this run: `[derived.pdf — PDF p. 3](<review_1_4_1/preprocessing/converted_pdf/derived.pdf#page=3>)`;
- workbook: link `../support.xlsx` and state worksheet plus exact cell/range;
- CSV: link `../support.csv` and state exact row/column or keyed record;
- DOC/DOCX without a derived PDF: link `../support.docx` and state stable paragraph/table IDs.

Every evidence-card PDF link ends in `#page=N`. Preserve complete actual filenames and stable document
IDs. Do not fabricate PDF pages for Office evidence.

## HTML

Render with:

```bash
python3 workflow_1_4_1/scripts/render_report.py \
  .ai_paper_validation/final_report_1_4_1.md \
  .ai_paper_validation/final_report_1_4_1.html \
  --profile 1.4.1
```

Use Pandoc when available and the dependency-free local fallback otherwise. HTML must be standalone
UTF-8 HTML5 with embedded CSS, a table of contents, responsive/print styling, stable candidate
anchors, and unchanged local relative links. It must load nothing from the web.
