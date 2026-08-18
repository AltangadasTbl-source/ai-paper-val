# Quantitative Quality-Control Review 1.4.2 — Full Source-First Restart

The current project root is exactly one paper package containing one main article and zero or more
support files. Workflow 1.4.2 restarts the entire review from supplied sources, including inventory,
text/table extraction, page rendering/OCR decisions, quantitative relationship mapping, discovery,
recheck, and reporting. Existing audit outputs may remain in the package, but they are not evidence
inputs or discovery boundaries for this run.

Use English only in prompts, generated artifacts, logs, and reports. Preserve every supplied source
and every pre-existing audit artifact. Write new work only to:

- `.ai_paper_validation/review_1_4_2/`
- `.ai_paper_validation/final_report_1_4_2.md`
- `.ai_paper_validation/final_report_1_4_2.html`

## Agent-first execution

Start immediately and operate autonomously. The coordinator plans source and stage coverage,
delegates bounded disjoint scopes to specialist agents, merges their durable artifacts, and verifies
completion. Python is auxiliary only. Do not use Python to orchestrate scientific review, choose
pages, select candidates, perform ordinary PDF extraction, or run OCR. Prefer direct local tools:
`sha256sum`, `file`, `pdfinfo`, `pdftotext`, `pdftoppm`/`pdftocairo`, `tesseract`, and
`libreoffice`/`soffice`. The only permitted Python helpers are the optional Office structure
extractor, report renderer, and final validator in `workflow_1_4_2/scripts/`.

Use artifact-first handoffs. Every specialist writes complete English output to one unique assigned
path and returns only compact status, exact scope, counts, limitations, and artifact paths. Never let
two agents write the same artifact concurrently. Shard by disjoint pages, tables, relationships, or
candidate IDs when needed; shard size is a context bound, never a finding limit.

## Read before reviewing

Read completely:

- `QUALITY_CONTROL_SCOPE.md`
- `PERFORMANCE_PROFILE.md`
- `workflow_1_4_2/review_contract.md`
- `workflow_1_4_2/report_spec.md`
- `workflow_1_4_2/settings.toml`

Ignore all old OCR, extracted text/tables, candidate sets, review queues, verifier/critic records,
endetail reports, and final reports as evidence inputs. Do not delete them. The only permissible use
of an old audit directory is to avoid writing into or overwriting it.

## Required workflow

1. Inventory every direct source and record SHA-256 in
   `.ai_paper_validation/review_1_4_2/source_hashes_before.sha256`. Before the first substantive tool
   call, record the UTC start time and 20–25 minute target fields from `PERFORMANCE_PROFILE.md` in
   `run_state.md`.
2. Use `qc14_fresh_source_preprocessor` to classify all direct sources and create a new evidence-asset
   inventory under `review_1_4_2/`. Extract PDF native text and layout text directly. Convert Office
   sources locally when possible and use the optional structure extractor only when needed. Render
   result-relevant pages and use direct CPU Tesseract only for pages whose native text is unusable.
3. Create `coverage_manifest.md` before scientific extraction. Record every source/evidence unit and
   disjoint stage assignment. The plan must cover all result-relevant main and support contents, not
   only primary outcomes, significant results, or old cited pages.
4. Run `qc14_main_quantitative_mapper` and `qc14_support_quantitative_mapper` in parallel over disjoint
   newly prepared units. Map all result-relevant numeric and statistical relationships.
5. Run `qc14_numeric_consistency_reviewer`, `qc14_statistical_consistency_reviewer` pass 1, and
   `qc14_cross_source_consistency_reviewer` in parallel. Each lane completes every assigned
   relationship. There is no target, minimum, maximum, top-N rule, or review queue.
6. Merge only genuine duplicates before stable IDs. Assign `C001`, `C002`, ... to every distinct
   candidate and write `candidate_ledger.md`, preserving all provenance and locations.
7. Run `qc14_evidence_rechecker` over every stable ID against exact source locations.
8. Run statistical pass 2 over every statistical relationship, the complete cross-lane ledger, and all
   recheck facts. Append genuinely new candidates without renumbering, then recheck every appended ID.
9. Run `qc14_quality_control_auditor` over every stable ID and coverage row. Repair supportable
   omissions, but never delete or suppress an assigned candidate ID.
10. Run `qc14_report_generator` to assemble the complete Markdown report. It must contain every ledger
    candidate. If complete coverage finds none, produce a zero-candidate report documenting coverage
    and limitations. For a large ledger, generate disjoint candidate-card parts in parallel waves and
    merge all parts; never shorten the report to fit one agent call.
11. Immediately after Markdown assembly, finalize `run_state.md`, copy the exact performance fields
    into the report, recompute source hashes, render HTML once, and validate:

```bash
python3 workflow_1_4_2/scripts/render_report.py \
  .ai_paper_validation/final_report_1_4_2.md \
  .ai_paper_validation/final_report_1_4_2.html \
  --profile 1.4.2
python3 workflow_1_4_2/scripts/validate_review.py --profile 1.4.2 --package .
```

Repair correctable defects until
`.ai_paper_validation/review_1_4_2/review_validation.json` reports `PASS`.
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

Do not finish until all coverage rows are complete, both statistical passes cover every registered
statistical relationship, ledger/recheck/quality/report ID sets are identical, every local evidence
link resolves, source hashes are unchanged, standalone HTML exists with embedded CSS and a table of
contents, and the validator reports `PASS`.
