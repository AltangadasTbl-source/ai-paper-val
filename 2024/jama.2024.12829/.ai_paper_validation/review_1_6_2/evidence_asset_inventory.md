# Evidence-asset inventory

Every one of the 472 eligible pre-existing artifacts below .ai_paper_validation is inventoried below and hashed in reused_artifact_hashes_before.sha256 using package-relative paths: 416 text files, 47 PNG page renders, two result extraction/source-location maps, three page manifests, three document records, and one package inventory. New review_1_6_2 files and tooling are excluded. No old candidate, screening, verifier, critic, quality, endetail, classification, or final-report record is used as a discovery input. Legacy selection statements in inventory metadata are not adopted.

Fitness is artifact-specific. USABLE means readable text or a valid retained PNG with an exact source-page locator; PARTIAL means sparse figure text, approximate OCR, selected evidence maps, or metadata that cannot cover a page alone; DUPLICATE means overlapping aggregated or additional recheck extraction; UNREADABLE means an empty OCR sidecar. No source unit depends solely on a PARTIAL or UNREADABLE asset. No STALE artifact was established: original source hashes were not retained in these legacy locators, so absence of staleness is not a whole-document source-identity guarantee. The current source remains authoritative. Modified metadata alone does not establish changed content.

All 47 rendered files passed the local file-format check as PNG images. Every text file was checked for non-whitespace content. DOC-002 page 12 OCR is empty; native page 9 has only 24 alphanumeric characters and requires its retained image. Pages 10-13 have sparse figure text and retained images. DOC-003 page 144 native/layout text has 36 alphanumeric characters: visual inspection of its page-144-render.png confirms an otherwise blank page with header, line numbers, and footer, so this text is USABLE. OCR glyph substitutions on DOC-002 page 6 illustrate why OCR is PARTIAL and images remain necessary.

Commands and engines: `rg --files --hidden .ai_paper_validation -g '!**/review_1_6_2/**'` enumerated assets; `sha256sum -- PATH` hashed each; `file PATH` checked PNGs; shell `tr`/`wc` checked text content. Legacy basis native_pages are pdftotext -layout output as documented by their page manifests; corresponding PNGs are retained page renders, with exact original engine version unavailable. review_1_5_3 native/layout/OCR/render derivatives carry exact page locators but do not retain reliable engine versions; they are recorded here as legacy native/layout, legacy OCR, and legacy page render rather than assigning an unestablished engine. Initial PDF counts used supplied pdf_tools.py info with the user environment, PyMuPDF 1.28.0. A direct current DOC-001 p8 inspection used `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text jama_sun_2024_oi_240088_1746815064.14747.pdf --first 8 --last 8 /dev/stdout --layout`, PyMuPDF 1.26.4 sorted reading order; its table agrees with the retained p8 transcription. It produced no persisted derivative. No new OCR or rendering was performed by this stage.

Disjoint mapper scopes: DOC-001 pp1-11 (main mapper); DOC-002 pp1-25 (support mapper); DOC-003 pp1-32,33-64,65-96,97-128,129-160,161-167 (support mapper shards). Each plan shard has at most 32 source pages. The pagewise layout character totals are respectively 68065, 76367, 61175, 72409, 56855, 9962; each is below 200000 characters. Prefer exact page files rather than legacy selected evidence summaries.

Canonical reusable paths: DOC-001 `.ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-NNN.txt` for pp1-11; DOC-002 `.ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-NNN.txt` for pp1-2,10-25 and `.ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-NNN-layout.txt` for pp3-9; DOC-003 the six named page-range directories under `.ai_paper_validation/review_1_5_3/preprocessing/`, with exact paths enumerated below. Retained sparse-page image anchors are DOC-002 pp6-9 `doc002_pp003-009/page-NNN.png`, pp10-13 `document_outputs/basis_results_supplement/extraction/page_images/page-NNN-NN.png`, and DOC-003 p144 `support_doc003_pp129-160/page-144-render.png`.

Artifact coverage below uses PDF page numbers. Metadata rows locate the whole source but contribute zero page coverage by themselves. DUPLICATE and PARTIAL rows do not increase unique reusable-unit counts. Initial curator assessment was zero fresh-required units; mapper correction establishes two (pp46 and48), and all203 pages received new scientific mapping, including visual inspection of image-bearing figures.

