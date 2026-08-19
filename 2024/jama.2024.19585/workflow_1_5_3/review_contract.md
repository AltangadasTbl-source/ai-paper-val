# Workflow 1.5.3 Review Contract

## Purpose

Perform a new, complete quantitative quality-control review from existing local evidence assets. The
old 10-candidate boundary is void. Reuse eligible OCR, native text, layout text, table/workbook
extraction, rendered pages, manifests, and document maps to avoid unnecessary preprocessing, but do
not reuse old candidate selection as the scope of discovery.

This profile is not a legacy-candidate recovery pass. It re-examines all result-relevant evidence
across every supplied source unit and rebuilds the quantitative relationship inventory and candidate
ledger from the beginning. Reusable assets accelerate covered units; they never authorize omission of
uncovered source units.

## Evidence precedence and reuse

Use evidence in this order:

1. direct source files and stable document identity;
2. reusable page/sheet/paragraph/table maps and extraction metadata;
3. reusable native or layout text;
4. reusable OCR and rendered pages;
5. reusable table/workbook extraction;
6. fresh direct-source extraction and mapping for every unit not covered by a usable reusable asset.

Old checker, candidate, queue, verifier, critic, endetail, quality, and report records are preserved
but not read as scientific inputs or candidate sources in workflow 1.5.3.

Derived evidence is a locator and transcription aid. Confirm every candidate against an exact source
page, workbook cell/range, CSV row/column, or DOC/DOCX paragraph/table location. Record OCR/source
disagreements; never silently normalize them.

The asset curator must identify which source locations each reused artifact covers, its method, and
whether it is `USABLE`, `PARTIAL`, `STALE`, `DUPLICATE`, or `UNREADABLE`. Partial assets create explicit
fresh-source assignments; they do not permit sampling or an unresolved scientific-coverage gap.

## Complete source-coverage ledger

Write exactly one data row per direct source in `source_coverage.md`:

```markdown
| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | main.pdf | PDF_PAGE | 12 | 10 | 2 | 12 | COMPLETE |
```

Use a package-relative plain path and a stable unit type. Count unique source units, not overlapping
derivative files. For every row, reusable units plus fresh-required units must equal total units,
mapped units must equal total units, and status must be `COMPLETE`. If a reusable derivative is absent,
stale, partial, or unreadable for a unit, count that unit as fresh-required and map it directly.
`source_coverage.md` may describe the derivative gap as a limitation only after the direct-source
mapping closes the scientific gap.

## Direct tooling pattern

Use exact quoted paths and selected pages. Typical commands are:

```bash
sha256sum -- "source.pdf"
pdfinfo "source.pdf"
pdftotext -f N -l N "source.pdf" ".ai_paper_validation/review_1_5_3/preprocessing/native-N.txt"
pdftotext -layout -f N -l N "source.pdf" ".ai_paper_validation/review_1_5_3/preprocessing/layout-N.txt"
pdftoppm -f N -l N -singlefile -png "source.pdf" ".ai_paper_validation/review_1_5_3/preprocessing/page-N"
tesseract ".ai_paper_validation/review_1_5_3/preprocessing/page-N.png" ".ai_paper_validation/review_1_5_3/preprocessing/ocr-N" -l eng --psm 6
libreoffice --headless --convert-to pdf --outdir ".ai_paper_validation/review_1_5_3/preprocessing/converted_pdf" "support.docx"
python3 workflow_1_5_3/scripts/extract_office_source.py "support.xlsx" ".ai_paper_validation/review_1_5_3/preprocessing/office_structure/support"
```

Run the first seven tools directly. Use the Python Office helper only when exact local structure is
otherwise unavailable. Store commands, tool versions, source locations, and outputs in the evidence
asset inventory. Never pass unresolved globs as source scope.

## Quantitative relationship inventory

Before checking, map all result-relevant relationships, including:

- every displayed count, total, numerator, denominator, percentage, rate, person-time quantity, mean,
  median, dispersion value, change, difference, and unit;
- every effect estimate, interval, P value, test statistic, standard error, model/adjustment label,
  population, time point, contrast, reference group, scale, and direction;
- matching occurrences in abstract, narrative, tables, figures, captions, footnotes, supplement, and
  provided structured data;
- every label or definition needed to distinguish OR/RR/RD/HR, mean difference, standardized measure,
  rate, risk, proportion, and count;
- analysis-unit, randomization-level, sample-unit, or population definitions only when they affect a
  reported quantitative relationship.

Assign stable relationship IDs `N001`, `N002`, ... for numeric/reporting relationships and `S001`,
`S002`, ... for inferential-statistical relationships. A relationship may have both identifiers only
when separate tracking is genuinely useful; cross-reference rather than duplicate its evidence.

## Complete discovery with no count target

