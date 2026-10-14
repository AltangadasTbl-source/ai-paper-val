# Tooling Record

- **Probe UTC:** 2026-10-11T18:29:13Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** pymupdf==1.26.4; pypdf==5.9.0
- **Fallback capabilities used:** info, text, layout, render
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Direct PDF information, text, rendering and OCR executables were absent. The recorded package-local PDF fallback and user-approved RapidOCR CUDA engine completed all required extraction and confirmation; no scientific source-unit gap remains. Some reused derivatives do not retain their original engine versions.

The user requested RTX 5070 GPU OCR through Windows PowerShell 5.1 or PowerShell 7 and the existing ~/venvs/stt/bin/python. The recorded probe and tooling bootstrap use that interpreter; the workflow fallback helper uses its temporary package-local interpreter. Packages are not installed globally. Probe output: preprocessing/tool_probe.json. Fresh OCR was restricted to the 26 protocol pages whose font-mapped native text was unreadable, after reusable assets and native extraction were assessed.

PowerShell read-only GPU check succeeded outside the sandbox: NVIDIA GeForce RTX 5070 Laptop GPU, driver 616.56, 8151 MiB. Engine: Windows nvidia-smi via powershell.exe -NoProfile -NonInteractive. Initial sandbox launch could not access the WSL interoperability socket. No fresh CPU OCR was used.

GPU OCR engine approved by user: RapidOCR with ONNX Runtime CUDA. Existing interpreter: /home/juliz/venvs/stt/bin/python, RapidOCR 1.4.4, ONNX Runtime GPU 1.28.0; no GPU packages installed for this run. Direct CLI invocation is used because the supplied fallback OCR helper supports CPU only. Execution: Windows PowerShell 5.1 -> wsl.exe -> existing Python RapidOCR CLI with --det_use_cuda --cls_use_cuda --rec_use_cuda. GPU-library search includes existing NVIDIA Python package libraries and /usr/lib/wsl/lib. CPU render engine: PyMuPDF 1.26.4 at 200 dpi. Source scope: DOC-002 pp. 1–26, where font-mapped native text is unreadable. Raw bounding boxes/confidences and timing remain in per-page GPU OCR logs; a Perl formatter copies strings to per-page text without scientific selection. Commands: preprocessing/gpu-ocr.sh, preprocessing/protocol-gpu-batch.sh, preprocessing/ocr-log-to-text.pl. The user explicitly authorized the GPU OCR engine and existing interpreter.

DOC-002 GPU OCR finished for every page 1–26. All 26 plaintext transcriptions are nonempty. Post-run local rg inspection of all 26 raw logs found no automatic CPU-shift, unavailable-CUDA-provider, CUDA initialization or library-load failure. RapidOCR's existing engine verifies that CUDA is the first actual session provider and logs an automatic-shift warning otherwise. ONNX Runtime emitted plugin-registration warnings but no provider-shift warning. Initial GPU batch's internal rg check was unavailable in the Windows-launched WSL PATH; the complete equivalent check was performed after the batch from the recorded local environment, and the script now uses grep for portability. No OCR was rerun. Windows GPU process snapshot alone did not identify WSL sessions; it is retained as diagnostic provenance, not proof of provider selection. No scientific source-unit limitation remains from this tooling condition.

Temporary package-local PDF fallback removed after standalone HTML rendering and before final validation. Removal UTC: 2026-10-11T19:25:18Z. The existing user-managed stt environment is retained.
