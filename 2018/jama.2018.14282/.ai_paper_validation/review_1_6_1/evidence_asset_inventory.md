# Reusable Evidence Asset Inventory

All 396 eligible artifacts are located under review_1_5_2/preprocessing and are preserved unchanged. The audit tree contains no other existing artifact outside this preprocessing directory and the current run. Inventory and reuse include 144 page-native files, 144 page-layout files, 8 whole-document native/layout files, 89 PNG renders, 4 PDF-information files, 4 page previews, 2 page-character/usability metadata files, and 1 page-unit register. No OCR, table extraction, workbook extraction, Office conversion, or additional document-record assets were found. Every artifact below is hashed in reused_artifact_hashes_before.sha256 with its full package-relative path.

## Identity, fitness and engines

Direct commands: pdfinfo SOURCE; sha256sum -- SOURCE; pdftotext -f N -l N SOURCE -; pdftotext -layout -f N -l N SOURCE -; cmp against the exact page derivative; file on PNG files. Current direct engine: Poppler 25.03.0. Original text engine: Poppler pdftotext, original version unavailable. Prior PNG renderer: Poppler inferred, original version unavailable. No fallback, new OCR, GPU, or Office extraction was invoked. Exact current-source comparisons: native DOC-001 9/9, DOC-002 128/129 byte-matched plus p.11 whitespace-normalized matched, DOC-003 5/5, DOC-004 1/1; layout DOC-001 9/9, DOC-002 128/129 byte-matched plus p.11 whitespace-normalized matched, DOC-003 2/5, DOC-004 1/1. Layout DOC-003 pp.3-5 retains values but differs in figure label placement across extraction versions; classify these locators PARTIAL and use native plus PNG/PDF for quantity-to-label interpretation. These variations do not establish source changes. Whole-document aggregates overlap page derivatives and are classified DUPLICATE; their variations are the same page differences.

All 89 images are valid nonempty PNG files. Their filenames and page-unit register establish exact source/page correspondence; images are locator aids and do not substitute for final direct-source confirmation. Page previews are truncated and PARTIAL. PDF-information and page-count metadata are usable identity/location aids, never scientific coverage by themselves. The page-unit register is reused only for asset/page locations, with no inherited scientific relevance decisions. All 144 source pages have usable native text. No stale or unreadable asset was found; no unit is fresh-required.

## Exact Artifact Register

Paths are package-relative; DOC-001 maps to jama_azoulay_2018_oi_180109.pdf, DOC-002 to joi180109supp1_prod.pdf, DOC-003 to joi180109supp2_prod.pdf, DOC-004 to joi180109supp3_prod.pdf.

