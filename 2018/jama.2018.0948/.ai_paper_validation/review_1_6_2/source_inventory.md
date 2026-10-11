# Workflow 1.6.2 Direct-Source Inventory

Scope: the current paper package only. Four direct PDFs are supplied; no direct DOC, DOCX, XLS, XLSX, or CSV source exists. Document roles follow content, not supplement numbering. Unit counts were confirmed with direct `pdfinfo` (Poppler 25.03.0); SHA-256 uses direct `sha256sum`. No source or legacy artifact was modified.

| Source ID | Source path | Format | Total stable units | Unit type | Document role | Content basis | Mapping assignment |
|---|---|---|---:|---|---|---|---|
| DOC-001 | jama_parshuram_2018_oi_180015.pdf | PDF | 11 | PDF_PAGE | REPORT | Published EPOCH randomized trial article, abstract, methods, participant flow, results, tables and references | Main mapper, PDF pp. 1-11 |
| DOC-002 | joi180015supp1_prod.pdf | PDF | 37 | PDF_PAGE | PLAN | Research protocol, prospective outcomes, trial methods, sample size and operational appendices | Support mapper, PDF pp. 1-37 |
| DOC-003 | joi180015supp2_prod.pdf | PDF | 7 | PDF_PAGE | PLAN | EPOCH SAP; analysis plan, GEE models and analysis code | Support mapper, PDF pp. 1-7 |
| DOC-004 | joi180015supp3_prod.pdf | PDF | 14 | PDF_PAGE | REPORT | Supplementary online results, eFigures 1-2 and eTables 1-5 | Support mapper, PDF pp. 1-14 |

No mixed REPORT/PLAN source bundle was identified. DOC-002 includes operational plan appendices; DOC-004's outcome-definition tables accompany results and do not turn it into a prospective plan.

## Extraction identity and context sizes

All eight existing native/layout text files contain one form-feed-delimited record per PDF page. They cover all 69 source pages. Native text matches current direct extraction byte-for-byte for DOC-001, DOC-002 and DOC-003. Layout text matches byte-for-byte for DOC-002 and DOC-003. DOC-001 layout differs only in ordering/whitespace and has an identical token multiset. DOC-004 differences are graphic-label ordering and the split of `2per` into `2` and `per` on PDF p. 2; its existing rendered p. 2 provides readable visual evidence. The exact source remains final authority.

| Source ID | Native characters | Layout characters | Source scope |
|---|---:|---:|---|
| DOC-001 | 64405 | 119548 | PDF pp. 1-11 |
| DOC-002 | 134434 | 145785 | PDF pp. 1-37 |
| DOC-003 | 10527 | 12950 | PDF pp. 1-7 |
| DOC-004 | 25732 | 41722 | PDF pp. 1-14 |

Character counts use direct `wc -m`. Each source is below the 200000 normalized-text-character shard bound when a single native or layout representation is supplied; do not combine overlapping native and layout representations into an oversized shard. The support union exceeds that bound and must be split by direct source or bounded page scopes. The 37-page protocol exceeds the rendered-page bound if all pages are displayed in one shard; use targeted rendering or disjoint visual scopes of at most 32 pages.
