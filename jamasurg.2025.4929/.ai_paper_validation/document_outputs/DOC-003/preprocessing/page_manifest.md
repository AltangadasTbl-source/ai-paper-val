# Page-Level PDF Preprocessing Manifest - DOC-003

- **Source file:** `soi250075supp2_prod_1767031598.05318.pdf`
- **Document classification:** Results supplement.
- **Permitted scope:** PDF pages 1-3, following the document-level status `No AI Training Restriction Located in Provided Materials`.
- **Extraction rule:** Native PDF text was extracted first for every in-scope page. OCR and rendering were limited to the results-table page needed for later checks.
- **Canonical text:** The native normalized text files are canonical. The page-3 OCR text is retained only as a rendered-table aid and must be checked against the linked image/source PDF because OCR substituted some inequality symbols and punctuation.

| Source page | Content / later-check relevance | Native extraction | Native-text quality | Rendered image | OCR | Canonical normalized text | Page-level disposition |
|---:|---|---|---|---|---|---|---|
| 1 | Supplemental-content cover; identifies eTables 1 and 2 | `page-001-native.txt` | Good: 586 characters; title, citation, and table labels recoverable | Not needed | Not used | `page-001-normalized.txt` | Native text accepted |
| 2 | eTable 1 eligibility criteria; contextual eligibility information | `page-002-native.txt` | Good: 962 characters; all numbered inclusion/exclusion criteria recoverable | Not needed | Not used | `page-002-normalized.txt` | Native text accepted |
| 3 | eTable 2 univariate/multivariate morbidity results; required for table and statistical checks | `page-003-native.txt` | Fair: 1,667 characters; values recoverable but native reading order and table-column geometry are degraded | `images/page-003-results-table-180dpi.png` (1530 x 1980 px) | `page-003-ocr.txt`, Tesseract, page image, `--psm 6` | `page-003-normalized.txt` | Native text retained; image is required to resolve table columns; OCR is noncanonical |

## Retained document text

`DOC-003-normalized-native-text.txt` combines the three normalized page files in source-page order. Each page begins with its source filename, page number, and extraction method.

## OCR quality note for page 3

The OCR captures the table headings and most values, but converts several `>=` / `<` symbols imperfectly and introduces minor punctuation/letter substitutions. It is retained to aid searching only; later agents must use the rendered image for any value whose column or symbol matters.
