# Workflow 1.6.2 Evidence Asset Inventory

381 existing extraction/locator/metadata assets are inventoried individually below and hashed in `reused_artifact_hashes_before.sha256`: 274 USABLE, 98 DUPLICATE, 8 PARTIAL and 1 STALE; 0 UNREADABLE. Every hash path is package relative. Native/layout derivatives, normalized copies, OCR, images, extraction/page manifests and document identity records are eligible; previous scientific maps, checker findings, candidate sets, dispositions, classifications and reports are outside reuse discovery. No legacy script was executed. No standalone table/workbook extraction or source-location map beyond the enumerated manifests/document records is present. Legacy scripts, OCR logs, rights records and the mixed package-status manifest are not reused evidence inputs. A current `sha256sum -c` check passed for all 381 eligible assets and all four direct sources at inventory handoff.

Fitness is unit-specific: USABLE means adequate locator/transcription or image evidence; DUPLICATE means overlapping alternate text/image coverage, retained for optional corroboration; PARTIAL means identity/location metadata with inherited incomplete scope that is not applied to this review; STALE means legacy engine availability metadata that does not describe today's machine. No unreadable eligible assets were located. Images and OCR remain transcription aids; exact supplied source pages control scientific conclusions.

Source matching: all 45 plan-native and 45 plan-layout files matched current direct `pdftotext` extraction byte-for-byte; sharing native matched likewise. All 49 primary-group native files matched current direct layout extraction after whitespace removal. Alternate native extraction rearranges reading order and omits publication footers; it is a usable locator, including DOC001 p. 9, rather than the final authority. Normalized text is duplicate locator content. Complete extraction fitness does not mark any unit scientifically mapped.

Engines: plan/sharing text is Poppler `pdftotext` native or `-layout`; primary-group native is legacy layout text corroborated by current Poppler; alternate native is legacy native PDF extraction with engine version unspecified in its manifest; OCR is legacy rapidocr_onnxruntime with CPUExecutionProvider, as recorded in per-page metadata; rendered images are legacy PDF rasterization (version unspecified), with primary-group manifests recording 150 dpi. Current confirmation uses direct Poppler CPU tools. No new extraction/render/OCR derivative was written by the curator.

All assets map to exact PDF pages through numeric filename suffixes and the source-ID aliases in `source_inventory.md`; aggregate text and manifests map to explicitly listed source page sets. Derivative image gaps and current mapper assignments are detailed in `source_coverage.md`. Every source page is assigned to the downstream main or support mapper, regardless of old scope flags.

