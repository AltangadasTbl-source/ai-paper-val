# Direct-source inventory

Curator runtime: 01a12c3a-ad69-7ce3-9b2b-fe66c6bb1a9e; canonical task: /root/asset_curator; model gpt-6.1-sol; reasoning effort medium.

The package contains exactly three direct PDFs. No supplied DOC, DOCX, XLS, XLSX, or CSV source exists outside the audit/tooling area. Software dependency test data inside the new fallback environment are not supplied scientific sources. Every PDF page is a stable unit, including front matter and administrative pages. Earlier exclusions do not constrain this run.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_zahid_2025_oi_250093_1768590553.08463.pdf | PDF 1.4 | PDF_PAGE | 9 | REPORT | Published cluster randomized clinical trial article, with abstract, methods, participant flow, tables, figures and results. |
| DOC-002 | joi250093supp1_prod_1768590553.08963.pdf | PDF 1.6 | PDF_PAGE | 109 | PLAN | Bound study protocol versions, amendment/change note, statistical analysis plan, and prospective intervention SMS materials; table of contents visually confirms this content. |
| DOC-003 | joi250093supp2_prod_1768590553.09463.pdf | PDF 1.6 | PDF_PAGE | 16 | REPORT | Non-plan results supplement: contents, steering committee, eTables and eFigure. |

No bundle mixes REPORT results and PLAN specifications. DOC-002 contains multiple PLAN components. All direct sources are unencrypted. PDF counts were confirmed using the recorded missing-capability fallback: `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py info SOURCE`; engine PyMuPDF 1.26.4. Direct `file` and `sha256sum` were available. Hashes are recorded with package-relative paths in `source_hashes_before.sha256`.

All pages of each source are assigned to downstream mapping. DOC-001 goes to the main mapper. DOC-002 pp. 1-109 and DOC-003 pp. 1-16 go to support mapping; visual PLAN mapping must be sharded within the 32 rendered-page context bound.
