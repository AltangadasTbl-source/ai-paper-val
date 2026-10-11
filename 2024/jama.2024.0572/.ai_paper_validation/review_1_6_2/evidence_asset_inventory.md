# Reusable evidence-asset inventory

Exactly 250 eligible existing derivative files were inventoried and individually hashed in `reused_artifact_hashes_before.sha256`. Their union covers 227 unique direct-source pages. Derivatives include native/layout text, source-marked normalized text, page OCR, rendered full pages and a figure crop, two page manifests, two extraction summaries, seven document records, and two source-location/result extraction maps. There are no workbook extractions or direct Office sources. No old candidate, queue, screening, checker, verifier, critic, quality, classification, or final-report conclusions were read. Rights-screen records and old administrative audit metadata outside eligible document records were not used as discovery inputs.

Fitness vocabulary: USABLE is readable and mapped; PARTIAL omits source content but may be complemented by another asset; DUPLICATE repeats a canonical usable asset without adding unique coverage; STALE and UNREADABLE would enter fresh-required coverage unless another current usable asset covered the unit. None of the inventoried units is solely stale or unreadable. The old audit scope statements in document records are not inherited.

## Provenance and source-match checks

Current validation engines: direct Poppler `pdfinfo`, `pdftotext`, `pdftoppm` 26.01.0; `tesseract` 5.5.0 is available but no new OCR was needed for inventory. Legacy native/rendering summaries record native PDF extraction and 200-dpi PNG output without exact engine versions; legacy support extraction/OCR artifacts do not consistently store versions. Their original engine/version is therefore recorded as legacy-unrecorded, rather than inferred from current tool installations. Existing SAP images are 1530x1980; existing main/results page images are 1700x2200.

Source match commands, emitting transient pipeline output only: `pdfinfo "source.pdf"`; `pdftotext -f 1 -l 2 "source.pdf" -`; `cmp -s <(pdftotext -layout "source.pdf" -) "legacy-layout.txt"`; `file "legacy-image.png"`; direct local image inspection for trial SAP p. 2. No new extraction file was written by the curator. Main and DOC-002/003/005/007 whole-source layout assets exactly match current direct-source output. DOC-004 page images plus OCR cover all 40 scanned pages; OCR page markers enumerate all 40 pages. DOC-006 53 native text files and 49 images cover every source page; its page manifest identifies native sparse/partial pages, complemented by images. Candidate confirmation must use exact direct-source evidence.

## Canonical reuse groups and gaps

| Source | Canonical evidence | Exact unique coverage | Fitness / gap treatment |
|---|---|---|---|
| DOC-001 | review_1_5_3/preprocessing/DOC-001-MAIN/direct_layout_text.txt; preprocessing/DOC-001-MAIN/native_text and page_images | pp. 1-14 native/layout; pp. 5-9 images | USABLE all 14 pages; older native files and source map aid location; no extraction gap. |
| DOC-002 | review_1_5_3/preprocessing/support_mapper_fresh/DOC-002/layout.txt and by_page.txt | pp. 1-30 | USABLE 30 pages, direct layout match. |
| DOC-003 | review_1_5_3/preprocessing/support_mapper_fresh/DOC-003/layout.txt and by_page.txt | pp. 1-82 | USABLE 82 pages, direct layout match. |
| DOC-004 | review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr_by_page.txt, ocr/page-NN.txt, pages/page-NN.png | pp. 1-40 | USABLE image/OCR union 40 pages; OCR is transcription aid, image/source is authority. |
| DOC-005 | review_1_5_3/preprocessing/support_mapper_fresh/DOC-005/layout.txt and by_page.txt | pp. 1-7 | USABLE 7 pages, direct layout match. |
| DOC-006 | preprocessing/DOC-006-RESULTS-SUPP/native_text/page-NNN.txt and page_images/page-NNN.png | native pp. 1-53; images pp. 5-53 | USABLE union 53 pages. PARTIAL native pp. 5-8,13-25,37,48,50 complemented by images; no extraction gap. |
| DOC-007 | review_1_5_3/preprocessing/support_mapper_fresh/DOC-007/layout.txt and by_page.txt | p. 1 | USABLE 1 page, direct layout match. |

