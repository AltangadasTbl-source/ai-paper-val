# Tooling Record

- **Probe UTC:** 2026-10-11T16:08:36Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0
- **Fallback capabilities used:** info, render, text, layout
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Direct PDF tools absent; the pinned package-local helper supplies PDF information, native/sorted text and page rendering. PLAN native glyph encoding is unusable, so source-linked reusable OCR and readable source renderings govern transcription. Windows PowerShell GPU probe succeeds outside sandbox; sandboxed invocation fails with WSL socket access restriction. User-corrected ~/venvs/stt/bin/python exists with Python 3.12.3. RTX 5070 Laptop GPU confirmed, 8151 MiB, driver 616.56. No fresh OCR was required or performed; complete scientific mapping covers all 115 pages.

Rendering and native PDF extraction use CPU. The session announced CPU processing before rendering. The user's explicit GPU OCR request is preserved in the compute-device field; no OCR operation was necessary, so no OCR engine or GPU computation was executed. Probe output is preprocessing/tool_probe.json. GPU probe command: powershell.exe -NoProfile -NonInteractive -Command 'nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv,noheader'.

User correction: ~/venvs/stt/bin/python exists (Python 3.12.3) with PyMuPDF 1.28.0, pypdf 6.14.2, rapidocr-onnxruntime 1.4.4 and onnxruntime-gpu 1.28.0. No packages were installed into that environment. The initial sandboxed bootstrap failed because DNS/network access was blocked; the authorized unsandboxed retry installed the pinned temporary PDF packages successfully. Missing direct PDF tools are covered by the supplied helper using the package-local interpreter. All fresh text and rendering derivatives record PyMuPDF 1.26.4, CPU, in evidence_asset_inventory.md and their originating specialist artifacts. Reused OCR and rendering engine-version limits are recorded separately. No CPU OCR has been performed.

Finalization: standalone HTML was rendered with the bundled render_report.py and local Pandoc. The bundled bootstrap_tooling.py remove command then removed both tooling/venv and tooling/pip-cache; tooling/bootstrap_log.json preserves the exact removal UTC. No fallback interpreter remains. All 115 scientific source units are complete, no fresh OCR was required, and all decisive derivatives record their actual CPU PDF engine. Source and reused-artifact after-hash files are byte-identical to their before records.
