# Mechanical recheck derivative record

Runtime agent: /root/recheck. Compute device: CPU. No OCR or fallback environment used. All derivatives were produced directly from supplied PDFs; no source or reused asset was modified. Each PNG was visually inspected. Native layout text was read alongside its same-source rendered page, with rendered signs, labels, table columns and wording controlling the reading.

Engine for every TXT: direct `pdftotext -layout`, Poppler 25.03.0. Engine for every PNG: direct `pdftoppm -r 120 -singlefile -png`, Poppler 25.03.0, CPU, 120 dpi. Source page numbers below are physical PDF pages.

| Source | PDF page | Layout derivative | Render derivative |
|---|---:|---|---|
| jama_wang_2018_oi_180070.pdf | 1 | recheck-main-p1.txt | recheck-main-p1.png |
| jama_wang_2018_oi_180070.pdf | 3 | recheck-main-p3.txt | recheck-main-p3.png |
| jama_wang_2018_oi_180070.pdf | 4 | recheck-main-p4.txt | recheck-main-p4.png |
| jama_wang_2018_oi_180070.pdf | 5 | recheck-main-p5.txt | recheck-main-p5.png |
| jama_wang_2018_oi_180070.pdf | 6 | recheck-main-p6.txt | recheck-main-p6.png |
| jama_wang_2018_oi_180070.pdf | 7 | recheck-main-p7.txt | recheck-main-p7.png |
| jama_wang_2018_oi_180070.pdf | 8 | recheck-main-p8.txt | recheck-main-p8.png |
| joi180070supp1_prod.pdf | 16 | recheck-plan-p16.txt | recheck-plan-p16.png |
| joi180070supp1_prod.pdf | 18 | recheck-plan-p18.txt | recheck-plan-p18.png |
| joi180070supp1_prod.pdf | 19 | recheck-plan-p19.txt | recheck-plan-p19.png |
| joi180070supp2_prod.pdf | 2 | recheck-supp-p2.txt | recheck-supp-p2.png |

Command templates, instantiated separately for every table row:

```text
pdftotext -layout -f N -l N SOURCE .ai_paper_validation/review_1_6_2/preprocessing/STEM.txt
pdftoppm -r 120 -f N -l N -singlefile -png SOURCE .ai_paper_validation/review_1_6_2/preprocessing/STEM
```

All 22 extraction/render commands completed with exit code 0. These derivatives belong to this run and are locator/transcription aids; the supplied source PDF remains the evidence authority.
