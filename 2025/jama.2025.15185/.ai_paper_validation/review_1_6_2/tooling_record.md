# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T08:35:32Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`.
All direct capabilities (PDF information, extraction, rendering, OCR, Office conversion, SHA-256) are available. Python 3.14.4; no fallback modules are needed. CPU processing was announced before rendering or OCR. Derivative engines and commands are recorded in the evidence-asset inventory and extraction artifacts.

Direct engine versions: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0 (CPU); Pandoc 3.7.0.2.
