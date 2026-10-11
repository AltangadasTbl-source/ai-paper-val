# Tooling Record

- **Probe UTC:** 2026-10-11T02:52:34Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** Tesseract and Office conversion unavailable; supplied sources are PDF. Existing OCR and direct rendered-page inspection will cover any image-only units.

Probe command: `python3 workflow_1_6_1/scripts/pdf_tools.py probe`. Python 3.13.5. Direct PDF information, native/layout extraction, rendering, hashing, and Pandoc are available. CPU-only review.

Direct engine versions: Poppler pdfinfo/pdftotext/pdftoppm 25.03.0; Pandoc 3.1.11.1; GNU sha256sum 9.7. Curator confirmed all 132 source pages have usable reusable assets; fresh OCR and fallback installation are unnecessary.

Mapping identified four embedded-content gaps (DOC-002 pp13,54,63,67); direct CPU Poppler25.03.0 page renders and visual reading closed them. Native/layout remained partial for those units, so final fresh-required count is4. Direct confirms also produced DOC-001 p6 and DOC-002 p92 renders. No new OCR was necessary. Source coverage is132/132.

Final closure: standalone HTML rendered with local Pandoc3.1.11.1; bootstrap_tooling.py remove invoked after rendering. No fallback environment had been created. Fallback environment removed remains NOT_CREATED. Every supplied unit has mapped coverage; source and reused hashes remain unchanged. All31new source confirmation derivatives and their engines are inventoried. Tooling record complete.
