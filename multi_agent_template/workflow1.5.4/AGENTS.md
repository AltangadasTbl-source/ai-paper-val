# Quantitative Quality-Control Review 1.5.4 — Full Source-First Restart

The current project root is exactly one paper package containing one main article and zero or more
support files. Workflow 1.5.4 restarts the entire review from supplied sources, including inventory,
text/table extraction, page rendering/OCR decisions, quantitative relationship mapping, discovery,
recheck, and reporting. Existing audit outputs may remain in the package, but they are not evidence
inputs or discovery boundaries for this run.

Use English only in prompts, generated artifacts, logs, and reports. Preserve every supplied source
and every pre-existing audit artifact. Write new work only to:

- `.ai_paper_validation/review_1_5_4/`
- `.ai_paper_validation/final_report_1_5_4.md`
- `.ai_paper_validation/final_report_1_5_4.html`

## Agent-first execution

Start immediately and operate autonomously. The coordinator plans source and stage coverage,
delegates bounded disjoint scopes to specialist agents, merges their durable artifacts, and verifies
completion. Python is auxiliary only. Do not use Python to orchestrate scientific review, choose
pages, select candidates, perform ordinary PDF extraction, or run OCR. Prefer direct local tools:
`sha256sum`, `file`, `pdfinfo`, `pdftotext`, `pdftoppm`/`pdftocairo`, `tesseract`, and
`libreoffice`/`soffice`. The only permitted Python helpers are the optional Office structure
extractor, deterministic token-cost calculator, report renderer, and final validator in
`workflow_1_5_4/scripts/`. The calculator summarizes authoritative runtime usage; it does not estimate
tokens from review text.

Use artifact-first handoffs. Every specialist writes complete English output to one unique assigned
path and returns only compact status, exact scope, counts, limitations, and one artifact path. Never let
two agents write the same artifact concurrently. Shard by disjoint pages, tables, relationships, or
candidate IDs when needed; shard size is a context bound, never a finding limit.

Do not create, rewrite, or require a writable package-root `.codex/` directory during validation.
The bundled `.codex` files are optional runtime presets. When a named preset is unavailable, spawn a
fresh default agent with the full role contract and explicit reasoning effort, but omit the spawn-model
override so the launcher-enforced `agents.default_subagent_model` remains authoritative.

## OpenRouter routing contract

Start only through `workflow_1_5_4/scripts/launch_openrouter.sh`. Before scientific work, require the
launcher-created `routing_preflight.md` to report `PASS`, provider `openrouter`, coordinator/default
subagent model `~openai/gpt-latest`, and all nine named agent presets verified against their required
model/effort pairs. The launcher uses CLI overrides because they take precedence over
project and user configuration; a nested package `.codex/config.toml` is not sufficient enforcement.

Every mandatory specialist stage uses a fresh agent and a distinct runtime ID. Use the named custom
agent preset when available. Otherwise use a fresh default agent, inherit the launcher-enforced model,
set the required reasoning effort explicitly, and include the role contract in the spawn prompt. Never
reuse an agent for another mandatory stage, promote an agent with follow-up, or pass a different model
in a spawn call. Record the requested route `~openai/gpt-latest` in the execution manifest and token
ledger, and preserve any separately exposed resolved upstream model in authoritative usage metadata.

## Read before reviewing

Read completely:

- `QUALITY_CONTROL_SCOPE.md`
- `PERFORMANCE_PROFILE.md`
- `workflow_1_5_4/review_contract.md`
- `workflow_1_5_4/report_spec.md`
- `workflow_1_5_4/settings.toml`

Ignore all old OCR, extracted text/tables, candidate sets, review queues, verifier/critic records,
endetail reports, and final reports as evidence inputs. Do not delete them. The only permissible use
of an old audit directory is to avoid writing into or overwriting it.

## Required workflow

1. Verify `routing_preflight.md` first. Record the UTC start time, then inventory every direct source, its complete stable unit count, and
   SHA-256 in `.ai_paper_validation/review_1_5_4/source_hashes_before.sha256`. Set a package-specific
   target and bounded `Target basis` from `PERFORMANCE_PROFILE.md`; do not infer either from SAP length
   or page count alone. Initialize every required field in `run_state.md`. Initialize
   `agent_execution_manifest.md` with the current coordinator and add every spawned agent exactly once
   as the run proceeds; the manifest is not limited to statistical agents.
2. Use a fresh `qc15_fresh_source_preprocessor` agent to classify all direct sources and create a new evidence-asset
   inventory under `review_1_5_4/`. Extract PDF native text and layout text directly. Convert Office
   sources locally when possible and use the optional structure extractor only when needed. Render
   result-relevant pages and use direct CPU Tesseract only for pages whose native text is unusable.
   In `source_coverage.md`, record one row per direct source with total units, zero reusable units,
   fresh-required units equal to total units, mapped units, and status.
3. Create `coverage_manifest.md` before scientific extraction. Record every source/evidence unit and
   disjoint stage assignment. The plan must cover all result-relevant main and support contents, not
   only primary outcomes, significant results, or old cited pages. Each row contains exactly one plain
   relative artifact path; put every shard part on its own row.
