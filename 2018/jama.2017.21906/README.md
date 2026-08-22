# Workflow 1.5.3 — Reuse Evidence Assets and Restart the Review

Use this profile when a paper package already contains usable OCR, native/layout text, table or
workbook extraction, rendered pages, or document maps. Workflow 1.5.3 treats those assets as a
read-only evidence cache, but restarts quantitative relationship mapping and candidate discovery.
Old candidate sets, review queues, verifier/critic decisions, endetail reports, and final reports are
preserved but are not scientific inputs or candidate sources. Every source unit missing a usable
reusable derivative is freshly inspected; missing derivatives are not scientific coverage exclusions.

## Main changes

- Timing is set separately after each package inventory; no SAP length, page count, or timing band is
  universal. The prior 102-total-page run is calibration only for comparable workloads.
- The coordinator uses `gpt-5.6-sol`/`high`; ordinary specialists use
  `gpt-5.6-terra`/`medium`; both statistical passes use fresh `gpt-5.6-terra`/`high` agents; evidence
  recheck and final quality audit use fresh `gpt-5.6-sol`/`high` agents.
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
- Validation checks full source-unit coverage, the fixed model matrix, a distinct fresh runtime ID
  for every mandatory specialist, exact `__` human placeholders, and one artifact path per coverage
  row without requiring root `.codex` files.
- A coherent very small P value printed as zero is explicitly excluded as a standalone candidate;
  only an independent source-grounded contradiction can qualify.
- Every runtime agent, including the coordinator and repair agents, is tracked. Authoritative token
  usage is summarized separately by agent and by model and priced from the bundled dated Sol/Terra
  token-rate snapshot when complete billing detail is available.

## Installation and start

First satisfy `OPENROUTER_SETUP.md`. Copy the workflow controls into one
paper-package root. Preserve all sources and the existing
`.ai_paper_validation/` directory. Merge the nine hidden `.codex/agents/` role presets without
overwriting unrelated root `.codex` controls; do not place provider credentials in project config.
From the package root run `codex --approve-for-me`. After the interactive session opens, send
`Read START_PROMPT.md completely and execute Workflow 1.5.3 now.` as the first request. No shell
launcher or non-interactive `codex exec` fallback is used.

## Main outputs

```text
.ai_paper_validation/
├── final_report_1_5_3.md
├── final_report_1_5_3.html
└── review_1_5_3/
    ├── routing_preflight.md
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
