# Workflow 1.6.1 — Reuse Evidence Assets, Screen Findings, and Classify Candidates

Use this profile when a paper package already contains usable OCR, native/layout text, table or
workbook extraction, rendered pages, or document maps. Workflow 1.6.1 treats those assets as a
read-only evidence cache, but performs quantitative relationship mapping, finding discovery, inclusion
screening, and classification from the beginning. Old candidate sets, review queues, verifier/critic
decisions, endetail reports, classification records, and final reports are preserved but are not
scientific inputs or candidate sources. Every source unit missing a usable reusable derivative is
freshly inspected; missing derivatives are not scientific coverage exclusions.

## Main features

- Every finding passes an independent inclusion screen before it can become a candidate. A candidate
  must be reproduced, fall within the four focus areas (counts and denominators, estimate and test
  logic, statistical method logic, planned versus reported statistical design), be unresolvable at
  once by a statistically literate reader in the field from the immediate context, and be able to
  change the interpretation of a named result or an extracted value.
- Rounding and display-precision differences, display-zero P values, notation and typographic slips,
  terminology and wording differences across the text, model-based estimates compared with crude
  ratios, conditional observations, and peripheral cross-document comparisons are screened out with a
  reason code. Cross-document comparisons are tiered: primary and key secondary results and
  planned-versus-reported analysis and endpoint elements can qualify; baseline descriptive values,
  per-time-point counts, pointers, sites, and recruitment calendars normally cannot. The screening log keeps every decision; the report counts screened-out findings without cards.
- One candidate per issue: a repeated pattern is one candidate listing every affected location.
- There is no expected, typical, minimum, maximum, or target number of candidates.
- Every candidate is assigned one of four review domains (`statistical_results`,
  `report_internal_inconsistency`, `protocol_report`, `plan_material`), consistent with its
  relationship type (`P_R`, `P_P`, `S_C`, `S_W`).
- Generated text never calls a candidate an error, mistake, or defect; the validator checks this.
- Every role uses `gpt-6.1-sol`. The coordinator runs at `high`; ordinary specialists at `medium`;
  both statistical passes, the inclusion screener, the evidence rechecker, and the final auditor use
  fresh `high` agents.
- Timing is set separately after each package inventory; no SAP length, page count, or timing band is
  universal.
- Agents perform inventory, coverage planning, mapping, checking, screening, classification,
  rechecking, and synthesis. Python is limited to optional Office structure extraction, a local tool
  probe and temporary fallback environment for missing PDF/OCR tools, local HTML rendering, and
  mechanical validation.
- The run works on Linux, macOS, or Windows machines without poppler or tesseract: it records the
  available tools, installs pinned PyMuPDF/pypdf (and CPU OCR if needed) into a temporary
  package-local environment, and removes that environment at the end.
- The run uses the provider of the current Codex session; nothing is configured for a specific
  provider.

## Installation and start

First read `CODEX_SETUP.md`. Copy the workflow controls into one
paper-package root. Preserve all sources and the existing
`.ai_paper_validation/` directory. Merge the ten hidden `.codex/agents/` role presets without
overwriting unrelated root `.codex` controls; do not place provider credentials in project config.
From the package root run `codex --approve-for-me`. After the interactive session opens, send
`Read START_PROMPT.md completely and execute Workflow 1.6.1 now.` as the first request. No shell
launcher or non-interactive `codex exec` fallback is used.

## Main outputs

```text
.ai_paper_validation/
├── final_report_1_6_1.md
├── final_report_1_6_1.html
└── review_1_6_1/
    ├── routing_preflight.md
    ├── tooling_record.md
    ├── run_state.md
    ├── agent_execution_manifest.md
    ├── evidence_asset_inventory.md
    ├── coverage_manifest.md
    ├── screening/inclusion_screen.md
    ├── candidate_ledger.md
    ├── verification/evidence_recheck.md
    ├── quality/evidence_quality_audit.md
    └── review_validation.json
```

The workflow never overwrites old reports or extraction assets. Completion requires validator status
`PASS`. When observed time exceeds the selected target band, `run_state.md` records bounded causes.
