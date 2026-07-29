# Page-Level Preprocessing Manifest — JAMA-2024-23898-SUPP-03-RESULTS

- Source PDF: `joi240139supp3_prod_1741633738.18862.pdf` (unchanged)
- Scoped source pages: PDF pp. 1-2
- Native extraction: Poppler `pdftotext` 26.01.0. `native_text/` preserves layout; `normalized_text/` is raw native reading order for downstream text processing.
- Rendering: Poppler `pdftoppm` 26.01.0 at 300 dpi, PNG.
- OCR: no local OCR executable was available (`tesseract`, `ocrmypdf`, `gocr`, `cuneiform`, `ocrad`, `kraken`, `easyocr`, and `paddleocr` were not present). The eFigure's graphical labels are therefore retained through the rendered image rather than an invented OCR transcript.

| PDF page | Source-page reference | Native-text quality | Extraction used | Visual content / rendering decision | Derived artifacts |
|---:|---|---|---|---|---|
| 1 | `JAMA-2024-23898-SUPP-03-RESULTS`, `joi240139supp3_prod_1741633738.18862.pdf`, PDF p. 1 | High for its cover/title content (434 normalized bytes); no result values expected on this page | Native | Cover page only; no render | `native_text/page-001.txt`; `normalized_text/page-001.txt` |
| 2 | `JAMA-2024-23898-SUPP-03-RESULTS`, same PDF, PDF p. 2 | Native text is usable for title and explanatory footnotes (1,183 bytes) but sparse for the eFigure because subgroup labels and estimates are rendered as vector graphics | Native + rendered image | eFigure is result-relevant and required for later figure/statistical checks; rendered at 300 dpi. OCR required by the sparse graphical text condition, but no local OCR engine was available. Use the image as the authoritative visual complement to native text. | `native_text/page-002.txt`; `normalized_text/page-002.txt`; `page_images/page-002.png` |

## Processing Outcome

Both scoped supplement pages have native text. PDF p. 2 also has a high-resolution render because the result-relevant eFigure's plotted labels are not represented in the native text layer. OCR was unavailable locally; no source PDF was modified.
