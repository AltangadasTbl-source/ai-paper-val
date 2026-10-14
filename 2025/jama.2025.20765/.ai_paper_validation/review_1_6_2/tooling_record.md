# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T18:29:03Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** pymupdf==1.26.4; pypdf==5.9.0; rapidocr-onnxruntime==1.3.24
- **Fallback capabilities used:** info, text, layout, render
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Initial sandbox installation failed; the authorized elevated retry succeeded with all pinned packages. GPU access requires elevated execution under WSL. No source unit is omitted for tool availability.

The user explicitly requested the RTX 5070 Laptop GPU through PowerShell 5.1 or PowerShell 7 and the `/home/juliz/venvs/stt/bin/python` interpreter, then expressly approved RapidOCR with ONNX Runtime CUDA. Elevated read-only `powershell.exe -NoProfile -NonInteractive -Command 'nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv,noheader'` and WSL `nvidia-smi` both identify NVIDIA GeForce RTX 5070 Laptop GPU, driver 616.56, 8151 MiB. Rendering uses the CPU. Existing usable extraction takes precedence; only targeted OCR was run.

GPU OCR uses the existing `/home/juliz/venvs/stt/bin/rapidocr_onnxruntime` console command (the requested interpreter), RapidOCR ONNX Runtime 1.4.4 / ONNX Runtime GPU 1.28.0, with `--det_use_cuda --cls_use_cuda --rec_use_cuda`. Its existing CUDA 13 and cuDNN 9 libraries are exposed with a command-local library path. Successful targeted output exists for DOC-002 PDF pp. 10 and 80 under `preprocessing/gpu_ocr/DOC-002/`, with raw bounding-box/score logs and plain-text locators. The page-80 execution snapshot records the RTX 5070 at 57% GPU utilization and 5016 MiB used. Initial page-29 trial lacked the library path and automatically ran on the CPU; that log is preserved and is not presented as GPU output. The repeatable shell wrapper and raw logs preserve execution details without any custom Python extraction script.

The standard probe output is preserved in `preprocessing/tool_probe.json`. The user-selected existing interpreter reports PyMuPDF 1.28.0, pypdf 6.14.2, RapidOCR ONNX Runtime 1.4.4, and ONNX Runtime GPU 1.28.0. It was used to invoke the bundled bootstrap script, which successfully created the package-local fallback interpreter at `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python`. No package has been installed globally or into the existing user environment. Only the bundled auxiliary scripts are permitted for PDF extraction and rendering.

New CPU render: DOC-002 PDF p. 13, PyMuPDF 1.26.4 at 200 dpi, preprocessing/support001_p013.png; source clipping was confirmed directly.

The bundled bootstrap removal command removed the package-local fallback interpreter and package cache after HTML rendering. Bootstrap provenance and all evidence derivatives remain preserved. Source and reused-artifact SHA-256 lists are unchanged between the before and after checks.
