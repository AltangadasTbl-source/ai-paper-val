# New source derivative provenance

| Source | Unit | Derivative | Engine | Compute device | Purpose |
|---|---|---|---|---|---|
| DOC-001 | PDF pp. 1-9 | preprocessing/main_source_layout.txt | Bundled pdf_tools.py text --layout; PyMuPDF 1.26.4 sorted reading order | CPU | Source-native locator and table alignment corroboration |
| DOC-002 | PDF p. 13 | preprocessing/support001_p013.png | Bundled pdf_tools.py render; PyMuPDF 1.26.4; 200 dpi | CPU | Direct source confirmation of clipped lower flow-diagram branch |

The supplied PDFs are authoritative and preserved. Targeted GPU OCR has its own manifest under preprocessing/gpu_ocr/manifest.md. Later checker/recheck render provenance is recorded with the derivative-producing agent's durable artifact.

Numeric support source renders: DOC-003 pp. 6, 9, 13 and DOC-002 pp. 16, 53, 62, 63, 64; bundled pdf_tools.py render, PyMuPDF 1.26.4, CPU. Exact derivative names/provenance are recorded in the numeric support checker artifact and its handoff.

Cross-source checker renders: 32 uniquely cross_main_, cross_plan_, and cross_supp_ page images, with exact source page/filename listing in checkers/cross_source_consistency.md. Engine bundled pdf_tools.py render, PyMuPDF 1.26.4, CPU, 160 dpi.

Statistical pass1 source render: DOC-001 PDF p. 6, preprocessing/st1-main-006.png; bundled pdf_tools.py render; PyMuPDF 1.26.4; 200 dpi; CPU.
