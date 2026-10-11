# Quantitative Quality-Control Review 1.6 — Reuse Existing Evidence Assets

The current project root is exactly one paper package. The package may contain earlier
`.ai_paper_validation/` records. Workflow 1.6 performs candidate discovery from the beginning without
a count limit, while reusing all usable existing OCR, native text, layout text, table extraction,
workbook extraction, rendered pages, and document maps. Reuse is an optimization, not a coverage
boundary: every direct-source unit that lacks usable reusable extraction must be freshly inspected and
mapped from the supplied source. Every stable candidate receives a document-role classification as
part of the review.

Use English only in prompts, generated artifacts, logs, and reports. Preserve every supplied source
and every pre-existing audit artifact. Write new work only to:

- `.ai_paper_validation/review_1_6/`
- `.ai_paper_validation/final_report_1_6.md`
- `.ai_paper_validation/final_report_1_6.html`

## Agent-first execution

Start immediately and operate autonomously. The coordinator plans coverage, delegates bounded and
disjoint evidence scopes to specialist agents, merges their durable artifacts, and verifies coverage.
Python is auxiliary only. Do not use Python to orchestrate the scientific review, select or classify
candidates, or replace agent reasoning. Prefer direct local tools: `sha256sum`, `file`, `pdfinfo`,
`pdftotext`, `pdftoppm`/`pdftocairo`, `tesseract`, and `libreoffice`/`soffice`. The only permitted
Python helpers are those in `workflow_1_6/scripts/`: the optional Office structure extractor, the
tooling bootstrap and PDF/OCR/hash fallback helper described below, the report renderer, and the final
validator. Do not write other Python for extraction or OCR.

## Local tools and the temporary fallback environment

The review runs on a local machine (Linux, macOS, or Windows) where direct tools may be missing.
Before source inventory, probe the machine and record the result in
`.ai_paper_validation/review_1_6/tooling_record.md`:

```bash
python3 workflow_1_6/scripts/pdf_tools.py probe
```

If PDF information, text, or page rendering is unavailable as a direct tool, create the temporary
package-local fallback environment; add `--ocr` only when OCR may be needed and `tesseract` is absent:

```bash
python3 workflow_1_6/scripts/bootstrap_tooling.py create
```

The environment is created only under `.ai_paper_validation/review_1_6/tooling/`, with pinned
packages and a local package cache; never install into the global Python environment. Then use the
fallback helper with that environment's interpreter, and only for capabilities the probe recorded as
missing:

```bash
.ai_paper_validation/review_1_6/tooling/venv/bin/python workflow_1_6/scripts/pdf_tools.py info "source.pdf"
.ai_paper_validation/review_1_6/tooling/venv/bin/python workflow_1_6/scripts/pdf_tools.py text "source.pdf" --first N --last N ".ai_paper_validation/review_1_6/preprocessing/native-N.txt"
.ai_paper_validation/review_1_6/tooling/venv/bin/python workflow_1_6/scripts/pdf_tools.py text "source.pdf" --first N --last N ".ai_paper_validation/review_1_6/preprocessing/layout-N.txt" --layout
.ai_paper_validation/review_1_6/tooling/venv/bin/python workflow_1_6/scripts/pdf_tools.py render "source.pdf" --page N ".ai_paper_validation/review_1_6/preprocessing/page-N.png"
.ai_paper_validation/review_1_6/tooling/venv/bin/python workflow_1_6/scripts/pdf_tools.py ocr ".ai_paper_validation/review_1_6/preprocessing/page-N.png" ".ai_paper_validation/review_1_6/preprocessing/ocr-N.txt"
python3 workflow_1_6/scripts/pdf_tools.py sha256 "source.pdf"
```

On Windows the interpreter is `.ai_paper_validation\review_1_6\tooling\venv\Scripts\python.exe`.
Every specialist uses the tooling recorded in `tooling_record.md`. Record the engine with every
derivative it produces. If installation fails, for example because the sandbox blocks network access,
record `INSTALL_FAILED`, continue with reusable assets and the tools that are available, inspect
rendered or reusable page images visually where text is unusable, and list every affected unit as a
limitation. A missing tool never permits omitting a source unit. After rendering HTML and before the
final validation, remove the environment with `python3 workflow_1_6/scripts/bootstrap_tooling.py
remove` and record the removal.

Use artifact-first handoffs. Every specialist writes complete English output to one unique assigned
path and returns only a compact status, exact scope, counts, limitations, and artifact path. Never let
two agents write the same artifact concurrently. Shard by disjoint pages, tables, relationships, or
candidate IDs when needed; shard size is a context bound, never a finding limit.

