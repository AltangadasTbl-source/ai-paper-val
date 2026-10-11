# Direct-source inventory

All direct PDF, DOC, DOCX, XLS, XLSX, and CSV files in the current package were inventoried. There are four direct PDFs and no direct Office or CSV sources. Supplied source identity was established by `pdfinfo` and `sha256sum`; content roles were established from directly extracted title/front pages. Source IDs retain the existing identity convention while every page enters the new review.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis and complete scope |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_thille_2019_oi_190108.pdf | PDF | PDF_PAGE | 11 | REPORT | PDF p.1 identifies JAMA Original Investigation and the randomized clinical trial. Main article, PDF pp.1-11, including appended material. |
| DOC-002 | joi190108supp1_prod.pdf | PDF | PDF_PAGE | 48 | PLAN | PDF pp.1-2 identify HIGH-WEAN study, version 4 dated 17 October 2017, and clinical trial protocol; prospective protocol and appendices, PDF pp.1-48. No REPORT bundle identified. |
| DOC-003 | joi190108supp2_prod.pdf | PDF | PDF_PAGE | 9 | REPORT | PDF p.1 lists eTables 1-5 and the survival eFigure, presented as additional results material; PDF pp.1-9. |
| DOC-004 | joi190108supp3_prod.pdf | PDF | PDF_PAGE | 1 | REPORT | PDF p.1 is a retrospective data-sharing statement accompanying the published report; administrative REPORT content, no prospective statistical plan. Entire PDF p.1 must be mapped even if it contains no applicable quantitative relationship. |

Total: 69 unique PDF_PAGE units. Hashes are recorded in `source_hashes_before.sha256` with package-relative paths.

Tooling: direct `pdfinfo` and `pdftotext` Poppler 26.01.0; direct `sha256sum`. No fallback helper, Python extraction, Office conversion, OCR execution, external source, or sibling package was used for this inventory.

Historical scope exclusions in reused document records and manifests are metadata only and do not limit this run. All four sources receive complete fresh reasoning and mapping. No earlier candidate, checker, screening, classification, adjudication, or final report was read as discovery input.
