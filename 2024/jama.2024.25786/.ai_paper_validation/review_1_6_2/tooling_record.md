# Workflow 1.6.2 Local Tooling

- **Probe UTC:** 2026-10-11T06:36:30Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Direct information, text, rendering, OCR, Office conversion, and SHA-256 capabilities are all available. No fallback installation is required. CPU processing and the option to request GPU OCR were communicated before rendering or OCR.

All derivative producers record their tool, source scope, command, and output in their artifacts or the evidence asset inventory.

## Direct tool versions

- Poppler pdfinfo, pdftotext, and pdftoppm: 26.01.0.
- Tesseract: 5.5.0; Leptonica: 1.86.0; CPU SIMD/OpenMP capabilities reported.
- Pandoc: 3.7.0.2.
- Version probe commands: `pdfinfo -v`, `pdftotext -v`, `pdftoppm -v`, `tesseract --version`, `pandoc --version`.

## Final local closeout

After complete Markdown assembly, direct `sha256sum` recomputed all five supplied-source and all 58 reused-artifact hashes. The before/after files compare identically with `cmp`. New native text and renders remain below the permitted review preprocessing tree, with their Poppler engine and CPU device recorded in the producing artifacts. No OCR or Office conversion was needed.

The bundled `render_report.py --profile 1.6.2` rendered the complete Markdown using available Pandoc 3.7.0.2 and the bundled stylesheet, producing standalone HTML with embedded CSS and a table of contents. The cleanup command `python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove` returned `{"removed": []}`: no fallback environment or package cache had been created, and none remains. Fallback environment removed stays `NOT_CREATED`.

After the first validation requested individually serialized pass-1 IDs, the coordinator expanded the existing records mechanically and refreshed the report timing. HTML was rendered again solely to carry that finalized closeout metadata; all source evidence and candidate cards remain unchanged.