Paths in this group summary are relative to `.ai_paper_validation/`; individual inventory below uses package-relative paths. Overlapping by-page and combined layouts are not extra source units. A cropped image is PARTIAL because it covers only the Figure2 region of main p. 7; full p. 7 image covers that unit. Recheck-folder native/layout/image assets are permitted extraction assets, not recheck conclusions; their scope is taken from their filenames only.

## Individual assets

| Asset path | Source ID | Exact source units / locations | Kind and legacy engine | Fitness |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001-MAIN/document_record.md | DOC-001 | PDF pp. 1-14 | Document identity record; inventory metadata | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-001-MAIN/main_text_extraction.md | DOC-001 | PDF pp. 1-14 | Source-location/table result extraction map; legacy engine unrecorded | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-002-ADMIN-COLLAB/document_record.md | DOC-002 | PDF pp. 1-30 | Document identity record; inventory metadata | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-003-PROTOCOL/document_record.md | DOC-003 | PDF pp. 1-82 | Document identity record; inventory metadata | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-004-SAP-TRIAL/document_record.md | DOC-004 | PDF pp. 1-40 | Document identity record; inventory metadata | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-005-SAP-ANALYSIS/document_record.md | DOC-005 | PDF pp. 1-7 | Document identity record; inventory metadata | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-006-RESULTS-SUPP/document_record.md | DOC-006 | PDF pp. 1-53 | Document identity record; inventory metadata | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-006-RESULTS-SUPP/results_supplement_evidence_map.md | DOC-006 | PDF pp. 1-53 | Source-location/table result extraction map; legacy engine unrecorded | PARTIAL |
| .ai_paper_validation/document_outputs/DOC-007-ADMIN-DATA/document_record.md | DOC-007 | PDF p. 1 | Document identity record; inventory metadata | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/extraction_summary.md | DOC-001 | PDF pp. 1-14 | Extraction metadata; legacy engine unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-001.txt | DOC-001 | PDF p. 1 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-002.txt | DOC-001 | PDF p. 2 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-003.txt | DOC-001 | PDF p. 3 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-004.txt | DOC-001 | PDF p. 4 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-005.txt | DOC-001 | PDF p. 5 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-006.txt | DOC-001 | PDF p. 6 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-007.txt | DOC-001 | PDF p. 7 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-008.txt | DOC-001 | PDF p. 8 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-009.txt | DOC-001 | PDF p. 9 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-010.txt | DOC-001 | PDF p. 10 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-011.txt | DOC-001 | PDF p. 11 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-012.txt | DOC-001 | PDF p. 12 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-013.txt | DOC-001 | PDF p. 13 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-014.txt | DOC-001 | PDF p. 14 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/normalized_text.txt | DOC-001 | PDF pp. 1-14 | Source-marked native text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/page_images/page-005.png | DOC-001 | PDF p. 5 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/page_images/page-006.png | DOC-001 | PDF p. 6 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/page_images/page-007.png | DOC-001 | PDF p. 7 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/page_images/page-008.png | DOC-001 | PDF p. 8 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/page_images/page-009.png | DOC-001 | PDF p. 9 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-001-MAIN/page_manifest.csv | DOC-001 | PDF pp. 1-14 | Page-location manifest; legacy engine unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/extraction_summary.md | DOC-006 | PDF pp. 1-53 | Extraction metadata; legacy engine unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-001.txt | DOC-006 | PDF p. 1 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-002.txt | DOC-006 | PDF p. 2 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-003.txt | DOC-006 | PDF p. 3 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-004.txt | DOC-006 | PDF p. 4 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-005.txt | DOC-006 | PDF p. 5 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-006.txt | DOC-006 | PDF p. 6 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-007.txt | DOC-006 | PDF p. 7 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-008.txt | DOC-006 | PDF p. 8 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-009.txt | DOC-006 | PDF p. 9 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-010.txt | DOC-006 | PDF p. 10 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-011.txt | DOC-006 | PDF p. 11 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-012.txt | DOC-006 | PDF p. 12 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-013.txt | DOC-006 | PDF p. 13 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-014.txt | DOC-006 | PDF p. 14 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-015.txt | DOC-006 | PDF p. 15 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-016.txt | DOC-006 | PDF p. 16 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-017.txt | DOC-006 | PDF p. 17 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-018.txt | DOC-006 | PDF p. 18 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-019.txt | DOC-006 | PDF p. 19 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-020.txt | DOC-006 | PDF p. 20 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-021.txt | DOC-006 | PDF p. 21 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-022.txt | DOC-006 | PDF p. 22 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-023.txt | DOC-006 | PDF p. 23 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-024.txt | DOC-006 | PDF p. 24 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-025.txt | DOC-006 | PDF p. 25 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-026.txt | DOC-006 | PDF p. 26 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-027.txt | DOC-006 | PDF p. 27 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-028.txt | DOC-006 | PDF p. 28 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-029.txt | DOC-006 | PDF p. 29 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-030.txt | DOC-006 | PDF p. 30 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-031.txt | DOC-006 | PDF p. 31 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-032.txt | DOC-006 | PDF p. 32 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-033.txt | DOC-006 | PDF p. 33 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-034.txt | DOC-006 | PDF p. 34 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-035.txt | DOC-006 | PDF p. 35 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-036.txt | DOC-006 | PDF p. 36 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-037.txt | DOC-006 | PDF p. 37 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-038.txt | DOC-006 | PDF p. 38 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-039.txt | DOC-006 | PDF p. 39 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-040.txt | DOC-006 | PDF p. 40 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-041.txt | DOC-006 | PDF p. 41 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-042.txt | DOC-006 | PDF p. 42 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-043.txt | DOC-006 | PDF p. 43 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-044.txt | DOC-006 | PDF p. 44 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-045.txt | DOC-006 | PDF p. 45 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-046.txt | DOC-006 | PDF p. 46 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-047.txt | DOC-006 | PDF p. 47 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-048.txt | DOC-006 | PDF p. 48 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-049.txt | DOC-006 | PDF p. 49 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-050.txt | DOC-006 | PDF p. 50 | Native PDF text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-051.txt | DOC-006 | PDF p. 51 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-052.txt | DOC-006 | PDF p. 52 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-053.txt | DOC-006 | PDF p. 53 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/normalized_text.txt | DOC-006 | PDF pp. 1-53 | Source-marked native text; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-005.png | DOC-006 | PDF p. 5 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-006.png | DOC-006 | PDF p. 6 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-007.png | DOC-006 | PDF p. 7 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-008.png | DOC-006 | PDF p. 8 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-009.png | DOC-006 | PDF p. 9 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-010.png | DOC-006 | PDF p. 10 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-011.png | DOC-006 | PDF p. 11 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-012.png | DOC-006 | PDF p. 12 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-013.png | DOC-006 | PDF p. 13 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-014.png | DOC-006 | PDF p. 14 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-015.png | DOC-006 | PDF p. 15 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-016.png | DOC-006 | PDF p. 16 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-017.png | DOC-006 | PDF p. 17 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-018.png | DOC-006 | PDF p. 18 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-019.png | DOC-006 | PDF p. 19 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-020.png | DOC-006 | PDF p. 20 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-021.png | DOC-006 | PDF p. 21 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-022.png | DOC-006 | PDF p. 22 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-023.png | DOC-006 | PDF p. 23 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-024.png | DOC-006 | PDF p. 24 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-025.png | DOC-006 | PDF p. 25 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-026.png | DOC-006 | PDF p. 26 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-027.png | DOC-006 | PDF p. 27 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-028.png | DOC-006 | PDF p. 28 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-029.png | DOC-006 | PDF p. 29 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-030.png | DOC-006 | PDF p. 30 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-031.png | DOC-006 | PDF p. 31 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-032.png | DOC-006 | PDF p. 32 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-033.png | DOC-006 | PDF p. 33 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-034.png | DOC-006 | PDF p. 34 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-035.png | DOC-006 | PDF p. 35 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-036.png | DOC-006 | PDF p. 36 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-037.png | DOC-006 | PDF p. 37 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-038.png | DOC-006 | PDF p. 38 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-039.png | DOC-006 | PDF p. 39 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-040.png | DOC-006 | PDF p. 40 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-041.png | DOC-006 | PDF p. 41 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-042.png | DOC-006 | PDF p. 42 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-043.png | DOC-006 | PDF p. 43 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-044.png | DOC-006 | PDF p. 44 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-045.png | DOC-006 | PDF p. 45 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-046.png | DOC-006 | PDF p. 46 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-047.png | DOC-006 | PDF p. 47 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-048.png | DOC-006 | PDF p. 48 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-049.png | DOC-006 | PDF p. 49 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-050.png | DOC-006 | PDF p. 50 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-051.png | DOC-006 | PDF p. 51 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-052.png | DOC-006 | PDF p. 52 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-053.png | DOC-006 | PDF p. 53 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_manifest.csv | DOC-006 | PDF pp. 1-53 | Page-location manifest; legacy engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/DOC-001-MAIN/direct_layout_page-004.txt | DOC-001 | PDF p. 4 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/DOC-001-MAIN/direct_layout_page-005.txt | DOC-001 | PDF p. 5 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/DOC-001-MAIN/direct_layout_page-006.txt | DOC-001 | PDF p. 6 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/DOC-001-MAIN/direct_layout_page-007.txt | DOC-001 | PDF p. 7 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/DOC-001-MAIN/direct_layout_page-008.txt | DOC-001 | PDF p. 8 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/DOC-001-MAIN/direct_layout_page-009.txt | DOC-001 | PDF p. 9 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/DOC-001-MAIN/direct_layout_page-010.txt | DOC-001 | PDF p. 10 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/DOC-001-MAIN/direct_layout_page-011.txt | DOC-001 | PDF p. 11 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/DOC-001-MAIN/direct_layout_page-012.txt | DOC-001 | PDF p. 12 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/DOC-001-MAIN/direct_layout_text.txt | DOC-001 | PDF pp. 1-14 | Native layout text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/DOC-001-MAIN/direct_native_text.txt | DOC-001 | PDF pp. 1-14 | Native PDF text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/main_page_6.png | DOC-001 | PDF p. 6 | Rendered PNG; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/main_page_7.png | DOC-001 | PDF p. 7 | Rendered PNG; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/main_page_7_figure_crop.png | DOC-001 | PDF p. 7 Figure2 crop | Rendered PNG; legacy engine/version unrecorded | PARTIAL |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/main_page_9.png | DOC-001 | PDF p. 9 | Rendered PNG; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/main_pages_4_9_layout.txt | DOC-001 | PDF pp. 4-9 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/supp3_page_17.png | DOC-004 | PDF p. 17 | Rendered PNG; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/supp3_pages_17_20_layout.txt | DOC-004 | PDF pp. 17-20 | Native layout text; legacy engine/version unrecorded | UNREADABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/supp4_page_4.png | DOC-005 | PDF p. 4 | Rendered PNG; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/supp4_pages_4_5_layout.txt | DOC-005 | PDF pp. 4-5 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/supp5_page_38.png | DOC-006 | PDF p. 38 | Rendered PNG; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/supp5_page_38_layout.txt | DOC-006 | PDF p. 38 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/supp5_page_43.png | DOC-006 | PDF p. 43 | Rendered PNG; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/supp5_page_43_layout.txt | DOC-006 | PDF p. 43 | Native layout text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/recheck/supp5_page_8.png | DOC-006 | PDF p. 8 | Rendered PNG; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-002/by_page.txt | DOC-002 | PDF pp. 1-30 | Source-marked native text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-002/layout.txt | DOC-002 | PDF pp. 1-30 | Native layout text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-003/by_page.txt | DOC-003 | PDF pp. 1-82 | Source-marked native text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-003/layout.txt | DOC-003 | PDF pp. 1-82 | Native layout text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-01.txt | DOC-004 | PDF p. 1 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-02.txt | DOC-004 | PDF p. 2 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-03.txt | DOC-004 | PDF p. 3 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-04.txt | DOC-004 | PDF p. 4 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-05.txt | DOC-004 | PDF p. 5 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-06.txt | DOC-004 | PDF p. 6 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-07.txt | DOC-004 | PDF p. 7 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-08.txt | DOC-004 | PDF p. 8 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-09.txt | DOC-004 | PDF p. 9 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-10.txt | DOC-004 | PDF p. 10 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-11.txt | DOC-004 | PDF p. 11 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-12.txt | DOC-004 | PDF p. 12 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-13.txt | DOC-004 | PDF p. 13 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-14.txt | DOC-004 | PDF p. 14 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-15.txt | DOC-004 | PDF p. 15 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-16.txt | DOC-004 | PDF p. 16 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-17.txt | DOC-004 | PDF p. 17 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-18.txt | DOC-004 | PDF p. 18 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-19.txt | DOC-004 | PDF p. 19 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-20.txt | DOC-004 | PDF p. 20 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-21.txt | DOC-004 | PDF p. 21 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-22.txt | DOC-004 | PDF p. 22 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-23.txt | DOC-004 | PDF p. 23 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-24.txt | DOC-004 | PDF p. 24 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-25.txt | DOC-004 | PDF p. 25 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-26.txt | DOC-004 | PDF p. 26 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-27.txt | DOC-004 | PDF p. 27 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-28.txt | DOC-004 | PDF p. 28 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-29.txt | DOC-004 | PDF p. 29 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-30.txt | DOC-004 | PDF p. 30 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-31.txt | DOC-004 | PDF p. 31 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-32.txt | DOC-004 | PDF p. 32 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-33.txt | DOC-004 | PDF p. 33 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-34.txt | DOC-004 | PDF p. 34 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-35.txt | DOC-004 | PDF p. 35 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-36.txt | DOC-004 | PDF p. 36 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-37.txt | DOC-004 | PDF p. 37 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-38.txt | DOC-004 | PDF p. 38 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-39.txt | DOC-004 | PDF p. 39 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-40.txt | DOC-004 | PDF p. 40 | Page OCR; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr_by_page.txt | DOC-004 | PDF pp. 1-40 | Page OCR; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-01.png | DOC-004 | PDF p. 1 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-02.png | DOC-004 | PDF p. 2 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-03.png | DOC-004 | PDF p. 3 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-04.png | DOC-004 | PDF p. 4 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-05.png | DOC-004 | PDF p. 5 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-06.png | DOC-004 | PDF p. 6 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-07.png | DOC-004 | PDF p. 7 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-08.png | DOC-004 | PDF p. 8 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-09.png | DOC-004 | PDF p. 9 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-10.png | DOC-004 | PDF p. 10 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-11.png | DOC-004 | PDF p. 11 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-12.png | DOC-004 | PDF p. 12 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-13.png | DOC-004 | PDF p. 13 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-14.png | DOC-004 | PDF p. 14 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-15.png | DOC-004 | PDF p. 15 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-16.png | DOC-004 | PDF p. 16 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-17.png | DOC-004 | PDF p. 17 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-18.png | DOC-004 | PDF p. 18 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-19.png | DOC-004 | PDF p. 19 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-20.png | DOC-004 | PDF p. 20 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-21.png | DOC-004 | PDF p. 21 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-22.png | DOC-004 | PDF p. 22 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-23.png | DOC-004 | PDF p. 23 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-24.png | DOC-004 | PDF p. 24 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-25.png | DOC-004 | PDF p. 25 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-26.png | DOC-004 | PDF p. 26 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-27.png | DOC-004 | PDF p. 27 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-28.png | DOC-004 | PDF p. 28 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-29.png | DOC-004 | PDF p. 29 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-30.png | DOC-004 | PDF p. 30 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-31.png | DOC-004 | PDF p. 31 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-32.png | DOC-004 | PDF p. 32 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-33.png | DOC-004 | PDF p. 33 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-34.png | DOC-004 | PDF p. 34 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-35.png | DOC-004 | PDF p. 35 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-36.png | DOC-004 | PDF p. 36 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-37.png | DOC-004 | PDF p. 37 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-38.png | DOC-004 | PDF p. 38 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-39.png | DOC-004 | PDF p. 39 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-40.png | DOC-004 | PDF p. 40 | Rendered PNG; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-005/by_page.txt | DOC-005 | PDF pp. 1-7 | Source-marked native text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-005/layout.txt | DOC-005 | PDF pp. 1-7 | Native layout text; legacy engine/version unrecorded | USABLE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-007/by_page.txt | DOC-007 | PDF p. 1 | Source-marked native text; legacy engine/version unrecorded | DUPLICATE |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-007/layout.txt | DOC-007 | PDF p. 1 | Native layout text; legacy engine/version unrecorded | USABLE |

