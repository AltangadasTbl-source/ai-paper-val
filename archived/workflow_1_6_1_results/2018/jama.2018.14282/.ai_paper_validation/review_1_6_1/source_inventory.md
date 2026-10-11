# Direct Source Inventory

Scope: every direct PDF, DOC, DOCX, XLS, XLSX, and CSV file within the current package. Four supplied PDFs were found; no Office, workbook, or CSV sources exist. No sibling package or external evidence was inspected. Document roles derive from source content.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content and identity |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_azoulay_2018_oi_180109.pdf | PDF | PDF_PAGE | 9 | REPORT | HIGH randomized trial article: reported outcomes, tables, figures, methods, discussion, references. |
| DOC-002 | joi180109supp1_prod.pdf | PDF | PDF_PAGE | 129 | PLAN | Bound initial/final protocol versions and original/final statistical analysis plans; contents p.1 identifies each plan section. All versions remain PLAN; no REPORT/PLAN mixed bundle. |
| DOC-003 | joi180109supp2_prod.pdf | PDF | PDF_PAGE | 5 | REPORT | Non-plan supplementary oxygenation/ventilation table and three outcome figures, with cover p.1. |
| DOC-004 | joi180109supp3_prod.pdf | PDF | PDF_PAGE | 1 | REPORT | Publication data-sharing statement; administrative report content. |

Stable unit count: 144 unique PDF pages, including covers, administrative pages and references. Direct pdfinfo confirmed page counts; sha256sum records identities in source_hashes_before.sha256. Every page's native and layout extraction was compared against the current source with direct pdftotext 25.03.0; 143 native and 140 layout pages matched byte-for-byte. DOC-002 p.11 matches after whitespace normalization; its difference is line wrapping. DOC-003 pp.3-5 layout variations relocate figure labels without changing printed tokens; native text matches byte-for-byte. The original asset engine was Poppler pdftotext, version not recorded in eligible metadata; current confirmation engine is Poppler 25.03.0. Rendered assets use PNG page coordinates and explicit document/page filenames; prior rendering engine inferred as Poppler from standard naming and page-register metadata, version unavailable.

Scientific mapping was pending at inventory handoff and is now complete in the main/support mapper artifacts and source_coverage.md. Inventory does not inherit legacy page relevance or scientific conclusions. Exact source pages remain authoritative.
