# Agent Response Index

| Workflow agent | Retained response/artifact | Disposition |
|---|---|---|
| package_inventory | `package_manifest.md`; per-document `inventory.md` | Complete |
| ai_use_restriction_checker — DOC-001 | `document_outputs/DOC-001/ai_training_restriction_record.md` | Explicit AI Training Restriction; approval later confirmed |
| ai_use_restriction_checker — DOC-002 | `document_outputs/DOC-002/ai_training_restriction_record.md` | No restriction located; scientific audit Not Audited by Design |
| ai_use_restriction_checker — DOC-003 | `document_outputs/DOC-003/ai_training_restriction_record.md` | Explicit AI Training Restriction; approval later confirmed |
| pdf_preprocessor | DOC-001 and DOC-003 `preprocessing_record.md` and `preprocessing_page_manifest.json` | Complete |
| main_text_extractor | `document_outputs/DOC-001/main_text_extractor_response.md` | Complete; no standalone main-text candidate |
| results_supplement_extractor | `document_outputs/DOC-003/results_supplement_extractor_response.md` | Complete; eTable 6 title/body candidate raised |
| table_arithmetic_checker | `table_arithmetic_checker_response.md` | Two candidates raised |
| figure_flow_checker | `figure_flow_checker_response.md` | Eight presentation/flow candidates raised; lower-priority items not shortlisted |
| statistical_consistency_checker | `statistical_consistency_checker_response.md` | Nine candidates raised, including overlaps |
| evidence_verifier | `verification_results.md` | 9 Verified; 1 Uncertain; 0 Rejected |
| critic | `critic_review.md` | 8 retained; 1 Uncertain; 1 Rejected |
| report_generator | `final_report.md` | Final human-adjudication report |

DOC-002 has an explicit `Not Audited by Design` processing record at `document_outputs/DOC-002/processing_status.md`.

