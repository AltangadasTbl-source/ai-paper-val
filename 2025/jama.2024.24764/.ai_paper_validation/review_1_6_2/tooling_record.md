# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T16:07:51Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0
- **Fallback capabilities used:** info, text, render
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Linux direct PDF, OCR, and Office conversion tools are absent. The recorded fallback supplies PDF information, text, sorted reading order, and rendering. The initial singular venv path did not exist; the user corrected it to /home/juliz/venvs/stt/bin/python, which exists. Reusable OCR and native text are assessed first. Any residual page with unusable text must be inspected visually or processed with the installed GPU OCR engine.

## Probe and installation

The complete initial probe is stored in tool_probe.json. SHA-256 uses /usr/bin/sha256sum; HTML rendering uses /usr/bin/pandoc. Initial sandboxed package installation failed because network access was restricted. The authorized escalated retry succeeded with the exact pinned packages; tooling/bootstrap_log.json records READY and installed versions. No global Python installation was performed.

## GPU and PowerShell access

The user explicitly requested RTX 5070 GPU OCR through PowerShell 5.1 or PowerShell 7. Sandboxed nvidia-smi reports GPU access blocked, and sandboxed PowerShell reports a WSL socket failure. Authorized read-only checks outside the sandbox succeeded using /mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe, version 5.1.26100.9444. GPU: NVIDIA GeForce RTX 5070 Laptop GPU; Windows driver 616.56; WSL NVIDIA-SMI 615.65.06; CUDA driver capability 13.4. These checks establish access, rather than execution of GPU OCR. PowerShell 7 and a Windows tesseract executable were also located. No rendering or OCR has occurred during preflight.

The fallback PDF renderer runs on the CPU. GPU OCR will use the existing engine selected by the user's corrected environment path if required by page fitness. The user was notified before rendering or OCR. /home/juliz/venvs/stt/bin/python contains rapidocr-onnxruntime 1.4.4 and onnxruntime-gpu 1.28.0. The installed rapidocr_onnxruntime CLI exposes --det_use_cuda, --cls_use_cuda, and --rec_use_cuda. No installation into that existing environment is needed. GPU availability checks do not establish that OCR inference used CUDA; any actual OCR invocation must preserve provider diagnostics.

## Derivative engines

Mechanical recheck produced 39 current-run derivatives under preprocessing/recheck/: 18 exact-page native text files and 18 corresponding page images, plus full-document native text for the main article, results supplement and protocol. PyMuPDF 1.26.4 supplies native text and CPU 200dpi renders; every cited page was visually inspected. The complete source/page command access table is in verification/evidence_recheck.md. No OCR was necessary, and GPU OCR inference was not performed. The user's corrected existing environment remains unmodified.

Cross-source source confirmation produced preprocessing/cross_source/main-p4.txt, main-p8.txt, sap-p23-26.txt and protocol-p17.txt via the recorded fallback text command. Engine: PyMuPDF 1.26.4 native text. Exact scopes and commands are documented in checkers/cross_source_consistency.md. These are confirmation derivatives for reusable-backed pages, rather than new uncovered units.

DOC-002 PDF page 32's image-only assessment schedule was freshly rendered to preprocessing/support_mapper/DOC-002-p32.png using the recorded fallback helper render command, --page 32 --dpi 200, source joi240145supp1_prod_1741627844.87412.pdf. Engine: PyMuPDF 1.26.4 on the CPU. The mapper completed visual inspection and mapping of that source-derived image; this page sets the fresh-required count to one. No GPU OCR inference was needed or performed.

Specialists must record each derivative's command, source scope, and engine in their assigned artifact. Use .ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py for unavailable PDF capabilities only. PyMuPDF 1.26.4 produces information, native text, sorted reading order text, and page images. Sorted reading order text is not geometric pdftotext layout. Do not run CPU OCR without a recorded reason consistent with the user's requested GPU processing.

## Final cleanup

After standalone HTML rendering and before final validation, the supplied bootstrap_tooling.py remove command removed both the package-local fallback venv and its pip-cache. tooling/bootstrap_log.json retains the pinned installation record and exact removal UTC. Existing reusable evidence, new source-derived derivatives, and the user's /home/juliz/venvs/stt environment remain unchanged. No additional packages were installed into that existing environment. Rendering and source visual inspection completed every required unit; no fresh OCR or scientific-coverage limitation remains.
