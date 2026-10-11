# Workflow 1.6 Direct-Source Inventory

Inventory is confined to this paper package. Every supplied PDF, DOC, DOCX, XLS, XLSX, and CSV was sought recursively; the only direct sources are the three PDFs below. There are no Office or CSV sources. Unit counts were read using direct Poppler pdfinfo 25.03.0. SHA-256 was computed with direct sha256sum and is recorded using package-relative paths in source_hashes_before.sha256.

| Source ID | Source path | Format | Stable units | Document role | Content basis and exact scope |
|---|---|---|---:|---|---|
| DOC-001 | jama_jabre_2018_oi_180004.pdf | PDF | 9 PDF_PAGE | REPORT | Published main trial article, PDF pp. 1-9, containing abstract, reported outcomes, tables, figures, discussion and references. |
| DOC-002 | joi180004supp1_prod.pdf | PDF | 134 PDF_PAGE | PLAN | Bound original/final protocol, amendments and statistical analysis plans. PDF p. 1 contents; pp. 2-56 initial protocol and operational annexes; pp. 57-107 later protocol; pp. 108-116 amendments/change documents; pp. 117-125 English SAP; pp. 126-134 further plan material needing OCR or visual reading. Historical/background quantitative data inside this bundle remain PLAN. No REPORT results section is identified. |
| DOC-003 | joi180004supp2_prod.pdf | PDF | 3 PDF_PAGE | REPORT | Non-plan supplementary reported results: p. 1 cover, p. 2 centre contributions eTable 1, p. 3 post-hoc analyses eTable 2. |

Role assignments are grounded in content, including the bound supplement's contents and protocol/SAP titles, rather than supplement number. No mixed REPORT/PLAN bundle was identified. All sources are unencrypted and can be directly rendered.

## Inventory commands and evidence identity

`pdfinfo "source.pdf"` supplied complete page counts 9, 134 and 3. Direct native and layout extraction to stdout with `pdftotext "source.pdf" -` and `pdftotext -layout "source.pdf" -` was SHA-256 compared with the six reused native/layout files; all six are byte-identical. These comparisons establish current-source identity without creating replacement derivatives. Full page-segment enumeration used form-feed separators and checked all 146 page units.

The native/layout DOC-002 text is sparse on p. 52 and empty on pp. 108, 109, 126-134. Source-hash-matched existing OCR and rendered images cover p. 52, pp. 108-109 and pp. 126-133. Only p. 134 has no usable reused derivative and must be directly rendered and mapped by the support mapper. Empty extracted text is not evidence that the PDF page is blank.
