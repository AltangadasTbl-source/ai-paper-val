# Direct-Source Inventory — Workflow 1.5.1

## Inventory basis

This inventory covers every supplied direct PDF in the package root. No DOC, DOCX, XLS, XLSX, or CSV direct source is present. Counts are stable PDF-page units obtained with `pdfinfo`; source hashes are recorded in `source_hashes_before.sha256`.

| Source ID | Package-relative path | File type | PDF pages / stable units | Text-layer observation | SHA-256 |
|---|---|---|---:|---|---|
| DOC-001 | jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf | PDF | 11 | Native text layer present and readable in the reusable page records. | `8bec9f9aefd9a033e0758d29ec41e064d9860aa5dd865e5020596488b9947920` |
| DOC-002 | joi250084supp1_prod_1765403089.61351.pdf | PDF | 90 | Native layer is present but prior page-record metadata describes sampled content as glyph-encoded; no page-level reusable extraction exists. | `f1d9b84740da4218ae58ade4c5e0db3d3586d1eefd6615121f856bda7900b82b` |
| DOC-003 | joi250084supp2_prod_1765403089.61751.pdf | PDF | 69 | Native text layer is present; reusable native/OCR/image assets cover a partial, disjoint page set. | `7f14f61d2055fa1972417bc25634c5eaed3f3a36722ecc437418efbc61e05b35` |

**Total direct-source units:** 170 PDF pages.

## Direct-source tool record

- `pdfinfo` confirmed 11, 90, and 69 pages respectively; all three PDFs are unencrypted letter-size PDFs.
- `sha256sum` was run on the three direct sources before scientific mapping. The direct PDFs were read only.
- There are no supplied Office workbooks, word-processing documents, or CSV files to inventory.

## Stable-unit convention

Each PDF page is one source unit. The source IDs above remain stable even though the pre-existing audit area uses longer document-directory labels. The reusable-evidence partition and unassigned fresh ranges are in `source_coverage.md`; asset-level provenance and fitness are in `evidence_asset_inventory.md`.
