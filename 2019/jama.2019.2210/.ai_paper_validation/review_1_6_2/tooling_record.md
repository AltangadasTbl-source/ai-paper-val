# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T04:55:10Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe engine: Python 3.14.4, bundled pdf_tools.py probe. Complete probe output: preprocessing/tool_probe.json. Current source extraction and page rendering used available direct Poppler tools on CPU; no new OCR was required. Hashing used direct sha256sum. The coordinator notified the user before rendering or OCR. Derivative engines and source locations are recorded in the evidence asset inventory and mapper artifacts. Final tooling verification is complete: HTML was rendered with the bundled report renderer using available Pandoc, and the bundled bootstrap_tooling.py remove check returned an empty removed list because no fallback environment was created. No temporary venv remains. All four source and381 reused-asset hashes match their before manifests exactly.
