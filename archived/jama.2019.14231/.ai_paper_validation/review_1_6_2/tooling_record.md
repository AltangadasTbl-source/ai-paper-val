# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T04:55:26Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe: python3 workflow_1_6_2/scripts/pdf_tools.py probe; Python 3.14.4. All direct tools resolve under /usr/bin; PDF info/text/render, OCR, Office conversion, and SHA-256 are available. No global packages were installed. CPU processing notification was given before processing.

Direct engine versions: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0 with Leptonica 1.86.0; Pandoc 3.7.0.2. New extraction/rendering derivatives must name their direct engine and CPU device in the evidence inventory or derivative log.

Final tooling check: the prescribed bootstrap_tooling.py remove command completed after HTML rendering with no environment or package cache to remove. No temporary fallback environment was created or remains. All new derivatives record Poppler 26.01.0 / CPU in their owning artifacts and the evidence-asset inventory. No new OCR, GPU processing, or global installation was used.
