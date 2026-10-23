# Quantitative Quality-Control Review 1.6.2 — Reuse Existing Evidence Assets

The current project root is exactly one paper package. The package may contain earlier
`.ai_paper_validation/` records. Workflow 1.6.2 performs candidate discovery from the beginning, while
reusing all usable existing OCR, native text, layout text, table extraction,
workbook extraction, rendered pages, and document maps. Reuse is an optimization, not a coverage
boundary: every direct-source unit that lacks usable reusable extraction must be freshly inspected and
mapped from the supplied source. Every finding passes an independent inclusion screen under
`QUALITY_CONTROL_SCOPE.md` before it can become a candidate, and every candidate is assigned one of
four review domains.

Use English only in prompts, generated artifacts, logs, and reports. Preserve every supplied source
and every pre-existing audit artifact. Write new work only to:

- `.ai_paper_validation/review_1_6_2/`
- `.ai_paper_validation/final_report_1_6_2.md`
- `.ai_paper_validation/final_report_1_6_2.html`

## Agent-first execution

Start immediately and operate autonomously. The coordinator plans coverage, delegates bounded and
disjoint evidence scopes to specialist agents, merges their durable artifacts, and verifies coverage.
Python is auxiliary only. Do not use Python to orchestrate the scientific review, select or classify
candidates, or replace agent reasoning. Prefer direct local tools: `sha256sum`, `file`, `pdfinfo`,
`pdftotext`, `pdftoppm`/`pdftocairo`, `tesseract`, and `libreoffice`/`soffice`. The only permitted
Python helpers are those in `workflow_1_6_2/scripts/`: the optional Office structure extractor, the
tooling bootstrap and PDF/OCR/hash fallback helper described below, the report renderer, and the final
validator. Do not write other Python for extraction or OCR.

## Local tools and the temporary fallback environment

The review runs on a local machine (Linux, macOS, or Windows) where direct tools may be missing.
Before source inventory, probe the machine and record the result in
`.ai_paper_validation/review_1_6_2/tooling_record.md`:

```bash
python3 workflow_1_6_2/scripts/pdf_tools.py probe
```

If PDF information, text, or page rendering is unavailable as a direct tool, create the temporary
package-local fallback environment; add `--ocr` only when OCR may be needed and `tesseract` is absent:

```bash
python3 workflow_1_6_2/scripts/bootstrap_tooling.py create
```

