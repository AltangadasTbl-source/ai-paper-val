# Tooling Record
- **Probe UTC:** 2026-10-11T02:46:34Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe: `python3 workflow_1_6_1/scripts/pdf_tools.py probe`. All required capabilities are direct CPU tools; no environment installation is needed.

Direct versions: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0; Pandoc 3.7.0.2; LibreOffice 26.2.6.3. LibreOffice version probing printed a read-only dconf notice; no Office sources or conversion are required, so coverage is unaffected.

Final removal check: `python3 workflow_1_6_1/scripts/bootstrap_tooling.py remove` returned an empty removal list because no fallback environment was created. Fallback environment removed remains NOT_CREATED. Final direct-tool derivatives and versions are fully cross-linked in evidence_asset_inventory.md and each producing artifact; no unresolved tooling limitation remains.
