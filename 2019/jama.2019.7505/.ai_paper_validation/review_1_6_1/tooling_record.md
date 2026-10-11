# Tooling record

- **Probe UTC:** 2026-10-11T02:44:50Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_1/scripts/pdf_tools.py probe`. All required direct capabilities are available. Native/layout extraction and rendering use Poppler; OCR, if required, uses Tesseract CPU. SHA-256 uses sha256sum. No global installation, fallback environment, or GPU is required.

## Direct tool versions

- Poppler pdfinfo/pdftotext: 26.01.0
- Tesseract: 5.5.0; Leptonica 1.86.0
- Pandoc: 3.7.0.2
- Tool probe interpreter: Python 3.14.4 (auxiliary workflow helpers only)

## Lifecycle

All direct capabilities available; fallback creation is not needed. Derivative engines and source scopes are recorded by their producers. Final removal check completed with the bundled bootstrap_tooling.py remove helper after HTML rendering; it returned removed: [] because no fallback environment was created. Fallback lifecycle remains NOT_CREATED.
