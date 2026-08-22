# Fresh Evidence-Asset Inventory

All assets below were produced freshly from the direct PDFs. The outputs are package-relative to `.ai_paper_validation/review_1_5_2/`.

## Tooling

| Tool | Version | Applied method |
|---|---|---|
| `pdfinfo` | 26.01.0 | Source metadata, page count, page geometry, encryption status |
| `pdftotext` | 26.01.0 | Native text extraction for every page of every PDF |
| `pdftotext -layout` | 26.01.0 | Layout-preserving text extraction for every page, including aligned table displays |
| `pdftoppm` | 26.01.0 | CPU rendering at 200 DPI of result-relevant visual-evidence pages |
| `tesseract` | 5.5.0 | Not invoked: native and layout text were usable for all relevant textual/table evidence |

Direct commands used, with each concrete PDF path substituted exactly:

```text
pdfinfo -- SOURCE.pdf
pdftotext -- SOURCE.pdf preprocessing/native_text/STEM.txt
pdftotext -layout -- SOURCE.pdf preprocessing/layout_text/STEM.txt
pdftoppm -f PAGE -l PAGE -singlefile -r 200 -png -- SOURCE.pdf preprocessing/rendered_pages/STEM-pPAGE
```

## Per-source assets and decisions

| Source ID | Native text | Layout text | Native/layout usability and OCR decision | Rendered result-relevant pages | Exact result-relevant scope |
|---|---|---|---|---|---|
| DOC-001 | `preprocessing/native_text/jama_simonis_2018_oi_180108.txt` (50034 bytes) | `preprocessing/layout_text/jama_simonis_2018_oi_180108.txt` (90896 bytes) | Usable for abstract, narrative, tables, and figure labels. No OCR. | 1, 3, 5, 6, 7 | Abstract/outcomes; CONSORT flow; Table 1 baseline characteristics; Table 2 clinical outcomes; Figure 2 mortality curves. |
| DOC-002 | `preprocessing/native_text/joi180108supp1_prod.txt` (82121 bytes) | `preprocessing/layout_text/joi180108supp1_prod.txt` (93091 bytes) | Usable for protocol text and tables. No OCR. | 10, 11, 15, 17-35, 48, 49 | Protocol summary/objectives; study population and sample size; intervention; methods/data variables; safety; primary/secondary outcome definitions; statistical and cost-effectiveness analysis; ARDS-definition table; tracheostomy scheme. |
| DOC-003 | `preprocessing/native_text/joi180108supp2_prod.txt` (28412 bytes) | `preprocessing/layout_text/joi180108supp2_prod.txt` (33446 bytes) | Usable for SAP text and amendment table. No OCR. | 3, 5-15, 21, 22 | SAP background, design/population/intervention, primary/secondary outcomes, database status, analysis procedures, conclusion, and modifications table. |
| DOC-004 | `preprocessing/native_text/joi180108supp3_prod.txt` (22884 bytes) | `preprocessing/layout_text/joi180108supp3_prod.txt` (35288 bytes) | Usable for eMethods/eTables 1-5. Figure pages contain titles rather than figure data in text, but were rendered for visual review; OCR would not improve the image evidence. | 1-3, 5-13 | Supplementary methods; eTables 1-5; eFigures 1-4. Page 4 is references only and was not rendered. |
| DOC-005 | `preprocessing/native_text/joi180108supp4_prod.txt` (506 bytes) | `preprocessing/layout_text/joi180108supp4_prod.txt` (536 bytes) | Usable for the complete sole-page collaborator content. No OCR. | 1 | Complete supplied source. |

## Asset counts

| Asset class | Count | Detail |
|---|---:|---|
| Native text files | 5 | One complete direct extraction per source, covering 94 pages |
| Layout text files | 5 | One complete direct extraction per source, covering 94 pages |
| Rendered PNG pages | 56 | Result-relevant visual evidence at 200 DPI |
| OCR text files | 0 | No relevant native/layout text was unusable |
| Identified quantitative display tables | 10 | DOC-001 Tables 1-2; DOC-002 protocol/appendix Tables 1-2; DOC-003 modifications table; DOC-004 eTables 1-5 |
| Identified visual figures | 6 | DOC-001 Figures 1-2; DOC-004 eFigures 1-4 |

No Office conversion or Office structure extraction applied because no Office source was supplied.
