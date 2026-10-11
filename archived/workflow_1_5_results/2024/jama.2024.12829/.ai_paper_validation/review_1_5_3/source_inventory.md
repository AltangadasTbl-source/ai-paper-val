# Direct Source Inventory

This inventory was created from the supplied package root with `file`, `pdfinfo`, and SHA-256. No source was modified. A direct-source unit is one physical PDF page; no Office or CSV source was present.

| Source ID | Package-relative source path | Format and stable unit type | Total units | Text layer | SHA-256 | Direct-tool result |
|---|---|---|---:|---|---|---|
| DOC-001 | jama_sun_2024_oi_240088_1746815064.14747.pdf | PDF, `PDF_PAGE` | 11 | Available; not encrypted | af8f0e97daf2e2dfc4bb52a52e97246655498c1632d1743047fee02bef51a13a | PDF 1.4; letter pages; `pdfinfo` reports 11 pages. |
| DOC-002 | joi240088supp1_prod_1746815064.21247.pdf | PDF, `PDF_PAGE` | 25 | Available; not encrypted | 4cc1cb72c622145ddb5781a4a579b51747085fe231630b3c6ce58618d1b8a635 | PDF 1.6; letter pages; `pdfinfo` reports 25 pages. |
| DOC-003 | joi240088supp2_prod_1746815064.36071.pdf | PDF, `PDF_PAGE` | 167 | Available; tagged; not encrypted | bd80ae9cde96500aa9c8b5f8d862e4b3f3e933f1ac1c82835fbf7cfde46ca0bb | PDF 1.5; letter pages; `pdfinfo` reports 167 pages. |

**Counts:** 3 direct sources and 203 unique direct-source page units. The complete pre-review source hashes are in `source_hashes_before.sha256`.

**Source-unit mapping requirement:** DOC-001 pages 1-11 are reuse-backed. DOC-002 pages 1-2 and 10-25 are reuse-backed, while pages 3-9 require fresh direct-source mapping. DOC-003 pages 1-167 require fresh direct-source mapping. Thus, reusable and fresh-required units partition all 203 direct-source units.
