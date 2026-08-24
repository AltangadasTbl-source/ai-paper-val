# Workflow 1.5.2 Run State

- **Profile:** 1.5.2
- **Status:** COMPLETE
- **Target basis:** Three supplied PDFs comprise 44 fresh page units (10-page main article plus 25-page and 9-page supplements), with native and layout extraction, visual result-page review, parallel relationship mapping, and two full statistical passes required; preferred Linux PDF tools are absent, adding a bounded local-tool fallback burden.
- **Total source units:** 44
- **Fresh-source units:** 44
- **Target elapsed minutes:** 30-60
- **Started UTC:** 2026-08-24T00:16:27Z
- **Finished UTC:** 2026-08-24T01:15:46Z
- **Observed elapsed minutes:** 59.3
- **Target status:** MET_TARGET
- **Exceedance causes:** None
- **Evidence basis:** Supplied package sources only; legacy audit derivatives excluded.
- **Runtime limitations:** Preferred Linux `pdfinfo`, `pdftotext`, rendering, and Tesseract commands were not found in PATH. Installed local Acrobat automation supplied native page text and coordinate-layout evidence for all 44 pages; no result-relevant page required OCR after text-usability assessment.
- **Unresolved checks:** Scientific relationship mapping and consistency review remain in progress.

## Stage Status

| Stage | Status | Notes |
|---|---|---|
| source_inventory | COMPLETE | Three direct research PDFs identified and hashed; 44 PDF pages total. |
| evidence_assets | COMPLETE | Fresh native and coordinate-layout evidence exists for all 44 pages. |
| coverage_planning | COMPLETE | Every source page and required stage has a disjoint assignment. |
| quantitative_mapping | COMPLETE | 61 numeric/reporting and 67 statistical relationships mapped across all pages. |
| consistency_review | IN_PROGRESS | Numeric, statistical pass 1, and cross-source lanes starting concurrently. |
| candidate_registration | COMPLETE | 11 distinct candidates assigned C001-C011 after one genuine duplicate merge. |
| evidence_recheck | COMPLETE | All C001-C011 mechanically rechecked; C004 source transcription corrected while its stable ID remains preserved. |
| evidence_quality | COMPLETE | All C001-C011, 44 source units, 61 N relationships, 67 S relationships in both passes, coverage rows, and manifested agents audited; correctable link/transcription defects repaired before reporting. |
| report_generation | COMPLETE | All 11 candidate cards assembled in canonical order. |
| validation | COMPLETE | Standalone HTML rendered; Workflow 1.5.2 validator reports PASS with no errors. |
