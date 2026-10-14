# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T16:08:30Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0
- **Fallback capabilities used:** info, text, layout, render
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Direct PDF tools and CPU OCR absent; the temporary pinned fallback supplied all missing PDF capabilities. The user's corrected /home/juliz/venvs/stt/bin/python initiated successful bootstrap. No new OCR was needed. All 86 source pages were mapped, including visual coverage of every encoded SAP page; no scientific coverage gap remains.

The probe JSON is preprocessing/tool_probe.json. The first sandboxed installation failed because network package access was restricted; preprocessing/bootstrap_first_attempt.json preserves that log. An approved retry using /home/juliz/venvs/stt/bin/python completed successfully with the exact workflow pins; tooling/bootstrap_log.json records installed versions. After standalone HTML rendering, the bundled removal helper removed tooling/venv and tooling/pip-cache. System Python 3.12.3 has fitz and pypdf, but fallback use followed the bundled bootstrap contract.

GPU access was checked after a sandbox-restricted PowerShell probe failed. An approved read-only probe outside the sandbox confirmed Windows PowerShell 5.1.26100.9444, Windows nvidia-smi, and NVIDIA GeForce RTX 5070 Laptop GPU with driver 616.56 and 8151 MiB. Rendering used CPU. GPU OCR was explicitly requested by the user; no new OCR was necessary and no GPU OCR engine was selected or executed. The corrected environment has onnxruntime-gpu==1.28.0, PyMuPDF==1.28.0, and pypdf==6.14.2; PDF helpers for this review used the package-local exact pins. No global packages were installed. Every new PDF derivative's engine is recorded in evidence_asset_inventory.md; reusable engines lacking historical metadata are explicitly identified. Pandoc rendered standalone HTML with embedded workflow CSS and a table of contents.
