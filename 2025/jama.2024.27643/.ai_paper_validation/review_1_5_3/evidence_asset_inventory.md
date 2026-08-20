# Reused Evidence-Asset Inventory

Scope: every existing OCR text, native/layout text, table/workbook extraction, rendered page, page manifest, document record, and source-location map below the pre-existing audit area. Old candidate, verifier, critic, endetail, quality, queue, disposition, and final-report records were neither read nor treated as discovery scope. Hashes for all 65 qualifying reusable artifacts are in `reused_artifact_hashes_before.sha256` using package-relative paths.

## Asset counts

| Asset class | Count | Coverage outcome |
|---|---:|---|
| Native page text | 38 | 38 usable PDF pages: DOC-001 pp. 1-12 and DOC-004 pp. 1-26 |
| Normalized native text | 2 | Duplicate convenience derivatives; not independently counted for coverage |
| Rendered PNG pages | 16 | Usable visual companions for layout-intensive pages; not independently counted for coverage |
| Page manifests | 2 | Usable source-location maps for DOC-001 and DOC-004 |
| Document records | 6 | Usable identity/scope locators for DOC-001 and DOC-004; PARTIAL metadata locators for DOC-002, DOC-003, DOC-005, and DOC-006 |
| Package source-location map | 1 | PARTIAL cross-document inventory locator |
| OCR text | 0 | None found |
| Layout-text-only assets | 0 | None found separately from native page text |
| Table/workbook extraction | 0 | None found |
| Workbook/CSV sources or maps | 0 | None found |

## Document records and source-location map

| Asset path | Asset type | Exact source location mapped | Method and fitness | Classification | Gap or use |
|---|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001/document_record.md | Document record | DOC-001 PDF pp. 1-12 | Source identity, stable total, and derivative links match the current direct-source hash. | USABLE | Locator for full document; native page text supplies page content. |
| .ai_paper_validation/document_outputs/DOC-002/document_record.md | Document record | DOC-002 inventory evidence: PDF pp. 1-3; document identity: pp. 1-229 | Record describes only initial text-layer probe and has no reusable page extraction. | PARTIAL | Fresh direct mapping required for pp. 1-229. |
| .ai_paper_validation/document_outputs/DOC-003/document_record.md | Document record | DOC-003 inventory evidence: PDF pp. 1-3; document identity: pp. 1-130 | Record describes only initial text-layer probe and has no reusable page extraction. | PARTIAL | Fresh direct mapping required for pp. 1-130. |
| .ai_paper_validation/document_outputs/DOC-004/document_record.md | Document record | DOC-004 PDF pp. 1-26 | Source identity, stable total, and derivative links match the current direct-source hash. | USABLE | Locator for full document; native page text supplies page content. |
| .ai_paper_validation/document_outputs/DOC-005/document_record.md | Document record | DOC-005 inventory evidence: PDF pp. 1-3; document identity: pp. 1-6 | Record describes only initial text-layer probe and has no reusable page extraction. | PARTIAL | Fresh direct mapping required for pp. 1-6. |
| .ai_paper_validation/document_outputs/DOC-006/document_record.md | Document record | DOC-006 inventory evidence: PDF p. 1; document identity: PDF p. 1 | Record has only document-level inventory metadata and no reusable page extraction. | PARTIAL | Fresh direct mapping required for p. 1. |
| .ai_paper_validation/document_outputs/package_manifest.md | Source-location map | DOC-001 pp. 1-3; DOC-002 pp. 1-3; DOC-003 pp. 1-3; DOC-004 pp. 1-3; DOC-005 pp. 1-3; DOC-006 p. 1, plus page totals for all six PDFs | Cross-document inventory and source hashes match current direct sources; it is not a complete page-content map. | PARTIAL | Does not substitute for page-level evidence; use only as identity and coverage locator. |

## Native-text assets

Each listed individual native-text file is a `pdftotext -layout` derivative. Text probes confirmed readable content on DOC-001 p. 1 and p. 5 and DOC-004 p. 1 and p. 14. The page manifests record usable native text on all corresponding pages. DOC-004 p. 26 is sparse as expected for rights/end matter and is usable to establish that it contains no result content.

