# Reusable-evidence asset inventory

Inventory covers all existing native/layout text, page images, extraction maps, source-location maps, page manifests, document records and package preprocessing metadata below the existing audit area. Fifty-two eligible files are enumerated and hashed in reused_artifact_hashes_before.sha256: 26 per-page native/layout texts; 9 layout-range texts; 1 duplicate layout text; 5 rendered PNGs; 5 document records; 1 package manifest; 2 page manifests; 2 source-linked quantitative evidence maps; and 1 OCR-engine metadata record. Five rights-screen records are preserved but are not extraction assets. New workflow1.6.1 files are not reused assets.

Fitness means usefulness for source location and transcription, never scientific adjudication. No prior candidate, checker, verifier, critic, screening, classification or final-report content was read. Source-linked document records and maps are permitted locators; their old scope exclusions do not limit this review.

## Engines, provenance and fitness procedure

Current direct extraction engine: Poppler pdftotext26.01.0; page inventory: pdfinfo26.01.0; integrity: sha256sum uutils coreutils0.10.0. Every per-page native text was byte-compared against `pdftotext -layout -nopgbrk -f N -l N "SOURCE.pdf" -`; all26 matched. All9 nonduplicate range texts were byte-compared against `pdftotext -layout -f FIRST -l LAST "SOURCE.pdf" -`; every range matched. Comparisons used process substitution and cmp; no additional derivative or source was written. Range records are separated by form-feed characters, so their relative record number plus FIRST-1 gives exact PDF page. `awk` with form-feed record separator identified20 empty protocol segments.

Historical native extraction engine is pdftotext, exact historical version unrecorded. Historical PNG renderer/version and source hash are unrecorded; file dimensions were checked with file and protocol p80 was visually inspected and readable. Existing images remain PARTIAL aids pending direct-source confirmation, conservatively adding no reusable-unit coverage. Existing OCR metadata records a CPU backend, but no retained OCR text exists; no GPU was probed or invoked. Current mapper derivatives must record their own engines. Tesseract5.5.0 CPU OCR is available for fresh-required pages if necessary.

## Exact eligible asset catalogue

Paths are package-relative. Each row is one actual file. USABLE text adds coverage only once even when a map or image overlaps. PARTIAL maps/records are source-linked locator aids whose legacy scope is incomplete for the current review. No stale or unreadable file was identified. DUPLICATE does not add coverage.

