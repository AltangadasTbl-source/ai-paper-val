# Direct Source Inventory

Inventory performed within the current paper package only. Source identity is established by current SHA-256 and direct `pdfinfo`; document roles are assigned from source-matched native text. No old scientific review outputs were read.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_barkin_2018_oi_180075.pdf | PDF | PDF_PAGE | 11 | REPORT | Original Investigation: Effect of a Behavioral Intervention for Underserved Preschool-Age Children on Change in Body Mass Index; randomized clinical trial methods and reported results. |
| DOC-002 | joi180075supp1_prod.pdf | PDF | PDF_PAGE | 113 | PLAN | Cover explicitly identifies original/revised protocols and amendments, original/final statistical analysis plans and amendments. All bound versions are PLAN; prospective design and historical planning material retain this role. |
| DOC-003 | joi180075supp2_prod.pdf | PDF | PDF_PAGE | 8 | REPORT | Supplementary Online Content: eTables 1–2 and eFigures 1–3 reporting trial results. Page 6 is copyright-only, confirmed by reusable rendered image. |

No direct DOC, DOCX, XLS, XLSX, or CSV sources are supplied. No source mixes REPORT and PLAN content. PDF page indexing is one-based physical PDF indexing, including covers and sparse pages. Total: 3 sources, 132 PDF_PAGE units.

Hashes are in `source_hashes_before.sha256` using package-relative paths. PDF information engine: direct Poppler `pdfinfo`; source comparison engine: direct Poppler `pdftotext`; hash engine: direct `sha256sum`. Tool availability is recorded in `tooling_record.md`.

## Downstream unit assignments

- Main mapper: DOC-001 pages 1–11, all reusable-backed.
- Support shard 1: DOC-002 pages 1–32, all reusable-backed.
- Support shard 2: DOC-002 pages 33–64, all reusable-backed.
- Support shard 3: DOC-002 pages 65–96, all reusable-backed.
- Support shard 4: DOC-002 pages 97–113 plus DOC-003 pages 1–8, all reusable-backed.

Each shard has at most 32 source pages; main text is about 61,000 bytes, plan native text about 349,000 bytes, and results supplement native text about 9,000 bytes. Page-bounded support shards stay under 200,000 normalized text characters. Mapping must inspect all assigned units, including figure graphics and sparse pages, and record result-relevant relationships. Fresh-required units: none at inventory time. Existing render gaps are derivative gaps only; direct rendering remains available if mapping identifies unreadable graphics.

## Final mapping correction

Initial all-reusable assessment was refined by detailed mapping: DOC-002 pp13,54,63,67 require fresh embedded-content inspection. Direct rendering mapped these units completely; final source partition is132 total,128 reusable,4 fresh-required,132 mapped. All initially assigned shards already contained these pages, so no page was left unassigned. Final counts are authoritative in source_coverage.md.
