# Targeted GPU OCR provenance

The user requested GPU OCR and approved RapidOCR ONNX Runtime CUDA. PowerShell 5.1 and WSL NVIDIA checks confirmed the RTX 5070 Laptop GPU, driver 616.56, 8151 MiB. The requested existing stt environment supplies the console command. No new package was installed into that environment. Source PDFs remain authoritative; these outputs are transcription locators only.

| Source location | Image input | Engine and device | Derivative | Execution |
|---|---|---|---|---|
| DOC-002 PDF p. 10 | .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/page_images/page-010.jpg | RapidOCR 1.4.4; ONNX Runtime GPU 1.28.0; CUDA; RTX 5070 | preprocessing/gpu_ocr/DOC-002/page-010.log | Completed with CUDA flags and installed CUDA/cuDNN library path |
| DOC-002 PDF p. 10 | Same source image | Same engine/device; Perl formatting of console log | preprocessing/gpu_ocr/DOC-002/page-010.txt | Plain-text locator from preserved bounding-box/score log |
| DOC-002 PDF p. 80 | .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/page_images/page-080.jpg | RapidOCR 1.4.4; ONNX Runtime GPU 1.28.0; CUDA; RTX 5070 | preprocessing/gpu_ocr/DOC-002/page-080.log | Completed via run_page.sh; device snapshot preserved |
| DOC-002 PDF p. 80 | Same source image | Same engine/device; Perl formatting of console log | preprocessing/gpu_ocr/DOC-002/page-080.txt | Plain-text locator from preserved bounding-box/score log |
| DOC-002 PDF p. 29 | .ai_paper_validation/review_1_5_1/preprocessing/DOC-002/page_images/page-029.jpg | RapidOCR 1.4.4; CPU fallback on initial CUDA trial | preprocessing/gpu_ocr/DOC-002/page-029.log | CUDA library loading did not complete; retained as tooling diagnostic, no claim of GPU execution |

All new writes are inside this review. Reused input images are preserved and included in the before/after hash checks. No full-bundle OCR was repeated because fresh specialist visual inspection covered every PLAN page.
