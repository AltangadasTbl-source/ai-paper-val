# Workflow 1.6.2 Review Contract

## Purpose

Perform a complete quantitative quality-control review from existing local evidence assets, register
only the reporting issues that meet the inclusion threshold of `QUALITY_CONTROL_SCOPE.md`, and assign
every candidate one of the four review domains. Reuse eligible OCR, native text, layout text,
table/workbook extraction, rendered pages, manifests, and document maps to avoid unnecessary
preprocessing, but do not reuse old candidate selection as the scope of discovery.

This profile is not a legacy-candidate recovery pass. It re-examines all result-relevant evidence
across every supplied source unit and rebuilds the quantitative relationship inventory and candidate
ledger from the beginning, screens every finding, then classifies every stable candidate. Reusable assets accelerate covered
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

Old checker, candidate, queue, screening, verifier, critic, endetail, quality, and report records are
preserved but not read as scientific inputs or candidate sources in workflow 1.6.2.

Derived evidence is a locator and transcription aid. Confirm every candidate against an exact source
page, workbook cell/range, CSV row/column, or DOC/DOCX paragraph/table location. Record OCR/source
disagreements; never silently normalize them. An inconsistency that exists only between a derivative
and the source is a transcription matter, not a reporting issue.

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
pdftotext -f N -l N "source.pdf" ".ai_paper_validation/review_1_6_2/preprocessing/native-N.txt"
pdftotext -layout -f N -l N "source.pdf" ".ai_paper_validation/review_1_6_2/preprocessing/layout-N.txt"
pdftoppm -f N -l N -singlefile -png "source.pdf" ".ai_paper_validation/review_1_6_2/preprocessing/page-N"
tesseract ".ai_paper_validation/review_1_6_2/preprocessing/page-N.png" ".ai_paper_validation/review_1_6_2/preprocessing/ocr-N" -l eng --psm 6
libreoffice --headless --convert-to pdf --outdir ".ai_paper_validation/review_1_6_2/preprocessing/converted_pdf" "support.docx"
python3 workflow_1_6_2/scripts/extract_office_source.py "support.xlsx" ".ai_paper_validation/review_1_6_2/preprocessing/office_structure/support"
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
- **Compute device:** CPU, or GPU_USER_REQUESTED when the user explicitly asked for GPU OCR
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

## Findings and checker self-screening

Every checker processes its full assigned scope. There is no minimum, maximum, desired, or typical
count, no top-N selection, no review queue, and no early stopping. The coordinator may shard large
scopes, but the union of shards must be complete and disjoint.

Each checker applies the inclusion threshold and the screened-out catalogue of
`QUALITY_CONTROL_SCOPE.md` to every observation in its scope:

- An observation that the checker judges to meet the threshold becomes a finding with an ID of the
  form `F-NUM-001` (numeric checker), `F-XS-001` (cross-source checker), `F-ST1-001` (statistical pass
  1), or `F-ST2-001` (statistical pass 2), written as a `### F-...` heading.
- A repeated pattern (same rule, same evident cause) is one finding that lists every affected location.
- Every other observation is listed once in a compact `Excluded observations` table with columns
  `Location | Observation | Reason code`, using the reason codes of `QUALITY_CONTROL_SCOPE.md`. Do not
  give excluded observations finding IDs. List only apparent issues that the checker decided not to
  emit; checks that reconcile belong in the relationship records, not in this table.
- A reproduced observation in a route A (always-register) category of `QUALITY_CONTROL_SCOPE.md` is
  always a finding.

Each finding records:

- exact source locations, with the document role (`REPORT` or `PLAN`) of each;
- the printed values or statements compared;
- the arithmetic, statistical, or logical rule applied and the reproduced calculation;
- the focus area (A, B, C, or D) and the proposed review domain;
- **Qualifying route:** `Route A, category N` (N = 1 to 5) or `Route B`;
- **Affected result or extracted value:** the specific result whose interpretation, or the value whose
  extraction, could change;
- **Why context does not resolve it:** why a statistically literate reader in the field could not
  identify the intended value or meaning at once from the immediate context (for route A, state the
  category instead);
- source-grounded alternative interpretations and any missing definition.

## Required checks

Apply every relevant source-grounded check within focus areas A to D:

1. counts and denominators: participant flow, randomized, treated, analyzed and followed-up totals,
   event counts, numerator/denominator pairs, row/column and subgroup totals, and the same count in
   different locations;
2. point-estimate containment, interval endpoint order, and direction agreement across estimate,
   interval, labels, narrative, and figure;
