# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T04:55:19Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. All PDF, hashing, OCR, and Office capabilities are available directly. CPU processing was announced before rendering or OCR. New derivatives must record their direct engine and source units; reusable derivatives retain their provenance. No global packages will be installed.

Final processing record: current-run direct Poppler 26.01.0 text/layout and source-page rendering completed on CPU; no fresh OCR, Office conversion, GPU operation or package installation was needed. Source-confirmation derivative engines and locations are documented in the new evidence asset inventory and specialist artifacts. No fallback environment was created. Standalone report rendering uses the bundled renderer with local Pandoc; the removal check runs before final validation.
