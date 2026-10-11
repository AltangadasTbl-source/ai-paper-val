# Workflow 1.6.1 Tooling Record

- **Probe UTC:** 2026-10-11T02:52:33Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** CPU OCR and Office conversion unavailable; PDF native/layout extraction and rendering available. Any unreadable text will be inspected visually. No Office sources are supplied. All 69 PDF pages have usable source-matched text; figures have rendered-page support. No OCR is currently needed.

Probe command: python3 workflow_1_6_1/scripts/pdf_tools.py probe. Raw output: preprocessing/tool_probe.json.

Direct tool versions: Poppler pdfinfo/pdftotext/pdftoppm/pdftocairo 25.03.0; Pandoc 3.1.11.1. Source derivative engines and exact coverage are recorded in evidence_asset_inventory.md.

Final tooling state: all supplied sources are PDFs and all source units were covered using usable text and visual page evidence. No OCR, Office conversion or fallback installation was necessary. Final rendering uses the supplied render_report.py with Pandoc 3.1.11.1; final validation uses the supplied validate_review.py. Temporary-environment cleanup is checked after rendering.

Cleanup command completed: bootstrap_tooling.py remove returned an empty removed list; no temporary fallback environment was created or remains. Fallback environment removed: NOT_CREATED.
