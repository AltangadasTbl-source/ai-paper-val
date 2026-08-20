# Workflow 1.4.2 Review Contract

## Purpose

Perform a complete source-first quantitative quality-control review. Rebuild the source inventory,
text/layout/table evidence, quantitative relationship inventories, candidate ledger, recheck, quality
audit, and reports. Existing audit derivatives and decisions are outside the evidence chain for this
run and must neither constrain nor shortcut discovery.

## Fresh evidence preparation

For every direct source, assign a stable document ID, record the exact filename, type, size, SHA-256,
role, page/sheet/paragraph/table availability, extraction method, and result-relevant scope.

Prepare evidence in this order:

1. PDF metadata and native text with direct `pdfinfo` and `pdftotext` calls;
2. layout-preserving text with `pdftotext -layout` for tables and aligned result displays;
3. local Office conversion with `libreoffice`/`soffice` when available;
4. optional standard-library Office structure extraction only when conversion or direct reading is
   insufficient and exact paragraph/table/cell identity is needed;
5. rendering of result-relevant pages with `pdftoppm` or `pdftocairo` for visual tables/figures;
6. direct CPU `tesseract` only for pages whose relevant evidence has unusable native/layout text.

Write all new derivatives below `.ai_paper_validation/review_1_4_2/preprocessing/`. Never modify a
source, silently change OCR engines, invoke a GPU, install software, browse the web, or read old audit
derivatives as evidence. If a tool is absent, record the affected exact units and continue all
unblocked work.

## Direct tooling pattern

Use exact quoted paths and selected pages. Typical commands are:

```bash
sha256sum -- "source.pdf"
pdfinfo "source.pdf"
pdftotext "source.pdf" ".ai_paper_validation/review_1_4_2/preprocessing/native_text/source.txt"
pdftotext -layout "source.pdf" ".ai_paper_validation/review_1_4_2/preprocessing/layout_text/source.txt"
pdftoppm -f N -l N -singlefile -png "source.pdf" ".ai_paper_validation/review_1_4_2/preprocessing/rendered_pages/source-N"
tesseract ".ai_paper_validation/review_1_4_2/preprocessing/rendered_pages/source-N.png" ".ai_paper_validation/review_1_4_2/preprocessing/ocr_text/source-N" -l eng --psm 6
libreoffice --headless --convert-to pdf --outdir ".ai_paper_validation/review_1_4_2/preprocessing/converted_pdf" "support.docx"
python3 workflow_1_4_2/scripts/extract_office_source.py "support.xlsx" ".ai_paper_validation/review_1_4_2/preprocessing/office_structure/support"
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
`S002`, ... for inferential-statistical relationships. Cross-reference overlapping evidence rather
than duplicating it.

## Complete discovery with no count target

Every checker processes its complete assigned scope and emits every distinct qualifying candidate.
There is no minimum, maximum, desired count, top-N selection, review queue, or early stopping after a
round number. The coordinator may shard large scopes, but shard union must be complete and disjoint.

Merge before stable candidate IDs only when records concern the same printed values or statements,
the same comparator, and the same consistency rule. Retain all locations and provenance. Similar
topics, shared causes, neighboring rows, or repeated consequences are not enough to merge. After
stable IDs are assigned, never delete, renumber, or merge them.

## Required checks

Apply every relevant source-grounded check:

1. arithmetic, row/column totals, subgroup sums, displayed differences, and rounding tolerance;
2. numerator, denominator, proportion, percentage, total, missingness, and analysis-population identity;
3. point-estimate containment and interval endpoint ordering;
4. sign/direction agreement across estimate, interval, labels, narrative, figure, and event direction;
5. interval/P-value/test/SE/statistic compatibility only when supplied definitions establish compatible
   tests, sidedness, model, variance, confidence level, and adjustment rules;
6. matched-result agreement across abstract, narrative, tables, figures, captions, supplement, and
   structured files after population/time/contrast/model/precision matching;
7. effect-measure, scale, unit, reference-group, transform, and direction labels;
8. rate, risk, proportion, percentage, frequency, person-time, and count distinctions;
9. repeated or duplicated values/rows where different results are expected;
10. analysis-unit or population statements only when they concretely conflict with a displayed
    number, statistic, denominator, label, or interpretation.

Do not infer unreported model details. Diagnostic approximations must be labelled and must not replace
the reported analysis.

## Two statistical passes

Pass 1 covers every `S` relationship independently. Pass 2 occurs after the full cross-lane candidate
ledger and mechanical recheck exist. It revisits every `S` relationship for denominator, arithmetic,
label, scale, duplicate-value, cross-source, and recheck implications. Every relationship receives
explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records, including relationships yielding no
candidate or lacking a named definition needed for mechanical reconciliation.

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

Hash every direct source before preprocessing and recompute all hashes before completion. Never modify
a source or old audit artifact. Never inspect sibling packages or the web. Record missing tools and
evidence as limitations while completing all unaffected scopes.