| Artifact path | Source | Exact source units | Kind / engine | Fitness | Bytes |
|---|---|---|---|---|---:|
| .ai_paper_validation/document_outputs/basis_main_article/document_record.yaml | DOC-001 | PDF pages 1-11; metadata only | legacy document/page metadata | PARTIAL | 3284 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-001.txt | DOC-001 | PDF page 1 | pdftotext -layout; version unavailable | USABLE | 7547 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-002.txt | DOC-001 | PDF page 2 | pdftotext -layout; version unavailable | USABLE | 8588 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-003.txt | DOC-001 | PDF page 3 | pdftotext -layout; version unavailable | USABLE | 8976 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-004.txt | DOC-001 | PDF page 4 | pdftotext -layout; version unavailable | USABLE | 8450 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-005.txt | DOC-001 | PDF page 5 | pdftotext -layout; version unavailable | USABLE | 9064 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-006.txt | DOC-001 | PDF page 6 | pdftotext -layout; version unavailable | USABLE | 11713 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-007.txt | DOC-001 | PDF page 7 | pdftotext -layout; version unavailable | USABLE | 9596 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-008.txt | DOC-001 | PDF page 8 | pdftotext -layout; version unavailable | USABLE | 10063 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-009.txt | DOC-001 | PDF page 9 | pdftotext -layout; version unavailable | USABLE | 10991 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-010.txt | DOC-001 | PDF page 10 | pdftotext -layout; version unavailable | USABLE | 11862 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/native_pages/page-011.txt | DOC-001 | PDF page 11 | pdftotext -layout; version unavailable | USABLE | 8096 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/normalized_text/main_article_selected_pages.txt | DOC-001 | PDF pages 1-11 | legacy native/layout; version unavailable | DUPLICATE | 105980 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/page_images/page-005-05.png | DOC-001 | PDF page 5 | legacy PNG page render; version unavailable | USABLE | 620080 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/page_images/page-006-06.png | DOC-001 | PDF page 6 | legacy PNG page render; version unavailable | USABLE | 698237 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/page_images/page-007-07.png | DOC-001 | PDF page 7 | legacy PNG page render; version unavailable | USABLE | 542617 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/page_images/page-008-08.png | DOC-001 | PDF page 8 | legacy PNG page render; version unavailable | USABLE | 722599 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/page_images/page-009-09.png | DOC-001 | PDF page 9 | legacy PNG page render; version unavailable | USABLE | 726371 |
| .ai_paper_validation/document_outputs/basis_main_article/extraction/page_manifest.yaml | DOC-001 | PDF pages 1-11; metadata only | legacy document/page metadata | PARTIAL | 3664 |
| .ai_paper_validation/document_outputs/basis_main_article/main_text_extraction.md | DOC-001 | PDF pages 1-11; selected result locations | source-location/result extraction map | PARTIAL | 12063 |
| .ai_paper_validation/document_outputs/basis_protocol_sap/document_record.yaml | DOC-003 | PDF pages 1-167; metadata only | legacy document/page metadata | PARTIAL | 4233 |
| .ai_paper_validation/document_outputs/basis_protocol_sap/extraction/page_manifest.yaml | DOC-003 | PDF pages 1-167; metadata only | legacy document/page metadata | PARTIAL | 596 |
| .ai_paper_validation/document_outputs/basis_results_supplement/document_record.yaml | DOC-002 | PDF pages 1-25; metadata only | legacy document/page metadata | PARTIAL | 4127 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-001.txt | DOC-002 | PDF page 1 | pdftotext -layout; version unavailable | USABLE | 545 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-002.txt | DOC-002 | PDF page 2 | pdftotext -layout; version unavailable | USABLE | 3357 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-010.txt | DOC-002 | PDF page 10 | pdftotext -layout; version unavailable | PARTIAL | 196 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-011.txt | DOC-002 | PDF page 11 | pdftotext -layout; version unavailable | PARTIAL | 119 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-012.txt | DOC-002 | PDF page 12 | pdftotext -layout; version unavailable | PARTIAL | 130 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-013.txt | DOC-002 | PDF page 13 | pdftotext -layout; version unavailable | PARTIAL | 333 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-014.txt | DOC-002 | PDF page 14 | pdftotext -layout; version unavailable | USABLE | 4239 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-015.txt | DOC-002 | PDF page 15 | pdftotext -layout; version unavailable | USABLE | 4125 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-016.txt | DOC-002 | PDF page 16 | pdftotext -layout; version unavailable | USABLE | 1094 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-017.txt | DOC-002 | PDF page 17 | pdftotext -layout; version unavailable | USABLE | 4006 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-018.txt | DOC-002 | PDF page 18 | pdftotext -layout; version unavailable | USABLE | 1388 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-019.txt | DOC-002 | PDF page 19 | pdftotext -layout; version unavailable | USABLE | 1188 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-020.txt | DOC-002 | PDF page 20 | pdftotext -layout; version unavailable | USABLE | 890 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-021.txt | DOC-002 | PDF page 21 | pdftotext -layout; version unavailable | USABLE | 2119 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-022.txt | DOC-002 | PDF page 22 | pdftotext -layout; version unavailable | USABLE | 2139 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-023.txt | DOC-002 | PDF page 23 | pdftotext -layout; version unavailable | USABLE | 2010 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-024.txt | DOC-002 | PDF page 24 | pdftotext -layout; version unavailable | USABLE | 3825 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/native_pages/page-025.txt | DOC-002 | PDF page 25 | pdftotext -layout; version unavailable | USABLE | 1630 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/normalized_text/results_supplement_selected_pages.txt | DOC-002 | PDF pages 1-2, 10-25 | legacy native/layout; version unavailable | DUPLICATE | 34747 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-010-10.png | DOC-002 | PDF page 10 | legacy PNG page render; version unavailable | USABLE | 392643 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-011-11.png | DOC-002 | PDF page 11 | legacy PNG page render; version unavailable | USABLE | 178608 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-012-12.png | DOC-002 | PDF page 12 | legacy PNG page render; version unavailable | USABLE | 258455 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-013-13.png | DOC-002 | PDF page 13 | legacy PNG page render; version unavailable | USABLE | 399486 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-014-14.png | DOC-002 | PDF page 14 | legacy PNG page render; version unavailable | USABLE | 258828 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-015-15.png | DOC-002 | PDF page 15 | legacy PNG page render; version unavailable | USABLE | 267466 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-016-16.png | DOC-002 | PDF page 16 | legacy PNG page render; version unavailable | USABLE | 107247 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-017-17.png | DOC-002 | PDF page 17 | legacy PNG page render; version unavailable | USABLE | 265962 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-018-18.png | DOC-002 | PDF page 18 | legacy PNG page render; version unavailable | USABLE | 121581 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-019-19.png | DOC-002 | PDF page 19 | legacy PNG page render; version unavailable | USABLE | 129953 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-020-20.png | DOC-002 | PDF page 20 | legacy PNG page render; version unavailable | USABLE | 87665 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-021-21.png | DOC-002 | PDF page 21 | legacy PNG page render; version unavailable | USABLE | 206443 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-022-22.png | DOC-002 | PDF page 22 | legacy PNG page render; version unavailable | USABLE | 208592 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-023-23.png | DOC-002 | PDF page 23 | legacy PNG page render; version unavailable | USABLE | 199915 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-024-24.png | DOC-002 | PDF page 24 | legacy PNG page render; version unavailable | USABLE | 246709 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_images/page-025-25.png | DOC-002 | PDF page 25 | legacy PNG page render; version unavailable | USABLE | 124888 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/page_manifest.yaml | DOC-002 | PDF pages 1-25; metadata only | legacy document/page metadata | PARTIAL | 7151 |
| .ai_paper_validation/document_outputs/basis_results_supplement/extraction/results_supplement_evidence_map.md | DOC-002 | PDF pages 10-25; selected result locations | source-location/result extraction map | PARTIAL | 10768 |
| .ai_paper_validation/package_manifest.yaml | DOC-001, DOC-002, DOC-003 | all three direct sources; metadata only | legacy package inventory | PARTIAL | 1901 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_figures/page-010-ocr.txt | DOC-002 | PDF page 10 | legacy OCR; engine version unavailable | PARTIAL | 825 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_figures/page-010.png | DOC-002 | PDF page 10 | legacy PNG page render; version unavailable | USABLE | 1000722 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_figures/page-011-ocr.txt | DOC-002 | PDF page 11 | legacy OCR; engine version unavailable | PARTIAL | 667 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_figures/page-011.png | DOC-002 | PDF page 11 | legacy PNG page render; version unavailable | USABLE | 442918 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_figures/page-012-ocr.txt | DOC-002 | PDF page 12 | legacy OCR; engine version unavailable | UNREADABLE | 0 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_figures/page-012.png | DOC-002 | PDF page 12 | legacy PNG page render; version unavailable | USABLE | 631563 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-003-layout.txt | DOC-002 | PDF page 3 | legacy native/layout; version unavailable | USABLE | 3188 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-003-native.txt | DOC-002 | PDF page 3 | legacy native/layout; version unavailable | USABLE | 1729 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-004-layout.txt | DOC-002 | PDF page 4 | legacy native/layout; version unavailable | USABLE | 461 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-004-native.txt | DOC-002 | PDF page 4 | legacy native/layout; version unavailable | USABLE | 272 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-005-layout.txt | DOC-002 | PDF page 5 | legacy native/layout; version unavailable | USABLE | 2949 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-005-native.txt | DOC-002 | PDF page 5 | legacy native/layout; version unavailable | USABLE | 1897 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-006-layout.txt | DOC-002 | PDF page 6 | legacy native/layout; version unavailable | USABLE | 420 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-006-native.txt | DOC-002 | PDF page 6 | legacy native/layout; version unavailable | USABLE | 365 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-006-ocr.txt | DOC-002 | PDF page 6 | legacy OCR; engine version unavailable | PARTIAL | 726 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-006.png | DOC-002 | PDF page 6 | legacy PNG page render; version unavailable | USABLE | 225267 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-007-layout.txt | DOC-002 | PDF page 7 | legacy native/layout; version unavailable | USABLE | 120 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-007-native.txt | DOC-002 | PDF page 7 | legacy native/layout; version unavailable | USABLE | 67 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-007-ocr.txt | DOC-002 | PDF page 7 | legacy OCR; engine version unavailable | PARTIAL | 1294 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-007.png | DOC-002 | PDF page 7 | legacy PNG page render; version unavailable | USABLE | 445062 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-008-layout.txt | DOC-002 | PDF page 8 | legacy native/layout; version unavailable | USABLE | 120 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-008-native.txt | DOC-002 | PDF page 8 | legacy native/layout; version unavailable | USABLE | 69 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-008-ocr.txt | DOC-002 | PDF page 8 | legacy OCR; engine version unavailable | PARTIAL | 268 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-008.png | DOC-002 | PDF page 8 | legacy PNG page render; version unavailable | USABLE | 703479 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-009-layout.txt | DOC-002 | PDF page 9 | legacy native/layout; version unavailable | PARTIAL | 73 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-009-native.txt | DOC-002 | PDF page 9 | legacy native/layout; version unavailable | PARTIAL | 37 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-009-ocr.txt | DOC-002 | PDF page 9 | legacy OCR; engine version unavailable | PARTIAL | 749 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc002_pp003-009/page-009.png | DOC-002 | PDF page 9 | legacy PNG page render; version unavailable | USABLE | 781502 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/layout.txt | DOC-003 | PDF pages 65-96 | legacy native/layout; version unavailable | DUPLICATE | 61468 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/native.txt | DOC-003 | PDF pages 65-96 | legacy native/layout; version unavailable | DUPLICATE | 49329 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-065-layout.txt | DOC-003 | PDF page 65 | legacy native/layout; version unavailable | USABLE | 2710 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-065-native.txt | DOC-003 | PDF page 65 | legacy native/layout; version unavailable | USABLE | 1813 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-066-layout.txt | DOC-003 | PDF page 66 | legacy native/layout; version unavailable | USABLE | 2738 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-066-native.txt | DOC-003 | PDF page 66 | legacy native/layout; version unavailable | USABLE | 1798 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-067-layout.txt | DOC-003 | PDF page 67 | legacy native/layout; version unavailable | USABLE | 2764 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-067-native.txt | DOC-003 | PDF page 67 | legacy native/layout; version unavailable | USABLE | 1792 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-068-layout.txt | DOC-003 | PDF page 68 | legacy native/layout; version unavailable | USABLE | 2103 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-068-native.txt | DOC-003 | PDF page 68 | legacy native/layout; version unavailable | USABLE | 1671 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-069-layout.txt | DOC-003 | PDF page 69 | legacy native/layout; version unavailable | USABLE | 2849 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-069-native.txt | DOC-003 | PDF page 69 | legacy native/layout; version unavailable | USABLE | 1761 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-069-render.png | DOC-003 | PDF page 69 | legacy PNG page render; version unavailable | USABLE | 274338 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-070-layout.txt | DOC-003 | PDF page 70 | legacy native/layout; version unavailable | USABLE | 487 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-070-native.txt | DOC-003 | PDF page 70 | legacy native/layout; version unavailable | USABLE | 285 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-071-layout.txt | DOC-003 | PDF page 71 | legacy native/layout; version unavailable | USABLE | 1313 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-071-native.txt | DOC-003 | PDF page 71 | legacy native/layout; version unavailable | USABLE | 1112 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-072-layout.txt | DOC-003 | PDF page 72 | legacy native/layout; version unavailable | USABLE | 786 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-072-native.txt | DOC-003 | PDF page 72 | legacy native/layout; version unavailable | USABLE | 615 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-073-layout.txt | DOC-003 | PDF page 73 | legacy native/layout; version unavailable | USABLE | 5526 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-073-native.txt | DOC-003 | PDF page 73 | legacy native/layout; version unavailable | USABLE | 2494 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-073-render.png | DOC-003 | PDF page 73 | legacy PNG page render; version unavailable | USABLE | 370703 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-074-layout.txt | DOC-003 | PDF page 74 | legacy native/layout; version unavailable | USABLE | 353 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-074-native.txt | DOC-003 | PDF page 74 | legacy native/layout; version unavailable | USABLE | 215 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-075-layout.txt | DOC-003 | PDF page 75 | legacy native/layout; version unavailable | USABLE | 2198 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-075-native.txt | DOC-003 | PDF page 75 | legacy native/layout; version unavailable | USABLE | 2037 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-076-layout.txt | DOC-003 | PDF page 76 | legacy native/layout; version unavailable | USABLE | 1868 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-076-native.txt | DOC-003 | PDF page 76 | legacy native/layout; version unavailable | USABLE | 1717 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-077-layout.txt | DOC-003 | PDF page 77 | legacy native/layout; version unavailable | USABLE | 2225 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-077-native.txt | DOC-003 | PDF page 77 | legacy native/layout; version unavailable | USABLE | 1992 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-078-layout.txt | DOC-003 | PDF page 78 | legacy native/layout; version unavailable | USABLE | 1948 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-078-native.txt | DOC-003 | PDF page 78 | legacy native/layout; version unavailable | USABLE | 1772 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-079-layout.txt | DOC-003 | PDF page 79 | legacy native/layout; version unavailable | USABLE | 1867 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-079-native.txt | DOC-003 | PDF page 79 | legacy native/layout; version unavailable | USABLE | 1612 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-080-layout.txt | DOC-003 | PDF page 80 | legacy native/layout; version unavailable | USABLE | 1606 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-080-native.txt | DOC-003 | PDF page 80 | legacy native/layout; version unavailable | USABLE | 1398 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-081-layout.txt | DOC-003 | PDF page 81 | legacy native/layout; version unavailable | USABLE | 1886 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-081-native.txt | DOC-003 | PDF page 81 | legacy native/layout; version unavailable | USABLE | 1711 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-082-layout.txt | DOC-003 | PDF page 82 | legacy native/layout; version unavailable | USABLE | 1885 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-082-native.txt | DOC-003 | PDF page 82 | legacy native/layout; version unavailable | USABLE | 1685 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-083-layout.txt | DOC-003 | PDF page 83 | legacy native/layout; version unavailable | USABLE | 1887 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-083-native.txt | DOC-003 | PDF page 83 | legacy native/layout; version unavailable | USABLE | 1698 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-084-layout.txt | DOC-003 | PDF page 84 | legacy native/layout; version unavailable | USABLE | 1819 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-084-native.txt | DOC-003 | PDF page 84 | legacy native/layout; version unavailable | USABLE | 1662 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-084-render.png | DOC-003 | PDF page 84 | legacy PNG page render; version unavailable | USABLE | 231492 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-085-layout.txt | DOC-003 | PDF page 85 | legacy native/layout; version unavailable | USABLE | 1793 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-085-native.txt | DOC-003 | PDF page 85 | legacy native/layout; version unavailable | USABLE | 1630 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-086-layout.txt | DOC-003 | PDF page 86 | legacy native/layout; version unavailable | USABLE | 1938 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-086-native.txt | DOC-003 | PDF page 86 | legacy native/layout; version unavailable | USABLE | 1737 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-087-layout.txt | DOC-003 | PDF page 87 | legacy native/layout; version unavailable | USABLE | 1900 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-087-native.txt | DOC-003 | PDF page 87 | legacy native/layout; version unavailable | USABLE | 1688 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-088-layout.txt | DOC-003 | PDF page 88 | legacy native/layout; version unavailable | USABLE | 1947 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-088-native.txt | DOC-003 | PDF page 88 | legacy native/layout; version unavailable | USABLE | 1787 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-089-layout.txt | DOC-003 | PDF page 89 | legacy native/layout; version unavailable | USABLE | 1825 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-089-native.txt | DOC-003 | PDF page 89 | legacy native/layout; version unavailable | USABLE | 1639 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-090-layout.txt | DOC-003 | PDF page 90 | legacy native/layout; version unavailable | USABLE | 1912 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-090-native.txt | DOC-003 | PDF page 90 | legacy native/layout; version unavailable | USABLE | 1752 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-091-layout.txt | DOC-003 | PDF page 91 | legacy native/layout; version unavailable | USABLE | 1815 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-091-native.txt | DOC-003 | PDF page 91 | legacy native/layout; version unavailable | USABLE | 1653 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-092-layout.txt | DOC-003 | PDF page 92 | legacy native/layout; version unavailable | USABLE | 1861 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-092-native.txt | DOC-003 | PDF page 92 | legacy native/layout; version unavailable | USABLE | 1665 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-093-layout.txt | DOC-003 | PDF page 93 | legacy native/layout; version unavailable | USABLE | 1404 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-093-native.txt | DOC-003 | PDF page 93 | legacy native/layout; version unavailable | USABLE | 1217 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-094-layout.txt | DOC-003 | PDF page 94 | legacy native/layout; version unavailable | USABLE | 1406 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-094-native.txt | DOC-003 | PDF page 94 | legacy native/layout; version unavailable | USABLE | 1224 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-095-layout.txt | DOC-003 | PDF page 95 | legacy native/layout; version unavailable | USABLE | 1375 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-095-native.txt | DOC-003 | PDF page 95 | legacy native/layout; version unavailable | USABLE | 1200 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-096-layout.txt | DOC-003 | PDF page 96 | legacy native/layout; version unavailable | USABLE | 1474 |
| .ai_paper_validation/review_1_5_3/preprocessing/doc003_pp065-096/page-096-native.txt | DOC-003 | PDF page 96 | legacy native/layout; version unavailable | USABLE | 1297 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc001_p002_layout.txt | DOC-001 | PDF page 2 | legacy native/layout; version unavailable | DUPLICATE | 8588 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc001_p003_layout.txt | DOC-001 | PDF page 3 | legacy native/layout; version unavailable | DUPLICATE | 8976 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc001_p004_layout.txt | DOC-001 | PDF page 4 | legacy native/layout; version unavailable | DUPLICATE | 8450 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc001_p005_layout.txt | DOC-001 | PDF page 5 | legacy native/layout; version unavailable | DUPLICATE | 9064 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc001_p006_layout.txt | DOC-001 | PDF page 6 | legacy native/layout; version unavailable | DUPLICATE | 11713 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc001_p008_layout.txt | DOC-001 | PDF page 8 | legacy native/layout; version unavailable | DUPLICATE | 10063 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p006.png | DOC-002 | PDF page 6 | legacy PNG page render; version unavailable | DUPLICATE | 166178 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p006_layout.txt | DOC-002 | PDF page 6 | legacy native/layout; version unavailable | DUPLICATE | 420 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p010.png | DOC-002 | PDF page 10 | legacy PNG page render; version unavailable | DUPLICATE | 243534 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p010_layout.txt | DOC-002 | PDF page 10 | legacy native/layout; version unavailable | DUPLICATE | 196 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p014_layout.txt | DOC-002 | PDF page 14 | legacy native/layout; version unavailable | DUPLICATE | 4239 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p016_layout.txt | DOC-002 | PDF page 16 | legacy native/layout; version unavailable | DUPLICATE | 1094 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p017_layout.txt | DOC-002 | PDF page 17 | legacy native/layout; version unavailable | DUPLICATE | 4006 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p019_layout.txt | DOC-002 | PDF page 19 | legacy native/layout; version unavailable | DUPLICATE | 1188 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p020_layout.txt | DOC-002 | PDF page 20 | legacy native/layout; version unavailable | DUPLICATE | 890 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p021_layout.txt | DOC-002 | PDF page 21 | legacy native/layout; version unavailable | DUPLICATE | 2119 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p022_layout.txt | DOC-002 | PDF page 22 | legacy native/layout; version unavailable | DUPLICATE | 2139 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc002_p023_layout.txt | DOC-002 | PDF page 23 | legacy native/layout; version unavailable | DUPLICATE | 2010 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc003_p001_layout.txt | DOC-003 | PDF page 1 | legacy native/layout; version unavailable | DUPLICATE | 784 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc003_p002_layout.txt | DOC-003 | PDF page 2 | legacy native/layout; version unavailable | DUPLICATE | 519 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc003_p003_layout.txt | DOC-003 | PDF page 3 | legacy native/layout; version unavailable | DUPLICATE | 787 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc003_p004_layout.txt | DOC-003 | PDF page 4 | legacy native/layout; version unavailable | DUPLICATE | 4936 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc003_p005_layout.txt | DOC-003 | PDF page 5 | legacy native/layout; version unavailable | DUPLICATE | 3936 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc003_p007_layout.txt | DOC-003 | PDF page 7 | legacy native/layout; version unavailable | DUPLICATE | 2642 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc003_p015_layout.txt | DOC-003 | PDF page 15 | legacy native/layout; version unavailable | DUPLICATE | 5435 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc003_p021_layout.txt | DOC-003 | PDF page 21 | legacy native/layout; version unavailable | DUPLICATE | 1896 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc003_p035_layout.txt | DOC-003 | PDF page 35 | legacy native/layout; version unavailable | DUPLICATE | 1708 |
| .ai_paper_validation/review_1_5_3/preprocessing/evidence_recheck_doc003_p096_layout.txt | DOC-003 | PDF page 96 | legacy native/layout; version unavailable | DUPLICATE | 1474 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-001.layout.txt | DOC-003 | PDF page 1 | legacy native/layout; version unavailable | USABLE | 784 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-001.native.txt | DOC-003 | PDF page 1 | legacy native/layout; version unavailable | USABLE | 580 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-002.layout.txt | DOC-003 | PDF page 2 | legacy native/layout; version unavailable | USABLE | 519 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-002.native.txt | DOC-003 | PDF page 2 | legacy native/layout; version unavailable | USABLE | 361 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-003.layout.txt | DOC-003 | PDF page 3 | legacy native/layout; version unavailable | USABLE | 787 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-003.native.txt | DOC-003 | PDF page 3 | legacy native/layout; version unavailable | USABLE | 514 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-004.layout.txt | DOC-003 | PDF page 4 | legacy native/layout; version unavailable | USABLE | 4936 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-004.native.txt | DOC-003 | PDF page 4 | legacy native/layout; version unavailable | USABLE | 4590 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-005.layout.txt | DOC-003 | PDF page 5 | legacy native/layout; version unavailable | USABLE | 3936 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-005.native.txt | DOC-003 | PDF page 5 | legacy native/layout; version unavailable | USABLE | 3640 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-006.layout.txt | DOC-003 | PDF page 6 | legacy native/layout; version unavailable | USABLE | 1106 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-006.native.txt | DOC-003 | PDF page 6 | legacy native/layout; version unavailable | USABLE | 867 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-007.layout.txt | DOC-003 | PDF page 7 | legacy native/layout; version unavailable | USABLE | 2642 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-007.native.txt | DOC-003 | PDF page 7 | legacy native/layout; version unavailable | USABLE | 1704 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-008.layout.txt | DOC-003 | PDF page 8 | legacy native/layout; version unavailable | USABLE | 2480 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-008.native.txt | DOC-003 | PDF page 8 | legacy native/layout; version unavailable | USABLE | 1651 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-009.layout.txt | DOC-003 | PDF page 9 | legacy native/layout; version unavailable | USABLE | 2625 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-009.native.txt | DOC-003 | PDF page 9 | legacy native/layout; version unavailable | USABLE | 1689 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-010.layout.txt | DOC-003 | PDF page 10 | legacy native/layout; version unavailable | USABLE | 2266 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-010.native.txt | DOC-003 | PDF page 10 | legacy native/layout; version unavailable | USABLE | 1793 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-011.layout.txt | DOC-003 | PDF page 11 | legacy native/layout; version unavailable | USABLE | 2605 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-011.native.txt | DOC-003 | PDF page 11 | legacy native/layout; version unavailable | USABLE | 1945 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-012.layout.txt | DOC-003 | PDF page 12 | legacy native/layout; version unavailable | USABLE | 1932 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-012.native.txt | DOC-003 | PDF page 12 | legacy native/layout; version unavailable | USABLE | 1203 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-013.layout.txt | DOC-003 | PDF page 13 | legacy native/layout; version unavailable | USABLE | 1553 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-013.native.txt | DOC-003 | PDF page 13 | legacy native/layout; version unavailable | USABLE | 1026 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-014.layout.txt | DOC-003 | PDF page 14 | legacy native/layout; version unavailable | USABLE | 1085 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-014.native.txt | DOC-003 | PDF page 14 | legacy native/layout; version unavailable | USABLE | 879 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-015.layout.txt | DOC-003 | PDF page 15 | legacy native/layout; version unavailable | USABLE | 5435 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-015.native.txt | DOC-003 | PDF page 15 | legacy native/layout; version unavailable | USABLE | 2436 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-016.layout.txt | DOC-003 | PDF page 16 | legacy native/layout; version unavailable | USABLE | 348 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-016.native.txt | DOC-003 | PDF page 16 | legacy native/layout; version unavailable | USABLE | 213 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-017.layout.txt | DOC-003 | PDF page 17 | legacy native/layout; version unavailable | USABLE | 2390 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-017.native.txt | DOC-003 | PDF page 17 | legacy native/layout; version unavailable | USABLE | 2223 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-018.layout.txt | DOC-003 | PDF page 18 | legacy native/layout; version unavailable | USABLE | 2159 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-018.native.txt | DOC-003 | PDF page 18 | legacy native/layout; version unavailable | USABLE | 2001 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-019.layout.txt | DOC-003 | PDF page 19 | legacy native/layout; version unavailable | USABLE | 2339 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-019.native.txt | DOC-003 | PDF page 19 | legacy native/layout; version unavailable | USABLE | 2104 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-020.layout.txt | DOC-003 | PDF page 20 | legacy native/layout; version unavailable | USABLE | 2154 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-020.native.txt | DOC-003 | PDF page 20 | legacy native/layout; version unavailable | USABLE | 1917 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-021.layout.txt | DOC-003 | PDF page 21 | legacy native/layout; version unavailable | USABLE | 1896 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-021.native.txt | DOC-003 | PDF page 21 | legacy native/layout; version unavailable | USABLE | 1667 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-022.layout.txt | DOC-003 | PDF page 22 | legacy native/layout; version unavailable | USABLE | 2026 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-022.native.txt | DOC-003 | PDF page 22 | legacy native/layout; version unavailable | USABLE | 1832 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-023.layout.txt | DOC-003 | PDF page 23 | legacy native/layout; version unavailable | USABLE | 1968 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-023.native.txt | DOC-003 | PDF page 23 | legacy native/layout; version unavailable | USABLE | 1778 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-024.layout.txt | DOC-003 | PDF page 24 | legacy native/layout; version unavailable | USABLE | 2054 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-024.native.txt | DOC-003 | PDF page 24 | legacy native/layout; version unavailable | USABLE | 1888 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-025.layout.txt | DOC-003 | PDF page 25 | legacy native/layout; version unavailable | USABLE | 2234 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-025.native.txt | DOC-003 | PDF page 25 | legacy native/layout; version unavailable | USABLE | 2069 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-026.layout.txt | DOC-003 | PDF page 26 | legacy native/layout; version unavailable | USABLE | 2119 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-026.native.txt | DOC-003 | PDF page 26 | legacy native/layout; version unavailable | USABLE | 1880 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-027.layout.txt | DOC-003 | PDF page 27 | legacy native/layout; version unavailable | USABLE | 2225 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-027.native.txt | DOC-003 | PDF page 27 | legacy native/layout; version unavailable | USABLE | 2027 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-028.layout.txt | DOC-003 | PDF page 28 | legacy native/layout; version unavailable | USABLE | 2030 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-028.native.txt | DOC-003 | PDF page 28 | legacy native/layout; version unavailable | USABLE | 1872 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-029.layout.txt | DOC-003 | PDF page 29 | legacy native/layout; version unavailable | USABLE | 2076 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-029.native.txt | DOC-003 | PDF page 29 | legacy native/layout; version unavailable | USABLE | 1912 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-030.layout.txt | DOC-003 | PDF page 30 | legacy native/layout; version unavailable | USABLE | 1753 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-030.native.txt | DOC-003 | PDF page 30 | legacy native/layout; version unavailable | USABLE | 1586 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-031.layout.txt | DOC-003 | PDF page 31 | legacy native/layout; version unavailable | USABLE | 2063 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-031.native.txt | DOC-003 | PDF page 31 | legacy native/layout; version unavailable | USABLE | 1865 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-032.layout.txt | DOC-003 | PDF page 32 | legacy native/layout; version unavailable | USABLE | 1826 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp001-032/page-032.native.txt | DOC-003 | PDF page 32 | legacy native/layout; version unavailable | USABLE | 1624 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-045.png | DOC-003 | PDF page 45 | legacy PNG page render; version unavailable | USABLE | 355408 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-047.png | DOC-003 | PDF page 47 | legacy PNG page render; version unavailable | USABLE | 343026 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-058.png | DOC-003 | PDF page 58 | legacy PNG page render; version unavailable | USABLE | 280773 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-33.layout.txt | DOC-003 | PDF page 33 | legacy native/layout; version unavailable | USABLE | 1386 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-33.native.txt | DOC-003 | PDF page 33 | legacy native/layout; version unavailable | USABLE | 1212 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-34.layout.txt | DOC-003 | PDF page 34 | legacy native/layout; version unavailable | USABLE | 1521 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-34.native.txt | DOC-003 | PDF page 34 | legacy native/layout; version unavailable | USABLE | 1347 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-35.layout.txt | DOC-003 | PDF page 35 | legacy native/layout; version unavailable | USABLE | 1708 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-35.native.txt | DOC-003 | PDF page 35 | legacy native/layout; version unavailable | USABLE | 1532 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-36.layout.txt | DOC-003 | PDF page 36 | legacy native/layout; version unavailable | USABLE | 2207 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-36.native.txt | DOC-003 | PDF page 36 | legacy native/layout; version unavailable | USABLE | 2044 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-37.layout.txt | DOC-003 | PDF page 37 | legacy native/layout; version unavailable | USABLE | 2428 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-37.native.txt | DOC-003 | PDF page 37 | legacy native/layout; version unavailable | USABLE | 1866 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-38.layout.txt | DOC-003 | PDF page 38 | legacy native/layout; version unavailable | USABLE | 2078 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-38.native.txt | DOC-003 | PDF page 38 | legacy native/layout; version unavailable | USABLE | 1905 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-39.layout.txt | DOC-003 | PDF page 39 | legacy native/layout; version unavailable | USABLE | 2184 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-39.native.txt | DOC-003 | PDF page 39 | legacy native/layout; version unavailable | USABLE | 2025 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-40.layout.txt | DOC-003 | PDF page 40 | legacy native/layout; version unavailable | USABLE | 2095 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-40.native.txt | DOC-003 | PDF page 40 | legacy native/layout; version unavailable | USABLE | 1934 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-41.layout.txt | DOC-003 | PDF page 41 | legacy native/layout; version unavailable | USABLE | 1689 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-41.native.txt | DOC-003 | PDF page 41 | legacy native/layout; version unavailable | USABLE | 1513 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-42.layout.txt | DOC-003 | PDF page 42 | legacy native/layout; version unavailable | USABLE | 2237 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-42.native.txt | DOC-003 | PDF page 42 | legacy native/layout; version unavailable | USABLE | 1772 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-43.layout.txt | DOC-003 | PDF page 43 | legacy native/layout; version unavailable | USABLE | 3731 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-43.native.txt | DOC-003 | PDF page 43 | legacy native/layout; version unavailable | USABLE | 2638 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-44.layout.txt | DOC-003 | PDF page 44 | legacy native/layout; version unavailable | USABLE | 2484 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-44.native.txt | DOC-003 | PDF page 44 | legacy native/layout; version unavailable | USABLE | 2101 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-45.layout.txt | DOC-003 | PDF page 45 | legacy native/layout; version unavailable | USABLE | 1542 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-45.native.txt | DOC-003 | PDF page 45 | legacy native/layout; version unavailable | USABLE | 1340 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-46.layout.txt | DOC-003 | PDF page 46 | legacy native/layout; version unavailable | PARTIAL | 871 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-46.native.txt | DOC-003 | PDF page 46 | legacy native/layout; version unavailable | PARTIAL | 707 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-47.layout.txt | DOC-003 | PDF page 47 | legacy native/layout; version unavailable | USABLE | 1296 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-47.native.txt | DOC-003 | PDF page 47 | legacy native/layout; version unavailable | USABLE | 1119 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-48.layout.txt | DOC-003 | PDF page 48 | legacy native/layout; version unavailable | PARTIAL | 1289 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-48.native.txt | DOC-003 | PDF page 48 | legacy native/layout; version unavailable | PARTIAL | 1136 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-49.layout.txt | DOC-003 | PDF page 49 | legacy native/layout; version unavailable | USABLE | 1464 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-49.native.txt | DOC-003 | PDF page 49 | legacy native/layout; version unavailable | USABLE | 1286 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-50.layout.txt | DOC-003 | PDF page 50 | legacy native/layout; version unavailable | USABLE | 4857 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-50.native.txt | DOC-003 | PDF page 50 | legacy native/layout; version unavailable | USABLE | 4307 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-51.layout.txt | DOC-003 | PDF page 51 | legacy native/layout; version unavailable | USABLE | 1278 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-51.native.txt | DOC-003 | PDF page 51 | legacy native/layout; version unavailable | USABLE | 747 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-52.layout.txt | DOC-003 | PDF page 52 | legacy native/layout; version unavailable | USABLE | 2006 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-52.native.txt | DOC-003 | PDF page 52 | legacy native/layout; version unavailable | USABLE | 1054 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-53.layout.txt | DOC-003 | PDF page 53 | legacy native/layout; version unavailable | USABLE | 3970 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-53.native.txt | DOC-003 | PDF page 53 | legacy native/layout; version unavailable | USABLE | 2894 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-54.layout.txt | DOC-003 | PDF page 54 | legacy native/layout; version unavailable | USABLE | 5380 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-54.native.txt | DOC-003 | PDF page 54 | legacy native/layout; version unavailable | USABLE | 3347 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-55.layout.txt | DOC-003 | PDF page 55 | legacy native/layout; version unavailable | USABLE | 4283 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-55.native.txt | DOC-003 | PDF page 55 | legacy native/layout; version unavailable | USABLE | 2979 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-56.layout.txt | DOC-003 | PDF page 56 | legacy native/layout; version unavailable | USABLE | 5764 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-56.native.txt | DOC-003 | PDF page 56 | legacy native/layout; version unavailable | USABLE | 3263 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-57.layout.txt | DOC-003 | PDF page 57 | legacy native/layout; version unavailable | USABLE | 1603 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-57.native.txt | DOC-003 | PDF page 57 | legacy native/layout; version unavailable | USABLE | 1291 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-58.layout.txt | DOC-003 | PDF page 58 | legacy native/layout; version unavailable | USABLE | 597 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-58.native.txt | DOC-003 | PDF page 58 | legacy native/layout; version unavailable | USABLE | 397 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-59.layout.txt | DOC-003 | PDF page 59 | legacy native/layout; version unavailable | USABLE | 1215 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-59.native.txt | DOC-003 | PDF page 59 | legacy native/layout; version unavailable | USABLE | 862 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-60.layout.txt | DOC-003 | PDF page 60 | legacy native/layout; version unavailable | USABLE | 829 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-60.native.txt | DOC-003 | PDF page 60 | legacy native/layout; version unavailable | USABLE | 551 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-61.layout.txt | DOC-003 | PDF page 61 | legacy native/layout; version unavailable | USABLE | 4997 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-61.native.txt | DOC-003 | PDF page 61 | legacy native/layout; version unavailable | USABLE | 4645 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-62.layout.txt | DOC-003 | PDF page 62 | legacy native/layout; version unavailable | USABLE | 3778 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-62.native.txt | DOC-003 | PDF page 62 | legacy native/layout; version unavailable | USABLE | 3500 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-63.layout.txt | DOC-003 | PDF page 63 | legacy native/layout; version unavailable | USABLE | 1147 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-63.native.txt | DOC-003 | PDF page 63 | legacy native/layout; version unavailable | USABLE | 909 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-64.layout.txt | DOC-003 | PDF page 64 | legacy native/layout; version unavailable | USABLE | 2763 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/page-64.native.txt | DOC-003 | PDF page 64 | legacy native/layout; version unavailable | USABLE | 1768 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/pages-033-064.layout.txt | DOC-003 | PDF pages 33-64 | legacy native/layout; version unavailable | DUPLICATE | 76677 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp033-064/pages-033-064.native.txt | DOC-003 | PDF pages 33-64 | legacy native/layout; version unavailable | DUPLICATE | 59991 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-100.layout.txt | DOC-003 | PDF page 100 | legacy native/layout; version unavailable | USABLE | 1768 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-100.native.txt | DOC-003 | PDF page 100 | legacy native/layout; version unavailable | USABLE | 1612 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-101.layout.txt | DOC-003 | PDF page 101 | legacy native/layout; version unavailable | USABLE | 1993 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-101.native.txt | DOC-003 | PDF page 101 | legacy native/layout; version unavailable | USABLE | 1837 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-102.layout.txt | DOC-003 | PDF page 102 | legacy native/layout; version unavailable | USABLE | 1914 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-102.native.txt | DOC-003 | PDF page 102 | legacy native/layout; version unavailable | USABLE | 1760 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-103.layout.txt | DOC-003 | PDF page 103 | legacy native/layout; version unavailable | USABLE | 1594 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-103.native.txt | DOC-003 | PDF page 103 | legacy native/layout; version unavailable | USABLE | 1428 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-104.layout.txt | DOC-003 | PDF page 104 | legacy native/layout; version unavailable | USABLE | 2303 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-104.native.txt | DOC-003 | PDF page 104 | legacy native/layout; version unavailable | USABLE | 1819 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-105.layout.txt | DOC-003 | PDF page 105 | legacy native/layout; version unavailable | USABLE | 3233 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-105.native.txt | DOC-003 | PDF page 105 | legacy native/layout; version unavailable | USABLE | 2332 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-106.layout.txt | DOC-003 | PDF page 106 | legacy native/layout; version unavailable | USABLE | 2343 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-106.native.txt | DOC-003 | PDF page 106 | legacy native/layout; version unavailable | USABLE | 1855 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-107.layout.txt | DOC-003 | PDF page 107 | legacy native/layout; version unavailable | USABLE | 1830 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-107.native.txt | DOC-003 | PDF page 107 | legacy native/layout; version unavailable | USABLE | 1653 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-108.layout.txt | DOC-003 | PDF page 108 | legacy native/layout; version unavailable | USABLE | 1061 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-108.native.txt | DOC-003 | PDF page 108 | legacy native/layout; version unavailable | USABLE | 889 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-109.layout.txt | DOC-003 | PDF page 109 | legacy native/layout; version unavailable | USABLE | 1279 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-109.native.txt | DOC-003 | PDF page 109 | legacy native/layout; version unavailable | USABLE | 1110 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-110.layout.txt | DOC-003 | PDF page 110 | legacy native/layout; version unavailable | USABLE | 1109 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-110.native.txt | DOC-003 | PDF page 110 | legacy native/layout; version unavailable | USABLE | 955 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-111.layout.txt | DOC-003 | PDF page 111 | legacy native/layout; version unavailable | USABLE | 1717 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-111.native.txt | DOC-003 | PDF page 111 | legacy native/layout; version unavailable | USABLE | 1546 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-112.layout.txt | DOC-003 | PDF page 112 | legacy native/layout; version unavailable | USABLE | 4462 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-112.native.txt | DOC-003 | PDF page 112 | legacy native/layout; version unavailable | USABLE | 3967 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-113.layout.txt | DOC-003 | PDF page 113 | legacy native/layout; version unavailable | USABLE | 1927 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-113.native.txt | DOC-003 | PDF page 113 | legacy native/layout; version unavailable | USABLE | 1594 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-114.layout.txt | DOC-003 | PDF page 114 | legacy native/layout; version unavailable | USABLE | 889 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-114.native.txt | DOC-003 | PDF page 114 | legacy native/layout; version unavailable | USABLE | 646 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-115.layout.txt | DOC-003 | PDF page 115 | legacy native/layout; version unavailable | USABLE | 1883 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-115.native.txt | DOC-003 | PDF page 115 | legacy native/layout; version unavailable | USABLE | 1071 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-116.layout.txt | DOC-003 | PDF page 116 | legacy native/layout; version unavailable | USABLE | 3348 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-116.native.txt | DOC-003 | PDF page 116 | legacy native/layout; version unavailable | USABLE | 2251 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-117.layout.txt | DOC-003 | PDF page 117 | legacy native/layout; version unavailable | USABLE | 3666 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-117.native.txt | DOC-003 | PDF page 117 | legacy native/layout; version unavailable | USABLE | 2791 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-118.layout.txt | DOC-003 | PDF page 118 | legacy native/layout; version unavailable | USABLE | 4378 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-118.native.txt | DOC-003 | PDF page 118 | legacy native/layout; version unavailable | USABLE | 2912 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-119.layout.txt | DOC-003 | PDF page 119 | legacy native/layout; version unavailable | USABLE | 4270 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-119.native.txt | DOC-003 | PDF page 119 | legacy native/layout; version unavailable | USABLE | 3109 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-120.layout.txt | DOC-003 | PDF page 120 | legacy native/layout; version unavailable | USABLE | 2489 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-120.native.txt | DOC-003 | PDF page 120 | legacy native/layout; version unavailable | USABLE | 1479 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-121.layout.txt | DOC-003 | PDF page 121 | legacy native/layout; version unavailable | USABLE | 1639 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-121.native.txt | DOC-003 | PDF page 121 | legacy native/layout; version unavailable | USABLE | 1296 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-122.layout.txt | DOC-003 | PDF page 122 | legacy native/layout; version unavailable | USABLE | 612 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-122.native.txt | DOC-003 | PDF page 122 | legacy native/layout; version unavailable | USABLE | 403 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-123.layout.txt | DOC-003 | PDF page 123 | legacy native/layout; version unavailable | USABLE | 1239 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-123.native.txt | DOC-003 | PDF page 123 | legacy native/layout; version unavailable | USABLE | 822 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-124.layout.txt | DOC-003 | PDF page 124 | legacy native/layout; version unavailable | USABLE | 2810 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-124.native.txt | DOC-003 | PDF page 124 | legacy native/layout; version unavailable | USABLE | 1549 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-125.layout.txt | DOC-003 | PDF page 125 | legacy native/layout; version unavailable | USABLE | 1930 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-125.native.txt | DOC-003 | PDF page 125 | legacy native/layout; version unavailable | USABLE | 1510 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-126.layout.txt | DOC-003 | PDF page 126 | legacy native/layout; version unavailable | USABLE | 2488 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-126.native.txt | DOC-003 | PDF page 126 | legacy native/layout; version unavailable | USABLE | 1005 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-127.layout.txt | DOC-003 | PDF page 127 | legacy native/layout; version unavailable | USABLE | 1250 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-127.native.txt | DOC-003 | PDF page 127 | legacy native/layout; version unavailable | USABLE | 758 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-128.layout.txt | DOC-003 | PDF page 128 | legacy native/layout; version unavailable | USABLE | 4842 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-128.native.txt | DOC-003 | PDF page 128 | legacy native/layout; version unavailable | USABLE | 4499 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-97.layout.txt | DOC-003 | PDF page 97 | legacy native/layout; version unavailable | USABLE | 2035 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-97.native.txt | DOC-003 | PDF page 97 | legacy native/layout; version unavailable | USABLE | 1871 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-98.layout.txt | DOC-003 | PDF page 98 | legacy native/layout; version unavailable | USABLE | 2291 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-98.native.txt | DOC-003 | PDF page 98 | legacy native/layout; version unavailable | USABLE | 1871 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-99.layout.txt | DOC-003 | PDF page 99 | legacy native/layout; version unavailable | USABLE | 1896 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/page-99.native.txt | DOC-003 | PDF page 99 | legacy native/layout; version unavailable | USABLE | 1589 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/rendered-108.png | DOC-003 | PDF page 108 | legacy PNG page render; version unavailable | USABLE | 447003 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/rendered-109.png | DOC-003 | PDF page 109 | legacy PNG page render; version unavailable | USABLE | 344080 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp097-128/rendered-110.png | DOC-003 | PDF page 110 | legacy PNG page render; version unavailable | USABLE | 271668 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-129.layout.txt | DOC-003 | PDF page 129 | legacy native/layout; version unavailable | USABLE | 1327 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-129.native.txt | DOC-003 | PDF page 129 | legacy native/layout; version unavailable | USABLE | 1105 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-130.layout.txt | DOC-003 | PDF page 130 | legacy native/layout; version unavailable | USABLE | 1671 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-130.native.txt | DOC-003 | PDF page 130 | legacy native/layout; version unavailable | USABLE | 1503 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-131.layout.txt | DOC-003 | PDF page 131 | legacy native/layout; version unavailable | USABLE | 1857 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-131.native.txt | DOC-003 | PDF page 131 | legacy native/layout; version unavailable | USABLE | 1559 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-132.layout.txt | DOC-003 | PDF page 132 | legacy native/layout; version unavailable | USABLE | 1585 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-132.native.txt | DOC-003 | PDF page 132 | legacy native/layout; version unavailable | USABLE | 1405 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-133.layout.txt | DOC-003 | PDF page 133 | legacy native/layout; version unavailable | USABLE | 2078 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-133.native.txt | DOC-003 | PDF page 133 | legacy native/layout; version unavailable | USABLE | 1846 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-134.layout.txt | DOC-003 | PDF page 134 | legacy native/layout; version unavailable | USABLE | 1840 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-134.native.txt | DOC-003 | PDF page 134 | legacy native/layout; version unavailable | USABLE | 1684 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-135.layout.txt | DOC-003 | PDF page 135 | legacy native/layout; version unavailable | USABLE | 1800 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-135.native.txt | DOC-003 | PDF page 135 | legacy native/layout; version unavailable | USABLE | 1642 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-136.layout.txt | DOC-003 | PDF page 136 | legacy native/layout; version unavailable | USABLE | 2037 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-136.native.txt | DOC-003 | PDF page 136 | legacy native/layout; version unavailable | USABLE | 1892 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-137.layout.txt | DOC-003 | PDF page 137 | legacy native/layout; version unavailable | USABLE | 1982 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-137.native.txt | DOC-003 | PDF page 137 | legacy native/layout; version unavailable | USABLE | 1835 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-138.layout.txt | DOC-003 | PDF page 138 | legacy native/layout; version unavailable | USABLE | 2328 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-138.native.txt | DOC-003 | PDF page 138 | legacy native/layout; version unavailable | USABLE | 2183 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-139.layout.txt | DOC-003 | PDF page 139 | legacy native/layout; version unavailable | USABLE | 1904 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-139.native.txt | DOC-003 | PDF page 139 | legacy native/layout; version unavailable | USABLE | 1741 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-140.layout.txt | DOC-003 | PDF page 140 | legacy native/layout; version unavailable | USABLE | 1568 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-140.native.txt | DOC-003 | PDF page 140 | legacy native/layout; version unavailable | USABLE | 1359 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-141.layout.txt | DOC-003 | PDF page 141 | legacy native/layout; version unavailable | USABLE | 1841 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-141.native.txt | DOC-003 | PDF page 141 | legacy native/layout; version unavailable | USABLE | 1568 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-142.layout.txt | DOC-003 | PDF page 142 | legacy native/layout; version unavailable | USABLE | 1969 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-142.native.txt | DOC-003 | PDF page 142 | legacy native/layout; version unavailable | USABLE | 1807 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-143.layout.txt | DOC-003 | PDF page 143 | legacy native/layout; version unavailable | USABLE | 1495 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-143.native.txt | DOC-003 | PDF page 143 | legacy native/layout; version unavailable | USABLE | 1231 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-144-render.png | DOC-003 | PDF page 144 | legacy PNG page render; version unavailable | USABLE | 24089 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-144.layout.txt | DOC-003 | PDF page 144 | legacy native/layout; version unavailable | USABLE | 81 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-144.native.txt | DOC-003 | PDF page 144 | legacy native/layout; version unavailable | USABLE | 47 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-145.layout.txt | DOC-003 | PDF page 145 | legacy native/layout; version unavailable | USABLE | 1250 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-145.native.txt | DOC-003 | PDF page 145 | legacy native/layout; version unavailable | USABLE | 757 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-146.layout.txt | DOC-003 | PDF page 146 | legacy native/layout; version unavailable | USABLE | 4315 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-146.native.txt | DOC-003 | PDF page 146 | legacy native/layout; version unavailable | USABLE | 3982 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-147.layout.txt | DOC-003 | PDF page 147 | legacy native/layout; version unavailable | USABLE | 1201 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-147.native.txt | DOC-003 | PDF page 147 | legacy native/layout; version unavailable | USABLE | 980 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-148.layout.txt | DOC-003 | PDF page 148 | legacy native/layout; version unavailable | USABLE | 1600 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-148.native.txt | DOC-003 | PDF page 148 | legacy native/layout; version unavailable | USABLE | 1447 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-149.layout.txt | DOC-003 | PDF page 149 | legacy native/layout; version unavailable | USABLE | 1868 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-149.native.txt | DOC-003 | PDF page 149 | legacy native/layout; version unavailable | USABLE | 1567 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-150.layout.txt | DOC-003 | PDF page 150 | legacy native/layout; version unavailable | USABLE | 1700 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-150.native.txt | DOC-003 | PDF page 150 | legacy native/layout; version unavailable | USABLE | 1425 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-151.layout.txt | DOC-003 | PDF page 151 | legacy native/layout; version unavailable | USABLE | 1791 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-151.native.txt | DOC-003 | PDF page 151 | legacy native/layout; version unavailable | USABLE | 1634 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-152.layout.txt | DOC-003 | PDF page 152 | legacy native/layout; version unavailable | USABLE | 2059 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-152.native.txt | DOC-003 | PDF page 152 | legacy native/layout; version unavailable | USABLE | 1835 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-153.layout.txt | DOC-003 | PDF page 153 | legacy native/layout; version unavailable | USABLE | 1775 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-153.native.txt | DOC-003 | PDF page 153 | legacy native/layout; version unavailable | USABLE | 1629 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-154.layout.txt | DOC-003 | PDF page 154 | legacy native/layout; version unavailable | USABLE | 1840 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-154.native.txt | DOC-003 | PDF page 154 | legacy native/layout; version unavailable | USABLE | 1691 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-155.layout.txt | DOC-003 | PDF page 155 | legacy native/layout; version unavailable | USABLE | 1493 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-155.native.txt | DOC-003 | PDF page 155 | legacy native/layout; version unavailable | USABLE | 1346 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-156.layout.txt | DOC-003 | PDF page 156 | legacy native/layout; version unavailable | USABLE | 1725 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-156.native.txt | DOC-003 | PDF page 156 | legacy native/layout; version unavailable | USABLE | 1573 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-157.layout.txt | DOC-003 | PDF page 157 | legacy native/layout; version unavailable | USABLE | 1796 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-157.native.txt | DOC-003 | PDF page 157 | legacy native/layout; version unavailable | USABLE | 1647 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-158.layout.txt | DOC-003 | PDF page 158 | legacy native/layout; version unavailable | USABLE | 1946 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-158.native.txt | DOC-003 | PDF page 158 | legacy native/layout; version unavailable | USABLE | 1799 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-159.layout.txt | DOC-003 | PDF page 159 | legacy native/layout; version unavailable | USABLE | 1852 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-159.native.txt | DOC-003 | PDF page 159 | legacy native/layout; version unavailable | USABLE | 1698 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-160.layout.txt | DOC-003 | PDF page 160 | legacy native/layout; version unavailable | USABLE | 1472 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp129-160/page-160.native.txt | DOC-003 | PDF page 160 | legacy native/layout; version unavailable | USABLE | 1271 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-161.layout.txt | DOC-003 | PDF page 161 | legacy native/layout; version unavailable | USABLE | 2105 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-161.native.txt | DOC-003 | PDF page 161 | legacy native/layout; version unavailable | USABLE | 1788 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-161.png | DOC-003 | PDF page 161 | legacy PNG page render; version unavailable | USABLE | 322819 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-162.layout.txt | DOC-003 | PDF page 162 | legacy native/layout; version unavailable | USABLE | 1637 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-162.native.txt | DOC-003 | PDF page 162 | legacy native/layout; version unavailable | USABLE | 1481 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-162.png | DOC-003 | PDF page 162 | legacy PNG page render; version unavailable | USABLE | 272915 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-163.layout.txt | DOC-003 | PDF page 163 | legacy native/layout; version unavailable | USABLE | 1928 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-163.native.txt | DOC-003 | PDF page 163 | legacy native/layout; version unavailable | USABLE | 1721 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-163.png | DOC-003 | PDF page 163 | legacy PNG page render; version unavailable | USABLE | 318056 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-164.layout.txt | DOC-003 | PDF page 164 | legacy native/layout; version unavailable | USABLE | 408 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-164.native.txt | DOC-003 | PDF page 164 | legacy native/layout; version unavailable | USABLE | 287 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-164.png | DOC-003 | PDF page 164 | legacy PNG page render; version unavailable | USABLE | 94803 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-165.layout.txt | DOC-003 | PDF page 165 | legacy native/layout; version unavailable | USABLE | 3212 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-165.native.txt | DOC-003 | PDF page 165 | legacy native/layout; version unavailable | USABLE | 2081 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-165.png | DOC-003 | PDF page 165 | legacy PNG page render; version unavailable | USABLE | 368016 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-166.layout.txt | DOC-003 | PDF page 166 | legacy native/layout; version unavailable | USABLE | 483 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-166.native.txt | DOC-003 | PDF page 166 | legacy native/layout; version unavailable | USABLE | 379 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-166.png | DOC-003 | PDF page 166 | legacy PNG page render; version unavailable | USABLE | 84443 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-167.layout.txt | DOC-003 | PDF page 167 | legacy native/layout; version unavailable | USABLE | 212 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-167.native.txt | DOC-003 | PDF page 167 | legacy native/layout; version unavailable | USABLE | 212 |
| .ai_paper_validation/review_1_5_3/preprocessing/support_doc003_pp161-167/page-167.png | DOC-003 | PDF page 167 | legacy PNG page render; version unavailable | USABLE | 90906 |

