# Reusable Evidence Asset Inventory

All 90 eligible legacy evidence files are inventoried individually below and hashed in reused_artifact_hashes_before.sha256. Only source-linked factual evidence is reusable. Native texts were compared with direct Poppler 26.01.0 extraction after removing whitespace; all 27 page files and all four combined files match current supplied source text. Combined extraction form-feed counts are five and seven, matching their declared page scopes. Current source hashes match legacy identity records. Normalized text is DUPLICATE as an overlapping derivative; page images are USABLE locator/visual aids, with exact page identity from the manifest. OCR remains PARTIAL because transcription is not source authority. No scientific gap remains in text coverage.

Fitness meanings: USABLE supports its entire declared scope; PARTIAL supports only source-linked identity, location, or selected evidence; DUPLICATE overlaps another usable derivative. No STALE or UNREADABLE eligible asset was found. A PARTIAL map or metadata file contributes no additional unique covered units beyond the source-matched text.

Engines: legacy page native text is native PDF extraction, source-matched using direct pdftotext -layout; normalized text uses the recorded UTF-8/whitespace normalization; combined native/layout files match direct pdftotext without/with -layout, respectively (their original version was not recorded); images are retained PNG PDF renders with engine version unrecorded; p3 OCR records rapidocr_onnxruntime CPU with onnxruntime 1.28.0. No fresh OCR, rendering, Office conversion, or Python extraction was performed during curation.

Checks: pdfinfo "SOURCE.pdf"; sha256sum -- "SOURCE.pdf"; pdftotext -layout -f N -l N "SOURCE.pdf" - compared with the corresponding page file using cmp after tr -d [:space:]; combined native/layout checks use -f 1 -l 5 or -l 7. Source/output paths and exact locations are recorded per row.

