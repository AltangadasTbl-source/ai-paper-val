# Reused Evidence-Asset Inventory

## Method and boundary

This inventory covers every eligible pre-existing OCR/native text, rendered page, page/document map, table/workbook extraction, and document record below `.ai_paper_validation/document_outputs`. It excludes prior candidate, queue, verifier, critic, endetail, quality, and final-report artifacts from scientific discovery. SHA-256 values for all listed inventory inputs are recorded in `reused_artifact_hashes_before.sha256`; paths are package-relative. Direct source remains authoritative for all later confirmation.

Fitness meanings: `USABLE` reliably maps the stated unit(s); `PARTIAL` has a known coverage or legibility gap; `DUPLICATE` is supplementary to a canonical derivative; `STALE` is a prior-scope record that supplies no current scientific extraction; `UNREADABLE` was not observed.

| Asset path(s) | Asset kind / method | Exact source units or locations | Fitness | Curation disposition |
|---|---|---|---|---|
| `.ai_paper_validation/document_outputs/DOC-001-MAIN/inventory_record.md` | document record | DOC-001 PDF pp. 1-14 | USABLE | Source identity and complete page scope retained. |
| `.ai_paper_validation/document_outputs/DOC-001-MAIN/preprocessing_record.md` | preprocessing record | DOC-001 PDF pp. 1-14 | USABLE | Records all-page native extraction and selective visual/OCR support. |
| `.ai_paper_validation/document_outputs/DOC-001-MAIN/page_manifest.json` | page/source-location map | DOC-001 PDF pp. 1-14 | USABLE | Canonical machine-readable page-to-derivative map. |
| `.ai_paper_validation/document_outputs/DOC-001-MAIN/page_manifest.md` | page/source-location map | DOC-001 PDF pp. 1-14 | DUPLICATE | Human-readable duplicate of the JSON page map. |
| `.ai_paper_validation/document_outputs/DOC-001-MAIN/main_text_evidence.md` | result-location map / table extraction | DOC-001 PDF pp. 1-11 (with cited table and figure locations) | USABLE | Locator only; mapper must retain pp. 12-14 through canonical page text. |
| `.ai_paper_validation/document_outputs/DOC-001-MAIN/normalized_text/page_001.txt` through `page_008.txt`, `page_012.txt` through `page_014.txt` | native normalized text | DOC-001 PDF pp. 1-8, 12-14 | USABLE | Canonical reusable text for 11 pages. |
| `.ai_paper_validation/document_outputs/DOC-001-MAIN/normalized_text/page_009.txt`, `page_010.txt`, `page_011.txt` | coordinate-reconstructed normalized text | DOC-001 PDF pp. 9-11 | USABLE | Canonical table-page text; visual derivative available for direct confirmation. |
| `.ai_paper_validation/document_outputs/DOC-001-MAIN/normalized_text/page_009.native.txt`, `page_010.native.txt`, `page_011.native.txt` | raw native text | DOC-001 PDF pp. 9-11 | DUPLICATE | Reversed/rotated raw text; retained only as reconstruction provenance. |
| `.ai_paper_validation/document_outputs/DOC-001-MAIN/normalized_text/page_009.ocr.txt`, `page_010.ocr.txt`, `page_011.ocr.txt` | OCR check text | DOC-001 PDF pp. 9-11 | DUPLICATE | Supplemental OCR checks beside canonical reconstructed text. |
| `.ai_paper_validation/document_outputs/DOC-001-MAIN/page_images/page_005.png` through `page_011.png` | rendered PDF pages | DOC-001 PDF pp. 5-11 | USABLE | Visual confirmation for result tables, figures, and flow diagram. |
| `.ai_paper_validation/document_outputs/DOC-002-PROTOCOL/inventory_record.md`, `preprocessing_record.md` | document and preprocessing records | DOC-002 PDF pp. 1-77 | USABLE | Establish identity, unit count, and absence of usable scientific derivative. |
| `.ai_paper_validation/document_outputs/DOC-002-PROTOCOL/results_evidence.md` | prior-scope record | DOC-002 PDF pp. 1-77 | STALE | States “Not Audited by Design”; it supplies no source extraction for this complete review. |
| `.ai_paper_validation/document_outputs/DOC-003-SAP/inventory_record.md`, `preprocessing_record.md` | document and preprocessing records | DOC-003 PDF pp. 1-29 | USABLE | Establish identity, unit count, and absence of usable scientific derivative. |
| `.ai_paper_validation/document_outputs/DOC-003-SAP/results_evidence.md` | prior-scope record | DOC-003 PDF pp. 1-29 | STALE | States “Not Audited by Design”; it supplies no source extraction for this complete review. |
| `.ai_paper_validation/document_outputs/DOC-004-INTERVENTION/inventory_record.md`, `preprocessing_record.md` | document and preprocessing records | DOC-004 PDF pp. 1-7 | USABLE | Establish identity, unit count, and absence of usable scientific derivative. |
| `.ai_paper_validation/document_outputs/DOC-004-INTERVENTION/results_evidence.md` | prior-scope record | DOC-004 PDF pp. 1-7 | STALE | States “Not Audited by Design”; it supplies no source extraction for this complete review. |
| `.ai_paper_validation/document_outputs/DOC-005-RESULTS/inventory_record.md`, `preprocessing_record.md` | document and preprocessing records | DOC-005 PDF pp. 1-19 | USABLE | Records an older selected scope limited to p. 2-18; this exposes pp. 1 and 19 as gaps. |
| `.ai_paper_validation/document_outputs/DOC-005-RESULTS/page_manifest.json` | page/source-location map | DOC-005 PDF pp. 2-18 | PARTIAL | Exact mapping for 17 pages only; p. 12 is sparse and pp. 1/19 are absent. |
| `.ai_paper_validation/document_outputs/DOC-005-RESULTS/page_manifest.md` | page/source-location map | DOC-005 PDF pp. 2-18 | DUPLICATE | Human-readable duplicate of the JSON page map. |
| `.ai_paper_validation/document_outputs/DOC-005-RESULTS/results_evidence.md` | result-location map / table extraction | DOC-005 PDF pp. 2-18 | PARTIAL | Useful locator, but not a substitute for p. 12 recovery or direct mapping of pp. 1 and 19. |
| `.ai_paper_validation/document_outputs/DOC-005-RESULTS/normalized_text/page_002.txt` through `page_011.txt`, and `page_013.txt` through `page_018.txt` | native normalized text | DOC-005 PDF pp. 2-11 and 13-18 | USABLE | Canonical reusable text for 16 pages. |
| `.ai_paper_validation/document_outputs/DOC-005-RESULTS/normalized_text/page_003.ocr.txt` | OCR check text | DOC-005 PDF p. 3 | DUPLICATE | Supplemental recovery/check text beside the p. 3 canonical normalized text. |
| `.ai_paper_validation/document_outputs/DOC-005-RESULTS/normalized_text/page_012.txt` | sparse native normalized text | DOC-005 PDF p. 12 | PARTIAL | 119 nonspace characters; requires fresh direct-source recovery/mapping. |
| `.ai_paper_validation/document_outputs/DOC-005-RESULTS/page_images/page_003.png`, `page_007.png` through `page_011.png`, and `page_014.png` through `page_018.png` | rendered PDF pages | DOC-005 PDF pp. 3, 7-11, 14-18 | USABLE | Visual table/figure confirmation for 11 pages. |
| `.ai_paper_validation/document_outputs/DOC-006-XLSX/inventory_record.md`, `preprocessing_record.md` | workbook document/preprocessing records | DOC-006 worksheet `eTable 3` | USABLE | Establishes workbook identity, worksheet, and 115-row × 10-column structure. |
| `.ai_paper_validation/document_outputs/DOC-006-XLSX/results_evidence.md` | workbook source-location map | DOC-006 `eTable 3`, A1:J115 | USABLE | Complete worksheet range map and result-relevant grouped cell locations; native workbook remains authoritative. |

