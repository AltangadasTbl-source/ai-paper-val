# Reused Evidence-Asset Inventory

This inventory includes every eligible existing OCR/native/layout text, table or workbook extraction, rendered page, page manifest, document record, and source-location map below the pre-existing audit area. No OCR, table/workbook extraction, or Office source exists. Prior candidate, verifier, critic, endetail, and final-report files were not used as discovery scope and are not listed as reusable evidence assets. `USABLE` assets can locate and transcribe the stated units; they remain derivative evidence rather than final authority.

| Asset path | Asset type / method | Exact source locations | Fitness | Coverage and gap disposition |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/package_manifest.json | Package document map | D001 pp. 1-9; D002 pp. 1-15; D003 pp. 1-16 | PARTIAL | Identifies all three sources and page counts, but retains prior selective scientific scope; not a content extraction. Fresh assignments remain D002 pp. 1-15 and D003 pp. 2-3,16. |
| .ai_paper_validation/document_outputs/D001_main_article/document_record.json | Document record | D001 pp. 1-9 | USABLE | Stable source identity, page count, and artifact links for all D001 units. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/page_manifest.json | Page manifest / `pdftotext -layout` map | D001 pp. 1-9; rendered pp. 4-7 | USABLE | Maps every D001 page to readable native text and records visual-page coverage. |
| .ai_paper_validation/document_outputs/D001_main_article/agent_outputs/main_text_extractor_evidence.md | Source-location evidence map | D001 pp. 1-9, with table/figure emphasis pp. 4-7 | USABLE | Source-linked result map; page-native files and rendered pages provide the underlying reusable coverage. |
| .ai_paper_validation/document_outputs/D001_main_article/full_text_search_only.txt | Native text, unsegmented search copy | D001 pp. 1-9 | DUPLICATE | Duplicates page-native text without reliable per-page unit boundaries; use page-specific text instead. |
| .ai_paper_validation/document_outputs/D001_main_article/page_1_rights_screen.txt | Page text / rights screen | D001 p. 1 | PARTIAL | Duplicates p. 1 text and records rights context only; not a complete evidence extraction. |
| .ai_paper_validation/document_outputs/D001_main_article/page_9_rights_screen.txt | Page text / rights screen | D001 p. 9 | PARTIAL | Duplicates p. 9 text and records rights context only; not a complete evidence extraction. |
| .ai_paper_validation/document_outputs/D001_main_article/ai_training_restriction_record.json | Administrative document record | D001 document-level; related screen pp. 1,9 | PARTIAL | Rights metadata only; no scientific unit coverage. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/main_article_native_text_normalized.txt | Normalized native layout text | D001 pp. 1-9 | DUPLICATE | Normalized concatenation duplicates the page-native files; page-specific files retain exact unit mapping. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/native_text/page_001.txt | Native layout text / `pdftotext -layout` | D001 p. 1 | USABLE | Readable source-matched page text. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/native_text/page_002.txt | Native layout text / `pdftotext -layout` | D001 p. 2 | USABLE | Readable source-matched page text. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/native_text/page_003.txt | Native layout text / `pdftotext -layout` | D001 p. 3 | USABLE | Readable source-matched page text. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/native_text/page_004.txt | Native layout text / `pdftotext -layout` | D001 p. 4 | USABLE | Readable text including Table 1 headings/cells; corresponding rendered page is available. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/native_text/page_005.txt | Native layout text / `pdftotext -layout` | D001 p. 5 | USABLE | Readable text including continued Table 1 and results. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/native_text/page_006.txt | Native layout text / `pdftotext -layout` | D001 p. 6 | USABLE | Readable figure boxes and Table 2 text; corresponding rendered page is available. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/native_text/page_007.txt | Native layout text / `pdftotext -layout` | D001 p. 7 | USABLE | Readable Table 3 text; corresponding rendered page is available. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/native_text/page_008.txt | Native layout text / `pdftotext -layout` | D001 p. 8 | USABLE | Readable source-matched page text. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/native_text/page_009.txt | Native layout text / `pdftotext -layout` | D001 p. 9 | USABLE | Readable source-matched page text. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/page_images/page_004.png | Rendered PDF page | D001 p. 4 | USABLE | Visual confirmation for Table 1 layout. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/page_images/page_005.png | Rendered PDF page | D001 p. 5 | USABLE | Visual confirmation for continued Table 1 layout. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/page_images/page_006.png | Rendered PDF page | D001 p. 6 | USABLE | Visual confirmation for participant flow and Table 2 layout. |
| .ai_paper_validation/document_outputs/D001_main_article/preprocessing/page_images/page_007.png | Rendered PDF page | D001 p. 7 | USABLE | Visual confirmation for Table 3 layout. |
| .ai_paper_validation/document_outputs/D002_protocol/document_record.json | Document record | D002 pp. 1-15 | STALE | Stable identity and page count remain useful, but the prior “not audited” scope is not sufficient for this complete-coverage workflow; fresh mapping assigned for all pages. |
| .ai_paper_validation/document_outputs/D002_protocol/not_audited_by_design.json | Scope-status document map | D002 pp. 1-15 | STALE | Records absence of extraction rather than evidence; every page is fresh-required. |
| .ai_paper_validation/document_outputs/D002_protocol/ai_training_restriction_record.json | Administrative document record | D002 document-level | PARTIAL | Rights metadata only; no scientific unit coverage. |
| .ai_paper_validation/document_outputs/D003_results_supplement/document_record.json | Document record | D003 pp. 1-16 | PARTIAL | Stable identity and existing artifact links are usable, but its prior exclusion of pp. 2-3,16 leaves those units fresh-required. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/page_manifest.json | Page manifest / `pdftotext -layout` map | D003 pp. 1,4-15; explicitly unextracted pp. 2-3,16 | PARTIAL | Maps 13 usable native-text units and identifies the three exact gaps for fresh mapping. |
| .ai_paper_validation/document_outputs/D003_results_supplement/agent_outputs/results_supplement_evidence_map.md | Source-location evidence map | D003 pp. 1,4-15 | USABLE | Source-linked results map for 13 pages; it does not cover pp. 2-3 or 16. |
| .ai_paper_validation/document_outputs/D003_results_supplement/ai_training_restriction_record.json | Administrative document record | D003 document-level | PARTIAL | Rights metadata only; no scientific unit coverage. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/results_supplement_native_text_normalized.txt | Normalized native layout text | D003 pp. 1,4-15 | DUPLICATE | Concatenated duplicate of the 13 page-native files; no coverage of pp. 2-3,16. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_001.txt | Native layout text / `pdftotext -layout` | D003 p. 1 | USABLE | Readable source-matched page text. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_004.txt | Native layout text / `pdftotext -layout` | D003 p. 4 | USABLE | Readable source-matched page text. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_005.txt | Native layout text / `pdftotext -layout` | D003 p. 5 | USABLE | Readable source-matched page text. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_006.txt | Native layout text / `pdftotext -layout` | D003 p. 6 | USABLE | Readable source-matched page text. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_007.txt | Native layout text / `pdftotext -layout` | D003 p. 7 | USABLE | Readable source-matched eTable text; rendered page is available. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_008.txt | Native layout text / `pdftotext -layout` | D003 p. 8 | USABLE | Readable source-matched eTable text; rendered page is available. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_009.txt | Native layout text / `pdftotext -layout` | D003 p. 9 | USABLE | Readable source-matched eTable text; rendered page is available. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_010.txt | Native layout text / `pdftotext -layout` | D003 p. 10 | USABLE | Readable source-matched eTable text; rendered page is available. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_011.txt | Native layout text / `pdftotext -layout` | D003 p. 11 | USABLE | Readable source-matched eTable text; rendered page is available. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_012.txt | Native layout text / `pdftotext -layout` | D003 p. 12 | USABLE | Readable source-matched eTable text; rendered page is available. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_013.txt | Native layout text / `pdftotext -layout` | D003 p. 13 | USABLE | Readable source-matched eTable text; rendered page is available. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_014.txt | Native layout text / `pdftotext -layout` | D003 p. 14 | USABLE | Readable source-matched eTable text; rendered page is available. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/native_text/page_015.txt | Native layout text / `pdftotext -layout` | D003 p. 15 | USABLE | Readable source-matched eTable text; rendered page is available. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/page_images/page_007.png | Rendered PDF page | D003 p. 7 | USABLE | Visual eTable layout confirmation. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/page_images/page_008.png | Rendered PDF page | D003 p. 8 | USABLE | Visual eTable layout confirmation. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/page_images/page_009.png | Rendered PDF page | D003 p. 9 | USABLE | Visual eTable layout confirmation. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/page_images/page_010.png | Rendered PDF page | D003 p. 10 | USABLE | Visual eTable layout confirmation. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/page_images/page_011.png | Rendered PDF page | D003 p. 11 | USABLE | Visual eTable layout confirmation. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/page_images/page_012.png | Rendered PDF page | D003 p. 12 | USABLE | Visual eTable layout confirmation. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/page_images/page_013.png | Rendered PDF page | D003 p. 13 | USABLE | Visual eTable layout confirmation. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/page_images/page_014.png | Rendered PDF page | D003 p. 14 | USABLE | Visual eTable layout confirmation. |
| .ai_paper_validation/document_outputs/D003_results_supplement/preprocessing/page_images/page_015.png | Rendered PDF page | D003 p. 15 | USABLE | Visual eTable layout confirmation. |

## Asset totals and explicit gaps

- Eligible reused assets inventoried and hashed: 52.
- USABLE: 39; PARTIAL: 8; STALE: 2; DUPLICATE: 3; UNREADABLE: 0; administrative/right-screen artifacts whose metadata does not form scientific evidence: 5 (included in the PARTIAL count).
- Existing OCR assets: 0. Existing table/workbook extractions: 0. Existing Office/workbook assets: 0.
- Reusable source-unit coverage: D001 pp. 1-9 and D003 pp. 1,4-15 (22 unique units).
- Every non-usable or uncovered direct-source unit is fresh-required: D002 pp. 1-15 and D003 pp. 2-3,16 (18 unique units), assigned to fresh direct-source extraction and support mapping.
