# Tooling Record

- **Probe UTC:** 2026-10-11T02:46:18Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_1/scripts/pdf_tools.py probe`. All PDF information, text, layout, rendering, hashing, CPU OCR, Office conversion and report rendering capabilities are available directly. No global packages are installed.

## Final tooling verification

All direct tooling remained available throughout source inventory, mapping, checking, source recheck and audit. Engines and exact derivative locations are recorded in evidence_asset_inventory.md. The standalone HTML renderer was invoked after complete Markdown assembly with profile 1.6.1. The bundled `bootstrap_tooling.py remove` check returned an empty removal set because no fallback environment was created; removal field remains NOT_CREATED. No global installation, network source, GPU or unapproved Python extraction was used. The bundled final validator is the final mechanical quality-control check.
