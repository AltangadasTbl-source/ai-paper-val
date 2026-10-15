# Tooling Record

- **Probe UTC:** 2026-10-14T16:23:07Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=no; pdftotext=no; pdftoppm=no; pdftocairo=no; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** CREATED
- **Fallback packages:** PyMuPDF==1.26.4; pypdf==5.9.0
- **Fallback capabilities used:** info, text, render, ocr
- **Fallback environment removed:** YES
- **Compute device:** CPU
- **Tooling limitations:** Direct PDF/OCR tools absent. Pinned package-local PDF helper provides source metadata, text and rendering. Under the user's explicit interpreter authorization, existing /home/juliz/venvs/stt/bin/python runs the supplied pdf_tools.py OCR command with RapidOCR-onnxruntime1.4.4 and onnxruntime1.28.0, CPU. No global packages were installed. Native text is corrupted/sparse for protocol/SAP/code; usable older images and fresh CPU OCR cover them, with visual confirmation required.

First sandboxed PDF bootstrap returned INSTALL_FAILED; authorized retry succeeded at2026-10-14T16:24:02Z using both exact pinned versions, recorded in tooling/bootstrap_log.json.

User authorized RapidOCR with RTX5070Laptop, pwsh7 and ~/venvs/stt/bin/python. CUDA trial could not load libcublasLt.so.13 and selected CPUExecutionProvider; GPU has not processed evidence. Trial detail is preprocessing/fresh_ocr/gpu_trial.log. Actual fresh protocol/SAP OCR uses CPU only, the supplied helper, and prior1.5.1 source-linked images. Each derivative's engine/source/output is recorded in preprocessing/fresh_ocr/engine_log.jsonl. OCR input images were hashed before processing in preprocessing/fresh_ocr/input_hashes.sha256. All OCR output is a locator, not final candidate authority.

User explicitly instructed deletion/exclusion of pre-existing1.6.2 assets. Those and the support maps dependent on them were deleted; the current review reuses only older document_outputs/review1.5.1 assets. The validator remains unchanged. No prior1.6.2 evidence or scientific result is reused.

Fresh OCR completed successfully for all112pages (94protocol+18SAP);112engine records and112nonempty output files. The first long batch stopped after57completed pages with exit143; a missing-output-only continuation completed the remainder without repeating completed OCR. New derivative integrity is recorded in preprocessing/fresh_ocr/derivative_hashes.sha256. Source images remained unchanged. All fresh OCR belongs to this current run and is excluded from reused-artifact counts/hashes.

Temporary package-local PDF environment removed at 2026-10-14T17:43:56Z after HTML rendering. The bootstrap log remains preserved; the user-provided existing OCR interpreter was not modified or removed.
