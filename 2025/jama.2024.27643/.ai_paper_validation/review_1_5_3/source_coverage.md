# Direct-Source Coverage

Stable units are physical PDF pages, established with `pdfinfo` against every supplied direct PDF. A reusable unit has a source-matched usable native-text or page-location asset. A fresh-required unit has no such usable extraction and is assigned to fresh direct-source mapping. “Mapped units” records the complete planned partition for downstream mappers; all fresh-required units must be directly extracted and mapped before scientific review completes.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_berry_2025_oi_240158_1742927563.7361.pdf | PDF_PAGE | 12 | 12 | 0 | 12 | COMPLETE |
| DOC-002 | joi240158supp1_prod_1742927563.7611.pdf | PDF_PAGE | 229 | 0 | 229 | 229 | COMPLETE |
| DOC-003 | joi240158supp2_prod_1742927563.7711.pdf | PDF_PAGE | 130 | 0 | 130 | 130 | COMPLETE |
| DOC-004 | joi240158supp3_prod_1742927563.7911.pdf | PDF_PAGE | 26 | 26 | 0 | 26 | COMPLETE |
| DOC-005 | joi240158supp4_prod_1742927563.8061.pdf | PDF_PAGE | 6 | 0 | 6 | 6 | COMPLETE |
| DOC-006 | joi240158supp5_prod_1742927563.8111.pdf | PDF_PAGE | 1 | 0 | 1 | 1 | COMPLETE |

## Exact unit partition and downstream assignment

| Source ID | Reusable-backed units | Fresh-required units | Downstream mapper assignment | Coverage note |
|---|---|---|---|---|
| DOC-001 | PDF pp. 1-12 | None | main quantitative mapper: reuse native text for PDF pp. 1-12; use retained rendered pages 5-8 for visual confirmation | Page-native text and page manifest are source-matched and usable for every page. |
| DOC-002 | None | PDF pp. 1-229 | support quantitative mapper: fresh direct native/layout extraction and page mapping for PDF pp. 1-229 | Existing document record is inventory metadata only and does not provide page-level content extraction. |
| DOC-003 | None | PDF pp. 1-130 | support quantitative mapper: fresh direct native/layout extraction and page mapping for PDF pp. 1-130 | Existing document record is inventory metadata only and does not provide page-level content extraction. |
| DOC-004 | PDF pp. 1-26 | None | support quantitative mapper: reuse native text for PDF pp. 1-26; use retained rendered pages 14-25 for visual confirmation | Pages 1-25 have usable scientific native text; page 26 has usable sparse rights/end matter confirming no result content. |
| DOC-005 | None | PDF pp. 1-6 | support quantitative mapper: fresh direct native/layout extraction and page mapping for PDF pp. 1-6 | Existing document record is inventory metadata only and does not provide page-level content extraction. |
| DOC-006 | None | PDF p. 1 | support quantitative mapper: fresh direct native/layout extraction and page mapping for PDF p. 1 | Existing document record is inventory metadata only and does not provide page-level content extraction. |

## Counts and gaps

- Unique direct sources: 6.
- Unique stable source units: 404 PDF pages.
- Reusable-backed units: 38 pages (DOC-001 pp. 1-12; DOC-004 pp. 1-26).
- Fresh-required units: 366 pages (DOC-002 pp. 1-229; DOC-003 pp. 1-130; DOC-005 pp. 1-6; DOC-006 p. 1).
- Mapped planned units: 404 pages; reusable plus fresh-required equals total for every source.
- There are no supplied DOC, DOCX, XLS, XLSX, or CSV direct sources and no supplied workbook/table-extraction assets.
- Reusable-derivative gaps: DOC-002, DOC-003, DOC-005, and DOC-006 lack page-level text, OCR, rendered-page, or table extraction. Their complete page ranges are fresh-required; no scientific-coverage gap is accepted.
