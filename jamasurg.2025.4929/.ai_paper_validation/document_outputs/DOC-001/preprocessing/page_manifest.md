# Page-Level PDF Preprocessing Manifest - DOC-001

- **Source file:** `jamasurgery_dat_2025_oi_250075_1767031598.03318.pdf`
- **Document classification:** Main article.
- **Authorized scientific-audit scope:** PDF pages 1-9, following the recorded Human Compliance Review authorization dated 2026-07-21.
- **Excluded scientific scope:** PDF page 10, which begins an Invited Commentary, is **Not Audited by Design** for main-study evidence.
- **Extraction rule:** Native PDF text was extracted first for every in-scope page. Rendering and OCR were limited to pages containing the CONSORT flow diagram or a numbered results table needed by later checks.
- **Canonical text:** The native normalized text files are canonical for searchable prose. For pages 3-7, confirm flow paths, table cells, column assignment, inequalities, and symbols against the linked page image/source PDF. OCR is a noncanonical search aid only.

| Source page | Content / later-check relevance | Native extraction | Native-text quality | Rendered image | OCR | Canonical normalized text | Page-level disposition |
|---:|---|---|---|---|---|---|---|
| 1 | Title, abstract, trial identifiers, and summary results | `page-001-native.txt` (12,496 characters) | Good: complete readable title/abstract and trial summary; spacing expanded by the source text layer | Not needed | Not used | `page-001-normalized.txt` | Native text accepted |
| 2 | Introduction and methods context | `page-002-native.txt` (14,428 characters) | Good: headings and prose recovered; source spacing expanded | Not needed | Not used | `page-002-normalized.txt` | Native text accepted |
| 3 | Figure: CONSORT diagram; methods prose | `page-003-native.txt` (12,403 characters) | Good for prose and flow labels/counts; visual branch geometry requires page image | `images/page-003-consort-flow-180dpi.png` (1530 x 1980 px) | `page-003-ocr.txt`, Tesseract, page image, `--psm 6` | `page-003-normalized.txt` | Native text retained; image required for participant-flow checks; OCR noncanonical |
| 4 | Table 1, Patient Characteristics; results narrative | `page-004-native.txt` (49,318 characters) | Fair: table labels and values recoverable, but source layout has excessive spacing and degraded row/column geometry | `images/page-004-table-1-180dpi.png` (1530 x 1980 px) | `page-004-ocr.txt`, Tesseract, page image, `--psm 6` | `page-004-normalized.txt` | Native text retained; image required for Table 1 cell verification; OCR noncanonical |
| 5 | Table 2, Surgical Outcomes; morbidity results prose | `page-005-native.txt` (32,957 characters) | Fair: prose and table values recoverable, but table-column geometry is degraded | `images/page-005-table-2-180dpi.png` (1530 x 1980 px) | `page-005-ocr.txt`, Tesseract, page image, `--psm 6` | `page-005-normalized.txt` | Native text retained; image required for Table 2 cell verification; OCR noncanonical |
| 6 | Table 3, Pathological Characteristics; risk-factor results prose | `page-006-native.txt` (52,336 characters) | Fair: prose and table values recoverable, but table-column geometry is degraded | `images/page-006-table-3-180dpi.png` (1530 x 1980 px) | `page-006-ocr.txt`, Tesseract, page image, `--psm 6` | `page-006-normalized.txt` | Native text retained; image required for Table 3 cell verification; OCR noncanonical |
| 7 | Table 4, Postoperative Outcomes; discussion prose | `page-007-native.txt` (58,219 characters) | Fair: prose and table values recoverable, but table-column geometry is degraded | `images/page-007-table-4-180dpi.png` (1530 x 1980 px) | `page-007-ocr.txt`, Tesseract, page image, `--psm 6` | `page-007-normalized.txt` | Native text retained; image required for Table 4 cell verification; OCR noncanonical |
| 8 | Discussion conclusion, article information, disclosures | `page-008-native.txt` (15,509 characters) | Good: headings and prose recovered; source spacing expanded | Not needed | Not used | `page-008-normalized.txt` | Native text accepted |
| 9 | References and article-end material | `page-009-native.txt` (24,495 characters) | Good: reference entries recoverable; source spacing expanded | Not needed | Not used | `page-009-normalized.txt` | Native text accepted |
| 10 | Invited Commentary begins | Not extracted for scientific preprocessing | Not assessed for scientific extraction | Not rendered by this preprocessing stage | Not used | Not applicable | **Not Audited by Design** - excluded from main-study evidence by package manifest |

## Retained document text

`DOC-001-normalized-native-text.txt` combines normalized native text from source pages 1-9 in source-page order. Each page block states the source PDF filename, page number, and extraction method. It deliberately contains no page-10 scientific text.

## OCR quality note

The page-3 OCR recovers the CONSORT labels and counts but adds stray line/shape characters. The table-page OCRs recover most headings, row labels, and values, but may combine cells or alter punctuation, comparison symbols, and footnote markers. They are retained for searchability only; downstream checks must verify any figure path or table value with the associated image/source PDF.
