# Workflow 1.6.1 Tooling Record

- **Probe UTC:** 2026-10-11T02:52:26Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None; all native-text PDF units were fully mapped with available direct extraction and visual rendering. OCR and Office conversion were not required.

Probe command: `python3 workflow_1_6_1/scripts/pdf_tools.py probe`. Python 3.13.5. All required PDF capabilities and direct hashing are available. No global packages installed and no GPU invoked.

Direct tool versions: Poppler pdfinfo/pdftotext/pdftoppm 25.03.0; Pandoc 3.1.11.1. The package contains only native-text PDFs, so absent OCR and Office conversion do not currently affect coverage.

Final tooling status: all49 source pages mapped. No fallback environment was created. After standalone HTML rendering, `python3 workflow_1_6_1/scripts/bootstrap_tooling.py remove` confirmed an empty removed list; no environment or local package cache remains. Direct Poppler extraction/rendering, sha256sum and Pandoc supported the completed workflow. Tooling record finalized before mechanical validation.
