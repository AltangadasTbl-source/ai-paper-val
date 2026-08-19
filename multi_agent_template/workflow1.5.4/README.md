# Workflow 1.5.4 — OpenRouter Full Source-First Restart

Use this profile when a paper package must be reviewed again from the supplied PDF, Office, workbook,
or CSV sources. Workflow 1.5.4 rebuilds inventory, native/layout text, table evidence, page rendering,
OCR decisions, quantitative relationship maps, candidates, rechecks, and reports. Existing audit
outputs remain untouched but are not evidence inputs.

## Main changes

- Timing is set separately after each package inventory; no SAP length, page count, or timing band is
  universal. The prior 102-total-page run is calibration only for comparable workloads.
- Every coordinator and specialist role uses `~openai/gpt-latest` with `high` reasoning. Mandatory
  stages still start in distinct fresh agents.
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
  deterministic token-cost calculation, local HTML rendering, and mechanical validation.
- Validation checks full source-unit coverage, authenticated launcher routing preflight, a distinct
  fresh runtime ID and `~openai/gpt-latest`/`high` for every mandatory specialist, exact `__` human
  placeholders, and one artifact path per coverage row without requiring root `.codex` files.
- A coherent very small P value printed as zero is explicitly excluded as a standalone candidate;
  only an independent source-grounded contradiction can qualify.
- Every runtime agent, including the coordinator and repair agents, is tracked. Authoritative token
  usage is summarized separately by agent and by model. Because `~openai/gpt-latest` is a dynamic
  OpenRouter route, the complete price stays blank unless dated rates for the exact resolved model are
  deliberately added; the workflow never reuses a fixed-model OpenAI rate for the alias.

## Installation and start

First satisfy `OPENROUTER_SETUP.md`. Copy the workflow controls into one
paper-package root. Preserve all source files and old
`.ai_paper_validation/` records. Merge the nine hidden `.codex/agents/` role presets without
overwriting unrelated root `.codex` controls; do not place provider credentials in project config.
From the package root run
`bash workflow_1_5_4/scripts/launch_openrouter.sh`; do not start with plain `codex` or `resume`. The
launcher authenticates one ephemeral request, ignores conflicting base user defaults, and then runs
the review to completion through `codex exec`.

## Main outputs

```text
.ai_paper_validation/
├── final_report_1_5_4.md
├── final_report_1_5_4.html
└── review_1_5_4/
    ├── routing_preflight.md
    ├── run_state.md
    ├── agent_execution_manifest.md
    ├── token_usage_ledger.csv
    ├── token_usage_summary.md
    ├── token_usage_summary.json
    ├── evidence_asset_inventory.md
    ├── preprocessing/
    ├── coverage_manifest.md
    ├── candidate_ledger.md
    ├── verification/evidence_recheck.md
    ├── quality/evidence_quality_audit.md
    └── review_validation.json
```

The workflow never overwrites sources or old review outputs. Completion requires validator status
`PASS`. When observed time exceeds the selected target band, `run_state.md` records bounded causes.
If runtime usage telemetry is unavailable, the affected agent is recorded as `UNAVAILABLE` with `__`
token fields; known subtotals remain visible, while the complete package total and price stay blank
instead of being fabricated.
