# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T16:08:08Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0
- **Fallback capabilities used:** info, render
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Direct Linux PDF and OCR executables are unavailable; the workflow-local temporary environment supplies PDF capabilities. The corrected shared interpreter /home/juliz/venvs/stt/bin/python supplies the existing RapidOCR CLI for requested GPU OCR. The first GPU smoke test omitted CUDA 13 libraries and fell back to CPU; the corrected library path loaded CUDA without a CPU fallback message. OCR remains a transcription aid subject to visual source confirmation.

The user explicitly requested RTX 5070 Laptop GPU OCR via PowerShell 5.1 or PowerShell 7. A read-only elevated PowerShell 5.1 check returned version 5.1.26100.9444 and the NVIDIA executable at C:\Windows\system32\nvidia-smi.exe. An elevated NVIDIA check returned NVIDIA GeForce RTX 5070 Laptop GPU, driver 616.56, 8151 MiB. The sandbox denied initial PowerShell interop and NVML access; elevated read-only checks succeeded. PDF inspection and rendering used CPU; user-requested GPU OCR completed for all 136 DOC-002 pages. All 104 fresh-required page images and 136 nonempty OCR transcription aids were recorded; no batch CPU-fallback message or traceback appeared.

The complete local-tool probe is recorded in tool_probe.json. Every derivative records its engine in the evidence asset inventory or its preprocessing log.

The corrected user-specified shared interpreter was inspected with its pip list command. Existing packages include numpy==2.5.1, onnxruntime==1.28.0, onnxruntime-gpu==1.28.0, opencv-python==5.0.0.93, pymupdf==1.28.0, pypdf==6.14.2, and rapidocr-onnxruntime==1.4.4. No packages were installed in this shared environment. PDF fallbacks remain pinned in the workflow-local temporary environment for reproducibility.

Fresh PDF rasters use pinned PyMuPDF 1.26.4 via pdf_tools.py, CPU, 170 dpi. The 104 uncovered DOC-002 pages were rendered; 32 selected reusable page images cover the remainder. RapidOCR 1.4.4 is invoked through PowerShell 5.1 -> wsl.exe -> its installed CLI with detection, classification and recognition CUDA flags, at two concurrent page processes. Existing CUDA 13 and cuDNN 9 libraries are selected through LD_LIBRARY_PATH; nothing was installed in the shared environment. The GPU batch writes one log, plain-text transcription, and provenance record per DOC-002 page. Perl transcribes the CLI's logged text fields without scientific interpretation. A live NVIDIA check during OCR reported 1435 MiB of GPU memory in use and 9% utilization. No CPU-fallback message appeared in the corrected smoke-test log; ONNX Runtime's plugin-device warning remains recorded in raw logs.

## Final derivative and environment closure

All 136 DOC-002 OCR outputs are nonempty and all104 fresh-required page rasters are recorded in preprocessing/fresh_derivative_inventory.md; page-specific logs and engine provenance are retained. Missing OCR lines were recovered through complete source-image mapping and direct mechanical recheck. No tooling limitation leaves a scientific source unit uncovered. Final source and reused-asset hash comparisons are PASS in integrity_checks.md.

After standalone HTML rendering, bootstrap_tooling.py remove was run with /home/juliz/venvs/stt/bin/python. It removed only this run's tooling/venv and tooling/pip-cache. The bootstrap log remains as provenance. The existing shared interpreter, GPU toolkit, all supplied sources and every reused or historical audit artifact remain unchanged. The fallback environment is absent; rendering used the supplied report renderer with local Pandoc and embedded CSS.
