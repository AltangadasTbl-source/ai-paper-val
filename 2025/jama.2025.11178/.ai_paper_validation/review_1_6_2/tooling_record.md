# Tooling Record

- **Probe UTC:** 2026-10-11T08:19:01Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe engine: python3 3.14.4 running workflow_1_6_2/scripts/pdf_tools.py probe. All direct capabilities are available. New PDF text uses Poppler pdftotext; page information uses pdfinfo; rendering uses pdftoppm/pdftocairo; targeted OCR uses Tesseract CPU. Office structure may use the permitted bundled helper. No global packages are installed.

Direct engine versions: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0; LibreOffice 26.2.6.3; Pandoc 3.7.0.2. LibreOffice version probe emitted a read-only dconf-cache notice; the executable returned its version successfully. Any Office conversion uses a run-local profile where needed.
