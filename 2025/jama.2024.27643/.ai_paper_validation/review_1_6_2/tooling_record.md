# Tooling record

- **Probe UTC:** 2026-10-11T16:08:06Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0
- **Fallback capabilities used:** info, text, layout, render
- **Fallback environment removed:** YES
- **Compute device:** GPU_USER_REQUESTED
- **Tooling limitations:** Direct PDF and OCR binaries absent. Corrected user-specified /home/juliz/venvs/stt/bin/python is available (PyMuPDF 1.28.0; pypdf 6.14.2; onnxruntime-gpu 1.28.0). Package-local fallback creation completed after elevated network retry. GPU and PowerShell are accessible outside the sandbox.

User explicitly requested RTX 5070 Laptop GPU OCR through Windows PowerShell 5.1 or PowerShell 7. Elevated read-only PowerShell and nvidia-smi probes confirm NVIDIA GeForce RTX 5070 Laptop GPU, driver 616.56. Rendering used CPU; completed extraction-fitness assessment and targeted visual mapping established that no fresh OCR was needed. No GPU OCR ran and no new OCR engine was selected. Source-matched reusable derivatives were used first.

Probe: python3 workflow_1_6_2/scripts/pdf_tools.py probe. Available system Python is 3.12.3 with fitz and pypdf. Bootstrap uses the permitted bundled helper; no global environment is modified.

User path correction received: ~/venvs/stt/bin/python. Use /home/juliz/venvs/stt/bin/python for permitted bundled helper calls and report rendering/validation, honoring the user's interpreter preference. The package-local fallback retains pinned PDF packages and will be removed at completion. Existing user environment is preserved. GPU ONNX Runtime is available; rapidocr-onnxruntime 1.4.4 is installed. No new OCR engine is selected unless OCR is needed. Initial sandbox bootstrap download failed, followed by a successful elevated retry; bootstrap_log.json records READY.

Current-run mapping derivatives use the user interpreter, PyMuPDF1.28.0 and bundled pdf_tools.py for unavailable info/text/layout/render. New renders are CPU200dpi and were visually inspected. DOC-002 fresh units108,121,137,138,187; DOC-003 fresh units54,55,58,59,60. Additional DOC-003 p105 render is targeted equation confirmation; DOC-004 full26page layout corroborates the source-linked reusable assets. No new OCR or GPU inference was necessary. Source-matched legacy OCR remains reused, with historical engine version unavailable. Exact commands/output paths are in each mapper's provenance section.

Checker and screening source confirmations likewise use the user interpreter and bundled helpers; each stage records exact source spans/derivative paths and PyMuPDF1.28.0 CPU200dpi render provenance in its own artifact. Reused source locators remain unchanged. Direct-source Figure1 inspection corrected one current-run transcription before inclusion screening; the supplied PDF itself is unchanged.

Completion: standalone HTML rendered with the user interpreter and bundled render_report.py. Then bootstrap_tooling.py remove deleted the package-local tooling/venv and tooling/pip-cache; removal confirmed 2026-10-11T17:40:56Z. The bootstrap log is retained. No package was installed into or removed from the user interpreter. Final six-source and 270-reused-asset SHA-256 recomputation exactly matches the before inventories.
