# Local tooling record

- **Probe UTC:** 2026-10-11T02:45:53Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Command: `python3 workflow_1_6_1/scripts/pdf_tools.py probe`. Python 3.14.4; all required direct capabilities available. CPU-only direct tools will be used and engines/commands documented in evidence assets. No fallback environment was created.

## Final tooling status

Report rendered with the supplied render_report.py using direct Pandoc 3.7.0.2 and embedded workflow CSS. Direct Poppler 26.01.0 provided all fresh native/layout and targeted page-render confirmation. Direct GNU sha256sum produced both after-hash manifests; each compares byte-identically to its before manifest. After HTML rendering, `python3 workflow_1_6_1/scripts/bootstrap_tooling.py remove` returned `{"removed": []}`: no fallback environment or package cache was created or remains. Tooling status is complete; no tool-related source unit is unresolved.
