# Workflow 1.6.2 tooling record

- **Probe UTC:** 2026-10-11T18:28:32Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0
- **Fallback capabilities used:** info, text, layout, render
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Direct PDF and OCR tools are absent. PDF information, native text, sorted reading-order text, and CPU rendering use the bundled pdf_tools.py helper with tooling/venv/bin/python. The initial package installation was blocked by sandbox network restrictions; the authorized installation outside the sandbox succeeded. GPU access and Windows PowerShell startup require execution outside the sandbox.

The user explicitly requested the RTX 5070 laptop GPU through PowerShell 5.1 or PowerShell 7 and the existing `/home/juliz/venvs/stt/bin/python` environment. PowerShell 5.1.26100.9444 and NVIDIA GeForce RTX 5070 Laptop GPU, driver 616.56, were confirmed outside the sandbox. Reuse and native extraction were checked before targeted OCR. Rendering uses the CPU. The user's existing environment contains PyMuPDF 1.28.0, pypdf 6.14.2, rapidocr-onnxruntime 1.4.4, and onnxruntime-gpu 1.28.0; it was used to run the probe and bootstrap. Workflow PDF derivatives use the pinned temporary environment. No global environment was modified.

Probe output: tool_probe.json. Installation details: tooling/bootstrap_log.json. Final capability and removal fields are complete.

Targeted SAP pp. 5-6 OCR completed through PowerShell 5.1 invoking the existing stt Python in WSL. Engine: rapidocr-onnxruntime 1.4.4 with onnxruntime-gpu 1.28.0, requested CUDA on detection/classification/recognition. An initial p. 5 attempt used CPU after a missing CUDA library path; reruns used a process-local path to existing CUDA13/cuDNN9 libraries and completed without the engine's CPU-shift warning. Actual CUDA use is inferred from the engine's session-provider verification; the full commands, logs and limitation are in preprocessing/gpu_ocr/engine_record.md. No package installation was needed for OCR. Rendering remains CPU.

Temporary package-local fallback venv and pip cache were removed after standalone HTML rendering and before final validation by the supplied bootstrap_tooling.py remove command, using the authorized stt interpreter. Removal UTC: 2026-10-11T19:41:13Z. The bootstrap log and all derivative provenance remain preserved. No shared/global environment was changed.
