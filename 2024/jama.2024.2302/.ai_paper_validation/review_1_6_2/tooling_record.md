# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:36:57Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Python 3.14.4; direct tools under /usr/bin. All required direct capabilities were available. CPU processing was announced before rendering or OCR. Each producer records the engine and source locations for its derivatives. No global packages are installed.

Direct tool version checks: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0; LibreOffice 26.2.6.3; Pandoc 3.7.0.2. LibreOffice's version query emitted a dconf read-only-cache notice; conversion has not been required.

Completion: standalone HTML was rendered with the supplied report renderer and direct Pandoc. The prescribed `python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove` returned `{"removed": []}`: no fallback environment had been created, and no tooling virtual environment remains. Fallback environment removed remains NOT_CREATED. All rendering and OCR used CPU; no GPU was requested or used. No direct-tool or installation limitation remains.
