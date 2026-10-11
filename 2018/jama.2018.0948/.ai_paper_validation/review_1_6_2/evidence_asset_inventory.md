# Workflow 1.6.2 Reusable Evidence-Asset Inventory

The existing audit area contains 67 extraction/provenance assets: 4 native texts, 4 layout texts, 53 rendered PNG pages, 4 PDF metadata records, 1 obsolete page-status manifest and 1 earlier tool probe. There are no existing OCR text files, standalone table/workbook extractions or other document/source-location maps. All 67 consulted assets are hashed in `reused_artifact_hashes_before.sha256`; hashing the obsolete manifest preserves inventory provenance and does not make it a scientific input. No legacy candidate, checker, screening, verifier, critic, endetail, classification or final-report content was read.

## Fitness and coverage rules

USABLE means readable and source-linked for its stated locator/transcription purpose. PARTIAL means an asset needs a complementary representation for part of its stated scope. STALE means the asset cannot determine current tooling or completion. DUPLICATE means overlapping metadata that adds no unique source units. No unreadable asset was found. Overlapping native text, layout text, images and metadata count each direct source page only once.

The inherited metadata identifies Poppler 26.01.0 for `pdfinfo`; inherited extraction/rendering versions are not recorded. Current identity/fitness checks use direct Poppler 25.03.0 `pdfinfo` and `pdftotext`, `cmp`, `diff`, `awk`, `file` and visual image inspection. Current Pandoc is 3.1.11.1; it creates no evidence derivative in this stage. No new OCR, render or extraction derivative was written. The CPU is the recorded compute device. Existing PNGs are readable 1530 × 1980 RGB images (150-dpi letter-page dimensions); their original rendering engine is unrecorded. Numeric evidence remains subject to exact direct-source confirmation.

## Text assets

| Asset path | Source ID | Exact source units | Method/engine | Fitness | Unique-coverage basis and limitations |
|---|---|---|---|---|---|
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/jama_parshuram_2018_oi_180015.txt | DOC-001 | PDF pp. 1-11 | Inherited native text; current pdftotext 25.03.0 comparison | USABLE | Exact current bytes; all 11 form-feed-delimited pages |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/jama_parshuram_2018_oi_180015.txt | DOC-001 | PDF pp. 1-11 | Inherited layout text; current pdftotext 25.03.0 comparison | USABLE | Identical token multiset; whitespace/order changes only |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180015supp1_prod.txt | DOC-002 | PDF pp. 1-37 | Inherited native text; current pdftotext 25.03.0 comparison | USABLE | Exact current bytes; all 37 pages |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi180015supp1_prod.txt | DOC-002 | PDF pp. 1-37 | Inherited layout text; current pdftotext 25.03.0 comparison | USABLE | Exact current bytes; all 37 pages |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180015supp2_prod.txt | DOC-003 | PDF pp. 1-7 | Inherited native text; current pdftotext 25.03.0 comparison | USABLE | Exact current bytes; all 7 pages; native reading order puts line numbers separately |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi180015supp2_prod.txt | DOC-003 | PDF pp. 1-7 | Inherited layout text; current pdftotext 25.03.0 comparison | USABLE | Exact current bytes; line-numbered SAP and code layout retained |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180015supp3_prod.txt | DOC-004 | PDF pp. 1-14 | Inherited native text; current pdftotext 25.03.0 comparison | PARTIAL | p. 2 graph-label reading order is not reliable alone; rendered p. 2 supplies visual coverage; remaining pages readable |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi180015supp3_prod.txt | DOC-004 | PDF pp. 1-14 | Inherited layout text; current pdftotext 25.03.0 comparison | PARTIAL | p. 2 overlapping labels/order and `2per` token segmentation differ; rendered p. 2 supplies visual coverage |

## Rendered pages

Every row maps one existing image to one physical PDF page using the stable source IDs above. File signatures/dimensions are readable; visual inspection of DOC-003 p. 1 and DOC-004 p. 2 confirms representative source identity and legibility. Mappers inspect each relevant image as needed; this inventory makes no scientific-coverage claim.

