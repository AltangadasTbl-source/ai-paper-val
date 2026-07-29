# DOC-001 / Main article — preprocessing page manifest

Source PDF: `jama_engelter_2025_oi_250066_1761597796.45511.pdf` (unchanged)

Selected scientific-audit scope: PDF pages 1-10. Native text was extracted first from every selected page. `normalized_text/` is a page-preserving derivative of `native_text/` with form-feed characters and trailing whitespace removed; it retains the source page number in its filename.

| PDF page | Native text | Extraction quality | Rendered evidence | Source-page mapping |
|---:|---|---|---|---|
| 1 | `native_text/page-001.txt` | Adequate | — | PDF p1 → `normalized_text/page-001.txt` |
| 2 | `native_text/page-002.txt` | Adequate | — | PDF p2 → `normalized_text/page-002.txt` |
| 3 | `native_text/page-003.txt` | Adequate | — | PDF p3 → `normalized_text/page-003.txt` |
| 4 | `native_text/page-004.txt` | Adequate; table layout preserved as positioned text | `page_images/page-004.png` (Table 1) | PDF p4 → `normalized_text/page-004.txt` / PNG |
| 5 | `native_text/page-005.txt` | Adequate; figure/flow content needs visual inspection | `page_images/page-005.png` (Figure 1) | PDF p5 → `normalized_text/page-005.txt` / PNG |
| 6 | `native_text/page-006.txt` | Adequate; table/figure values need visual inspection | `page_images/page-006.png` (Table 2, Figure 2) | PDF p6 → `normalized_text/page-006.txt` / PNG |
| 7 | `native_text/page-007.txt` | Adequate | — | PDF p7 → `normalized_text/page-007.txt` |
| 8 | `native_text/page-008.txt` | Adequate | — | PDF p8 → `normalized_text/page-008.txt` |
| 9 | `native_text/page-009.txt` | Adequate | — | PDF p9 → `normalized_text/page-009.txt` |
| 10 | `native_text/page-010.txt` | Adequate | — | PDF p10 → `normalized_text/page-010.txt` |

OCR status: Not required. No selected main-article page had missing, sparse, or corrupted native text. The three rendered pages are retained because they contain result-relevant tables, a participant-flow diagram, or a figure.
