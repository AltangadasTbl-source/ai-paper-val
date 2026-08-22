# Fresh Evidence-Asset Inventory

## Methods, commands, and tool versions

- Hashing: `sha256sum -- <each exact source filename>`; SHA-256 values are in `source_inventory.md` and the coordinator-owned before-hash ledger.
- Metadata: `pdfinfo <source>` (Poppler 26.01.0), one complete output per source in `preprocessing/metadata/`.
- Native text: `pdftotext <source> <output>` (Poppler 26.01.0), one source-complete text asset per PDF.
- Layout text: `pdftotext -layout <source> <output>` (Poppler 26.01.0), one source-complete table/layout asset per PDF.
- Rendering: `pdftoppm -r 150 -png <source> preprocessing/rendered_pages/DOC-00N` (Poppler 26.01.0). All 83 pages were rendered at 150 dpi, a conservative superset of the result-relevant visual scope.
- OCR decision: native and layout text was usable for every relevant page; therefore direct CPU Tesseract 5.5.0 was not run (0 OCR pages). No GPU was probed or used.

## Per-source evidence assets

| Source ID | Metadata asset | Native-text asset (bytes) | Layout-text asset (bytes) | Rendered visual units | OCR units | Extraction method and result-relevant visual scope | Limitations |
|---|---|---:|---:|---:|---:|---|---|
| DOC-001 | `preprocessing/metadata/DOC-001_pdfinfo.txt` | `preprocessing/native_text/DOC-001.txt` (58735) | `preprocessing/layout_text/DOC-001.txt` (100416) | 10 PNG pages (`DOC-001-01.png` to `DOC-001-10.png`) | 0 | Native + layout extraction; pp. 1-10 rendered, covering abstract/results narrative, Figure 1 on p. 4, Table 1 on p. 5, Figure 3 on p. 6, Table 2 on pp. 7-8, and remaining quantitative narrative. | PDF table/figure geometry is preserved best in the layout asset and renders; native reading order of multi-column prose can differ from visual order. |
| DOC-002 | `preprocessing/metadata/DOC-002_pdfinfo.txt` | `preprocessing/native_text/DOC-002.txt` (103605) | `preprocessing/layout_text/DOC-002.txt` (128021) | 55 PNG pages (`DOC-002-01.png` to `DOC-002-55.png`) | 0 | Native + layout extraction; all pp. 1-55 rendered. Result-defining areas include design/schedules (pp. 12-17 and 46), sample-size planning (pp. 19-21), endpoints (pp. 31-34), Bayesian analysis/interim rules (pp. 40-43), and recruitment/population material (pp. 44-45). | Some schedules/tables are visually dense; use rendered pages and layout text together for exact row/column alignment. Pages 51-55 are reference pages, rendered for source-complete coverage but contain no newly reported trial result. |
| DOC-003 | `preprocessing/metadata/DOC-003_pdfinfo.txt` | `preprocessing/native_text/DOC-003.txt` (24081) | `preprocessing/layout_text/DOC-003.txt` (31845) | 17 PNG pages (`DOC-003-01.png` to `DOC-003-17.png`) | 0 | Native + layout extraction; all pp. 1-17 rendered, covering eTables 1-4 (pp. 2-6), eFigures 1-3 (pp. 7-9), model code/parameter definitions (pp. 10-14), and simulation outputs (pp. 15-17). | Multi-column eTables and code blocks should be checked against rendered pages for exact cell/line alignment. |
| DOC-004 | `preprocessing/metadata/DOC-004_pdfinfo.txt` | `preprocessing/native_text/DOC-004.txt` (258) | `preprocessing/layout_text/DOC-004.txt` (261) | 1 PNG page (`DOC-004-1.png`) | 0 | Native + layout extraction; p. 1 rendered. The short text clearly states data availability is “No.” | No numerical table or analysis output is present. |

## Asset-count reconciliation

| Asset type | Count |
|---|---:|
| Direct source PDFs | 4 |
| Stable PDF pages | 83 |
| `pdfinfo` metadata files | 4 |
| Native-text files | 4 |
| Layout-text files | 4 |
| Rendered PNG pages | 83 |
| OCR text files | 0 |

All asset paths are relative to `.ai_paper_validation/review_1_5_2/`. The supplied PDFs were not modified.