| Asset path | Kind / engine | Exact source location | Fitness | Coverage / limitation |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/jama2019-14231-main-article/document_record.json | Document identity metadata | DOC-001 | PARTIAL | Identity/hash/count fields only; legacy outcomes ignored |
| .ai_paper_validation/document_outputs/jama2019-14231-main-article/main_text_extraction.json | Source-location extraction map | DOC-001 PDF pp1–12, selected result locations | PARTIAL | Factual locations and extracted values only; reread full source |
| .ai_paper_validation/document_outputs/jama2019-14231-main-article/main_text_extraction.md | Source-location extraction map | DOC-001 PDF pp1–12, selected result locations | PARTIAL | Factual locations and extracted values only; reread full source |
| .ai_paper_validation/document_outputs/jama2019-14231-supplement-1/document_record.json | Document identity metadata | DOC-002 | PARTIAL | Identity/hash/count fields only; legacy outcomes ignored |
| .ai_paper_validation/document_outputs/jama2019-14231-supplement-1/results_evidence_map.md | Source-location extraction map | DOC-002 PDF pp6–20, selected results | PARTIAL | No pp1–5 evidence; full source mapping required |
| .ai_paper_validation/document_outputs/jama2019-14231-supplement-2/document_record.json | Document identity metadata | DOC-003 | PARTIAL | Identity/hash/count fields only; legacy outcomes ignored |
| .ai_paper_validation/document_outputs/package_manifest.json | Package identity metadata | DOC-001 pp1–12; DOC-002 pp1–20; DOC-003 pp1–7 | PARTIAL | Source names/counts only; legacy scope ignored |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/images/page-003.png | PNG PDF render | DOC-001 PDF p3 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/images/page-005.png | PNG PDF render | DOC-001 PDF p5 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/images/page-006.png | PNG PDF render | DOC-001 PDF p6 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/images/page-007.png | PNG PDF render | DOC-001 PDF p7 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/images/page-008.png | PNG PDF render | DOC-001 PDF p8 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/images/page-009.png | PNG PDF render | DOC-001 PDF p9 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/images/page-010.png | PNG PDF render | DOC-001 PDF p10 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-001.txt | Native/layout PDF text | DOC-001 PDF p1 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-002.txt | Native/layout PDF text | DOC-001 PDF p2 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-003.txt | Native/layout PDF text | DOC-001 PDF p3 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-004.txt | Native/layout PDF text | DOC-001 PDF p4 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-005.txt | Native/layout PDF text | DOC-001 PDF p5 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-006.txt | Native/layout PDF text | DOC-001 PDF p6 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-007.txt | Native/layout PDF text | DOC-001 PDF p7 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-008.txt | Native/layout PDF text | DOC-001 PDF p8 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-009.txt | Native/layout PDF text | DOC-001 PDF p9 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-010.txt | Native/layout PDF text | DOC-001 PDF p10 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-011.txt | Native/layout PDF text | DOC-001 PDF p11 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/native_text/page-012.txt | Native/layout PDF text | DOC-001 PDF p12 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-001.txt | Normalized PDF text | DOC-001 PDF p1 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-002.txt | Normalized PDF text | DOC-001 PDF p2 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-003.txt | Normalized PDF text | DOC-001 PDF p3 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-004.txt | Normalized PDF text | DOC-001 PDF p4 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-005.txt | Normalized PDF text | DOC-001 PDF p5 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-006.txt | Normalized PDF text | DOC-001 PDF p6 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-007.txt | Normalized PDF text | DOC-001 PDF p7 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-008.txt | Normalized PDF text | DOC-001 PDF p8 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-009.txt | Normalized PDF text | DOC-001 PDF p9 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-010.txt | Normalized PDF text | DOC-001 PDF p10 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-011.txt | Normalized PDF text | DOC-001 PDF p11 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/normalized_text/page-012.txt | Normalized PDF text | DOC-001 PDF p12 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/ocr_metadata/page-003.json | RapidOCR CPU metadata | DOC-001 PDF p3 | PARTIAL | Engine and image/text paths only |
| .ai_paper_validation/preprocessing/jama2019-14231-main-article/ocr_text/page-003.txt | RapidOCR CPU text | DOC-001 PDF p3 | PARTIAL | p3 transcription aid; direct source is authority |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-006.png | PNG PDF render | DOC-002 PDF p6 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-007.png | PNG PDF render | DOC-002 PDF p7 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-008.png | PNG PDF render | DOC-002 PDF p8 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-009.png | PNG PDF render | DOC-002 PDF p9 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-010.png | PNG PDF render | DOC-002 PDF p10 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-011.png | PNG PDF render | DOC-002 PDF p11 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-012.png | PNG PDF render | DOC-002 PDF p12 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-013.png | PNG PDF render | DOC-002 PDF p13 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-014.png | PNG PDF render | DOC-002 PDF p14 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-015.png | PNG PDF render | DOC-002 PDF p15 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-016.png | PNG PDF render | DOC-002 PDF p16 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-018.png | PNG PDF render | DOC-002 PDF p18 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-019.png | PNG PDF render | DOC-002 PDF p19 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/images/page-020.png | PNG PDF render | DOC-002 PDF p20 | USABLE | Exact page image; rendering version unrecorded |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-006.txt | Native/layout PDF text | DOC-002 PDF p6 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-007.txt | Native/layout PDF text | DOC-002 PDF p7 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-008.txt | Native/layout PDF text | DOC-002 PDF p8 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-009.txt | Native/layout PDF text | DOC-002 PDF p9 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-010.txt | Native/layout PDF text | DOC-002 PDF p10 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-011.txt | Native/layout PDF text | DOC-002 PDF p11 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-012.txt | Native/layout PDF text | DOC-002 PDF p12 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-013.txt | Native/layout PDF text | DOC-002 PDF p13 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-014.txt | Native/layout PDF text | DOC-002 PDF p14 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-015.txt | Native/layout PDF text | DOC-002 PDF p15 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-016.txt | Native/layout PDF text | DOC-002 PDF p16 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-017.txt | Native/layout PDF text | DOC-002 PDF p17 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-018.txt | Native/layout PDF text | DOC-002 PDF p18 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-019.txt | Native/layout PDF text | DOC-002 PDF p19 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/native_text/page-020.txt | Native/layout PDF text | DOC-002 PDF p20 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-006.txt | Normalized PDF text | DOC-002 PDF p6 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-007.txt | Normalized PDF text | DOC-002 PDF p7 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-008.txt | Normalized PDF text | DOC-002 PDF p8 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-009.txt | Normalized PDF text | DOC-002 PDF p9 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-010.txt | Normalized PDF text | DOC-002 PDF p10 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-011.txt | Normalized PDF text | DOC-002 PDF p11 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-012.txt | Normalized PDF text | DOC-002 PDF p12 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-013.txt | Normalized PDF text | DOC-002 PDF p13 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-014.txt | Normalized PDF text | DOC-002 PDF p14 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-015.txt | Normalized PDF text | DOC-002 PDF p15 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-016.txt | Normalized PDF text | DOC-002 PDF p16 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-017.txt | Normalized PDF text | DOC-002 PDF p17 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-018.txt | Normalized PDF text | DOC-002 PDF p18 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-019.txt | Normalized PDF text | DOC-002 PDF p19 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/jama2019-14231-supplement-1/normalized_text/page-020.txt | Normalized PDF text | DOC-002 PDF p20 | DUPLICATE | Overlaps source-matched native page text |
| .ai_paper_validation/preprocessing/ocr_backend.json | CPU OCR engine metadata | DOC-001 PDF p3 | PARTIAL | Engine metadata only |
| .ai_paper_validation/preprocessing/page_manifest.json | Page/location manifest | DOC-001 pp1–12; DOC-002 pp1–20; DOC-003 pp1–7 | PARTIAL | Text coverage DOC-001 pp1–12 and DOC-002 pp6–20; later assets close remaining units |
| .ai_paper_validation/review_1_5_1/preprocessing/joi190103supp1_prod_pp1-5_layout.txt | Combined pdftotext layout | DOC-002 PDF pp1–5 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/review_1_5_1/preprocessing/joi190103supp1_prod_pp1-5_native.txt | Combined pdftotext native | DOC-002 PDF pp1–5 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/review_1_5_1/preprocessing/joi190103supp2_prod_pp1-7_layout.txt | Combined pdftotext layout | DOC-003 PDF pp1–7 | USABLE | Entire declared page scope; source match confirmed |
| .ai_paper_validation/review_1_5_1/preprocessing/joi190103supp2_prod_pp1-7_native.txt | Combined pdftotext native | DOC-003 PDF pp1–7 | USABLE | Entire declared page scope; source match confirmed |

