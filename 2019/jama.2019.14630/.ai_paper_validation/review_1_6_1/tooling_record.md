# Workflow 1.6.1 Tooling Record

- **Probe UTC:** 2026-10-11T02:46:06Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6_1/scripts/pdf_tools.py probe`. All required direct capabilities, including SHA-256, are available. Use direct local tools. No global or package-local installation is required. All newly generated derivatives must identify their direct engine and source units in the evidence asset record or their mapping artifact.

Direct tool versions recorded by the coordinator: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0 with Leptonica 1.86.0; Pandoc 3.7.0.2; sha256sum (uutils coreutils) 0.10.0. All extraction, page rendering, and targeted OCR use these local CPU tools. Reusable derivative engines are documented separately in evidence_asset_inventory.md.

Finalization: standalone HTML rendered by the bundled renderer using available local Pandoc. The required bootstrap_tooling.py remove command returned an empty removal list; no fallback environment or cache was created, and removal status remains NOT_CREATED. All source extraction and visual confirmation used the recorded direct CPU engines.
