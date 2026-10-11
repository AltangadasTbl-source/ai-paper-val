# Mechanical Recheck Derivative Record

Every file is newly derived from its exact supplied source using direct Poppler on CPU. Existing source-matched evidence was also reread independently. No OCR or fallback was used. Commands are `pdftotext -layout SOURCE OUTPUT` for complete text and `pdftoppm -f N -l N -singlefile -png SOURCE OUTPUT_PREFIX` for selected pages; the producing evidence recheck records the source/engine/device.

| Artifact | Exact source scope | Engine / device |
|---|---|---|
| preprocessing/evidence_recheck/main-full.txt | DOC-001 PDF pp. 1-11 | Poppler pdftotext -layout 26.01.0 / CPU |
| preprocessing/evidence_recheck/plan-full.txt | DOC-002 PDF pp. 1-33 | Poppler pdftotext -layout 26.01.0 / CPU |
| preprocessing/evidence_recheck/supp-full.txt | DOC-003 PDF pp. 1-19 | Poppler pdftotext -layout 26.01.0 / CPU |
| preprocessing/evidence_recheck/sharing-full.txt | DOC-004 PDF p. 1; report-wide absence check | Poppler pdftotext -layout 26.01.0 / CPU |
| preprocessing/evidence_recheck/plan-32.png | DOC-002 PDF p. 32 model equations | Poppler pdftoppm 26.01.0 / CPU |
| preprocessing/evidence_recheck/main-8.png | DOC-001 PDF p. 8 table/figure columns | Poppler pdftoppm 26.01.0 / CPU |
| preprocessing/evidence_recheck/supp-17.png | DOC-003 PDF p. 17 biomarker plot content | Poppler pdftoppm 26.01.0 / CPU |
