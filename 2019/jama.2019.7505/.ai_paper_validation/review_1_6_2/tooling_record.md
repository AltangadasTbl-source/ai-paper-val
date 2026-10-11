# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T04:55:46Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe: preprocessing/tool_probe.json. Native Poppler PDF tools, Tesseract CPU OCR, LibreOffice, Pandoc and sha256sum are available. CPU processing notification delivered before rendering or OCR.

## Direct engine versions

Poppler pdfinfo/pdftotext/pdftoppm: 26.01.0. Tesseract: 5.5.0 (CPU). Pandoc: 3.7.0.2. Version commands: pdfinfo -v; pdftotext -v; pdftoppm -v; tesseract --version; pandoc --version. Reusable PNG historical engines are unrecorded and disclosed in evidence_asset_inventory.md.

Final tooling check: bootstrap_tooling.py remove completed after HTML rendering; no fallback environment was created. Removal state remains NOT_CREATED. All current derivatives used the recorded direct tools on CPU.
