# Workflow 1.6 — Reuse Evidence Assets, Review, and Classify Candidates

Use this profile when a paper package already contains usable OCR, native/layout text, table or
workbook extraction, rendered pages, or document maps. Workflow 1.6 treats those assets as a
read-only evidence cache, but performs quantitative relationship mapping, candidate discovery, and
document-role classification from the beginning. Old candidate sets, review queues, verifier/critic
decisions, endetail reports, classification records, and final reports are preserved but are not
scientific inputs or candidate sources. Every source unit missing a usable reusable derivative is
freshly inspected; missing derivatives are not scientific coverage exclusions.

## Main features

- Timing is set separately after each package inventory; no SAP length, page count, or timing band is
  universal. The prior 102-total-page run is calibration only for comparable workloads.
- Every role uses `gpt-6.1-sol`. The coordinator runs at `high`; ordinary specialists at `medium`;
  both statistical passes use fresh `high` agents; evidence recheck with classification confirmation
  and the final quality and classification audit use fresh `high` agents.
- Larger default shards and fewer redundant waves reduce orchestration latency without permitting
  sampling, early stopping, or incomplete coverage.
- There is no candidate-count limit and no review queue. The final Markdown and HTML reports contain
  every stable candidate.
- The review focuses on numeric, denominator/proportion/total, statistical-reporting, cross-document
  numeric, effect-measure/label/scale, and rate-versus-count consistency.
- Every stable candidate is classified by document role into one of four relationship types: `P_R`
  (report versus protocol/SAP), `P_P` (within plan material), `S_C` (between report documents), or
  `S_W` (within one report document). The review domain and suggested review disposition are derived
  mechanically from the relationship type, primary category, and evidence state, so the report can
  pre-fill the human review workbook directly.
- The report uses a quality-control and proofreading tone. It describes bounded risk of preventable
  defects entering systematic reviews or meta-analyses without claiming serious harm or conclusion
  change.
- Agents perform inventory, coverage planning, mapping, checking, classification, rechecking, and
  synthesis. Python is limited to optional Office structure extraction, a local tool probe and
  temporary fallback environment for missing PDF/OCR tools, local HTML rendering, and mechanical
  validation.
- The run works on Linux, macOS, or Windows machines without poppler or tesseract: it records the
  available tools, installs pinned PyMuPDF/pypdf (and CPU OCR if needed) into a temporary
  package-local environment, and removes that environment at the end.
- Validation checks full source-unit coverage, the fixed model matrix, a distinct fresh runtime ID
  for every mandatory specialist, complete and internally consistent classifications, exact `__`
  human placeholders, and one artifact path per coverage row without requiring root `.codex` files.
- A coherent very small P value printed as zero is explicitly excluded as a standalone candidate;
  only an independent source-grounded contradiction can qualify.
- Every runtime agent, including the coordinator and repair agents, is recorded in the execution
  manifest.

## Installation and start

First satisfy `OPENROUTER_SETUP.md`. Copy the workflow controls into one
paper-package root. Preserve all sources and the existing
`.ai_paper_validation/` directory. Merge the nine hidden `.codex/agents/` role presets without
overwriting unrelated root `.codex` controls; do not place provider credentials in project config.
From the package root run `codex --approve-for-me`. After the interactive session opens, send
`Read START_PROMPT.md completely and execute Workflow 1.6 now.` as the first request. No shell
launcher or non-interactive `codex exec` fallback is used.

## Main outputs

```text
.ai_paper_validation/
├── final_report_1_6.md
├── final_report_1_6.html
└── review_1_6/
    ├── routing_preflight.md
    ├── tooling_record.md
    ├── run_state.md
    ├── agent_execution_manifest.md
    ├── evidence_asset_inventory.md
    ├── coverage_manifest.md
    ├── candidate_ledger.md
    ├── verification/evidence_recheck.md
    ├── quality/evidence_quality_audit.md
    └── review_validation.json
```

The workflow never overwrites old reports or extraction assets. Completion requires validator status
`PASS`. When observed time exceeds the selected target band, `run_state.md` records bounded causes.