Do not put provider credentials or provider selection in the package-root `.codex/config.toml`.
The direct interactive session requires the nine bundled `.codex/agents/` role presets and verifies
each one before scientific work. Preserve unrelated package `.codex` controls when copying those
files. Validation does not rewrite `.codex/`.

## Fixed model routing contract

Start from the package root with `codex --approve-for-me`, then send `Read START_PROMPT.md completely
and execute Workflow 1.6 now.` as the first request. The user-level Codex configuration supplies the
provider and authentication; the project config fixes the coordinator at `gpt-6.1-sol`/`high` and the
nine named presets fix every specialist model/effort pair. Every role uses `gpt-6.1-sol`; roles differ
only in reasoning effort. Do not use `~openai/gpt-latest`, another moving alias, a shell launcher, or
`codex exec` fallback.

Before scientific work, create `routing_preflight.md` and require it to report `PASS`, coordinator
`gpt-6.1-sol`/`high`, ordinary specialists `gpt-6.1-sol`/`medium`, statistical specialists
`gpt-6.1-sol`/`high`, recheck and audit specialists `gpt-6.1-sol`/`high`, `Coordinator inference:
PASS`, execution mode `INTERACTIVE_CLI`, and all nine named agent presets verified against their
required pairs.

Every mandatory specialist stage uses a fresh agent and a distinct runtime ID. Use the named custom
agent preset when available. Otherwise use a fresh default agent, pass the exact fixed model and
reasoning effort for that role, and include the role contract in the spawn prompt. Never reuse an
agent for another mandatory stage, promote an agent with follow-up, omit a fallback model override, or
change the fixed reasoning effort of a role. Record the exact model ID in the execution manifest.

## Read before reviewing

Read completely:

- `QUALITY_CONTROL_SCOPE.md`
- `PERFORMANCE_PROFILE.md`
- `workflow_1_6/review_contract.md`
- `workflow_1_6/report_spec.md`
- `workflow_1_6/settings.toml`

Do not read an old candidate set, review queue, verifier disposition, critic decision, endetail
section, classification record, or final report as a scientific input or candidate source. Preserve
those records unchanged, but build discovery and classification from source-linked reusable assets
plus mandatory direct-source inspection of every uncovered unit.

## Required workflow

1. Verify `routing_preflight.md` first. Probe local tools, create the fallback environment if needed,
   and write `tooling_record.md`. Record the UTC start time, then inventory every direct source, its complete stable unit count, and
   SHA-256 in `.ai_paper_validation/review_1_6/source_hashes_before.sha256`. Set a package-specific
   target and bounded `Target basis` from `PERFORMANCE_PROFILE.md`; do not infer either from SAP length
   or page count alone. Initialize every required field in `run_state.md`. Initialize
   `agent_execution_manifest.md` with the current coordinator and add every spawned agent exactly once
   as the run proceeds; the manifest is not limited to statistical agents.
2. Use a fresh `qc16_reuse_asset_curator` agent to inventory and hash every reused OCR/text/table/page/document-map
   artifact in `reused_artifact_hashes_before.sha256`, assess its coverage and fitness, and write the
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
5. Run fresh, distinct `qc16_main_quantitative_mapper` and `qc16_support_quantitative_mapper` agents in parallel over the
   disjoint union of reusable-backed and fresh-required units. Reconstruct every result-relevant
   numeric and statistical relationship.
6. Run numeric and cross-source review in two distinct fresh `gpt-6.1-sol`/`medium` agents. Independently spawn a new
   `gpt-6.1-sol`/`high` agent for statistical pass 1; do not reuse a mapper agent or use follow-up to
   request a reasoning-effort change. Every checker records, for each candidate it emits, the compared
   locations and the document role of each. Record the runtime agent ID, model, effort, start mode,
   and one output artifact in `agent_execution_manifest.md`.
7. Merge only genuine duplicates before stable IDs. Assign `C001`, `C002`, ... to every distinct
   candidate and write `candidate_ledger.md`. Preserve all checker provenance and source locations.
   Assign each candidate its primary category, a provisional relationship type, all relationships, and
   the derived review domain under `QUALITY_CONTROL_SCOPE.md`, and write the classification table
   required by the review contract.
8. Run a fresh `qc16_evidence_rechecker`/`high` agent over every stable ID against the exact source page or truthful Office
   location. Existing OCR/text is a locator and transcription aid, not final authority. The rechecker
   confirms or corrects each document-role assignment and relationship type from content, and assigns
   the evidence state.
9. Spawn a different new `gpt-6.1-sol`/`high` agent for statistical pass 2 over every statistical
   relationship, the complete cross-lane ledger, and all recheck facts. Record its distinct runtime ID
   in `agent_execution_manifest.md`. Append genuinely new candidates without renumbering, classify
   them, then recheck every appended ID.
