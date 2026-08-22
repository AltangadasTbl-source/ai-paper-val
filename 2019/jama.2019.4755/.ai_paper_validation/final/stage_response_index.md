# Validation Stage Response Index

This index preserves the response location or explicit non-audit disposition for every required workflow stage. All paths are relative to the package root.

| Stage / agent role | Preserved response or disposition |
|---|---|
| `package_inventory` | `.ai_paper_validation/document_outputs/package_manifest.json` and each document’s `document_record.json` |
| `ai_use_restriction_checker` | Each document’s `document_record.json`; separate records also exist where emitted by the checker |
| `pdf_preprocessor` | `.ai_paper_validation/preprocessing/page_manifest.json`, `native_layout_quality_report.json`, and `ocr_backend.json` |
| `main_text_extractor` | `.ai_paper_validation/document_outputs/doc-799606a72443/main_article_evidence_inventory.json` |
| `results_supplement_extractor` | `.ai_paper_validation/document_outputs/doc-b45e07a04d82/results_supplement_evidence_map.json` |
| `table_arithmetic_checker` | `.ai_paper_validation/checks/table_arithmetic/table_arithmetic_report.json` |
| `figure_flow_checker` | `.ai_paper_validation/checks/figure_flow/figure_flow_candidates.md` |
| `statistical_consistency_checker` | `.ai_paper_validation/checks/statistical_consistency/statistical_consistency_candidates.json` and `.md` |
| `evidence_verifier` | Verified evidence cards are preserved verbatim in the final report’s two Scientific issues; both candidates were verified in two rounds |
| `critic` | Retained both verified issues as Minor Presentation inconsistencies; final order and tightened cards are preserved in the final report |
| `report_generator` | `.ai_paper_validation/final/human_adjudication_report.md` |

The protocol, SAP, and administrative documents are scientifically `Not Audited by Design`; their document records preserve that explicit disposition for preprocessing, extraction, and scientific checks. Their mandatory AI Training Restriction records are complete.

