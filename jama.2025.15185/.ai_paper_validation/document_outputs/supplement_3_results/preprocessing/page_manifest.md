# DOC-004 / Results supplement — preprocessing page manifest

Source PDF: `joi250066supp3_prod_1761597796.4701.pdf` (unchanged)

Selected scientific-audit scope: PDF pages 10-27. Native text was extracted first from every selected page. `normalized_text/` is a page-preserving derivative of `native_text/` with form-feed characters and trailing whitespace removed. All selected pages were rendered at 200 dpi because each contains a results-relevant eTable or eFigure. Every row maps source PDF page `N` to `normalized_text/page-NNN.txt` and, where rendered, `page_images/page-NNN.png`.

| PDF page | Principal content | Native extraction quality | OCR status | Source-linked render |
|---:|---|---|---|---|
| 10 | eTable 1 | Adequate | Not needed | `page_images/page-010.png` |
| 11 | eTable continuation | Adequate | Not needed | `page_images/page-011.png` |
| 12 | eTable 2 | Adequate | Not needed | `page_images/page-012.png` |
| 13 | eTable 2 continuation | Adequate | Not needed | `page_images/page-013.png` |
| 14 | eTable 3 | Adequate | Not needed | `page_images/page-014.png` |
| 15 | eTable 4 | Adequate | Not needed | `page_images/page-015.png` |
| 16 | eTable 5 | Adequate | Not needed | `page_images/page-016.png` |
| 17 | eTable 6 | Adequate | Not needed | `page_images/page-017.png` |
| 18 | eTables 7-8 (embedded table images) | Sparse: headings/footer only | Required; engine unavailable | `page_images/page-018.png` |
| 19 | eTable 9 | Adequate | Not needed | `page_images/page-019.png` |
| 20 | eFigure 1 | Adequate | Not needed | `page_images/page-020.png` |
| 21 | eFigure 2 (study schedule image) | Sparse: title/footer only | Required; engine unavailable | `page_images/page-021.png` |
| 22 | eFigure 3 (enrollment image) | Sparse: title/footer only | Required; engine unavailable | `page_images/page-022.png` |
| 23 | eFigure 4 forest plot | Partial: title/legend; plotted values absent | Required for graphical values; engine unavailable | `page_images/page-023.png` |
| 24 | eFigure 4 legend continuation | Adequate for its text-only content | Not needed | `page_images/page-024.png` |
| 25 | eFigure 5 plot | Sparse: title/legend only | Required for graphical values; engine unavailable | `page_images/page-025.png` |
| 26 | eFigure 6 plot | Sparse: title/footer only | Required for graphical values; engine unavailable | `page_images/page-026.png` |
| 27 | eFigure 7 forest plot | Partial: title/legend; plotted values absent | Required for graphical values; engine unavailable | `page_images/page-027.png` |

OCR limitation: no executable OCR engine (Tesseract, OCRmyPDF, GOCR, Cuneiform, or OCRAD) was available in the supplied environment. The pages needing OCR are preserved as 200-dpi source-linked PNGs for later visual review. No content was inferred or added to the text derivatives.