10. Run a fresh `qc16_quality_control_auditor`/`high` agent over every stable ID, every coverage row, the complete
   `source_coverage.md`, the classification table, and the statistical execution manifest. Audit every
   relationship type, precedence decision, derived review domain, evidence state, and suggested review
   disposition. Repair supportable omissions, but never delete or suppress an assigned candidate ID.
11. Run a fresh `qc16_report_generator`/`medium` agent to assemble the complete Markdown report. It must contain every
    candidate in the ledger with its classification fields and a document-role classification
    summary. If no candidate is found after complete coverage, produce a zero-candidate report that
    states the completed scope and limitations. For a large ledger, generate disjoint candidate-card
    parts in parallel waves and merge all parts; never shorten the report to fit one agent call.
12. Immediately after Markdown assembly, finalize `run_state.md` and copy the exact performance fields
    into the report. Recompute source and reused-artifact hashes, render HTML once, remove the
    fallback environment if one was created, finalize `tooling_record.md`, and validate:

```bash
python3 workflow_1_6/scripts/render_report.py \
  .ai_paper_validation/final_report_1_6.md \
  .ai_paper_validation/final_report_1_6.html \
  --profile 1.6
python3 workflow_1_6/scripts/bootstrap_tooling.py remove
python3 workflow_1_6/scripts/validate_review.py --profile 1.6 --package .
```

Repair correctable defects until
`.ai_paper_validation/review_1_6/review_validation.json` reports `PASS`.
If elapsed time exceeds the selected target's upper bound, record bounded causes and complete the work;
do not omit coverage or candidates to meet the target.
If a repair requires another model call after `Finished UTC`, update the finish time, manifest, and
report timing fields before rendering and validation.

## Fixed scientific and communication boundaries

- Prioritize numeric, denominator/proportion/total, inferential-statistical, cross-document numeric,
  effect-measure/label/scale, and rate-versus-count consistency.
- Analysis-unit, randomization-level, sample-unit, or population-definition issues are secondary and
  qualify only when they create a concrete inconsistency in a reported number, statistic, denominator,
  label, or interpretation.
- Do not perform a broad methodology, study-design, clinical, novelty, misconduct, or raw-data audit.
- Use only supplied package evidence. Do not browse the web or use external literature.
- Never register a candidate solely because a very small P value is displayed as `P = 0`, `p = 0.000`,
  or equivalent. Treat coherent display zero as finite-precision shorthand and record
  `DISPLAY_ZERO_NOT_CANDIDATE`. Require an independent supplied-source contradiction before assigning
  a `C` ID, and frame the candidate around that contradiction.
- Treat findings as quality-control candidates: small preventable reporting defects may matter because
  they can propagate into systematic reviews, meta-analyses, or other downstream evidence products.
  Do not inflate that possibility into a claim that the paper's conclusion is wrong.
- Classify every candidate's document roles and relationship type by content under
  `QUALITY_CONTROL_SCOPE.md`. The review domain and suggested review disposition are derived
  mechanically from the classification and evidence state; they pre-fill human review and are not
  adjudications.
- Never assign `Major`, `Minor`, `Verified`, `Rejected`, `Uncertain`, severity, validity, acceptance,
  or a final correction, and never delete a candidate. Every candidate remains `Pending Human
  Adjudication`.
- Preserve 1.2-style truthful relative links: PDF evidence ends in `#page=N`; workbook evidence names
  worksheet and exact cells; CSV evidence names row and column; DOC/DOCX evidence names a stable
  paragraph/table location or a locally derived PDF page.
- The target is a local CPU-only machine. Reuse existing OCR first. Use direct native/layout
  extraction for uncovered units, or the recorded fallback helper when a direct tool is missing, and
  targeted OCR only when text is unusable or visual confirmation requires it; never probe or invoke a
  GPU.

## Completion

Do not finish until every direct-source row has mapped units equal to total units; all coverage rows
are complete and contain one artifact path; routing preflight is `PASS`; every mandatory specialist
stage has a distinct fresh runtime agent with the required model and effort; both fresh
`gpt-6.1-sol`/`high` statistical agents cover every registered relationship; every actual agent
including the coordinator appears in the execution manifest; ledger/recheck/quality/report ID sets are
identical; every candidate has a complete classification that agrees between the ledger and the
report; `tooling_record.md` is complete and any fallback environment has been removed; every local
evidence link resolves; source and reused-artifact hashes are unchanged; standalone
HTML exists with embedded CSS and a table of contents; and the validator reports `PASS`.
