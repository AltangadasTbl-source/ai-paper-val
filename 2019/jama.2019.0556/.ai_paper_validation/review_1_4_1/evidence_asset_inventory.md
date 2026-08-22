# Reusable Evidence Asset Inventory

## Inclusion rule

Eligible reuse assets are source-linked native text, OCR text, rendered source pages, OCR metadata, page manifests, document maps, and extraction/source-identity metadata below the pre-existing audit area. Each included file is enumerated individually in `reused_artifact_hashes_before.sha256`. There are 72 eligible files.

Legacy candidate, queue, verifier, critic, quality, agent-response, validation, and final-report records were excluded as scientific inputs. Compliance-only records, preprocessing programs, packaged OCR software, and the current Workflow 1.4.1 outputs were also excluded because they are not source evidence assets. Where an eligible document record contains a legacy scientific-scope or disposition field, that field is ignored; only stable identity, page count, and extraction-location metadata may be reused.

## Fitness definitions

- `USABLE`: source matched, nonempty, and fit as a locator or transcription/rendering aid for the stated locations.
- `PARTIAL`: useful metadata or evidence is present, but page coverage, quality metadata, or method provenance is incomplete.
- `STALE`: stable identity fields may be reused, but old scope/disposition or relocated-path fields must not control this review.
- `DUPLICATE`: content is represented more precisely by another included source-linked asset.
- `UNREADABLE`: file cannot be used. None were found.

## Inventory by artifact group

| Asset group and exact path scope | Count | Source locations covered | Method/provenance available | Fitness | Use and limitations |
|---|---:|---|---|---|---|
| `.ai_paper_validation/package_manifest.md` | 1 | DOC-001 pp. 1-11; DOC-002 pp. 1-60; DOC-003 pp. 1-5; DOC-004 pp. 1-25; DOC-005 p. 1 at document/page-count level | Prior package mapping; tool/version not recorded | STALE | Reuse document IDs, filenames, classifications, and page counts only. Prior audit-scope declarations are not Workflow 1.4.1 boundaries. |
| `.ai_paper_validation/preprocessing/current_run_manifest.json` | 1 | Source hashes for all five PDFs; extraction locations for DOC-001 pp. 1-11 and DOC-004 pp. 1-2, 16-23 | Records Tesseract CPU selection and completed status; native/render commands and versions absent | PARTIAL | Source hashes match current PDFs. Extraction coverage is incomplete for three documents and part of DOC-004. |
| `.ai_paper_validation/preprocessing/ocr_backend.json` | 1 | Method metadata only; no independent source page | Tesseract CPU recorded; no confidence; stored executable path refers to a relocated package path | PARTIAL | Useful for backend identity only. The executable exists at the analogous path in the current package, not at the stored absolute path. |
| `.ai_paper_validation/document_outputs/DOC-001/document_status.json` through `DOC-005/document_status.json` | 5 | Identity and page-count records for all five documents; extraction-scope fields for DOC-001 and DOC-004 | Prior document processing records | STALE | Reuse identity/page fields only. Do not reuse old exclusions, dispositions, or candidate counts. |
| `.ai_paper_validation/document_outputs/DOC-001/page_manifest.json` | 1 | DOC-001 pp. 1-11; native paths for every page; visual paths for pp. 3, 5-8 | Per-page native character checks, vector/image counts, Tesseract CPU completion metadata | USABLE | Complete page map for the main article. Some nonvisual pages retain `pending manual classification`; this is not a discovery boundary. |
| `.ai_paper_validation/document_outputs/DOC-004/page_manifest.json` | 1 | DOC-004 pp. 1-2 and 16-23 have page records; pp. 3-15 and 24-25 appear only in the excluded-page list | Same per-page metadata as above for mapped pages | PARTIAL | Precise for the 10 mapped pages, but no reusable evidence records for 15 other pages. Old exclusions are void for Workflow 1.4.1. |
| `DOC-001/normalized_text/page_001.txt` through `page_011.txt` | 11 | DOC-001 pp. 1-11 | Native extraction; per-page files are nonempty; tool/version/command not recorded | USABLE | Preferred reusable page-level text locator. Direct PDF confirmation remains required for candidates. |
| `DOC-004/normalized_text/page_001.txt`, `page_002.txt`, and `page_016.txt` through `page_023.txt` | 10 | DOC-004 pp. 1-2, 16-23 | Native extraction; per-page files are nonempty; tool/version/command not recorded | USABLE | Good locator for mapped pages; incomplete document coverage. |
| `DOC-001/normalized_text.txt` and `DOC-004/normalized_text.txt` | 2 | Same locations as their page-level native-text sets | Aggregate normalized native text | DUPLICATE | Page-specific counterparts provide more truthful locations and should be preferred. |
| `DOC-001/ocr_text/page_003.txt`, `page_005.txt` through `page_008.txt` | 5 | DOC-001 pp. 3, 5-8 | Tesseract CPU; nonempty output; no mean confidence | USABLE | Visual/table transcription aid only; verify printed values against PDF pages. |
| `DOC-004/ocr_text/page_016.txt` through `page_023.txt` | 8 | DOC-004 pp. 16-23 | Tesseract CPU; nonempty output; no mean confidence | USABLE | Visual/table transcription aid only; verify printed values against PDF pages. |
| `DOC-001/ocr_metadata/page_003.json`, `page_005.json` through `page_008.json` | 5 | DOC-001 pp. 3, 5-8 | Input image, output text, character count, backend, and completion status recorded | PARTIAL | Mean confidence is null, command/version is absent, and embedded absolute backend path is relocated. |
| `DOC-004/ocr_metadata/page_016.json` through `page_023.json` | 8 | DOC-004 pp. 16-23 | Same fields as DOC-001 OCR metadata | PARTIAL | Same provenance limitations. |
| `DOC-001/rendered_pages/page_003.png`, `page_005.png` through `page_008.png` | 5 | DOC-001 pp. 3, 5-8 | 1530 x 1980 RGB PNG; rendering tool/command/version not recorded | USABLE | Stable visual locator for flow, tables, and figures; direct source page remains authoritative. |
| `DOC-004/rendered_pages/page_016.png` through `page_023.png` | 8 | DOC-004 pp. 16-23 | 1530 x 1980 RGB PNG; rendering tool/command/version not recorded | USABLE | Stable visual locator for eAppendix result displays; direct source page remains authoritative. |

