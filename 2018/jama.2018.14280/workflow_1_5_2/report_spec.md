# Workflow 1.5.2 Artifact and Report Specification

## Canonical artifacts

Write new artifacts only below `.ai_paper_validation/review_1_5_2/`, except for the two versioned
reports stored directly below `.ai_paper_validation/`:

```text
.ai_paper_validation/
├── final_report_1_5_2.md
├── final_report_1_5_2.html
└── review_1_5_2/
    ├── run_state.md
    ├── source_inventory.md
    ├── source_hashes_before.sha256
    ├── evidence_asset_inventory.md
    ├── source_coverage.md
    ├── coverage_manifest.md
    ├── agent_execution_manifest.md
    ├── token_usage_ledger.csv
    ├── token_usage_summary.md
    ├── token_usage_summary.json
    ├── preprocessing/native_text/
    ├── preprocessing/layout_text/
    ├── preprocessing/office_structure/
    ├── preprocessing/converted_pdf/
    ├── preprocessing/rendered_pages/
    ├── preprocessing/ocr_text/
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
`coverage_manifest.md` on its own row and merged without loss into the canonical artifact. The
`Artifact` cell always contains one plain relative path.

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

The final field must use this exact mechanically verifiable blank template; do not substitute a dash,
empty checkbox, omitted value, or prose:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

`Potential downstream evidence impact` must be bounded: identify what a systematic review,
meta-analysis, guideline, or data extractor could copy if the candidate is confirmed; do not claim
that propagation or conclusion change has occurred.

Do not create a card for a coherent very small P value displayed as `P = 0` or equivalent. If a card
mentions a display-zero P value because the same result has an independent supplied-source
contradiction, add this conditional field:

```markdown
**Independent contradiction beyond P=0 display:** Exact conflicting value, rule, and source location.
```

The field must identify the independent mismatch; finite precision, underflow, and the claim that an
exact P value cannot mathematically be zero are not qualifying values.

## Final report order

1. Title framed as a quantitative quality-control consistency review.
2. Prominent `Pending Human Adjudication` notice.
3. Executive Quality-Control Summary with the actual candidate count and no severity language.
4. Package and Fresh-Processing Provenance.
5. Scope, Complete Coverage, and Exclusions.
6. Quantitative and Statistical Relationship Coverage, including both statistical passes.
7. Candidate Index containing every stable ID.
8. Candidate Evidence Cards containing every stable ID.
9. Downstream Evidence-Chain Considerations, stated generically and without assumed harm.
10. Limitations and Missing Definitions.
11. Human Adjudication Checklist.
12. Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata,
    including target basis, source-unit counts, selected target, observed elapsed minutes, target
    status, bounded exceedance causes, every agent/model, token-accounting status, model-level token
    totals, package total, known token cost, and complete estimated token cost when available.

The final report token-accounting subsection must contain these exact labels:

```markdown
- **Token accounting status:** COMPLETE, INCOMPLETE_BILLING_BREAKDOWN, or INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** COMPLETE or INCOMPLETE
- **Total tokens:** INTEGER KNOWN THROUGH THE ACCOUNTING WINDOW
- **Known token cost (USD):** DECIMAL
- **Estimated complete token cost (USD):** DECIMAL or __
```

Also include one compact row per model from `token_usage_summary.md` and refer to the versioned token
summary artifact for the per-agent detail. Cached input and cache-write counts are input subsets;
reasoning is an output subset. Never present their sum as additional total tokens. Label every amount
as a token-only API-equivalent estimate under the dated price snapshot, not an invoice.

Do not reproduce old AI dispositions, a top-10 list, a severity ranking, or a deferred-by-cap section.

## Evidence links

From a report stored directly in `.ai_paper_validation/`:

- source PDF: `[main.pdf — PDF p. 8](<../main.pdf#page=8>)`;
- freshly derived PDF: `[derived.pdf — PDF p. 3](<review_1_5_2/preprocessing/converted_pdf/derived.pdf#page=3>)` and name its source Office file;
- workbook: link `../support.xlsx` and state worksheet plus exact cell/range;
- CSV: link `../support.csv` and state exact row/column or keyed record;
- DOC/DOCX without derived PDF: link `../support.docx` and state stable paragraph/table IDs.

Every evidence-card PDF link ends in `#page=N`. Preserve complete actual filenames and stable document
IDs. Do not fabricate PDF pages for Office evidence.

## HTML

Render with:

```bash
python3 workflow_1_5_2/scripts/render_report.py \
  .ai_paper_validation/final_report_1_5_2.md \
  .ai_paper_validation/final_report_1_5_2.html \
  --profile 1.5.2
```

Use Pandoc when available and the dependency-free local fallback otherwise. HTML must be standalone
UTF-8 HTML5 with embedded CSS, a table of contents, responsive/print styling, stable candidate
anchors, and unchanged local relative links. It must load nothing from the web.
