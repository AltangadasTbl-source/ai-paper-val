# Direct-source recheck derivative record

Scope: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018.

Engine: Poppler 25.03.0 direct local CPU `pdftoppm` (PNG rendering) and `pdftotext -layout` (locator text). Arithmetic: direct local awk, no Python. The source images, not extracted text, were read for the registered comparisons.

| Source | Exact source units | Derivatives | Engine / command |
|---|---|---|---|
| jama_jabre_2018_oi_180004.pdf | PDF pages 1, 2, 3, 4, 5, 6, 7 | main-p1.png/main-p1.txt through main-p7.png/main-p7.txt, each one page | pdftoppm -f N -l N -singlefile -scale-to 1800 -png; pdftotext -layout -f N -l N |
| jama_jabre_2018_oi_180004.pdf | PDF page 6, Table 2 ETI PP row and nearby headers/footnote | main-p6-table2-detail.png | pdftoppm -f 6 -l 6 -singlefile -r 220 -x 800 -y 550 -W 950 -H 900 -png |
| joi180004supp2_prod.pdf | PDF pages 2, 3 | supp2-p2.png/supp2-p2.txt; supp2-p3.png/supp2-p3.txt | pdftoppm -f N -l N -singlefile -scale-to 1800 -png; pdftotext -layout -f N -l N |
| Visually confirmed inputs above | C001 through C018 | calculations.txt | awk BEGIN arithmetic; %.12f diagnostic values and nearest decimal displays |

Source correspondence: `sha256sum -c .ai_paper_validation/review_1_6/source_hashes_before.sha256` returned OK for all three supplied PDF sources. Main source SHA-256: 114e922542bbb1f8369ca9b5c19be65d93856e16cf4ff295c483439e4e208839. Results supplement SHA-256: 937e18794fc87074907b1e9ab792f9a35d2f2d895d586dd27e7cbf44d5ed8d46.

All derivative paths in this record are relative to this recheck001 directory. No source or reused artifact was modified. No OCR, GPU, temporary environment, or external evidence was needed. Native layout text matches the visual values in the registered comparisons. An initial low-resolution glance at C007 was ambiguous between 370 and 377; the 220-dpi source crop unambiguously prints 377, consistent with native text and the ledger. That initial glance was not a source/text discrepancy. The durable arithmetic file uses 377.
