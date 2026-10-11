# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:39:19Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** None. Missing direct OCR and Office conversion are not required for the three native-text PDFs; all 49 pages have usable source-matched reusable text and local visual inspection is available.

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Python 3.13.5. The session informed the user of CPU processing before any rendering or OCR. All specialists must use direct available tools and record engines for derivatives. If OCR becomes necessary, request coordinator bootstrap of the permitted package-local environment; visual inspection remains available.

Direct versions: Poppler pdfinfo/pdftotext/pdftoppm/pdftocairo 25.03.0; Pandoc 3.1.11.1; GNU coreutils sha256sum 9.7. Inventory found only native-text PDFs. All 49 pages have usable reusable native extraction, so missing direct OCR and Office conversion create no required preprocessing gap. No fallback environment was created.

Mechanical evidence recheck used current-source CPU pdftotext -layout for all three PDFs and targeted CPU pdftoppm rendering at110dpi for main pages5-7 and100dpi for main page8/support page4. Every derivative and engine is listed in evidence_asset_inventory.md; exact location and confirmation purpose are recorded in verification/evidence_recheck.md. No OCR or GPU was used.

Finalization: Markdown rendered to standalone UTF-8 HTML5 using the bundled render_report.py and Pandoc3.1.11.1, with embedded workflow CSS and a table of contents. The bundled bootstrap_tooling.py remove command reported an empty removed list, confirming no fallback environment had been created or remained. Fallback environment removed: NOT_CREATED. Direct-source and reused-asset before/after hash files compare identically. Final compute device remains CPU.

Validation completion: final validator reports PASS with no findings in its mechanical failure list and no warnings. Standalone HTML has27 internal anchor targets, all resolving. HTML was refreshed once after the required timing update for the mechanical pass-1 scope repair; no scientific content or candidate classification changed. Rendering and validation remain outside the recorded review duration. All3 source hashes and47 reused-asset hashes remain unchanged; no temporary fallback environment remains.
