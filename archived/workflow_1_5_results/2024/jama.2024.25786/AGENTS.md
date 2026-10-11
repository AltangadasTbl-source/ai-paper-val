# Quantitative Quality-Control Review 1.5.3 — Reuse Existing Evidence Assets

The current project root is exactly one paper package. The package may contain earlier
`.ai_paper_validation/` records whose discovery stopped at, prioritized, or reported only 10
candidates. Workflow 1.5.3 starts candidate discovery again without a count limit, while reusing all
usable existing OCR, native text, layout text, table extraction, workbook extraction, rendered pages,
and document maps. Reuse is an optimization, not a coverage boundary: every direct-source unit that
lacks usable reusable extraction must be freshly inspected and mapped from the supplied source.

Use English only in prompts, generated artifacts, logs, and reports. Preserve every supplied source
and every pre-existing audit artifact. Write new work only to:

- `.ai_paper_validation/review_1_5_3/`
- `.ai_paper_validation/final_report_1_5_3.md`
- `.ai_paper_validation/final_report_1_5_3.html`

## Agent-first execution

Start immediately and operate autonomously. The coordinator plans coverage, delegates bounded and
disjoint evidence scopes to specialist agents, merges their durable artifacts, and verifies coverage.
Python is auxiliary only. Do not use Python to orchestrate the scientific review, select candidates,
perform ordinary PDF extraction, run OCR, or replace agent reasoning. Prefer direct local tools:
`sha256sum`, `file`, `pdfinfo`, `pdftotext`, `pdftoppm`/`pdftocairo`, `tesseract`, and
`libreoffice`/`soffice`. The only permitted Python helpers are the optional Office structure
extractor, deterministic token-cost calculator, report renderer, and final validator in
`workflow_1_5_3/scripts/`. The calculator summarizes authoritative runtime usage; it does not estimate
tokens from review text.

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
and execute Workflow 1.5.3 now.` as the first request. The user-level Codex configuration supplies the
provider and authentication; the project config fixes the coordinator at `gpt-5.6-sol`/`high` and the
nine named presets fix every specialist model/effort pair. Do not use `~openai/gpt-latest`, another
moving alias, a shell launcher, or `codex exec` fallback.

Before scientific work, create `routing_preflight.md` and require it to report `PASS`, coordinator
`gpt-5.6-sol`/`high`, ordinary specialists `gpt-5.6-terra`/`medium`, statistical specialists
`gpt-5.6-terra`/`high`, Sol specialists `gpt-5.6-sol`/`high`, `Coordinator inference: PASS`, execution
mode `INTERACTIVE_CLI`, and all nine named agent presets verified against their required pairs.

Every mandatory specialist stage uses a fresh agent and a distinct runtime ID. Use the named custom
agent preset when available. Otherwise use a fresh default agent, pass the exact fixed model and
reasoning effort for that role, and include the role contract in the spawn prompt. Never reuse an
agent for another mandatory stage, promote an agent with follow-up, omit a fallback model override, or
substitute Sol for a Terra role. Record the exact model ID in the execution manifest and token ledger.

## Read before reviewing

Read completely:

- `QUALITY_CONTROL_SCOPE.md`
- `PERFORMANCE_PROFILE.md`
- `workflow_1_5_3/review_contract.md`
- `workflow_1_5_3/report_spec.md`
- `workflow_1_5_3/settings.toml`

Do not read an old candidate set, review queue, verifier disposition, critic decision, endetail
section, or final report as a scientific input or candidate source. Preserve those records unchanged,
but rebuild discovery from source-linked reusable assets plus mandatory direct-source inspection of
every uncovered unit.

## Required workflow

1. Verify `routing_preflight.md` first. Record the UTC start time, then inventory every direct source, its complete stable unit count, and
   SHA-256 in `.ai_paper_validation/review_1_5_3/source_hashes_before.sha256`. Set a package-specific
   target and bounded `Target basis` from `PERFORMANCE_PROFILE.md`; do not infer either from SAP length
   or page count alone. Initialize every required field in `run_state.md`. Initialize
   `agent_execution_manifest.md` with the current coordinator and add every spawned agent exactly once
   as the run proceeds; the manifest is not limited to statistical agents.
2. Use a fresh `qc15_reuse_asset_curator` agent to inventory and hash every reused OCR/text/table/page/document-map
   artifact in `reused_artifact_hashes_before.sha256`, assess its coverage and fitness, and write the
   source and evidence-asset inventories. In `source_coverage.md`, record one row per direct source with
   total, reusable, fresh-required, and mapped unit counts. Do not modify reused artifacts.
3. Compare reusable coverage against every direct-source unit. Assign every uncovered page, sheet,
   record group, paragraph group, and table group to fresh direct-source extraction and mapping. The
   reusable and fresh-required unit counts must partition the total, and mapped units must equal the
   total before completion. A reusable-derivative gap may remain a limitation; a scientific-coverage
   gap may not.
4. Create `coverage_manifest.md` before scientific mapping. Record every disjoint source/evidence unit
   and stage assignment. Each table row contains exactly one plain relative artifact path; put every
   shard part on its own row.
5. Run fresh, distinct `qc15_main_quantitative_mapper` and `qc15_support_quantitative_mapper` agents in parallel over the
   disjoint union of reusable-backed and fresh-required units. Reconstruct every result-relevant
   numeric and statistical relationship.
6. Run numeric and cross-source review in two distinct fresh `gpt-5.6-terra`/`medium` agents. Independently spawn a new
   `gpt-5.6-terra`/`high` agent for statistical pass 1; do not reuse a mapper agent or use follow-up to
   request a reasoning-effort change. Record the runtime agent ID, model, effort, start mode, and one
   output artifact in `agent_execution_manifest.md`. After each completed model response, retain its
   authoritative runtime usage record for later token accounting when the runtime exposes it.
7. Merge only genuine duplicates before stable IDs. Assign `C001`, `C002`, ... to every distinct
   candidate and write `candidate_ledger.md`. Preserve all checker provenance and source locations.
8. Run a fresh `qc15_evidence_rechecker`/`high` agent over every stable ID against the exact source page or truthful Office
   location. Existing OCR/text is a locator and transcription aid, not final authority.
9. Spawn a different new `gpt-5.6-terra`/`high` agent for statistical pass 2 over every statistical
   relationship, the complete cross-lane ledger, and all recheck facts. Record its distinct runtime ID
   in `agent_execution_manifest.md`. Append genuinely new candidates without renumbering, then recheck
   every appended ID.
10. Run a fresh `qc15_quality_control_auditor`/`high` agent over every stable ID, every coverage row, the complete
   `source_coverage.md`, and the statistical execution manifest. Repair supportable
   omissions, but never delete or suppress an assigned candidate ID.
11. Run a fresh `qc15_report_generator`/`high` agent to assemble the complete Markdown report. It must contain every
    candidate in the ledger. If no candidate is found after complete coverage, produce a zero-candidate
    report that states the completed scope and limitations. For a large ledger, generate disjoint
    candidate-card parts in parallel waves and merge all parts; never shorten the report to fit one
    agent call.
12. Immediately after Markdown assembly, finalize `run_state.md`. Treat `Finished UTC` as the token-
    accounting cutoff. Write `token_usage_ledger.csv` for the coordinator and every manifested agent,
    using exact response-level runtime/API usage only. Use `TOTALS_ONLY` when exact input/output/total
    counts exist without billing details; use `UNAVAILABLE` plus exact `__` token fields when no count
    is exposed. Never approximate from text length. Run the bundled cost
    calculator, then copy the exact performance fields, token-accounting status, per-model totals,
    package total, and complete token-only price when available into the report using the bundled
    dated Sol/Terra pricing snapshot. Recompute source and reused-artifact
    hashes, render HTML once, and validate:

```bash
python3 workflow_1_5_3/scripts/calculate_token_cost.py \
  --ledger .ai_paper_validation/review_1_5_3/token_usage_ledger.csv \
  --pricing workflow_1_5_3/token_pricing.toml \
  --markdown .ai_paper_validation/review_1_5_3/token_usage_summary.md \
  --json .ai_paper_validation/review_1_5_3/token_usage_summary.json
