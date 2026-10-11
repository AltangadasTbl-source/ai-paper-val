# Workflow 1.6.2 Tooling Record

- **Probe UTC:** 2026-10-11T06:39:51Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Compute device:** CPU
- **Tooling limitations:** Tesseract and LibreOffice absent. No Office sources supplied. DOC-002 pp.104,105,127,140-162,183-185,187 have no usable body text and are assigned to visual mapping of source-matched reusable page images. All 229 PDF pages have usable reusable text or images; no uncovered scientific unit is permitted.

Probe command: `python3 workflow_1_6_2/scripts/pdf_tools.py probe`. Full result: `tool_probe.json`. sha256sum is available. No global installations or provider changes.

Current-run confirmation engines: Poppler pdfinfo/pdftotext/pdftoppm/pdftocairo 25.03.0; CPU. Recheck derivative command parameters, exact paths and SHA-256 values are recorded in verification/evidence_recheck.md. The additional monitoring confirmation image is recorded in evidence_asset_inventory.md. No OCR or Office conversion was needed; all assigned textless units were visually mapped.

Second-pass derivative provenance: checkers/parts/statistical_report_support_pass_2.md records its direct-layout derivative; checkers/parts/statistical_monitoring_pass_2.md records its eight direct text/render derivatives; screening/inclusion_screen_pass_2.md records its three direct-layout derivatives. All use Poppler25.03.0 on CPU. No fallback installation or additional OCR was needed.

Finalization: Markdown assembled with all15 stable IDs; standalone HTML rendered using the bundled render_report.py and available Pandoc, with embedded CSS and a table of contents. The prescribed bootstrap_tooling.py remove command returned an empty removal list because no fallback environment or cache was created. Fallback environment removed remains NOT_CREATED. Appended recheck and support-audit derivative provenance is recorded in verification/evidence_recheck_appended.md and quality/parts/audit_support.md. All four source hashes and305 reused-artifact hashes match their before-and-after files. Compute device remained CPU throughout.