| Asset path | Source ID | Exact source unit | Method/engine | Fitness |
|---|---|---|---|---|
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p1.png | DOC-001 | PDF p. 1 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p2.png | DOC-001 | PDF p. 2 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p3.png | DOC-001 | PDF p. 3 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p4.png | DOC-001 | PDF p. 4 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p5.png | DOC-001 | PDF p. 5 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p6.png | DOC-001 | PDF p. 6 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p7.png | DOC-001 | PDF p. 7 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p8.png | DOC-001 | PDF p. 8 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p9.png | DOC-001 | PDF p. 9 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p10.png | DOC-002 | PDF p. 10 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p11.png | DOC-002 | PDF p. 11 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p12.png | DOC-002 | PDF p. 12 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p13.png | DOC-002 | PDF p. 13 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p14.png | DOC-002 | PDF p. 14 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p15.png | DOC-002 | PDF p. 15 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p16.png | DOC-002 | PDF p. 16 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p17.png | DOC-002 | PDF p. 17 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p19.png | DOC-002 | PDF p. 19 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p20.png | DOC-002 | PDF p. 20 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p21.png | DOC-002 | PDF p. 21 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p22.png | DOC-002 | PDF p. 22 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p23.png | DOC-002 | PDF p. 23 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p24.png | DOC-002 | PDF p. 24 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p25.png | DOC-002 | PDF p. 25 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p26.png | DOC-002 | PDF p. 26 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p27.png | DOC-002 | PDF p. 27 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p28.png | DOC-002 | PDF p. 28 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p29.png | DOC-002 | PDF p. 29 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p30.png | DOC-002 | PDF p. 30 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p7.png | DOC-002 | PDF p. 7 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p8.png | DOC-002 | PDF p. 8 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p9.png | DOC-002 | PDF p. 9 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p1.png | DOC-003 | PDF p. 1 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p2.png | DOC-003 | PDF p. 2 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p3.png | DOC-003 | PDF p. 3 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p4.png | DOC-003 | PDF p. 4 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p5.png | DOC-003 | PDF p. 5 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p6.png | DOC-003 | PDF p. 6 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p7.png | DOC-003 | PDF p. 7 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p1.png | DOC-004 | PDF p. 1 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p10.png | DOC-004 | PDF p. 10 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p11.png | DOC-004 | PDF p. 11 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p12.png | DOC-004 | PDF p. 12 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p13.png | DOC-004 | PDF p. 13 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p14.png | DOC-004 | PDF p. 14 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p2.png | DOC-004 | PDF p. 2 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p3.png | DOC-004 | PDF p. 3 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p4.png | DOC-004 | PDF p. 4 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p5.png | DOC-004 | PDF p. 5 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p6.png | DOC-004 | PDF p. 6 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p7.png | DOC-004 | PDF p. 7 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p8.png | DOC-004 | PDF p. 8 | Inherited PNG; original engine unrecorded | USABLE |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-p9.png | DOC-004 | PDF p. 9 | Inherited PNG; original engine unrecorded | USABLE |

## Metadata and manifests

| Asset path | Source ID | Exact source units | Method/engine | Fitness | Use and limitation |
|---|---|---|---|---|---|
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-001_pdfinfo.txt | DOC-001 | PDF pp. 1-11 identity/count only | pdfinfo 26.01.0, confirmed by current 25.03.0 | USABLE | 11-page source identity; no numeric result transcription |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002_pdfinfo.txt | DOC-002 | PDF pp. 1-37 identity/count only | pdfinfo 26.01.0, confirmed by current 25.03.0 | USABLE | 37-page source identity; no numeric result transcription |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003_pdfinfo.txt | DOC-003 | PDF pp. 1-7 identity/count only | pdfinfo 26.01.0, confirmed by current 25.03.0 | USABLE | 7-page source identity; no numeric result transcription |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-004_pdfinfo.txt | DOC-004 | PDF pp. 1-14 identity/count only | pdfinfo 26.01.0, confirmed by current 25.03.0 | USABLE | 14-page source identity; no numeric result transcription |
| .ai_paper_validation/review_1_5_2/preprocessing/tool_and_page_status.md | DOC-001, DOC-002, DOC-003, DOC-004 | Enumerates all 69 PDF pages | Historical manual page-tree/tool-status record | STALE | States tools were absent and pages blocked; superseded by current tool probe and confirmed sources. Not used to assert scientific completion |
| .ai_paper_validation/review_1_6_1/preprocessing/tool_probe.json | None | No source units | Supplied pdf_tools.py probe, Python 3.13.5 | DUPLICATE | Historical operational provenance only; current tooling_record.md determines tools |

## Unit partition and gaps

DOC-001 pp. 1-11, DOC-002 pp. 1-37, DOC-003 pp. 1-7 and DOC-004 pp. 1-14 are all reusable-backed. No source unit lacks a usable combination of text and, where required for graphic layout, image. Therefore reusable units = 69 and fresh-required units = 0. All 69 must still enter mandatory fresh scientific mapping assignments.

Rendered-image availability is DOC-001 pp. 1-9; DOC-002 pp. 7-17 and 19-30; DOC-003 pp. 1-7; DOC-004 pp. 1-14. Image gaps are DOC-001 pp. 10-11 and DOC-002 pp. 1-6, 18, 31-37. Those 16 pages have usable native/layout text. Targeted direct rendering can close any visual derivative need without OCR. The DOC-004 text p. 2 partial coverage is complemented by DOC-004-p2.png and does not create a source-coverage gap. There are no Office/CSV units requiring conversion or structure extraction.

## Current-run derivatives

