# Direct-source inventory

Complete package-only enumeration found four PDFs and no DOC, DOCX, XLS, XLSX, or CSV sources. Stable units are physical PDF pages, including covers, bibliography, administrative pages, scanned pages, and linked-document pointer pages. No external linked documents were fetched. Hashes use SHA-256 with package-relative paths in source_hashes_before.sha256.

| Source ID | Source path | Format | Document role | Total units | Exact scope and content basis |
|---|---|---|---|---:|---|
| DOC-001 | jama_cooper_2018_oi_180132.pdf | PDF | REPORT | 10 | PDF pp. 1–10; completed randomized trial article, abstract, tables, figures, methods and results. |
| DOC-002 | joi180132supp1_prod.pdf | PDF | PLAN | 194 | PDF pp. 1–194; protocol versions, protocol amendments, published protocol pointer, SAP pointers and update scans, DSMC charter/stopping rules and operational monitoring reports. Bound plan bundle, including prospective monitoring decisions; no separate final-outcome results supplement within it. |
| DOC-003 | joi180132supp2_prod.pdf | PDF | REPORT | 24 | PDF pp. 1–24; supplementary results, eTables 1–13 and eFigures 1–7, per-protocol, as-treated and post hoc results. |
| DOC-004 | joi180132supp3_prod.pdf | PDF | REPORT | 1 | PDF p. 1; retrospective publication data-sharing statement, not a prospective statistical analysis plan. |

Inventory engine: direct pdfinfo 25.03.0; role confirmed by direct pdftotext first-page content and source-linked full native-text structural headings. SHA engine: sha256sum. All sources are unencrypted. Complete total: 229 PDF_PAGE units.

## Source locations and mapper assignment

DOC-001 main mapping: pp. 1–10. Support mapping: DOC-002 pp. 1–194, DOC-003 pp. 1–24, DOC-004 p. 1. Every physical page requires new scientific mapping, even when reusable extraction is complete.

DOC-002 structural subdivisions: p. 1 contents; pp. 2–51 original protocol; p. 52 published-protocol pointer; pp. 53–138 final protocol; pp. 139–180 amendments and associated appendices; pp. 181–187 published SAP pointer, SAP update and correction; pp. 188–194 DSMC stopping rules and reports. The supplied pointer pages are covered as supplied; external linked content is outside the supplied package.

For context bounds, split the plan mapping into disjoint pp. 1–52, 53–83, 84–138, 139–194; layout-character burdens respectively 130466, 111596, 151366 and 51110 before normalization. Target visual review where text is absent or only headers: pp. 104, 105, 127, 140–162, 183–185, 187. The pp. 139–194 shard contains 27 textless pages; no shard requires more than 32 rendered-page inputs when text-bearing pages use text locators. If a mapper exceeds 120 relationships, use additional disjoint relationship shards rather than truncation.

## Embedded-location role qualification

DOC-002 retains the overall document role PLAN because it is the supplied bound protocol/SAP/monitoring package. The fresh evidence rechecker distinguishes observed DSMB result displays on pp.189–194 as REPORT content for location-specific candidate classification. This exception follows the normative content rule rather than the file name. Prospective charter and stopping rules remain PLAN. The independent quality audit will review the exception.
