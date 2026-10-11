# Workflow 1.6 Tooling Record

- **Probe UTC:** 2026-10-11T00:43:43Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** Tesseract and Office conversion are unavailable. There are no Office sources. DOC-002 image-only pages 52,108-109,126-133 were covered by source-hash-matched reusable OCR/images and visual inspection; p134 was freshly rendered and visually mapped. All candidate evidence pages were visually rechecked. No scientific-coverage gap remains.

Probe: `python3 workflow_1_6/scripts/pdf_tools.py probe`. Versions: Poppler pdfinfo/pdftotext/pdftoppm 25.03.0; Pandoc 3.1.11.1; Python 3.13.5 for bundled auxiliary scripts only. Direct SHA-256 hashing is available. Mapping and recheck artifacts record every derivative's engine, command and location; the evidence-asset inventory indexes reused and new derivative coverage.

No new OCR engine, Python environment, package installation, GPU probe or GPU invocation was needed. The user required any necessary environment under /tmp; no environment was created anywhere and no global packages were installed. The workflow bootstrap removal check ran after HTML rendering and returned {"removed": []}, confirming that no temporary environment existed to remove. Historical GPU-related metadata in reused OCR records describes earlier generation only.

Final removal command: `python3 workflow_1_6/scripts/bootstrap_tooling.py remove`. Durable result: bootstrap_removal_check.json (`{"removed": []}`). Fallback environment removed remains NOT_CREATED. HTML rendering used Pandoc 3.1.11.1 via the bundled report renderer; no package installation occurred.
