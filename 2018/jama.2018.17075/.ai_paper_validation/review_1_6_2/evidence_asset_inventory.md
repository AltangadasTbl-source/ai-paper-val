# Reusable evidence-asset inventory

Inventory includes every legacy preprocessing asset: 305 files (eight whole-document native/layout text files, 229 rendered pages, 50 metadata/text locator files, and 18 page-specific text/image derivatives). No standalone OCR files, table/workbook extractions, page manifests, document records, or source-location maps exist elsewhere below the supplied audit area. No legacy scientific conclusions were read. Every listed artifact is hashed in reused_artifact_hashes_before.sha256; sources and assets remain unchanged.

## Fitness, source match and engines

Whole-document native text is byte-identical to fresh direct pdftotext output for all four sources. Layout text is byte-identical for DOC-002, DOC-003 and DOC-004. DOC-001 layout differs only in extracted vertical-axis-label placement on p. 5, remaining usable as a locator with direct-source precedence. Complete rendered-page filenames cover unique source units DOC-001 1–10, DOC-002 1–194, DOC-003 1–24, DOC-004 1. Every file is nonempty. PNG p. 140 of DOC-002 was visually inspected and its bytes exactly match direct pdftoppm output from the current PDF (SHA-256 295ef133dd4e42dcece286b819b09275e3c16be45bd28285687c79b376887be3). All native-derived location numbering is physical PDF order separated by form feeds, not printed page numbers.

Legacy native/layout and metadata text methods: Poppler-style extraction; exact historical tool version is not supplied. Legacy page-image method: PNG rendered page; exact historical engine/version is not supplied. Source-match confirmation engine used this run: pdftotext and pdftoppm 25.03.0, CPU. No new persistent derivative was created. Commands: `pdfinfo SOURCE`; `pdftotext SOURCE -`; `pdftotext -layout SOURCE -`; compare stdout to the named reusable text with `cmp`; `pdftoppm -f 140 -l 140 -singlefile -png joi180132supp1_prod.pdf` piped to sha256sum. Output: native comparisons all identical, layout comparisons identical except DOC-001 placement described above, p. 140 PNG hash identical. File signature confirmed PNG 1240 × 1754 RGB for the inspected A4 page. Hash engine: sha256sum.

DOC-002 native/layout text is PARTIAL: pp. 140–162, 183–185 and 187 have no native text; pp. 104, 105 and 127 contain only headers. These 30 pages have USABLE rendered-page evidence and must receive visual mapping. No scientific unit is uncovered; fresh-required count is zero because the usable reusable image union is complete. Text-bearing figure, diagram and table pages still receive visual confirmation where needed. Every usable artifact remains a locator/transcription aid; source PDFs are final authority.

Metadata and page-specific text/image files duplicate full-document locators or the complete rendered-page collection and add no unique unit coverage. The hidden metadata `.txt` is a compact DOC-004 p. 1 locator, classified PARTIAL rather than a full-page transcript. DUPLICATE classification means not counted twice; these assets are preserved and hashed. No STALE or UNREADABLE asset was found by identity, nonempty-content and format checks. Historical engine/version uncertainty is a derivative-provenance limitation, not an uncovered source unit.

## Artifact-by-artifact scope

Rows give package-relative paths. The full-document text rows cover all listed page numbers subject to the DOC-002 gap rule above. A rendered-page filename DOC-XXX-NNN.png covers exactly physical page NNN of DOC-XXX. No page is inferred from an old candidate location.

