# Workflow 1.6 Tooling Record

- **Probe UTC:** 2026-10-11T00:43:40Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** OCR and Office conversion are unavailable. All four supplied files are PDFs; all69 pages have usable native/layout text or complementary readable page images. Both mapping lanes completed all pages without OCR or conversion. No source unit is affected by these absent tools.

Probe engine: workflow_1_6/scripts/pdf_tools.py probe, Python 3.13.5. No packages installed. Derivative engine requirements: direct Poppler pdfinfo/pdftotext/pdftoppm/pdftocairo, SHA-256 via sha256sum. CPU only. If a fallback becomes necessary it will use a temporary local environment, respecting the user's instruction.

Recorded versions: Poppler pdfinfo and pdftotext25.03.0; Pandoc3.1.11.1. Historical derivative versions are explicitly unrecorded except old pdfinfo metadata26.01.0. New targeted stdout reads use direct Poppler25.03.0; new page renders, if required for recheck, use direct pdftoppm25.03.0 and their source pages/commands are recorded in the recheck artifact. No environment or global package installation was needed.

Exact-source recheck generated four direct layout derivatives and three PNGs using Poppler25.03.0; paths, commands, DPI, source pages and engines are individually recorded in evidence_asset_inventory.md and verification/evidence_recheck.md. These confirmation derivatives are new run outputs. No tooling coverage limitation remains.

The distinct appended-ID rechecker generated three targeted layout texts and three source-page PNGs under preprocessing/recheck_append, all with direct Poppler25.03.0. Exact commands and visual confirmation for mainp7, resultsp6 and protocolp12 are recorded in verification/parts/evidence_recheck_append.md and merged into canonical recheck; every derivative is inventoried. No fallback or installed package was used.

Final cleanup check: after standalone HTML rendering, ran the supplied bootstrap_tooling.py remove helper at 2026-10-11 01:26:39 UTC. Output: {"removed": []}. No environment or package cache had been created; removal state remains NOT_CREATED. Rendering used the supplied render_report.py with profile1.6 and direct Pandoc3.1.11.1, embedded CSS and local-only links.
