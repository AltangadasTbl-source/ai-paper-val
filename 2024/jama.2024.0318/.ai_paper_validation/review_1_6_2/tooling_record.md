# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:36:12Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Python 3.14.4; direct PDF information, extraction, rendering, OCR, Office conversion, and SHA-256 capabilities available. Missing optional Python PDF/OCR modules do not affect direct capabilities. CPU processing was announced before rendering or OCR. Each newly produced derivative must record its direct engine in the evidence inventory or mapper provenance.

## Completed preprocessing provenance

All retained new derivatives use direct Poppler 26.01.0 on the CPU: 34 source-page PNGs (six mapping, four statistical pass 1, seven screening, fifteen recheck, two statistical pass 2) and eleven layout-text derivatives. Complete artifact/source-unit/engine rows are in evidence_asset_inventory.md; owning stage artifacts retain commands and resolutions. No new OCR, Office conversion, GPU engine, package installation, or fallback capability was used. Historical engine-version gaps are bounded in limitations.md. Source and reused-asset integrity checks reconfirm all four PDFs and all 234 reused assets unchanged.

Final tooling cleanup: `python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove` returned `{"removed": []}` after HTML rendering. No temporary environment was created or remained. The fallback removal field remains NOT_CREATED.
