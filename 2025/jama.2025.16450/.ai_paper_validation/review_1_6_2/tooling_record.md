# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T18:29:08Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0; rapidocr-onnxruntime==1.3.24 (complete dependency versions in tooling/bootstrap_log.json)
- **Fallback capabilities used:** info, text, layout, render
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** PDF/OCR direct commands absent; use workflow fallback helper. Rendering uses CPU. User explicitly approved RapidOCR with CUDA for OCR. GPU access requires approved unsandboxed execution.

Probe output: tooling_probe.json. Approved PowerShell 5.1 and WSL checks identify NVIDIA GeForce RTX 5070 Laptop GPU, driver 616.56, 8151 MiB. Sandboxed GPU access and Windows interoperation were unavailable; the approved check succeeded. Existing user interpreter /home/juliz/venvs/stt/bin/python has rapidocr-onnxruntime 1.4.4, onnxruntime-gpu 1.28.0, PyMuPDF 1.28.0, and pypdf 6.14.2. Do not install globally. Record actual OCR provider and any CPU fallback for each derivative.

GPU OCR command: preprocessing/run_gpu_ocr.sh calls the installed RapidOCR CLI with --det_use_cuda --cls_use_cuda --rec_use_cuda, using the user-requested stt interpreter through its console entry point. CUDA 13 libraries and cuDNN 9 are supplied by existing environment paths. Three independent CPU fallback warnings occurred in the initial CUDA-12-path test and are preserved in gpu-ocr-test.log; the CUDA-13 retry and production logs report no CPU fallback. A PowerShell nvidia-smi observation during production recorded RTX 5070 utilization 67% and GPU memory 4460 MiB. Raw CLI logs and faithful string transcriptions are stored side by side for each page. OCR strings are locators; source images/pages remain authority.

Production preprocessing completed: 245 PLAN pages have page-scoped RapidOCR CUDA output records and raw bounding-box/confidence logs, indexed in preprocessing/gpu_ocr/derivative_manifest.md. Three unusable reusable renders (protocol pages 23 and 27; manual page 119) were preserved and replaced for current reading by fresh source-PDF renders with PyMuPDF 1.26.4 CPU, followed by successful GPU OCR retries. Source-page mapping closes all 241 fresh-required units; four readable PLAN units were also OCR-transcribed as overlap. Targeted source confirmation in checker, screening and verification artifacts uses the recorded CPU renderer and does not change the GPU OCR device record. Native-font encoding and reusable-image limitations are resolved by complete visual mapping; no affected unit remains scientifically uncovered.

Blank-source handling: DOC-003 PDF page 153 is genuinely blank and is explicitly mapped as such. A nonempty derivative file containing provenance headers is not evidence of source text on that page; the OCR attempt and blank visual inspection close the unit without inventing content.

Final cleanup: the allowed bootstrap remove helper removed the package-local fallback venv and pip-cache after standalone HTML rendering. Removal UTC: 2026-10-11T19:55:10Z. tooling/bootstrap_log.json is retained. The existing user stt environment is preserved. All missing direct capabilities were supplied by the recorded helper or approved CUDA OCR; no source unit remains uncovered.
