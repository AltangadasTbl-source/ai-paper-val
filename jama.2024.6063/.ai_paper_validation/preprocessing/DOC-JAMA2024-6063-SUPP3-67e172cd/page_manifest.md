# Page-Level Preprocessing Manifest

- Document ID: `DOC-JAMA2024-6063-SUPP3-67e172cd`
- Source PDF: `joi240048supp3_prod_1727199125.83025.pdf`
- Source-page convention: `PDF page` is the one-based physical page in the source PDF.
- Native extractor: `pdftotext -layout`; normalization removed CR and form-feed characters only, preserving table layout and text order.
- Quality decision: all pages have usable native text. Pages with few characters are caption/small-table/figure pages rather than failed extraction. No page needed OCR.
- Rendered images: all result-table and eFigure pages (2–15) were retained at 200 dpi for downstream table/figure/flow checking. The cover/index page 1 was not rendered.

| PDF page | Audit status | Native-text quality | Final extraction method | Normalized text | Rendered page image | Reason / source content |
|---:|---|---|---|---|---|---|
| 1 | Selected | Good (1,218 native characters; legible index) | Native | `normalized_text/page-001.txt` | — | Supplement contents/index |
| 2 | Selected | Good (843; compact, complete table) | Native | `normalized_text/page-002.txt` | `page_images/page-002.png` | eTable 1 |
| 3 | Selected | Good (1,003; compact, complete table) | Native | `normalized_text/page-003.txt` | `page_images/page-003.png` | eTable 2 |
| 4 | Selected | Good (747; compact, complete table) | Native | `normalized_text/page-004.txt` | `page_images/page-004.png` | eTable 3 |
| 5 | Selected | Good (8,136; structured multi-page table) | Native | `normalized_text/page-005.txt` | `page_images/page-005.png` | eTable 4, continued |
| 6 | Selected | Good (7,661; structured multi-page table) | Native | `normalized_text/page-006.txt` | `page_images/page-006.png` | eTable 4, continued |
| 7 | Selected | Good (1,280; table notes) | Native | `normalized_text/page-007.txt` | `page_images/page-007.png` | eTable 4 notes |
| 8 | Selected | Good (545; compact, complete table) | Native | `normalized_text/page-008.txt` | `page_images/page-008.png` | eTable 5 |
| 9 | Selected | Good (882; compact, complete table) | Native | `normalized_text/page-009.txt` | `page_images/page-009.png` | eTable 6 |
| 10 | Selected | Good (3,462; structured table) | Native | `normalized_text/page-010.txt` | `page_images/page-010.png` | eTable 7, continued |
| 11 | Selected | Good (2,719; structured table continuation) | Native | `normalized_text/page-011.txt` | `page_images/page-011.png` | eTable 7, continued |
| 12 | Selected | Good (2,486; structured table continuation) | Native | `normalized_text/page-012.txt` | `page_images/page-012.png` | eTable 7, continued |
| 13 | Selected | Good (649; table end note) | Native | `normalized_text/page-013.txt` | `page_images/page-013.png` | eTable 7 conclusion |
| 14 | Selected | Good (2,674; structured table) | Native | `normalized_text/page-014.txt` | `page_images/page-014.png` | eTable 8 |
| 15 | Selected | Good for caption (198; expected sparse figure page) | Native | `normalized_text/page-015.txt` | `page_images/page-015.png` | eFigure; image retained for visual review |

OCR was not used: all table labels, values, and the eFigure caption are available through native extraction. Page 15 is sparse by design, so the retained rendering—not OCR—preserves its visual evidence.