The SAP/results mapper produced `preprocessing/sap-results-DOC004-p2.png` and `preprocessing/sap-results-DOC004-p4.png` from DOC-004 physical PDF pp. 2 and 4 using direct Poppler pdftoppm 25.03.0 at 120 dpi on CPU. Complete commands and graphic mapping are retained in extraction/parts/sap_results_evidence.md. These are current-run derivatives, not reused legacy assets.

Main numeric checker derivatives: `preprocessing/numeric-main-layout.txt`, direct `pdftotext -layout -f 1 -l 9` from DOC-001 PDF pp. 1-9, and `preprocessing/numeric-main-source-p7.png`, direct `pdftoppm -f 7 -l 7 -singlefile -r 100 -png` from DOC-001 PDF p. 7. Both use Poppler 25.03.0 on CPU. Exact commands and observations are in checkers/numeric_consistency.md and its numeric inventory. No OCR was used.

Cross-source checker derivatives: `preprocessing/cross-main.txt` (DOC-001 pp. 1-11), `preprocessing/cross-protocol.txt` (DOC-002 pp. 1-37), `preprocessing/cross-sap.txt` (DOC-003 pp. 1-7), and `preprocessing/cross-results.txt` (DOC-004 pp. 1-14). Each was generated with `pdftotext -layout SOURCE OUTPUT`, Poppler 25.03.0, CPU; physical form-feed page boundaries are retained. Exact use is recorded in checkers/cross_source_consistency.md.

Support numeric derivatives: `preprocessing/numeric-support-results-p1-7.txt` and `numeric-support-results-p8-14.txt` (DOC-004 respective page ranges), `numeric-support-sap.txt` (DOC-003 pp. 1-7), `numeric-support-protocol-p14-15.txt` and `numeric-support-protocol-p29-30.txt` (DOC-002 respective ranges), all direct `pdftotext -layout`, Poppler 25.03.0, CPU. `preprocessing/numeric-support-protocol-p29.png` is direct `pdftoppm` 25.03.0, 100 dpi, CPU, DOC-002 p. 29. All exact source/value checks are recorded in checkers/parts/numeric_support.md and its inventory.

Statistical pass-1 derivatives use direct Poppler 25.03.0 on CPU: layout text `preprocessing/st1-main-p4-9.txt` (DOC-001 pp. 4-9), `st1-sap.txt` (DOC-003 pp. 1-7), `st1-protocol-p11-16.txt`, `st1-protocol-p20.txt`, `st1-protocol-p24.txt`, `st1-protocol-p29-30.txt` (DOC-002 named physical page ranges), `st1-results-p6.txt`, and `st1-results-p12-14.txt` (DOC-004 named ranges). CPU PNGs `st1-main-p6.png`, `st1-main-p7.png`, and `st1-protocol-p29.png` use direct pdftoppm for DOC-001 pp. 6/7 and DOC-002 p. 29. Every derivative's source page scope and use is retained in statistics/relationship_inventory.md. No OCR or fallback environment was used.

Initial screener derivatives: direct Poppler pdftotext 25.03.0 layout text on CPU `preprocessing/screen-main.txt` (DOC-001 pp. 1-9), `screen-protocol10-16.txt`, `screen-protocol24.txt`, `screen-protocol29.txt` (DOC-002 named pages), `screen-sap.txt` (DOC-003 pp. 1-7), and `screen-results.txt` (DOC-004 pp. 1-14). Direct Poppler pdftoppm 25.03.0 CPU visual derivatives: `screen-main4.png`, `screen-main5.png`, `screen-main6.png`, `screen-main7.png`; `screen-protocol12.png`, `screen-protocol14.png`, `screen-protocol16.png`, `screen-protocol24.png`, `screen-protocol29.png`; `screen-sap1.png` through `screen-sap6.png`; and `screen-results6.png`, `screen-results12.png`, all under preprocessing and corresponding to the named source IDs/physical pages. Exact use and source rereads are recorded in screening/inclusion_screen.md; no OCR was needed.

Evidence-recheck derivatives use direct Poppler 25.03.0 on CPU. PNGs `preprocessing/recheck-main1.png`, `recheck-main2.png`, `recheck-main3.png`, `recheck-main8.png` through `recheck-main11.png`; `recheck-protocol1.png`, `recheck-protocol10.png`, `recheck-protocol11.png`; and `recheck-results1.png`, `recheck-results3.png`, `recheck-results5.png`, `recheck-results7.png` through `recheck-results11.png`, `recheck-results13.png`, `recheck-results14.png` correspond to the named DOC-001, DOC-002 and DOC-004 physical pages. All use pdftoppm with `-r 110 -singlefile -png`. Layout derivatives `recheck-main-complete.txt` and `recheck-results-complete.txt` cover DOC-001 pp. 1-11 and DOC-004 pp. 1-14; `recheck-sap7.txt` covers DOC-003 p. 7. Full commands, reused current-render provenance and complete absence coverage are retained in verification/evidence_recheck.md. No OCR or fallback was used.
