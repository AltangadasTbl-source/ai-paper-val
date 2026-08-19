# Reused Evidence-Asset Inventory

This is an inventory of eligible existing OCR, native/layout text, extraction, rendered-page, manifest, document-record, and source-location-map assets below `.ai_paper_validation/`. Legacy candidate, verifier, critic, checker, and final-report outputs were neither read nor used as discovery scope. No eligible OCR sidecar, Office/workbook extraction, or structured-data extraction exists. No asset was modified.

## Inventory summary

| Asset class | Asset count | Source coverage represented | Fitness result |
|---|---:|---|---|
| Source-location map | 1 | DOC-001 pages 1-11; DOC-002 pages 1-25; DOC-003 pages 1-167 at inventory level only | PARTIAL |
| Document records | 3 | DOC-001 pages 1-11; DOC-002 pages 1-25; DOC-003 pages 1-167 | 1 USABLE, 2 PARTIAL |
| Page manifests | 3 | DOC-001 pages 1-11; DOC-002 pages 1-25; DOC-003 pages 1-167 | 1 USABLE, 2 PARTIAL |
| Native/layout page text | 29 | DOC-001 pages 1-11; DOC-002 pages 1-2 and 10-25 | 25 USABLE, 4 PARTIAL |
| Normalized aggregate text | 2 | DOC-001 pages 1-11; DOC-002 pages 1-2 and 10-25 | DUPLICATE |
| Rendered PDF pages | 21 | DOC-001 pages 5-9; DOC-002 pages 10-25 | USABLE visual complements |
| Source-location evidence maps | 2 | DOC-001 selected result locations; DOC-002 pages 1-2 and 10-25 | PARTIAL |

**Total hashed reusable artifacts:** 61. The hash file contains one SHA-256 entry with an exact package-relative path for every asset. There are no `UNREADABLE` assets; no eligible OCR, Office/workbook, CSV, or table-extraction file is present.

## Exact assets, source locations, and fitness

