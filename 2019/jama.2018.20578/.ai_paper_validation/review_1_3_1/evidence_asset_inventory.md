# Reused Evidence-Asset Inventory

All 47 eligible files below are preserved unchanged and hashed individually in
`reused_artifact_hashes_before.sha256`. Fitness means fitness as a locator or transcription aid, not
authority for a candidate. Direct source confirmation remains mandatory.

## Document maps and provenance metadata

| Asset | Package-relative artifact | Exact source coverage | Method/provenance | Fitness | Limitation |
|---|---|---|---|---|---|
| A001 | `.ai_paper_validation/document_outputs/package_manifest.md` | DOC-001 pp. 1-10; DOC-002 pp. 1-7; DOC-003 pp. 1-29 | Prior package inventory | `PARTIAL` | Identity, page counts, and filenames are usable; prior-profile scientific dispositions are not reused |
| A002 | `.ai_paper_validation/document_outputs/DOC-001/document_record.md` | DOC-001 pp. 1-10 | Prior document inventory and preprocessing update | `STALE` | Identity/hash/headings usable; OCR availability statement conflicts with present pp. 7-9 OCR assets |
| A003 | `.ai_paper_validation/document_outputs/DOC-002/document_record.md` | DOC-002 pp. 1-7 | Prior document inventory | `PARTIAL` | Identity/hash/heading locations usable; old exclusion decision is outside 1.3.1 reuse scope |
| A004 | `.ai_paper_validation/document_outputs/DOC-003/document_record.md` | DOC-003 pp. 1-29 | Prior document inventory and contents map | `PARTIAL` | Identity/hash/eMethods/eTable/eFigure locations usable; old exclusion decision is not reused |
| A005 | `.ai_paper_validation/preprocessing/DOC-001/page_manifest.json` | DOC-001 pp. 1-10 | Prior extraction manifest | `STALE` | Incorrectly reports absent/incomplete OCR for pp. 7-9; p. 6 confidence also conflicts with its OCR metadata |
| A006 | `.ai_paper_validation/preprocessing/ocr_backend.json` | OCR provenance for DOC-001 pp. 3, 5-9 | RapidOCR/ONNX Runtime CPU backend record | `USABLE` | Provenance only; no scientific source content |

## DOC-001 native layout text

Each native file was reproduced byte-for-byte from the unchanged source using current
`pdftotext -layout -f N -l N`.

| Asset | Artifact | Exact source location | Fitness | Limitation |
|---|---|---|---|---|
| A007 | `.ai_paper_validation/preprocessing/DOC-001/native_text/page-01.txt` | DOC-001 PDF p. 1 | `USABLE` | Text-layer locator; direct PDF is authority |
| A008 | `.ai_paper_validation/preprocessing/DOC-001/native_text/page-02.txt` | DOC-001 PDF p. 2 | `USABLE` | Text-layer locator; direct PDF is authority |
| A009 | `.ai_paper_validation/preprocessing/DOC-001/native_text/page-03.txt` | DOC-001 PDF p. 3 | `USABLE` | Figure geometry requires image/direct PDF |
| A010 | `.ai_paper_validation/preprocessing/DOC-001/native_text/page-04.txt` | DOC-001 PDF p. 4 | `USABLE` | Text-layer locator; direct PDF is authority |
| A011 | `.ai_paper_validation/preprocessing/DOC-001/native_text/page-05.txt` | DOC-001 PDF p. 5 | `USABLE` | Table layout requires image/direct PDF |
| A012 | `.ai_paper_validation/preprocessing/DOC-001/native_text/page-06.txt` | DOC-001 PDF p. 6 | `USABLE` | Table layout requires image/direct PDF |
| A013 | `.ai_paper_validation/preprocessing/DOC-001/native_text/page-07.txt` | DOC-001 PDF p. 7 | `USABLE` | Table layout requires image/direct PDF |
| A014 | `.ai_paper_validation/preprocessing/DOC-001/native_text/page-08.txt` | DOC-001 PDF p. 8 | `PARTIAL` | 61,835 bytes with over-expanded/unusable table reading order |
| A015 | `.ai_paper_validation/preprocessing/DOC-001/native_text/page-09.txt` | DOC-001 PDF p. 9 | `USABLE` | Table layout requires image/direct PDF |
| A016 | `.ai_paper_validation/preprocessing/DOC-001/native_text/page-10.txt` | DOC-001 PDF p. 10 | `USABLE` | Text-layer locator; direct PDF is authority |

