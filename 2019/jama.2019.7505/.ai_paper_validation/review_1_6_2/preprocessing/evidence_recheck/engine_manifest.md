# Evidence-recheck derivative engine manifest

Owner runtime: 01a1296f-944f-75b1-9a85-459ba68c6feb. Compute device: CPU, as recorded in tooling_record.md. Direct Poppler pdftoppm/pdftotext 26.01.0. No OCR, Office conversion, GPU or fallback environment was used. These are targeted confirmations and complete-search derivatives, not new uncovered units. Supplied sources and reused assets were not changed.

Full-page rendering command pattern: `pdftoppm -f N -l N -r DPI -singlefile -png SOURCE.pdf OUTPUT_STEM`. Targeted glyph command: `pdftoppm -f 32 -l 32 -r 300 -x 350 -y 1940 -W 1900 -H 220 -singlefile -png joi190055supp1_prod_16092.pdf protocol-p32-coma-detail`. Complete-text pattern: `pdftotext -layout SOURCE.pdf OUTPUT.txt`. Every output below is relative to this manifest's directory.

| Derivative | Exact supplied source | PDF pages | Engine/method | Device | Purpose |
|---|---|---|---|---|---|
| main-p1.png | jama_bluth_2019_oi_190055_16092.pdf | 1 | pdftoppm 26.01.0, PNG, 120 dpi full page | CPU | Visual exact-source confirmation |
| main-p7.png | jama_bluth_2019_oi_190055_16092.pdf | 7 | pdftoppm 26.01.0, PNG, 120 dpi full page | CPU | Visual exact-source confirmation |
| main-p8.png | jama_bluth_2019_oi_190055_16092.pdf | 8 | pdftoppm 26.01.0, PNG, 120 dpi full page | CPU | Visual exact-source confirmation |
| main-p9.png | jama_bluth_2019_oi_190055_16092.pdf | 9 | pdftoppm 26.01.0, PNG, 120 dpi full page | CPU | Visual exact-source confirmation |
| main-p10.png | jama_bluth_2019_oi_190055_16092.pdf | 10 | pdftoppm 26.01.0, PNG, 120 dpi full page | CPU | Visual exact-source confirmation |
| results-p29.png | joi190055supp4_prod_16092.pdf | 29 | pdftoppm 26.01.0, PNG, 120 dpi full page | CPU | Visual exact-source confirmation |
| results-p30.png | joi190055supp4_prod_16092.pdf | 30 | pdftoppm 26.01.0, PNG, 120 dpi full page | CPU | Visual exact-source confirmation |
| results-p38.png | joi190055supp4_prod_16092.pdf | 38 | pdftoppm 26.01.0, PNG, 120 dpi full page | CPU | Visual exact-source confirmation |
| results-p42.png | joi190055supp4_prod_16092.pdf | 42 | pdftoppm 26.01.0, PNG, 120 dpi full page | CPU | Visual exact-source confirmation |
| results-p20.png | joi190055supp4_prod_16092.pdf | 20 | pdftoppm 26.01.0, PNG, 120 dpi full page | CPU | Visual exact-source confirmation |
| results-p21.png | joi190055supp4_prod_16092.pdf | 21 | pdftoppm 26.01.0, PNG, 120 dpi full page | CPU | Visual exact-source confirmation |
| protocol-p31.png | joi190055supp1_prod_16092.pdf | 31 | pdftoppm 26.01.0, PNG, 160 dpi full page | CPU | Visual exact-source confirmation |
| protocol-p32.png | joi190055supp1_prod_16092.pdf | 32 | pdftoppm 26.01.0, PNG, 160 dpi full page | CPU | Visual exact-source confirmation |
| protocol-p32-coma-detail.png | joi190055supp1_prod_16092.pdf | 32 | pdftoppm 26.01.0, PNG, 300 dpi, crop x=350 y=1940 W=1900 H=220 device pixels | CPU | Confirm detached underline of protocol coma ≤8 |
| main-complete.txt | jama_bluth_2019_oi_190055_16092.pdf | 1–14 | pdftotext 26.01.0, native layout text | CPU | Independent complete report search |
| results-complete.txt | joi190055supp4_prod_16092.pdf | 1–43 | pdftotext 26.01.0, native layout text | CPU | Independent complete report search |

Derivative count: 16 (13 full-page images, one targeted glyph image, two complete layout-text files). All images were viewed by this fresh rechecker. Reusable current-run native extracts from inclusion_initial and statistics_pass_1 were useful locators; exact PDF rereading/rendering decided all comparisons. Direct stdout extractions produced no derivative: main pp.1–4,10–11; protocol pp.5,12,31–32; all SAP/amendment pages. Fresh complete text was searched with ripgrep for log-rank/log rank, clinical severity/severity weight, weighted, readmission, ventilation and sensitivity; image-only eFigure 12 content was visually read. No machine-text absence was treated as source-image absence.

