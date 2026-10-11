# Mechanical recheck derivatives

Compute device: CPU. Direct engines: pdftotext and pdftoppm, Poppler 25.03.0. No OCR or fallback engine was used. No direct source or reusable artifact was modified.

Fresh layout text was produced directly from each supplied source with `pdftotext -layout SOURCE DESTINATION`: `jama_stunnenberg_2018_oi_180136.pdf` to `main-layout.txt` (all 10 PDF pages), `joi180136supp1_prod.pdf` to `plan-layout.txt` (all 55 pages), and `joi180136supp2_prod.pdf` to `supp-layout.txt` (all 17 pages). These files reside beside this record. Text supplied location/transcription assistance; the exact candidate pages were independently rendered from the supplied PDFs and visually inspected.

Each render used `pdftoppm -f N -l N -scale-to SIZE -singlefile -png SOURCE PREFIX`, producing PREFIX.png beside this record.

| Source | PDF pages N | SIZE | Output prefix pattern | Visual inspection |
|---|---|---:|---|---|
| jama_stunnenberg_2018_oi_180136.pdf | 1, 3, 4, 6 | 1600 | main-pN | COMPLETE |
| jama_stunnenberg_2018_oi_180136.pdf | 5, 8 | 2000 | main-pN | COMPLETE |
| jama_stunnenberg_2018_oi_180136.pdf | 7 | 2300 | main-pN | COMPLETE |
| joi180136supp1_prod.pdf | 7, 12, 31, 32, 33, 35, 38, 40, 41, 42 | 1500 | plan-pN | COMPLETE |
| joi180136supp1_prod.pdf | 39, 43 | 2000 | plan-pN | COMPLETE |
| joi180136supp1_prod.pdf | 21, 26 | 1600 | plan-pN | COMPLETE; prospective simulation and historical measurement alternatives |
| joi180136supp2_prod.pdf | 3, 4, 5, 10, 11, 12, 13, 14 | 1700 | supp-pN | COMPLETE |

Total: 29 fresh exact-source page renders, all visually inspected, including 27 candidate-comparison pages and two additional context/alternative pages. Additional complete current-source report texts were read/searched to confirm the supplied-package absence of the named robustness and interaction counterparts; prospective simulations and post hoc virtual-data simulations were distinguished from observed-trial analyses.

Auxiliary arithmetic was independently evaluated in the session's JavaScript tool environment: interval endpoints and gaps, hypergeometric permutation sums, and Student t probabilities via regularized incomplete-beta integration with a continued fraction and Lanczos log-gamma calculation. No Python scientific extraction, orchestration, selection or classification was used. Numerical diagnostics do not assert actual unavailable case weights or degrees of freedom.
