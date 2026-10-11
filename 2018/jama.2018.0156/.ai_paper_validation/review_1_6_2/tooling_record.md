# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:38:44Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** OCR and Office conversion are unavailable directly. All direct sources are PDFs. DOC-002 p52, pp108–109, and pp126–133 are covered by reusable source-matched OCR and images; p134 is covered by a readable reusable image. No fresh-required unit needs OCR or conversion. Native PDF information, text, layout, rendering, and SHA-256 capabilities are available.

Probe command: python3 workflow_1_6_2/scripts/pdf_tools.py probe. Python 3.13.5. Direct executables reside under /usr/bin. The helper reported fallback_environment_needed=false. CPU processing was announced before rendering or OCR. No GPU was requested.

Direct versions confirmed: pdfinfo, pdftotext, and pdftoppm use Poppler 25.03.0; Pandoc is 3.1.11.1. Targeted derivatives must record the executable and source units in their mapping artifacts.

Final cleanup: after standalone HTML rendering and before validation, python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove completed. No fallback environment was created; no temporary fallback environment remains. Fallback environment removed: NOT_CREATED. Final HTML uses the direct Pandoc 3.1.11.1 engine with embedded CSS and a table of contents. No new OCR or GPU processing occurred.
