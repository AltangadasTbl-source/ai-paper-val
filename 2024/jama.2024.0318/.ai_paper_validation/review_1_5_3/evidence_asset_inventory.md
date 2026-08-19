# Reused Evidence-Asset Inventory

Inventory boundary: existing artifacts below `.ai_paper_validation/document_outputs/`. Old candidate, verifier, critic, endetail, and final-report content was not read or used as a discovery scope. The inventory contains every existing native/layout text, rendered page, page manifest, document record, and package source-location map. No OCR text, table/workbook extraction, DOC/DOCX extraction, workbook extraction, CSV extraction, or separate native-text/layout-text asset exists outside the listed page text files.

Fitness terms: **USABLE** means source-matched and adequate as a locator/transcription aid; **PARTIAL** means exact but insufficient alone; **STALE**, **DUPLICATE**, and **UNREADABLE** mean no such asset was found in this package.

## Document records and source-location maps

| Asset path | Asset class and method | Exact source location(s) | Fitness | Coverage and gap |
|---|---|---|---|---|
| document_outputs/package_manifest.md | Package source-location map; prior local filename and PDF-metadata inventory | DOC-001 PDF pp. 1-11; DOC-002 pp. 1-65; DOC-003 pp. 1-22; DOC-004 p. 1 | PARTIAL | Maps all four documents and page totals, but not page-level evidence; it cannot substitute for fresh mapping. |
| document_outputs/DOC-001/document_record.md | Document record; local PDF metadata and preprocessing description | DOC-001 PDF pp. 1-11 | PARTIAL | Identifies source and complete legacy preprocessing but contains no page-level evidence values. |
| document_outputs/DOC-002/document_record.md | Document record; local PDF metadata | DOC-002 PDF pp. 1-65 | PARTIAL | Identifies source only; all 65 pages remain fresh-required. |
| document_outputs/DOC-003/document_record.md | Document record; local PDF metadata and preprocessing description | DOC-003 PDF pp. 1-22 | PARTIAL | Identifies source and legacy pp. 8-22 processing but leaves pp. 1-7 uncovered. |
| document_outputs/DOC-004/document_record.md | Document record; local PDF metadata | DOC-004 PDF p. 1 | PARTIAL | Identifies source only; p. 1 remains fresh-required. |
| document_outputs/DOC-001/preprocessing/page_manifest.md | Page manifest; Poppler layout extraction and selected 200-dpi rendering map | DOC-001 PDF pp. 1-11; visual derivatives pp. 3-8 | USABLE | Exact one-to-one page mapping for all DOC-001 text assets and renders. |
| document_outputs/DOC-003/preprocessing/page_manifest.md | Page manifest; Poppler layout extraction and 200-dpi rendering map | DOC-003 PDF pp. 8-22; records no derivative for pp. 1-7 | USABLE | Exact one-to-one mapping for existing assets; explicitly establishes pp. 1-7 as a gap. |

## Native/layout text assets

Method for each file: Poppler `pdftotext -layout`, UTF-8 text. All paths below are individual assets and map one-to-one to their stated PDF page.

| Asset path | Exact source page | Fitness | Coverage and gap |
|---|---:|---|---|
| document_outputs/DOC-001/preprocessing/normalized_text/page-001.txt | DOC-001 p. 1 | USABLE | Native text adequate. |
| document_outputs/DOC-001/preprocessing/normalized_text/page-002.txt | DOC-001 p. 2 | USABLE | Native text adequate. |
| document_outputs/DOC-001/preprocessing/normalized_text/page-003.txt | DOC-001 p. 3 | USABLE | Native text adequate; render also available. |
| document_outputs/DOC-001/preprocessing/normalized_text/page-004.txt | DOC-001 p. 4 | USABLE | Native text adequate; render also available. |
| document_outputs/DOC-001/preprocessing/normalized_text/page-005.txt | DOC-001 p. 5 | USABLE | Native text adequate; render also available. |
| document_outputs/DOC-001/preprocessing/normalized_text/page-006.txt | DOC-001 p. 6 | USABLE | Native text adequate; render also available. |
| document_outputs/DOC-001/preprocessing/normalized_text/page-007.txt | DOC-001 p. 7 | USABLE | Native text adequate; render also available. |
| document_outputs/DOC-001/preprocessing/normalized_text/page-008.txt | DOC-001 p. 8 | USABLE | Native text adequate; render also available. |
| document_outputs/DOC-001/preprocessing/normalized_text/page-009.txt | DOC-001 p. 9 | USABLE | Native text adequate. |
| document_outputs/DOC-001/preprocessing/normalized_text/page-010.txt | DOC-001 p. 10 | USABLE | Native text adequate. |
| document_outputs/DOC-001/preprocessing/normalized_text/page-011.txt | DOC-001 p. 11 | USABLE | Native text adequate. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-008.txt | DOC-003 p. 8 | PARTIAL | Sparse figure text; exact render is usable visual evidence. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-009.txt | DOC-003 p. 9 | PARTIAL | Sparse figure text; exact render is usable visual evidence. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-010.txt | DOC-003 p. 10 | PARTIAL | Sparse figure text; exact render is usable visual evidence. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-011.txt | DOC-003 p. 11 | PARTIAL | Sparse figure text; exact render is usable visual evidence. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-012.txt | DOC-003 p. 12 | PARTIAL | Sparse figure text; exact render is usable visual evidence. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-013.txt | DOC-003 p. 13 | PARTIAL | Partial figure text; exact render is usable visual evidence. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-014.txt | DOC-003 p. 14 | USABLE | Table text adequate. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-015.txt | DOC-003 p. 15 | USABLE | Table text adequate. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-016.txt | DOC-003 p. 16 | USABLE | Table continuation/footnote text adequate. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-017.txt | DOC-003 p. 17 | USABLE | Table text adequate. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-018.txt | DOC-003 p. 18 | USABLE | Table text adequate. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-019.txt | DOC-003 p. 19 | USABLE | Table text adequate. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-020.txt | DOC-003 p. 20 | USABLE | Table continuation text adequate. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-021.txt | DOC-003 p. 21 | USABLE | Table text adequate. |
| document_outputs/DOC-003/preprocessing/normalized_text/page-022.txt | DOC-003 p. 22 | USABLE | Table text adequate. |