4. Run fresh, distinct `qc15_main_quantitative_mapper` and `qc15_support_quantitative_mapper` agents in parallel over disjoint
   newly prepared units. Map all result-relevant numeric and statistical relationships.
5. Run numeric and cross-source review in two distinct fresh `~openai/gpt-latest`/`medium` agents. Independently spawn a new
   `~openai/gpt-latest`/`high` agent for statistical pass 1; do not reuse a mapper agent or use follow-up to
   request a reasoning-effort change. Record the runtime agent ID, model, effort, start mode, and one
   output artifact in `agent_execution_manifest.md`. After each completed model response, retain its
   authoritative runtime usage record for later token accounting when the runtime exposes it. Each lane completes every assigned relationship.
   There is no target, minimum, maximum, top-N rule, or review queue.
6. Merge only genuine duplicates before stable IDs. Assign `C001`, `C002`, ... to every distinct
   candidate and write `candidate_ledger.md`, preserving all provenance and locations.
7. Run a fresh `qc15_evidence_rechecker`/`high` agent over every stable ID against exact source locations.
8. Spawn a different new `~openai/gpt-latest`/`high` agent for statistical pass 2 over every statistical
   relationship, the complete cross-lane ledger, and all recheck facts. Record its distinct runtime ID
   in `agent_execution_manifest.md`. Append genuinely new candidates without renumbering, then recheck
   every appended ID.
9. Run a fresh `qc15_quality_control_auditor`/`high` agent over every stable ID, coverage row, source-coverage row, and the
   statistical execution manifest. Repair supportable
   omissions, but never delete or suppress an assigned candidate ID.
10. Run a fresh `qc15_report_generator`/`medium` agent to assemble the complete Markdown report. It must contain every ledger
    candidate. If complete coverage finds none, produce a zero-candidate report documenting coverage
    and limitations. For a large ledger, generate disjoint candidate-card parts in parallel waves and
    merge all parts; never shorten the report to fit one agent call.
11. Immediately after Markdown assembly, finalize `run_state.md`. Treat `Finished UTC` as the token-
    accounting cutoff. Write `token_usage_ledger.csv` for the coordinator and every manifested agent,
    using exact response-level runtime/API usage only. Use `TOTALS_ONLY` when exact input/output/total
    counts exist without billing details; use `UNAVAILABLE` plus exact `__` token fields when no count
    is exposed. Never approximate from text length. Run the bundled cost
    calculator, then copy the exact performance fields, token-accounting status, per-model totals,
    package total, and complete token-only price when available into the report. Dynamic routing is
    unpriced by default; leave the complete price blank unless dated rates for the exact resolved
    model are deliberately configured. Recompute source hashes, render HTML
    once, and validate:

```bash
python3 workflow_1_5_4/scripts/calculate_token_cost.py \
  --ledger .ai_paper_validation/review_1_5_4/token_usage_ledger.csv \
  --pricing workflow_1_5_4/token_pricing.toml \
  --markdown .ai_paper_validation/review_1_5_4/token_usage_summary.md \
  --json .ai_paper_validation/review_1_5_4/token_usage_summary.json
python3 workflow_1_5_4/scripts/render_report.py \
  .ai_paper_validation/final_report_1_5_4.md \
  .ai_paper_validation/final_report_1_5_4.html \
  --profile 1.5.4
python3 workflow_1_5_4/scripts/validate_review.py --profile 1.5.4 --package .
```

Repair correctable defects until
`.ai_paper_validation/review_1_5_4/review_validation.json` reports `PASS`.
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
- Treat findings as quality-control candidates. Explain that small preventable reporting defects can
  enter systematic reviews, meta-analyses, or later evidence products, but do not claim propagation or
  conclusion change without supplied-package evidence.
- Never assign `Major`, `Minor`, `Verified`, `Rejected`, `Uncertain`, severity, validity, acceptance,
  exclusion, or a final correction. Every candidate remains `Pending Human Adjudication`.
- Preserve 1.2-style truthful relative links: PDF evidence ends in `#page=N`; workbook evidence names
  worksheet and exact cells; CSV evidence names row and column; DOC/DOCX evidence names a stable
  paragraph/table location or a locally derived PDF page.
- The Linux target is CPU-only. Use native text first and targeted direct Tesseract OCR only when
  needed; never probe or invoke a GPU.

## Completion

Do not finish until every direct-source row has mapped units equal to total units; all coverage rows
are complete and contain one artifact path; routing preflight is `PASS`; every mandatory specialist
stage has a distinct fresh runtime agent with the required model and effort; both fresh OpenRouter/high
statistical agents cover every registered relationship; every actual agent including the coordinator appears in both the
execution manifest and token ledger; agent- and model-level token summaries are current;
ledger/recheck/quality/report ID sets are identical; every local
evidence link resolves; source hashes are unchanged; standalone HTML exists with embedded CSS and a
table of contents; and the validator reports `PASS`.