Excluded legacy files are scientific-check records, rights-screen records, and a preprocessing script; their content was not used. No separate workbook/table extraction, CSV extraction, DOC paragraph map, or additional OCR asset exists in this package. Exact source inventory covers every eligible source format.

## New run derivatives

| Derivative path | Direct engine / device | Exact source unit | Purpose |
|---|---|---|---|
| preprocessing/main-mapper-page-007-layout.txt | pdftotext -layout, Poppler 26.01.0 / CPU | DOC-001 PDF p7 | Table 2 alignment confirmation |
| preprocessing/support_mapper-doc002-p002.png | pdftoppm, Poppler 26.01.0 / CPU | DOC-002 PDF p2 | Bold-code operational definition visual confirmation |

New derivatives are stored only in this run; they do not belong in the legacy reused-artifact baseline. Exact commands are recorded in the respective mapper artifacts.

| Derivative path | Direct engine / device | Exact source unit | Purpose |
|---|---|---|---|
| preprocessing/numeric-main-p005-006.txt | pdftotext -layout, Poppler 26.01.0 / CPU | DOC-001 pp5–6 | Complete baseline count and percentage checks |
| preprocessing/numeric-main-p007.txt | pdftotext -layout, Poppler 26.01.0 / CPU | DOC-001 p7 | Risk-difference display confirmation |
| preprocessing/numeric-support-p005-007.txt | pdftotext -layout, Poppler 26.01.0 / CPU | DOC-002 pp5–7 | Medication and risk/rate display confirmation |
| preprocessing/cross-main-layout.txt | pdftotext -layout, Poppler 26.01.0 / CPU | DOC-001 pp1–12 | Exact report comparison text |
| preprocessing/cross-support-layout.txt | pdftotext -layout, Poppler 26.01.0 / CPU | DOC-002 pp1–20 | Exact results supplement comparison text |
| preprocessing/cross-plan-layout.txt | pdftotext -layout, Poppler 26.01.0 / CPU | DOC-003 pp1–7 | Exact original/amended plan comparison text |
| preprocessing/cross-plan-p003.png | pdftoppm, Poppler 26.01.0 / CPU | DOC-003 p3 | Matching allocation visual confirmation |
| preprocessing/cross-plan-p004.png | pdftoppm, Poppler 26.01.0 / CPU | DOC-003 p4 | Endpoint code-set visual confirmation |
| preprocessing/stat1-main-layout.txt | pdftotext -layout, Poppler 26.01.0 / CPU | DOC-001 pp1–12 | Statistical source confirmation |
| preprocessing/stat1-supp-layout.txt | pdftotext -layout, Poppler 26.01.0 / CPU | DOC-002 pp1–20 | Statistical source confirmation |
| preprocessing/stat1-plan-layout.txt | pdftotext -layout, Poppler 26.01.0 / CPU | DOC-003 pp1–7 | Statistical plan confirmation |

Exact commands and specific use are retained in the owning checker artifacts. These are confirmation derivatives of reusable-backed pages; fresh-required source count remains zero.

Initial inclusion screen confirmation derivatives: direct Poppler 26.01.0, CPU. Nine unique files under screening/confirmation: screener-main-layout.txt (DOC-001 pp1–12); screener-results-layout.txt (DOC-002 pp1–20); screener-plan-layout.txt (DOC-003 pp1–7); screener-main-p007.png (DOC-001 p7); screener-results-p002.png, screener-results-p012.png, screener-results-p020.png (DOC-002 pp2,12,20); screener-plan-p003.png, screener-plan-p004.png (DOC-003 pp3,4). Exact commands and scaling are in screening/inclusion_screen.md. These new confirmation artifacts preserve the supplied sources and all reused files.
