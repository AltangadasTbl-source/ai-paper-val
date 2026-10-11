# Tooling Record

- **Probe UTC:** 2026-10-11T02:52:40Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** OCR and Office conversion tools are unavailable. All five sources are PDFs; native extraction, reused or fresh page rendering, and visual inspection covered every unit. No source unit required OCR or Office conversion, and no scientific coverage gap remains.

Probe command: python3 workflow_1_6_1/scripts/pdf_tools.py probe. Full result: tool_probe.json. Poppler pdfinfo/pdftotext version 25.03.0; Pandoc 3.1.11.1. All processing is local CPU.

Mapping closure:94/94 pages;86 reusable-backed and8 fresh-required protocol pages. Fresh text/layout/render derivatives used direct Poppler25.03.0; no fallback capability was used or environment created. Current-source page confirmations by later specialists use the same recorded direct tools. Tooling finalization requires no global installs, GPU access or conversion.
