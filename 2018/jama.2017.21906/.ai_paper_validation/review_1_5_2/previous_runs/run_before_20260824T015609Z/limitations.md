# Limitations

- The user instructed this run to reuse existing OCR and not rerun OCR on CPU. The existing OCR bundle covers DOC-004 pages 3-16 and is cryptographically matched to the current source PDF. Native and layout text remain the primary evidence for every source.
- Poppler was unavailable in the base PATH; a locally extracted matching Poppler 24.02.0 runtime under `/tmp/qc15-poppler` was used for direct PDF metadata, text extraction, and any needed rendering.