| Asset path | Exact source units | Type / engine | Fitness | Gap or fitness explanation |
|---|---|---|---|---|
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-001.txt | DOC-001 PDF p.1 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-002.txt | DOC-001 PDF p.2 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-003.txt | DOC-001 PDF p.3 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-004.txt | DOC-001 PDF p.4 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-005.txt | DOC-001 PDF p.5 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-006.txt | DOC-001 PDF p.6 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-007.txt | DOC-001 PDF p.7 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-008.txt | DOC-001 PDF p.8 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-009.txt | DOC-001 PDF p.9 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-010.txt | DOC-001 PDF p.10 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-001.txt | DOC-002 PDF p.1 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-002.txt | DOC-002 PDF p.2 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-003.txt | DOC-002 PDF p.3 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-004.txt | DOC-002 PDF p.4 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-005.txt | DOC-002 PDF p.5 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-006.txt | DOC-002 PDF p.6 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-007.txt | DOC-002 PDF p.7 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-008.txt | DOC-002 PDF p.8 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-009.txt | DOC-002 PDF p.9 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-010.txt | DOC-002 PDF p.10 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-011.txt | DOC-002 PDF p.11 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-012.txt | DOC-002 PDF p.12 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-013.txt | DOC-002 PDF p.13 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-014.txt | DOC-002 PDF p.14 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-015.txt | DOC-002 PDF p.15 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-016.txt | DOC-002 PDF p.16 | Native layout text / historical pdftotext | USABLE | Byte-identical current source extraction; no gap. |
| .ai_paper_validation/review_1_5_1/preprocessing/protocol_pp001_032_layout.txt | DOC-003 PDF pp.1-32 | Layout / pdftotext | PARTIAL | Source match; empty pp.15,19 require fresh inspection. |
| .ai_paper_validation/review_1_5_1/preprocessing/protocol_pp033_064_layout.txt | DOC-003 PDF pp.33-64 | Layout / pdftotext | USABLE | Source match; no text gap. |
| .ai_paper_validation/review_1_5_1/preprocessing/protocol_pp065_096_layout.txt | DOC-003 PDF pp.65-96 | Layout / pdftotext | PARTIAL | Source match; empty pp.74,80,81,84,89,90,91,94,96 require fresh inspection. |
| .ai_paper_validation/review_1_5_1/preprocessing/protocol_pp097_128_layout.txt | DOC-003 PDF pp.97-128 | Layout / pdftotext | PARTIAL | Source match; empty pp.105,107,109,116,118,120 require fresh inspection. |
| .ai_paper_validation/review_1_5_1/preprocessing/protocol_pp129_153_layout.txt | DOC-003 PDF pp.129-153 | Layout / pdftotext | PARTIAL | Source match; empty pp.133,134,136 require fresh inspection. |
| .ai_paper_validation/review_1_5_1/preprocessing/sap_pp001_032_layout.txt | DOC-004 PDF pp.1-32 | Layout / pdftotext | USABLE | Source match; no text gap. |
| .ai_paper_validation/review_1_5_1/preprocessing/sap_pp033_064_layout.txt | DOC-004 PDF pp.33-64 | Layout / pdftotext | USABLE | Source match; no text gap. |
| .ai_paper_validation/review_1_5_1/preprocessing/sap_pp065_083_layout.txt | DOC-004 PDF pp.65-83 | Layout / pdftotext | USABLE | Source match; no text gap. |
| .ai_paper_validation/review_1_5_1/preprocessing/sap_pp065_083_direct_check.txt | DOC-004 PDF pp.65-83 | Layout / pdftotext | DUPLICATE | Byte-identical sap_pp065_083_layout.txt. |
| .ai_paper_validation/review_1_5_1/preprocessing/data_sharing_p001_layout.txt | DOC-005 PDF p.1 | Layout / pdftotext | USABLE | Source match; no text gap. |
| .ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck_protocol_p080.png | DOC-003 PDF p.80 | PNG1700x2200 / historical renderer unrecorded | PARTIAL | Visually readable; provenance lacks original source hash/render command; fresh-required retained. |
| .ai_paper_validation/review_1_5_1/preprocessing/sap_pp065_067_render-65.png | DOC-004 PDF p.65 | PNG1360x1760 / historical renderer unrecorded | PARTIAL | Optional visual aid; source-matched layout is available. |
| .ai_paper_validation/review_1_5_1/preprocessing/sap_pp065_067_render-66.png | DOC-004 PDF p.66 | PNG1360x1760 / historical renderer unrecorded | PARTIAL | Optional visual aid; source-matched layout is available. |
| .ai_paper_validation/review_1_5_1/preprocessing/sap_pp065_067_render-67.png | DOC-004 PDF p.67 | PNG1360x1760 / historical renderer unrecorded | PARTIAL | Optional visual aid; source-matched layout is available. |
| .ai_paper_validation/review_1_5_1/preprocessing/sap_pp074_render-74.png | DOC-004 PDF p.74 | PNG1360x1760 / historical renderer unrecorded | PARTIAL | Optional visual aid; source-matched layout is available. |
| .ai_paper_validation/preprocessing/manifests/JAMA2019-12618-MAIN-page-manifest.md | DOC-001 PDF pp.1-10; one row per page | Page manifest / legacy record | USABLE | Exact page-to-text links match present source and all10 texts. |
| .ai_paper_validation/preprocessing/manifests/JAMA2019-12618-SUPP-RESULTS-page-manifest.md | DOC-002 PDF pp.1-16; one row per page | Page manifest / legacy record | USABLE | Exact page-to-text links match present source and all16 texts. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-MAIN/document_record.md | DOC-001 PDF pp.1-10; identity and p.1 headings | Document record / legacy record | PARTIAL | Identity usable; does not replace full mapping. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-SUPP-RESULTS/document_record.md | DOC-002 PDF pp.1-16; headings and table references | Document record / legacy record | PARTIAL | Identity usable; legacy selective scope ignored. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-PROTOCOL/document_record.md | DOC-003 PDF pp.1-153 identity; headings pp.1-3 | Document record / legacy record | PARTIAL | Legacy no-audit restriction ignored; not full extraction. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-SAP/document_record.md | DOC-004 PDF pp.1-83 identity; headings pp.1-3 | Document record / legacy record | PARTIAL | Legacy no-audit restriction ignored; not full extraction. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-DATA-SHARING/document_record.md | DOC-005 PDF p.1 | Document record / legacy record | PARTIAL | Legacy no-audit restriction ignored; source page mapped in current review. |
| .ai_paper_validation/document_outputs/package_manifest.md | DOC-001 pp.1-10; DOC-002 pp.1-16; DOC-003 pp.1-153; DOC-004 pp.1-83; DOC-005 p.1 identities | Package source-location manifest / legacy record | PARTIAL | Source counts independently confirmed; historical scope restrictions ignored. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-MAIN/main_article_result_evidence.md | DOC-001 PDF pp.1,3-9, Figure1 p.3, Table1 p.5, Table2 p.6, Figure2 p.7, Table3 p.8; selected methods p.3 | Source-linked quantitative evidence map / legacy extraction | PARTIAL | Selected values only; current mapping covers full pp.1-10 from usable texts. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-SUPP-RESULTS/result_relevant_evidence_map.md | DOC-002 PDF p.8 eTable2; pp.10-16 eTables4-9; contextual pointers pp.1-7,9 | Source-linked quantitative evidence map / legacy extraction | PARTIAL | Selected values only; old exclusions ignored; full pp.1-16 text reused. |
| .ai_paper_validation/preprocessing/ocr_backend.json | DOC-001 pp.1-10; DOC-002 pp.1-16 preprocessing configuration only | CPU OCR metadata / historical rapidocr_onnxruntime | USABLE | Provenance metadata only; no OCR page coverage or OCR text retained. |

