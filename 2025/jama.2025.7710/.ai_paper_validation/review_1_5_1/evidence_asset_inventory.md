# Reused-Evidence Asset Inventory — Workflow 1.5.1

Eligible assets below the pre-existing audit area were inventoried without reading legacy candidate, queue, verifier, critic, endetail, quality, or final-report outputs. The companion hash file enumerates all **43** eligible artifacts with package-relative paths and SHA-256 values.

## Fitness classification and exact coverage

| Asset group / exact package-relative paths | Method / source locations | Fitness | Coverage decision |
|---|---|---|---|
| `.ai_paper_validation/document_outputs/DOC-001/preprocessing/page_level_manifest.json`; `preprocessing/native_text_normalized.md`; `preprocessing/ocr_selected_pages_normalized.md`; `preprocessing/rendered_pages/page-004.{png,ocr.txt}` through `page-008.{png,ocr.txt}`; `preprocessing_record.md`; `initial_document_record.md`; `main_text_extraction.md` | Native text map: pp. 1-11; selected rendered/OCR aids: pp. 4-8; document and source-location records: pp. 1-11. The retained package manifest reports a prior DOC-001 source SHA-256 `0e600c...d922`, whereas the current direct file is `10ab2f...73e3`. | STALE | No page is reusable. DOC-001 pp. 1-11 are fresh-required. The pages 4-8 visual/OCR subset is also stale and may serve only as an untrusted locator after fresh direct mapping. |
| `.ai_paper_validation/document_outputs/DOC-002/initial_document_record.md`; `preprocessing_record.md`; `rights_screen_render/page1.png`; `page22.png`; `page23.png`; `page24.png`; `page26.png` | Document records identify 26 PDF pages but contain no per-page scientific extraction. Renders cover only pp. 1, 22-24, and 26 and are rights screens, not usable content extraction. | PARTIAL | No page is reusable for quantitative mapping; DOC-002 pp. 1-26 are fresh-required. The rights renders are retained provenance only. |
| `.ai_paper_validation/document_outputs/DOC-003/initial_document_record.md`; `preprocessing_record.md` | Document records identify the 29-page SAP and broad contents locations only; no native/layout text, page map, table extraction, or rendering exists. | PARTIAL | No page is reusable; DOC-003 pp. 1-29 are fresh-required. |
| `.ai_paper_validation/document_outputs/DOC-004/preprocessing/page_level_manifest.json`; `preprocessing/native_text_normalized.md`; `preprocessing/ocr_selected_pages_normalized.md`; `preprocessing/rendered_pages/page-002.{png,ocr.txt}` through `page-006.{png,ocr.txt}`; `preprocessing_record.md`; `initial_document_record.md`; `results_supplement_extraction.md` | Page manifest/native text cover pp. 1-6; rendered/OCR aids cover pp. 2-6; result table/source-location extraction maps p. 2 eTable 1, pp. 3-5 eTable 2, and p. 6 eTable 3. The retained package-manifest SHA-256 equals the current direct source (`16131d...6e80`). | USABLE | DOC-004 pp. 1-6 are reusable-backed, subject to direct-source confirmation for any later candidate. |
| `.ai_paper_validation/document_outputs/package_manifest.md`; `.ai_paper_validation/preprocessing_summary.md` | Package-level document and source-location maps; `package_manifest.md` maps DOC-001 pp. 1-11, DOC-002 pp. 1-26, DOC-003 pp. 1-29, DOC-004 pp. 1-6. `preprocessing_summary.md` summarizes DOC-001 and DOC-004 extraction coverage. | PARTIAL | Useful inventory provenance only. It cannot close page-level mapping gaps; its obsolete DOC-001 hash confirms the stale classification above. |

## Asset counts by fitness

- USABLE: 16 assets, all linked to DOC-004; reusable page coverage: 6 pages.
- STALE: 16 assets, all linked to DOC-001; reusable page coverage: 0 pages.
- PARTIAL: 11 assets: DOC-002 (7), DOC-003 (2), package-level maps (2); reusable page coverage: 0 pages.
- DUPLICATE: 0 assets. No byte-identical eligible asset pair was identified in the inventory.
- UNREADABLE: 0 assets. All files were readable to the direct file/hash tools; content fitness still governs reuse.

## Tools, commands, and limitations

- Commands: `find .ai_paper_validation/document_outputs -type f ...`; `sha256sum -- <each eligible asset>`; `pdfinfo -- <each direct PDF>`; `file --brief -- <each direct PDF>`; and read-only inspection of page manifests, records, normalized text, and source-location maps.
- Versions: `sha256sum (uutils coreutils) 0.8.0`; `pdfinfo version 26.01.0`; `pdftotext version 26.01.0`; `file-5.46`.
- Limitation: DOC-001 reusable derivatives cannot be trusted for current-source coverage because recorded and current source identities differ. DOC-002/DOC-003 have no usable page-level content extraction. No fresh extraction, OCR, source alteration, or scientific candidate diagnosis was performed in this curation stage.
