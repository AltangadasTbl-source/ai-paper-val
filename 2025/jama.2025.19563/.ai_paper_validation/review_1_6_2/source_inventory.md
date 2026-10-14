# Direct-source inventory

All direct PDF, DOC, DOCX, XLS, XLSX, and CSV files in the current package were inventoried. Three direct PDFs were located; no direct Office or CSV sources were supplied. Stable units are PDF pages; every page enters downstream mapping, irrespective of prior scope restrictions. Sources remain unchanged.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis | Mapping scope |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf | PDF | PDF_PAGE | 11 | REPORT | JAMA Original Investigation reporting the randomized trial | pp. 1-11 |
| DOC-002 | joi250084supp1_prod_1765403089.61351.pdf | PDF | PDF_PAGE | 90 | PLAN | Protocol IRB00265873, versions, statistical analysis material, and amendment/change documentation; p. 76 begins Summary of Changes to Protocol | pp. 1-90 |
| DOC-003 | joi250084supp2_prod_1765403089.61751.pdf | PDF | PDF_PAGE | 69 | REPORT | Supplement 2 contains eMethods, eFigures, eTables, and references supporting reported analyses | pp. 1-69 |

Document role is assigned from content rather than supplement numbering. DOC-002 is a bound plan bundle: amendment/change tables may describe implementation and analyses retrospectively. Mappers must distinguish any REPORT passage by content and record the precise boundary if encountered; the bundle's plan versions remain PLAN. No independent REPORT document embedded in the bundle has been established by the inventory inspection.

## Source identity and engines

Page counts independently confirmed with `/home/juliz/venvs/stt/bin/python workflow_1_6_2/scripts/pdf_tools.py info <source>` (PyMuPDF 1.28.0 fallback for unavailable pdfinfo). All PDFs are unencrypted. SHA-256 is recorded in source_hashes_before.sha256 using direct sha256sum and package-relative paths. Source text/image identities agree with the preserved package and preprocessing manifests. No old scientific conclusions were used as discovery input.

## Context planning

Main article native text: 58,292 Unicode characters across 11 unique page files. Results supplement preferred unique-page native text is 103,297 Unicode characters across all 69 pages, supporting one text-backed mapping assignment if visual pages are divided into bounded groups. DOC-002 native/layout text is glyph-encoded and not a useful character burden; 90 retained full-page PNGs, of which four required direct-source replacement after decoder checks, require three separate visual shards: pp. 1-30, 31-60, 61-90. Every visual shard is within the 32-page bound. Text burdens and asset-by-asset byte lengths are recorded in evidence_asset_inventory.md; redundant native/layout/OCR copies do not increase unique source-unit counts.
