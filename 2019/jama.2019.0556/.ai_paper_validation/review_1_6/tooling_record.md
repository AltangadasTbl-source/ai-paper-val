# Workflow 1.6 Tooling Record

- **Probe UTC:** 2026-10-11T00:34:04Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: `python3 workflow_1_6/scripts/pdf_tools.py probe`. Python 3.14.4; all required direct capabilities available under /usr/bin. Every derivative must record its direct engine and command in its owning evidence artifact. CPU-only execution; no global installations.

Recorded direct engine versions: Poppler pdfinfo/pdftotext/pdftoppm 26.01.0; tesseract 5.5.0 (leptonica 1.86.0); pandoc 3.7.0.2. Runtime agent identifiers are the exact canonical task identifiers exposed by the collaboration interface; the interface does not expose another UUID.

Finalization: the standalone HTML was rendered with the bundled render_report.py profile1.6 helper using direct Pandoc3.7.0.2 and embedded local CSS. The required bootstrap_tooling.py remove command returned an empty removed list: no fallback environment or cache had been created, and no temporary environment remains. Fallback environment/removal fields remain NOT_NEEDED/NOT_CREATED. Additional direct raster-inventory engine: Poppler pdfimages26.01.0. An initial render was followed by a required metadata-refresh render after canonical statistical-record aggregation repair; no source evidence changed. All201 new derivative engines and assignments are indexed in evidence_asset_inventory.md; no tool limitation remains.