Every checker processes its full assigned scope and emits every distinct qualifying candidate. There
is no minimum, maximum, desired count, top-N selection, review queue, or early stopping after a round
number. The coordinator may shard large scopes, but the union of shards must be complete and disjoint.

Merge before stable candidate IDs only when records concern the same printed values or statements,
the same comparator, and the same consistency rule. Retain all source locations and checker
provenance. Similar topics, shared causes, neighboring rows, or repeated consequences are not enough
to merge. After IDs are assigned, never delete, renumber, or merge them.

## Required checks

Apply every relevant source-grounded check:

1. arithmetic, row/column totals, subgroup sums, displayed differences, and rounding tolerance;
2. numerator, denominator, proportion, percentage, total, missingness, and analysis-population identity;
3. point-estimate containment and interval endpoint ordering;
4. sign/direction agreement across estimate, interval, labels, narrative, figure, and event direction;
5. interval/P-value/test/SE/statistic compatibility only when the supplied source establishes compatible
   tests, sidedness, model, variance, confidence level, and adjustment rules;
6. matched-result agreement across abstract, narrative, tables, figures, captions, supplement, and
   structured files after population/time/contrast/model/precision matching;
7. effect-measure, scale, unit, reference-group, transform, and direction labels;
8. rate, risk, proportion, percentage, frequency, person-time, and count distinctions;
9. repeated or duplicated values/rows where different results are expected;
10. analysis-unit or population statements only when they concretely conflict with a displayed
    number, statistic, denominator, label, or interpretation.

Do not infer unreported model details. Diagnostic approximations must be labelled as diagnostics and
must not replace the reported analysis.

### P-value display-zero exclusion

Treat `P = 0`, `p = 0.000`, and equivalent finite-precision display zeros as non-candidates when the
remaining supplied result is coherent. Do not emit a candidate for literal-zero formatting, numeric
underflow, export precision, or the mathematical observation that a tail probability is positive.
Mark the checked relationship `DISPLAY_ZERO_NOT_CANDIDATE` when a durable coverage record is useful.

If the package contains a separate contradiction involving that result, register only the independent
contradiction. Preserve its exact comparator and location. A candidate card that mentions a display
zero must include `**Independent contradiction beyond P=0 display:**` followed by the independent
source-grounded mismatch. If no such mismatch exists, do not assign a `C` ID.

## Two statistical passes

