# Local Tooling Record

- **Probe UTC:** 2026-10-11T02:45:51Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: python3 workflow_1_6_1/scripts/pdf_tools.py probe. Direct PDF information, text, rendering, OCR, Office conversion, and SHA-256 capabilities are available. Use direct CPU tools; no GPU operations. Final cleanup and tooling completion recorded below.

Direct tool versions: pdfinfo, pdftotext and pdftoppm 26.01.0 (Poppler); tesseract 5.5.0; pandoc 3.7.0.2. New derivatives retain their engine/command/source location in the evidence-asset inventory and producing-stage artifacts. No new OCR has been used.

HTML initially rendered after complete Markdown and timing stabilization using the bundled render_report.py and direct Pandoc 3.7.0.2. A second render follows the validator-required explicit pass-1 ID-record repair and refreshed timing. The bundled bootstrap_tooling.py remove command was then executed; it returned an empty removed list because no fallback environment had been created. Fallback environment removed remains NOT_CREATED. Direct tools covered every source unit; no tooling limitation remains. Mechanical validation uses the supplied validate_review.py only.
Tooling finalized UTC: 2026-10-11T03:21:28Z
