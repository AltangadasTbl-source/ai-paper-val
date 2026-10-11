# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T04:55:30Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** Legacy raster and some OCR engine versions are unrecorded; all affected pages have usable source-linked evidence and complete mapping.

Probe: python3 workflow_1_6_2/scripts/pdf_tools.py probe. Python 3.14.4; all direct required capabilities available. At the initial probe, no rendering or OCR had yet been performed. Subsequent CPU rendering and layout extraction are recorded below. CPU processing and optional user-requested GPU OCR were announced before processing.

New CPU derivatives recorded during numeric checking: direct Poppler pdftoppm rendered joi190108supp2_prod.pdf pp.4 and 7 to preprocessing/numeric-results-p4.png and preprocessing/numeric-results-p7.png. The numeric checker records exact commands and engine details. No fallback tooling or GPU was used. Legacy rasters and some OCR lack exact engine versions; source-linked text/raster comparison and direct-source confirmation maintain scientific coverage.

Mechanical evidence recheck produced 13 direct-source text/render derivatives using CPU Poppler pdftotext/pdftoppm 26.01.0. The exact paths, source units, commands and render parameters are recorded in verification/evidence_recheck.md and incorporated in evidence_asset_inventory.md. No OCR, Office conversion, fallback interpreter or GPU was used.

Finalization: direct source hashes (4) and reused derivative hashes (152) were recomputed and exactly match their before inventories. No fallback environment was created; the removal command returned an empty removed list after standalone HTML rendering. Compute remained CPU throughout. All generated derivative engine/source records are complete, and no scientific source unit is uncovered.
