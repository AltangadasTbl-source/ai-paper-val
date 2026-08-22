# Supplement Text-Layer and GPU OCR Audit

## Scope

- Packages audited: the seven newly created 2018 and 2019 JAMA RCT packages.
- Supplement PDFs audited: 20.
- PDF pages audited: 474.
- Method: page-level native-text extraction with PyMuPDF, followed by visual review of pages with absent or unusable text layers.

## Result

Eighteen supplement PDFs have usable native text throughout. Two PDFs contain localized image-only or effectively image-only pages and required targeted OCR:

| Package | PDF | OCR pages (1-based PDF pages) | Reason |
|---|---|---:|---|
| `2018/jama.2017.21906` | `joi170166supp3_prod.pdf` | 3-16 | Embedded report pages have only a minimal, unusable text layer. |
| `2018/jama.2018.0156` | `joi180004supp1_prod.pdf` | 52, 108-109, 126-133 | Page 52 is an effectively image-only table; pages 108-109 and 126-133 are scanned amendment/SAP pages. |

Page 134 of `joi180004supp1_prod.pdf` has no useful native text but is visually blank apart from header/footer material, so it was intentionally not OCRed.

## OCR execution and retained assets

OCR was executed through Windows PowerShell into WSL with `/home/juliz/venvs/stt/bin/python` and RapidOCR. The recorded device is `NVIDIA GeForce RTX 5070 Laptop GPU, 8151 MiB`; detector, classifier, and recognizer sessions all list `CUDAExecutionProvider` first.

- `2018/jama.2017.21906/.ai_paper_validation/preprocessing/joi170166supp3_prod/`
  - 14 rendered page images
  - 14 page-level OCR text files
  - 14 page-level metadata files
  - 15,200 recognized characters
  - page mean-confidence range: 0.8097-0.9782
- `2018/jama.2018.0156/.ai_paper_validation/preprocessing/joi180004supp1_prod/`
  - 11 rendered page images
  - 11 page-level OCR text files
  - 11 page-level metadata files
  - 14,879 recognized characters
  - page mean-confidence range: 0.9536-0.9864

Each output directory includes:

- `ocr_pages/`: reusable UTF-8 OCR text with PDF filename, SHA-256, and 1-based source page in the header.
- `ocr_metadata/`: per-page character count, line count, confidence, elapsed time, and source provenance.
- `images/`: the exact rendered inputs retained for visual verification.
- `ocr_scope.json`: source hash, selected pages, total page count, and render scale.
- `gpu_ocr_backend_report.json`: GPU identity and actual execution-provider order.
- `ocr_manifest.json`: consolidated source, backend, and page-level records.

The source PDFs were not modified. A 3.0x render comparison was also run for the small-text ACS QUIK pages; its confidence was lower on 9 of 10 pages than the retained 2.25x run, so the 2.25x results were retained.

## Reproduction

The reusable runner is `scripts/gpu_ocr_selected_pages.py`. It rejects a run unless CUDA is the primary execution provider for all three RapidOCR stages.
