# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T04:53:35Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Python 3.14.4; all required direct capabilities available. Direct SHA-256 tool: /usr/bin/sha256sum. PDF text and rendering use Poppler; OCR, when needed, uses Tesseract CPU. No fallback environment will be created.

Direct versions: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0; Pandoc 3.7.0.2. Every new derivative records its engine and exact source scope in the evidence map or asset inventory.

## Final tooling closure

Complete Markdown was rendered once to standalone HTML using the supplied render_report.py helper and Pandoc 3.7.0.2. The supplied bootstrap_tooling.py remove command returned an empty removed list: no fallback environment or package cache had been created. Fallback environment removed remains NOT_CREATED. All processing used CPU; no fresh OCR, installation, or tool-related scientific limitation occurred.
