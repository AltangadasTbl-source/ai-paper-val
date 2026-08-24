# Workflow 1.5.1 — Reuse Evidence Assets and Restart the Review

Use this profile when a paper package already contains usable OCR, native/layout text, table or
workbook extraction, rendered pages, or document maps. Workflow 1.5.1 treats those assets as a
read-only evidence cache, but restarts quantitative relationship mapping and candidate discovery.
Old candidate sets, review queues, verifier/critic decisions, endetail reports, and final reports are
preserved but are not scientific inputs or candidate sources. Every source unit missing a usable
reusable derivative is freshly inspected; missing derivatives are not scientific coverage exclusions.

## Main changes

- Timing is set separately after each package inventory; no SAP length, page count, or timing band is
  universal. The prior 102-total-page run is calibration only for comparable workloads.
- Ordinary Terra roles use `medium` reasoning; only the two-pass statistical consistency role retains
  `high` reasoning, and each pass must start in a distinct fresh Terra/high agent.
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
  limited to optional Office structure extraction, deterministic token-cost calculation, local HTML
  rendering, and mechanical validation.
- Validation checks full source-unit coverage, fresh statistical-agent provenance, exact `__` human
  placeholders, and one artifact path per coverage row without requiring root `.codex` files.
- A coherent very small P value printed as zero is explicitly excluded as a standalone candidate;
  only an independent source-grounded contradiction can qualify.
- Every runtime agent, including the coordinator and repair agents, is tracked. Authoritative token
  usage is summarized separately by agent and by model, then priced with a dated, configurable
  OpenAI token-rate snapshot. The result is labelled a token-only API-equivalent estimate.

## Installation and start

Copy the workflow controls into one paper-package root. Preserve all sources and the existing
`.ai_paper_validation/` directory. The hidden `.codex` presets are optional; do not overwrite an
existing or read-only root `.codex`. Start a fresh Codex session at the package root and send the
complete English `START_PROMPT.md` as the first request.

## Main outputs

```text
.ai_paper_validation/
├── final_report_1_5_1.md
├── final_report_1_5_1.html
└── review_1_5_1/
    ├── run_state.md
    ├── agent_execution_manifest.md
    ├── token_usage_ledger.csv
    ├── token_usage_summary.md
    ├── token_usage_summary.json
    ├── evidence_asset_inventory.md
    ├── coverage_manifest.md
    ├── candidate_ledger.md
    ├── verification/evidence_recheck.md
    ├── quality/evidence_quality_audit.md
    └── review_validation.json
```

The workflow never overwrites old reports or extraction assets. Completion requires validator status
`PASS`. When observed time exceeds the selected target band, `run_state.md` records bounded causes.
If runtime usage telemetry is unavailable, the affected agent is recorded as `UNAVAILABLE` with `__`
token fields; known subtotals remain visible, while the complete package total and price stay blank
instead of being fabricated.
