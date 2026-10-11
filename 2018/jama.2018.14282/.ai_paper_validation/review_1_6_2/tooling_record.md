# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:39:59Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None. All supplied PDFs have usable native/layout extraction and reusable graphical pages; absent OCR and Office conversion do not affect coverage.

Probe output: preprocessing/tool_probe.json. CPU notification delivered before rendering/OCR. Direct derivative engines must be recorded in evidence_asset_inventory.md.

Current direct engine versions: Poppler pdfinfo/pdftotext/pdftoppm/pdftocairo 25.03.0; Pandoc 3.1.11.1; GNU coreutils sha256sum 9.7. Inventory found only PDFs, with usable native/layout coverage for all 144 source pages and reusable graphical pages. OCR and Office conversion are not required; no fallback environment was created.

Finalization UTC: 2026-10-11T07:52:17Z. Standalone HTML rendered with Pandoc 3.1.11.1 and embedded workflow CSS. `bootstrap_tooling.py remove` completed after rendering and reported an empty removal list: no temporary environment or package cache had been created. Fallback environment remains NOT_NEEDED; removal state NOT_CREATED. All targeted extraction and rendering derivatives use CPU and carry their engine records in evidence_asset_inventory.md. Source and reused-asset hashes were recomputed after Markdown assembly and are unchanged.