| Asset path | Source unit(s) | Kind / engine | Fitness | Coverage or restriction |
|---|---|---|---|---|
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-001.txt | DOC-001 PDF pp. 1–10 | Layout text; legacy Poppler-style extraction | USABLE | Source-matched page-delimited locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-002.txt | DOC-002 PDF pp. 1–194 | Layout text; legacy Poppler-style extraction | PARTIAL | Text gaps covered by rendered pages; see exact gap list |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-003.txt | DOC-003 PDF pp. 1–24 | Layout text; legacy Poppler-style extraction | USABLE | Source-matched page-delimited locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-004.txt | DOC-004 PDF pp. 1–1 | Layout text; legacy Poppler-style extraction | USABLE | Source-matched page-delimited locator |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/.txt | DOC-004 PDF p. 1 | Legacy source-derived text; historical engine not recorded | PARTIAL | Truncated source locator; canonical text covers full page |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-001-p1.txt | DOC-001 PDF p. 1 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-001-p4.txt | DOC-001 PDF p. 4 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-001-p7.txt | DOC-001 PDF p. 7 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-001-p8.txt | DOC-001 PDF p. 8 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-001_pdfinfo.txt | DOC-001 document metadata | Legacy source-derived text; historical engine not recorded | DUPLICATE | Metadata only; page counts confirmed directly |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p139.txt | DOC-002 PDF p. 139 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p179.txt | DOC-002 PDF p. 179 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p189.txt | DOC-002 PDF p. 189 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p19.txt | DOC-002 PDF p. 19 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p190.txt | DOC-002 PDF p. 190 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p191.txt | DOC-002 PDF p. 191 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p192.txt | DOC-002 PDF p. 192 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p193.txt | DOC-002 PDF p. 193 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p194.txt | DOC-002 PDF p. 194 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p28.txt | DOC-002 PDF p. 28 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p71.txt | DOC-002 PDF p. 71 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p73.txt | DOC-002 PDF p. 73 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p82.txt | DOC-002 PDF p. 82 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002-p83.txt | DOC-002 PDF p. 83 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-002_pdfinfo.txt | DOC-002 document metadata | Legacy source-derived text; historical engine not recorded | DUPLICATE | Metadata only; page counts confirmed directly |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p1.txt | DOC-003 PDF p. 1 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p10.txt | DOC-003 PDF p. 10 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p11.txt | DOC-003 PDF p. 11 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p12.txt | DOC-003 PDF p. 12 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p13.txt | DOC-003 PDF p. 13 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p14.txt | DOC-003 PDF p. 14 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p15.txt | DOC-003 PDF p. 15 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p16.txt | DOC-003 PDF p. 16 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p17.txt | DOC-003 PDF p. 17 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p18.txt | DOC-003 PDF p. 18 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p19.txt | DOC-003 PDF p. 19 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p2.txt | DOC-003 PDF p. 2 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p20.txt | DOC-003 PDF p. 20 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p21.txt | DOC-003 PDF p. 21 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p22.txt | DOC-003 PDF p. 22 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p23.txt | DOC-003 PDF p. 23 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p24.txt | DOC-003 PDF p. 24 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p3.txt | DOC-003 PDF p. 3 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p4.txt | DOC-003 PDF p. 4 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p5.txt | DOC-003 PDF p. 5 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p6.txt | DOC-003 PDF p. 6 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p7.txt | DOC-003 PDF p. 7 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p8.txt | DOC-003 PDF p. 8 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003-p9.txt | DOC-003 PDF p. 9 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-003_pdfinfo.txt | DOC-003 document metadata | Legacy source-derived text; historical engine not recorded | DUPLICATE | Metadata only; page counts confirmed directly |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-004-p1.txt | DOC-004 PDF p. 1 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/DOC-004_pdfinfo.txt | DOC-004 document metadata | Legacy source-derived text; historical engine not recorded | DUPLICATE | Metadata only; page counts confirmed directly |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-001.txt | DOC-001 PDF pp. 1–10 | Native text; legacy Poppler-style extraction | USABLE | Source-matched page-delimited locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-002.txt | DOC-002 PDF pp. 1–194 | Native text; legacy Poppler-style extraction | PARTIAL | Text gaps covered by rendered pages; see exact gap list |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-003.txt | DOC-003 PDF pp. 1–24 | Native text; legacy Poppler-style extraction | USABLE | Source-matched page-delimited locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-004.txt | DOC-004 PDF pp. 1–1 | Native text; legacy Poppler-style extraction | USABLE | Source-matched page-delimited locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-01.png | DOC-001 PDF p. 1 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-02.png | DOC-001 PDF p. 2 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-03.png | DOC-001 PDF p. 3 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-04.png | DOC-001 PDF p. 4 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-05.png | DOC-001 PDF p. 5 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-06.png | DOC-001 PDF p. 6 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-07.png | DOC-001 PDF p. 7 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-08.png | DOC-001 PDF p. 8 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-09.png | DOC-001 PDF p. 9 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-10.png | DOC-001 PDF p. 10 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-001.png | DOC-002 PDF p. 1 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-002.png | DOC-002 PDF p. 2 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-003.png | DOC-002 PDF p. 3 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-004.png | DOC-002 PDF p. 4 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-005.png | DOC-002 PDF p. 5 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-006.png | DOC-002 PDF p. 6 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-007.png | DOC-002 PDF p. 7 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-008.png | DOC-002 PDF p. 8 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-009.png | DOC-002 PDF p. 9 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-010.png | DOC-002 PDF p. 10 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-011.png | DOC-002 PDF p. 11 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-012.png | DOC-002 PDF p. 12 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-013.png | DOC-002 PDF p. 13 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-014.png | DOC-002 PDF p. 14 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-015.png | DOC-002 PDF p. 15 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-016.png | DOC-002 PDF p. 16 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-017.png | DOC-002 PDF p. 17 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-018.png | DOC-002 PDF p. 18 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-019.png | DOC-002 PDF p. 19 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-020.png | DOC-002 PDF p. 20 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-021.png | DOC-002 PDF p. 21 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-022.png | DOC-002 PDF p. 22 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-023.png | DOC-002 PDF p. 23 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-024.png | DOC-002 PDF p. 24 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-025.png | DOC-002 PDF p. 25 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-026.png | DOC-002 PDF p. 26 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-027.png | DOC-002 PDF p. 27 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-028.png | DOC-002 PDF p. 28 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-029.png | DOC-002 PDF p. 29 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-030.png | DOC-002 PDF p. 30 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-031.png | DOC-002 PDF p. 31 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-032.png | DOC-002 PDF p. 32 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-033.png | DOC-002 PDF p. 33 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-034.png | DOC-002 PDF p. 34 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-035.png | DOC-002 PDF p. 35 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-036.png | DOC-002 PDF p. 36 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-037.png | DOC-002 PDF p. 37 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-038.png | DOC-002 PDF p. 38 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-039.png | DOC-002 PDF p. 39 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-040.png | DOC-002 PDF p. 40 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-041.png | DOC-002 PDF p. 41 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-042.png | DOC-002 PDF p. 42 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-043.png | DOC-002 PDF p. 43 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-044.png | DOC-002 PDF p. 44 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-045.png | DOC-002 PDF p. 45 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-046.png | DOC-002 PDF p. 46 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-047.png | DOC-002 PDF p. 47 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-048.png | DOC-002 PDF p. 48 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-049.png | DOC-002 PDF p. 49 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-050.png | DOC-002 PDF p. 50 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-051.png | DOC-002 PDF p. 51 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-052.png | DOC-002 PDF p. 52 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-053.png | DOC-002 PDF p. 53 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-054.png | DOC-002 PDF p. 54 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-055.png | DOC-002 PDF p. 55 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-056.png | DOC-002 PDF p. 56 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-057.png | DOC-002 PDF p. 57 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-058.png | DOC-002 PDF p. 58 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-059.png | DOC-002 PDF p. 59 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-060.png | DOC-002 PDF p. 60 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-061.png | DOC-002 PDF p. 61 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-062.png | DOC-002 PDF p. 62 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-063.png | DOC-002 PDF p. 63 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-064.png | DOC-002 PDF p. 64 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-065.png | DOC-002 PDF p. 65 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-066.png | DOC-002 PDF p. 66 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-067.png | DOC-002 PDF p. 67 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-068.png | DOC-002 PDF p. 68 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-069.png | DOC-002 PDF p. 69 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-070.png | DOC-002 PDF p. 70 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-071.png | DOC-002 PDF p. 71 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-072.png | DOC-002 PDF p. 72 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-073.png | DOC-002 PDF p. 73 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-074.png | DOC-002 PDF p. 74 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-075.png | DOC-002 PDF p. 75 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-076.png | DOC-002 PDF p. 76 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-077.png | DOC-002 PDF p. 77 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-078.png | DOC-002 PDF p. 78 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-079.png | DOC-002 PDF p. 79 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-080.png | DOC-002 PDF p. 80 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-081.png | DOC-002 PDF p. 81 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-082.png | DOC-002 PDF p. 82 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-083.png | DOC-002 PDF p. 83 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-084.png | DOC-002 PDF p. 84 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-085.png | DOC-002 PDF p. 85 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-086.png | DOC-002 PDF p. 86 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-087.png | DOC-002 PDF p. 87 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-088.png | DOC-002 PDF p. 88 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-089.png | DOC-002 PDF p. 89 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-090.png | DOC-002 PDF p. 90 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-091.png | DOC-002 PDF p. 91 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-092.png | DOC-002 PDF p. 92 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-093.png | DOC-002 PDF p. 93 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-094.png | DOC-002 PDF p. 94 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-095.png | DOC-002 PDF p. 95 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-096.png | DOC-002 PDF p. 96 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-097.png | DOC-002 PDF p. 97 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-098.png | DOC-002 PDF p. 98 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-099.png | DOC-002 PDF p. 99 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-100.png | DOC-002 PDF p. 100 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-101.png | DOC-002 PDF p. 101 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-102.png | DOC-002 PDF p. 102 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-103.png | DOC-002 PDF p. 103 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-104.png | DOC-002 PDF p. 104 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-105.png | DOC-002 PDF p. 105 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-106.png | DOC-002 PDF p. 106 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-107.png | DOC-002 PDF p. 107 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-108.png | DOC-002 PDF p. 108 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-109.png | DOC-002 PDF p. 109 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-110.png | DOC-002 PDF p. 110 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-111.png | DOC-002 PDF p. 111 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-112.png | DOC-002 PDF p. 112 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-113.png | DOC-002 PDF p. 113 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-114.png | DOC-002 PDF p. 114 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-115.png | DOC-002 PDF p. 115 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-116.png | DOC-002 PDF p. 116 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-117.png | DOC-002 PDF p. 117 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-118.png | DOC-002 PDF p. 118 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-119.png | DOC-002 PDF p. 119 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-120.png | DOC-002 PDF p. 120 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-121.png | DOC-002 PDF p. 121 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-122.png | DOC-002 PDF p. 122 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-123.png | DOC-002 PDF p. 123 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-124.png | DOC-002 PDF p. 124 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-125.png | DOC-002 PDF p. 125 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-126.png | DOC-002 PDF p. 126 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-127.png | DOC-002 PDF p. 127 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-128.png | DOC-002 PDF p. 128 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-129.png | DOC-002 PDF p. 129 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-130.png | DOC-002 PDF p. 130 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-131.png | DOC-002 PDF p. 131 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-132.png | DOC-002 PDF p. 132 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-133.png | DOC-002 PDF p. 133 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-134.png | DOC-002 PDF p. 134 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-135.png | DOC-002 PDF p. 135 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-136.png | DOC-002 PDF p. 136 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-137.png | DOC-002 PDF p. 137 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-138.png | DOC-002 PDF p. 138 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-139.png | DOC-002 PDF p. 139 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-140.png | DOC-002 PDF p. 140 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-141.png | DOC-002 PDF p. 141 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-142.png | DOC-002 PDF p. 142 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-143.png | DOC-002 PDF p. 143 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-144.png | DOC-002 PDF p. 144 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-145.png | DOC-002 PDF p. 145 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-146.png | DOC-002 PDF p. 146 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-147.png | DOC-002 PDF p. 147 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-148.png | DOC-002 PDF p. 148 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-149.png | DOC-002 PDF p. 149 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-150.png | DOC-002 PDF p. 150 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-151.png | DOC-002 PDF p. 151 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-152.png | DOC-002 PDF p. 152 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-153.png | DOC-002 PDF p. 153 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-154.png | DOC-002 PDF p. 154 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-155.png | DOC-002 PDF p. 155 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-156.png | DOC-002 PDF p. 156 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-157.png | DOC-002 PDF p. 157 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-158.png | DOC-002 PDF p. 158 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-159.png | DOC-002 PDF p. 159 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-160.png | DOC-002 PDF p. 160 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-161.png | DOC-002 PDF p. 161 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-162.png | DOC-002 PDF p. 162 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-163.png | DOC-002 PDF p. 163 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-164.png | DOC-002 PDF p. 164 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-165.png | DOC-002 PDF p. 165 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-166.png | DOC-002 PDF p. 166 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-167.png | DOC-002 PDF p. 167 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-168.png | DOC-002 PDF p. 168 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-169.png | DOC-002 PDF p. 169 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-170.png | DOC-002 PDF p. 170 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-171.png | DOC-002 PDF p. 171 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-172.png | DOC-002 PDF p. 172 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-173.png | DOC-002 PDF p. 173 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-174.png | DOC-002 PDF p. 174 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-175.png | DOC-002 PDF p. 175 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-176.png | DOC-002 PDF p. 176 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-177.png | DOC-002 PDF p. 177 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-178.png | DOC-002 PDF p. 178 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-179.png | DOC-002 PDF p. 179 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-180.png | DOC-002 PDF p. 180 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-181.png | DOC-002 PDF p. 181 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-182.png | DOC-002 PDF p. 182 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-183.png | DOC-002 PDF p. 183 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-184.png | DOC-002 PDF p. 184 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-185.png | DOC-002 PDF p. 185 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-186.png | DOC-002 PDF p. 186 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-187.png | DOC-002 PDF p. 187 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-188.png | DOC-002 PDF p. 188 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-189.png | DOC-002 PDF p. 189 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-190.png | DOC-002 PDF p. 190 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-191.png | DOC-002 PDF p. 191 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-192.png | DOC-002 PDF p. 192 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-193.png | DOC-002 PDF p. 193 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-194.png | DOC-002 PDF p. 194 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-01.png | DOC-003 PDF p. 1 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-02.png | DOC-003 PDF p. 2 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-03.png | DOC-003 PDF p. 3 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-04.png | DOC-003 PDF p. 4 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-05.png | DOC-003 PDF p. 5 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-06.png | DOC-003 PDF p. 6 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-07.png | DOC-003 PDF p. 7 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-08.png | DOC-003 PDF p. 8 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-09.png | DOC-003 PDF p. 9 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-10.png | DOC-003 PDF p. 10 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-11.png | DOC-003 PDF p. 11 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-12.png | DOC-003 PDF p. 12 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-13.png | DOC-003 PDF p. 13 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-14.png | DOC-003 PDF p. 14 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-15.png | DOC-003 PDF p. 15 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-16.png | DOC-003 PDF p. 16 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-17.png | DOC-003 PDF p. 17 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-18.png | DOC-003 PDF p. 18 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-19.png | DOC-003 PDF p. 19 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-20.png | DOC-003 PDF p. 20 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-21.png | DOC-003 PDF p. 21 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-22.png | DOC-003 PDF p. 22 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-23.png | DOC-003 PDF p. 23 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-24.png | DOC-003 PDF p. 24 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-004-1.png | DOC-004 PDF p. 1 | PNG rendered page; historical engine not recorded | USABLE | Unique reusable page image |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-p1.png | DOC-001 PDF p. 1 | PNG rendered page; historical engine not recorded | DUPLICATE | Overlaps complete rendered-page set |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-p1.txt | DOC-001 PDF p. 1 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-p3.png | DOC-001 PDF p. 3 | PNG rendered page; historical engine not recorded | DUPLICATE | Overlaps complete rendered-page set |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-p3.txt | DOC-001 PDF p. 3 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-p4.png | DOC-001 PDF p. 4 | PNG rendered page; historical engine not recorded | DUPLICATE | Overlaps complete rendered-page set |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-p4.txt | DOC-001 PDF p. 4 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-p5.png | DOC-001 PDF p. 5 | PNG rendered page; historical engine not recorded | DUPLICATE | Overlaps complete rendered-page set |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-p5.txt | DOC-001 PDF p. 5 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-p7.png | DOC-001 PDF p. 7 | PNG rendered page; historical engine not recorded | DUPLICATE | Overlaps complete rendered-page set |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/main-p7.txt | DOC-001 PDF p. 7 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/plan-p101.png | DOC-002 PDF p. 101 | PNG rendered page; historical engine not recorded | DUPLICATE | Overlaps complete rendered-page set |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/plan-p101.txt | DOC-002 PDF p. 101 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/plan-p77.png | DOC-002 PDF p. 77 | PNG rendered page; historical engine not recorded | DUPLICATE | Overlaps complete rendered-page set |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/plan-p77.txt | DOC-002 PDF p. 77 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-p10.png | DOC-003 PDF p. 10 | PNG rendered page; historical engine not recorded | DUPLICATE | Overlaps complete rendered-page set |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-p10.txt | DOC-003 PDF p. 10 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-p11.png | DOC-003 PDF p. 11 | PNG rendered page; historical engine not recorded | DUPLICATE | Overlaps complete rendered-page set |
| .ai_paper_validation/review_1_6_1/preprocessing/recheck/results-p11.txt | DOC-003 PDF p. 11 | Legacy source-derived text; historical engine not recorded | DUPLICATE | Overlaps canonical full-document text |
| .ai_paper_validation/review_1_6_1/preprocessing/screening/main-p5.png | DOC-001 PDF p. 5 | PNG rendered page; historical engine not recorded | DUPLICATE | Overlaps complete rendered-page set |
| .ai_paper_validation/review_1_6_1/preprocessing/screening/results-p11.png | DOC-003 PDF p. 11 | PNG rendered page; historical engine not recorded | DUPLICATE | Overlaps complete rendered-page set |

## Current-run direct-source confirmation derivative

preprocessing/stat-monitoring-source-192.png was produced from DOC-002 physical p192 by direct Poppler pdftoppm25.03.0 on CPU for statistical monitoring confirmation. SHA-256 896d75c181fa92bdf2e073e48525233019cfc060e87dffdea34e93aa21e8b6fa. This new confirmation asset is not included in the reused-artifact hash set and does not change the initial fresh-required unit count. Exact command and device are documented in the monitoring checker part.