| Asset path or exact path set | Type and method | Exact source locations | Coverage and fitness | Classification | Required handling |
|---|---|---|---|---|---|
| `.ai_paper_validation/package_manifest.yaml` | Source-location map; local filename and PDF-metadata inventory | DOC-001 PDF pages 1-11; DOC-002 PDF pages 1-25; DOC-003 PDF pages 1-167 | Identifies all sources and page counts but carries an earlier selective scientific scope. | PARTIAL | Use only as source identity/location aid; direct coverage rows and fresh assignments supersede the selective scope. |
| `.ai_paper_validation/document_outputs/basis_main_article/document_record.yaml` | Document record | DOC-001 PDF pages 1-11 | Correct document identity and all-page native-text coverage. | USABLE | Use as provenance and location aid. |
| `.ai_paper_validation/document_outputs/basis_main_article/extraction/page_manifest.yaml` | Page manifest; `pdftotext -layout` record | DOC-001 PDF pages 1-11 | Maps every page to a usable native-text file and maps rendered complements for pages 5-9. | USABLE | Reuse for page-level navigation. |
| `.ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-001.txt` through `page-011.txt` | Native/layout page text; one file per page | DOC-001 PDF pages 1-11, respectively | All 11 pages have usable text. | USABLE | Reuse for mapping; confirm source PDF for any candidate. |
| `.ai_paper_validation/document_outputs/basis_main_article/extraction/normalized_text/main_article_selected_pages.txt` | Normalized aggregate of native/layout text | DOC-001 PDF pages 1-11 | Same content locations as the individual native-page text; no independent coverage. | DUPLICATE | Locator only; do not double-count units. |
| `.ai_paper_validation/document_outputs/basis_main_article/extraction/page_images/page-005-05.png`, `page-006-06.png`, `page-007-07.png`, `page-008-08.png`, `page-009-09.png` | Rendered PDF pages | DOC-001 PDF pages 5, 6, 7, 8, and 9, respectively | Visual complements for Figure 1, Table 1, Figure 2, Table 2, and Figure 3. | USABLE | Reuse for visual/table alignment; direct PDF remains authority. |
| `.ai_paper_validation/document_outputs/basis_main_article/main_text_extraction.md` | Source-location evidence map | DOC-001 PDF pages 1, 3-10, with repeated table/figure locations on pages 5-9 | Result-focused map; it is not a complete page-by-page mapping of all text. | PARTIAL | Use only as a locator; native page files cover the complete DOC-001 page set. |
| `.ai_paper_validation/document_outputs/basis_results_supplement/document_record.yaml` | Document record | DOC-002 PDF pages 1-25 | Correct identity and maps retained page assets, but records pages 3-9 as excluded. | PARTIAL | Freshly map pages 3-9. |
| `.ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_manifest.yaml` | Page manifest; `pdftotext -layout` record | DOC-002 PDF pages 1-2, 3-9, and 10-25 | Maps retained text/renders for pages 1-2 and 10-25; explicitly has no retained extraction for pages 3-9. | PARTIAL | Freshly map pages 3-9. |
| `.ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-001.txt`, `page-002.txt` | Native/layout page text | DOC-002 PDF pages 1-2, respectively | Usable title and contents text. | USABLE | Reuse for scope/context mapping. |
| `.ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-010.txt`, `page-011.txt`, `page-012.txt`, `page-013.txt` | Native/layout page text | DOC-002 PDF pages 10-13, respectively | Sparse figure text; insufficient alone for figure-label extraction. | PARTIAL | Reuse with the paired rendered page; direct source confirmation remains required. |
| `.ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-014.txt` through `page-025.txt` | Native/layout page text; one file per page | DOC-002 PDF pages 14-25, respectively | Usable layout-preserved table text. | USABLE | Reuse for mapping; use paired render where spatial alignment matters. |
| `.ai_paper_validation/document_outputs/basis_results_supplement/extraction/normalized_text/results_supplement_selected_pages.txt` | Normalized aggregate of native/layout text | DOC-002 PDF pages 1-2 and 10-25 | Duplicate of retained individual native page text; pages 3-9 absent. | DUPLICATE | Locator only; do not count as coverage and freshly map pages 3-9. |
| `.ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-010-10.png` through `page-025-25.png` | Rendered PDF pages; one file per page | DOC-002 PDF pages 10-25, respectively | Visual confirmation is usable for figures S1-S5 (pages 10-13) and table layout (pages 14-25). | USABLE | Reuse with native text; direct PDF is final authority. |
| `.ai_paper_validation/document_outputs/basis_results_supplement/extraction/results_supplement_evidence_map.md` | Source-location evidence map | DOC-002 PDF pages 1-2 and 10-25, including Figures S1-S5 and Tables S1-S12 | Result-focused and accurate as a locator, but it omits pages 3-9 by earlier design. | PARTIAL | Freshly map pages 3-9 and do not treat the map as an audit boundary. |
| `.ai_paper_validation/document_outputs/basis_protocol_sap/document_record.yaml` | Document record | DOC-003 PDF pages 1-167 | Correct source identity and page count, but it contains no scientific extraction. | PARTIAL | Fresh direct-source mapping for pages 1-167. |
| `.ai_paper_validation/document_outputs/basis_protocol_sap/extraction/page_manifest.yaml` | Page manifest | DOC-003 PDF pages 1-167 | Explicitly records no native, rendered, or OCR extraction. | PARTIAL | Fresh direct-source mapping for pages 1-167. |

## Gaps and assignments

1. DOC-002 pages 3-9 have no reusable text, render, OCR, or table asset. They are fresh-required and assigned to `qc15_support_quantitative_mapper`.
2. DOC-003 pages 1-167 have no reusable content derivative. They are fresh-required and assigned to `qc15_support_quantitative_mapper`.
3. DOC-002 pages 10-13 have sparse native text, but usable paired renders close the reusable derivative gap; mapping still requires direct-PDF confirmation for any exact scientific claim.
4. All reusable assets are immutable provenance/locator aids. They do not replace direct-source confirmation during candidate recheck.
