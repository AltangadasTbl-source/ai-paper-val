# Workflow 1.6.2 Tooling Record

- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** OCR and Office conversion unavailable; all sources are readable native-text PDFs, and image-only content is covered by reusable page images. No source unit depends on a missing tool. Some historical derivative renderer versions are unrecorded.

- **Probe UTC:** 2026-10-11T06:39:43Z

Current-run derivative engines: direct pdftotext -layout and pdftoppm, Poppler 25.03.0, CPU. Initial recheck: 22 derivatives from 11 pages at 120 dpi for PNGs, recorded per file in preprocessing/recheck_derivative_record.md. Appended C005 recheck: four derivatives from results-supplement pp.6–7 at 150 dpi for PNGs, recorded per file in verification/parts/evidence_recheck_appended.md. No OCR was needed. Historical renderer/version gaps remain recorded in the reusable-asset inventory.

Hash engine: sha256sum, GNU coreutils 9.7. HTML renderer available: Pandoc 3.1.11.1, invoked through the supplied render_report.py helper with profile 1.6.2.

Final production closure: the supplied profile-1.6.2 renderer produced standalone HTML using Pandoc 3.1.11.1 after complete Markdown assembly. The supplied bootstrap_tooling.py remove command returned an empty removed list: no fallback environment or package cache was created. Compute device remains CPU; fallback environment removed remains NOT_CREATED. All source/reused before and after hash files are byte-identical. No source unit has a tooling-related scientific coverage gap.