## Rendered-page assets

Method for each file: source-matched 200-dpi PNG rendering. Each is an individual page asset and remains a locator/visual aid; direct PDF remains the authority.

| Asset path | Exact source page | Fitness | Coverage and gap |
|---|---:|---|---|
| document_outputs/DOC-001/preprocessing/page_images/page-003.png | DOC-001 p. 3 | USABLE | Visual confirmation for Figure 1 and page evidence. |
| document_outputs/DOC-001/preprocessing/page_images/page-004.png | DOC-001 p. 4 | USABLE | Visual confirmation for Table 1 and page evidence. |
| document_outputs/DOC-001/preprocessing/page_images/page-005.png | DOC-001 p. 5 | USABLE | Visual confirmation for Figure 2 and page evidence. |
| document_outputs/DOC-001/preprocessing/page_images/page-006.png | DOC-001 p. 6 | USABLE | Visual confirmation for Table 2 and page evidence. |
| document_outputs/DOC-001/preprocessing/page_images/page-007.png | DOC-001 p. 7 | USABLE | Visual confirmation for Figure 3 and page evidence. |
| document_outputs/DOC-001/preprocessing/page_images/page-008.png | DOC-001 p. 8 | USABLE | Visual confirmation for Table 3 and page evidence. |
| document_outputs/DOC-003/preprocessing/page_images/page-008.png | DOC-003 p. 8 | USABLE | Required visual evidence for eFigure 1. |
| document_outputs/DOC-003/preprocessing/page_images/page-009.png | DOC-003 p. 9 | USABLE | Required visual evidence for eFigure 2. |
| document_outputs/DOC-003/preprocessing/page_images/page-010.png | DOC-003 p. 10 | USABLE | Required visual evidence for eFigure 3. |
| document_outputs/DOC-003/preprocessing/page_images/page-011.png | DOC-003 p. 11 | USABLE | Required visual evidence for eFigure 4. |
| document_outputs/DOC-003/preprocessing/page_images/page-012.png | DOC-003 p. 12 | USABLE | Required visual evidence for eFigure 5. |
| document_outputs/DOC-003/preprocessing/page_images/page-013.png | DOC-003 p. 13 | USABLE | Required visual evidence for eFigure 6. |
| document_outputs/DOC-003/preprocessing/page_images/page-014.png | DOC-003 p. 14 | USABLE | Visual confirmation for eTable 1. |
| document_outputs/DOC-003/preprocessing/page_images/page-015.png | DOC-003 p. 15 | USABLE | Visual confirmation for eTable 2. |
| document_outputs/DOC-003/preprocessing/page_images/page-016.png | DOC-003 p. 16 | USABLE | Visual confirmation for eTable 2 continuation. |
| document_outputs/DOC-003/preprocessing/page_images/page-017.png | DOC-003 p. 17 | USABLE | Visual confirmation for eTable 3. |
| document_outputs/DOC-003/preprocessing/page_images/page-018.png | DOC-003 p. 18 | USABLE | Visual confirmation for eTable 4. |
| document_outputs/DOC-003/preprocessing/page_images/page-019.png | DOC-003 p. 19 | USABLE | Visual confirmation for eTable 5. |
| document_outputs/DOC-003/preprocessing/page_images/page-020.png | DOC-003 p. 20 | USABLE | Visual confirmation for eTable 5 continuation. |
| document_outputs/DOC-003/preprocessing/page_images/page-021.png | DOC-003 p. 21 | USABLE | Visual confirmation for eTable 6. |
| document_outputs/DOC-003/preprocessing/page_images/page-022.png | DOC-003 p. 22 | USABLE | Visual confirmation for eTable 7. |

## Asset totals and limitations

| Asset class | Count | USABLE | PARTIAL | STALE | DUPLICATE | UNREADABLE |
|---|---:|---:|---:|---:|---:|---:|
| Document records | 4 | 0 | 4 | 0 | 0 | 0 |
| Package source-location maps | 1 | 0 | 1 | 0 | 0 | 0 |
| Page manifests | 2 | 2 | 0 | 0 | 0 | 0 |
| Native/layout page text | 26 | 20 | 6 | 0 | 0 | 0 |
| Rendered pages | 21 | 21 | 0 | 0 | 0 | 0 |
| OCR text | 0 | 0 | 0 | 0 | 0 | 0 |
| Table/workbook extraction | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **54** | **43** | **11** | **0** | **0** | **0** |

No legacy asset is stale, duplicate, or unreadable. The 11 PARTIAL map/record/native-text assets are never used as complete page evidence by themselves; uncovered source pages and native-text gaps are explicitly routed in `source_coverage.md`.