3. compatibility of estimate, interval, P value, test statistic, and standard error when the supplied
   source establishes the test, sidedness, model, confidence level, and adjustment; an interval that
   excludes the null while the P value or test is nonsignificant at the stated level, or the reverse,
   needs only the stated confidence and significance levels (conventionally 95% and .05 when the
   paper states no other) and is always a finding;
4. superiority, noninferiority, equivalence, multiplicity, interim, and stopping conclusions against
   the stated rule and margin;
5. statistical method logic: missing or contradicted steps, analysis descriptions too unclear to tell
   which analysis produced a reported number, and methods inconsistent with the stated design or data
   structure, including sample size reproduction from the stated inputs;
6. matched-result agreement across abstract, narrative, tables, figures, supplement, and structured
   files after population, time point, contrast, and model matching;
7. effect-measure identity (OR, RR, RD, HR, mean difference, rate) when a label conflicts with how the
   displayed values were evidently computed;
8. planned versus reported statistical design elements, and inconsistencies of those elements inside
   plan material.

Apply the cross-document comparison tiers of `QUALITY_CONTROL_SCOPE.md` to checks 1, 6, and 8: a
peripheral comparison is listed as an excluded observation with reason code `PERIPHERAL_COMPARISON`
unless it changes a primary or key secondary result, the size of an analysis population, or a planned
decision rule.

Before emitting a finding, apply interval arithmetic for display precision: allow each displayed input
its half-unit rounding interval, and allow the printed number its own. Screen the observation out under `ROUNDING_OR_DISPLAY_PRECISION`
when any combination of values within those intervals satisfies the rule, or when the remaining
discrepancy divided by the absolute printed value (or the reference copy) is at most 0.05. A relative
discrepancy above 0.05, or any discrepancy when the printed value is zero, is never rounding. Record the recomputed interval and the
relative discrepancy in the finding. An interval that excludes the null while the P value or test is
nonsignificant at the stated level, or the reverse, is always a finding. Compare a model-based
estimate with a crude recomputation only when the source states that the estimate is crude or
unadjusted. Do not infer unreported model details. Diagnostic approximations must be labelled as
diagnostics and must not replace the reported analysis. A very small P value displayed as `P = 0`,
`P = .000`, or equivalent is screened out; a finding about that result must rest on an independent
contradiction and be framed around it.

## Inclusion screen

A fresh `qc162_inclusion_screener`/`high` agent reads every finding from the numeric, cross-source,
and statistical pass 1 checkers, rereads each cited source location, and applies the inclusion
threshold independently of the checker's judgment. It merges findings that describe the same issue or
the same pattern, keeping every location, and decides each finding on the criteria alone, without a
target number and without reference to other papers or earlier runs. Findings from statistical pass 2
are screened the same way by a different fresh screener recorded as stage `inclusion_screener_pass_2`.

`screening/inclusion_screen.md` contains exactly one screening table with this header and one row per
finding:

```markdown
| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-001 | cross_source_consistency_reviewer | initial | SCREENED_OUT | TERMINOLOGY_OR_WORDING | — |
| F-ST1-002 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |
```

Rules:

- `Source checker` is `numeric_consistency_reviewer`, `cross_source_consistency_reviewer`,
  `statistics_pass_1`, `statistics_pass_2`, or `quality_control_auditor`.
- `Screening stage` is `initial`, `pass_2`, or `audit`.
- `INCLUDE` rows use reason code `MEETS_THRESHOLD` and name the candidate ID. Several findings may
  share one candidate ID.
- `SCREENED_OUT` rows use exactly one screened-out reason code from `QUALITY_CONTROL_SCOPE.md`.
  `DUPLICATE_OF_INCLUDED` names the candidate ID it duplicates; every other screened-out row uses `—`.
- Below the table, give a one-sentence justification for every `INCLUDE` and every screened-out row
  whose reason is not self-evident from its code.

The quality-control auditor may change a screening decision only by appending an audit row
(`Screening stage` `audit`) for that finding; a finding that the auditor itself raises uses the
source checker `quality_control_auditor` and an ID of the form `F-QA-001`.

## Two statistical passes

