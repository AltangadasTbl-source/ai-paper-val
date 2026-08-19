# Workflow 1.5.3 Coverage Manifest

This manifest was created before scientific mapping. Page ranges are disjoint within each mapping stage. Candidate- and relationship-ID scopes will be replaced with the complete explicit stable-ID lists after registration; no count limit applies.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 through DOC-006; all six direct PDFs; 404 PDF pages | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | 65 source-linked reusable artifacts covering DOC-001 pp. 1-12 and DOC-004 pp. 1-26 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-12; reusable-backed | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-76; fresh-required | extraction/parts/support_doc002_p001_p076.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 PDF pp. 77-152; fresh-required | extraction/parts/support_doc002_p077_p152.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 PDF pp. 153-229; fresh-required | extraction/parts/support_doc002_p153_p229.md | COMPLETE |
| support_evidence_mapping | support-004 | DOC-003 PDF pp. 1-65; fresh-required | extraction/parts/support_doc003_p001_p065.md | COMPLETE |
| support_evidence_mapping | support-005 | DOC-003 PDF pp. 66-130; fresh-required | extraction/parts/support_doc003_p066_p130.md | COMPLETE |
| support_evidence_mapping | support-006 | DOC-004 PDF pp. 1-26 reusable-backed; DOC-005 PDF pp. 1-6 fresh-required; DOC-006 PDF p. 1 fresh-required | extraction/parts/support_doc004_doc005_doc006.md | COMPLETE |
| support_evidence_mapping | support-merge | Complete disjoint union of support-001 through support-006 | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | Every matched main/support quantitative result across DOC-001 through DOC-006 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006, C007, C008 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008 plus every coverage row | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008 | ../final_report_1_5_3.md | COMPLETE |
