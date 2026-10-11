# Local tooling record

- **Probe UTC:** 2026-10-11T06:36:44Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Python 3.14.4. All requested direct capabilities available: PDF information, text, rendering, OCR, Office conversion, and SHA-256. Python modules fitz, pypdf, and rapidocr_onnxruntime absent; direct tools supply these capabilities. Executables are under /usr/bin. No global packages installed. CPU processing was announced before preprocessing.

Direct tool versions: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; tesseract 5.5.0 (Leptonica 1.86.0); LibreOffice 26.2.6.3; pandoc 3.7.0.2. Derivative commands, engines, and source locations are recorded in evidence_asset_inventory.md and the mapping artifacts.
Completion tooling check at 2026-10-11 08:07:44 UTC: standalone HTML rendered with supplied render_report.py using Pandoc 3.7.0.2. Supplied bootstrap_tooling.py remove returned {"removed": []}; no temporary environment was created and no tooling/venv remains. Compute device remained CPU. No new OCR, Office conversion, GPU processing or fallback installation occurred. Final source/reused hashes were recomputed with GNU sha256sum and compared byte-for-byte with cmp; both sets match.
