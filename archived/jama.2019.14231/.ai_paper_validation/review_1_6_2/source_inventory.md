# Direct Source Inventory

Scope: the current paper package only. Recursive extension inventory located three direct PDFs and no DOC, DOCX, XLS, XLSX, or CSV sources. No converted PDF derivatives were counted as direct sources. Stable unit type is PDF_PAGE, including contents, definitions, references, and administrative pages. SHA-256 values agree with the factual identity fields of the legacy document records and the coordinator's source baseline.

| Source ID | Source path | Format | Document role | Total units | Exact content and role basis | Reusable evidence scope | Mapper assignment |
|---|---|---|---|---:|---|---|---|
| DOC-001 | jama_aminian_2019_oi_190103.pdf | PDF | REPORT | 12 | Main original investigation, Association of Metabolic Surgery With Major Adverse Cardiovascular Outcomes in Patients With Type 2 Diabetes and Obesity; retrospective matched-cohort results, PDF p1; printed JAMA pp1271–1282 | PDF pp1–12 native and normalized text, source-linked extraction maps, selected page images, p3 OCR | Main mapper, every PDF page 1–12 |
| DOC-002 | joi190103supp1_prod.pdf | PDF | REPORT | 20 | Non-plan results supplement: PDF p1 contents lists diagnosis/procedure definitions, medications, event rates, cumulative incidence, hazard ratios, longitudinal results, and sensitivity analyses; pp2–20 contain those report materials | PDF pp1–5 combined native/layout extraction; pp6–20 page native/normalized text and partial result map; selected page images | Support mapper, every PDF page 1–20 |
| DOC-003 | joi190103supp2_prod.pdf | PDF | PLAN | 7 | Original study protocol dated January 6, 2019, pp2–6, and amendment dated August 2, 2019, p7; p1 contents identifies both | PDF pp1–7 combined native/layout extraction | Support mapper, every PDF page 1–7 |

No source bundle mixes REPORT and PLAN content. DOC-003 contains two plan versions in one bound PLAN bundle. The observational study content governs interpretation of protocol terminology.

Identity and counts: direct pdfinfo (Poppler 26.01.0) reports 12, 20, and 7 pages, respectively, with native text layers and no encryption. Direct sha256sum gives:

- DOC-001: fcf715eadcef54b5c78a557ae684311a96c22c502f4297293156d6cf7f94e4b9
- DOC-002: ec4e0375222279bcc2137db1be3649d22fd86997f308c1c8f0cba85cfba4c322
- DOC-003: 254d15bd2cc32b6c0c21d399caa17ac84fd6b1136e320cd046e0cfefc3ed713f

The coordinator owns source_hashes_before.sha256 and timing fields. All supplied source and legacy assets remain unchanged. No legacy scientific-check, candidate, screening, classification, verifier, critic, or final-report file was used as inventory evidence. Factual identity/format fields from document records and manifests were used; their legacy scope restrictions and processing outcomes do not constrain this review.