Paths beginning with `DOC-001/` or `DOC-004/` in the table are relative to `.ai_paper_validation/document_outputs/`.

## Counts by fitness

| Fitness | File count |
|---|---:|
| USABLE | 48 |
| PARTIAL | 16 |
| STALE | 6 |
| DUPLICATE | 2 |
| UNREADABLE | 0 |
| **Total** | **72** |

## Absent reusable asset classes

No separately identified layout-text extraction, table extraction, workbook extraction, CSV extraction, Office structure map, or Office-derived PDF exists. There are no Office or structured-data direct sources in this package. The native and OCR text may contain table transcriptions, but they are not represented as structured table assets.

## Excluded records and materials

- `.ai_paper_validation/final_report.md`: old final report; excluded.
- `.ai_paper_validation/document_outputs/DOC-*/agent_response_trace.md`: old agent/review traces; excluded.
- `.ai_paper_validation/validation_trace.md`: old validation/quality trace; excluded.
- `.ai_paper_validation/document_outputs/DOC-*/ai_training_restriction_record.json`: compliance-only record, not scientific evidence; excluded.
- `.ai_paper_validation/preprocessing/*.py`, `.ai_paper_validation/preprocessing/README.md`, and `.ai_paper_validation/local_ocr/**`: programs, documentation, and software payloads, not source-linked evidence artifacts; excluded.
- `.ai_paper_validation/review_1_4_1/**`: current workflow outputs, not pre-existing reuse inputs; excluded from the reuse hash set.

No old candidate/queue/verifier/critic/quality/final-report content was used to define evidence scope or scientific discovery.
