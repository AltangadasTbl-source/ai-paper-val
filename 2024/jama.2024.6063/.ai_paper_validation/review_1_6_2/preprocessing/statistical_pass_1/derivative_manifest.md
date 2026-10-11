# Statistical pass 1 derivative provenance

Owner runtime01a129b5-1c4b-7ed3-955e-c6ca5e85d0b6. These are fresh source-derived aids; sources remain unchanged. Compute device CPU, no OCR. Text engine Poppler26.01.0 pdftotext -layout; image engine Poppler26.01.0 pdftoppm. Four generated images were visually inspected.

| Derivative | Exact supplied source scope | Engine and operation |
|---|---|---|
| main-p04-p07.txt | jama_laslett_2024_oi_240048_1727199125.7595.pdf physical pp4–7 | pdftotext -layout -f4 -l7 |
| result-p05-p07.txt | joi240048supp3_prod_1727199125.83025.pdf physical pp5–7 | pdftotext -layout -f5 -l7 |
| protocol-p08.txt | joi240048supp1_prod_1727199125.7845.pdf physical p8 | pdftotext -layout -f8 -l8 |
| protocol-p12.txt | joi240048supp1_prod_1727199125.7845.pdf physical p12 | pdftotext -layout -f12 -l12 |
| sap-p01.txt | joi240048supp2_prod_1727199125.8245.pdf physical p1 | pdftotext -layout -f1 -l1 |
| result-p02.txt | joi240048supp3_prod_1727199125.83025.pdf physical p2 | pdftotext -layout -f2 -l2 |
| main-p06.png | jama_laslett_2024_oi_240048_1727199125.7595.pdf physical p6 | pdftoppm -f6 -l6 -singlefile -scale-to2400 -png |
| result-p05.png | joi240048supp3_prod_1727199125.83025.pdf physical p5 | pdftoppm -f5 -l5 -singlefile -scale-to2600 -png |
| result-p06.png | joi240048supp3_prod_1727199125.83025.pdf physical p6 | pdftoppm -f6 -l6 -singlefile -scale-to2800 -png |
| protocol-p12.png | joi240048supp1_prod_1727199125.7845.pdf physical p12 | pdftoppm -f12 -l12 -singlefile -scale-to1800 -png |
| diagnostic_power.txt | Protocol p12 supplied power inputs | R4.5.2 base stats qnorm/pnorm/power.t.test; labelled diagnostic normal/t two-arm calculations, not asserted original method |

No fallback environment or global installation was used. No source, reusable asset or other agent's artifact was altered.
