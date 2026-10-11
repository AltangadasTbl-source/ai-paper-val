# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T04:55:09Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`; Python 3.14.4. All direct capabilities are available. Native/layout extraction uses Poppler; rendering uses Poppler on CPU; targeted OCR uses Tesseract on CPU. Every derivative records its engine in the evidence asset inventory or producing artifact. CPU processing was announced before rendering or OCR.

Direct engines verified: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0 with Leptonica 1.86.0; Pandoc 3.7.0.2; sha256sum uutils coreutils 0.10.0. LibreOffice is available but no Office sources require conversion.

Finalization: native SHA-256 recomputation matched all5 source and108 reused-asset before entries exactly; after manifests are preserved. Standalone HTML rendered with Pandoc3.7.0.2 using the approved renderer. The prescribed bootstrap_tooling.py remove command ran after rendering; no fallback environment had been created, so removal status remains NOT_CREATED. No GPU, new OCR, Office conversion or unapproved extraction helper was used.
