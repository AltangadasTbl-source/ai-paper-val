# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T18:28:19Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** User-provided /home/juliz/venvs/stt/bin/python: pymupdf==1.28.0; pypdf==6.14.2; rapidocr-onnxruntime==1.4.4; onnxruntime-gpu==1.28.0
- **Fallback capabilities used:** info, render
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Direct PDF and OCR tools absent. User explicitly instructed use of the existing stt interpreter, overriding temporary-environment creation. Bundled pdf_tools.py is available through that interpreter for missing PDF capabilities. User-approved RapidOCR CUDA engine exercised successfully; four historical image-decoder gaps covered by direct source renders and visual mapping.

## Device access

The user explicitly requested RTX 5070 Laptop GPU access through PowerShell and authorized package installation in the existing stt environment. PowerShell requires execution outside the Linux sandbox due to WSL socket isolation; the read-only check succeeded through the approval reviewer. GPU: NVIDIA GeForce RTX 5070 Laptop GPU; driver 616.56; VRAM 8151 MiB. Ordinary PDF rendering uses CPU; fresh OCR will use the requested GPU when an approved engine is available. Reusable OCR is preferred.

## Probe

python3 workflow_1_6_2/scripts/pdf_tools.py probe recorded all direct PDF/render/OCR tools missing; pandoc and sha256sum available. The user-requested stt interpreter has the PDF and OCR modules above. No packages have been installed and no temporary environment has been created.

## Approved GPU OCR

User approved RapidOCR with CUDA in the session. Direct CLI engine: /home/juliz/venvs/stt/bin/rapidocr_onnxruntime (1.4.4), ONNX Runtime GPU 1.28.0, CUDA 13 libraries and cuDNN 9.24.0.43 already installed in stt. No package installation needed. The first two sandbox attempts fell back to CPU (recorded in their logs); adding the existing CUDA/cuDNN library paths and executing outside device isolation successfully selected CUDA without a CPU-fallback message. Successful probe: preprocessing/gpu_ocr/protocol-page-001-cuda-access.log. Production shell command and per-page engine logs are retained under preprocessing/gpu_ocr/. PowerShell 5.1 nvidia-smi independently confirmed the requested physical GPU. Source PDF rendering remains CPU; OCR runs on the approved GPU. CLI logs are reduced to quoted recognized lines using Perl solely as a transcription aid; exact source images remain authoritative.

## GPU OCR completion

Production CUDA CLI extraction completed all 90 protocol page-image attempts. Four images (PDF pp. 45, 54, 72, 73) could not be decoded and yielded no OCR text. Fresh direct source renders and complete visual transcription in mapper artifacts cover those four units; no source coverage remains absent. All other page outputs are recognized-text aids, with confidence/box coordinates preserved in the corresponding CLI log. CUDA-provider requests and runtime verification are in every log. No new packages or global-environment changes were made. This workflow intentionally does not repeat OCR for pages already covered by direct visual mapping.

## Tooling closeout

At 2026-10-11T19:51:41Z, after standalone HTML rendering and before final validation, the bundled bootstrap_tooling.py remove command completed with {"removed": []}. No package-local fallback environment was created, so its removal state remains NOT_CREATED. The user-provided stt environment was preserved. Rendering used the bundled report renderer with embedded CSS and a table of contents.
