# Workflow 1.6 Tooling Record

- **Probe UTC:** 2026-10-11T00:34:52Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6/scripts/pdf_tools.py probe`. Complete result: `tool_probe.json`. Direct tools will be used for all PDF information, extraction, rendering, OCR, Office conversion if applicable, and hashing. No global packages or GPU operations are required.

## Actual engines and finalization

- Direct native/layout extraction: pdftotext, Poppler 26.01.0.
- Direct targeted page rendering: pdftoppm, Poppler 26.01.0.
- Available CPU OCR: Tesseract 5.5.0; no new OCR was required.
- HTML engine: Pandoc 3.7.0.2 through the supplied report renderer.
- Hashing: direct sha256sum; before/after source and reuse lists identical.
- Scientific source-unit gaps: None; all 96 mapped.
- No temporary environment was created; removal check follows HTML rendering.

Engine and exact derivative provenance are recorded in each mapper/checker/recheck artifact. Historical unknown derivative versions remain disclosed; their files are preserved unchanged.

Final removal command: python3 workflow_1_6/scripts/bootstrap_tooling.py remove; returned an empty removed list because no fallback environment or cache was created. Fallback environment removed remains NOT_CREATED. Tooling record complete.
