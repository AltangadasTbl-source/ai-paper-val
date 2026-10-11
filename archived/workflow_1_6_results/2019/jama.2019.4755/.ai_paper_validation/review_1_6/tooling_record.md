# Workflow 1.6 Tooling Record

- **Probe UTC:** 2026-10-11T00:34:23Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: python3 workflow_1_6/scripts/pdf_tools.py probe. All required direct capabilities are available. SHA-256 engine: /usr/bin/sha256sum. Python version: 3.14.4; no auxiliary extraction modules are needed. Every derivative records its producing engine in the evidence inventory or the producing specialist's artifact. No fallback environment was created.

Finalization: the supplied report renderer produced standalone HTML with installed Pandoc after unchanged final source and reused-artifact hashes were recomputed. The supplied bootstrap_tooling.py remove command completed successfully after rendering and found no environment to remove (removed list empty). Fallback environment removed remains NOT_CREATED, truthfully reflecting that no environment existed. All final direct-tool operations were CPU-only.
