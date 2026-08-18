# Workflow 1.4.2 — Full Source-First Restart

Use this profile when a paper package must be reviewed again from the supplied PDF, Office, workbook,
or CSV sources. Workflow 1.4.2 rebuilds inventory, native/layout text, table evidence, page rendering,
OCR decisions, quantitative relationship maps, candidates, rechecks, and reports. Existing audit
outputs remain untouched but are not evidence inputs.

## Main changes

- The planning target for a typical single medical-paper package is 20–25 minutes.
- Ordinary Terra roles use `medium` reasoning; only the two-pass statistical consistency role retains
  `high` reasoning.
- Larger default shards and fewer redundant waves reduce orchestration latency without permitting
  sampling, early stopping, or incomplete coverage.
- Source inventory and evidence preparation restart from the supplied files.
- There is no candidate-count limit and no review queue. The final Markdown and HTML reports contain
  every stable candidate.
- The review focuses on numeric, denominator/proportion/total, statistical-reporting, cross-document
  numeric, effect-measure/label/scale, and rate-versus-count consistency.
- The report uses a quality-control and proofreading tone and describes downstream evidence-chain risk
  without claiming serious harm or conclusion change.
- Agents lead the scientific workflow. Python is limited to optional Office structure extraction,
  local HTML rendering, and mechanical validation.

## Installation and start

Copy the entire directory, including hidden `.codex`, into one paper-package root. Preserve all source
files and old `.ai_paper_validation/` records. Start a fresh Codex session at that package root and
send the complete English `START_PROMPT.md` as the first request.

## Main outputs

```text
.ai_paper_validation/
├── final_report_1_4_2.md
├── final_report_1_4_2.html
└── review_1_4_2/
    ├── run_state.md
    ├── evidence_asset_inventory.md
    ├── preprocessing/
    ├── coverage_manifest.md
    ├── candidate_ledger.md
    ├── verification/evidence_recheck.md
    ├── quality/evidence_quality_audit.md
    └── review_validation.json
```

The workflow never overwrites sources or old review outputs. Completion requires validator status
`PASS`. When observed review time exceeds 25 minutes, `run_state.md` must record bounded causes.
