# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T16:07:56Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0
- **Fallback capabilities used:** info, text, layout, render
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Direct PDF and OCR utilities were absent; the pinned bundled fallback supplied PDF inspection and CPU page rendering. No scientific coverage gap remains. User corrected the requested environment to /home/juliz/venvs/stt/bin/python; it exists and contains an existing GPU-capable OCR engine.

Probe output: preprocessing/tool_probe.json. Python 3.12.3; system PyMuPDF and pypdf are available. No global installation is authorized by the workflow.

Windows PowerShell 5.1.26100.9444 is accessible after a sandbox escalation for the read-only hardware check. NVIDIA GeForce RTX 5070 Laptop GPU, driver 616.56, confirmed through Windows nvidia-smi. Initial sandboxed WSL GPU and Windows interoperability checks were blocked; the escalated Windows check succeeded. GPU use is requested by the user, who selected an existing GPU OCR engine. The corrected environment contains rapidocr-onnxruntime==1.4.4 and onnxruntime-gpu==1.28.0; this existing engine is selected if fresh OCR becomes necessary. No GPU OCR ran. All current PDF rendering ran on CPU. Existing packages in the requested environment require no installation; pinned PDF fallback packages remain package-local.

Current-run direct confirmation derivatives use the pinned fallback PyMuPDF 1.26.4. The protocol mapper confirmed protocol pp.48–51 to preprocessing/protocol-mapper-statistical-native.txt. Statistical pass1 produced preprocessing/statistical1-main.txt (main1–8), statistical1-protocol.txt (protocol48–51), statistical1-sap.txt (SAP3–9), statistical1-results.txt (results2–15); all text only. The protocol confirmation was duplicated before the coordinator's reuse reminder; these read-only derivative operations do not alter scientific scope or the source. Numeric and cross-source checker text/render derivatives are documented in their durable checker artifacts. CPU rendering is used for exact-source confirmation; no new OCR has run.

Independent recheck produced preprocessing/recheck-main-p6.png and preprocessing/recheck-results-p9.png using pinned PyMuPDF 1.26.4 CPU rendering for exact Table2 blank cells and the raster sensitivity footnote. No fresh OCR ran. The screener and rechecker also streamed targeted protocol text through the pinned helper without retaining an additional derivative. All current-run engine/page/command details are retained in their evidence artifacts.

After standalone HTML rendering, bootstrap_tooling.py remove removed the temporary venv and package cache; the exact removal UTC is retained in tooling/bootstrap_log.json. The user-requested /home/juliz/venvs/stt/bin/python was used for the bundled report renderer, cleanup helper and final validator. No package was installed in that existing environment. Source hashes and all 296 reused-asset hashes remained unchanged at final recomputation. All 119 supplied pages have complete scientific mapping; new OCR was unnecessary.
