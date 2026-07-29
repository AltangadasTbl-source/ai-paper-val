# Page-Level Preprocessing Manifest — JAMA-2024-23898-MAIN

- Source PDF: `jama_paterson_2024_oi_240139_1741633738.12862.pdf` (unchanged)
- Scoped source pages: PDF pp. 1-10
- Native extraction: Poppler `pdftotext` 26.01.0. `native_text/` preserves layout; `normalized_text/` is raw native reading order for downstream text processing.
- Rendering: Poppler `pdftoppm` 26.01.0 at 300 dpi, PNG. Images were created only for result-relevant tables, figures, and the participant-flow diagram.
- OCR: no local OCR executable was available (`tesseract`, `ocrmypdf`, `gocr`, `cuneiform`, `ocrad`, `kraken`, `easyocr`, and `paddleocr` were not present). Native text was retained as the text source; no OCR output was fabricated.

| PDF page | Source-page reference | Native-text quality | Extraction used | Visual content / rendering decision | Derived artifacts |
|---:|---|---|---|---|---|
| 1 | `JAMA-2024-23898-MAIN`, `jama_paterson_2024_oi_240139_1741633738.12862.pdf`, PDF p. 1 | High (4,052 normalized bytes); complete abstract/prose | Native | No result-relevant table, figure, or flow diagram requiring later checking; no render | `native_text/page-001.txt`; `normalized_text/page-001.txt` |
| 2 | `JAMA-2024-23898-MAIN`, same PDF, PDF p. 2 | High (6,147 bytes); complete prose/section labels | Native | No required visual result artifact; no render | `native_text/page-002.txt`; `normalized_text/page-002.txt` |
| 3 | `JAMA-2024-23898-MAIN`, same PDF, PDF p. 3 | High (3,245 bytes); flow labels/counts and exclusions recoverable | Native | Figure 1 participant flow required for flow checking; rendered for visual structure | `native_text/page-003.txt`; `normalized_text/page-003.txt`; `page_images/page-003.png` |
| 4 | `JAMA-2024-23898-MAIN`, same PDF, PDF p. 4 | High (5,635 bytes); Table 1 text recoverable, but column layout is spatial | Native | Table 1 required for later table checks; rendered | `native_text/page-004.txt`; `normalized_text/page-004.txt`; `page_images/page-004.png` |
| 5 | `JAMA-2024-23898-MAIN`, same PDF, PDF p. 5 | High (5,847 bytes); complete analysis/results prose | Native | No table, figure, or flow diagram on page; no render | `native_text/page-005.txt`; `normalized_text/page-005.txt` |
| 6 | `JAMA-2024-23898-MAIN`, same PDF, PDF p. 6 | High (3,625 bytes); Table 2 values/footnotes recoverable, but column layout is spatial | Native | Table 2 required for later table/statistical checks; rendered | `native_text/page-006.txt`; `normalized_text/page-006.txt`; `page_images/page-006.png` |
| 7 | `JAMA-2024-23898-MAIN`, same PDF, PDF p. 7 | High (3,732 bytes); continued Table 2 values/footnotes recoverable, but column layout is spatial | Native | Continued Table 2 required for later table/statistical checks; rendered | `native_text/page-007.txt`; `normalized_text/page-007.txt`; `page_images/page-007.png` |
| 8 | `JAMA-2024-23898-MAIN`, same PDF, PDF p. 8 | High (3,943 bytes); Figure 2 caption/table and Table 3 text recoverable; plot structure remains visual | Native | Figure 2 and Table 3 required for later figure/table checks; rendered | `native_text/page-008.txt`; `normalized_text/page-008.txt`; `page_images/page-008.png` |
| 9 | `JAMA-2024-23898-MAIN`, same PDF, PDF p. 9 | High (7,351 bytes); complete discussion/conclusion text | Native | No result-relevant table, figure, or flow diagram requiring rendering; no render | `native_text/page-009.txt`; `normalized_text/page-009.txt` |
| 10 | `JAMA-2024-23898-MAIN`, same PDF, PDF p. 10 | High (3,062 bytes); references text complete | Native | No result-relevant table, figure, or flow diagram requiring rendering; no render | `native_text/page-010.txt`; `normalized_text/page-010.txt` |

## Processing Outcome

All scoped main-article pages have a usable native text layer. Pages 3, 4, 6, 7, and 8 additionally have their required visual evidence retained as 300-dpi images. OCR was not needed to recover prose or table values and could not be run because no local OCR engine is installed. No source PDF was modified.
