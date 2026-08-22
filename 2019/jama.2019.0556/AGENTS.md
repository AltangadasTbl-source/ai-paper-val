# Quantitative Quality-Control Review 1.4.1 — Reuse Existing Evidence Assets

The current project root is exactly one paper package. The package may contain earlier
`.ai_paper_validation/` records whose discovery stopped at, prioritized, or reported only 10
candidates. Workflow 1.4.1 starts candidate discovery again without a count limit, while reusing all
usable existing OCR, native text, layout text, table extraction, workbook extraction, rendered pages,
and document maps.

Use English only in prompts, generated artifacts, logs, and reports. Preserve every supplied source
and every pre-existing audit artifact. Write new work only to:

- `.ai_paper_validation/review_1_4_1/`
- `.ai_paper_validation/final_report_1_4_1.md`
- `.ai_paper_validation/final_report_1_4_1.html`

## Agent-first execution

Start immediately and operate autonomously. The coordinator plans coverage, delegates bounded and
disjoint evidence scopes to specialist agents, merges their durable artifacts, and verifies coverage.
Python is auxiliary only. Do not use Python to orchestrate the scientific review, select candidates,
perform ordinary PDF extraction, run OCR, or replace agent reasoning. Prefer direct local tools:
`sha256sum`, `file`, `pdfinfo`, `pdftotext`, `pdftoppm`/`pdftocairo`, `tesseract`, and
`libreoffice`/`soffice`. The only permitted Python helpers are the optional Office structure
extractor, report renderer, and final validator in `workflow_1_4_1/scripts/`.

Use artifact-first handoffs. Every specialist writes complete English output to one unique assigned
path and returns only a compact status, exact scope, counts, limitations, and artifact path. Never let
two agents write the same artifact concurrently. Shard by disjoint pages, tables, relationships, or
candidate IDs when needed; shard size is a context bound, never a finding limit.

## Read before reviewing

Read completely:

- `QUALITY_CONTROL_SCOPE.md`
- `PERFORMANCE_PROFILE.md`
- `workflow_1_4_1/review_contract.md`
- `workflow_1_4_1/report_spec.md`
- `workflow_1_4_1/settings.toml`

Do not read an old candidate set, review queue, verifier disposition, critic decision, endetail
section, or final report as a scientific input or candidate source. Preserve those records unchanged,
but rebuild discovery only from source-linked OCR, text, table, workbook, page, and document-map assets.

## Required workflow

1. Inventory every direct source and record SHA-256 in
   `.ai_paper_validation/review_1_4_1/source_hashes_before.sha256`. Before the first substantive tool
   call, record the UTC start time and 20–25 minute target fields from `PERFORMANCE_PROFILE.md` in
   `run_state.md`.
2. Use `qc14_reuse_asset_curator` to inventory and hash every reused OCR/text/table/page/document-map
   artifact in `reused_artifact_hashes_before.sha256`, assess its coverage and fitness, and write the
   source and evidence-asset inventories. Do not modify reused artifacts.
3. Create `coverage_manifest.md` before scientific extraction. Record every source/evidence unit and
   disjoint stage assignment. Coverage must include the complete result-relevant contents represented
   by the reusable assets, not just pages or tables mentioned in old candidate records.
4. Run `qc14_main_quantitative_mapper` and `qc14_support_quantitative_mapper` in parallel over disjoint
   units. Reconstruct all result-relevant numeric and statistical relationships from the reused assets.
5. Run `qc14_numeric_consistency_reviewer`, `qc14_statistical_consistency_reviewer` pass 1, and
   `qc14_cross_source_consistency_reviewer` in parallel. Each lane examines all assigned relationships
   and continues after finding candidates. There is no target, minimum, maximum, top-N rule, or review
   queue.
6. Merge only genuine duplicates before stable IDs. Assign `C001`, `C002`, ... to every distinct
   candidate and write `candidate_ledger.md`. Preserve all checker provenance and source locations.
7. Run `qc14_evidence_rechecker` over every stable ID against the exact source page or truthful Office
   location. Existing OCR/text is a locator and transcription aid, not final authority.
8. Run statistical pass 2 over every statistical relationship, the complete cross-lane ledger, and all
   recheck facts. Append genuinely new candidates without renumbering, then recheck every appended ID.
9. Run `qc14_quality_control_auditor` over every stable ID and every coverage row. Repair supportable
   omissions, but never delete or suppress an assigned candidate ID.
10. Run `qc14_report_generator` to assemble the complete Markdown report. It must contain every
    candidate in the ledger. If no candidate is found after complete coverage, produce a zero-candidate
    report that states the completed scope and limitations. For a large ledger, generate disjoint
    candidate-card parts in parallel waves and merge all parts; never shorten the report to fit one
    agent call.
11. Immediately after Markdown assembly, finalize `run_state.md`, copy the exact performance fields
    into the report, recompute source and reused-artifact hashes, render HTML once, and validate:

```bash
python3 workflow_1_4_1/scripts/render_report.py \
  .ai_paper_validation/final_report_1_4_1.md \
  .ai_paper_validation/final_report_1_4_1.html \
  --profile 1.4.1
python3 workflow_1_4_1/scripts/validate_review.py --profile 1.4.1 --package .
```

Repair correctable defects until
`.ai_paper_validation/review_1_4_1/review_validation.json` reports `PASS`.
If elapsed time exceeds 25 minutes, record bounded causes and complete the work; do not omit coverage
or candidates to meet the target.

## Fixed scientific and communication boundaries

- Prioritize numeric, denominator/proportion/total, inferential-statistical, cross-document numeric,
  effect-measure/label/scale, and rate-versus-count consistency.
- Analysis-unit, randomization-level, sample-unit, or population-definition issues are secondary and
  qualify only when they create a concrete inconsistency in a reported number, statistic, denominator,
  label, or interpretation.
- Do not perform a broad methodology, study-design, clinical, novelty, misconduct, or raw-data audit.
- Use only supplied package evidence. Do not browse the web or use external literature.
- Treat findings as quality-control candidates: small preventable reporting defects may matter because
  they can propagate into systematic reviews, meta-analyses, or other downstream evidence products.
  Do not inflate that possibility into a claim that the paper's conclusion is wrong.
- Never assign `Major`, `Minor`, `Verified`, `Rejected`, `Uncertain`, severity, validity, acceptance,
  exclusion, or a final correction. Every candidate remains `Pending Human Adjudication`.
- Preserve 1.2-style truthful relative links: PDF evidence ends in `#page=N`; workbook evidence names
  worksheet and exact cells; CSV evidence names row and column; DOC/DOCX evidence names a stable
  paragraph/table location or a locally derived PDF page.
- The Linux target is CPU-only. Reuse existing OCR first. Use targeted direct Tesseract OCR only when
  an exact location cannot otherwise be confirmed; never probe or invoke a GPU.

## Completion

Do not finish until all coverage rows are complete, both statistical passes cover every registered
statistical relationship, ledger/recheck/quality/report ID sets are identical, every local evidence
link resolves, source and reused-artifact hashes are unchanged, standalone HTML exists with embedded
CSS and a table of contents, and the validator reports `PASS`.
