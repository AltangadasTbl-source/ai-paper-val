# Workflow 1.4.1 — Reuse Evidence Assets and Restart the Review

Use this profile when a paper package already contains usable OCR, native/layout text, table or
workbook extraction, rendered pages, or document maps. Workflow 1.4.1 treats those assets as a
read-only evidence cache, but restarts quantitative relationship mapping and candidate discovery.
Old candidate sets, review queues, verifier/critic decisions, endetail reports, and final reports are
preserved but are not scientific inputs or candidate sources.

## Main changes

- The planning target for a typical single medical-paper package is 20–25 minutes.
- Ordinary Terra roles use `medium` reasoning; only the two-pass statistical consistency role retains
  `high` reasoning.
- Larger default shards and fewer redundant waves reduce orchestration latency without permitting
  sampling, early stopping, or incomplete coverage.
- There is no candidate-count limit and no review queue. The final Markdown and HTML reports contain
  every stable candidate.
- The review focuses on numeric, denominator/proportion/total, statistical-reporting, cross-document
  numeric, effect-measure/label/scale, and rate-versus-count consistency.
- The report uses a quality-control and proofreading tone. It describes bounded risk of preventable
  defects entering systematic reviews or meta-analyses without claiming serious harm or conclusion
  change.
- Agents perform inventory, coverage planning, mapping, checking, rechecking, and synthesis. Python is
  limited to optional Office structure extraction, local HTML rendering, and mechanical validation.

## Installation and start

Copy the entire directory, including hidden `.codex`, into one paper-package root. Preserve all source
files and the existing `.ai_paper_validation/` directory. Start a fresh Codex session at that package
root and send the complete English `START_PROMPT.md` as the first request.

## Main outputs

```text
.ai_paper_validation/
├── final_report_1_4_1.md
├── final_report_1_4_1.html
└── review_1_4_1/
    ├── run_state.md
    ├── evidence_asset_inventory.md
    ├── coverage_manifest.md
    ├── candidate_ledger.md
    ├── verification/evidence_recheck.md
    ├── quality/evidence_quality_audit.md
    └── review_validation.json
```

The workflow never overwrites old reports or extraction assets. Completion requires validator status
`PASS`. When observed review time exceeds 25 minutes, `run_state.md` must record bounded causes.