| Individual asset paths | Exact source pages mapped one-to-one | Fitness | Classification | Gap or use |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001/preprocessing/native_pages/page-01.txt; page-02.txt; page-03.txt; page-04.txt; page-05.txt; page-06.txt; page-07.txt; page-08.txt; page-09.txt; page-10.txt; page-11.txt; page-12.txt | DOC-001 PDF pp. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 respectively | Readable native layout text; source hash matches current direct PDF. | USABLE | Covers all DOC-001 page units; p. 5 remains layout-intensive and has a rendered companion. |
| .ai_paper_validation/document_outputs/DOC-004/preprocessing/native_pages/page-01.txt; page-02.txt; page-03.txt; page-04.txt; page-05.txt; page-06.txt; page-07.txt; page-08.txt; page-09.txt; page-10.txt; page-11.txt; page-12.txt; page-13.txt; page-14.txt; page-15.txt; page-16.txt; page-17.txt; page-18.txt; page-19.txt; page-20.txt; page-21.txt; page-22.txt; page-23.txt; page-24.txt; page-25.txt; page-26.txt | DOC-004 PDF pp. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26 respectively | Readable native layout text on pp. 1-25; expected sparse rights/end matter on p. 26. Source hash matches current direct PDF. | USABLE | Covers all DOC-004 page units; pp. 14-25 have rendered companions for table/figure confirmation. |

## Normalized-text assets

| Asset path | Exact source pages mapped | Fitness | Classification | Gap or use |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001/preprocessing/normalized_text.txt | DOC-001 PDF pp. 1-12, with source-page delimiters | Aggregates the usable page-native files without adding page-level information. | DUPLICATE | Convenience locator only; individual native files retain exact locations. |
| .ai_paper_validation/document_outputs/DOC-004/preprocessing/normalized_text.txt | DOC-004 PDF pp. 1-25, with source-page delimiters | Aggregates the usable page-native files without adding page-level information; excludes rights-only p. 26. | DUPLICATE | Convenience locator only; individual native files retain exact locations. |

## Rendered-page assets

| Individual asset paths | Exact source page mapped one-to-one | Fitness | Classification | Gap or use |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001/preprocessing/page_images/page-05.png; page-06.png; page-07.png; page-08.png | DOC-001 PDF pp. 5, 6, 7, 8 respectively | 200-dpi retained direct-page renders for Figure 1, Table 1, Figure 2/Table 2, and Figure 3. | USABLE | Visual confirmation companion for layout-intensive content; native text remains the primary reuse artifact. |
| .ai_paper_validation/document_outputs/DOC-004/preprocessing/page_images/page-14.png; page-15.png; page-16.png; page-17.png; page-18.png; page-19.png; page-20.png; page-21.png; page-22.png; page-23.png; page-24.png; page-25.png | DOC-004 PDF pp. 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 respectively | 200-dpi retained direct-page renders for eTables 1-5 and the eFigure. | USABLE | Visual confirmation companion for tables/figure; native text remains the primary reuse artifact. |

## Page manifests

| Asset path | Exact source pages mapped | Fitness | Classification | Gap or use |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001/preprocessing/page_manifest.md | DOC-001 PDF pp. 1-12; individual native pages; rendered pp. 5-8 | Explicit page-level source map, method record, text-quality statement, and retained-render locations. | USABLE | Confirms full reusable page coverage. |
| .ai_paper_validation/document_outputs/DOC-004/preprocessing/page_manifest.md | DOC-004 PDF pp. 1-26; individual native pages; rendered pp. 14-25 | Explicit page-level source map, method record, text-quality statement, and retained-render locations. | USABLE | Confirms full reusable page coverage, including expected sparse p. 26. |

## Fitness conclusion

There are 38 reusable-backed page units and 366 fresh-required page units. No qualifying reused asset is STALE or UNREADABLE: the current direct-source hashes agree with the source hashes recorded by the existing package map where supplied, and every hashed reused asset is readable. The only non-usable-for-complete-content assets are the PARTIAL document/map records and the intentionally DUPLICATE normalized text. No OCR or table/workbook extraction exists to reduce the 366-page fresh direct-source assignment.
