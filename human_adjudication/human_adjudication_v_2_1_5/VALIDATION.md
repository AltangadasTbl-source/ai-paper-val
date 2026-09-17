# Human adjudication v.2.1.5 — Validation

Validation date: 2026-09-13. Version/revision: v.2.1.5. Schema: xlsx-adjudication-7. Environment: Python 3.12.3, openpyxl 3.1.5.

## Release checks

Four annual templates contain 45 paper sheets and 412 candidates, with annual totals 119/71/91/131. Each retains the v.2.1.4 19-column Checker layout, header order, column widths, row heights, colors, wrapping, filter range, and B2 freeze position. The two synthetic 2019 workbooks remain under examples, separate from the four templates.

Disposition dropdowns contain exactly retain, exclude, and discuss. Review-domain dropdowns use report_internal_inconsistency, explicitly defined by main paper and updated supplement. Retired codes and their old option labels are absent from cells and relevant comments across all six review workbooks. Codebook names and dropdown ranges remain consistent.

The v.2.1.4 catalog is the immediate source. Only the suggested domain is renamed on 130 candidates, in both aiInitialAssessment.domain and suggestedDomain. Deep comparison verifies all other candidate content, evidence, source references, and relationship codes remain unchanged. The new catalog records its parent signature and rename count. No human answers are imported.

## Regression tests

All 27 tests passed in 125.916 seconds. The suite covers the inherited two-stage review workflow, structural protections, saved-value validation, handoff, discussion resolution, defaults, zero and unfinished counts, and a four-year export with all 412 candidates and 45 papers. Additional checks specifically cover:

- The limited 130-candidate terminology migration and parent provenance.
- The three remaining disposition options and new domain across four templates and two examples.
- Rejection of pasted out_of_scope and internal_nonstatistical codes in primary and checker stages.
- Required internalStatus for a retained report_internal_inconsistency candidate.
- Primary snapshot, visible summary, checker inheritance, final_domain export, and secondary_temporal classification with the renamed domain.

```bash
python3 -m unittest discover -s human_adjudication/human_adjudication_v_2_1_5 -p test_v_2_1_5.py -v
```

Regression simulations are confined to temporary directories. The published 2019 example is explicitly marked SYNTHETIC TEST DATA ONLY: 71 completed primary exclude placeholders and 71 pending checker records. Both example files pass saved-value validation.

## Formula and document checks

All 3,324 formulas across the four templates and two examples passed tokenization; the longest is 2,227 characters. The Chinese TeX document compiled with two XeLaTeX passes into a two-page PDF. There are no missing characters, overfull boxes, undefined references, or fatal errors. The installed CTEX packages emit LaTeX release-date warnings.

All 31 local links across seven current-entry and v.2.1.5 Markdown documents resolve.

## Limits

Native desktop Excel/WPS/LibreOffice dropdown interaction and recalculation have not been tested. Validation reads saved answers and interprets known defaults without trusting cached formula results. The primary-to-checker transition still requires prepare-checker; the ready test sample already includes that handoff. Existing inputs are preserved. Older human-answer files are not automatically migrated to this schema.
