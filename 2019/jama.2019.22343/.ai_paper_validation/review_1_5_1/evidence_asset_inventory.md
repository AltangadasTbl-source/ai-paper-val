# Reused Evidence Asset Inventory

This is an inventory of every eligible existing reuse asset below the earlier audit area. Old candidate, checker, verifier, critic, endetail, quality, and final-report content was not read or used to define discovery scope. The individually hashed file register in `reused_artifact_hashes_before.sha256` has 89 rows, one for each asset described here.

## Asset totals and fitness

| Asset family | Files | Exact direct-source locations | Fitness | Coverage decision |
|---|---:|---|---|---|
| Native PDF text | 11 | DOC-001 PDF pp. 1-11; one same-numbered `page-###.txt` file per page | USABLE | Reusable for all 11 DOC-001 units. |
| Native PDF text | 29 | DOC-003 PDF pp. 17-45; one same-numbered `page-###.txt` file per page | USABLE | Reusable for 29 DOC-003 units. |
| Rendered visual pages | 4 | DOC-001 PDF pp. 4, 5, 6, and 8 | USABLE | Visual-only aid; native text remains the textual reuse asset. |
| Rendered visual pages | 29 | DOC-003 PDF pp. 17-45; one same-numbered PNG per page | USABLE | Visual-only aid; native text remains the textual reuse asset. |
| Page manifest | 1 | DOC-001 pp. 1-11 and DOC-003 pp. 17-45 | PARTIAL | Truthful page-level mapping for its recorded pages; it omits DOC-002 and DOC-003 pp. 1-16 and 46-49. |
| OCR backend record | 1 | No OCR output pages | DUPLICATE | Administrative metadata only. It reports zero OCR execution and does not supply textual coverage. |
| Package manifest | 1 | DOC-001 pp. 1-11; DOC-002 pp. 1-15; DOC-003 pp. 1-49 | PARTIAL | Source identity and page counts are usable; its old scientific-scope exclusions cannot define current coverage. |
| Initial and preprocessing document records | 6 | DOC-001 pp. 1-11; DOC-002 pp. 1-15; DOC-003 pp. 1-49, with old extraction statements | PARTIAL | Useful identity and provenance locators. DOC-002’s old non-audit decision and DOC-003’s old partial scope leave fresh assignments. |
| Existing source-location and table-oriented extraction maps | 2 | DOC-001 pp. 1-11 and DOC-003 pp. 17-45 | PARTIAL | Locator and transcription aids only; absent for DOC-002 and uncovered DOC-003 pages. |
| Training-restriction document records | 5 | Administrative package and document records; no result page, table, or paragraph coverage | DUPLICATE | No quantitative-evidence coverage. |

There are no existing OCR text outputs, layout-text outputs, workbook extractions, spreadsheet assets, CSV assets, or standalone machine-readable table extractions. No eligible asset was unreadable. No asset is classified STALE by a direct-source hash mismatch; direct PDF hashes match the values recorded in the older package manifest. “PARTIAL” identifies incomplete source-unit coverage, not a source-hash mismatch.

## Exact reusable asset paths and source mappings

