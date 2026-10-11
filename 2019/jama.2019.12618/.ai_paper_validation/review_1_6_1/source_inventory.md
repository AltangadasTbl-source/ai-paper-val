# Direct-source inventory

Inventory is limited to the current paper package. Recursive extension inventory found five direct PDFs and no DOC, DOCX, XLS, XLSX or CSV source. Poppler pdfinfo 26.01.0 established page counts; direct pdftotext 26.01.0 page-one headings established roles by content. All files are unencrypted. Legacy discovery scopes are not adopted.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content-based role and bundle description |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_rathinam_2019_oi_190092.pdf | PDF | PDF_PAGE | 10 | REPORT | Original Investigation reporting the randomized FAST uveitis trial; full article including references. |
| DOC-002 | joi190092supp1_prod.pdf | PDF | PDF_PAGE | 16 | REPORT | Non-plan supplementary results with eligibility, adverse-event definitions, dose guidance, enrollment and adverse-event tables and primary-outcome homogeneity tests. Contextual method content belongs to this results supplement. |
| DOC-003 | joi190092supp2_prod.pdf | PDF | PDF_PAGE | 153 | PLAN | Original protocol, final protocol/manual of operations and summary of changes; multiple plan versions within one bound plan bundle. No independent results report identified. |
| DOC-004 | joi190092supp3_prod.pdf | PDF | PDF_PAGE | 83 | PLAN | Original and final statistical analysis plans and summary of changes; multiple plan versions within one bound plan bundle. |
| DOC-005 | joi190092supp4_prod.pdf | PDF | PDF_PAGE | 1 | REPORT | Data Sharing Statement supplied with the article; administrative report-associated content, not a prospective statistical protocol or SAP. It will be mapped with no applicable quantitative relationship if source content warrants that conclusion. |

Total: 263 unique PDF_PAGE units. Stable IDs follow main article, results supplement, protocol, SAP, then administrative statement. No REPORT/PLAN mixed bundle identified; the protocol and SAP contain multiple PLAN versions.

## Reproducible commands and integrity

- `find . -type f` with case-insensitive direct-source extension filters, excluding workflow controls and .git/.codex, established the complete source set.
- `pdfinfo "SOURCE.pdf"` established each stable page count.
- `pdftotext -layout -f 1 -l 1 "SOURCE.pdf" -` established role evidence from source headings.
- `sha256sum -- "SOURCE.pdf"` established hashes in source_hashes_before.sha256 with package-relative paths.

No source was modified. No scientific candidate diagnosis was performed during this stage.
