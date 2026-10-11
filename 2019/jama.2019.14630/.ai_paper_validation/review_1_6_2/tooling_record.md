# Local tooling record

- **Probe UTC:** 2026-10-11T04:55:25Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU

Probe engine: python3 3.14.4, supplied workflow_1_6_2/scripts/pdf_tools.py probe. All direct capabilities are present. Derivative-producing agents must record the specific direct engine in their artifact provenance. CPU processing was announced before rendering or OCR. No global installations were performed.

- **Tooling limitations:** None

## Derivative provenance during mapping and checking

- Protocol mapping: preprocessing/protocol_p054.png, direct Poppler pdftoppm 26.01.0, DOC-002 PDF p.54, CPU. Command and visual purpose recorded in extraction/support_protocol.md.
- Statistical pass 1 support B: preprocessing/stat1-support-b-p15.png, preprocessing/stat1-support-b-p22.png, preprocessing/stat1-support-b-p26.png, direct Poppler pdftoppm 26.01.0, DOC-004 PDF pp.15,22,26, CPU. Exact commands recorded in checker provenance.
- Support numerical check: preprocessing/numeric_support/results-p7.png, direct Poppler pdftoppm 26.01.0, CPU, DOC-004 PDF p.7, rendered at scale-to 2000; exact command in checkers/parts/numeric_support.md.
- Mechanical recheck: 25 preprocessing/recheck_*.txt exact-page layout files and five preprocessing/recheck_*.png page images; direct Poppler pdftotext/pdftoppm 26.01.0, CPU. Exact filenames, pages, commands and visual confirmations are recorded in verification/evidence_recheck.md. No OCR or fallback was needed.

Pass-2 extension recheck produced 17 additional derivatives with direct Poppler pdftotext/pdftoppm 26.01.0 on CPU: eleven exact-page layout texts, three complete REPORT text streams and three targeted page images. Exact source/page/engine/command/file provenance is recorded in verification/pass_2_extension_C005.md. No OCR or fallback was used.

Final tooling closure: standalone HTML was rendered by the supplied profile 1.6.2 renderer using local Pandoc. The supplied bootstrap_tooling.py remove command completed after rendering; no fallback environment had been created and removal state remains NOT_CREATED. No tooling directory or temporary virtual environment remains. All derivatives used CPU and the recorded direct engines. Tooling record: COMPLETE.
