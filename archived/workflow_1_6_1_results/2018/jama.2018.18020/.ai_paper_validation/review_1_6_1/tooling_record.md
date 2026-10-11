# Workflow 1.6.1 Tooling Record

- **Probe UTC:** 2026-10-11T02:52:51Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** CPU OCR and Office conversion are unavailable. PDF information, native/layout extraction and rendering are available directly; reusable page images and direct visual inspection cover any text ambiguity. Completed inventory found no Office or CSV source. All83 PDF pages are mapped; no source unit was affected by unavailable OCR or Office conversion.

Probe command: `python3 workflow_1_6_1/scripts/pdf_tools.py probe`.
All derivatives must record their direct tool and source locations. No global packages are installed.

Direct engines: Poppler `pdftotext` and `pdftoppm` 25.03.0; Pandoc 3.1.11.1. Source hashes use `sha256sum`. PDF metadata, extraction and rendering all use available direct tools.

Finalized after HTML rendering. Pandoc 3.1.11.1 rendered standalone HTML with embedded local CSS and table of contents. `python3 workflow_1_6_1/scripts/bootstrap_tooling.py remove` confirmed cleanup; no fallback environment was created or remains. Fallback environment removed stays NOT_CREATED. All13 new direct confirmation renders record Poppler25.03.0, exact source pages and commands in evidence_asset_inventory.md. No source unit required OCR or Office conversion. No global packages or provider configuration were changed.
