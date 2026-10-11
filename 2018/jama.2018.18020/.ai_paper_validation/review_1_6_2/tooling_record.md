# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:39:38Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** Historical extraction/render engine versions are unrecorded. OCR and Office conversion are unavailable; no Office sources exist, and all graphical PDF content is covered by reusable renders plus visual mapping. No affected unit remains uncovered.

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Python 3.13.5; direct tools are in /usr/bin. PDF fallback is not needed. Rendering and OCR CPU policy was communicated before processing.

Verified direct PDF engine: Poppler 25.03.0 (`pdftotext -v`). No fresh rendering or OCR was needed for initial mapping. Source fitness was checked with current direct pdfinfo/pdftotext/cmp/file/sha256sum; historical images and source-matched text are reused unchanged. Any targeted source confirmation derivatives will record direct engine, command and source unit in their metadata.

Targeted confirmation: direct Poppler 25.03.0 CPU rendering was used for two protocol diagrams, two independent screen renders/crops, and 29 recheck pages. Exact per-derivative commands and locations are in evidence_asset_inventory.md, screening/inclusion_screen.md and preprocessing/recheck/derivative_record.md. No OCR, Office conversion, GPU or fallback capabilities were used.

Finalization: direct sha256sum recomputed all four source and 108 reusable-asset hashes; both after inventories match the before inventories. Supplied render_report.py uses local Pandoc with bundled embedded CSS. Supplied bootstrap_tooling.py remove confirms no fallback environment was created; removal state remains NOT_CREATED. Final validation uses the supplied validate_review.py helper.
