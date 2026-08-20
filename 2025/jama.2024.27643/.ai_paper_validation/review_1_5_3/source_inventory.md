# Direct Source Inventory

Inventory method: package-root direct-file scan limited to PDF, DOC, DOCX, XLS, XLSX, and CSV; `file` and `pdfinfo` for supplied PDFs; SHA-256 recorded in `source_hashes_before.sha256`. No web or sibling package was inspected. No legacy candidate, verifier, critic, endetail, quality, queue, disposition, or final-report content was used as discovery scope.

| Source ID | Package-relative source path | Format | Stable units | Direct-tool result | Reusable evidence coverage | Fresh-required exact units |
|---|---|---|---:|---|---|---|
| DOC-001 | jama_berry_2025_oi_240158_1742927563.7361.pdf | PDF 1.4, unencrypted, letter pages | 12 PDF pages | `pdfinfo`: 12 pages; native text layer confirmed by reusable page-native extraction | USABLE: native page text and page manifest for pp. 1-12; rendered pages 5-8 for layout confirmation | None |
| DOC-002 | joi240158supp1_prod_1742927563.7611.pdf | PDF 1.7, unencrypted, letter pages | 229 PDF pages | `pdfinfo`: 229 pages; existing record reports a text layer but no reusable page extraction | PARTIAL: document record only, with classification metadata from pp. 1-3 | PDF pp. 1-229 |
| DOC-003 | joi240158supp2_prod_1742927563.7711.pdf | PDF 1.3, unencrypted, letter pages | 130 PDF pages | `pdfinfo`: 130 pages; existing record reports a text layer but no reusable page extraction | PARTIAL: document record only, with classification metadata from pp. 1-3 | PDF pp. 1-130 |
| DOC-004 | joi240158supp3_prod_1742927563.7911.pdf | PDF 1.7, unencrypted, letter pages | 26 PDF pages | `pdfinfo`: 26 pages; native page text reviewed for pp. 1-26 | USABLE: native page text and page manifest for pp. 1-26; rendered pages 14-25 for layout confirmation | None |
| DOC-005 | joi240158supp4_prod_1742927563.8061.pdf | PDF 1.7, unencrypted, 965.85 × 746.34 pt pages | 6 PDF pages | `pdfinfo`: 6 pages; existing record reports a text layer but no reusable page extraction | PARTIAL: document record only, with classification metadata from pp. 1-3 | PDF pp. 1-6 |
| DOC-006 | joi240158supp5_prod_1742927563.8111.pdf | PDF 1.4, unencrypted, A4 pages | 1 PDF page | `pdfinfo`: 1 page; existing record reports a text layer but no reusable page extraction | PARTIAL: document record only, with classification metadata from p. 1 | PDF p. 1 |

## Direct-source totals

- Direct-source files: 6 PDFs; 0 DOC; 0 DOCX; 0 XLS; 0 XLSX; 0 CSV.
- Stable source-unit total: 404 PDF pages.
- Reusable-backed source units: 38 pages.
- Fresh-required source units: 366 pages.
- Source identity and before-review integrity: all six SHA-256 values are recorded with package-relative paths in `source_hashes_before.sha256`.

## Fitness and limitations

DOC-001 and DOC-004 have complete, source-matched page-native coverage. The retained PNG renders are usable visual companions for layout-intensive pages, not replacements for direct PDFs. DOC-002, DOC-003, DOC-005, and DOC-006 have only document-level inventory records; those records are PARTIAL and do not cover page content. No reusable OCR, layout-text-only, table extraction, workbook extraction, Office source, or CSV source exists. Every uncovered page is explicitly assigned for fresh direct-source mapping in `source_coverage.md`.
