# Workflow 1.6 Tooling Record

- **Probe UTC:** 2026-10-11T01:09:20Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6/scripts/pdf_tools.py probe`; JSON retained in preprocessing/tool_probe.json. Python 3.14.4; Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; tesseract 5.5.0; pandoc 3.7.0.2. All source operations use direct CPU-only tools. No Python installation is required. No global environment changes or GPU operations are authorized or performed.
