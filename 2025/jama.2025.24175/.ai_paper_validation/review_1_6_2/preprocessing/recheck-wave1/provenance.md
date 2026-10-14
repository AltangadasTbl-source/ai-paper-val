# Fresh mechanical recheck source derivatives: wave 1

Scope: DOC-001 PDF pp.3,5,6,7,8 and DOC-002 PDF pp.7,24,25,26,27,57,66,67,68,69,70,71,72. Eighteen unique source pages, all freshly rendered and visually reread for C001, C002, C003, C004, C005, C006 and C007. No OCR was needed. Sources and reused evidence assets were unchanged.

Engine: PyMuPDF 1.26.4 through the supplied `workflow_1_6_2/scripts/pdf_tools.py`; PDF rendering device: CPU; resolution: 200 dpi. The run records GPU_USER_REQUESTED as the user's OCR preference, but these readable PDF renders require no OCR/GPU engine.

For each listed DOC-001 page N, the exact command template was:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf --page N .ai_paper_validation/review_1_6_2/preprocessing/recheck-wave1/main-N.png
```

For each listed DOC-002 page N:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render joi250116supp1_prod_1771885794.26255.pdf --page N .ai_paper_validation/review_1_6_2/preprocessing/recheck-wave1/plan-N.png
```

Complete source-native article text was additionally extracted for the C007 bounded absence check:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf --first 1 --last 12 .ai_paper_validation/review_1_6_2/preprocessing/recheck-wave1/main-full-native.txt
```

Outputs: main-3.png, main-5.png, main-6.png, main-7.png, main-8.png; plan-7.png, plan-24.png, plan-25.png, plan-26.png, plan-27.png, plan-57.png, plan-66.png, plan-67.png, plan-68.png, plan-69.png, plan-70.png, plan-71.png, plan-72.png; main-full-native.txt. All source visual confirmation belongs to verification/evidence_recheck.md; this provenance record contains no separate candidate decision.
