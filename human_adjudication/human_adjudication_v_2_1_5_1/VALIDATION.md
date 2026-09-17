# Human adjudication v.2.1.5.1 — Validation

Validation date: 2026-09-17. Version/revision: v.2.1.5.1. Schema: xlsx-adjudication-8. Workbook generator: openpyxl 3.1.5. Formula and visual QA: Artifact Tool.

## Release checks

The four annual templates contain 45 paper sheets and 412 candidates (119/71/91/131 per year). Two separate synthetic 2019 examples contain 71 completed primary placeholders and 71 pending checker records. All six review workbooks pass saved-answer validation.

Every review sheet has 18 columns: statistical/numerical issue in H, report-internal/planning-material inconsistency in K, Primary assessment in M, checker/discussion fields N–Q, and Notes in R. The primary summary remains locked; Notes is editable. No Related cluster field remains in human-review records or exports. Field widths follow their content when moved. Two long labels receive wider columns and the review header is 60 points high. Other widths, data-row heights, colors, wrapping, filters, and B2 freezing preserve the previous layout conventions.

Codebook fields, options, explanations, examples, and review-header comments contain no error terminology. Both relevant dropdowns include minor_presentation and non_inconsistency and omit wording_only. Statistical verdicts use confirmed_issue, probable_issue, not_issue, and indeterminate. Defined option ranges match the Codebook exactly.

Deep source comparison confirms the v.2.1.5 catalog is unchanged apart from release/provenance metadata: all 412 candidates, evidence, AI suggestions, source references, and relationship codes are preserved, with the same source signature. No human answers were imported. The existing v.2.1.5 workbooks, including the locally edited 2019 file, were not changed by this release.

## Regression checks

All 30 regression checks pass. The initial run passed 29 checks; its remaining layout comparison encountered Excel-normalized color metadata in the user's edited v.2.1.5 reference. That test now uses the unchanged v.2.1.4 baseline styles (also used by v.2.1.5), and the targeted rerun passes. No workbook change was needed for that fixture correction.

Coverage includes both review stages, key-based inheritance after row sorting, protected snapshots, required fields, clearing optional values, discussion resolution, invalid/retired pasted codes, defaults, primary/checker identity, no-overwrite behavior, partial counts, and four-year export with all 412 decisions and 45 papers. New checks exercise issue verdicts and the two wording classifications through primary completion, handoff, checker inheritance, notes amendments, final export, and temporal/descriptive outcomes.

```bash
python3 -m unittest discover -s human_adjudication/human_adjudication_v_2_1_5_1 -p test_v_2_1_5_1.py -v
```

## Formula and visual checks

Artifact Tool recalculated all six delivered review workbooks in memory and found no Excel formula failures. In each annual template, a retained statistical candidate remains CHECK FIELDS until both required judgments are supplied. A later domain change flags stale answers, then requests the newly required judgment. The new non_inconsistency code completes the planning-material branch correctly.

In the checker example, the relocated N/O columns correctly drive agreement and comment-needed prompts. All QA mutations were confined to disposable in-memory workbooks and did not alter delivered files. All 3,324 saved-workbook formulas pass tokenization and contain no broken references. All 23 local Markdown links in the release and current entry point resolve.

Rendered review headers, primary summaries, and the revised Codebook sections were visually inspected before and after the changes. The new labels and option explanations are legible with wrapping and sufficient row height.

## Limits

Native desktop Excel dropdown interaction and recalculation were not tested. The delivered files retain automatic recalculation on open. The validator reads saved answers and interprets known defaults without relying on formula caches. Earlier human-answer workbooks require a separately reviewed migration to this schema; wording_only cannot be converted without assessing its meaning.