| Asset paths, each file individually listed in the hash register | Type | Exact source location mapping | Fitness |
|---|---|---|---|
| `.ai_paper_validation/preprocessing/native_text/JAMA2019_22343_MAIN/page-001.txt` through `page-011.txt` | Native PDF text; 11 files | DOC-001 PDF pp. 1-11 respectively | USABLE |
| `.ai_paper_validation/preprocessing/native_text/JAMA2019_22343_SUPP2_RESULTS/page-017.txt` through `page-045.txt` | Native PDF text; 29 files | DOC-003 PDF pp. 17-45 respectively | USABLE |
| `.ai_paper_validation/preprocessing/ocr_images/JAMA2019_22343_MAIN/page-004.png`, `page-005.png`, `page-006.png`, and `page-008.png` | Rendered pages; 4 files | DOC-001 PDF pp. 4, 5, 6, and 8 respectively | USABLE |
| `.ai_paper_validation/preprocessing/ocr_images/JAMA2019_22343_SUPP2_RESULTS/page-017.png` through `page-045.png` | Rendered pages; 29 files | DOC-003 PDF pp. 17-45 respectively | USABLE |
| `.ai_paper_validation/preprocessing/page_manifest.json` | Page manifest | DOC-001 pp. 1-11 and DOC-003 pp. 17-45 | PARTIAL |
| `.ai_paper_validation/preprocessing/ocr_backend.json` | OCR backend record | No direct-source page output | DUPLICATE |
| `.ai_paper_validation/document_outputs/package_manifest.json` | Package document manifest | DOC-001 pp. 1-11; DOC-002 pp. 1-15; DOC-003 pp. 1-49 | PARTIAL |
| `.ai_paper_validation/document_outputs/JAMA2019_22343_MAIN/initial_document_record.md` and `preprocessing_record.md` | Document records; 2 files | DOC-001 pp. 1-11 | PARTIAL |
| `.ai_paper_validation/document_outputs/JAMA2019_22343_SUPP1_PROTOCOL/initial_document_record.md` and `preprocessing_record.md` | Document records; 2 files | DOC-002 pp. 1-15; no reusable page text exists | PARTIAL |
| `.ai_paper_validation/document_outputs/JAMA2019_22343_SUPP2_RESULTS/initial_document_record.md` and `preprocessing_record.md` | Document records; 2 files | DOC-003 pp. 17-45 reusable; all other DOC-003 pages are uncovered by prior scientific preprocessing | PARTIAL |
| `.ai_paper_validation/document_outputs/JAMA2019_22343_MAIN/main_text_extraction.md` | Existing source-location map and table-oriented extraction | DOC-001 pp. 1-11 | PARTIAL |
| `.ai_paper_validation/document_outputs/JAMA2019_22343_SUPP2_RESULTS/results_supplement_evidence_map.md` | Existing source-location map and table-oriented extraction | DOC-003 pp. 17-45 | PARTIAL |
| `.ai_paper_validation/document_outputs/JAMA2019_22343_MAIN/ai_training_restriction_record.md`, `.ai_paper_validation/document_outputs/JAMA2019_22343_SUPP1_PROTOCOL/ai_training_restriction_record.md`, `.ai_paper_validation/document_outputs/JAMA2019_22343_SUPP2_RESULTS/ai_training_restriction_record.md`, `.ai_paper_validation/document_outputs/doc-4786726a6b91/ai_training_restriction_record.json`, and `.ai_paper_validation/document_outputs/joi190154supp1_prod/ai_training_restriction_record.md` | Administrative document records; 5 files | No quantitative source unit | DUPLICATE |

## Fresh direct-source extraction created for every reuse gap

| Direct source pages | New native-text artifact family | New layout-text artifact family | Fitness and mapper instruction |
|---|---|---|---|
| DOC-002 PDF pp. 1-15 | `preprocessing/native_text/DOC-002_PROTOCOL/page-001.txt` through `page-015.txt` | `preprocessing/layout_text/DOC-002_PROTOCOL/page-001.txt` through `page-015.txt` | USABLE direct extraction, except normal sparse front-matter content where source PDF remains authoritative; assign all 15 pages to support mapping. |
| DOC-003 PDF pp. 1-16 and 46-49 | `preprocessing/native_text/DOC-003_RESULTS/page-001.txt` through `page-016.txt`, `page-046.txt` through `page-049.txt` | `preprocessing/layout_text/DOC-003_RESULTS/page-001.txt` through `page-016.txt`, `page-046.txt` through `page-049.txt` | USABLE direct extraction for page mapping. Page 8 is sparse text and has a paired rendered page; use the direct PDF visual for any table or figure transcription. |
| DOC-003 PDF p. 8 | `preprocessing/rendered_pages/DOC-003_RESULTS/page-008.png` | Not applicable | USABLE visual confirmation aid for a sparse-text page. |

## Gap conclusion

- DOC-001 has no reuse gap: 11 usable native-text-backed pages.
- DOC-002 has a 15-page reuse gap: all pages were newly extracted and assigned to support mapping.
- DOC-003 has a 20-page reuse gap: pages 1-16 and 46-49 were newly extracted and assigned to support mapping; pages 17-45 retain usable reuse support.
- The reusable and fresh-required partitions are complete; no non-usable or uncovered source page lacks a downstream mapper assignment.
