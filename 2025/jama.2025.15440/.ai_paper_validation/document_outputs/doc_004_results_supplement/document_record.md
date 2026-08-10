# Document Record: doc_004_results_supplement

- Source: `joi250068supp3_prod_1760999665.30362.pdf`
- SHA-256: `b23b7b0f4699d6a025bf18e7f95e6098372a122b8bdb0f7580ac82c29638d01a`
- Page count: 11
- Native text layer: available and usable on 11/11 pages.
- Classification: Results supplement.
- Heading evidence: page 1 “Supplemental Online Content” lists eTable 1 (Patch usage metrics), eTable 2 (Baseline characteristics by patch ECG data availability), eTable 3 (Patch-detected conditions), and eFigures 1-4. The listed eTables/eFigures occupy pages 4-11.
- Results-relevant scope: page 1 (contents) and pages 4-11. Pages 2-3 are eMethods and references, excluded from default results audit.
- Scientific processing status: Preprocessed for downstream results-supplement audit (pages 1 and 4-11 only).
- Extraction/OCR scope: Native text extracted and normalized for pages 1 and 4-11; all selected pages passed page-level usability review. Rendered page images retained for pages 4-11 (eTables and eFigures). Supplemental OCR was retained for pages 4-7; it did not replace native text. Pages 2-3 (eMethods and references) are **Not Audited by Design** for the default results audit.
- Preprocessing artifacts: `normalized_text.md`, `page_extraction_manifest.md`, `page_extraction_manifest.json`, `normalized_text/page_001.txt` and `normalized_text/page_004.txt` through `normalized_text/page_011.txt`, plus selective `page_images/` and `ocr_text/` artifacts. Every artifact identifies its source PDF and source page.

## AI Training Restriction Record

- Status: **Explicit AI Training Restriction**.
- Exact quotation: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.”
- Location: `joi250068supp3_prod_1760999665.30362.pdf`, footer, PDF pages 4 and 8 (visually verified); embedded document-info metadata (`/Author`: `Guilherme Pessoa-Amorim`; no Title, Rights, Copyright, or License field).
- Stated scope: The footer expressly reserves rights for AI training. It also names text and data mining and similar technologies; those are recorded separately from the AI-training restriction. The eMethods description of a proprietary deep-learning algorithm (page 2) is study-analysis text, not a rights term.
- Human Compliance Review: **Yes - flag retained.** User/institutional authorization for model-mediated processing is recorded in the package instructions; that authorization does not change the supplied-materials classification.

## Retained Agent Outputs

- Inventory and classification: `../../package_manifest.md`
- AI-use restriction screen: `ai_training_restriction_record.md`
- Preprocessing: `page_extraction_manifest.md` and `page_extraction_manifest.json`
- Results-supplement extraction: `results_supplement_evidence_map.md`
- Table arithmetic check: `../../agent_outputs/table_arithmetic_checker_response.md`
- Figure and participant-flow check: `../../agent_outputs/figure_flow_checker_response.md`
- Statistical consistency check: `../../agent_outputs/statistical_consistency_checker_response.md`
- Evidence verification: `../../agent_outputs/evidence_verifier_response.md`
- Critic disposition: `../../agent_outputs/critic_response.md`
- Final report: `../../final_report.md`