The legacy DOC-004 pp. 17-20 layout derivative contains only four form-feed bytes and is UNREADABLE as text. These same units have USABLE page images and OCR, so the unreadable derivative does not create a fresh-required source unit. No solely unreadable unit remains.

## Fresh gap coverage discovered during mapping

The protocol mapper identified incomplete embedded-graphic/formula coverage on DOC-003 pages 13, 18, 21, 71, 78, 80, 81. Reusable text remains usable for textual portions, but these seven unique units are classified fresh-required in the final coverage partition. Direct Poppler pdftoppm 26.01.0 on CPU produced preprocessing/support_protocol/page-N.png for each listed page; scale1800 for13/18, scale1400 for the others. Exact commands and source locations are in extraction/support_parts/protocol.md. Every image was inspected and mapped, closing the gap. Fresh derivatives are outside the reused-artifact hashes. Final counts: 250 preserved reused assets, 227 total pages, 220 reusable-backed pages, seven fresh-required pages, 227 mapped pages. No source or reused file was modified.

First statistical pass main-source visual confirmation: preprocessing/stat1_main/page-10.png, current DOC-001 physical PDF page10, direct Poppler pdftoppm26.01.0 CPU, -singlefile -scale-to2000 -png. This targeted confirmation is a fresh derivative outside the reused hashes; it verifies cited significance wording and does not change the already complete source-page partition.

