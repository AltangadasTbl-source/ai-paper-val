# Selective PDF Preprocessing

The authoritative source-linked page manifest is `page_manifest.json`. Native PDF text was extracted first for all 12 selected pages: DOC-001 pages 1-9 and DOC-004 pages 1-3. No further OCR was required for extraction completion. The validated OCR backend selection is recorded in `ocr_backend.json` as `rapidocr-cpu`; it is CPU-only, not CUDA.

All generated artifacts in this directory derive from supplied PDFs. No source PDF was modified, moved, renamed, or overwritten.
