# Fresh mechanical recheck source derivatives: wave 2

Scope: DOC-003 PDF pp.16,20,21,22,23,24,46,47,49,50,51,52,53. Thirteen unique source pages, all freshly rendered and visually reread for the REPORT destinations or bounded context of C002, C004, C006 and C007. Together with wave 1, the assigned cited-page union is 31 unique pages. No OCR was needed. Sources and reused evidence assets were unchanged.

Engine: PyMuPDF 1.26.4 through the supplied `workflow_1_6_2/scripts/pdf_tools.py`; PDF rendering device: CPU; resolution: 200 dpi. The run records GPU_USER_REQUESTED as the user's OCR preference; no OCR engine was needed or used.

For each listed DOC-003 page N, the exact command template was:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render joi250116supp2_prod_1771885794.27755.pdf --page N .ai_paper_validation/review_1_6_2/preprocessing/recheck-wave2/report-N.png
```

The complete 54-page results supplement was freshly extracted for index/locator and bounded absence searching:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text joi250116supp2_prod_1771885794.27755.pdf --first 1 --last 54 .ai_paper_validation/review_1_6_2/preprocessing/recheck-wave2/report-full-native.txt
```

Outputs: report-16.png, report-20.png, report-21.png, report-22.png, report-23.png, report-24.png, report-46.png, report-47.png, report-49.png, report-50.png, report-51.png, report-52.png, report-53.png; report-full-native.txt. Native text does not transcribe every embedded figure-panel value; the relevant source images were all visually reread. Candidate-specific evidence facts are in verification/evidence_recheck.md.
