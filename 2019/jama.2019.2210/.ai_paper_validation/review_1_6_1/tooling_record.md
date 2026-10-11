# Workflow 1.6.1 Tooling Record

- **Probe UTC:** 2026-10-11T02:45:02Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_1/scripts/pdf_tools.py probe`. Python 3.14.4. Direct SHA-256 tooling is also available. PDF information, native/layout extraction, rendering, CPU OCR, Office conversion, and Pandoc rendering are available. No global installations or GPU tooling are required.

Direct engines: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0 with Leptonica 1.86.0; LibreOffice 26.2.6.3; Pandoc 3.7.0.2. Hashing uses sha256sum. Tool-version probes completed locally on CPU.

Final tooling closure: standalone HTML was rendered once with the permitted render_report.py helper and direct Pandoc 3.7.0.2. After rendering, `python3 workflow_1_6_1/scripts/bootstrap_tooling.py remove` returned `{"removed": []}`. No fallback environment had been created and none remains; NOT_NEEDED / NOT_CREATED is final. All fresh PDF derivatives use the recorded direct Poppler engine; no new OCR or Office conversion was required. Source and reused-artifact final hashes were recomputed with sha256sum and matched their unchanged baselines. Final tooling record complete before validation.
