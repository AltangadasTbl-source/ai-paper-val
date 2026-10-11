# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:37:14Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: python3 workflow_1_6_2/scripts/pdf_tools.py probe. Python 3.14.4; all required direct capabilities available. Direct tools reside in /usr/bin. No global installation or fallback installation is needed. Rendering and OCR CPU notification was provided before preprocessing. Each derivative records its engine and source location in the evidence inventories or extraction artifact.

Direct PDF information, native/layout extraction, and rendering engines: Poppler 26.01.0 (pdfinfo, pdftotext, pdftoppm). Available OCR engine: Tesseract 5.5.0 with Leptonica 1.86.0, CPU. Versions obtained with each tool's version option.

Statistical diagnostic engine: R 4.5.2 base stats, as recorded in statistical pass 1; computations are labelled diagnostics and are not substitutes for source-specified analyses. Derivative provenance for the numeric, cross-source and statistical reviewers is recorded in each canonical checker artifact; direct Poppler 26.01.0 extraction and CPU renders only, no OCR.

Finalized UTC: 2026-10-11T07:45:34Z. Direct CPU source rendering and extraction completed; no OCR was necessary. The report was rendered with the bundled render_report.py profile 1.6.2 and local Pandoc. After HTML rendering, bootstrap_tooling.py remove returned {"removed": []}; no fallback environment had been created and none remains. Removal state remains NOT_CREATED. Four source hashes and all 116 reused-artifact hashes were recomputed and match their before inventories exactly. No tooling or installation limitation remains.

Final closeout: HTML was rerendered after one audit-bookkeeping vocabulary repair and refreshed timing. A repeated post-render bootstrap removal check returned {"removed": []}; no temporary environment remains. Final validation reports PASS with no warnings; Compute device remains CPU and Tooling limitations remain None.
