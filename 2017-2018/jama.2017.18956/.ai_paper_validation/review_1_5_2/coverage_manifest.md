# Workflow 1.5.2 Coverage Manifest

Artifacts are plain paths relative to `.ai_paper_validation/review_1_5_2/`. Scientific scopes are disjoint at mapping and complete at each later checker stage.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 pp. 1-8; DOC-002 pp. 1-16; DOC-003 pp. 1-4 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Fresh native and layout text for DOC-001 pp. 1-8, DOC-002 pp. 1-16, DOC-003 pp. 1-4; rendered result displays on 14 documented pages; OCR decision for all 28 pages | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-8 | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-16; DOC-003 PDF pp. 1-4 | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001-N072 across DOC-001, DOC-002, and DOC-003 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | All 14 documented matched-result groups across DOC-001, DOC-002, and DOC-003 after population, time, contrast, model, measure, and precision matching | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | registration-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050; complete C001-C010 ledger and recheck facts | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010; every coverage row; all DOC-001, DOC-002, DOC-003 source-coverage rows; both fresh statistical executions | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010; all required provenance, coverage, limitations, execution, performance, token, and cost metadata | ../final_report_1_5_2.md | COMPLETE |
