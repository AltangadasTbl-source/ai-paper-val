# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:37:03Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Direct PDF information, text, rendering, OCR, Office conversion, and SHA-256 capabilities are available. CPU processing was announced before any rendering or OCR. Use direct tools and record their engines with derivatives. No global installation is permitted or needed.

Direct engine versions confirmed: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0 with Leptonica 1.86.0; Pandoc 3.7.0.2. Rendering and OCR device: CPU. Version probes are operational checks and do not consume supplied-source content.

Exact supplied-distribution calculations in statistical pass 1 used local Rscript 4.5.2 (2025-10-31), with qbeta/pbeta for the stated beta inputs and qnorm/exp for the stated normal prior. These reproduce printed distribution definitions only; no empirical posterior, GEE fit, or Monte Carlo realization was substituted. Engines, input sources and results are recorded in statistics/relationship_inventory.md and checkers/statistical_pass_1.md.

## Final tooling closure

Complete Markdown was rendered, then refreshed after mechanical validation repairs with workflow_1_6_2/scripts/render_report.py using available Pandoc3.7.0.2. The standalone HTML embeds CSS and a table of contents; no external asset is required. The required bootstrap_tooling.py remove command returned an empty removed list because no fallback environment was created. Final fallback environment removed: NOT_CREATED. Rendering, direct source checks and defined-distribution calculations remained on CPU; no OCR or GPU was used. Source and reused-artifact after hashes match every before entry.