| Artifact path | Source ID | Exact source units | Asset type / engine | Fitness |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/document_record.json | DOC001 | PDF pp. 1-8 | Document identity/location metadata | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/native_text/page-001.txt | DOC001 | PDF p. 1 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/native_text/page-002.txt | DOC001 | PDF p. 2 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/native_text/page-003.txt | DOC001 | PDF p. 3 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/native_text/page-004.txt | DOC001 | PDF p. 4 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/native_text/page-005.txt | DOC001 | PDF p. 5 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/native_text/page-006.txt | DOC001 | PDF p. 6 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/native_text/page-007.txt | DOC001 | PDF p. 7 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/native_text/page-008.txt | DOC001 | PDF p. 8 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/normalized_text.txt | DOC001 | PDF pp. 1-8 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/normalized_text/page-001.txt | DOC001 | PDF p. 1 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/normalized_text/page-002.txt | DOC001 | PDF p. 2 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/normalized_text/page-003.txt | DOC001 | PDF p. 3 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/normalized_text/page-004.txt | DOC001 | PDF p. 4 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/normalized_text/page-005.txt | DOC001 | PDF p. 5 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/normalized_text/page-006.txt | DOC001 | PDF p. 6 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/normalized_text/page-007.txt | DOC001 | PDF p. 7 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/normalized_text/page-008.txt | DOC001 | PDF p. 8 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/rendered_pages/page-4.png | DOC001 | PDF p. 4 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/rendered_pages/page-5.png | DOC001 | PDF p. 5 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/rendered_pages/page-6.png | DOC001 | PDF p. 6 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/rendered_pages/page-7.png | DOC001 | PDF p. 7 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-MAIN/rendered_pages/page-8.png | DOC001 | PDF p. 8 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-DATA-SHARING/document_record.json | DOC004 | PDF p. 1 | Document identity/location metadata | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-PROTOCOL-SAP/document_record.json | DOC002 | PDF pp. 1-45 | Document identity/location metadata | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/document_record.json | DOC003 | PDF pp. 1-41 | Document identity/location metadata | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-001.txt | DOC003 | PDF p. 1 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-002.txt | DOC003 | PDF p. 2 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-003.txt | DOC003 | PDF p. 3 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-004.txt | DOC003 | PDF p. 4 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-005.txt | DOC003 | PDF p. 5 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-006.txt | DOC003 | PDF p. 6 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-007.txt | DOC003 | PDF p. 7 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-008.txt | DOC003 | PDF p. 8 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-009.txt | DOC003 | PDF p. 9 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-010.txt | DOC003 | PDF p. 10 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-011.txt | DOC003 | PDF p. 11 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-012.txt | DOC003 | PDF p. 12 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-013.txt | DOC003 | PDF p. 13 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-014.txt | DOC003 | PDF p. 14 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-015.txt | DOC003 | PDF p. 15 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-016.txt | DOC003 | PDF p. 16 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-017.txt | DOC003 | PDF p. 17 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-018.txt | DOC003 | PDF p. 18 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-019.txt | DOC003 | PDF p. 19 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-020.txt | DOC003 | PDF p. 20 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-021.txt | DOC003 | PDF p. 21 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-022.txt | DOC003 | PDF p. 22 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-023.txt | DOC003 | PDF p. 23 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-024.txt | DOC003 | PDF p. 24 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-025.txt | DOC003 | PDF p. 25 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-026.txt | DOC003 | PDF p. 26 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-027.txt | DOC003 | PDF p. 27 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-028.txt | DOC003 | PDF p. 28 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-029.txt | DOC003 | PDF p. 29 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-030.txt | DOC003 | PDF p. 30 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-031.txt | DOC003 | PDF p. 31 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-032.txt | DOC003 | PDF p. 32 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-033.txt | DOC003 | PDF p. 33 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-034.txt | DOC003 | PDF p. 34 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-035.txt | DOC003 | PDF p. 35 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-036.txt | DOC003 | PDF p. 36 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-037.txt | DOC003 | PDF p. 37 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-038.txt | DOC003 | PDF p. 38 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-039.txt | DOC003 | PDF p. 39 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-040.txt | DOC003 | PDF p. 40 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-041.txt | DOC003 | PDF p. 41 | Legacy layout text; current Poppler corroboration | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text.txt | DOC003 | PDF pp. 1-41 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-001.txt | DOC003 | PDF p. 1 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-002.txt | DOC003 | PDF p. 2 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-003.txt | DOC003 | PDF p. 3 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-004.txt | DOC003 | PDF p. 4 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-005.txt | DOC003 | PDF p. 5 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-006.txt | DOC003 | PDF p. 6 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-007.txt | DOC003 | PDF p. 7 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-008.txt | DOC003 | PDF p. 8 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-009.txt | DOC003 | PDF p. 9 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-010.txt | DOC003 | PDF p. 10 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-011.txt | DOC003 | PDF p. 11 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-012.txt | DOC003 | PDF p. 12 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-013.txt | DOC003 | PDF p. 13 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-014.txt | DOC003 | PDF p. 14 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-015.txt | DOC003 | PDF p. 15 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-016.txt | DOC003 | PDF p. 16 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-017.txt | DOC003 | PDF p. 17 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-018.txt | DOC003 | PDF p. 18 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-019.txt | DOC003 | PDF p. 19 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-020.txt | DOC003 | PDF p. 20 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-021.txt | DOC003 | PDF p. 21 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-022.txt | DOC003 | PDF p. 22 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-023.txt | DOC003 | PDF p. 23 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-024.txt | DOC003 | PDF p. 24 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-025.txt | DOC003 | PDF p. 25 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-026.txt | DOC003 | PDF p. 26 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-027.txt | DOC003 | PDF p. 27 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-028.txt | DOC003 | PDF p. 28 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-029.txt | DOC003 | PDF p. 29 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-030.txt | DOC003 | PDF p. 30 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-031.txt | DOC003 | PDF p. 31 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-032.txt | DOC003 | PDF p. 32 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-033.txt | DOC003 | PDF p. 33 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-034.txt | DOC003 | PDF p. 34 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-035.txt | DOC003 | PDF p. 35 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-036.txt | DOC003 | PDF p. 36 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-037.txt | DOC003 | PDF p. 37 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-038.txt | DOC003 | PDF p. 38 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-039.txt | DOC003 | PDF p. 39 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-040.txt | DOC003 | PDF p. 40 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/normalized_text/page-041.txt | DOC003 | PDF p. 41 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-02.png | DOC003 | PDF p. 2 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-03.png | DOC003 | PDF p. 3 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-04.png | DOC003 | PDF p. 4 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-05.png | DOC003 | PDF p. 5 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-06.png | DOC003 | PDF p. 6 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-07.png | DOC003 | PDF p. 7 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-08.png | DOC003 | PDF p. 8 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-09.png | DOC003 | PDF p. 9 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-10.png | DOC003 | PDF p. 10 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-11.png | DOC003 | PDF p. 11 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-12.png | DOC003 | PDF p. 12 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-13.png | DOC003 | PDF p. 13 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-14.png | DOC003 | PDF p. 14 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-15.png | DOC003 | PDF p. 15 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-16.png | DOC003 | PDF p. 16 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-17.png | DOC003 | PDF p. 17 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-18.png | DOC003 | PDF p. 18 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-19.png | DOC003 | PDF p. 19 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-20.png | DOC003 | PDF p. 20 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-21.png | DOC003 | PDF p. 21 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-22.png | DOC003 | PDF p. 22 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-23.png | DOC003 | PDF p. 23 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-24.png | DOC003 | PDF p. 24 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-25.png | DOC003 | PDF p. 25 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-26.png | DOC003 | PDF p. 26 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-27.png | DOC003 | PDF p. 27 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-28.png | DOC003 | PDF p. 28 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-29.png | DOC003 | PDF p. 29 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-30.png | DOC003 | PDF p. 30 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-31.png | DOC003 | PDF p. 31 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-32.png | DOC003 | PDF p. 32 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-33.png | DOC003 | PDF p. 33 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-34.png | DOC003 | PDF p. 34 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-35.png | DOC003 | PDF p. 35 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-36.png | DOC003 | PDF p. 36 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-37.png | DOC003 | PDF p. 37 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-38.png | DOC003 | PDF p. 38 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-39.png | DOC003 | PDF p. 39 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-40.png | DOC003 | PDF p. 40 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/rendered_pages/page-41.png | DOC003 | PDF p. 41 | Legacy rasterization, 150 dpi | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_extraction_manifest.json | DOC001 | PDF pp. 1-9 | Native extraction location manifest | PARTIAL |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-001.txt | DOC001 | PDF p. 1 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-002.txt | DOC001 | PDF p. 2 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-003.txt | DOC001 | PDF p. 3 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-004.txt | DOC001 | PDF p. 4 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-005.txt | DOC001 | PDF p. 5 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-006.txt | DOC001 | PDF p. 6 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-007.txt | DOC001 | PDF p. 7 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-008.txt | DOC001 | PDF p. 8 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-009.txt | DOC001 | PDF p. 9 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/normalized_text.txt | DOC001 | PDF pp. 1-9 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/ocr_page_images/page-004.png | DOC001 | PDF p. 4 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/ocr_page_images/page-005.png | DOC001 | PDF p. 5 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/ocr_page_images/page-006.png | DOC001 | PDF p. 6 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/ocr_page_images/page-007.png | DOC001 | PDF p. 7 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/ocr_page_images/page-008.png | DOC001 | PDF p. 8 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/ocr_text_pages/page-004.txt | DOC001 | PDF p. 4 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/ocr_text_pages/page-005.txt | DOC001 | PDF p. 5 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/ocr_text_pages/page-006.txt | DOC001 | PDF p. 6 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/ocr_text_pages/page-007.txt | DOC001 | PDF p. 7 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/page_ocr_metadata/page-004.json | DOC001 | PDF p. 4 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/page_ocr_metadata/page-005.json | DOC001 | PDF p. 5 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/page_ocr_metadata/page-006.json | DOC001 | PDF p. 6 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-01/page_ocr_metadata/page-007.json | DOC001 | PDF p. 7 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_extraction_manifest.json | DOC003 | PDF pp. 1-41 | Native extraction location manifest | PARTIAL |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-001.txt | DOC003 | PDF p. 1 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-002.txt | DOC003 | PDF p. 2 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-003.txt | DOC003 | PDF p. 3 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-004.txt | DOC003 | PDF p. 4 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-005.txt | DOC003 | PDF p. 5 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-006.txt | DOC003 | PDF p. 6 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-007.txt | DOC003 | PDF p. 7 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-008.txt | DOC003 | PDF p. 8 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-009.txt | DOC003 | PDF p. 9 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-010.txt | DOC003 | PDF p. 10 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-011.txt | DOC003 | PDF p. 11 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-012.txt | DOC003 | PDF p. 12 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-013.txt | DOC003 | PDF p. 13 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-014.txt | DOC003 | PDF p. 14 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-015.txt | DOC003 | PDF p. 15 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-016.txt | DOC003 | PDF p. 16 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-017.txt | DOC003 | PDF p. 17 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-018.txt | DOC003 | PDF p. 18 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-019.txt | DOC003 | PDF p. 19 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-020.txt | DOC003 | PDF p. 20 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-021.txt | DOC003 | PDF p. 21 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-022.txt | DOC003 | PDF p. 22 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-023.txt | DOC003 | PDF p. 23 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-024.txt | DOC003 | PDF p. 24 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-025.txt | DOC003 | PDF p. 25 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-026.txt | DOC003 | PDF p. 26 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-027.txt | DOC003 | PDF p. 27 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-028.txt | DOC003 | PDF p. 28 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-029.txt | DOC003 | PDF p. 29 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-030.txt | DOC003 | PDF p. 30 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-031.txt | DOC003 | PDF p. 31 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-032.txt | DOC003 | PDF p. 32 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-033.txt | DOC003 | PDF p. 33 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-034.txt | DOC003 | PDF p. 34 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-035.txt | DOC003 | PDF p. 35 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-036.txt | DOC003 | PDF p. 36 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-037.txt | DOC003 | PDF p. 37 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-038.txt | DOC003 | PDF p. 38 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-039.txt | DOC003 | PDF p. 39 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-040.txt | DOC003 | PDF p. 40 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/native_text_pages/page-041.txt | DOC003 | PDF p. 41 | Legacy native text; engine unspecified | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/normalized_text.txt | DOC003 | PDF pp. 1-41 | Normalized aggregate/page text | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-002.png | DOC003 | PDF p. 2 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-003.png | DOC003 | PDF p. 3 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-004.png | DOC003 | PDF p. 4 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-005.png | DOC003 | PDF p. 5 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-006.png | DOC003 | PDF p. 6 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-007.png | DOC003 | PDF p. 7 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-008.png | DOC003 | PDF p. 8 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-009.png | DOC003 | PDF p. 9 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-010.png | DOC003 | PDF p. 10 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-011.png | DOC003 | PDF p. 11 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-012.png | DOC003 | PDF p. 12 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-013.png | DOC003 | PDF p. 13 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-014.png | DOC003 | PDF p. 14 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-015.png | DOC003 | PDF p. 15 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-016.png | DOC003 | PDF p. 16 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-017.png | DOC003 | PDF p. 17 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-018.png | DOC003 | PDF p. 18 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-019.png | DOC003 | PDF p. 19 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-020.png | DOC003 | PDF p. 20 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-021.png | DOC003 | PDF p. 21 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-022.png | DOC003 | PDF p. 22 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-023.png | DOC003 | PDF p. 23 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-024.png | DOC003 | PDF p. 24 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-025.png | DOC003 | PDF p. 25 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-026.png | DOC003 | PDF p. 26 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-027.png | DOC003 | PDF p. 27 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-028.png | DOC003 | PDF p. 28 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-029.png | DOC003 | PDF p. 29 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-030.png | DOC003 | PDF p. 30 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-031.png | DOC003 | PDF p. 31 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-032.png | DOC003 | PDF p. 32 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-033.png | DOC003 | PDF p. 33 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-034.png | DOC003 | PDF p. 34 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-035.png | DOC003 | PDF p. 35 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-036.png | DOC003 | PDF p. 36 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-037.png | DOC003 | PDF p. 37 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-038.png | DOC003 | PDF p. 38 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-039.png | DOC003 | PDF p. 39 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-040.png | DOC003 | PDF p. 40 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_page_images/page-041.png | DOC003 | PDF p. 41 | Legacy OCR input rasterization | DUPLICATE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-002.txt | DOC003 | PDF p. 2 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-003.txt | DOC003 | PDF p. 3 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-004.txt | DOC003 | PDF p. 4 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-005.txt | DOC003 | PDF p. 5 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-006.txt | DOC003 | PDF p. 6 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-007.txt | DOC003 | PDF p. 7 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-008.txt | DOC003 | PDF p. 8 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-009.txt | DOC003 | PDF p. 9 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-010.txt | DOC003 | PDF p. 10 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-011.txt | DOC003 | PDF p. 11 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-012.txt | DOC003 | PDF p. 12 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-013.txt | DOC003 | PDF p. 13 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-014.txt | DOC003 | PDF p. 14 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-015.txt | DOC003 | PDF p. 15 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/ocr_text_pages/page-016.txt | DOC003 | PDF p. 16 | rapidocr_onnxruntime CPU OCR | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-002.json | DOC003 | PDF p. 2 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-003.json | DOC003 | PDF p. 3 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-004.json | DOC003 | PDF p. 4 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-005.json | DOC003 | PDF p. 5 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-006.json | DOC003 | PDF p. 6 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-007.json | DOC003 | PDF p. 7 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-008.json | DOC003 | PDF p. 8 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-009.json | DOC003 | PDF p. 9 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-010.json | DOC003 | PDF p. 10 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-011.json | DOC003 | PDF p. 11 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-012.json | DOC003 | PDF p. 12 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-013.json | DOC003 | PDF p. 13 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-014.json | DOC003 | PDF p. 14 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-015.json | DOC003 | PDF p. 15 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/document_outputs/JAMA2019-2210-DOC-03/page_ocr_metadata/page-016.json | DOC003 | PDF p. 16 | CPU OCR page metadata | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-1.txt | DOC002 | PDF p. 1 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-10.txt | DOC002 | PDF p. 10 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-11.txt | DOC002 | PDF p. 11 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-12.txt | DOC002 | PDF p. 12 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-13.txt | DOC002 | PDF p. 13 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-14.txt | DOC002 | PDF p. 14 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-15.txt | DOC002 | PDF p. 15 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-16.txt | DOC002 | PDF p. 16 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-17.txt | DOC002 | PDF p. 17 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-18.txt | DOC002 | PDF p. 18 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-19.txt | DOC002 | PDF p. 19 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-2.txt | DOC002 | PDF p. 2 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-20.txt | DOC002 | PDF p. 20 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-21.txt | DOC002 | PDF p. 21 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-22.txt | DOC002 | PDF p. 22 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-23.txt | DOC002 | PDF p. 23 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-24.txt | DOC002 | PDF p. 24 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-25.txt | DOC002 | PDF p. 25 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-26.txt | DOC002 | PDF p. 26 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-27.txt | DOC002 | PDF p. 27 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-28.txt | DOC002 | PDF p. 28 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-29.txt | DOC002 | PDF p. 29 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-3.txt | DOC002 | PDF p. 3 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-30.txt | DOC002 | PDF p. 30 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-31.txt | DOC002 | PDF p. 31 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-32.txt | DOC002 | PDF p. 32 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-33.txt | DOC002 | PDF p. 33 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-34.txt | DOC002 | PDF p. 34 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-35.txt | DOC002 | PDF p. 35 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-36.txt | DOC002 | PDF p. 36 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-37.txt | DOC002 | PDF p. 37 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-38.txt | DOC002 | PDF p. 38 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-39.txt | DOC002 | PDF p. 39 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-4.txt | DOC002 | PDF p. 4 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-40.txt | DOC002 | PDF p. 40 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-41.txt | DOC002 | PDF p. 41 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-42.txt | DOC002 | PDF p. 42 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-43.txt | DOC002 | PDF p. 43 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-44.txt | DOC002 | PDF p. 44 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-45.txt | DOC002 | PDF p. 45 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-5.txt | DOC002 | PDF p. 5 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-6.txt | DOC002 | PDF p. 6 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-7.txt | DOC002 | PDF p. 7 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-8.txt | DOC002 | PDF p. 8 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-layout-9.txt | DOC002 | PDF p. 9 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-1.txt | DOC002 | PDF p. 1 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-10.txt | DOC002 | PDF p. 10 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-11.txt | DOC002 | PDF p. 11 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-12.txt | DOC002 | PDF p. 12 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-13.txt | DOC002 | PDF p. 13 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-14.txt | DOC002 | PDF p. 14 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-15.txt | DOC002 | PDF p. 15 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-16.txt | DOC002 | PDF p. 16 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-17.txt | DOC002 | PDF p. 17 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-18.txt | DOC002 | PDF p. 18 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-19.txt | DOC002 | PDF p. 19 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-2.txt | DOC002 | PDF p. 2 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-20.txt | DOC002 | PDF p. 20 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-21.txt | DOC002 | PDF p. 21 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-22.txt | DOC002 | PDF p. 22 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-23.txt | DOC002 | PDF p. 23 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-24.txt | DOC002 | PDF p. 24 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-25.txt | DOC002 | PDF p. 25 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-26.txt | DOC002 | PDF p. 26 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-27.txt | DOC002 | PDF p. 27 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-28.txt | DOC002 | PDF p. 28 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-29.txt | DOC002 | PDF p. 29 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-3.txt | DOC002 | PDF p. 3 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-30.txt | DOC002 | PDF p. 30 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-31.txt | DOC002 | PDF p. 31 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-32.txt | DOC002 | PDF p. 32 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-33.txt | DOC002 | PDF p. 33 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-34.txt | DOC002 | PDF p. 34 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-35.txt | DOC002 | PDF p. 35 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-36.txt | DOC002 | PDF p. 36 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-37.txt | DOC002 | PDF p. 37 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-38.txt | DOC002 | PDF p. 38 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-39.txt | DOC002 | PDF p. 39 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-4.txt | DOC002 | PDF p. 4 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-40.txt | DOC002 | PDF p. 40 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-41.txt | DOC002 | PDF p. 41 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-42.txt | DOC002 | PDF p. 42 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-43.txt | DOC002 | PDF p. 43 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-44.txt | DOC002 | PDF p. 44 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-45.txt | DOC002 | PDF p. 45 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-5.txt | DOC002 | PDF p. 5 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-6.txt | DOC002 | PDF p. 6 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-7.txt | DOC002 | PDF p. 7 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-8.txt | DOC002 | PDF p. 8 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/plan-native-9.txt | DOC002 | PDF p. 9 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/sharing-layout-1.txt | DOC004 | PDF p. 1 | Poppler pdftotext -layout | USABLE |
| .ai_paper_validation/review_1_6_1/preprocessing/sharing-native-1.txt | DOC004 | PDF p. 1 | Poppler pdftotext native | USABLE |
| .ai_paper_validation/preprocessing/page_level_manifest.json | DOC001, DOC002, DOC003, DOC004 | DOC001 pp. 1-8; DOC003 pp. 1-41 | Page-level extraction/render manifest | PARTIAL |
| .ai_paper_validation/preprocessing/preprocessing_manifest.json | DOC001, DOC002, DOC003, DOC004 | Metadata references for four source documents | Document extraction manifest | PARTIAL |
| .ai_paper_validation/preprocessing/ocr_backend.json | DOC001, DOC002, DOC003, DOC004 | Historical tooling metadata; no unique page coverage | Legacy OCR engine availability record | STALE |

