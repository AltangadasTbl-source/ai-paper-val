# Document Record: doc_001_main_article

- Source: `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`
- SHA-256: `4bb1cfc9284d00a83984f493da34bab05357d4cca69abf0c06a281a5597fd927`
- Page count: 9
- Native text layer: available and usable on 9/9 pages.
- Classification: Main article.
- Heading evidence: page 1, “Remote Screening for Asymptomatic Atrial Fibrillation: The AMALFI Randomized Clinical Trial”; structured abstract includes Results. Pages 2-8 include Methods, Results, Discussion, and tables/figures.
- Results-relevant scope: pages 1-8. Page 9 is references.
- Scientific processing status: Preprocessed for downstream scientific audit (pages 1-8 only).
- Extraction/OCR scope: Native text extracted and normalized for pages 1-8; all selected pages passed page-level usability review. Rendered page images retained for pages 4-8 (participant flow, tables, and figures). Supplemental OCR was retained for pages 4-8; it did not replace native text. Page 9 (references) is **Not Audited by Design** for scientific extraction.
- Preprocessing artifacts: `normalized_text.md`, `page_extraction_manifest.md`, `page_extraction_manifest.json`, `normalized_text/page_001.txt` through `normalized_text/page_008.txt`, and selective `page_images/` and `ocr_text/` artifacts. Every artifact identifies its source PDF and source page.

## AI Training Restriction Record

- Status: **Explicit AI Training Restriction**.
- Exact quotation: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.”
- Location: `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`, footer, PDF pages 1-9 (verified on page 1; same footer located by native-text search on pages 2-9). Embedded document-info metadata identifies `/Author` as `American Medical Association` and contains no separate Rights or License field.
- Stated scope: The footer expressly reserves rights for **AI training**, as well as text and data mining and similar technologies. This record treats the AI-training clause as the training-related restriction; it does not treat the separate text-and-data-mining wording as an inference about other uses.
- Human Compliance Review: **Yes - flag retained.** The package instruction records that the user/institution has already authorized model-mediated processing; that authorization is noted operationally and does not change the supplied-materials status.

## Retained Agent Outputs

- Inventory and classification: `../../package_manifest.md`
- AI-use restriction screen: `ai_training_restriction_record.md`
- Preprocessing: `page_extraction_manifest.md` and `page_extraction_manifest.json`
- Main-article result extraction: `main_text_extractor_response.md`
- Table arithmetic check: `../../agent_outputs/table_arithmetic_checker_response.md`
- Figure and participant-flow check: `../../agent_outputs/figure_flow_checker_response.md`
- Statistical consistency check: `../../agent_outputs/statistical_consistency_checker_response.md`
- Evidence verification: `../../agent_outputs/evidence_verifier_response.md`
- Critic disposition: `../../agent_outputs/critic_response.md`
- Final report: `../../final_report.md`
