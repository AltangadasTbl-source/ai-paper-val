# Tooling Record

- **Probe UTC:** 2026-10-11T06:39:46Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** No supplied unit depends on unavailable OCR or Office conversion. All132PDF pages have source-matched reusable text; graphical or encoded text is covered visually with reused images or direct CPU rendering. Legacy OCR and image engine metadata limitations remain recorded in the evidence inventory.

Probe command: python3 workflow_1_6_2/scripts/pdf_tools.py probe. Python 3.13.5; direct PDF information, text, rendering and SHA-256 tools available. No temporary environment is needed for PDF processing.

## Direct engine versions

- PDF information, native/layout extraction and CPU rendering: Poppler 25.03.0 (pdfinfo, pdftotext, pdftoppm).
- Hashing: sha256sum, GNU coreutils 9.7.
- HTML rendering backend available: Pandoc 3.1.11.1.
- No Office source supplied. All 132 PDF pages have source-matched reusable text; rendered figures provide visual confirmation. No unit depends on unavailable OCR or Office conversion.

Current-run derivatives use direct Poppler25.03.0 on CPU: one numeric-check PLAN p36 image, three whole-source layout locators, four independent-screen PLAN images (pp16/63/64/67), and one support-audit REPORT p7 image. Exact commands/source units are recorded in the evidence asset inventory and assigned stage artifacts. No OCR or Office derivative was needed.

Final tooling removal check: python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove completed after HTML rendering; no temporary environment existed and the helper reports no removed paths. Removal state remains NOT_CREATED; the durable result is tooling_removal.json. Standalone HTML was rendered by bundled render_report.py using Pandoc3.1.11.1; no fallback or GPU processing was used.