## Coverage decision

| Source ID | Reusable source units | Fresh-required source units | Exact fresh gap |
|---|---:|---:|---|
| DOC-001 | 14 | 0 | None. |
| DOC-002 | 0 | 77 | PDF pp. 1-77; no native/layout/OCR/rendered/table derivative exists. |
| DOC-003 | 0 | 29 | PDF pp. 1-29; no native/layout/OCR/rendered/table derivative exists. |
| DOC-004 | 0 | 7 | PDF pp. 1-7; no native/layout/OCR/rendered/table derivative exists. |
| DOC-005 | 16 | 3 | PDF pp. 1 and 19 absent; p. 12 has only PARTIAL sparse native text. |
| DOC-006 | 1 | 0 | None; existing workbook location map covers the sole worksheet. |

The Office structure artifacts under `.ai_paper_validation/review_1_5_1/preprocessing/office_structure/` were generated in this review, are fresh preprocessing rather than reusable evidence, and are intentionally excluded from this reuse inventory and hash set. No eligible asset was UNREADABLE. There are 78 hashed eligible audit-area assets: 32 DOC-001 assets, 3 DOC-002 assets, 3 DOC-003 assets, 3 DOC-004 assets, 34 DOC-005 assets, and 3 DOC-006 assets.

## Current-review fresh preprocessing provenance

- `sha256sum (uutils coreutils) 0.8.0` was used for direct-source and reused-artifact integrity checks.
- `pdfinfo 26.01.0` established PDF page counts; `pdftotext 26.01.0` generated native and layout text for DOC-002 through DOC-005 under `preprocessing/fresh_text/`.
- `LibreOffice 26.2.4.2` and the permitted `workflow_1_5_1/scripts/extract_office_source.py` helper extracted DOC-006 worksheet structure and a local inspection PDF under `preprocessing/office_structure/joi250046supp5/`.
- `tesseract 5.5.0` was available, but no coordinator-wide OCR run was required; mapper/rechecker artifacts document any targeted direct-page rendering or OCR used for visually complex pages.
- Representative commands were `pdftotext SOURCE.pdf preprocessing/fresh_text/DOC.native.txt`, `pdftotext -layout SOURCE.pdf preprocessing/fresh_text/DOC.layout.txt`, and `python3 workflow_1_5_1/scripts/extract_office_source.py SOURCE.xlsx preprocessing/office_structure/OUTPUT`. Exact source filenames and resulting paths are recorded in the source inventory and mapper artifacts.
