# DOC-001 page-level extraction manifest

- Source PDF: `/home/bulunte/ai-paper-val/jama.2024.4183/jama_cinciripini_2024_oi_240036_1716416465.98349.pdf`
- Selected scientific-audit range: PDF pages 1–10.
- Method: native PDF text (`pdftotext -layout`) was extracted before any rendering. Text was normalized by removing trailing whitespace only; source order and table layout were retained.
- OCR rule applied: no page required OCR. All selected pages had a usable native text layer; visual pages were rendered to preserve layout for downstream checks, not as OCR input.
- Image resolution: 200 dpi JPEG.

| Source PDF page | Native text file | Non-whitespace characters | Extraction-quality assessment | Page visual / purpose | Rendered image | OCR status |
|---:|---|---:|---|---|---|---|
| 1 | `native_text/page-001.txt` | 4191 | Good | Article abstract/results | No | Not required — usable native text |
| 2 | `native_text/page-002.txt` | 5608 | Good | Methods | No | Not required — usable native text |
| 3 | `native_text/page-003.txt` | 1245 | Adequate; figure labels are represented in native text | Figure 1, SMART design | `page_images/page-003.jpg` | Not required — native labels and rendered layout are usable |
| 4 | `native_text/page-004.txt` | 5203 | Good | Methods/results transition | No | Not required — usable native text |
| 5 | `native_text/page-005.txt` | 3779 | Good; table content is represented | Baseline Table and primary-outcome text | `page_images/page-005.jpg` | Not required — native table text and rendered layout are usable |
| 6 | `native_text/page-006.txt` | 2248 | Adequate; flow labels are represented | Figure 2, participant flow | `page_images/page-006.jpg` | Not required — native labels and rendered layout are usable |
| 7 | `native_text/page-007.txt` | 3777 | Good; figure labels and adjacent results are represented | Figure 3, outcome distributions | `page_images/page-007.jpg` | Not required — native figure text and rendered layout are usable |
| 8 | `native_text/page-008.txt` | 5243 | Good | Discussion/results interpretation | No | Not required — usable native text |
| 9 | `native_text/page-009.txt` | 7805 | Good | Article information/references | No | Not required — usable native text |
| 10 | `native_text/page-010.txt` | 3298 | Good | References | No | Not required — usable native text |

## Derived files

- `native_text/selected-pages-normalized.txt` — combined native extraction for PDF pages 1–10; form-feed characters preserve page boundaries.
- `native_text/page-001.txt` through `native_text/page-010.txt` — one normalized native extraction per source page.
- `page_images/page-003.jpg`, `page_images/page-005.jpg`, `page_images/page-006.jpg`, `page_images/page-007.jpg` — only visual-evidence pages required for later figure/table/flow checks.