## Current-run direct-source derivatives

These are new derivatives, not reused legacy assets; their source authority and confirmation facts are in the assigned mapper/checker/recheck artifacts. All computations used CPU. No OCR or Office conversion was needed. Tool versions are recorded in preprocessing/direct_tool_versions.txt. All derivative rows below have separate coverage-manifest artifact rows.

| New derivative path, relative to review_1_6_2 | Exact supplied-source units | Engine |
|---|---|---|
| preprocessing/support-core-plan-p14.png | DOC002 p14 | Poppler pdftoppm CPU110dpi |
| preprocessing/cross-main-p3.png | DOC001 p3 | Poppler pdftoppm CPU100dpi |
| preprocessing/cross-plan-p25.png | DOC002 p25 | Poppler pdftoppm CPU100dpi |
| preprocessing/cross-plan-p31.png | DOC002 p31 | Poppler pdftoppm CPU100dpi |
| preprocessing/st1-plan-p19.png | DOC002 p19 | Poppler pdftoppm CPU120dpi |
| preprocessing/st1-plan-p45.png | DOC002 p45 | Poppler pdftoppm CPU120dpi |
| preprocessing/st1-plan-p19.txt | DOC002 p19 | Poppler pdftotext layout CPU |
| preprocessing/st1-plan-p45.txt | DOC002 p45 | Poppler pdftotext layout CPU |
| preprocessing/recheck-main-p1-p9.txt | DOC001 pp1-9 | Poppler pdftotext layout CPU |
| preprocessing/recheck-plan-p1-p45.txt | DOC002 pp1-45 | Poppler pdftotext layout CPU |
| preprocessing/recheck-report-supp2-p1-p41.txt | DOC003 pp1-41 | Poppler pdftotext layout CPU |
| preprocessing/recheck-report-supp3-p1.txt | DOC004 p1 | Poppler pdftotext layout CPU |
| preprocessing/recheck-main-p2.png | DOC001 p2 | Poppler pdftoppm CPU120dpi |
| preprocessing/recheck-main-p4.png | DOC001 p4 | Poppler pdftoppm CPU120dpi |
| preprocessing/recheck-main-p5.png | DOC001 p5 | Poppler pdftoppm CPU120dpi |
| preprocessing/recheck-main-p6.png | DOC001 p6 | Poppler pdftoppm CPU120dpi |
| preprocessing/recheck-main-p7.png | DOC001 p7 | Poppler pdftoppm CPU120dpi |
| preprocessing/recheck-main-p8.png | DOC001 p8 | Poppler pdftoppm CPU120dpi |
| preprocessing/recheck-plan-p45.png | DOC002 p45 | Poppler pdftoppm CPU180dpi |

The coordinator created checking-map projections with awk from complete canonical maps; only duplicated source-text annexes were omitted, and all keyed quantitative fields were retained. Original parts and canonical complete maps remain available. A second awk projection retains all39 original checker exclusion rows. The genotype-calculation table is an exact mechanical copy of all22 affected cells from the numeric checker. These current-run projections are unmodified scientific handoff aids, not direct supplied sources or pre-existing assets.