## Coordinator gap correction after fresh mapping began

DOC-003 pp46 and48 contain embedded device parameter tables absent from retained native/layout text and have no retained page images. Those text artifacts are PARTIAL for complete unit coverage; the two pages are now fresh-required in source_coverage.md. CPU PyMuPDF 1.26.4 helper renders at 200 dpi were produced as preprocessing/plan-page-46.png and preprocessing/plan-page-48.png, and the assigned mapper visually inspects them to close coverage. The initial count of zero fresh-required units is superseded by two. DOC-003 pp108-110 do have retained rendered-108.png, rendered-109.png, rendered-110.png; these remain reusable-backed. Additional p108/p110 renders were produced concurrently while resolving the image locators, and are preserved as new derivatives with the same engine/device. No new OCR has been needed.

## Current-run direct-source derivatives and confirmations

All following images are fresh current-source renders from the supplied pdf_tools.py helper, PyMuPDF1.26.4, CPU,200dpi. They are not reused artifacts and are excluded from the reused hash inventory. Current-source direct text confirmations are recorded in mapper/checker artifacts and use the same pinned helper/engine; some were transient /dev/stdout outputs.

| New derivative relative to review directory | Direct source page | Engine / device |
|---|---|---|
| preprocessing/plan-page-46.png | DOC-003p46 | PyMuPDF1.26.4 / CPU200dpi |
| preprocessing/plan-page-48.png | DOC-003p48 | PyMuPDF1.26.4 / CPU200dpi |
| preprocessing/plan-page-108.png | DOC-003p108 | PyMuPDF1.26.4 / CPU200dpi |
| preprocessing/plan-page-110.png | DOC-003p110 | PyMuPDF1.26.4 / CPU200dpi |
| preprocessing/stat1-main-p8.png | DOC-001p8 | PyMuPDF1.26.4 / CPU200dpi |
| preprocessing/stat1-supp-p13.png | DOC-002p13 | PyMuPDF1.26.4 / CPU200dpi |
| preprocessing/stat1-supp-p24.png | DOC-002p24 | PyMuPDF1.26.4 / CPU200dpi |
| preprocessing/stat1-supp-p19.png | DOC-002p19 | PyMuPDF1.26.4 / CPU200dpi |
| preprocessing/stat1-supp-p21.png | DOC-002p21 | PyMuPDF1.26.4 / CPU200dpi |
| preprocessing/numeric_checker-supp13.png | DOC-002p13 | PyMuPDF1.26.4 / CPU200dpi |
| preprocessing/cross_checker/report-supp-p13.png | DOC-002p13 | PyMuPDF1.26.4 / CPU200dpi |

