# Reused Evidence-Asset Inventory

This inventory covers every reusable OCR/native text, rendered page, OCR metadata, document record, preprocessing manifest, package manifest, and pre-existing source-linked evidence map below the prior audit area. The accompanying `reused_artifact_hashes_before.sha256` enumerates and hashes all 57 individual files. Old candidate, checker, verifier, critic, quality, adjudication, and final-report content was not used as discovery scope and is not included as a reusable evidence asset.

Fitness labels: `USABLE` means page-matched and fit as a locator/transcription aid; `PARTIAL` means useful but not complete enough to close an independent source-unit gap; `STALE` means metadata/scope is inconsistent with the current full-coverage contract or an observed artifact; `DUPLICATE` means it adds no unit coverage beyond a stronger reusable asset; `UNREADABLE` was not encountered.

| Individual artifact path or exact path set | Asset type | Exact source location(s) | Fitness | Coverage / fitness assessment and gap action |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/package_manifest.json | Package document map | DOC-001 pp. 1-10; DOC-002 pp. 1-76; DOC-003 pp. 1-13; DOC-004 p. 1 | STALE | Correct filenames, IDs, and page counts, but its old “Not Audited by Design” scopes for DOC-002 and DOC-004 cannot define this run. Fresh-map DOC-002 pp. 1-76 and DOC-004 p. 1. |
| .ai_paper_validation/document_outputs/DOC-001/document_record.json | Document record | DOC-001 pp. 1-10 | USABLE | Hash-bound document identity, page count, text-layer availability, and page scope; supports all DOC-001 page locations but does not replace native text. |
| .ai_paper_validation/document_outputs/DOC-001/preprocessing_manifest.json | Page/source-location map | DOC-001 pp. 1-10; render/OCR detail pp. 4-7 | PARTIAL | Correct native-text and render mapping; its OCR completed-pages list says pp. 4-5 while present metadata/text also cover pp. 6-7. Use actual page-matched files; do not rely on this list for coverage. |
| .ai_paper_validation/document_outputs/DOC-001/main_text_extractor_evidence.md | Source-linked extraction map | DOC-001 pp. 1-10 | PARTIAL | Result-focused locator map with page citations, useful for navigation only. It is not a full transcription or an independently hash-bound replacement for native page text. |
| .ai_paper_validation/document_outputs/DOC-002/document_record.json | Document record | DOC-002 pp. 1-76 | PARTIAL | Verifies file identity, page count, and text-layer availability, but its former exclusion is not reusable source extraction. Fresh-map every page. |
| .ai_paper_validation/document_outputs/DOC-002/preprocessing_manifest.json | Preprocessing map | DOC-002 pp. 1-76 | STALE | States no asset was created and an obsolete exclusion. It provides no reusable page evidence; fresh-map every page. |
| .ai_paper_validation/document_outputs/DOC-003/document_record.json | Document record | DOC-003 pp. 1-13 | USABLE | Hash-bound document identity, page count, and text-layer availability; supports page matching but does not replace native text. |
| .ai_paper_validation/document_outputs/DOC-003/preprocessing_manifest.json | Page/source-location map | DOC-003 pp. 1-13; renders pp. 4-13 | USABLE | Correctly maps complete native text and visual renders; sparse native output on figure/table-continuation pages is expected and should be paired with the render. |
| .ai_paper_validation/document_outputs/DOC-003/results_supplement_evidence_map.md | Source-linked extraction map | DOC-003 pp. 1-13 | PARTIAL | Result-focused locator map with page citations; useful for navigation, but it is not a complete page extraction. Native page text closes reusable coverage. |
| .ai_paper_validation/document_outputs/DOC-004/document_record.json | Document record | DOC-004 p. 1 | PARTIAL | Verifies source identity and text-layer availability, but supplies no reusable page extraction. Fresh-map p. 1. |
| .ai_paper_validation/document_outputs/DOC-004/preprocessing_manifest.json | Preprocessing map | DOC-004 p. 1 | STALE | States no asset and obsolete exclusion; no reusable page evidence. Fresh-map p. 1. |
| .ai_paper_validation/preprocessing/ocr_backend.json | OCR run record | DOC-001 pp. 4-7 only | STALE | Records CPU RapidOCR environment but not a complete current page map; use the individual page metadata for OCR provenance. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page_001.txt | Native text | DOC-001 PDF p. 1 | USABLE | Page-matched nonempty native text; reusable-backed. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page_002.txt | Native text | DOC-001 PDF p. 2 | USABLE | Page-matched nonempty native text; reusable-backed. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page_003.txt | Native text | DOC-001 PDF p. 3 | USABLE | Page-matched nonempty native text; reusable-backed. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page_004.txt | Native text | DOC-001 PDF p. 4 | USABLE | Page-matched nonempty native text; reusable-backed; render is available for the figure. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page_005.txt | Native text | DOC-001 PDF p. 5 | USABLE | Page-matched nonempty native text; reusable-backed; render is available for Table 1. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page_006.txt | Native text | DOC-001 PDF p. 6 | USABLE | Page-matched nonempty native text; reusable-backed; render is available for table confirmation. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page_007.txt | Native text | DOC-001 PDF p. 7 | USABLE | Page-matched nonempty native text; reusable-backed; render is available for table confirmation. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page_008.txt | Native text | DOC-001 PDF p. 8 | USABLE | Page-matched nonempty native text; reusable-backed. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page_009.txt | Native text | DOC-001 PDF p. 9 | USABLE | Page-matched nonempty native text; reusable-backed. |
| .ai_paper_validation/preprocessing/DOC-001/native_text/page_010.txt | Native text | DOC-001 PDF p. 10 | USABLE | Page-matched nonempty native text; reusable-backed. |
| .ai_paper_validation/preprocessing/DOC-001/page_images/page_004.png | Rendered page | DOC-001 PDF p. 4 | USABLE | 300-dpi visual confirmation for the figure; supplements native text and does not add a separate unit. |
| .ai_paper_validation/preprocessing/DOC-001/page_images/page_005.png | Rendered page | DOC-001 PDF p. 5 | USABLE | 300-dpi visual confirmation for Table 1; supplements native text and does not add a separate unit. |
| .ai_paper_validation/preprocessing/DOC-001/page_images/page_006.png | Rendered page | DOC-001 PDF p. 6 | USABLE | 300-dpi visual confirmation for table content; supplements native text and does not add a separate unit. |
| .ai_paper_validation/preprocessing/DOC-001/page_images/page_007.png | Rendered page | DOC-001 PDF p. 7 | USABLE | 300-dpi visual confirmation for table content; supplements native text and does not add a separate unit. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_text/page_004.txt | OCR text | DOC-001 PDF p. 4 | DUPLICATE | Completed CPU OCR (metadata confidence 0.896); native text and render are stronger reusable coverage. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_text/page_005.txt | OCR text | DOC-001 PDF p. 5 | DUPLICATE | Completed CPU OCR (metadata confidence 0.886); native text and render are stronger reusable coverage. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_text/page_006.txt | OCR text | DOC-001 PDF p. 6 | DUPLICATE | Completed CPU OCR (metadata confidence 0.873); native text and render are stronger reusable coverage. |
| .ai_paper_validation/preprocessing/DOC-001/ocr_text/page_007.txt | OCR text | DOC-001 PDF p. 7 | DUPLICATE | Completed CPU OCR (metadata confidence 0.868); native text and render are stronger reusable coverage. |
| .ai_paper_validation/preprocessing/DOC-001/page_ocr_metadata/page_004.json | OCR page manifest | DOC-001 PDF p. 4 | USABLE | Confirms source render, output path, completion, and confidence for OCR p. 4. |
| .ai_paper_validation/preprocessing/DOC-001/page_ocr_metadata/page_005.json | OCR page manifest | DOC-001 PDF p. 5 | USABLE | Confirms source render, output path, completion, and confidence for OCR p. 5. |
| .ai_paper_validation/preprocessing/DOC-001/page_ocr_metadata/page_006.json | OCR page manifest | DOC-001 PDF p. 6 | USABLE | Confirms source render, output path, completion, and confidence for OCR p. 6. |
| .ai_paper_validation/preprocessing/DOC-001/page_ocr_metadata/page_007.json | OCR page manifest | DOC-001 PDF p. 7 | USABLE | Confirms source render, output path, completion, and confidence for OCR p. 7. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_001.txt | Native text | DOC-003 PDF p. 1 | USABLE | Page-matched native text; reusable-backed. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_002.txt | Native text | DOC-003 PDF p. 2 | USABLE | Page-matched native text; reusable-backed. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_003.txt | Native text | DOC-003 PDF p. 3 | USABLE | Page-matched native text; reusable-backed. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_004.txt | Native text | DOC-003 PDF p. 4 | USABLE | Page-matched native text; reusable-backed; render supplies visual table confirmation. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_005.txt | Native text | DOC-003 PDF p. 5 | USABLE | Page-matched native text; reusable-backed; render supplies visual table confirmation. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_006.txt | Native text | DOC-003 PDF p. 6 | USABLE | Page-matched native text; reusable-backed; render supplies visual table confirmation. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_007.txt | Native text | DOC-003 PDF p. 7 | USABLE | Page-matched native text; reusable-backed; render supplies visual table confirmation. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_008.txt | Native text | DOC-003 PDF p. 8 | USABLE | Page-matched native text; reusable-backed; render supplies visual table confirmation. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_009.txt | Native text | DOC-003 PDF p. 9 | USABLE | Sparse table-continuation text is expected; render supplies visual confirmation. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_010.txt | Native text | DOC-003 PDF p. 10 | USABLE | Page-matched native text; reusable-backed; render supplies visual table confirmation. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_011.txt | Native text | DOC-003 PDF p. 11 | USABLE | Page-matched native text; reusable-backed; render supplies visual table confirmation. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_012.txt | Native text | DOC-003 PDF p. 12 | USABLE | Sparse figure-page text is expected; render supplies visual confirmation. |
| .ai_paper_validation/preprocessing/DOC-003/native_text/page_013.txt | Native text | DOC-003 PDF p. 13 | USABLE | Sparse figure-page text is expected; render supplies visual confirmation. |
| .ai_paper_validation/preprocessing/DOC-003/page_images/page_004.png | Rendered page | DOC-003 PDF p. 4 | USABLE | 300-dpi visual confirmation for eTable 1; supplements native text. |
| .ai_paper_validation/preprocessing/DOC-003/page_images/page_005.png | Rendered page | DOC-003 PDF p. 5 | USABLE | 300-dpi visual confirmation for eTable 2; supplements native text. |
| .ai_paper_validation/preprocessing/DOC-003/page_images/page_006.png | Rendered page | DOC-003 PDF p. 6 | USABLE | 300-dpi visual confirmation for eTable 3; supplements native text. |
| .ai_paper_validation/preprocessing/DOC-003/page_images/page_007.png | Rendered page | DOC-003 PDF p. 7 | USABLE | 300-dpi visual confirmation for eTable 4; supplements native text. |
| .ai_paper_validation/preprocessing/DOC-003/page_images/page_008.png | Rendered page | DOC-003 PDF p. 8 | USABLE | 300-dpi visual confirmation for eTable 5; supplements native text. |
| .ai_paper_validation/preprocessing/DOC-003/page_images/page_009.png | Rendered page | DOC-003 PDF p. 9 | USABLE | 300-dpi visual confirmation for eTable 5 continuation; supplements sparse native text. |
| .ai_paper_validation/preprocessing/DOC-003/page_images/page_010.png | Rendered page | DOC-003 PDF p. 10 | USABLE | 300-dpi visual confirmation for eTable 6; supplements native text. |
| .ai_paper_validation/preprocessing/DOC-003/page_images/page_011.png | Rendered page | DOC-003 PDF p. 11 | USABLE | 300-dpi visual confirmation for eTable 6 continuation; supplements native text. |
| .ai_paper_validation/preprocessing/DOC-003/page_images/page_012.png | Rendered page | DOC-003 PDF p. 12 | USABLE | 300-dpi visual confirmation for eFigure 1; supplements sparse native text. |
| .ai_paper_validation/preprocessing/DOC-003/page_images/page_013.png | Rendered page | DOC-003 PDF p. 13 | USABLE | 300-dpi visual confirmation for eFigure 2; supplements sparse native text. |

## Asset-count summary

- Hashed reusable assets: 57 individual files.
- Native-text files: 23 (DOC-001 pp. 1-10; DOC-003 pp. 1-13), all `USABLE`.
- Rendered-page files: 14 (DOC-001 pp. 4-7; DOC-003 pp. 4-13), all `USABLE`.
- OCR text files: 4 (DOC-001 pp. 4-7), all `DUPLICATE` to stronger native text plus renders.
- OCR page-metadata files: 4 (DOC-001 pp. 4-7), all `USABLE` as provenance.
- Document/package/preprocessing maps, source-linked extraction maps, and the OCR run record: 12 files; 3 `USABLE`, 5 `PARTIAL`, and 4 `STALE`.
- Table/workbook extraction files: 0. Layout-text files: 0. No `UNREADABLE` reusable asset was found.

## Coverage conclusion

The unique reusable source coverage is 23 of 100 PDF-page units, derived only from the complete native-text sets. All other source units are explicitly fresh-required: DOC-002 pp. 1-76 and DOC-004 p. 1. Reused renders and OCR remain available for visual/source confirmation but do not double-count source units.