First statistical pass forest-A direct-source confirmation: preprocessing/stat1_forest_a/direct-p13.png and direct-p14.png, DOC-006 physical pages13/14, direct Poppler pdftoppm26.01.0 CPU. Exact commands and provenance are recorded in statistics/parts/forest_a.md. These fresh confirmation derivatives are outside reused hashes and do not change mapped-unit coverage.

Report-matching direct-source confirmations: preprocessing/cross_reports/main-p7.png (DOC-001 p7), supp-13.png and supp-14.png (DOC-006 pp13/14), supp-p19.png, supp-p23.png and supp-p47.png (DOC-006 pp19/23/47). Direct Poppler pdftoppm26.01.0 CPU; all source pages rendered and viewed; commands recorded in checkers/cross_source_parts/reports.md. Fresh confirmations remain outside reused hashes and do not alter the completed coverage partition.

## Independent inclusion-screen source derivatives

Current run: preprocessing/inclusion_initial contains four full-source layout derivatives (main, analysis-specific SAP, protocol, results supplement) and 14 targeted PDF page PNGs. Direct Poppler 26.01.0; CPU. Exact source filenames, pages, commands and output names are recorded in screening/inclusion_screen.md. These are new derivatives, outside the immutable reused-asset hash set. No OCR or fallback was used. All source confirmations cover the complete 31-finding union.

