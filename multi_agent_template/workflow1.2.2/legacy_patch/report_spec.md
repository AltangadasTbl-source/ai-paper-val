# Patch 1.2.2 artifact and report specification

## Required patch artifacts

Write new files only at these paths:

```text
.ai_paper_validation/
├── final_report_1_2_2.md
├── final_report_1_2_2.html
└── patch_1_2_2/
    ├── legacy_inventory.json
    ├── legacy_inventory.md
    ├── run_state.json
    ├── source_hashes_before.json
    ├── endetail_harvest.md
    ├── legacy_source_coverage.md
    ├── lineage_map.md
    ├── recovered_candidate_ledger.md
    ├── evidence_recheck.md
    ├── statistical_reconciliation.md
    ├── review_queue.md
    ├── quality_audit.md
    ├── recovery_log.md
    └── patch_validation.json
```

Do not rename, edit, or move any pre-existing file.

`endetail_harvest.md` must account for every stable candidate heading in the expanded legacy report,
including candidates in its Uncertain and Rejected sections. It preserves calculations and limits for
reuse while treating every old disposition as non-authoritative provenance.

## Source coverage

`legacy_source_coverage.md` must quote every path listed under `candidate_sources` in
`legacy_inventory.json` and record one status: `MAPPED`, `CONTEXT_ONLY`, or `UNREADABLE`. For
`UNREADABLE`, give the exact reason and continue. This table proves the patch did not rely only on the
old final report.

## Ledger, lineage, and queue

Use `## Cxx — ...`, `## Cxxx — ...`, or `## Rxxx — ...` headings for stable candidates in the
recovered ledger, evidence recheck, quality audit, queue, and report. `lineage_map.md` must map every
raw candidate occurrence to one retained ID or a context-only status.

The ledger has no count limit. The queue has at most 10 IDs and is a subset of the ledger. Give every
ledger ID a queue routing status and tuple values from the deterministic queue policy. Do not show an
AI severity or scientific disposition.

## Final report order

1. Title and prominent `Pending Human Adjudication` notice.
2. Patch Provenance and Legacy Inputs.
3. Endetail Reuse Summary: harvested candidates/calculations, source-confirmed reuse, and repairs.
4. Package Manifest.
5. AI Training Restriction Summary, carried forward separately when legacy records contain it.
6. Recovery Scope, Source Coverage, and Known Legacy Gaps.
7. Human Review Queue Index (at most 10).
8. Candidate Evidence Cards, exactly matching the queue.
9. Deferred-Ledger Summary with counts and a link to `patch_1_2_2/recovered_candidate_ledger.md`.
10. Limitations and Missing Evidence.
11. Human Adjudication Checklist.
12. Reproducibility and Source-Integrity Metadata.

Do not reproduce old AI disposition tables in the patched report.

## Evidence card fields

Each queued candidate section must contain these exact bold field labels:

- **Candidate statement:**
- **Category:**
- **Exact source locations:**
- **Source evidence:**
- **Reported-versus-comparator:**
- **Reasoning procedure:**
- **Calculation:**
- **Alternative source-grounded interpretations:**
- **Mechanical evidence recheck:**
- **Bounded impact:**
- **Human verification steps:**
- **Human adjudication fields:**

The last field contains blank entries for validity, importance, action, initials, and notes. Do not
fill them. A candidate may state that a calculation is not applicable, but it may not omit the field.

## Links and HTML

Every evidence location must pair the stable document ID (when available) with the complete actual
filename, PDF page, and table/figure/row/column/section label. From a report stored directly in
`.ai_paper_validation/`, use links such as:

```markdown
[main_article.pdf — PDF p. 8](<../main_article.pdf#page=8>)
```

Every evidence-card PDF link ends in `#page=N`. For spreadsheet-only evidence, link the actual `.xls`
or `.xlsx` file and state the worksheet plus exact cell/range; for CSV, state row and column; for
DOC/DOCX without a derived PDF, state the exact paragraph/table identifier. Render with:

```bash
python3 legacy_patch/scripts/render_report.py \
  .ai_paper_validation/final_report_1_2_2.md \
  .ai_paper_validation/final_report_1_2_2.html
```

The HTML must be standalone UTF-8 HTML5 with an embedded stylesheet and table of contents.