## DOC-001 normalized text

Every normalized file is exactly its corresponding native file with the terminal form-feed removed.
It adds no source content; p. 8 also inherits the native file's reading-order defect.

| Asset | Artifact | Exact source location | Fitness |
|---|---|---|---|
| A017 | `.ai_paper_validation/preprocessing/DOC-001/normalized_text/page-01.txt` | DOC-001 PDF p. 1 | `DUPLICATE` |
| A018 | `.ai_paper_validation/preprocessing/DOC-001/normalized_text/page-02.txt` | DOC-001 PDF p. 2 | `DUPLICATE` |
| A019 | `.ai_paper_validation/preprocessing/DOC-001/normalized_text/page-03.txt` | DOC-001 PDF p. 3 | `DUPLICATE` |
| A020 | `.ai_paper_validation/preprocessing/DOC-001/normalized_text/page-04.txt` | DOC-001 PDF p. 4 | `DUPLICATE` |
| A021 | `.ai_paper_validation/preprocessing/DOC-001/normalized_text/page-05.txt` | DOC-001 PDF p. 5 | `DUPLICATE` |
| A022 | `.ai_paper_validation/preprocessing/DOC-001/normalized_text/page-06.txt` | DOC-001 PDF p. 6 | `DUPLICATE` |
| A023 | `.ai_paper_validation/preprocessing/DOC-001/normalized_text/page-07.txt` | DOC-001 PDF p. 7 | `DUPLICATE` |
| A024 | `.ai_paper_validation/preprocessing/DOC-001/normalized_text/page-08.txt` | DOC-001 PDF p. 8 | `DUPLICATE` |
| A025 | `.ai_paper_validation/preprocessing/DOC-001/normalized_text/page-09.txt` | DOC-001 PDF p. 9 | `DUPLICATE` |
| A026 | `.ai_paper_validation/preprocessing/DOC-001/normalized_text/page-10.txt` | DOC-001 PDF p. 10 | `DUPLICATE` |

## DOC-001 rendered pages

| Asset | Artifact | Exact source location | Render metadata | Fitness | Limitation |
|---|---|---|---|---|---|
| A027 | `.ai_paper_validation/preprocessing/DOC-001/page_images/page-03.png` | DOC-001 PDF p. 3 | 2550×3300 RGB, 300 dpi | `USABLE` | Rendered locator; direct PDF remains authority |
| A028 | `.ai_paper_validation/preprocessing/DOC-001/page_images/page-05.png` | DOC-001 PDF p. 5 | 2550×3300 RGB, 300 dpi | `USABLE` | Rendered locator; direct PDF remains authority |
| A029 | `.ai_paper_validation/preprocessing/DOC-001/page_images/page-06.png` | DOC-001 PDF p. 6 | 1700×2200 RGB, 200 dpi | `USABLE` | Rendered locator; direct PDF remains authority |
| A030 | `.ai_paper_validation/preprocessing/DOC-001/page_images/page-07.png` | DOC-001 PDF p. 7 | 1700×2200 RGB, 200 dpi | `USABLE` | Rendered locator; direct PDF remains authority |
| A031 | `.ai_paper_validation/preprocessing/DOC-001/page_images/page-08.png` | DOC-001 PDF p. 8 | 1275×1650 RGB, 150 dpi | `USABLE` | Lower resolution; direct PDF confirmation required |
| A032 | `.ai_paper_validation/preprocessing/DOC-001/page_images/page-09.png` | DOC-001 PDF p. 9 | 1700×2200 RGB, 200 dpi | `USABLE` | Rendered locator; direct PDF remains authority |

