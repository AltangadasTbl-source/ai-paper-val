# Workflow 1.6.1 Tooling Record

- **Probe UTC:** 2026-10-11T02:44:22Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: python3 workflow_1_6_1/scripts/pdf_tools.py probe. Python 3.14.4; all required direct capabilities available. Use direct CPU tools and record derivative engines and commands in evidence_asset_inventory.md. No global installation or GPU use.

Finalization: all direct capabilities remained available. Poppler PDF tools 26.01.0; Tesseract 5.5.0 (leptonica 1.86.0); Pandoc 3.7.0.2; SHA-256 uutils coreutils 0.10.0. HTML rendered through the bundled renderer with Pandoc. The mandated bootstrap removal command returned an empty removed list because no fallback environment was created. No temporary environment remains. Source-confirmation derivative commands and engines are recorded in evidence_asset_inventory.md and the producing stage artifacts. No tooling-related source unit remains uncovered.
