# Workflow 1.2.0 artifact and report specification

## Canonical artifacts

All outputs live below `.ai_paper_validation/`:

```text
source_inventory.json
source_inventory.md
source_hashes_before.json
run_state.json
package_manifest.json
package_manifest.md
source_coverage.md
coverage_manifest.json
documents/<document-id>/record.md
rights/content_use_restriction_summary.md
preprocessing/native_text/
preprocessing/office_text/
preprocessing/workbooks/
preprocessing/converted_pdf/
preprocessing/rendered_pages/
preprocessing/ocr_text/
extraction/main_evidence.md
extraction/support_evidence.md
checkers/table_arithmetic.md
checkers/figure_flow.md
checkers/statistical_pass_1.md
checkers/statistical_pass_2.md
statistics/coverage_matrix.md
statistics/coverage_matrix.json
candidate_ledger.md
verification/evidence_recheck.md
quality/evidence_quality_audit.md
review_queue.md
final_report_1_2_0.md
final_report_1_2_0.html
audit_validation_1_2_0.json
```

## Candidate artifacts

Use `## C001 — ...` headings in the ledger, evidence recheck, quality audit, queue, and report. The
ledger, recheck, and quality ID sets are identical. The queue is a subset of at most 10. The final
report ID set exactly equals the queue.

Every ledger section includes `**Queue routing status:**`. Every report card contains these exact
labels:

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

Human validity, importance, action, initials, and notes remain blank.

## Final report order

1. Title and prominent `Pending Human Adjudication` notice.
2. Package Manifest.
3. Content-Use Restriction Summary, separate from scientific candidates.
4. Audit Scope, Format Handling, Coverage, and Exclusions.
5. Processing and CPU-OCR Provenance.
6. Statistical Coverage Summary for both passes.
7. Human Review Queue Index, at most 10.
8. Candidate Evidence Cards, exactly the queue.
9. Deferred Candidate Ledger Summary with a link to `candidate_ledger.md`.
10. Limitations and Missing Evidence.
11. Human Adjudication Checklist.
12. Reproducibility and Source-Integrity Metadata.

## Evidence links

- PDF: `[paper.pdf — PDF p. 8](<../paper.pdf#page=8>)`.
- Converted Office PDF: link under `preprocessing/converted_pdf/...#page=N` and name the original.
- DOCX without PDF: link `../support.docx` and state `P####` or `T### R### C###`.
- Workbook: link `../support.xlsx` and state worksheet plus exact cell/range.
- CSV: link `../support.csv` and state exact row/column or key.

Render with `workflow_1_2_0/scripts/render_report.py`. Use Pandoc when present; otherwise use its
dependency-free renderer. HTML must be standalone UTF-8 HTML5 with embedded CSS and a TOC.