## DOC-001 OCR text

All OCR files are nonempty RapidOCR CPU outputs and are usable only as transcription aids.

| Asset | Artifact | Exact source location | Per-page metadata confidence | Fitness |
|---|---|---|---:|---|
| A033 | `.ai_paper_validation/preprocessing/DOC-001/ocr_text/page-03.txt` | DOC-001 PDF p. 3 | 0.8923 | `USABLE` |
| A034 | `.ai_paper_validation/preprocessing/DOC-001/ocr_text/page-05.txt` | DOC-001 PDF p. 5 | 0.8646 | `USABLE` |
| A035 | `.ai_paper_validation/preprocessing/DOC-001/ocr_text/page-06.txt` | DOC-001 PDF p. 6 | 0.8904 | `USABLE` |
| A036 | `.ai_paper_validation/preprocessing/DOC-001/ocr_text/page-07.txt` | DOC-001 PDF p. 7 | 0.8404 | `USABLE` |
| A037 | `.ai_paper_validation/preprocessing/DOC-001/ocr_text/page-08.txt` | DOC-001 PDF p. 8 | 0.8795 | `USABLE` |
| A038 | `.ai_paper_validation/preprocessing/DOC-001/ocr_text/page-09.txt` | DOC-001 PDF p. 9 | 0.9003 | `USABLE` |

## DOC-001 OCR metadata

| Asset | Artifact | Exact source location | Recorded method | Fitness | Limitation |
|---|---|---|---|---|---|
| A039 | `.ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page-03.json` | DOC-001 PDF p. 3 / A027 / A033 | `rapidocr_onnxruntime`, CPUExecutionProvider, completed | `USABLE` | Metadata/provenance only |
| A040 | `.ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page-05.json` | DOC-001 PDF p. 5 / A028 / A034 | `rapidocr_onnxruntime`, CPUExecutionProvider, completed | `USABLE` | Metadata/provenance only |
| A041 | `.ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page-06.json` | DOC-001 PDF p. 6 / A029 / A035 | `rapidocr_onnxruntime`, CPUExecutionProvider, completed | `USABLE` | Overrides stale manifest confidence |
| A042 | `.ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page-07.json` | DOC-001 PDF p. 7 / A030 / A036 | `rapidocr_onnxruntime`, CPUExecutionProvider, completed | `USABLE` | Overrides stale manifest absence statement |
| A043 | `.ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page-08.json` | DOC-001 PDF p. 8 / A031 / A037 | `rapidocr_onnxruntime`, CPUExecutionProvider, completed | `USABLE` | Overrides stale manifest incomplete statement |
| A044 | `.ai_paper_validation/preprocessing/DOC-001/ocr_metadata/page-09.json` | DOC-001 PDF p. 9 / A032 / A038 | `rapidocr_onnxruntime`, CPUExecutionProvider, completed | `USABLE` | Overrides stale manifest absence statement |

## Full-document rights-screen layout text

Each file was reproduced byte-for-byte from the current source with `pdftotext -layout`; its form-feed
count equals its PDF page count.

| Asset | Artifact | Exact source coverage | Method | Fitness | Limitation |
|---|---|---|---|---|---|
| A045 | `.ai_paper_validation/rights_screen/jama_flint_2019_oi_190079.txt` | DOC-001 PDF pp. 1-10 | Full-document `pdftotext -layout` | `DUPLICATE` | Exact concatenated equivalent of A007-A016 |
| A046 | `.ai_paper_validation/rights_screen/joi180151supp1_prod.txt` | DOC-002 PDF pp. 1-7 | Full-document `pdftotext -layout` | `USABLE` | No page-level derivatives; use form-feed page boundaries and direct PDF |
| A047 | `.ai_paper_validation/rights_screen/joi180151supp2_prod.txt` | DOC-003 PDF pp. 1-29 | Full-document `pdftotext -layout` | `PARTIAL` | Text layer is complete, but visual table/figure geometry on pp. 7-26 is not fully represented |

