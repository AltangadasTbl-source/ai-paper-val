# Local tooling record

- **Probe UTC:** 2026-10-11T06:39:32Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** Direct OCR and Office conversion unavailable; all supplied sources are PDFs with usable source-matched text and reusable raster-page images. All image-bearing units are assigned visual mapping; no fallback capability is needed. Historical derivative-engine metadata is partly absent and documented in evidence_asset_inventory.md.

Probe command: python3 workflow_1_6_2/scripts/pdf_tools.py probe. PDF information, text, rendering, and SHA-256 direct capabilities available. No fallback environment required by probe. Every derivative must record its engine.

Direct PDF suite: Poppler 25.03.0. HTML renderer: pandoc 3.1.11.1. Raw probe: tooling_probe.json. CPU processing was announced before rendering/OCR.

All newly produced text derivatives listed in coverage_manifest.md use direct pdftotext -layout, Poppler 25.03.0, CPU. All newly produced PNG derivatives there use direct pdftoppm PNG, Poppler 25.03.0, CPU. Exact source scopes are recorded per row and the producing specialist's artifact; recheck-C010-supp3-p8.png additionally uses 130 dpi. No OCR derivative was produced. Reused derivative engines remain truthfully unspecified where historical metadata is absent, as inventoried by the curator.

Final cleanup command: python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove. Result: {"removed": []}; no fallback environment or package cache was created, so removal state remains NOT_CREATED. Final rendering used the supplied render_report.py --profile 1.6.2 with Pandoc 3.1.11.1. Source and reused before/after hash inventories are byte-identical. Tooling finalized before mechanical validation.
