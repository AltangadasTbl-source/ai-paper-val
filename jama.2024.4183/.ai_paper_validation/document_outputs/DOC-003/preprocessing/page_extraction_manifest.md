# DOC-003 page-level extraction manifest

- Source PDF: `/home/bulunte/ai-paper-val/jama.2024.4183/joi240036supp2_prod_1716416466.01349.pdf`
- Selected scientific-audit range: PDF pages 4–35. PDF pages 1–3 (cover/contents) and page 36 (references) were excluded from scientific extraction by scope selection.
- Method: native PDF text (`pdftotext -layout`) was extracted before any rendering. Text was normalized by removing trailing whitespace only; source order and table layout were retained.
- OCR rule applied: no selected page required OCR. All selected pages had a usable native text layer. Tables and figures were rendered at 200 dpi for later visual checks; their native text remains the authoritative text artifact.

| Source PDF page | Native text file | Non-whitespace characters | Extraction-quality assessment | Page visual / purpose | Rendered image | OCR status |
|---:|---|---:|---|---|---|---|
| 4 | `native_text/page-004.txt` | 2242 | Good | eAppendix sample-size text | No | Not required — usable native text |
| 5 | `native_text/page-005.txt` | 2211 | Good | eAppendix modeling text | No | Not required — usable native text |
| 6 | `native_text/page-006.txt` | 2172 | Good | eAppendix modeling text | No | Not required — usable native text |
| 7 | `native_text/page-007.txt` | 1338 | Adequate | eAppendix modeling text | No | Not required — usable native text |
| 8 | `native_text/page-008.txt` | 2416 | Good | eAppendix simulations text | No | Not required — usable native text |
| 9 | `native_text/page-009.txt` | 2204 | Good | Secondary-outcome text | No | Not required — usable native text |
| 10 | `native_text/page-010.txt` | 2215 | Good | Secondary-outcome text | No | Not required — usable native text |
| 11 | `native_text/page-011.txt` | 2065 | Good | Secondary-outcome text | No | Not required — usable native text |
| 12 | `native_text/page-012.txt` | 2214 | Good | Secondary-outcome text | No | Not required — usable native text |
| 13 | `native_text/page-013.txt` | 1833 | Good | Secondary-outcome text | No | Not required — usable native text |
| 14 | `native_text/page-014.txt` | 1099 | Adequate; figure labels are represented | E-Figure 1 | `page_images/page-014.jpg` | Not required — native labels and rendered layout are usable |
| 15 | `native_text/page-015.txt` | 855 | Adequate; figure labels are represented | E-Figure 2 | `page_images/page-015.jpg` | Not required — native labels and rendered layout are usable |
| 16 | `native_text/page-016.txt` | 868 | Adequate; figure labels are represented | E-Figure 3 | `page_images/page-016.jpg` | Not required — native labels and rendered layout are usable |
| 17 | `native_text/page-017.txt` | 674 | Adequate; table content is represented | E-Table 1 | `page_images/page-017.jpg` | Not required — native table text and rendered layout are usable |
| 18 | `native_text/page-018.txt` | 1315 | Good; table content is represented | E-Table 2 | `page_images/page-018.jpg` | Not required — native table text and rendered layout are usable |
| 19 | `native_text/page-019.txt` | 1589 | Good; table content is represented | E-Table 3 (start) | `page_images/page-019.jpg` | Not required — native table text and rendered layout are usable |
| 20 | `native_text/page-020.txt` | 1175 | Good; table content is represented | E-Table 3 (continuation) | `page_images/page-020.jpg` | Not required — native table text and rendered layout are usable |
| 21 | `native_text/page-021.txt` | 552 | Adequate; compact table page | E-Table 4 | `page_images/page-021.jpg` | Not required — native table text and rendered layout are usable |
| 22 | `native_text/page-022.txt` | 1784 | Good; table content is represented | E-Table 5 (start) | `page_images/page-022.jpg` | Not required — native table text and rendered layout are usable |
| 23 | `native_text/page-023.txt` | 1682 | Good; table content is represented | E-Table 5 (continuation) | `page_images/page-023.jpg` | Not required — native table text and rendered layout are usable |
| 24 | `native_text/page-024.txt` | 1617 | Good; table content is represented | E-Table 5 (continuation) | `page_images/page-024.jpg` | Not required — native table text and rendered layout are usable |
| 25 | `native_text/page-025.txt` | 602 | Adequate; compact table page | E-Table 5 (continuation) | `page_images/page-025.jpg` | Not required — native table text and rendered layout are usable |
| 26 | `native_text/page-026.txt` | 2269 | Good; table content is represented | E-Table 6 (start) | `page_images/page-026.jpg` | Not required — native table text and rendered layout are usable |
| 27 | `native_text/page-027.txt` | 1882 | Good; table content is represented | E-Table 6 (continuation) | `page_images/page-027.jpg` | Not required — native table text and rendered layout are usable |
| 28 | `native_text/page-028.txt` | 2012 | Good; table content is represented | E-Table 6 (continuation) | `page_images/page-028.jpg` | Not required — native table text and rendered layout are usable |
| 29 | `native_text/page-029.txt` | 1862 | Good; table content is represented | E-Table 6 (continuation) | `page_images/page-029.jpg` | Not required — native table text and rendered layout are usable |
| 30 | `native_text/page-030.txt` | 1608 | Good; table content is represented | E-Table 6 (continuation) | `page_images/page-030.jpg` | Not required — native table text and rendered layout are usable |
| 31 | `native_text/page-031.txt` | 427 | Adequate; compact table page | E-Table 7 | `page_images/page-031.jpg` | Not required — native table text and rendered layout are usable |
| 32 | `native_text/page-032.txt` | 701 | Adequate; compact table page | E-Table 8 | `page_images/page-032.jpg` | Not required — native table text and rendered layout are usable |
| 33 | `native_text/page-033.txt` | 1014 | Good; table content is represented | E-Table 9 | `page_images/page-033.jpg` | Not required — native table text and rendered layout are usable |
| 34 | `native_text/page-034.txt` | 730 | Adequate; compact table page | E-Table 10 | `page_images/page-034.jpg` | Not required — native table text and rendered layout are usable |
| 35 | `native_text/page-035.txt` | 900 | Adequate; table content is represented | E-Tables 11–12 | `page_images/page-035.jpg` | Not required — native table text and rendered layout are usable |

## Derived files

- `native_text/selected-pages-normalized.txt` — combined native extraction for PDF pages 4–35; form-feed characters preserve page boundaries.
- `native_text/page-004.txt` through `native_text/page-035.txt` — one normalized native extraction per source page.
- `page_images/page-014.jpg` through `page_images/page-035.jpg` — only result figure/table pages needed for later figure and table checks.