Spawn a new configured statistical agent for pass 1 with reasoning effort `high`. If the configured
role is unavailable, use a fresh default agent, omit the model override so the launcher-enforced
`~openai/gpt-latest` default applies, and set reasoning effort `high` explicitly. After the full
cross-lane candidate ledger and mechanical recheck exist, spawn a different new agent under the same
model/effort contract for pass 2. Never repurpose a medium agent through follow-up and never use a
follow-up request as evidence of changed reasoning effort. Pass 2 revisits every `S` relationship for
denominator, arithmetic, label, scale, duplicate-value, cross-source, and recheck implications. Every
relationship receives an explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` record, including
relationships that yield no candidate or cannot be mechanically reconciled because a named definition
is absent.

Record every runtime agent used by the paper-package review in `agent_execution_manifest.md`, not
only the statistical agents. Use one row per agent ID and one primary artifact path. Include the
current coordinator exactly once:

```markdown
| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | ~openai/gpt-latest | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | RUNTIME-ID-CURATOR | ~openai/gpt-latest | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | RUNTIME-ID-MAIN-MAPPER | ~openai/gpt-latest | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | RUNTIME-ID-SUPPORT-MAPPER | ~openai/gpt-latest | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | RUNTIME-ID-NUMERIC | ~openai/gpt-latest | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | RUNTIME-ID-CROSS-SOURCE | ~openai/gpt-latest | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | RUNTIME-ID-1 | ~openai/gpt-latest | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | RUNTIME-ID-RECHECK | ~openai/gpt-latest | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | RUNTIME-ID-2 | ~openai/gpt-latest | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | RUNTIME-ID-AUDIT | ~openai/gpt-latest | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | RUNTIME-ID-REPORT | ~openai/gpt-latest | medium | FRESH_SPAWN | limitations.md |
```

Replace every placeholder runtime ID. All mandatory specialist rows must have different IDs, and each
must be a fresh spawn. Optional shard or repair agents also receive one row, use a new ID, inherit the
same requested route, and may not replace a mandatory stage row. If one agent has several artifacts,
list its primary durable artifact here and list all artifacts separately in `coverage_manifest.md`.

## Token usage and price calculation

Account for model usage from `Started UTC` through `Finished UTC`, including the coordinator and every
agent in `agent_execution_manifest.md`. After the complete Markdown report is assembled and all model
work inside that accounting window is finished, write request-level authoritative runtime/API usage
to `token_usage_ledger.csv` with this exact CSV header:

```text
record_id,agent_id,role,model,service_tier,context_class,price_multiplier,input_tokens,cached_input_tokens,cache_write_tokens,output_tokens,reasoning_tokens,total_tokens,usage_source,status
```

Use one `EXACT` row per response-level usage record. `record_id` and `usage_source` must be unique.
Use the exact manifest `Stage` value as `role`, and keep each agent's model identical to the manifest.
For this OpenRouter profile, that manifest model is the configured route `~openai/gpt-latest`; do not
replace it with a built-in Codex model slug. If the runtime separately exposes a resolved upstream
model, preserve that value in `usage_source` so a dated exact-model price can be configured later.
Copy token counts from runtime or API usage metadata; do not infer them from characters, words, local
tokenizers, context limits, or transcript length. Normalize `PRIORITY` service tier to `FAST`. Set
`context_class` to `LONG` only when that request has more than 272,000 input tokens, otherwise use
`SHORT`. Use `price_multiplier=1` unless a known regional or other token-price multiplier applies.

`cached_input_tokens` and `cache_write_tokens` are subsets of `input_tokens`, while
`reasoning_tokens` is a subset of `output_tokens`. Therefore:

```text
uncached_input = input_tokens - cached_input_tokens - cache_write_tokens
total_tokens = input_tokens + output_tokens
```

Never add cached, cache-write, or reasoning tokens to `total_tokens` a second time. If authoritative
input, output, and total counts exist but cached/cache-write/reasoning details do not, use
`TOTALS_ONLY`: keep exact integers in `input_tokens`, `output_tokens`, and `total_tokens`; put `__` in
the three detail fields and price-classification fields. The package token count remains usable, but
the complete price remains blank. If authoritative usage for any response or agent is unavailable,
add an `UNAVAILABLE` row for that agent, put exact
`__` in every token field, explain the unavailable runtime source in `usage_source`, and do not invent
an estimate. The complete package count and price then remain explicitly incomplete, although known
subtotals are retained.

Run `calculate_token_cost.py` with the bundled `token_pricing.toml`. It deterministically writes
`token_usage_summary.md` and `token_usage_summary.json`, with separate rollups by agent and by model,
then a package total. The bundled snapshot intentionally has no price for the dynamic route, so exact
usage receives `INCOMPLETE_PRICE_UNAVAILABLE` and the complete USD amount remains `__`. Add rates only
for an exact resolved model and a verified date; never apply a stale fixed-model price to
`~openai/gpt-latest`. Non-token tools, containers, storage, subscriptions, taxes, and other vendor
charges remain outside the calculation. A later model repair reopens the accounting window: update
the finish time, append its exact usage and agent row, and rerun the calculation before validation.

## Mechanical recheck

For every `C` ID, record separately:

- cited location found;
- source printed value/text matched;
- comparator printed value/text matched;
- consistency rule applicable;
- calculation or logical comparison reproduced;
- necessary inputs available, with missing inputs named;
- source-grounded alternative interpretation;
- direct observation separated from inferred explanation;
- exact remaining human question.

These facts are not an AI disposition. A `no` or missing definition never authorizes deletion.

## Coverage manifest

Use this table in `coverage_manifest.md`:

```markdown
| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| main_evidence_mapping | main-001 | DOC001 PDF pp. 1-12 | extraction/main_quantitative_evidence.md | COMPLETE |
```

The `Artifact` cell must contain exactly one undecorated POSIX-style relative path. Do not place two
paths, prose, Markdown links, commas, or semicolon-separated values in one row. When a stage has
multiple artifacts, add one uniquely identified row per artifact.

Required stages are `source_inventory`, `evidence_assets`, `main_evidence_mapping`,
`support_evidence_mapping`, `numeric_checks`, `statistics_pass_1`, `cross_source_checks`,
`candidate_registration`, `evidence_recheck`, `statistics_pass_2`, `evidence_quality`, and
`report_generation`. Use `COMPLETE` for a documented no-applicable-unit scope; do not omit the stage.
For every candidate-stage row, `Exact scope` must enumerate each assigned `C` ID; do not use an ID
range as shorthand. The union for each of `candidate_registration`, `evidence_recheck`,
`evidence_quality`, and `report_generation` must equal the full ledger ID set. Likewise, each
statistical-pass scope must enumerate its assigned `S` IDs and cover the full statistical inventory.

## Integrity and boundaries

Hash every direct source and every reused artifact before scientific work. Recompute both sets before
completion. Never modify a source or reused artifact. Never inspect sibling packages or the web.
Record missing tools and evidence as limitations while completing all unaffected scopes. The validator
uses versioned workflow controls and run artifacts; it must neither require nor write package-root
`.codex` files.
