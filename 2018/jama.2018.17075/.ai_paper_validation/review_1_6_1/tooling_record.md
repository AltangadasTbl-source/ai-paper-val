# Local tooling record

- **Probe UTC:** 2026-10-11T02:52:41Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** CPU OCR and Office conversion absent. All supplied sources are PDF; reusable OCR and rendered pages will be assessed, and any unusable native text will be covered visually from source-matched rendered pages. No scientific unit will be omitted.

Probe command: python3 workflow_1_6_1/scripts/pdf_tools.py probe. Direct PDF info, text, rendering and SHA-256 capabilities available; fallback environment not required. No GPU inspected or used.

Final review tooling summary: all four supplied sources were PDFs; no Office conversion was applicable. Direct native/layout tools, source-matched reusable page images, and targeted direct Poppler source rendering completed every unit and confirmed every candidate. No new OCR or fallback capability was used, no fallback environment was created, and no global packages were installed. Poppler25.03.0 engine and new derivative commands/locations are documented in evidence_asset_inventory.md and evidence_recheck.md. The absent CPU OCR tool leaves no scientific gap. HTML will use available local Pandoc and embedded workflow CSS; bootstrap removal and final validation are coordinator completion actions.
