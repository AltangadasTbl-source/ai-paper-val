# Workflow 1.6.1 Tooling Record

- **Probe UTC:** 2026-10-11T02:45:41Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe engine: python3 workflow_1_6_1/scripts/pdf_tools.py probe; Python 3.14.4. Direct tools are installed under /usr/bin. Source processing will use direct Poppler tools, sha256sum and targeted Tesseract CPU OCR when needed. Tool versions and derivative commands are recorded in the evidence asset inventory or mapper artifacts.

Direct version checks: Poppler pdfinfo 26.01.0; Tesseract 5.5.0; sha256sum (uutils coreutils) 0.10.0; pandoc 3.7.0.2. No temporary environment is needed.

Current fresh visual derivatives: direct Poppler26.01.0 rendering and layout extraction under preprocessing/protocol_a/, protocol_b/, protocol_c/ and sap_formula/. Targeted OCR uses Tesseract5.5.0 CPU English psm6 where recorded in mapper parts. Every derivative command and exact source scope is preserved in its unique mapper artifact. No fallback environment or global package installation occurred.

Final closure: the prescribed bootstrap_tooling.py remove command returned an empty removal list because no temporary environment was created. Fallback environment remains NOT_NEEDED and removal state NOT_CREATED. Source/reuse SHA-256 recomputation matched both before manifests. HTML was rendered using the local bundled renderer with direct pandoc; validation follows in review_validation.json.

A final validator formatting repair made all77 existing pass-1 records explicit in the checker. Timing fields were advanced and HTML was necessarily re-rendered from the finalized Markdown; no scientific evidence changed. The fallback removal check again returned an empty list, consistent with NOT_CREATED. Both complete integrity manifests remained identical before final revalidation.