The environment is created only under `.ai_paper_validation/review_1_6_2/tooling/`, with pinned
packages and a local package cache; never install into the global Python environment. Then use the
fallback helper with that environment's interpreter, and only for capabilities the probe recorded as
missing:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py info "source.pdf"
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text "source.pdf" --first N --last N ".ai_paper_validation/review_1_6_2/preprocessing/native-N.txt"
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text "source.pdf" --first N --last N ".ai_paper_validation/review_1_6_2/preprocessing/layout-N.txt" --layout
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render "source.pdf" --page N ".ai_paper_validation/review_1_6_2/preprocessing/page-N.png"
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py ocr ".ai_paper_validation/review_1_6_2/preprocessing/page-N.png" ".ai_paper_validation/review_1_6_2/preprocessing/ocr-N.txt"
python3 workflow_1_6_2/scripts/pdf_tools.py sha256 "source.pdf"
```

On Windows the interpreter is `.ai_paper_validation\review_1_6_2\tooling\venv\Scripts\python.exe`.
Every specialist uses the tooling recorded in `tooling_record.md`. Record the engine with every
derivative it produces. If installation fails, for example because the sandbox blocks network access,
record `INSTALL_FAILED`, continue with reusable assets and the tools that are available, inspect
rendered or reusable page images visually where text is unusable, and list every affected unit as a
limitation. A missing tool never permits omitting a source unit. After rendering HTML and before the
final validation, remove the environment with `python3 workflow_1_6_2/scripts/bootstrap_tooling.py
remove` and record the removal.

Use artifact-first handoffs. Every specialist writes complete English output to one unique assigned
path and returns only a compact status, exact scope, counts, limitations, and artifact path. Never let
two agents write the same artifact concurrently. Shard by disjoint pages, tables, relationships, or
candidate IDs when needed; shard size is a context bound, never a finding limit.

Do not put provider credentials or provider selection in the package-root `.codex/config.toml`.
The direct interactive session requires the ten bundled `.codex/agents/` role presets and verifies
each one before scientific work. Preserve unrelated package `.codex` controls when copying those
files. Validation does not rewrite `.codex/`.

## Run model selection

The default run model is `gpt-6.1-sol`, and every role uses one run model; roles differ only in
reasoning effort. Wherever these instructions, the presets, or the examples name `gpt-6.1-sol`, read
it as the run model. If `gpt-6.1-sol` is rejected or unavailable at preflight, or the user wants a
different model (for example a later release), stop before scientific work and ask the user which
exact model ID to use. Never choose a substitute model yourself. Once the user names it, set that ID
as `model` in `.codex/config.toml` and in all ten `.codex/agents/qc162-*.toml` presets (or confirm the
user has done so), and record `Run model: <ID>` with `Run model source: USER_SELECTED` in
`routing_preflight.md`; otherwise record `Run model: gpt-6.1-sol` with `Run model source: DEFAULT`.
Use an exact model ID, never a moving alias such as `~openai/gpt-latest`, so that repeated reviews
run under the same recorded conditions.

## CPU by default

Rendering and OCR run on the CPU by default. Before the first rendering or OCR step, tell the user in
the session that processing is running on the CPU and that GPU OCR can be used if they ask for it.
Use a GPU only after the user explicitly requests it, with a GPU-capable OCR engine the user approves;
record the device in `tooling_record.md` (`Compute device: CPU` or `Compute device: GPU_USER_REQUESTED`)
and the engine with every derivative.

## Model routing contract

Start from the package root with `codex --approve-for-me`, then send `Read START_PROMPT.md completely
and execute Workflow 1.6.2 now.` as the first request. The current Codex session supplies the provider
and authentication; do not configure or change a provider; the project config fixes the coordinator at the run model/`high` and the
ten named presets fix every specialist model/effort pair. Every role uses the run model (default
`gpt-6.1-sol`); roles differ only in reasoning effort. Do not use `~openai/gpt-latest`, another moving alias, a shell launcher, or
`codex exec` fallback.

Before scientific work, create `routing_preflight.md` and require it to report `PASS`, the run model and its source, coordinator
`gpt-6.1-sol`/`high`, ordinary specialists `gpt-6.1-sol`/`medium`, statistical specialists
`gpt-6.1-sol`/`high`, screening, recheck and audit specialists `gpt-6.1-sol`/`high`, `Coordinator
inference: PASS`, execution mode `INTERACTIVE_CLI`, `Provider: CURRENT_SESSION`, and all
ten named agent presets verified against their required pairs.

Every mandatory specialist stage uses a fresh agent and a distinct runtime ID. Use the named custom
agent preset when available. Otherwise use a fresh default agent, pass the exact fixed model and
reasoning effort for that role, and include the role contract in the spawn prompt. Never reuse an
agent for another mandatory stage, promote an agent with follow-up, omit a fallback model override, or
change the fixed reasoning effort of a role. Record the exact model ID in the execution manifest.

## Read before reviewing

Read completely:

- `QUALITY_CONTROL_SCOPE.md`
- `PERFORMANCE_PROFILE.md`
- `workflow_1_6_2/review_contract.md`
- `workflow_1_6_2/report_spec.md`
- `workflow_1_6_2/settings.toml`

Do not read an old candidate set, review queue, verifier disposition, critic decision, endetail
section, screening log, classification record, or final report as a scientific input or candidate
source. Preserve
those records unchanged, but build discovery and classification from source-linked reusable assets
plus mandatory direct-source inspection of every uncovered unit.

## Required workflow

1. Verify `routing_preflight.md` first, asking the user for a model if the default is unavailable.
   Probe local tools, tell the user that rendering and OCR run on the CPU unless they request a GPU,
   create the fallback environment if needed, and write `tooling_record.md`. Record the UTC start time, then inventory every direct source, its complete stable unit count, and
   SHA-256 in `.ai_paper_validation/review_1_6_2/source_hashes_before.sha256`. Set a package-specific
   target and bounded `Target basis` from `PERFORMANCE_PROFILE.md`; do not infer either from SAP length
   or page count alone. Initialize every required field in `run_state.md`. Initialize
   `agent_execution_manifest.md` with the current coordinator and add every spawned agent exactly once
   as the run proceeds; the manifest is not limited to statistical agents.
2. Use a fresh `qc162_reuse_asset_curator` agent to inventory and hash every reused OCR/text/table/page/document-map
   artifact in `reused_artifact_hashes_before.sha256` (or, when the package has none, write the single
   line `# NO_REUSABLE_ASSETS` there and count every unit as fresh-required), assess its coverage and
   fitness, and write the
   source and evidence-asset inventories. In `source_coverage.md`, record one row per direct source with
   total, reusable, fresh-required, and mapped unit counts, and record each direct source's document
   role (`REPORT` or `PLAN`) by content in `source_inventory.md`. Do not modify reused artifacts.