| Artifact path | Exact source units | Fitness | Engine or method | Reuse purpose |
|---|---|---|---|---|
| .ai_paper_validation/review_1_5_2/preprocessing/DOC-001_page_text_preview.txt | DOC-001 PDF pp.1-9 | PARTIAL | Truncated page-text preview | Page navigation only |
| .ai_paper_validation/review_1_5_2/preprocessing/DOC-002_page_text_preview.txt | DOC-002 PDF pp.1-129 | PARTIAL | Truncated page-text preview | Page navigation only |
| .ai_paper_validation/review_1_5_2/preprocessing/DOC-003_page_text_preview.txt | DOC-003 PDF pp.1-5 | PARTIAL | Truncated page-text preview | Page navigation only |
| .ai_paper_validation/review_1_5_2/preprocessing/DOC-004_page_text_preview.txt | DOC-004 PDF p.1 | PARTIAL | Truncated page-text preview | Page navigation only |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-001.txt | DOC-001 PDF pp.1-9 | DUPLICATE | Poppler pdftotext (original version unavailable) | Whole-document extraction overlaps exact page files |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-002.txt | DOC-002 PDF pp.1-129 | DUPLICATE | Poppler pdftotext (original version unavailable) | Whole-document extraction overlaps exact page files |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-003.txt | DOC-003 PDF pp.1-5 | DUPLICATE | Poppler pdftotext (original version unavailable) | Whole-document extraction overlaps exact page files |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-004.txt | DOC-004 PDF p.1 | DUPLICATE | Poppler pdftotext (original version unavailable) | Whole-document extraction overlaps exact page files |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-001/p001.txt | DOC-001 PDF p.1 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-001/p002.txt | DOC-001 PDF p.2 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-001/p003.txt | DOC-001 PDF p.3 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-001/p004.txt | DOC-001 PDF p.4 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-001/p005.txt | DOC-001 PDF p.5 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-001/p006.txt | DOC-001 PDF p.6 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-001/p007.txt | DOC-001 PDF p.7 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-001/p008.txt | DOC-001 PDF p.8 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-001/p009.txt | DOC-001 PDF p.9 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p001.txt | DOC-002 PDF p.1 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p002.txt | DOC-002 PDF p.2 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p003.txt | DOC-002 PDF p.3 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p004.txt | DOC-002 PDF p.4 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p005.txt | DOC-002 PDF p.5 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p006.txt | DOC-002 PDF p.6 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p007.txt | DOC-002 PDF p.7 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p008.txt | DOC-002 PDF p.8 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p009.txt | DOC-002 PDF p.9 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p010.txt | DOC-002 PDF p.10 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p011.txt | DOC-002 PDF p.11 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p012.txt | DOC-002 PDF p.12 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p013.txt | DOC-002 PDF p.13 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p014.txt | DOC-002 PDF p.14 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p015.txt | DOC-002 PDF p.15 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p016.txt | DOC-002 PDF p.16 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p017.txt | DOC-002 PDF p.17 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p018.txt | DOC-002 PDF p.18 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p019.txt | DOC-002 PDF p.19 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p020.txt | DOC-002 PDF p.20 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p021.txt | DOC-002 PDF p.21 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p022.txt | DOC-002 PDF p.22 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p023.txt | DOC-002 PDF p.23 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p024.txt | DOC-002 PDF p.24 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p025.txt | DOC-002 PDF p.25 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p026.txt | DOC-002 PDF p.26 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p027.txt | DOC-002 PDF p.27 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p028.txt | DOC-002 PDF p.28 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p029.txt | DOC-002 PDF p.29 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p030.txt | DOC-002 PDF p.30 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p031.txt | DOC-002 PDF p.31 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p032.txt | DOC-002 PDF p.32 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p033.txt | DOC-002 PDF p.33 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p034.txt | DOC-002 PDF p.34 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p035.txt | DOC-002 PDF p.35 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p036.txt | DOC-002 PDF p.36 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p037.txt | DOC-002 PDF p.37 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p038.txt | DOC-002 PDF p.38 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p039.txt | DOC-002 PDF p.39 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p040.txt | DOC-002 PDF p.40 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p041.txt | DOC-002 PDF p.41 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p042.txt | DOC-002 PDF p.42 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p043.txt | DOC-002 PDF p.43 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p044.txt | DOC-002 PDF p.44 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p045.txt | DOC-002 PDF p.45 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p046.txt | DOC-002 PDF p.46 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p047.txt | DOC-002 PDF p.47 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p048.txt | DOC-002 PDF p.48 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p049.txt | DOC-002 PDF p.49 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p050.txt | DOC-002 PDF p.50 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p051.txt | DOC-002 PDF p.51 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p052.txt | DOC-002 PDF p.52 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p053.txt | DOC-002 PDF p.53 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p054.txt | DOC-002 PDF p.54 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p055.txt | DOC-002 PDF p.55 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p056.txt | DOC-002 PDF p.56 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p057.txt | DOC-002 PDF p.57 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p058.txt | DOC-002 PDF p.58 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p059.txt | DOC-002 PDF p.59 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p060.txt | DOC-002 PDF p.60 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p061.txt | DOC-002 PDF p.61 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p062.txt | DOC-002 PDF p.62 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p063.txt | DOC-002 PDF p.63 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p064.txt | DOC-002 PDF p.64 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p065.txt | DOC-002 PDF p.65 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p066.txt | DOC-002 PDF p.66 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p067.txt | DOC-002 PDF p.67 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p068.txt | DOC-002 PDF p.68 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p069.txt | DOC-002 PDF p.69 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p070.txt | DOC-002 PDF p.70 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p071.txt | DOC-002 PDF p.71 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p072.txt | DOC-002 PDF p.72 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p073.txt | DOC-002 PDF p.73 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p074.txt | DOC-002 PDF p.74 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p075.txt | DOC-002 PDF p.75 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p076.txt | DOC-002 PDF p.76 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p077.txt | DOC-002 PDF p.77 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p078.txt | DOC-002 PDF p.78 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p079.txt | DOC-002 PDF p.79 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p080.txt | DOC-002 PDF p.80 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p081.txt | DOC-002 PDF p.81 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p082.txt | DOC-002 PDF p.82 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p083.txt | DOC-002 PDF p.83 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p084.txt | DOC-002 PDF p.84 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p085.txt | DOC-002 PDF p.85 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p086.txt | DOC-002 PDF p.86 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p087.txt | DOC-002 PDF p.87 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p088.txt | DOC-002 PDF p.88 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p089.txt | DOC-002 PDF p.89 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p090.txt | DOC-002 PDF p.90 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p091.txt | DOC-002 PDF p.91 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p092.txt | DOC-002 PDF p.92 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p093.txt | DOC-002 PDF p.93 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p094.txt | DOC-002 PDF p.94 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p095.txt | DOC-002 PDF p.95 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p096.txt | DOC-002 PDF p.96 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p097.txt | DOC-002 PDF p.97 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p098.txt | DOC-002 PDF p.98 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p099.txt | DOC-002 PDF p.99 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p100.txt | DOC-002 PDF p.100 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p101.txt | DOC-002 PDF p.101 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p102.txt | DOC-002 PDF p.102 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p103.txt | DOC-002 PDF p.103 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p104.txt | DOC-002 PDF p.104 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p105.txt | DOC-002 PDF p.105 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p106.txt | DOC-002 PDF p.106 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p107.txt | DOC-002 PDF p.107 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p108.txt | DOC-002 PDF p.108 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p109.txt | DOC-002 PDF p.109 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p110.txt | DOC-002 PDF p.110 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p111.txt | DOC-002 PDF p.111 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p112.txt | DOC-002 PDF p.112 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p113.txt | DOC-002 PDF p.113 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p114.txt | DOC-002 PDF p.114 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p115.txt | DOC-002 PDF p.115 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p116.txt | DOC-002 PDF p.116 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p117.txt | DOC-002 PDF p.117 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p118.txt | DOC-002 PDF p.118 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p119.txt | DOC-002 PDF p.119 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p120.txt | DOC-002 PDF p.120 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p121.txt | DOC-002 PDF p.121 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p122.txt | DOC-002 PDF p.122 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p123.txt | DOC-002 PDF p.123 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p124.txt | DOC-002 PDF p.124 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p125.txt | DOC-002 PDF p.125 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p126.txt | DOC-002 PDF p.126 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p127.txt | DOC-002 PDF p.127 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p128.txt | DOC-002 PDF p.128 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/p129.txt | DOC-002 PDF p.129 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-003/p001.txt | DOC-003 PDF p.1 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-003/p002.txt | DOC-003 PDF p.2 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-003/p003.txt | DOC-003 PDF p.3 | PARTIAL | Poppler pdftotext (original version unavailable) | Figure tokens retained; confirm label pairing in source/PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-003/p004.txt | DOC-003 PDF p.4 | PARTIAL | Poppler pdftotext (original version unavailable) | Figure tokens retained; confirm label pairing in source/PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-003/p005.txt | DOC-003 PDF p.5 | PARTIAL | Poppler pdftotext (original version unavailable) | Figure tokens retained; confirm label pairing in source/PNG |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-004/p001.txt | DOC-004 PDF p.1 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-001.txt | DOC-001 PDF pp.1-9 | DUPLICATE | Poppler pdftotext (original version unavailable) | Whole-document extraction overlaps exact page files |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-002.txt | DOC-002 PDF pp.1-129 | DUPLICATE | Poppler pdftotext (original version unavailable) | Whole-document extraction overlaps exact page files |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-003.txt | DOC-003 PDF pp.1-5 | DUPLICATE | Poppler pdftotext (original version unavailable) | Whole-document extraction overlaps exact page files |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/DOC-004.txt | DOC-004 PDF p.1 | DUPLICATE | Poppler pdftotext (original version unavailable) | Whole-document extraction overlaps exact page files |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-001/p001.txt | DOC-001 PDF p.1 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-001/p002.txt | DOC-001 PDF p.2 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-001/p003.txt | DOC-001 PDF p.3 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-001/p004.txt | DOC-001 PDF p.4 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-001/p005.txt | DOC-001 PDF p.5 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-001/p006.txt | DOC-001 PDF p.6 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-001/p007.txt | DOC-001 PDF p.7 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-001/p008.txt | DOC-001 PDF p.8 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-001/p009.txt | DOC-001 PDF p.9 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p001.txt | DOC-002 PDF p.1 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p002.txt | DOC-002 PDF p.2 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p003.txt | DOC-002 PDF p.3 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p004.txt | DOC-002 PDF p.4 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p005.txt | DOC-002 PDF p.5 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p006.txt | DOC-002 PDF p.6 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p007.txt | DOC-002 PDF p.7 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p008.txt | DOC-002 PDF p.8 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p009.txt | DOC-002 PDF p.9 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p010.txt | DOC-002 PDF p.10 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p011.txt | DOC-002 PDF p.11 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p012.txt | DOC-002 PDF p.12 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p013.txt | DOC-002 PDF p.13 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p014.txt | DOC-002 PDF p.14 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p015.txt | DOC-002 PDF p.15 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p016.txt | DOC-002 PDF p.16 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p017.txt | DOC-002 PDF p.17 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p018.txt | DOC-002 PDF p.18 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p019.txt | DOC-002 PDF p.19 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p020.txt | DOC-002 PDF p.20 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p021.txt | DOC-002 PDF p.21 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p022.txt | DOC-002 PDF p.22 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p023.txt | DOC-002 PDF p.23 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p024.txt | DOC-002 PDF p.24 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p025.txt | DOC-002 PDF p.25 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p026.txt | DOC-002 PDF p.26 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p027.txt | DOC-002 PDF p.27 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p028.txt | DOC-002 PDF p.28 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p029.txt | DOC-002 PDF p.29 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p030.txt | DOC-002 PDF p.30 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p031.txt | DOC-002 PDF p.31 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p032.txt | DOC-002 PDF p.32 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p033.txt | DOC-002 PDF p.33 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p034.txt | DOC-002 PDF p.34 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p035.txt | DOC-002 PDF p.35 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p036.txt | DOC-002 PDF p.36 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p037.txt | DOC-002 PDF p.37 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p038.txt | DOC-002 PDF p.38 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p039.txt | DOC-002 PDF p.39 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p040.txt | DOC-002 PDF p.40 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p041.txt | DOC-002 PDF p.41 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p042.txt | DOC-002 PDF p.42 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p043.txt | DOC-002 PDF p.43 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p044.txt | DOC-002 PDF p.44 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p045.txt | DOC-002 PDF p.45 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p046.txt | DOC-002 PDF p.46 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p047.txt | DOC-002 PDF p.47 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p048.txt | DOC-002 PDF p.48 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p049.txt | DOC-002 PDF p.49 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p050.txt | DOC-002 PDF p.50 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p051.txt | DOC-002 PDF p.51 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p052.txt | DOC-002 PDF p.52 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p053.txt | DOC-002 PDF p.53 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p054.txt | DOC-002 PDF p.54 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p055.txt | DOC-002 PDF p.55 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p056.txt | DOC-002 PDF p.56 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p057.txt | DOC-002 PDF p.57 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p058.txt | DOC-002 PDF p.58 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p059.txt | DOC-002 PDF p.59 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p060.txt | DOC-002 PDF p.60 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p061.txt | DOC-002 PDF p.61 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p062.txt | DOC-002 PDF p.62 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p063.txt | DOC-002 PDF p.63 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p064.txt | DOC-002 PDF p.64 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p065.txt | DOC-002 PDF p.65 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p066.txt | DOC-002 PDF p.66 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p067.txt | DOC-002 PDF p.67 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p068.txt | DOC-002 PDF p.68 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p069.txt | DOC-002 PDF p.69 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p070.txt | DOC-002 PDF p.70 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p071.txt | DOC-002 PDF p.71 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p072.txt | DOC-002 PDF p.72 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p073.txt | DOC-002 PDF p.73 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p074.txt | DOC-002 PDF p.74 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p075.txt | DOC-002 PDF p.75 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p076.txt | DOC-002 PDF p.76 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p077.txt | DOC-002 PDF p.77 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p078.txt | DOC-002 PDF p.78 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p079.txt | DOC-002 PDF p.79 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p080.txt | DOC-002 PDF p.80 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p081.txt | DOC-002 PDF p.81 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p082.txt | DOC-002 PDF p.82 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p083.txt | DOC-002 PDF p.83 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p084.txt | DOC-002 PDF p.84 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p085.txt | DOC-002 PDF p.85 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p086.txt | DOC-002 PDF p.86 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p087.txt | DOC-002 PDF p.87 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p088.txt | DOC-002 PDF p.88 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p089.txt | DOC-002 PDF p.89 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p090.txt | DOC-002 PDF p.90 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p091.txt | DOC-002 PDF p.91 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p092.txt | DOC-002 PDF p.92 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p093.txt | DOC-002 PDF p.93 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p094.txt | DOC-002 PDF p.94 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p095.txt | DOC-002 PDF p.95 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p096.txt | DOC-002 PDF p.96 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p097.txt | DOC-002 PDF p.97 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p098.txt | DOC-002 PDF p.98 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p099.txt | DOC-002 PDF p.99 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p100.txt | DOC-002 PDF p.100 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p101.txt | DOC-002 PDF p.101 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p102.txt | DOC-002 PDF p.102 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p103.txt | DOC-002 PDF p.103 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p104.txt | DOC-002 PDF p.104 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p105.txt | DOC-002 PDF p.105 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p106.txt | DOC-002 PDF p.106 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p107.txt | DOC-002 PDF p.107 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p108.txt | DOC-002 PDF p.108 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p109.txt | DOC-002 PDF p.109 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p110.txt | DOC-002 PDF p.110 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p111.txt | DOC-002 PDF p.111 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p112.txt | DOC-002 PDF p.112 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p113.txt | DOC-002 PDF p.113 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p114.txt | DOC-002 PDF p.114 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p115.txt | DOC-002 PDF p.115 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p116.txt | DOC-002 PDF p.116 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p117.txt | DOC-002 PDF p.117 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p118.txt | DOC-002 PDF p.118 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p119.txt | DOC-002 PDF p.119 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p120.txt | DOC-002 PDF p.120 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p121.txt | DOC-002 PDF p.121 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p122.txt | DOC-002 PDF p.122 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p123.txt | DOC-002 PDF p.123 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p124.txt | DOC-002 PDF p.124 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p125.txt | DOC-002 PDF p.125 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p126.txt | DOC-002 PDF p.126 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p127.txt | DOC-002 PDF p.127 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p128.txt | DOC-002 PDF p.128 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/p129.txt | DOC-002 PDF p.129 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-003/p001.txt | DOC-003 PDF p.1 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-003/p002.txt | DOC-003 PDF p.2 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-003/p003.txt | DOC-003 PDF p.3 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-003/p004.txt | DOC-003 PDF p.4 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-003/p005.txt | DOC-003 PDF p.5 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-004/p001.txt | DOC-004 PDF p.1 | USABLE | Poppler pdftotext (original version unavailable) | Source-matched text locator |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text_page_character_counts.tsv | All DOC-001 pp.1-9; DOC-002 pp.1-129; DOC-003 pp.1-5; DOC-004 p.1 | USABLE | Legacy extraction metadata/page register | Page-to-artifact identity and usability metadata only |
| .ai_paper_validation/review_1_5_2/preprocessing/page_text_usability.tsv | All DOC-001 pp.1-9; DOC-002 pp.1-129; DOC-003 pp.1-5; DOC-004 p.1 | USABLE | Legacy extraction metadata/page register | Page-to-artifact identity and usability metadata only |
| .ai_paper_validation/review_1_5_2/preprocessing/page_unit_register.md | All DOC-001 pp.1-9; DOC-002 pp.1-129; DOC-003 pp.1-5; DOC-004 p.1 | USABLE | Legacy extraction metadata/page register | Page-to-artifact identity and usability metadata only |
| .ai_paper_validation/review_1_5_2/preprocessing/pdfinfo/DOC-001_pdfinfo.txt | DOC-001 PDF pp.1-9 | USABLE | Poppler pdfinfo (original version unavailable) | Document identity and unit-count metadata |
| .ai_paper_validation/review_1_5_2/preprocessing/pdfinfo/DOC-002_pdfinfo.txt | DOC-002 PDF pp.1-129 | USABLE | Poppler pdfinfo (original version unavailable) | Document identity and unit-count metadata |
| .ai_paper_validation/review_1_5_2/preprocessing/pdfinfo/DOC-003_pdfinfo.txt | DOC-003 PDF pp.1-5 | USABLE | Poppler pdfinfo (original version unavailable) | Document identity and unit-count metadata |
| .ai_paper_validation/review_1_5_2/preprocessing/pdfinfo/DOC-004_pdfinfo.txt | DOC-004 PDF p.1 | USABLE | Poppler pdfinfo (original version unavailable) | Document identity and unit-count metadata |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p001.png | DOC-001 PDF p.1 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p002.png | DOC-001 PDF p.2 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p003.png | DOC-001 PDF p.3 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p004.png | DOC-001 PDF p.4 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p005.png | DOC-001 PDF p.5 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p006.png | DOC-001 PDF p.6 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p007.png | DOC-001 PDF p.7 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p008.png | DOC-001 PDF p.8 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p006.png | DOC-002 PDF p.6 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p007.png | DOC-002 PDF p.7 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p008.png | DOC-002 PDF p.8 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p009.png | DOC-002 PDF p.9 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p010.png | DOC-002 PDF p.10 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p011.png | DOC-002 PDF p.11 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p012.png | DOC-002 PDF p.12 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p013.png | DOC-002 PDF p.13 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p014.png | DOC-002 PDF p.14 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p015.png | DOC-002 PDF p.15 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p016.png | DOC-002 PDF p.16 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p017.png | DOC-002 PDF p.17 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p018.png | DOC-002 PDF p.18 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p019.png | DOC-002 PDF p.19 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p020.png | DOC-002 PDF p.20 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p021.png | DOC-002 PDF p.21 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p022.png | DOC-002 PDF p.22 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p023.png | DOC-002 PDF p.23 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p024.png | DOC-002 PDF p.24 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p025.png | DOC-002 PDF p.25 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p026.png | DOC-002 PDF p.26 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p027.png | DOC-002 PDF p.27 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p028.png | DOC-002 PDF p.28 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p029.png | DOC-002 PDF p.29 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p030.png | DOC-002 PDF p.30 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p031.png | DOC-002 PDF p.31 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p032.png | DOC-002 PDF p.32 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p036.png | DOC-002 PDF p.36 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p037.png | DOC-002 PDF p.37 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p038.png | DOC-002 PDF p.38 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p039.png | DOC-002 PDF p.39 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p040.png | DOC-002 PDF p.40 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p041.png | DOC-002 PDF p.41 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p042.png | DOC-002 PDF p.42 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p043.png | DOC-002 PDF p.43 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p044.png | DOC-002 PDF p.44 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p045.png | DOC-002 PDF p.45 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p046.png | DOC-002 PDF p.46 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p047.png | DOC-002 PDF p.47 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p048.png | DOC-002 PDF p.48 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p049.png | DOC-002 PDF p.49 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p050.png | DOC-002 PDF p.50 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p051.png | DOC-002 PDF p.51 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p052.png | DOC-002 PDF p.52 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p053.png | DOC-002 PDF p.53 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p054.png | DOC-002 PDF p.54 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p055.png | DOC-002 PDF p.55 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p070.png | DOC-002 PDF p.70 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p072.png | DOC-002 PDF p.72 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p082.png | DOC-002 PDF p.82 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p083.png | DOC-002 PDF p.83 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p090.png | DOC-002 PDF p.90 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p091.png | DOC-002 PDF p.91 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p092.png | DOC-002 PDF p.92 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p093.png | DOC-002 PDF p.93 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p094.png | DOC-002 PDF p.94 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p095.png | DOC-002 PDF p.95 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p096.png | DOC-002 PDF p.96 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p097.png | DOC-002 PDF p.97 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p098.png | DOC-002 PDF p.98 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p099.png | DOC-002 PDF p.99 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p100.png | DOC-002 PDF p.100 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p101.png | DOC-002 PDF p.101 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p102.png | DOC-002 PDF p.102 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p103.png | DOC-002 PDF p.103 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p104.png | DOC-002 PDF p.104 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p105.png | DOC-002 PDF p.105 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p106.png | DOC-002 PDF p.106 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p107.png | DOC-002 PDF p.107 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p122.png | DOC-002 PDF p.122 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p123.png | DOC-002 PDF p.123 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p124.png | DOC-002 PDF p.124 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p125.png | DOC-002 PDF p.125 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p126.png | DOC-002 PDF p.126 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p127.png | DOC-002 PDF p.127 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p128.png | DOC-002 PDF p.128 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p001.png | DOC-003 PDF p.1 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p002.png | DOC-003 PDF p.2 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p003.png | DOC-003 PDF p.3 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p004.png | DOC-003 PDF p.4 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p005.png | DOC-003 PDF p.5 | USABLE | Poppler renderer inferred; PNG validated by file | Exact-page visual locator |

