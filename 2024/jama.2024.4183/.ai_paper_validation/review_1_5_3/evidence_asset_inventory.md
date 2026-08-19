# Reused Evidence-Asset Inventory

This inventory includes only existing OCR text, native/layout text, table/workbook extraction, rendered pages, page manifests, document records, and source-location maps below the pre-existing audit area. Old candidate, checker, verifier, critic, endetail, and final-report content was not read or used as discovery scope. All listed files are individually hashed in `reused_artifact_hashes_before.sha256`.

## Inventory summary

| Asset class | Asset count | Exact source locations represented | Fitness | Coverage consequence |
|---|---:|---|---|---|
| Package source-location map | 1 | DOC-001 pp. 1-10; DOC-002 pp. 1-45; DOC-003 pp. 1-36 | PARTIAL | DOC-001 and DOC-003 entries cite source hashes that differ from current direct sources; DOC-002 identity is current but no extraction is supplied. |
| DOC-001 native text | 11 | PDF pp. 1-10: 10 page files and one combined file | STALE | Not reusable; current source requires fresh mapping for pp. 1-10. |
| DOC-001 rendered pages | 4 | PDF pp. 3, 5, 6, 7 | STALE | Not reusable; current source requires fresh mapping. |
| DOC-001 page manifest, document record, preprocessing summary | 3 | PDF pp. 1-10 | STALE | The files name a prior nonmatching DOC-001 hash. |
| DOC-002 document record and preprocessing summary | 2 | PDF pp. 1-45 | USABLE | Usable only as an identity/no-derivative map; all pp. 1-45 remain fresh-required. |
| DOC-003 native text | 33 | PDF pp. 4-35: 32 page files and one combined file | STALE | Not reusable; current source requires fresh mapping for pp. 4-35. |
| DOC-003 rendered pages | 22 | PDF pp. 14-35 | STALE | Not reusable; current source requires fresh mapping. |
| DOC-003 page manifest, document record, preprocessing summary | 3 | PDF pp. 4-35 | STALE | The files name a prior nonmatching DOC-003 hash. |
| OCR text | 0 | None | USABLE | No OCR artifact exists; no duplicate or unreadable OCR asset was found. |
| Layout text distinct from native text | 0 | None | USABLE | No distinct layout-text artifact exists. |
| Table/workbook extraction | 0 | None | USABLE | No table, workbook, or CSV extraction artifact exists. |

No asset was classified `DUPLICATE` or `UNREADABLE`. `USABLE` DOC-002 documentation is not an evidence extraction and provides zero reusable source units.

## Exact artifact paths and locations

| Asset set | Individual package-relative paths | Exact source location(s) | Method | Fitness |
|---|---|---|---|---|
| Package map | `.ai_paper_validation/document_outputs/package_manifest.md` | DOC-001 pp. 1-10; DOC-002 pp. 1-45; DOC-003 pp. 1-36 | Prior direct-PDF inventory and page map | PARTIAL |
| DOC-001 native page text | `.ai_paper_validation/document_outputs/DOC-001/preprocessing/native_text/page-001.txt` through `page-010.txt` | DOC-001 PDF pp. 1-10, one file per matching page | Prior `pdftotext -layout`, normalized | STALE |
| DOC-001 combined native text | `.ai_paper_validation/document_outputs/DOC-001/preprocessing/native_text/selected-pages-normalized.txt` | DOC-001 PDF pp. 1-10 | Prior combined normalized native text | STALE |
| DOC-001 renders | `.ai_paper_validation/document_outputs/DOC-001/preprocessing/page_images/page-003.jpg`, `page-005.jpg`, `page-006.jpg`, `page-007.jpg` | DOC-001 PDF pp. 3, 5, 6, 7 | Prior 200-dpi JPEG rendering | STALE |
| DOC-001 maps and records | `.ai_paper_validation/document_outputs/DOC-001/preprocessing/page_extraction_manifest.md`; `.ai_paper_validation/document_outputs/DOC-001/document_record.md`; `.ai_paper_validation/document_outputs/DOC-001/preprocessing_summary.md` | DOC-001 PDF pp. 1-10 | Prior page map and document/preprocessing records | STALE |
| DOC-002 maps and records | `.ai_paper_validation/document_outputs/DOC-002/document_record.md`; `.ai_paper_validation/document_outputs/DOC-002/preprocessing_summary.md` | DOC-002 PDF pp. 1-45 | Prior document and no-extraction record | USABLE |
| DOC-003 native page text | `.ai_paper_validation/document_outputs/DOC-003/preprocessing/native_text/page-004.txt` through `page-035.txt` | DOC-003 PDF pp. 4-35, one file per matching page | Prior `pdftotext -layout`, normalized | STALE |
| DOC-003 combined native text | `.ai_paper_validation/document_outputs/DOC-003/preprocessing/native_text/selected-pages-normalized.txt` | DOC-003 PDF pp. 4-35 | Prior combined normalized native text | STALE |
| DOC-003 renders | `.ai_paper_validation/document_outputs/DOC-003/preprocessing/page_images/page-014.jpg` through `page-035.jpg` | DOC-003 PDF pp. 14-35, one file per matching page | Prior 200-dpi JPEG rendering | STALE |
| DOC-003 maps and records | `.ai_paper_validation/document_outputs/DOC-003/preprocessing/page_extraction_manifest.md`; `.ai_paper_validation/document_outputs/DOC-003/document_record.md`; `.ai_paper_validation/document_outputs/DOC-003/preprocessing_summary.md` | DOC-003 PDF pp. 4-35 | Prior page map and document/preprocessing records | STALE |

The path ranges above are inclusive and enumerate the filename sequence without omitting an asset; the hash inventory is the per-file authoritative listing. The reusable inventory contains 79 files: 44 native-text files, 26 rendered-page files, 2 page manifests, 3 document records, 3 preprocessing summaries, and 1 package source-location map.

## Current-source gaps

- DOC-001 PDF pp. 1-10: every prior derivative is stale after the source-hash mismatch.
- DOC-002 PDF pp. 1-45: no text, OCR, extraction, or rendered-page derivative exists.
- DOC-003 PDF pp. 1-36: pp. 4-35 have stale derivatives after the source-hash mismatch; pp. 1-3 and 36 have no derivative.

All 91 direct-source units are therefore fresh-required and assigned in `source_coverage.md`.
