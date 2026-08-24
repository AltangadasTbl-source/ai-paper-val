# Fresh Evidence-Asset Inventory

## Tooling and method

All commands were run locally in the package root against the six direct PDF sources. No network, GPU, software installation, Office conversion, Office-structure helper, or prior audit derivative was used.

| Tool | Version observed | Applied method |
|---|---|---|
| `sha256sum` | GNU coreutils system utility | SHA-256 calculated for each direct source before preprocessing; values are recorded in `source_inventory.md` and the coordinator-owned before-hash artifact. |
| `file` | system utility | File type inspected for each source; DOC-001's page estimate conflicted with `pdfinfo` and was not used as the unit count. |
| `pdfinfo` | 26.01.0 | Metadata and authoritative page count written per source to `preprocessing/pdfinfo/`. |
| `pdftotext` | 26.01.0 | Fresh native text written for every page of every source. |
| `pdftotext -layout` | 26.01.0 | Fresh layout-preserving text written for every source, including tables, aligned displays, and figures. |
| `pdftoppm` | 26.01.0 | 150-dpi PNG renders created for result-relevant pages listed below. |
| `tesseract` | 5.5.0 | Not invoked: native and layout text were usable for every result-relevant page. |

## Per-source derivatives and decisions

| Source ID | Metadata asset | Native-text asset | Layout-text asset | Rendered result-relevant pages | OCR decision and limitation |
|---|---|---|---|---|---|
| DOC-001 | `preprocessing/pdfinfo/jama_bluth_2019_oi_190055_16092.pdfinfo.txt` | `preprocessing/native_text/jama_bluth_2019_oi_190055_16092.txt` (76,343 bytes) | `preprocessing/layout_text/jama_bluth_2019_oi_190055_16092.txt` (131,510 bytes) | pp. 1-12; 12 PNG assets named `preprocessing/rendered_pages/jama_bluth_2019_oi_190055_16092-pN.png` | No OCR: native/layout extraction was legible and contained abstract, flow, tables, outcome results, captions, and narrative. Reference-only pp. 13-14 were not rendered. |
| DOC-002 | `preprocessing/pdfinfo/joi190055supp1_prod_16092.pdfinfo.txt` | `preprocessing/native_text/joi190055supp1_prod_16092.txt` (65,459 bytes) | `preprocessing/layout_text/joi190055supp1_prod_16092.txt` (79,641 bytes) | pp. 8-24, 29-34; 23 PNG assets named `preprocessing/rendered_pages/joi190055supp1_prod_16092-pN.png` | No OCR: native/layout text was usable. Render scope covers objectives, population/intervention/endpoints, analysis, and quantitative appendices; introductory/reference/administrative-only pages were not rendered. |
| DOC-003 | `preprocessing/pdfinfo/joi190055supp2_prod_16092.pdfinfo.txt` | `preprocessing/native_text/joi190055supp2_prod_16092.txt` (6,094 bytes) | `preprocessing/layout_text/joi190055supp2_prod_16092.txt` (6,887 bytes) | pp. 1-3; 3 PNG assets named `preprocessing/rendered_pages/joi190055supp2_prod_16092-pN.png` | No OCR: all pages have usable text and are analysis-change relevant. |
| DOC-004 | `preprocessing/pdfinfo/joi190055supp3_prod_16092.pdfinfo.txt` | `preprocessing/native_text/joi190055supp3_prod_16092.txt` (9,310 bytes) | `preprocessing/layout_text/joi190055supp3_prod_16092.txt` (9,516 bytes) | pp. 1-3; 3 PNG assets named `preprocessing/rendered_pages/joi190055supp3_prod_16092-pN.png` | No OCR: all pages have usable text and are final-analysis-plan relevant. |
| DOC-005 | `preprocessing/pdfinfo/joi190055supp4_prod_16092.pdfinfo.txt` | `preprocessing/native_text/joi190055supp4_prod_16092.txt` (75,193 bytes) | `preprocessing/layout_text/joi190055supp4_prod_16092.txt` (94,059 bytes) | pp. 18-42; 25 PNG assets named `preprocessing/rendered_pages/joi190055supp4_prod_16092-pN.png` | No OCR: native/layout text was usable. Render scope covers eMethods, eTables, and eFigures. Committee/investigator-list pp. 1-17 and references p. 43 were not rendered because they contain no result-bearing quantitative display. |
| DOC-006 | `preprocessing/pdfinfo/joi190055supp5_prod_16092.pdfinfo.txt` | `preprocessing/native_text/joi190055supp5_prod_16092.txt` (1,124 bytes) | `preprocessing/layout_text/joi190055supp5_prod_16092.txt` (1,126 bytes) | p. 1; 1 PNG asset `preprocessing/rendered_pages/joi190055supp5_prod_16092-p1.png` | No OCR: the single page has usable native/layout text. |

**Derivative totals:** 6 `pdfinfo` records; 6 native-text files; 6 layout-text files; 67 rendered PNG pages; 0 OCR text files. `preprocessing/office_structure/` and `preprocessing/converted_pdf/` are intentionally empty because no Office source was supplied.

## Exact command pattern

For each explicitly named source, the following direct commands were used, with destination basename matched to the source basename:

```text
sha256sum -- "SOURCE.pdf"
file --brief "SOURCE.pdf"
pdfinfo "SOURCE.pdf" > ".ai_paper_validation/review_1_5_2/preprocessing/pdfinfo/SOURCE.pdfinfo.txt"
pdftotext -- "SOURCE.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/native_text/SOURCE.txt"
pdftotext -layout -- "SOURCE.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/layout_text/SOURCE.txt"
pdftoppm -f N -l N -singlefile -r 150 -png -- "SOURCE.pdf" ".ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/SOURCE-pN"
```

No result-relevant page met the workflow condition for OCR: unusable relevant native/layout text.

