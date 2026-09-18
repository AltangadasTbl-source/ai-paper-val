# Human adjudication v.2.1.5.2 — Validation

Validation date: 2026-09-17. Version/revision: v.2.1.5.2. Schema: xlsx-adjudication-8. Workbook generator: the existing openpyxl 3.1.5 release builder. Visual QA: Artifact Tool.

## Release checks

The four annual templates contain 45 paper sheets and 412 candidates (119/71/91/131 per year). Every Primary assessment cell in column M is blank and locked. The completed-primary synthetic example also retains blank primary-stage assessment cells. Its prepared checker counterpart displays the completed primary summaries. All six review workbooks pass saved-answer validation.

A cell-by-cell comparison against v.2.1.5.1 confirmed the initial release changes: 412 blank primary assessment cells, four Codebook guidance cells, and release metadata/version labels. A subsequent Start-page correction updates B3, B8, B12 and B16 in all six workbooks to clarify identity, blank inheritance, discussion resolution and the locked Primary assessment column. The bundled checker example's primary-file hash was refreshed to match its revised primary example. All six saved workbooks pass validation after these corrections. Every other XLSX archive part was preserved byte-for-byte during the Start-page update. Sheet order, source values, formulas, styles, sheet protection, dropdown validation, conditional formatting, filters, and freeze panes are preserved. The frozen source signature is unchanged, with v.2.1.5.1 recorded as the parent catalog. Earlier releases were not modified.

## Regression checks

All 30 regression tests pass, including the annual-template check expanded to require blank, locked Primary assessment cells on every candidate row. Coverage includes saved-answer validation, completed primary handoff, populated checker summaries, snapshot protection, default formulas, required judgments, sorting, discussion, no-overwrite behavior, and four-year export. The historical style fixture points to its current location under previous/.

```bash
python3 -m unittest discover -s human_adjudication/human_adjudication_v_2_1_5_2 -p test_v_2_1_5_2.py -v
```

## Visual checks and limits

Artifact Tool rendered the changed 2019 review range before and after the change, plus the checker example. The primary column is visibly empty with its existing layout retained; the checker summary remains legible. The imported 2019 primary and checker workbooks were recalculated in memory for these previews. No formulas changed in this release.

After the instruction correction, the full Start pages for both primary and checker stages were rendered and inspected. The four revised instruction rows fit within the existing layout.

Native desktop Excel interaction was not tested. The validator checks saved answers without depending on formula caches. The workbooks retain automatic recalculation on open.