python3 workflow_1_5_3/scripts/render_report.py \
  .ai_paper_validation/final_report_1_5_3.md \
  .ai_paper_validation/final_report_1_5_3.html \
  --profile 1.5.3
python3 workflow_1_5_3/scripts/validate_review.py --profile 1.5.3 --package .
```

Repair correctable defects until
`.ai_paper_validation/review_1_5_3/review_validation.json` reports `PASS`.
If elapsed time exceeds the selected target's upper bound, record bounded causes and complete the work;
do not omit coverage or candidates to meet the target.
If a repair requires another model call after `Finished UTC`, reopen the accounting window, update the
finish time and manifest/ledger, and rerun the token calculation before rendering and validation.

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
- Never assign `Major`, `Minor`, `Verified`, `Rejected`, `Uncertain`, severity, validity, acceptance,
  exclusion, or a final correction. Every candidate remains `Pending Human Adjudication`.
- Preserve 1.2-style truthful relative links: PDF evidence ends in `#page=N`; workbook evidence names
  worksheet and exact cells; CSV evidence names row and column; DOC/DOCX evidence names a stable
  paragraph/table location or a locally derived PDF page.
- The Linux target is CPU-only. Reuse existing OCR first. Use direct native/layout extraction for
  uncovered units and targeted Tesseract only when text is unusable or visual confirmation requires
  it; never probe or invoke a GPU.

## Completion

Do not finish until every direct-source row has mapped units equal to total units; all coverage rows
are complete and contain one artifact path; routing preflight is `PASS`; every mandatory specialist
stage has a distinct fresh runtime agent with the required model and effort; both fresh Terra/high
statistical agents cover every registered relationship; every actual agent including the coordinator appears in both the
execution manifest and token ledger; agent- and model-level token summaries are current; ledger/recheck/quality/report ID sets are identical; every local
evidence link resolves; source and reused-artifact hashes are unchanged; standalone HTML exists with
embedded CSS and a table of contents; and the validator reports `PASS`.
