# DOC-004 Page-Level Preprocessing Manifest

Source PDF: `joi240158supp3_prod_1742927563.7911.pdf` (unchanged). Native extraction used `pdftotext -layout`; native text was assessed before any rendering. “Usable” means the text layer contains readable supplement content without missing/sparse/corrupted scientific text. Page images are 200-dpi PNG renders retained only where tables or figures are needed for later checks.

| PDF page | Content / audit role | Native-text quality | Text used | Render retained | OCR | Source-linked artifacts |
|---:|---|---|---|---|---|---|
| 1 | Contents / scope locator | Usable | Native | No | No—native sufficient | `native_pages/page-01.txt` |
| 2 | eMethods | Usable | Native | No | No—native sufficient | `native_pages/page-02.txt` |
| 3 | eMethods | Usable | Native | No | No—native sufficient | `native_pages/page-03.txt` |
| 4 | eMethods | Usable | Native | No | No—native sufficient | `native_pages/page-04.txt` |
| 5 | eMethods | Usable | Native | No | No—native sufficient | `native_pages/page-05.txt` |
| 6 | eMethods | Usable | Native | No | No—native sufficient | `native_pages/page-06.txt` |
| 7 | eMethods | Usable | Native | No | No—native sufficient | `native_pages/page-07.txt` |
| 8 | eMethods | Usable | Native | No | No—native sufficient | `native_pages/page-08.txt` |
| 9 | eMethods | Usable | Native | No | No—native sufficient | `native_pages/page-09.txt` |
| 10 | eMethods | Usable | Native | No | No—native sufficient | `native_pages/page-10.txt` |
| 11 | eMethods | Usable | Native | No | No—native sufficient | `native_pages/page-11.txt` |
| 12 | eMethods | Usable | Native | No | No—native sufficient | `native_pages/page-12.txt` |
| 13 | eMethods / table transition | Usable | Native | No | No—native sufficient | `native_pages/page-13.txt` |
| 14 | eTable 1 | Usable | Native | Yes—table | No—native sufficient | `native_pages/page-14.txt`; `page_images/page-14.png` |
| 15 | eTable 2 | Usable | Native | Yes—table | No—native sufficient | `native_pages/page-15.txt`; `page_images/page-15.png` |
| 16 | eTable 3A | Usable | Native | Yes—table | No—native sufficient | `native_pages/page-16.txt`; `page_images/page-16.png` |
| 17 | eTable 3B | Usable | Native | Yes—table | No—native sufficient | `native_pages/page-17.txt`; `page_images/page-17.png` |
| 18 | eTable 4 (starts) | Usable | Native | Yes—forest-plot table | No—native sufficient | `native_pages/page-18.txt`; `page_images/page-18.png` |
| 19 | eTable 4 (continuation) | Usable | Native | Yes—forest-plot table | No—native sufficient | `native_pages/page-19.txt`; `page_images/page-19.png` |
| 20 | eTable 4 (continuation) | Usable | Native | Yes—forest-plot table | No—native sufficient | `native_pages/page-20.txt`; `page_images/page-20.png` |
| 21 | eTable 5 (starts) | Usable | Native | Yes—adverse-event table | No—native sufficient | `native_pages/page-21.txt`; `page_images/page-21.png` |
| 22 | eTable 5 (continuation) | Usable | Native | Yes—adverse-event table | No—native sufficient | `native_pages/page-22.txt`; `page_images/page-22.png` |
| 23 | eTable 5 (continuation) | Usable | Native | Yes—adverse-event table | No—native sufficient | `native_pages/page-23.txt`; `page_images/page-23.png` |
| 24 | eTable 5 (continuation) | Usable | Native | Yes—adverse-event table | No—native sufficient | `native_pages/page-24.txt`; `page_images/page-24.png` |
| 25 | eFigure, neurofilament sensitivity analysis | Usable | Native | Yes—figure | No—native sufficient | `native_pages/page-25.txt`; `page_images/page-25.png` |
| 26 | Trailing blank / rights page | Sparse as expected; no result content | Not included in normalized audit text | No | Not Audited by Design | `native_pages/page-26.txt` |

Selected audit text range: PDF pp. 1–25. OCR page range: none. Retained image range: PDF pp. 14–25. PDF p. 26 is excluded as trailing non-scientific content. The combined normalized text preserves `SOURCE PDF PAGE` delimiters in `normalized_text.txt`.