Spawn a new configured `gpt-6.1-sol` statistical agent for pass 1 with reasoning effort `high`. If
the configured role is unavailable, use a fresh default agent and explicitly pass
`gpt-6.1-sol`/`high`. After the full
cross-lane candidate ledger, the screening log, and the mechanical recheck exist, spawn a different new agent under the same
model/effort contract for pass 2. Never repurpose an existing agent through follow-up and never use a
follow-up request as evidence of a fresh, distinct pass-2 spawn. Pass 2 revisits every `S` relationship for
count, denominator, estimate and test logic, method logic, cross-source, and recheck implications,
applies the same self-screening as the other checkers, and does not re-emit an observation that the
screening log already records. It rereads every checker `Excluded observations` row against the
route A (always-register) categories and the display-precision rule of `QUALITY_CONTROL_SCOPE.md` and emits a
finding for every row that belongs there. Every relationship receives an explicit `PASS_1_COMPLETE` and
`PASS_2_COMPLETE` record, including relationships that yield no finding or cannot be mechanically
reconciled because a named definition is absent.

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
| inclusion_screener | RUNTIME-ID-SCREEN | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | RUNTIME-ID-RECHECK | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | RUNTIME-ID-2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| inclusion_screener_pass_2 | RUNTIME-ID-SCREEN-2 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| quality_control_auditor | RUNTIME-ID-AUDIT | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | RUNTIME-ID-REPORT | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
```

The `inclusion_screener_pass_2` row is required only when statistical pass 2 emits findings; its
artifact holds its working notes, and its decisions are appended to the single table in
`screening/inclusion_screen.md`. Replace every placeholder runtime ID. All mandatory specialist rows must have different IDs, and each
must be a fresh spawn. Optional shard or repair agents also receive one row, use a new ID, retain the
model/effort class of the role they extend or repair, and may not replace a mandatory stage row. If one agent has several artifacts,
list its primary durable artifact here and list all artifacts separately in `coverage_manifest.md`.

## Mechanical recheck

For every `C` ID, record separately:

- cited location found, for every affected location;
- source printed value/text matched;
- comparator printed value/text matched;
- consistency rule applicable;
- calculation or logical comparison reproduced, including the display-precision interval check;
- necessary inputs available, with missing inputs named;
- source-grounded alternative interpretation;
- direct observation separated from inferred explanation;
- exact remaining human question;
- document role of every compared location, confirmed by content (`REPORT` or `PLAN`);
- relationship type, all relationships, and review domain, confirmed or corrected with the reason for
  any correction;
- evidence state (`reproduced`, `reproduced_after_transcription_correction`, or `not_reproduced`) with
  the recheck fact that determines it.

These facts are not an AI disposition. A `no`, a missing definition, or a `not_reproduced` evidence
state never authorizes deletion of an assigned ID.

## Document-role classification and review domain

Classify every stable candidate under `QUALITY_CONTROL_SCOPE.md`. Checkers record the compared
locations, the document role of each location, and a proposed review domain for every finding. At
registration the coordinator assigns the review domain, a provisional relationship type, and all
relationships. The evidence rechecker confirms or corrects them from content and assigns the evidence
state. The quality-control auditor audits every classification, precedence decision, and the inclusion
threshold. The final values are written back to the ledger by the coordinator before report generation.

`candidate_ledger.md` contains exactly one classification table with this header and one row per
stable ID, in stable-ID order:

```markdown
| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main article Table 2 vs REPORT main article Figure 2 | reproduced | CONFIRMED | F-NUM-001, F-ST1-002 |
```

Rules:

- `Review domain` is exactly one of `statistical_results`, `report_internal_inconsistency`,
  `protocol_report`, `plan_material`, and agrees with the relationship type: `P_R` →
  `protocol_report`, `P_P` → `plan_material`, `S_C`/`S_W` → `statistical_results` or
  `report_internal_inconsistency`.
- `Relationship type` is exactly one of `P_R`, `P_P`, `S_C`, `S_W`.
- `All relationships` lists one or more of those codes separated by `, `, includes the relationship
  type, and the relationship type is the highest-precedence code listed (`P_R` > `P_P` > `S_C` > `S_W`).
- `Evidence state` is exactly one of `reproduced`, `reproduced_after_transcription_correction`,
  `not_reproduced`.
- `Inclusion audit` is `CONFIRMED` or `QUESTIONED`, as recorded by the quality-control auditor.
- `Finding IDs` lists every finding with an `INCLUDE` decision for that candidate in the screening log.
- Each report card repeats the same values in its classification fields.

Do not add an `OTHER` type or domain. If a role assignment is uncertain, choose the best-supported type
by content, apply precedence, and state the uncertainty in `Classification ambiguity`.

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
`inclusion_screening`, `candidate_registration`, `evidence_recheck`, `statistics_pass_2`, `evidence_quality`, and
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
