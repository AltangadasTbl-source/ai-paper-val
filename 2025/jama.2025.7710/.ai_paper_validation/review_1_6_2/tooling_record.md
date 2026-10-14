# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T16:08:09Z
- **Platform:** Linux / WSL with Windows PowerShell 5.1 interoperation
- **Direct tools available:** sha256sum=yes; file=yes; pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0
- **Fallback capabilities used:** info, text, layout, render
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Direct PDF tools were absent; the prescribed package-local PDF fallback supplied every needed capability. All 72 source units were mapped, with no scientific coverage gap. Legacy extraction/render/OCR engine versions are unknown. Windows PowerShell required execution outside the sandbox because WSL interoperation was unavailable inside it; this did not limit source inspection. No Office sources or fresh OCR were needed.

## Probe and fallback provenance

The prescribed workflow_1_6_2/scripts/pdf_tools.py probe produced preprocessing/tool_probe.json. workflow_1_6_2/scripts/bootstrap_tooling.py create installed the temporary environment only under this run's tooling directory. The bootstrap log records floor-spec retries and pin_substituted=true; its pip_freeze confirms actual installed versions PyMuPDF1.26.4 and pypdf5.9.0. No global installation was performed. The package-local recorded interpreter and permitted pdf_tools.py helper supplied PDF information, native/layout text and CPU page rendering, because the corresponding direct commands were absent. Engine/version and derivative locations are recorded in source inventories, evidence maps, and specialist artifacts.

After standalone HTML rendering, the prescribed bootstrap_tooling.py remove command succeeded. The temporary tooling/venv and tooling/pip-cache directories were removed; bootstrap_log.json remains as durable package and cleanup provenance.

## Explicit GPU request and engine approval

The user requested GPU OCR on the RTX5070 Laptop GPU, corrected the interpreter to /home/juliz/venvs/stt/bin/python, and explicitly approved RapidOCR with CUDA. A read-only Windows PowerShell5.1 check outside the sandbox confirmed NVIDIA GeForce RTX5070 Laptop GPU and driver616.56. The corrected existing environment contains rapidocr-onnxruntime1.4.4 and onnxruntime-gpu1.28.0 with CUDA packages; no packages were installed into it.

Compute device GPU_USER_REQUESTED records this authorization. Existing source-linked OCR/native/layout assets plus fresh native extraction and direct visual page inspection provided complete evidence, so no new OCR or GPU inference was run. All actual PDF text extraction and page rendering ran on CPU using PyMuPDF1.26.4. No derivative is attributed to a GPU engine that was not executed. Any necessary fresh OCR would use the approved RapidOCR CUDA CLI with detection/classification/recognition CUDA flags and recorded provider verification through the authorized PowerShell/WSL route; no such run was necessary.
