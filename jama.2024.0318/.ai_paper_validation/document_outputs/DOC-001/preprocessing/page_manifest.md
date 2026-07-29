# Page-Level Preprocessing Manifest — DOC-001

- Source PDF: `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf` (unchanged)
- Scope: all 11 PDF pages (main article).
- Native extraction: Poppler `pdftotext -layout`, one UTF-8 text file per source PDF page.
- Rendering: 200-dpi PNG only for pages containing result-relevant flow, figures, or tables.
- OCR: not required for this document. Every page has a usable native text layer; visual assets are retained for the pages whose charts/tables/flow diagram require visual checking.
- Source linkage: Every row retains the source filename and PDF page number; the page-numbered derivative names correspond one-to-one with that source page.

| Source PDF page | Native text quality | Extraction used | Derived text | Visual derivative | OCR status | Reason / source content |
|---:|---|---|---|---|---|---|
| 1 | Good (5,849 characters) | Native | `normalized_text/page-001.txt` | — | Not needed | Article title, abstract, and reported results |
| 2 | Good (9,101 characters) | Native | `normalized_text/page-002.txt` | — | Not needed | Methods and outcomes |
| 3 | Good (10,634 characters) | Native | `normalized_text/page-003.txt` | `page_images/page-003.png` | Not needed | Figure 1 participant flow and results text |
| 4 | Good (9,452 characters) | Native | `normalized_text/page-004.txt` | `page_images/page-004.png` | Not needed | Table 1 and results text |
| 5 | Good (15,044 characters) | Native | `normalized_text/page-005.txt` | `page_images/page-005.png` | Not needed | Figure 2 trajectories |
| 6 | Good (10,643 characters) | Native | `normalized_text/page-006.txt` | `page_images/page-006.png` | Not needed | Table 2 and results text |
| 7 | Good (12,507 characters) | Native | `normalized_text/page-007.txt` | `page_images/page-007.png` | Not needed | Figure 3 and safety/results text |
| 8 | Good (12,300 characters) | Native | `normalized_text/page-008.txt` | `page_images/page-008.png` | Not needed | Table 3 and discussion text |
| 9 | Good (9,999 characters) | Native | `normalized_text/page-009.txt` | — | Not needed | Discussion and limitations |
| 10 | Good (14,213 characters) | Native | `normalized_text/page-010.txt` | — | Not needed | End matter and references |
| 11 | Good (5,349 characters) | Native | `normalized_text/page-011.txt` | — | Not needed | References |

## Extraction status

Complete for the audit scope. No source PDF was modified. No OCR derivative was produced because native extraction was sufficient; the required visual evidence is available as the six listed PNGs.
