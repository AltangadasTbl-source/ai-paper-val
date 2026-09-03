# Direct-Source Inventory — Workflow 1.5.1

Inventory completed with no sibling-package or web access. Direct-source scope is all supplied PDF, DOC, DOCX, XLS, XLSX, and CSV files at the package root. No DOC, DOCX, XLS, XLSX, or CSV source was present.

| Source ID | Package-relative path | File type | Stable unit type | Units | SHA-256 | Direct-tool identity |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_kumar_2025_oi_250034_1750956984.08518.pdf | PDF 1.6, zip-deflate | PDF_PAGE | 11 | 10ab2f532b03f65d1d84bc8e8a2a3a14e3b24a76f204123acd7049d67f7b73e3 | pdfinfo: 11 pages, Letter |
| DOC-002 | joi250034supp1_prod_1750956984.09018.pdf | PDF 1.7, zip-deflate | PDF_PAGE | 26 | 4d21c2d519df3a518ed23afdba74b221ae035e19222f7230081bb63d6f28221f | pdfinfo: 26 pages, A4 |
| DOC-003 | joi250034supp2_prod_1750956984.11521.pdf | PDF 1.5 | PDF_PAGE | 29 | 413d12db69bc43aa875801ea986fb6316a4511874b393ed8a71782ddb000e5b0 | pdfinfo: 29 pages, A4 |
| DOC-004 | joi250034supp3_prod_1750956984.12018.pdf | PDF 1.6, zip-deflate | PDF_PAGE | 6 | 16131dae3f154fd78dc8058b1b4203cdeda5a26f2fe4939365651305e80e6e80 | pdfinfo: 6 pages, A4 |

Total direct-source units: **72 PDF pages**.

## Commands and versions

- `file --brief -- <each source>`; `file-5.46`.
- `pdfinfo -- <each source>`; `pdfinfo version 26.01.0`.
- `sha256sum -- <each source>`; `sha256sum (uutils coreutils) 0.8.0`.
- `pdftotext -v`; `pdftotext version 26.01.0` (version checked; no fresh scientific extraction performed by this curation stage).

## Scope note

The review contract requires complete direct-source coverage. DOC-002 and DOC-003 were historically labelled protocol/SAP and not audited in the prior workflow; that historical scope does not remove their 55 pages from this 1.5.1 coverage inventory. Their absent reusable page-level extraction is assigned as fresh-required below.
