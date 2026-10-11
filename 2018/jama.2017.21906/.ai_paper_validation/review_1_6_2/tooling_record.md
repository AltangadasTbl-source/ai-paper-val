# Workflow 1.6.2 Local Tooling

- **Probe UTC:** 2026-10-11T06:39:56Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** Direct OCR and Office conversion were unavailable. All sources were PDFs; source-matched reused OCR plus current-source visual inspection covered scanned text. No fresh OCR, Office conversion, fallback installation or scientific coverage gap remained.

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Direct PDF information, native/layout text, rendering, and SHA-256 tools are available. CPU processing was announced before rendering. Engine provenance for each derivative belongs in evidence_asset_inventory.md.

Scientific processing completed with native/layout Poppler extraction and CPU page rendering, plus unchanged source-matched reusable OCR. Historical derivative engine/device provenance is recorded separately in evidence_asset_inventory.md and does not describe this run's compute device. No temporary fallback environment was created. Final cleanup confirmation will follow HTML rendering.

Final cleanup after HTML rendering: `python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove` returned an empty removed list. No environment or package cache had been created; Fallback environment removed remains NOT_CREATED. Direct CPU engines completed every required operation; no scientific coverage gap remains.
