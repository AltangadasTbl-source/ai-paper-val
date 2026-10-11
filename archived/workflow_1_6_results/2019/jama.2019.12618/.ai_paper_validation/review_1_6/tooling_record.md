# Workflow 1.6 Tooling Record

- **Probe UTC:** 2026-10-11T01:05:51Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6/scripts/pdf_tools.py probe`. Python 3.14.4. All direct capabilities are available; missing optional Python PDF modules do not require installation. Use direct Poppler text/layout/rendering, Tesseract CPU OCR, and sha256sum. Record derivative engines and commands in the evidence inventory. No environment or global package installation is needed.

Direct engine versions: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0 (Leptonica 1.86.0); Pandoc 3.7.0.2. No temporary environment created.
