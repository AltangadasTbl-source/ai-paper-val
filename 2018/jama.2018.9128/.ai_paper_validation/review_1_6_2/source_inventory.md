# Direct-source inventory

Inventory scope is this paper package only. All direct PDF, DOC, DOCX, XLS, XLSX, and CSV paths were searched, including hidden paths; exactly three direct PDFs and no Office or CSV sources were found. Derivative images/text are not direct sources. No legacy discovery or decision artifact was read.

| Source ID | Source path | Format | Document role | Total units | Unit type | Content basis |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_barkin_2018_oi_180075.pdf | PDF | REPORT | 11 | PDF_PAGE | Original investigation reporting the randomized trial and results. |
| DOC-002 | joi180075supp1_prod.pdf | PDF | PLAN | 113 | PDF_PAGE | Cover states original/revised protocol, original/final statistical analysis plan, and summaries of amendments; this is a bundle of plan versions and prospective operational material, not a REPORT/PLAN mixed bundle. |
| DOC-003 | joi180075supp2_prod.pdf | PDF | REPORT | 8 | PDF_PAGE | Supplementary online content containing eTables and eFigures of trial results. |

Stable units are physical PDF pages 1 through the listed total, including cover, contents, appendices, references, and sparse pages. Physical page and printed-page identifiers are retained separately by downstream mappers. Total unique direct-source units: 132. Direct-source SHA-256 hashes are recorded using package-relative paths in source_hashes_before.sha256.

Engines: direct Poppler pdfinfo and pdftotext version 25.03.0; direct sha256sum. Commands: `pdfinfo "SOURCE.pdf"`, `pdftotext "SOURCE.pdf" -`, and `sha256sum -- "SOURCE.pdf"`. Reuse matching used `cmp -s` on direct pdftotext output. No new derivative or fallback environment was needed for inventory.

Mapping assignments: DOC-001 pp. 1-11 main mapper; DOC-002 pp. 1-55 support mapper shard 1; DOC-002 pp. 56-113 support mapper shard 2; DOC-003 pp. 1-8 support mapper shard 1. These disjoint scopes partition all 132 units. Every unit remains subject to new quantitative mapping.
