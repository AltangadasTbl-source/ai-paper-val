# Reused Evidence-Asset Inventory

Scope: every existing source-linked OCR text, native or layout text, table/workbook extraction, rendered page, page manifest, document record, and source-location map below the pre-existing audit area. Legacy candidate, queue, verifier, critic, endetail, quality-decision, and final-report content was not read and is not an inventory input. No OCR text, layout-text asset, table/workbook extraction, Office source, CSV source, or separate page-manifest file exists.

Fitness criteria: `USABLE` means the asset is source-matched and has exact stable locations suitable for reuse as a locator or transcription aid; `DUPLICATE` means it adds no unique coverage and is not used to determine coverage. Current direct-source hashes match the recorded source hashes in the source-location map. All `USABLE` assets remain derivative aids; direct PDFs remain authoritative for downstream confirmation.

| Asset path | Asset type and method | Exact source locations | Coverage and fitness | Gap or downstream assignment |
|---|---|---|---|---|
| .ai_paper_validation/package_manifest.md | Source-location map; package inventory and source hashes | DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-103; DOC-003 PDF pp. 1-26; DOC-004 PDF pp. 1-3; DOC-005 PDF p. 1 | USABLE; maps all five direct sources and hashes match the current baseline | No gap; supports all mapper source assignments |
| .ai_paper_validation/preprocessor_record.md | Extraction record; legacy native-text preprocessing metadata | DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-103; DOC-003 PDF pp. 1-26; DOC-004 PDF pp. 1-3; DOC-005 PDF p. 1 | USABLE; documents the five complete page-delimited native-text derivatives | No gap; method metadata only |
| .ai_paper_validation/documents/DOC-001.md | Document record and source-location map | DOC-001 PDF pp. 1-11 | USABLE; identifies source, role, page count, native text, and rendered-page location | No gap; main mapper assignment DOC-001 pp. 1-11 |
| .ai_paper_validation/documents/DOC-002.md | Document record and source-location map | DOC-002 PDF pp. 1-103 | USABLE; identifies source, role, page count, and native-text location | No gap; support mapper assignment DOC-002 pp. 1-103 |
| .ai_paper_validation/documents/DOC-003.md | Document record and source-location map | DOC-003 PDF pp. 1-26 | USABLE; identifies source, role, page count, native text, and rendered-page location | No gap; support mapper assignment DOC-003 pp. 1-26 |
| .ai_paper_validation/documents/DOC-004.md | Document record and source-location map | DOC-004 PDF pp. 1-3 | USABLE; identifies source, role, page count, and native-text location | No gap; support mapper assignment DOC-004 pp. 1-3 |
| .ai_paper_validation/documents/DOC-005.md | Document record and source-location map | DOC-005 PDF p. 1 | USABLE; identifies source, role, page count, and native-text location | No gap; support mapper assignment DOC-005 p. 1 |
| .ai_paper_validation/preprocessed/DOC-001.txt | Native text; page-delimited legacy extraction with `===== SOURCE PAGE N =====` markers | DOC-001 PDF pp. 1-11 | USABLE; 11 markers for all 11 source pages | No gap; all 11 units reusable |
| .ai_paper_validation/preprocessed/DOC-002.txt | Native text; page-delimited legacy extraction with `===== SOURCE PAGE N =====` markers | DOC-002 PDF pp. 1-103 | USABLE; 103 markers for all 103 source pages | No gap; all 103 units reusable |
| .ai_paper_validation/preprocessed/DOC-003.txt | Native text; page-delimited legacy extraction with `===== SOURCE PAGE N =====` markers | DOC-003 PDF pp. 1-26 | USABLE; 26 markers for all 26 source pages | No gap; all 26 units reusable |
| .ai_paper_validation/preprocessed/DOC-004.txt | Native text; page-delimited legacy extraction with `===== SOURCE PAGE N =====` markers | DOC-004 PDF pp. 1-3 | USABLE; 3 markers for all 3 source pages | No gap; all 3 units reusable |
| .ai_paper_validation/preprocessed/DOC-005.txt | Native text; page-delimited legacy extraction with `===== SOURCE PAGE N =====` markers | DOC-005 PDF p. 1 | USABLE; 1 marker for the one source page | No gap; the unit is reusable |
| .ai_paper_validation/renders/DOC-001-contact-sheet.png | Rendered composite contact sheet | DOC-001 PDF pp. 1-11 | DUPLICATE; composite duplicates the individual page renders and native text | Not used for unit coverage; no fresh assignment because all pages are otherwise USABLE |
| .ai_paper_validation/renders/DOC-001-page-01.png | Rendered source page | DOC-001 PDF p. 1 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-001-page-02.png | Rendered source page | DOC-001 PDF p. 2 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-001-page-03.png | Rendered source page | DOC-001 PDF p. 3 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-001-page-04.png | Rendered source page | DOC-001 PDF p. 4 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-001-page-05.png | Rendered source page | DOC-001 PDF p. 5 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-001-page-06.png | Rendered source page | DOC-001 PDF p. 6 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-001-page-07.png | Rendered source page | DOC-001 PDF p. 7 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-001-page-08.png | Rendered source page | DOC-001 PDF p. 8 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-001-page-09.png | Rendered source page | DOC-001 PDF p. 9 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-001-page-10.png | Rendered source page | DOC-001 PDF p. 10 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-001-page-11.png | Rendered source page | DOC-001 PDF p. 11 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-contact-sheet.png | Rendered composite contact sheet | DOC-003 PDF pp. 13-25 | DUPLICATE; composite duplicates the individual page renders and native text | Not used for unit coverage; no fresh assignment because all pages are otherwise USABLE |
| .ai_paper_validation/renders/DOC-003-page-13.png | Rendered source page | DOC-003 PDF p. 13 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-14.png | Rendered source page | DOC-003 PDF p. 14 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-15.png | Rendered source page | DOC-003 PDF p. 15 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-16.png | Rendered source page | DOC-003 PDF p. 16 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-17.png | Rendered source page | DOC-003 PDF p. 17 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-18.png | Rendered source page | DOC-003 PDF p. 18 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-19.png | Rendered source page | DOC-003 PDF p. 19 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-20.png | Rendered source page | DOC-003 PDF p. 20 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-21.png | Rendered source page | DOC-003 PDF p. 21 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-22.png | Rendered source page | DOC-003 PDF p. 22 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-23.png | Rendered source page | DOC-003 PDF p. 23 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-24.png | Rendered source page | DOC-003 PDF p. 24 | USABLE; visual confirmation aid | No gap; page reusable |
| .ai_paper_validation/renders/DOC-003-page-25.png | Rendered source page | DOC-003 PDF p. 25 | USABLE; visual confirmation aid | No gap; page reusable |

Asset totals: 38 reused artifacts inventoried and hashed: 36 USABLE, 0 PARTIAL, 0 STALE, 2 DUPLICATE, and 0 UNREADABLE. Coverage determinant assets are the five complete native-text files; all 144 direct PDF_PAGE units are reusable. Renders provide 24 individual source-page visual aids: DOC-001 pp. 1-11 and DOC-003 pp. 13-25. The absent per-page render derivatives for DOC-002, DOC-004, DOC-005, and DOC-003 pp. 1-12 are format gaps only; complete USABLE native text covers those locations, so fresh-required units remain 0.
