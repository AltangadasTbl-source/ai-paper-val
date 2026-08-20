# Reused Evidence-Asset Inventory

This inventory records the pre-existing featured graphic and every OCR text, native text, and layout text observed under the audit area at curation time. The preprocessing files are current-workflow products, not assets that predate this workflow; they are excluded from the before-reuse hash snapshot and do not contribute reusable direct-source units. No pre-existing OCR text, native text, layout text, table/workbook extraction, page manifest, document record, or source-location map was present. Legacy candidate, verifier, critic, endetail, review-queue, and final-report records were not read as discovery inputs.

## Asset summary

- Eligible pre-existing reusable package-graphic assets: 1.
- Usable direct-source-backed reusable assets: 0.
- Current-workflow derivative assets inspected but excluded from reuse: 8.
- Partial assets: 1.
- Stale assets: 0.
- Duplicate assets: 0.
- Unreadable assets: 0.
- Direct-source units covered by an eligible reusable asset: 0 of 91.
- Direct-source units requiring fresh direct-source extraction and mapping: 91.

## Pre-existing reusable package graphic

| Asset ID | Package-relative artifact path | Asset type and method | Exact package coverage | Coverage | Fitness and reuse eligibility | Verification and limitation |
|---|---|---|---|---|---|---|
| EAI-R001 | joi200066_featured.png | Supplied raster figure derivative | One non-source package graphic corresponding to a main-article result figure | Graphic only; 0 direct PDF-page units | PARTIAL; REUSABLE AS PROVENANCE ONLY | Present before Started UTC and hashed in the reuse snapshot. It duplicates result-figure content but is not an independent direct source, does not replace direct-PDF inspection, and contributes no reusable source unit. |

## Current-workflow source-backed derivatives, excluded from reuse

| Asset ID | Package-relative artifact path | Asset type and method | Exact direct-source location coverage | Coverage | Fitness and reuse eligibility | Verification and limitation |
|---|---|---|---|---|---|---|
| EAI-001 | .ai_paper_validation/review_1_5_1/preprocessing/main_native.txt | Native text; page-delimited text extraction | DOC-001, PDF pages 1-10; one nonempty form-feed-delimited segment for each page | All 10 units | FRESH OUTPUT; USABLE after fresh extraction | Created after Started UTC; excluded from the reuse snapshot. It may support its later fresh direct-source mapping stage, but direct PDF confirmation remains required for any candidate. |
| EAI-002 | .ai_paper_validation/review_1_5_1/preprocessing/main_layout.txt | Layout text; page-delimited layout-preserving extraction | DOC-001, PDF pages 1-10; one nonempty form-feed-delimited segment for each page | All 10 units | FRESH OUTPUT; USABLE after fresh extraction | Created after Started UTC; excluded from the reuse snapshot. It supplements EAI-001 for later fresh direct-source mapping; direct PDF confirmation remains required for any candidate. |
| EAI-003 | .ai_paper_validation/review_1_5_1/preprocessing/supp1_native.txt | Native text; page-delimited text extraction | DOC-002, PDF pages 1-31; one nonempty form-feed-delimited segment for each page | All 31 units | FRESH OUTPUT; USABLE after fresh extraction | Created after Started UTC; excluded from the reuse snapshot. The generic file-type label does not prevent successful textual inspection. Direct PDF confirmation remains required for any candidate. |
| EAI-004 | .ai_paper_validation/review_1_5_1/preprocessing/supp1_layout.txt | Layout text; page-delimited layout-preserving extraction | DOC-002, PDF pages 1-31; one nonempty form-feed-delimited segment for each page | All 31 units | FRESH OUTPUT; USABLE after fresh extraction | Created after Started UTC; excluded from the reuse snapshot. It supplements EAI-003 for later fresh direct-source mapping; direct PDF confirmation remains required for any candidate. |
| EAI-005 | .ai_paper_validation/review_1_5_1/preprocessing/supp2_native.txt | Native text; page-delimited text extraction | DOC-003, PDF pages 1-48; one nonempty form-feed-delimited segment for each page | All 48 units | FRESH OUTPUT; USABLE after fresh extraction | Created after Started UTC; excluded from the reuse snapshot. Direct PDF confirmation remains required for any candidate. |
| EAI-006 | .ai_paper_validation/review_1_5_1/preprocessing/supp2_layout.txt | Layout text; page-delimited layout-preserving extraction | DOC-003, PDF pages 1-48; one nonempty form-feed-delimited segment for each page | All 48 units | FRESH OUTPUT; USABLE after fresh extraction | Created after Started UTC; excluded from the reuse snapshot. It supplements EAI-005 for later fresh direct-source mapping; direct PDF confirmation remains required for any candidate. |
| EAI-007 | .ai_paper_validation/review_1_5_1/preprocessing/supp3_native.txt | Native text; page-delimited text extraction | DOC-004, PDF pages 1-2; one nonempty form-feed-delimited segment for each page | All 2 units | FRESH OUTPUT; USABLE after fresh extraction | Created after Started UTC; excluded from the reuse snapshot. Direct PDF confirmation remains required for any candidate. |
| EAI-008 | .ai_paper_validation/review_1_5_1/preprocessing/supp3_layout.txt | Layout text; page-delimited layout-preserving extraction | DOC-004, PDF pages 1-2; one nonempty form-feed-delimited segment for each page | All 2 units | FRESH OUTPUT; USABLE after fresh extraction | Created after Started UTC; excluded from the reuse snapshot. It supplements EAI-007 for later fresh direct-source mapping; direct PDF confirmation remains required for any candidate. |

## Current-workflow non-source graphic derivative

| Asset ID | Package-relative artifact path | Asset type and method | Exact package location coverage | Coverage | Fitness and reuse eligibility | Verification and limitation |
|---|---|---|---|---|---|---|
| EAI-009 | .ai_paper_validation/review_1_5_1/preprocessing/featured_ocr.txt | OCR text | `joi200066_featured.png`, the non-source package graphic | Graphic only | FRESH OUTPUT; PARTIAL | Created after Started UTC; excluded from the reuse snapshot. The OCR is readable enough to identify graph-like labels but it is not mapped to a direct scientific source. It is excluded from direct-source coverage and must not be used as independent scientific evidence. |

## Mapping result and gaps

No pre-existing reusable direct-source-backed asset covers a direct PDF page. The pre-existing featured PNG is retained only as partial provenance. Accordingly, every direct-source page is a fresh-required unit: DOC-001 pages 1-10, DOC-002 pages 1-31, DOC-003 pages 1-48, and DOC-004 pages 1-2. The current-workflow derivatives can support fresh mapping after direct-source confirmation but may not be counted as reused coverage. There are no pre-existing reusable table/workbook extractions, page manifests, document records, or source-location maps.

The fresh mapping assignment is direct-source extraction and mapping with direct-PDF confirmation: main mapper for DOC-001 pages 1-10 and support mapper for DOC-002 pages 1-31, DOC-003 pages 1-48, and DOC-004 pages 1-2. The non-source graphic OCR has no downstream scientific mapper assignment.

## Inspection method

The curation inspection used `file` 5.46, `wc`, form-feed segment counts, and `sha256sum` 0.8.0. Current local extraction-tool versions available for later direct confirmation are `pdftotext` 26.01.0 and `tesseract` 5.5.0. The current-workflow extraction command metadata was not assumed or inferred. No supplied source or eligible reused artifact was modified.
