# Page-Level Preprocessing Manifest

- Document ID: `DOC-JAMA2024-6063-MAIN-2f574565`
- Source PDF: `jama_laslett_2024_oi_240048_1727199125.7595.pdf`
- Source-page convention: `PDF page` is the one-based physical page in the source PDF.
- Native extractor: `pdftotext -layout`; normalization removed CR and form-feed characters only, preserving table layout and text order.
- Quality decision: all selected pages have substantial, legible native text; no page needed OCR. The terminal form-feed emitted by the extractor is a normal page delimiter, not text corruption.
- Rendered images: 200 dpi PNGs were retained only for downstream review of required tables, figures, and participant flow.

| PDF page | Audit status | Native-text quality | Final extraction method | Normalized text | Rendered page image | Reason / source content |
|---:|---|---|---|---|---|---|
| 1 | Selected | Good (5,365 native characters; readable title/abstract) | Native | `normalized_text/page-001.txt` | — | Article title, abstract, key result text |
| 2 | Selected | Good (8,533; readable body text) | Native | `normalized_text/page-002.txt` | — | Methods and trial context |
| 3 | Selected | Good (8,018; readable flow labels/body text) | Native | `normalized_text/page-003.txt` | `page_images/page-003.png` | Figure 1 participant flow requires visual check |
| 4 | Selected | Good (8,283; readable body text) | Native | `normalized_text/page-004.txt` | — | Outcomes and analysis methods |
| 5 | Selected | Good (11,317; structured table text) | Native | `normalized_text/page-005.txt` | `page_images/page-005.png` | Table 1 baseline characteristics |
| 6 | Selected | Good (19,887; structured table text) | Native | `normalized_text/page-006.txt` | `page_images/page-006.png` | Table 2 study end points |
| 7 | Selected | Good (9,912; readable figure labels/body text) | Native | `normalized_text/page-007.txt` | `page_images/page-007.png` | Figure 2 knee-pain plot |
| 8 | Selected | Good (10,246; structured table text) | Native | `normalized_text/page-008.txt` | `page_images/page-008.png` | Table 3 adverse events |
| 9 | Selected | Good (12,010; readable discussion/conclusion text) | Native | `normalized_text/page-009.txt` | — | Conclusions and limitations |
| 10 | Not Audited by Design | Not assessed | Not extracted | — | — | Outside parent-specified main-article scope (pages 1–9) |

OCR was not used: every selected page retained a usable native text layer, including the table and figure-caption text; visual images were kept where image-level checking adds evidence unavailable from the text layer.
