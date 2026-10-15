# Tooling Record

- **Probe UTC:** 2026-10-14T16:23:10Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0; rapidocr-onnxruntime==1.3.24
- **Fallback capabilities used:** info, text, layout, render, ocr
- **Fallback environment removed:** YES
- **Compute device:** CPU
- **Tooling limitations:** Direct PDF/OCR/Office executables unavailable; pinned fallback PDF tools are available. Fresh OCR will cover source units without eligible earlier-workflow evidence. No Office conversion is needed for the supplied workbook.

Probe: workflow_1_6_2/scripts/pdf_tools.py probe; Python 3.12.3. sha256sum and Pandoc available. CPU rendering announced before processing. User authorized RapidOCR on RTX 5070 Laptop with ~/venvs/stt/bin/python if needed; pwsh is absent here. No GPU execution succeeded; the later compatibility test is recorded below.

User-directed restart: prior Workflow 1.6.2 derivatives and preserved snapshot deleted; no such asset will be reused. Fallback recreated with pinned RapidOCR CPU for fresh gaps. The user-approved GPU was probed through nvidia-smi, which reported operating-system GPU access blocked; no GPU OCR was executed. CPU fallback and visual source inspection remain available. No provider or validator change was made.

Temporary RapidOCR CPU runtime configuration: intra-op threads=2; inter-op threads=1, set only in the package-local environment's YAML to bound parallel OCR resource use. Model/package code and pinned versions are unchanged; the entire environment will be removed after rendering.

GPU compatibility check: an authorized read-only nvidia-smi probe outside the restricted sandbox identified NVIDIA GeForce RTX 5070 Laptop GPU, driver616.56. User's existing ~/venvs/stt RapidOCR1.4.4/onnxruntime-gpu1.28.0 CLI was tested on one freshly rendered protocol page. CUDA execution could not load libcublasLt.so.13 (CUDA13 runtime dependency); the engine reported CPU fallback. No GPU OCR ran. This compatibility log is tooling provenance, excluded from scientific extraction. Fresh scientific OCR uses pinned package-local RapidOCR1.3.24 CPU. No system/user environment was modified.

Finalization: Scientific Markdown assembled and timing finalized; standalone HTML rendered through supplied renderer/Pandoc. Temporary package-local venv and pip-cache removed with the provided bootstrap remove helper; tooling/bootstrap_log.json retains removal UTC and pinned package provenance. Compute device remained CPU for all scientific derivatives. All147sourceunits are scientifically mapped; no tooling-related scientific coverage gap remains.