## Complete partition and downstream assignments

DOC-00110/10, DOC-00216/16, DOC-00483/83, DOC-0051/1 pages have source-matched usable text. DOC-003133/153 pages have source-matched usable text; all20 remaining units require fresh visual inspection. Unique reusable total243 plus fresh-required20 equals263. Mapped counts remain zero until current mappers finish; all units must be assigned in coverage_manifest.md, irrespective of historical scope.

Exact fresh pages DOC-003:15,19,74,80,81,84,89,90,91,94,96,105,107,109,116,118,120,133,134,136. These are complete empty form-feed records, not proof of blank source pages. All non-usable records are backed by usable full text or enter these fresh assignments. No scientific unit may remain uncovered at completion.

Hash command: sorted eligible paths piped to sha256sum; before file contains52 package-relative entries. All eligible aids are frozen even if duplicate or only partly used, permitting end-of-run integrity confirmation. Sources and reused files were not modified.

## Fresh mapping gap discovered during current source inspection

DOC-003 p.18 contains an embedded endpoint flowchart omitted from reusable text despite the presence of native surrounding text. The protocol-a mapper rendered and visually mapped this page directly with Poppler, closing the gap. Its text asset is PARTIAL for that page. Updated unique partition: DOC-003132 reusable plus21 fresh-required equals153; package242 reusable plus21 fresh-required equals263. The eligible asset hash set remains unchanged. The complete fresh list now includes p.18 in addition to the20 initially identified text-empty pages.

Further mapper source inspection closed embedded-image/glyph gaps on DOC-003 pp.47,129,150. Reusable text omits Davis-scale labels on p.47, Miami-scale labels on p.129, and an eligibility glyph on p.150. All three were freshly rendered and visually mapped. Conservatively treating each partial-text page as fresh-required, final partition is DOC-003129 reusable plus24 fresh-required equals153; package239 reusable plus24 fresh-required equals263. These additional source inspections are documented in protocol-a and protocol-c mapper artifacts; original reuse hashes remain unchanged.

SAP formula subscripts on DOC-004 pp.23,24,26,34,63 were incompletely retained in reusable extraction. A fresh medium-effort mapper visually confirmed them from direct Poppler source renders, with adjacent pp.22,64 corroborated. Count five formula-gap pages fresh-required; DOC-00478reusable+5fresh=83. Final package partition234reusable+29fresh=263; scientific mapping is complete. The complete visual record is extraction/parts/sap_formula_visual_confirmation.md.