Final reusable-asset fitness after mapper gap correction: 412 USABLE,34 DUPLICATE,25 PARTIAL,1 UNREADABLE (472 total). The four native/layout files on DOC-003pp46/48 are PARTIAL because their raster device tables are absent. Hashes remain unchanged; fitness annotation is a new-review inventory judgment and does not alter the retained assets. Final source-unit partition is201 reusable and2 fresh-required, all203 mapped.

### Independent-screen derivatives

The initial inclusion screener used supplied pdf_tools.py with pinned PyMuPDF 1.26.4 on CPU. Renders were 200 dpi; native text used the helper's direct text mode. These current-run derivatives are not reused assets.

| New derivative relative to review directory | Direct source unit | Engine / device |
|---|---|---|
| preprocessing/screen-supp-p20.png | DOC-002 p20 | PyMuPDF 1.26.4 / CPU, 200 dpi |
| preprocessing/screen-supp-p23.png | DOC-002 p23 | PyMuPDF 1.26.4 / CPU, 200 dpi |
| preprocessing/screen-main.txt | DOC-001 pp1–8 | PyMuPDF 1.26.4 / CPU, native text |
| preprocessing/screen-supp.txt | DOC-002 pp13–24 | PyMuPDF 1.26.4 / CPU, native text |
| preprocessing/screen-origplan.txt | DOC-003 pp11–18 | PyMuPDF 1.26.4 / CPU, native text |
| preprocessing/screen-origstat.txt | DOC-003 pp40–41 | PyMuPDF 1.26.4 / CPU, native text |
| preprocessing/screen-finalstat.txt | DOC-003 pp102–103 | PyMuPDF 1.26.4 / CPU, native text |
| preprocessing/screen-origsap.txt | DOC-003 pp136–142 | PyMuPDF 1.26.4 / CPU, native text |
| preprocessing/screen-finalsap.txt | DOC-003 pp155–162 | PyMuPDF 1.26.4 / CPU, native text |
| preprocessing/screen-plan115.txt | DOC-003 p115 | PyMuPDF 1.26.4 / CPU, native text |

### Evidence-recheck derivatives

The fresh rechecker produced 23 source-page native text locators and 16 source-page renders under preprocessing/evidence_rechecker/. Every derivative uses supplied pdf_tools.py, PyMuPDF 1.26.4, CPU; renders are 200 dpi. The complete file-to-source-unit provenance appears in verification/evidence_recheck.md. These current-run derivatives are excluded from reused-asset hashes.

### Statistical-pass-2 derivatives

Seventeen current-source native text locators under preprocessing/statistics_pass_2/ use supplied pdf_tools.py, PyMuPDF 1.26.4, CPU. Exact derivative/source-unit associations are recorded in checkers/statistical_pass_2.md. These are new derivatives, outside reused-asset hashes; no additional renders or OCR were needed.
