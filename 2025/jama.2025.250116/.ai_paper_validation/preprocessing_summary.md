# PDF Preprocessing Summary

Native PDF text was extracted first for all 52 scientific-audit pages. The page-level method, quality assessment, source-page link, and derived-artifact paths are retained in `page_level_extraction_manifest.json`.

| Document | Scoped pages | Native only | Native + rendered PNG + OCR | Quality note |
|---|---|---:|---:|---|
| DOC-001-MAIN | 1-9 | 3 | 6 (pp 3-8) | Native text usable; visual derivatives retained for Figure 1, Tables 1-3, and Figure 2. |
| DOC-003-RESULTS-SUPP | 6-8, 14-53 | 0 | 43 | Native text usable on 35 pages with layout limits; 8 figure/table pages sparse for visual content and OCR-supported. |
| DOC-002-PROTOCOL | Not Audited by Design | 0 | 0 | No scientific extraction, rendering, or OCR performed. |

All retained visual images were rendered at 220 dpi and OCRed with Tesseract (`--psm 6`). Sampled flow, table, and figure images were visually legible. Source PDFs were read only and remain unchanged.