## Independent recheck and second-pass source confirmation

The fresh evidence rechecker inspected existing current-run exact-source renders and direct PDF text for all 18 candidates; no new derivative was produced. Its source-image list and direct-reading provenance are in verification/evidence_recheck.md. All candidate transcriptions were reproduced; C015 received a documented classification correction only.

Current-run fresh derivative preprocessing/stat2_tables_a/source-p44.png renders DOC-006 PDF p.44 using direct Poppler 26.01.0 on CPU. The second-pass table reviewer records the exact command and source comparison in checkers/statistical_parts/pass2_tables_a.md. Its provisional nine-record alignment concern was not reproduced: mechanical before/current comparison found the existing inventory cells identical to the source values, so zero transcription corrections were needed. The first-pass checker and all supplied/reused files are preserved. No stable candidate or F-ST1-401 value changes. This derivative is outside the immutable reused hash set.

## Second-pass independent screen derivatives

preprocessing/inclusion_pass2/protocol-p48.png: DOC-003 physical PDF p.48, pdftoppm26.01.0,120dpi,CPU. preprocessing/inclusion_pass2/protocol-layout.txt: DOC-003 physical PDF pp.1–82, pdftotext26.01.0 layout,CPU. Exact source names and commands are in screening/inclusion_screen_pass_2.md. The full layout is a version-language locator; the scientific comparison is bounded to the cited primary-rule pages. These fresh derivatives are outside the preserved reused-artifact hash set.
