# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:38:56Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** OCR and Office conversion are unavailable. All 69 supplied PDF pages have usable native/layout text or readable CPU-rendered evidence; no supplied unit requires OCR or Office conversion. No scientific coverage gap remains.

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Python 3.13.5. Direct PDF information, native/layout text, rendering and SHA-256 capabilities are available. No fallback environment is required for these capabilities. CPU processing was announced before any rendering or OCR.

Direct tool versions: Poppler pdfinfo, pdftotext, and pdftoppm 25.03.0; Pandoc 3.1.11.1. The complete machine-readable probe is retained in tooling_probe.json.

Finalization: standalone HTML was rendered with the supplied render_report.py using direct Pandoc 3.1.11.1 after complete Markdown assembly. After rendering and before final validation, `python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove` confirmed the fallback environment was not present. No fallback installation, global package installation, OCR, or GPU processing occurred. All direct-source units are mapped; no unit is limited by a missing tool.