3. Compare reusable coverage against every direct-source unit. Assign every uncovered page, sheet,
   record group, paragraph group, and table group to fresh direct-source extraction and mapping. The
   reusable and fresh-required unit counts must partition the total, and mapped units must equal the
   total before completion. A reusable-derivative gap may remain a limitation; a scientific-coverage
   gap may not.
4. Create `coverage_manifest.md` before scientific mapping. Record every disjoint source/evidence unit
   and stage assignment. Each table row contains exactly one plain relative artifact path; put every
   shard part on its own row.
5. Run fresh, distinct `qc162_main_quantitative_mapper` and `qc162_support_quantitative_mapper` agents in parallel over the
   disjoint union of reusable-backed and fresh-required units. Reconstruct every result-relevant
   numeric and statistical relationship.
6. Run numeric and cross-source review in two distinct fresh `gpt-6.1-sol`/`medium` agents. Independently spawn a new
   `gpt-6.1-sol`/`high` agent for statistical pass 1; do not reuse a mapper agent or use follow-up to
   request a reasoning-effort change. Each checker applies the inclusion threshold and the
   screened-out catalogue of `QUALITY_CONTROL_SCOPE.md` to its own observations, emits a finding ID
   (`F-NUM-001`, `F-XS-001`, `F-ST1-001`, ...) only for an observation it judges to meet the
   threshold, consolidates a repeated pattern into one finding, and lists its other observations in a
   compact `Excluded observations` table with one reason code each. Every finding records the compared
   locations, the document role of each, the proposed review domain, the affected result or extracted
   value, and why context does not resolve it. Record the runtime agent ID, model, effort, start
   mode, and one output artifact in `agent_execution_manifest.md`.
7. Run a fresh `qc162_inclusion_screener`/`high` agent over every finding from the three checkers. It
   rereads each cited source location, applies the inclusion threshold independently, consolidates
   findings that describe the same issue or pattern, and writes `screening/inclusion_screen.md` with
   one row per finding: `INCLUDE` or `SCREENED_OUT` with exactly one reason code. It never sets a
   target number and never compares with other papers.
8. Assign `C001`, `C002`, ... only to the included issues, in source order, and write
   `candidate_ledger.md`. Preserve the finding IDs, checker provenance, and every affected location.
   Assign each candidate its review domain, a provisional relationship type, and all relationships
   under `QUALITY_CONTROL_SCOPE.md`, and write the classification table required by the review
   contract. Write the candidate ID back into each `INCLUDE` row of the screening log.
9. Run a fresh `qc162_evidence_rechecker`/`high` agent over every stable ID against the exact source page or truthful Office
   location. Existing OCR/text is a locator and transcription aid, not final authority. The rechecker
   confirms or corrects each document-role assignment, relationship type, and review domain from
   content, and assigns the evidence state.
10. Spawn a different new `gpt-6.1-sol`/`high` agent for statistical pass 2 over every statistical
   relationship, the complete ledger, the screening log, and all recheck facts. Record its distinct
   runtime ID in `agent_execution_manifest.md`. It rereads every checker `Excluded observations` row
   against the route A (always-register) categories and the display-precision rule of `QUALITY_CONTROL_SCOPE.md` and
   emits a finding for any row that belongs there. If it emits new findings (`F-ST2-001`, ...), screen
   them with a different fresh `qc162_inclusion_screener`/`high` agent recorded as stage
   `inclusion_screener_pass_2`, append included issues to the ledger without renumbering, classify
   them, then recheck every appended ID.
11. Run a fresh `qc162_quality_control_auditor`/`high` agent over every stable ID, every screening
   decision, every checker `Excluded observations` table, every coverage row, the complete
   `source_coverage.md`, the classification table, and the execution manifest. Audit whether each
   candidate meets the inclusion threshold and record `CONFIRMED` or `QUESTIONED` with a reason, audit
   screening decisions in both directions, and audit every relationship type, precedence decision,
   review domain, and evidence state. A wrongly screened-out finding that meets the threshold is
   appended as a new candidate and rechecked; an assigned candidate ID is never deleted or suppressed.
12. Run a fresh `qc162_report_generator`/`medium` agent to assemble the complete Markdown report. It must contain every
    candidate in the ledger with its classification fields, an inclusion screening summary, and a
    review-domain summary. If no candidate is found after complete coverage, produce a zero-candidate
    report that states the completed scope, the screening summary, and limitations. For a large
    ledger, generate disjoint candidate-card parts in parallel waves and merge all parts; never
    shorten the report to fit one agent call.
13. Immediately after Markdown assembly, finalize `run_state.md` and copy the exact performance fields
    into the report. Recompute source and reused-artifact hashes, render HTML once, remove the
    fallback environment if one was created, finalize `tooling_record.md`, and validate:

```bash
python3 workflow_1_6_2/scripts/render_report.py \
  .ai_paper_validation/final_report_1_6_2.md \
  .ai_paper_validation/final_report_1_6_2.html \
  --profile 1.6.2
python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove
python3 workflow_1_6_2/scripts/validate_review.py --profile 1.6.2 --package .
```

Repair correctable validation failures until
`.ai_paper_validation/review_1_6_2/review_validation.json` reports `PASS`.
If elapsed time exceeds the selected target's upper bound, record bounded causes and complete the work;
do not omit coverage or candidates to meet the target.
If a repair requires another model call after `Finished UTC`, update the finish time, manifest, and
report timing fields before rendering and validation.

## Fixed scientific and communication boundaries

- Focus on counts and denominators, estimate and test logic, statistical method logic, and planned
  versus reported statistical design, as defined in `QUALITY_CONTROL_SCOPE.md`.
- Register only issues that meet the inclusion threshold. Screen out differences within the display-precision
  rule (relative discrepancy at most 0.05) and display-zero P values, notation and typographic slips, terminology and
  wording differences that a reader in the field resolves at once, model-based estimates compared with
  crude ratios, conditional observations, peripheral cross-document comparisons, and out-of-focus
  differences. A reproduced finding qualifies by route A (an always-register category of
  `QUALITY_CONTROL_SCOPE.md`, including every interval-versus-P-value or test conflict) or by route B
  (in focus, not resolved by context, and bearing on interpretation or extraction). When in doubt
  about wording, terminology, or a symbol, screen it out; when in doubt about a printed number,
  interval, P value, count, or planned-versus-reported element, register it.
- Keep cross-document and cross-location comparisons, tiered as in `QUALITY_CONTROL_SCOPE.md`: primary
  and key secondary results, misattributed results, quantity-changing labels, and planned-versus-
  reported analysis, endpoint, outcome-status, and intervention elements can qualify; copies of
  baseline descriptive values,
  per-time-point counts, pointers, sites, recruitment calendars, and other plan-internal details are
  peripheral unless they change a primary or key secondary result, an analysis-population size, or a
  planned decision rule.
- Register one candidate per issue; a repeated pattern is one candidate with all affected locations.
- There is no expected, typical, minimum, maximum, or target number of candidates.
- Do not perform a broad methodology, study-design, clinical, novelty, misconduct, or raw-data audit,
  and do not propose a preferred analysis.
- Use only supplied package evidence. Do not browse the web or use external literature.
- Never describe a candidate, a value, or the authors' work with the words error, mistake, defect,
  erroneous, wrong, or incorrect. Use candidate, reporting issue, inconsistency, discrepancy, unclear,
  or does not reconcile. Established statistical terms such as standard error keep their names.
- Assign every candidate one of the four review domains (`statistical_results`,
  `report_internal_inconsistency`, `protocol_report`, `plan_material`), consistent with its
  relationship type. These fields pre-fill human review and are not adjudications.
- Never assign `Major`, `Minor`, `Verified`, `Rejected`, `Uncertain`, severity, validity, acceptance,
  a suggested disposition, or a final correction, and never delete a candidate. Every candidate
  remains `Pending Human Adjudication`.
- Preserve 1.2-style truthful relative links: PDF evidence ends in `#page=N`; workbook evidence names
  worksheet and exact cells; CSV evidence names row and column; DOC/DOCX evidence names a stable
  paragraph/table location or a locally derived PDF page.
- The default target is a local CPU machine. Reuse existing OCR first. Use direct native/layout
  extraction for uncovered units, or the recorded fallback helper when a direct tool is missing, and
  targeted OCR only when text is unusable or visual confirmation requires it. Tell the user that
  processing runs on the CPU, and use a GPU only on the user's explicit request (see "CPU by
  default").

## Completion

Do not finish until every direct-source row has mapped units equal to total units; all coverage rows
are complete and contain one artifact path; routing preflight is `PASS`; every mandatory specialist
stage has a distinct fresh runtime agent with the required model and effort; both fresh
`gpt-6.1-sol`/`high` statistical agents cover every registered relationship; every actual agent
including the coordinator appears in the execution manifest; ledger/recheck/quality/report ID sets are
identical; every checker finding has exactly one screening decision and every included finding maps
to a candidate; every candidate has a complete classification that agrees between the ledger and the
report; `tooling_record.md` is complete and any fallback environment has been removed; every local
evidence link resolves; source and reused-artifact hashes are unchanged; standalone
HTML exists with embedded CSS and a table of contents; and the validator reports `PASS`.
