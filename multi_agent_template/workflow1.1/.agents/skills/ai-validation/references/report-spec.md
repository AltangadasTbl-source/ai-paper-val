# Report and artifact specification

## Canonical artifacts

Write only below `audit/`:

```text
audit/
├── package_manifest.md
├── package_manifest.json
├── run_metadata.json
├── context_coverage.md
├── documents/<document-id>/record.md
├── preprocessing/
│   ├── ocr_backend.json
│   ├── page_manifest.json
│   ├── converted_pdf/
│   ├── normalized_text/
│   ├── rendered_pages/
│   └── ocr_text/
├── extraction/
│   ├── main_evidence.md
│   └── supplement_evidence.md
├── checkers/
│   ├── table_arithmetic.md
│   ├── figure_flow.md
│   └── statistical_consistency.md
├── statistics/coverage_matrix.md
├── candidate_registry.md
├── verification/evidence_recheck.md
├── quality/evidence_quality_audit.md
├── final_report.md
├── final_report.html
└── audit_validation.json
```

Agent responses must be preserved at these paths or incorporated verbatim into the corresponding artifact. Do not depend on unrecorded chat messages.

Sharded specialist outputs may be stored in stage-specific `parts/` subdirectories. Each part requires
a unique scope and path in `context_coverage.md`. Canonical artifacts must contain the complete merged
content before report assembly, and every coverage row must be marked complete.

## Context coverage record

Use this exact five-column Markdown table in `audit/context_coverage.md`:

```markdown
| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| main_extraction | main-001 | DOC001 PDF pp. 1-12 | extraction/parts/main-001.md | COMPLETE |
```

The required stage IDs are `main_extraction`, `supplement_extraction`, `table_arithmetic`,
`figure_flow`, `statistics_pass_1`, `evidence_verification`, `statistics_pass_2`, `evidence_quality`,
and `report_generation`. Use one or more rows per stage. Shard IDs must be unique within a stage,
scopes must be disjoint and collectively exhaustive for that stage, and artifact paths are relative to
`audit/`. Every artifact must exist and be nonempty. Use only `COMPLETE`; the sole exception is
`supplement_extraction`, which may use `NOT_APPLICABLE` when the manifest confirms that no
result-relevant supplement exists. The final `report_generation` row points to `final_report.md`.

## Final report structure

Produce detailed professional English in this order:

1. Title and prominent `Pending Human Adjudication` notice.
2. Package Manifest.
3. Audit Scope, Coverage, and Exclusions.
4. Processing and OCR Backend Provenance.
5. Statistical Coverage Summary, including checked and not-checkable relationships.
6. Candidate Index with ID, category, concise statement, and HTML anchor.
7. Candidate Evidence Cards containing every candidate.
8. Limitations and Missing Evidence.
9. Human Adjudication Checklist.
10. Reproducibility Metadata.

Do not show AI-assigned severity, validity, disposition, acceptance, or rejection labels.

## Evidence card

Give every candidate a stable heading and anchor, for example `## C001 — ...`. Include:

- **Candidate statement:** one sentence naming the displayed inconsistency without declaring misconduct or final validity.
- **Category:** one allowed taxonomy value.
- **Exact PDF evidence locations:** stable document ID paired with complete filename, PDF page, journal page when available, and table/figure/panel/row/column/footnote/section label.
- **Source evidence:** labelled verbatim excerpts or printed values with units.
- **Reported-versus-comparator:** exact quantities/statements, discrepancy size and direction when calculable.
- **Reasoning procedure:** numbered, reproducible chain distinguishing direct observations from derived results.
- **Calculation:** inputs, formula or logical rule, result, units, precision, and rounding tolerance.
- **Alternative source-grounded interpretations:** include only alternatives supported by supplied pages.
- **Mechanical evidence recheck:** location found, values matched, calculation reproduced, and missing inputs as separate factual fields.
- **Bounded impact:** identify only which displayed total, statement, label, or interpretation would require confirmation or correction.
- **Human verification steps:** numbered checks and the results that would resolve the question.
- **Human adjudication fields:** blank validity, importance, action, initials, and notes fields.

Do not say merely “the values do not match.” Show all arithmetic or logic.

## Relative PDF deep links

Every evidence citation must link to its exact PDF page. From `audit/final_report.md` and `audit/final_report.html`:

```markdown
[main_article.pdf — PDF p. 8](<../main_article.pdf#page=8>)
[converted_supplement.pdf — PDF p. 12](<preprocessing/converted_pdf/converted_supplement.pdf#page=12>)
```

Pair document IDs with linked filenames rather than replacing either one. Links to a PDF as a whole are permitted in the package manifest, but every evidence-card citation requires `#page=N`.

## HTML rendering

Render the Markdown during the initial workflow with `scripts/render_report.py`. The HTML must be standalone UTF-8 HTML5 with an embedded stylesheet, table of contents, responsive tables, print styling, candidate anchors, and local relative PDF links. It must not load scripts, fonts, styles, or data from the web.

Run `scripts/validate_audit.py` after rendering. Repair validation failures before completion. A source file modified during the run is a failed audit, not a warning.
