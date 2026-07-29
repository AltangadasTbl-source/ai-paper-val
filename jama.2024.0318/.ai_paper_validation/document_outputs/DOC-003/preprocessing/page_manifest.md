# Page-Level Preprocessing Manifest — DOC-003

- Source PDF: `joi240004supp2_prod_1721756962.82552.pdf` (unchanged)
- Scientific extraction scope: PDF pages 8-22 only (supplemental eFigures 1-6 and eTables 1-7). Pages 1-7 are cover, contents, eMethods, statistical appendix, and references, and are **Not Audited by Design** for scientific checks.
- Native extraction: Poppler `pdftotext -layout`, UTF-8 text retained only for selected result-relevant pages.
- Rendering: 200-dpi PNG for each selected figure/table page.
- OCR limitation: no local OCR executable was available. Pages 8-13 have sparse native figure text and are marked OCR-required / unavailable; their rendered PNGs preserve the visual evidence for later human or image-based review. Table pages retain usable native text and did not require OCR.
- Source linkage: Every selected derivative is page-numbered and maps one-to-one to the named source PDF page.

| Source PDF page | Scope / native text quality | Extraction used | Derived text | Visual derivative | OCR status | Reason / source content |
|---:|---|---|---|---|---|---|
| 1 | **Not Audited by Design** | None retained | — | — | Not applicable | Cover / section list |
| 2 | **Not Audited by Design** | None retained | — | — | Not applicable | Contents |
| 3 | **Not Audited by Design** | None retained | — | — | Not applicable | eMethods |
| 4 | **Not Audited by Design** | None retained | — | — | Not applicable | eMethods |
| 5 | **Not Audited by Design** | None retained | — | — | Not applicable | Statistical supplementary appendix |
| 6 | **Not Audited by Design** | None retained | — | — | Not applicable | Statistical supplementary appendix |
| 7 | **Not Audited by Design** | None retained | — | — | Not applicable | References |
| 8 | Sparse (134 characters) | Native + rendered | `normalized_text/page-008.txt` | `page_images/page-008.png` | Required; unavailable | eFigure 1; plot labels/data are visual |
| 9 | Sparse (788 characters) | Native + rendered | `normalized_text/page-009.txt` | `page_images/page-009.png` | Required; unavailable | eFigure 2; plotted trajectories are visual |
| 10 | Sparse (203 characters) | Native + rendered | `normalized_text/page-010.txt` | `page_images/page-010.png` | Required; unavailable | eFigure 3; plotted medication use is visual |
| 11 | Sparse (199 characters) | Native + rendered | `normalized_text/page-011.txt` | `page_images/page-011.png` | Required; unavailable | eFigure 4; plotted medication use is visual |
| 12 | Sparse (417 characters) | Native + rendered | `normalized_text/page-012.txt` | `page_images/page-012.png` | Required; unavailable | eFigure 5; plotted trajectories are visual |
| 13 | Partial (1,042 characters) | Native + rendered | `normalized_text/page-013.txt` | `page_images/page-013.png` | Required; unavailable | eFigure 6; subgroup plot values are visual |
| 14 | Good (4,053 characters) | Native + rendered | `normalized_text/page-014.txt` | `page_images/page-014.png` | Not needed | eTable 1 |
| 15 | Good (5,006 characters) | Native + rendered | `normalized_text/page-015.txt` | `page_images/page-015.png` | Not needed | eTable 2 (first page) |
| 16 | Good (768 characters) | Native + rendered | `normalized_text/page-016.txt` | `page_images/page-016.png` | Not needed | eTable 2 footnotes / continuation |
| 17 | Good (5,022 characters) | Native + rendered | `normalized_text/page-017.txt` | `page_images/page-017.png` | Not needed | eTable 3 |
| 18 | Good (1,105 characters) | Native + rendered | `normalized_text/page-018.txt` | `page_images/page-018.png` | Not needed | eTable 4 |
| 19 | Good (3,522 characters) | Native + rendered | `normalized_text/page-019.txt` | `page_images/page-019.png` | Not needed | eTable 5 (first page) |
| 20 | Good (2,675 characters) | Native + rendered | `normalized_text/page-020.txt` | `page_images/page-020.png` | Not needed | eTable 5 (continuation) |
| 21 | Good (3,124 characters) | Native + rendered | `normalized_text/page-021.txt` | `page_images/page-021.png` | Not needed | eTable 6 |
| 22 | Good (1,041 characters) | Native + rendered | `normalized_text/page-022.txt` | `page_images/page-022.png` | Not needed | eTable 7 |

## Extraction status

Scientific preprocessing is complete for selected pages 8-22. The native PDF text includes minor replacement-character corruption in repeated copyright footers and mathematical notation; this does not affect retained table values. Exact visual content remains available in the page PNGs. No source PDF was modified.
