# Workflow 1.6.1 Tooling Record

- **Probe UTC:** 2026-10-11T02:52:30Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None affecting coverage. OCR and Office conversion are unavailable; the package contains only PDFs, all scanned quantitative material has source-linked reusable images/OCR, and fresh page134 was visually inspected with direct Poppler rendering. No fresh OCR or Office conversion was required.

Probe engine: python3 3.13.5 running workflow_1_6_1/scripts/pdf_tools.py probe. Direct binaries: /usr/bin/pdfinfo, /usr/bin/pdftotext, /usr/bin/pdftoppm, /usr/bin/pdftocairo, /usr/bin/pandoc, /usr/bin/sha256sum. CPU-only. No fallback capability is required by the probe.

Direct-tool version checks: pdfinfo 25.03.0; pdftotext 25.03.0; pdftoppm 25.03.0; pandoc 3.1.11.1. SHA-256 uses the available /usr/bin/sha256sum. Derivatives must record Poppler native/layout extraction or Poppler rendering as appropriate.

Fresh derivative: preprocessing/support_final/DOC-002-p134.png, from joi180004supp1_prod.pdf physical page134; direct CPU Poppler pdftoppm 25.03.0 with -f134 -l134 -singlefile -r100 -png, visually inspected by support-final mapper. Empty body with dated SAP header/footer; no OCR required. Current run reuses archived OCR outputs without invoking their historical engine or GPU.

Later direct confirmation derivatives use Poppler25.03.0 only: inclusion screener's page renders110dpi and layout extraction; rechecker's seven additional unique REPORT page renders90dpi (mainp7 110dpi). Source-page mappings, command patterns and filenames are recorded in evidence_asset_inventory.md, screening/inclusion_screen.md and verification/evidence_recheck.md. Native/reused page renders were not needlessly repeated by the rechecker.

Final tooling closure: the standalone report was rendered with the bundled render_report.py helper and direct Pandoc 3.1.11.1. After HTML rendering, python3 workflow_1_6_1/scripts/bootstrap_tooling.py remove completed successfully and returned {"removed": []}; no temporary fallback environment had been created and none remains. Fallback status remains NOT_NEEDED and removal status NOT_CREATED.
