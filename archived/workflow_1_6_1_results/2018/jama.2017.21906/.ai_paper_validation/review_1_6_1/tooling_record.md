# Local Tooling Record

- **Probe UTC:** 2026-10-11T02:52:35Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=no; libreoffice=no; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** CPU OCR and Office conversion tools are absent. PDF information, native/layout text, rendering, and hashing tools are available. Reusable OCR and visual inspection will cover any scanned pages; no Office sources are currently indicated. No GPU will be probed or invoked.

Probe command: `python3 workflow_1_6_1/scripts/pdf_tools.py probe`; full output: `preprocessing/tool_probe.json`.
Direct versions: pdfinfo 25.03.0; pdftotext 25.03.0; pdftoppm 25.03.0; Pandoc 3.1.11.1. Each new derivative records its direct engine and source page in its owning artifact.

The cross-source checker generated a targeted SAP p.7 render with direct pdftoppm 25.03.0 at120 dpi. It initially used a temporary path; the coordinator moved it into `preprocessing/xs-sap7.png` and updated its provenance reference. All durable derivatives reside in the permitted versioned review directory.

Finalization: all80 source pages are mapped, and all four direct-source plus77 reused-asset hashes are unchanged. The fallback remove command completed with NOT_CREATED; no temporary environment existed. HTML was generated with the supplied renderer using local Pandoc3.1.11.1 and embedded workflow CSS. No web resource or global package installation was used.
