# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:37:23Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None

Probe command: python3 workflow_1_6_2/scripts/pdf_tools.py probe. Direct PDF information, native/layout extraction, rendering, CPU OCR, Office conversion, hashing, and report rendering are available. No global package installation is needed. CPU processing was announced before any rendering or OCR.

## Direct tool versions

Poppler pdfinfo, pdftotext, pdftoppm: 26.01.0; Tesseract: 5.5.0; LibreOffice: 26.2.6.3; Pandoc: 3.7.0.2; sha256sum (uutils coreutils): 0.10.0; Python auxiliary interpreter: 3.14.4. LibreOffice version probing emitted a dconf runtime-directory access warning; conversion is not currently required. Each specialist records engines and derivative locations in its artifact.

Current-run processing: support mapping used direct Poppler pdftoppm 26.01.0 CPU rendering for DOC-002 physical PDF pp. 17, 18, 29 and 30. Outputs are unique files below preprocessing/support_map/ and are recorded by the mapper. These are new derivatives covering four fresh-required screenshot units, not reused assets. No OCR or Office conversion has been needed.

Numeric checking also used direct Poppler pdftotext 26.01.0 targeted layout extraction, writing eTable10-direct.txt, eTables3-5-direct.txt and Table3-direct.txt below preprocessing/numeric_check/. No OCR or fallback capability was used. Exact source locations and commands are recorded in the numeric inventory and checker artifacts.

Cross-source checking used 17 direct targeted Poppler pdftotext 26.01.0 layout confirmations below preprocessing/cross_check/. All exact source locations, derivative paths and commands are recorded in checkers/cross_source_consistency.md. No OCR was required.

Statistical pass 1 used five targeted direct Poppler pdftotext 26.01.0 layout derivatives below preprocessing/stat_pass1/. Commands and exact source pages are recorded in the statistical inventory. No OCR or fallback was used.

Initial inclusion screening used four direct Poppler pdftotext 26.01.0 layout files and five direct Poppler pdftoppm 26.01.0 CPU page images below preprocessing/inclusion_initial/. Exact source scopes and commands are recorded in screening/inclusion_screen.md. No OCR or fallback was needed.

Coverage accounting refinement: the support mapper's four DOC-002 screenshot renders close four fresh-required source units (pp. 17, 18, 29, 30), rather than purely auxiliary confirmations of fully reusable page content. Reusable caption text was only partial. Final source coverage is 76 reusable plus four freshly visually mapped pages, all complete.

Mechanical evidence recheck used direct Poppler pdftotext 26.01.0 layout confirmation of main REPORT 11 pages, results REPORT 23 pages, PLAN pp. 11–12 and 31–39, plus targeted Poppler pdftoppm 26.01.0 CPU images of PLAN pp. 12 and 37. Outputs are uniquely stored below preprocessing/evidence_recheck/; verification/evidence_recheck.md records every derivative and engine. No OCR/fallback or missing source-location confirmation was needed.

Final statistical pass 2 and quality audit reused confirmed text/page derivatives without additional OCR or extraction. The final standalone HTML was rendered with bundled render_report.py using Pandoc 3.7.0.2 and embedded workflow CSS. After rendering, bundled bootstrap_tooling.py remove confirmed that no fallback environment exists; removal result NOT_CREATED is final. No packages were installed. All processing remained CPU; every extraction/render derivative engine is recorded above and in its producing artifact.
