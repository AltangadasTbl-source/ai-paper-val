# Direct Source Inventory

Inventory method: package-root filename inventory, `pdfinfo`, and SHA-256 verification. No direct source was changed. A source unit is one PDF page. All supplied direct sources are included regardless of legacy audit labels.

| Source ID | Package-relative source path | Format | Stable units | SHA-256 | Direct-source fitness | Exact unit locations | Reuse/fresh coverage summary |
|---|---|---|---:|---|---|---|---|
| DOC-001 | jama_courcoulas_2024_oi_240004_1721756962.76052.pdf | PDF | 11 PDF pages | 0f153cf27727015b19cf33ba400d4c0cc36e20f58a1b85c08f74bd61f1d06647 | USABLE | PDF pp. 1-11 | Reusable native layout text covers pp. 1-11; rendered pages additionally cover pp. 3-8. |
| DOC-002 | joi240004supp1_prod_1721756962.80052.pdf | PDF | 65 PDF pages | 75275168ca11fb55b11821a0a07067812181adfe0ccc4487e04ff2a0673f2958 | USABLE | PDF pp. 1-65 | No reusable page-level extraction or rendering exists; all pages require fresh direct-source mapping. |
| DOC-003 | joi240004supp2_prod_1721756962.82552.pdf | PDF | 22 PDF pages | 4c2e87ee8ac1bcde5927e63f7b27ade27ace05dae1b6085dc81cb293c56afd81 | USABLE | PDF pp. 1-22 | Reusable native layout text and rendered pages cover pp. 8-22; pp. 1-7 require fresh direct-source mapping. |
| DOC-004 | joi240004supp3_prod_1721756962.84052.pdf | PDF | 1 PDF page | cfdde1a6a79f4b81980f2a69b095d9c0fed24c77759968078fffecd5f26979f8 | USABLE | PDF p. 1 | No reusable page-level extraction or rendering exists; p. 1 requires fresh direct-source mapping. |

Totals: 4 direct PDFs; 99 unique PDF-page units. No DOC, DOCX, XLS, XLSX, or CSV direct source is present in this paper package.

## Direct-source mapping requirement

All 99 pages have a mapping route. Reusable-backed mapping applies to DOC-001 pp. 1-11 and DOC-003 pp. 8-22 (26 units). Fresh direct-source mapping is mandatory for DOC-002 pp. 1-65, DOC-003 pp. 1-7, and DOC-004 p. 1 (73 units). The subsequent mappers must inspect source PDFs for every fresh-required unit and confirm exact source pages for any evidence used.
