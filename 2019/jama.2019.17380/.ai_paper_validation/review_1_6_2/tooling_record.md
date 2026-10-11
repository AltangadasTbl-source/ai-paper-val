# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T04:55:20Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Python 3.14.4; all direct capabilities available. Direct tools resolve under `/usr/bin/`. SHA-256 uses `sha256sum`. The session notified the user of CPU processing before rendering or OCR. Every new derivative records its direct engine in its producing artifact.

Finalization: Direct Poppler 26.01.0 produced all new text/layout confirmations and targeted page renders on CPU. Exact source windows, output paths and producing engines are recorded in evidence_asset_inventory.md and the individual screening/recheck/pass-2 derivative records. No OCR or Office conversion was required. Direct Pandoc rendered the completed standalone HTML through the supplied render_report.py helper. After rendering, `python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove` returned `{"removed": []}`; no fallback environment or local package cache had been created, so removal remains NOT_CREATED. Four direct-source and 63 reused-asset after-hash entries match their before manifests byte-for-byte.
