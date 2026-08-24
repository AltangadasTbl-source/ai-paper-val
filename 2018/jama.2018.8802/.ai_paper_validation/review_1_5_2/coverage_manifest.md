# Workflow 1.5.2 Coverage Manifest

This manifest was created after direct-source inventory and before scientific extraction. Pending scopes are replaced with explicit stable relationship/candidate IDs as those identities are assigned.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001, DOC-002, DOC-003 direct-source identities, page counts, sizes, roles, and hashes | source_inventory.md | COMPLETE |
| source_inventory | source-002 | DOC-001, DOC-002, DOC-003 pre-run SHA-256 records | source_hashes_before.sha256 | COMPLETE |
| evidence_assets | assets-001 | DOC-001 pp. 1-10; DOC-002 pp. 1-25; DOC-003 pp. 1-9 fresh native text, layout text, render/OCR decisions | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10 | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 provisional numeric relationships MN001 through MN041 | relationships/parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 provisional statistical relationships MS001 through MS024 | statistics/parts/main_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-25; DOC-003 PDF pp. 1-9 | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 and DOC-003 provisional numeric relationships UN001 through UN031 | relationships/parts/support_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 and DOC-003 provisional statistical relationships US001 through US037 | statistics/parts/support_statistical_relationships.md | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061, N062, N063, N064, N065, N066, N067, N068, N069, N070, N071, N072 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-source-001 | All mapped DOC-001, DOC-002, and DOC-003 internal and cross-document match keys from N001-N072 and S001-S061 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006, C007, C008 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061; C001, C002, C003, C004, C005, C006, C007, C008; complete cross-lane ledger and recheck facts | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008; every coverage row; every source-coverage row; all statistical executions | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008 and complete run metadata | report_generation.md | COMPLETE |
