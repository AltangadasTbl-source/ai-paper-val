# Local tooling record

- **Probe UTC:** 2026-10-11T02:52:33Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** Tesseract and Office conversion are unavailable. All supplied sources are PDFs; direct native/layout extraction and rendering are available. Visually inspect any text-unusable unit using direct rendering. No global installations.

Probe command: python3 workflow_1_6_1/scripts/pdf_tools.py probe. Python 3.13.5; direct tools at /usr/bin. Fallback PDF environment not required by the probe.

## Final tooling and removal record

Current derivatives use direct Poppler 25.03.0 pdftotext layout and pdftoppm CPU rendering, with engine/options recorded in the evidence-asset inventory and recheck. Hashing uses GNU sha256sum 9.7. Standalone HTML was rendered with the supplied render_report.py helper and Pandoc 3.1.11.1; no network assets are loaded.

After HTML rendering, the prescribed bootstrap_tooling.py remove command returned an empty removed list. No fallback environment was created or remains; Fallback environment removed stays NOT_CREATED. Native text and visual source inspection cover all 44 units; unavailable OCR and Office tools caused no scientific coverage gap.