## Fitness totals and exclusions

| Fitness | Count |
|---|---:|
| `USABLE` | 29 |
| `PARTIAL` | 5 |
| `STALE` | 2 |
| `DUPLICATE` | 11 |
| `UNREADABLE` | 0 |
| **Total** | **47** |

Not hashed as reusable scientific evidence: `.ai_paper_validation/final_report.md`, all
`workflow_response_summary.md` files, and all `ai_training_restriction_record.md` files. The first two
classes are legacy conclusions/workflow outputs prohibited as discovery inputs; the last is an
administrative rights decision rather than source-linked quantitative evidence. The three underlying
rights-screen text extractions are included as A045-A047.

## Targeted current-run confirmation derivatives

These files were created only after the before-hash inventory to close the visual-layout gap registered
for DOC-003 pp. 7-26. They are current-run outputs, are not reused artifacts, and therefore are not
included in `reused_artifact_hashes_before.sha256`. Every candidate still cites and was checked against
the direct PDF page.

- **Rendered outputs:**
  `.ai_paper_validation/review_1_3_1/preprocessing/support_pages/doc003-07.png` through
  `doc003-26.png`, covering DOC-003 PDF pp. 7-26 at 180 dpi.
- **Render command:**
  `mkdir -p .ai_paper_validation/review_1_3_1/preprocessing/support_pages && pdftoppm -f 7 -l 26 -r 180 -png 'joi180151supp2_prod.pdf' '.ai_paper_validation/review_1_3_1/preprocessing/support_pages/doc003' && file .ai_paper_validation/review_1_3_1/preprocessing/support_pages/doc003-*.png`
- **OCR outputs:**
  `.ai_paper_validation/review_1_3_1/preprocessing/support_pages/doc003-22-ocr.txt` through
  `doc003-26-ocr.txt`, covering only the embedded forest-plot text on DOC-003 PDF pp. 22-26.
- **OCR commands:** `tesseract` was invoked separately for pages 22, 23, 24, 25, and 26 as
  `tesseract .ai_paper_validation/review_1_3_1/preprocessing/support_pages/doc003-NN.png .ai_paper_validation/review_1_3_1/preprocessing/support_pages/doc003-NN-ocr -l eng --psm 6`.
- **Tool versions:** `pdftoppm` 26.01.0; `tesseract` 5.5.0 with Leptonica 1.86.0.
- **Fitness and use:** `USABLE` as direct-source render/transcription aids. The targeted OCR was not
  treated as authority; every transcribed forest-plot value was visually confirmed against its direct
  page render and cited to the source PDF.

DOC-001 PDF p. 8 was also rendered twice for temporary direct visual confirmation of its rotated
Table 4. These inspection files are under `/tmp`, are not package evidence assets, and are not linked
as evidence. Poppler `pdftoppm` 26.01.0 was run as
`qc13_tmp_dir=$(mktemp -d /tmp/qc13-main-page8-XXXXXX) && pdftoppm -f 8 -l 8 -singlefile -r 300 -png 'jama_flint_2019_oi_190079.pdf' "$qc13_tmp_dir/page-08-direct"`;
the resolved output was `/tmp/qc13-main-page8-B3JH2D/page-08-direct.png` (2550x3300 RGB). For readable
orientation, GPL Ghostscript 10.06.0 was run as
`gs -q -dNOPAUSE -dBATCH -sDEVICE=png16m -r300 -dFirstPage=8 -dLastPage=8 -sOutputFile=/tmp/qc13-page8-rotated.png -c '<</Orientation 3>> setpagedevice' -f 'jama_flint_2019_oi_190079.pdf'`;
the temporary output was `/tmp/qc13-page8-rotated.png` (3300x2550 RGB). Both were used only to confirm
the direct PDF layout and values.
