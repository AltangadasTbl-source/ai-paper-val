# Workflow 1.6 Local Tooling Record

- **Probe UTC:** 2026-10-11T00:34:38Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6/scripts/pdf_tools.py probe`. Python 3.14.4; direct tools in `/usr/bin/`. PDF info/text/render, CPU OCR, Office conversion, and SHA-256 capabilities are available. No fallback modules are needed or installed. Poppler pdfinfo/pdftotext 26.01.0; Tesseract 5.5.0; Pandoc 3.7.0.2. Use direct local tools and record derivative engines in the asset inventory. Never invoke legacy Python extraction scripts or GPU diagnostics.

Finalization: standalone HTML rendered with the supplied Pandoc-backed helper; removal command completed with an empty removed list because no fallback environment was created. The environment is absent; NOT_CREATED is the final removal state. Current-run PDF derivatives used direct CPU Poppler tools; no new OCR or GPU invocation occurred.
