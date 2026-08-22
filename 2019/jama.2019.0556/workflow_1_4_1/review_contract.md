# Workflow 1.4.1 Review Contract

## Purpose

Perform a new, complete quantitative quality-control review from existing local evidence assets. The
old 10-candidate boundary is void. Reuse eligible OCR, native text, layout text, table/workbook
extraction, rendered pages, manifests, and document maps to avoid unnecessary preprocessing, but do
not reuse old candidate selection as the scope of discovery.

This profile is not a legacy-candidate recovery pass. It re-examines all result-relevant evidence
represented by the reusable assets and rebuilds the quantitative relationship inventory and candidate
ledger from the beginning.

## Evidence precedence and reuse

Use evidence in this order:

1. direct source files and stable document identity;
2. reusable page/sheet/paragraph/table maps and extraction metadata;
3. reusable native or layout text;
4. reusable OCR and rendered pages;
5. reusable table/workbook extraction;
6. targeted new extraction only for a location that is missing or unusable.

Old checker, candidate, queue, verifier, critic, endetail, quality, and report records are preserved
but not read as scientific inputs or candidate sources in workflow 1.4.1.

Derived evidence is a locator and transcription aid. Confirm every candidate against an exact source
page, workbook cell/range, CSV row/column, or DOC/DOCX paragraph/table location. Record OCR/source
disagreements; never silently normalize them.

The asset curator must identify which source locations each reused artifact covers, its method, and
whether it is `USABLE`, `PARTIAL`, `STALE`, `DUPLICATE`, or `UNREADABLE`. Partial assets create explicit
coverage gaps; they do not permit sampling.

## Direct tooling pattern

Use exact quoted paths and selected pages. Typical commands are:

```bash
sha256sum -- "source.pdf"
pdfinfo "source.pdf"
pdftotext -f N -l N "source.pdf" ".ai_paper_validation/review_1_4_1/preprocessing/native-N.txt"
pdftotext -layout -f N -l N "source.pdf" ".ai_paper_validation/review_1_4_1/preprocessing/layout-N.txt"
pdftoppm -f N -l N -singlefile -png "source.pdf" ".ai_paper_validation/review_1_4_1/preprocessing/page-N"
tesseract ".ai_paper_validation/review_1_4_1/preprocessing/page-N.png" ".ai_paper_validation/review_1_4_1/preprocessing/ocr-N" -l eng --psm 6
libreoffice --headless --convert-to pdf --outdir ".ai_paper_validation/review_1_4_1/preprocessing/converted_pdf" "support.docx"
python3 workflow_1_4_1/scripts/extract_office_source.py "support.xlsx" ".ai_paper_validation/review_1_4_1/preprocessing/office_structure/support"
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

## Two statistical passes

Pass 1 covers every `S` relationship independently. Pass 2 occurs after the full cross-lane candidate
ledger and mechanical recheck exist. It revisits every `S` relationship for denominator, arithmetic,
label, scale, duplicate-value, cross-source, and recheck implications. Every relationship receives an
explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` record, including relationships that yield no
candidate or cannot be mechanically reconciled because a named definition is absent.

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
Record missing tools and evidence as limitations while completing all unaffected scopes.
