# Workflow 1.5.2 Run State

- **Profile:** 1.5.2
- **Review status:** COMPLETE
- **Target basis:** Four supplied PDFs totaling 80 pages: a 12-page main article, two text-rich support PDFs totaling 41 pages, and a 27-page support PDF with 14 source-hash-matched existing OCR pages. Fresh scientific mapping is required for all 80 pages; no new OCR is permitted by the user. Scope is smaller than the 102-page calibration package but includes multi-document tables and two independent statistical passes.
- **Total source units:** 80
- **Fresh-source units:** 80
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-24T00:26:03Z
- **Finished UTC:** 2026-08-24T01:03:39Z
- **Observed elapsed minutes:** 37.6
- **Target status:** MET_TARGET
- **Exceedance causes:** None
- **OCR handling:** User-authorized reuse of source-hash-matched OCR under `.ai_paper_validation/preprocessing/joi170166supp3_prod/`; no CPU or GPU OCR will be run in this review.
- **Tool limitation and repair:** Required Poppler commands were absent from PATH. Matching Ubuntu packages were downloaded and extracted under `/tmp/qc15-poppler`; commands are invoked directly with its local library path. No package source or audit artifact was modified.
- **Open issues:** None. Quality-audit repairs were completed before report assembly.
