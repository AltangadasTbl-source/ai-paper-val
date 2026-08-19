# Direct Source Inventory

This inventory covers every direct PDF source found at the package root. No DOC, DOCX, XLS, XLSX, or CSV direct source was present. Page counts were established with `pdfinfo`; identities were checked against the source PDF metadata and the existing package manifest. Direct sources were read only.

| Source ID | Package-relative source path | Type | Stable identity | Units | Direct-source SHA-256 | Text-layer result | Coverage decision |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_wilson_2020_oi_190154.pdf | PDF | Main article; JAMA Original Investigation | 11 PDF pages | 4786726a6b91df3e168d0f90afb52c3999f4aafe4283d767028ba364ec0cb0a2 | Extractable native text on 11 of 11 pages | Existing native page text is usable for pages 1-11. |
| DOC-002 | joi190154supp1_prod.pdf | PDF | Supplementary Online Content; Trial Protocol | 15 PDF pages | 04c91bf1e28f2e8948e128736028716a7f2c716ca288424f04176889f0bd228e | Extractable native text on 15 of 15 pages | No reusable scientific extraction covered any page; all pages freshly extracted in this run. |
| DOC-003 | joi190154supp2_prod.pdf | PDF | Supplementary Online Content; results supplement | 49 PDF pages | 76c413481a77777146f9468094dde137e001b0cb3d9ef2e2020bd4d25074b001 | Extractable native text on 49 of 49 pages | Existing native page text is usable for pages 17-45. Pages 1-16 and 46-49 were freshly extracted in this run. |

## Stable-unit accounting

- Unique direct sources: 3.
- Unique direct-source units: 75 PDF pages.
- Reusable-covered units: 40 PDF pages.
- Fresh-required units at inventory: 35 PDF pages.
- Direct-source identity and page-count tool: `pdfinfo` from the local environment.
- Direct-source hashing tool: `sha256sum` from the local environment.

The source hashes are recorded separately in `source_hashes_before.sha256`. No direct source was modified.
