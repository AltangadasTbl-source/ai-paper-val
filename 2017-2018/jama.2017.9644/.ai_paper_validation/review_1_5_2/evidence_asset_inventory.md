# Fresh Evidence Asset Inventory

Prepared from the three direct PDFs only. No legacy audit derivative was used. All paths below are package-relative.

## Tooling and commands

- `pdfinfo` 26.01.0; `pdftotext` 26.01.0; `pdftoppm` 26.01.0; `tesseract` 5.5.0 with leptonica 1.86.0.
- Metadata command: `pdfinfo "SOURCE.pdf"` for each direct PDF.
- Native extraction command: `pdftotext "SOURCE.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-ID.txt"`.
- Layout extraction command: `pdftotext -layout "SOURCE.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-ID.txt"`; each page was also freshly extracted with `-f PAGE -l PAGE -layout` to the corresponding `DOC-ID-pPAGE.txt` file.
- Render command, only for pages carrying results, result displays, or quantitative definitions: `pdftoppm -f PAGE -l PAGE -singlefile -r 180 -png "SOURCE.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-ID-pPAGE"`.
- OCR decision: no CPU Tesseract call. The relevant native and layout text were legible and the selected page renders visually confirmed tables/figures. No GPU was probed or used.

## Source-level assets

| Source ID | Direct source | Role | PDF metadata | Fresh text assets | Result-relevant renders | OCR | Limitation |
|---|---|---|---|---|---|---|---|
| DOC-001 | jama_lapergue_2017_oi_170084.pdf | Main randomized-trial article | PDF 1.4; 10 letter pages; 357554 bytes; unencrypted | `preprocessing/native_text/DOC-001.txt`; `preprocessing/layout_text/DOC-001.txt`; page layout files `DOC-001-p1.txt` through `DOC-001-p10.txt` | pp. 1, 4, 5, 6, 7, 8 | None required | Native text has ordinary PDF reading-order artifacts; layout text and renders preserve table/figure checking context. |
| DOC-002 | joi170084supp1_prod.pdf | Trial protocol/support document | PDF 1.5; 14 A4 pages; 697461 bytes; unencrypted, tagged | `preprocessing/native_text/DOC-002.txt`; `preprocessing/layout_text/DOC-002.txt`; page layout files `DOC-002-p1.txt` through `DOC-002-p14.txt` | pp. 3, 4, 5, 6, 7 | None required | This protocol contains planned methods/definitions rather than outcome-result tables; page line numbers are retained in text. |
| DOC-003 | joi170084supp2_prod.pdf | Statistical-analysis supplement, eTable, and eFigures | PDF 1.5; 6 A4 pages; 169285 bytes; unencrypted, tagged | `preprocessing/native_text/DOC-003.txt`; `preprocessing/layout_text/DOC-003.txt`; page layout files `DOC-003-p1.txt` through `DOC-003-p6.txt` | pp. 2, 4, 5, 6 | None required | Small figure labels require rendered-page confirmation alongside layout text. |

## Per-page assessment and fresh outputs

| Source ID | Page | Fresh native/layout assessment | Rendered | OCR | Limitation |
|---|---:|---|---|---|---|
| DOC-001 | 1 | Usable abstract including sample size, primary outcome, and results. | Yes | No | Two-column extraction order is handled by layout asset. |
| DOC-001 | 2 | Usable introduction and methods. | No | No | Not a result display. |
| DOC-001 | 3 | Usable outcomes and statistical-analysis definitions. | No | No | Not a tabular result display. |
| DOC-001 | 4 | Usable participant-flow figure and randomization/result narrative. | Yes | No | Flow layout checked in render. |
| DOC-001 | 5 | Usable Table 1 baseline values and footnotes. | Yes | No | Table alignment checked in render. |
| DOC-001 | 6 | Usable Table 2 efficacy values, intervals, P values, and footnotes. | Yes | No | Table alignment checked in render. |
| DOC-001 | 7 | Usable Figure 2 and clinical/adverse-event result narrative. | Yes | No | Figure labels checked in render. |
| DOC-001 | 8 | Usable Table 3 adverse events and discussion. | Yes | No | Table alignment checked in render. |
| DOC-001 | 9 | Usable discussion and article information. | No | No | No standalone result table/figure. |
| DOC-001 | 10 | Usable references. | No | No | No result-relevant quantitative display. |
| DOC-002 | 1 | Usable protocol cover/administrative content. | No | No | No result display. |
| DOC-002 | 2 | Usable background and planned population statements. | No | No | No standalone result display. |
| DOC-002 | 3 | Usable eligibility, endpoint, and assessment definitions. | Yes | No | Render preserves line-numbered protocol layout. |
| DOC-002 | 4 | Usable intervention/procedure details. | Yes | No | Render preserves line-numbered protocol layout. |
| DOC-002 | 5 | Usable primary-endpoint assessment and outcome definitions. | Yes | No | Render preserves line-numbered protocol layout. |
| DOC-002 | 6 | Usable sample-size and data-analysis text. | Yes | No | Render preserves line-numbered protocol layout. |
| DOC-002 | 7 | Usable statistical-analysis rules and planned comparisons. | Yes | No | Render preserves line-numbered protocol layout. |
| DOC-002 | 8 | Usable data-management/monitoring content. | No | No | No result display. |
| DOC-002 | 9 | Usable ethics/administrative content. | No | No | No result display. |
| DOC-002 | 10 | Usable archiving/publication content. | No | No | No result display. |
| DOC-002 | 11 | Usable references. | No | No | No result display. |
| DOC-002 | 12 | Usable references. | No | No | No result display. |
| DOC-002 | 13 | Usable references. | No | No | No result display. |
| DOC-002 | 14 | Usable final reference page. | No | No | No result display. |
| DOC-003 | 1 | Usable supplement contents list. | No | No | No standalone numeric display. |
| DOC-003 | 2 | Usable statistical-analysis methods and missing-data rules. | Yes | No | Render preserves formula/model context. |
| DOC-003 | 3 | Usable references. | No | No | No result display. |
| DOC-003 | 4 | Usable eTable device counts by assigned group and strategy. | Yes | No | Table alignment checked in render. |
| DOC-003 | 5 | Usable eFigure 1 ordinal outcome distribution. | Yes | No | Figure labels checked in render. |
| DOC-003 | 6 | Usable eFigure 2 subgroup counts, ORs, CIs, P values, and P heterogeneity. | Yes | No | Figure labels checked in render. |

## Evidence readiness

All 30 direct PDF pages have fresh native and layout text. The 15 rendered pages cover the identified result-relevant article results, protocol endpoint/statistical definitions, and supplement table/figures. There are no unavailable extraction units and no OCR units.
