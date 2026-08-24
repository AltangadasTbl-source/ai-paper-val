# Workflow 1.5.2 Run State

- **Target basis:** Four PDFs with 69 fresh-required pages (11-page main article and 58 support pages), fewer source units than the 102-page calibration package but with complete source-access limitation documentation required because native-text, rendering, and CPU OCR executables are unavailable.
- **Total source units:** 69
- **Fresh-source units:** 69
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-24T00:18:52Z
- **Finished UTC:** 2026-08-24T00:41:30Z
- **Observed elapsed minutes:** 22.6
- **Target status:** MET_TARGET
- **Exceedance causes:** None

## Runtime and review state

- **Workflow profile:** 1.5.2
- **Coordinator:** COORDINATOR-CURRENT-SESSION
- **Current stage:** Markdown assembled; local accounting, rendering, and validation
- **Direct sources identified:** 4 PDF files
- **Legacy audit derivatives used as evidence:** No
- **Internet/external literature used:** No
- **Runtime tool limitation:** `pdfinfo`, `pdftotext`, `pdftoppm`, `pdftocairo`, `tesseract`, `libreoffice`, and `soffice` were not found on PATH; all 69 PDF pages lack permissible fresh scientific text/layout/render/OCR derivatives. `file`, `sha256sum`, and `pandoc` were found.
- **Unresolved relationship escalation:** None
- **Accounting window:** Closed at Finished UTC
