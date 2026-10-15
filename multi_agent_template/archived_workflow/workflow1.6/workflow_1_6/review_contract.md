# Workflow 1.6 Review Contract

## Purpose

Perform a complete quantitative quality-control review from existing local evidence assets, and
classify every stable candidate by document role. There is no candidate-count boundary. Reuse eligible OCR, native text, layout text, table/workbook
extraction, rendered pages, manifests, and document maps to avoid unnecessary preprocessing, but do
not reuse old candidate selection as the scope of discovery.

This profile is not a legacy-candidate recovery pass. It re-examines all result-relevant evidence
across every supplied source unit and rebuilds the quantitative relationship inventory and candidate
ledger from the beginning, then classifies every stable candidate. Reusable assets accelerate covered
units; they never authorize omission of uncovered source units. Old classification records are not
read as inputs.

## Evidence precedence and reuse

Use evidence in this order:

1. direct source files and stable document identity;
2. reusable page/sheet/paragraph/table maps and extraction metadata;
3. reusable native or layout text;
4. reusable OCR and rendered pages;
5. reusable table/workbook extraction;
6. fresh direct-source extraction and mapping for every unit not covered by a usable reusable asset.

Old checker, candidate, queue, verifier, critic, endetail, quality, and report records are preserved
but not read as scientific inputs or candidate sources in workflow 1.6.

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
pdftotext -f N -l N "source.pdf" ".ai_paper_validation/review_1_6/preprocessing/native-N.txt"
pdftotext -layout -f N -l N "source.pdf" ".ai_paper_validation/review_1_6/preprocessing/layout-N.txt"
pdftoppm -f N -l N -singlefile -png "source.pdf" ".ai_paper_validation/review_1_6/preprocessing/page-N"
tesseract ".ai_paper_validation/review_1_6/preprocessing/page-N.png" ".ai_paper_validation/review_1_6/preprocessing/ocr-N" -l eng --psm 6
libreoffice --headless --convert-to pdf --outdir ".ai_paper_validation/review_1_6/preprocessing/converted_pdf" "support.docx"
python3 workflow_1_6/scripts/extract_office_source.py "support.xlsx" ".ai_paper_validation/review_1_6/preprocessing/office_structure/support"
```

Run the first seven tools directly when the tool probe recorded them as available. For each missing
capability, use the equivalent `pdf_tools.py` command with the temporary fallback environment, as
described in `AGENTS.md`, and store its derivatives in the same `preprocessing/` locations. Use the
Python Office helper only when exact local structure is otherwise unavailable.

`tooling_record.md` contains these exact fields:

```markdown
- **Probe UTC:** YYYY-MM-DDTHH:MM:SSZ
- **Platform:** linux, darwin, or win32 as reported by the probe
- **Direct tools available:** pdfinfo=yes|no; pdftotext=yes|no; pdftoppm=yes|no; pdftocairo=yes|no; tesseract=yes|no; libreoffice=yes|no; pandoc=yes|no
- **Fallback environment:** NOT_NEEDED, CREATED, or INSTALL_FAILED
- **Fallback packages:** exact installed versions from bootstrap_log.json, or None
- **Fallback capabilities used:** info, text, layout, render, ocr, sha256, or None
- **Fallback environment removed:** YES or NOT_CREATED
- **Tooling limitations:** None, or the affected source units and how they were covered
``` Store commands, tool versions, source locations, and outputs in the evidence
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

Spawn a new configured `gpt-6.1-sol` statistical agent for pass 1 with reasoning effort `high`. If
the configured role is unavailable, use a fresh default agent and explicitly pass
`gpt-6.1-sol`/`high`. After the full
cross-lane candidate ledger and mechanical recheck exist, spawn a different new agent under the same
model/effort contract for pass 2. Never repurpose an existing agent through follow-up and never use a
follow-up request as evidence of a fresh, distinct pass-2 spawn. Pass 2 revisits every `S` relationship for
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
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | RUNTIME-ID-CURATOR | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | RUNTIME-ID-MAIN-MAPPER | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | RUNTIME-ID-SUPPORT-MAPPER | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | RUNTIME-ID-NUMERIC | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | RUNTIME-ID-CROSS-SOURCE | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | RUNTIME-ID-1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | RUNTIME-ID-RECHECK | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | RUNTIME-ID-2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | RUNTIME-ID-AUDIT | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | RUNTIME-ID-REPORT | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
```

Replace every placeholder runtime ID. All mandatory specialist rows must have different IDs, and each
must be a fresh spawn. Optional shard or repair agents also receive one row, use a new ID, retain the
model/effort class of the role they extend or repair, and may not replace a mandatory stage row. If one agent has several artifacts,
list its primary durable artifact here and list all artifacts separately in `coverage_manifest.md`.

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
- exact remaining human question;
- document role of every compared location, confirmed by content (`REPORT` or `PLAN`);
- relationship type and all relationships, confirmed or corrected with the reason for any correction;
- evidence state (`recorded_candidate`, `not_reproduced`, `repaired_residual`, or
  `record_input_error`) with the recheck fact that determines it.

These facts are not an AI disposition. A `no`, a missing definition, or a `not_reproduced` evidence
state never authorizes deletion.

## Document-role classification

Classify every stable candidate under the document-role section of `QUALITY_CONTROL_SCOPE.md`.
Checkers record the compared locations and the document role of each location for every candidate
they emit. At registration the coordinator assigns the primary category, a provisional relationship
type, all relationships, and the derived review domain. The evidence rechecker confirms or corrects
document roles and relationship types from content and assigns the evidence state. The quality-control
auditor audits every classification, precedence decision, and derived field. The final values are
written back to the ledger by the coordinator before report generation.

`candidate_ledger.md` contains exactly one classification table with this header and one row per
stable ID, in stable-ID order:

```markdown
| ID | Primary category | Relationship type | All relationships | Compared document roles | Review domain | Evidence state | Suggested review disposition |
|---|---|---|---|---|---|---|---|
| C001 | Statistical reporting inconsistency | S_W | S_W | REPORT main article Table 2 vs REPORT main article abstract | statistical_results | recorded_candidate | retain |
```

Rules:

- `Relationship type` is exactly one of `P_R`, `P_P`, `S_C`, `S_W`.
- `All relationships` lists one or more of those codes separated by `, `, includes the relationship
  type, and the relationship type is the highest-precedence code listed (`P_R` > `P_P` > `S_C` > `S_W`).
- `Review domain` equals the mechanical derivation from relationship type and primary category.
- `Evidence state` is exactly one of `recorded_candidate`, `not_reproduced`, `repaired_residual`,
  `record_input_error`.
- `Suggested review disposition` equals the mechanical derivation from the evidence state.
- Each report card repeats the same values in its classification fields.

Do not add an `OTHER` type. If a role assignment is uncertain, choose the best-supported type by
content, apply precedence, and state the uncertainty in `Classification ambiguity`.

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
