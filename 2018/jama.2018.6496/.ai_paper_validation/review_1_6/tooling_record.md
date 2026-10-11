# Workflow 1.6 Tooling Record

- **Probe UTC:** 2026-10-11T00:43:54Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** OCR and Office conversion are unavailable. All supplied sources are PDFs with existing text and native PDF tools available. Visual page inspection will cover any image-only units. No package installation is currently needed.

Probe: `python3 workflow_1_6/scripts/pdf_tools.py probe`, recorded in `preprocessing/tool_probe.json`. Use direct pdfinfo, pdftotext, pdftoppm/pdftocairo, and sha256sum. No GPU operations. If packages become necessary, the user's temporary-folder requirement takes precedence; do not install globally.

Direct engine versions: Poppler pdfinfo/pdftotext/pdftoppm/pdftocairo 25.03.0; Pandoc 3.1.11.1; GNU coreutils sha256sum 9.7; system Python 3.13.5 is used only for allowed workflow helpers.

Recheck tooling completion: sixteen exact source pages freshly rendered at125dpi and visually inspected with direct Poppler25.03.0; no OCR or Office conversion was required, and no fallback environment was created. Engine and exact source/output substitutions are recorded in verification/evidence_recheck.md.

Final cleanup: `python3 workflow_1_6/scripts/bootstrap_tooling.py remove` returned `{"removed": []}` after HTML rendering. No fallback environment existed; removal state remains NOT_CREATED.
