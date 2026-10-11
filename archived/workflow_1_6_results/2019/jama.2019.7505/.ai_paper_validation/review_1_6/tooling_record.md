# Workflow 1.6 Tooling Record

- **Probe UTC:** 2026-10-11T00:34:50Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6/scripts/pdf_tools.py probe`. Exact output is retained in tooling_probe.json. Direct local tools cover all required PDF, OCR, Office, and hashing capabilities. No global packages or GPU are used. No temporary fallback environment is needed.

## Direct engine versions

- PDF information, native/layout text, and rendering: Poppler 26.01.0 (`pdfinfo`, `pdftotext`, `pdftoppm`, `pdftocairo`).
- CPU OCR: Tesseract 5.5.0, Leptonica 1.86.0.
- Office conversion: LibreOffice 26.2.6.3.
- HTML renderer backend: Pandoc 3.7.0.2.
- Source and reusable-artifact hashes: sha256sum, uutils coreutils 0.10.0.
- Probe and permitted workflow helpers: Python 3.14.4.

Version commands were executed locally on 2026-10-11T00:36:09Z. The mere presence of CPU instruction detection in Tesseract output does not invoke a GPU.

## Final tooling closure

After HTML rendering, the prescribed `python3 workflow_1_6/scripts/bootstrap_tooling.py remove` command completed successfully. No fallback environment had been created; removal state remains NOT_CREATED. All extraction/recheck/rendering used recorded direct local CPU tools. Sources and reused derivatives were preserved, and the temporary fallback path is absent.
