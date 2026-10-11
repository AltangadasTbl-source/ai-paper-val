# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T04:55:29Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Python 3.14.4; all required direct capabilities available. CPU rendering/OCR notice delivered before processing. Use direct Poppler, Tesseract, LibreOffice, Pandoc, and sha256sum tools; no fallback installation is required.

Direct versions confirmed: Poppler 26.01.0; Tesseract 5.5.0; Pandoc 3.7.0.2. Fresh text/layout and page derivatives must identify their engine in the evidence inventory or mapper artifact.

Final tooling state: COMPLETE. Direct CPU native/layout extraction and targeted Poppler page rendering supplied every required capability. Each saved derivative has source/engine provenance in its producing mapper, checker or recheck artifact; legacy engine uncertainty remains explicitly recorded. No new OCR, GPU processing, global installation or temporary fallback environment was required. Cleanup state is NOT_CREATED; there is no fallback environment to remove. Standalone HTML was rendered using the supplied render_report.py with available Pandoc 3.7.0.2. The supplied final validator reports PASS with no tooling limitation or warning.
