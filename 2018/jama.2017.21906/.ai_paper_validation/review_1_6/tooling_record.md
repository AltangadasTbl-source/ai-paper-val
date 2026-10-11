# Workflow 1.6 Tooling Record

- **Probe UTC:** 2026-10-11T00:43:38Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** Tesseract CPU OCR and Office conversion are absent. All supplied sources are PDFs; no Office conversion is required. DOC-004 pp. 3-16 were completely mapped using source-bound reusable OCR and page images, with direct Poppler rendering for targeted confirmation. DOC-002 p. 14 was freshly rendered and visually mapped. No source unit lacks scientific coverage, and no new OCR or package installation was needed.

Probe engine: Python 3.13.5 executing the supplied pdf_tools.py probe helper. PDF information, native/layout text, rendering, and hashing are direct local tools. No global package installation or GPU invocation is authorized or needed.

Direct tool versions: Poppler pdfinfo/pdftotext/pdftoppm 25.03.0; Pandoc 3.1.11.1. All review derivatives record a direct engine in the asset inventory or producing mapper/recheck record. Existing OCR may have historical GPU metadata; it is reused as supplied evidence only. This run performs no GPU probe or invocation.

Final closeout: standalone HTML rendered using the supplied render_report.py helper and direct Pandoc. After rendering, `python3 workflow_1_6/scripts/bootstrap_tooling.py remove` returned `{"removed": []}` because no fallback environment was created. Removal status remains NOT_CREATED; no temporary environment or installed package is left in this package. Direct source and reused-artifact before/after SHA-256 records are identical.
