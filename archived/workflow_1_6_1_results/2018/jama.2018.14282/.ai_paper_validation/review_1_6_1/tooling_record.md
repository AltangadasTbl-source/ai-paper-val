# Local Tooling Record

- **Probe UTC:** 2026-10-11T02:52:45Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** OCR and Office conversion unavailable; all 144 supplied PDF units were covered with usable native/layout text and targeted direct renders. No Office source exists and no OCR or fallback installation was required.

Probe command: python3 workflow_1_6_1/scripts/pdf_tools.py probe. Python 3.13.5. Direct hashing engine: /usr/bin/sha256sum. Direct PDF engines: /usr/bin/pdfinfo, /usr/bin/pdftotext, /usr/bin/pdftoppm, /usr/bin/pdftocairo. HTML renderer: /usr/bin/pandoc. No GPU operations or global installation.

Inventory confirms all four sources are PDF and all 144 pages have usable native text. No OCR or Office conversion is required. Text/info/render engine version: Poppler 25.03.0; Pandoc 3.1.11.1. Optional rendered-asset gaps are covered by text or direct rendering when confirmation is needed.

During scientific checking, independent screening and mechanical recheck, targeted confirmation text/render derivatives were generated with Poppler25.03.0 and recorded individually in evidence_asset_inventory.md and their owning artifacts. Statistical pass2 reused the durable confirmations and produced no new preprocessing derivative.

Final standalone HTML rendered with the supplied render_report.py and Pandoc. The supplied bootstrap_tooling.py remove command completed; no environment or cache existed and no fallback installation was attempted. No temporary environment remains. Source and reused-artifact after hashes match their before records.
