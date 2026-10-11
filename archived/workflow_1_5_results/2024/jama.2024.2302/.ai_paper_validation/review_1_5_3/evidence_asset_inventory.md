# Reused Evidence-Asset Inventory

This inventory covers every existing OCR text, native or layout text, table or workbook extraction, rendered page, page manifest, document record, and source-location map below the prior audit area. It excludes legacy candidate, checker, verifier, critic, detailed-error, and final-report content from discovery scope. No OCR text, layout text, table extraction, workbook extraction, or CSV extraction exists.

Fitness is assessed only for reuse as an extraction or location aid. Direct sources remain authoritative. Asset hashes are in `reused_artifact_hashes_before.sha256`.

| Asset path | Asset kind and method | Exact source coverage | Coverage and fitness | Gaps or mapper instruction |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/normalized_text/page-001.txt | Native PDF text | PDF-001 page 1 | USABLE | Direct-PDF confirmation remains required for any cited evidence. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/normalized_text/page-002.txt | Native PDF text | PDF-001 page 2 | USABLE | Direct-PDF confirmation remains required for any cited evidence. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/normalized_text/page-003.txt | Native PDF text | PDF-001 page 3 | USABLE | Pair with the page-003 render for figure-flow visual verification. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/normalized_text/page-004.txt | Native PDF text | PDF-001 page 4 | USABLE | Direct-PDF confirmation remains required for any cited evidence. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/normalized_text/page-005.txt | Native PDF text | PDF-001 page 5 | USABLE | Pair with the page-005 render for Table 1 visual verification. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/normalized_text/page-006.txt | Native PDF text | PDF-001 page 6 | USABLE | Pair with the page-006 render for Table 2 and Figure 2 visual verification. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/normalized_text/page-007.txt | Native PDF text | PDF-001 page 7 | USABLE | Pair with the page-007 render for Table 3 visual verification. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/normalized_text/page-008.txt | Native PDF text | PDF-001 page 8 | USABLE | Pair with the page-008 render for Figure 3 visual verification. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/normalized_text/page-009.txt | Native PDF text | PDF-001 page 9 | USABLE | Direct-PDF confirmation remains required for any cited evidence. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/normalized_text/page-010.txt | Native PDF text | PDF-001 page 10 | USABLE | Direct-PDF confirmation remains required for any cited evidence. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/page_images/page-001.png | Rendered PDF page | PDF-001 page 1 | STALE | The image filename maps it to page 1, but the page manifest does not register this render. It is not needed because native text is usable. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/page_images/page-003.png | Rendered PDF page | PDF-001 page 3 | USABLE | Registered visual aid for Figure 1 participant flow. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/page_images/page-005.png | Rendered PDF page | PDF-001 page 5 | USABLE | Registered visual aid for Table 1. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/page_images/page-006.png | Rendered PDF page | PDF-001 page 6 | USABLE | Registered visual aid for Table 2 and Figure 2. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/page_images/page-007.png | Rendered PDF page | PDF-001 page 7 | USABLE | Registered visual aid for Table 3. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/preprocessing/page_images/page-008.png | Rendered PDF page | PDF-001 page 8 | USABLE | Registered visual aid for Figure 3. |
| .ai_paper_validation/document_outputs/jama-2024-2302-supp3-results/preprocessing/normalized_text/page-002.txt | Native PDF text | PDF-004 page 2 | PARTIAL | Corrupted glyph mappings; use only as a locator and confirm against page render/direct PDF. |
| .ai_paper_validation/document_outputs/jama-2024-2302-supp3-results/preprocessing/normalized_text/page-003.txt | Native PDF text | PDF-004 page 3 | PARTIAL | Corrupted glyph mappings; use only as a locator and confirm against page render/direct PDF. |
| .ai_paper_validation/document_outputs/jama-2024-2302-supp3-results/preprocessing/normalized_text/page-004.txt | Native PDF text | PDF-004 page 4 | PARTIAL | Sparse and corrupted; use only as a locator and confirm against page render/direct PDF. |
| .ai_paper_validation/document_outputs/jama-2024-2302-supp3-results/preprocessing/normalized_text/page-005.txt | Native PDF text | PDF-004 page 5 | PARTIAL | Corrupted glyph mappings; use only as a locator and confirm against page render/direct PDF. |
| .ai_paper_validation/document_outputs/jama-2024-2302-supp3-results/preprocessing/page_images/page-002.png | Rendered PDF page | PDF-004 page 2 | USABLE | Visual source aid for eTable 1; direct PDF remains authoritative. |
| .ai_paper_validation/document_outputs/jama-2024-2302-supp3-results/preprocessing/page_images/page-003.png | Rendered PDF page | PDF-004 page 3 | USABLE | Visual source aid for eTable 1 continuation; direct PDF remains authoritative. |
| .ai_paper_validation/document_outputs/jama-2024-2302-supp3-results/preprocessing/page_images/page-004.png | Rendered PDF page | PDF-004 page 4 | USABLE | Visual source aid for eTable 1 continuation; direct PDF remains authoritative. |
| .ai_paper_validation/document_outputs/jama-2024-2302-supp3-results/preprocessing/page_images/page-005.png | Rendered PDF page | PDF-004 page 5 | USABLE | Visual source aid for eTable 2; direct PDF remains authoritative. |
| .ai_paper_validation/document_outputs/jama-2024-2302-main-article/document_record.json | Document record | PDF-001 pages 1-10 | USABLE | Source identity and all-page extraction map only; not a replacement for page evidence. |
| .ai_paper_validation/document_outputs/jama-2024-2302-supp1-protocol/document_record.json | Document record | PDF-002 pages 1-25 | PARTIAL | Records identity and page count but no scientific extraction; fresh mapping of all pages is required. |
| .ai_paper_validation/document_outputs/jama-2024-2302-supp2-sap/document_record.json | Document record | PDF-003 pages 1-10 | PARTIAL | Records identity and page count but no scientific extraction; fresh mapping of all pages is required. |
| .ai_paper_validation/document_outputs/jama-2024-2302-supp3-results/document_record.json | Document record | PDF-004 pages 1-8 | PARTIAL | Maps only pages 2-5 to derivatives; pages 1 and 6-8 require fresh mapping. |
| .ai_paper_validation/document_outputs/package_manifest.json | Package-level document record | PDF-001 pages 1-10; PDF-002 pages 1-25; PDF-003 pages 1-10; PDF-004 pages 1-8 | PARTIAL | It omits DOCX-001 and reflects an earlier limited audit scope; use only for source identity and prior derivative locations. |
| .ai_paper_validation/page_extraction_manifest.json | Page manifest and source-location map | PDF-001 pages 1-10; PDF-004 pages 2-5 | PARTIAL | It identifies usable page assets for 14 units, records quality limitations for PDF-004 text, and leaves PDF-002, PDF-003, PDF-004 pages 1 and 6-8, and DOCX-001 uncovered. |

## Asset counts and coverage

- Reusable assets inventoried and hashed: 30.
- USABLE assets: 21.
- PARTIAL assets: 8.
- STALE assets: 1.
- DUPLICATE assets: 0.
- UNREADABLE assets: 0.
- Reusable source coverage: PDF-001 pages 1-10 and PDF-004 pages 2-5, for 14 unique units.
- Fresh-required source coverage: PDF-002 pages 1-25, PDF-003 pages 1-10, PDF-004 pages 1 and 6-8, and DOCX-001 paragraphs 1-237, for 276 unique units.

The rendered PDF-004 pages make the four covered supplement pages reusable-backed even though their paired native text is PARTIAL. The downstream mapper must visually confirm values against the direct PDF and must not rely on corrupted glyphs as source wording.