## Fresh confirmation derivatives in this run

These derivatives are newly generated within review_1_6_1 and are not members of the reused-artifact hash set.

| Artifact path | Exact source units | Fitness | Engine or method | Purpose |
|---|---|---|---|---|
| .ai_paper_validation/review_1_6_1/preprocessing/support4-DOC003-p003.png | DOC-003 PDF p.3 | USABLE | pdftoppm Poppler25.03.0,160dpi CPU; command in support_part_4.md | Supplementary risk-table visual transcription |
| .ai_paper_validation/review_1_6_1/preprocessing/numeric_confirmation/main-p4-p7.txt | DOC-001 PDF pp.4-7 | USABLE | pdftotext -layout Poppler25.03.0 | Numeric finding source confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/statistical_pass_1/main-p003-p008.txt | DOC-001 PDF pp.3-8 | USABLE | pdftotext Poppler25.03.0 | Statistical source confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/statistical_pass_1/main-p002.txt | DOC-001 PDF p.2 | USABLE | pdftotext Poppler25.03.0 | Randomization definition confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/statistical_pass_1/plan-p082.txt | DOC-002 PDF p.82 | USABLE | pdftotext Poppler25.03.0 | Original SAP confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/statistical_pass_1/plan-p098-p099.txt | DOC-002 PDF pp.98-99 | USABLE | pdftotext Poppler25.03.0 | Final strata and intervention confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/statistical_pass_1/plan-p102-p105.txt | DOC-002 PDF pp.102-105 | USABLE | pdftotext Poppler25.03.0 | Final statistical specification confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/statistical_pass_1/main-p005.png | DOC-001 PDF p.5 | USABLE | pdftoppm Poppler25.03.0,140dpi CPU | Table2 alignment |
| .ai_paper_validation/review_1_6_1/preprocessing/statistical_pass_1/main-p007.png | DOC-001 PDF p.7 | USABLE | pdftoppm Poppler25.03.0,140dpi CPU | Figure3 direction and alignment |
| .ai_paper_validation/review_1_6_1/preprocessing/inclusion_screen_confirmation/main-p001-p008.txt | DOC-001 PDF pp.1-8 | USABLE | pdftotext -layout Poppler25.03.0 | Independent screening confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/inclusion_screen_confirmation/main-p009.txt | DOC-001 PDF p.9 | USABLE | pdftotext -layout Poppler25.03.0 | Independent screening confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/inclusion_screen_confirmation/results-p001-p005.txt | DOC-003 PDF pp.1-5 | USABLE | pdftotext -layout Poppler25.03.0 | Independent screening confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/inclusion_screen_confirmation/data-sharing-p001.txt | DOC-004 PDF p.1 | USABLE | pdftotext -layout Poppler25.03.0 | Independent screening confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/inclusion_screen_confirmation/plan-p055.txt | DOC-002 PDF p.55 | USABLE | pdftotext -layout Poppler25.03.0 | Independent screening confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/inclusion_screen_confirmation/plan-p082.txt | DOC-002 PDF p.82 | USABLE | pdftotext -layout Poppler25.03.0 | Independent screening confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/inclusion_screen_confirmation/plan-p095-p105.txt | DOC-002 PDF pp.95-105 | USABLE | pdftotext -layout Poppler25.03.0 | Independent screening confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/inclusion_screen_confirmation/main-p007.png | DOC-001 PDF p.7 | USABLE | pdftoppm Poppler25.03.0,115dpi CPU | Independent screening confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/inclusion_screen_confirmation/results-p003.png | DOC-003 PDF p.3 | USABLE | pdftoppm Poppler25.03.0,115dpi CPU | Independent screening confirmation |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/main-p001-p009.txt | Main PDF pp.1,2,3,4,5,6,7,8,9 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/results-p001-p005.txt | Results PDF pp.1,2,3,4,5 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/data-sharing-p001.txt | Data-sharing PDF p.1 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p55.txt | Plan PDF p.55 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p82.txt | Plan PDF p.82 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p95.txt | Plan PDF p.95 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p96.txt | Plan PDF p.96 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p98.txt | Plan PDF p.98 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p99.txt | Plan PDF p.99 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p100.txt | Plan PDF p.100, intervention context | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p101.txt | Plan PDF p.101, intervention context | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p102.txt | Plan PDF p.102, endpoint context | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p103.txt | Plan PDF p.103 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p104.txt | Plan PDF p.104 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/plan-p105.txt | Plan PDF p.105 | USABLE | Poppler pdftotext 25.03.0, native layout | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/main-p007.png | Main PDF p.7 | USABLE | Poppler pdftoppm 25.03.0, CPU PNG at 130 dpi | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/results-p004.png | Results PDF p.4 | USABLE | Poppler pdftoppm 25.03.0, CPU PNG at 100 dpi | Mechanical evidence recheck |
| .ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/results-p005.png | Results PDF p.5 | USABLE | Poppler pdftoppm 25.03.0, CPU PNG at 100 dpi | Mechanical evidence recheck |
