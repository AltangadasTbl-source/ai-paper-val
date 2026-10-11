# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:37:19Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`; complete result: preprocessing/tool_probe.json. Direct PDF information, native/layout text, page rendering, OCR, Office conversion, and SHA-256 capabilities are available. Rendering/OCR CPU notification was given in the session before processing. New derivatives must record their direct engine and source units in the evidence-asset inventory. No global installation or fallback environment is needed.

Direct engine versions: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0; Pandoc 3.7.0.2; sha256sum (uutils coreutils) 0.10.0. No new rendering, OCR, or conversion was required during curation. Reused text fitness was checked using current direct pdftotext output streamed to cmp; no derivative was created for those comparisons.

Scientific mapping directly rendered DOC-002 PDF p. 6 with pdftoppm Poppler 26.01.0 at 120 dpi on CPU to inspect an embedded mediation figure. Command and derivative are recorded in evidence_asset_inventory.md. No OCR was needed.

Independent inclusion screening used current-source pdftotext layout rereads and two targeted 120-dpi CPU pdftoppm renderings, DOC-001 p. 3 and DOC-003 p. 14. New derivatives and direct engines are recorded in evidence_asset_inventory.md. No OCR/fallback was used.

Finalization: all source and reused-asset after-hashes were recomputed with direct sha256sum and match their baseline files byte for byte. Evidence recheck, both statistical passes and quality audit used direct source reads without additional derivatives. The local report renderer uses available Pandoc with embedded workflow CSS. No fallback environment was ever created; the prescribed remove command is a no-op cleanup check.
