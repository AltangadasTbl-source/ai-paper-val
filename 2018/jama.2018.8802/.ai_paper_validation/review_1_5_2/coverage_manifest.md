# Coverage Manifest

This plan was initialized before scientific extraction. Source scopes are disjoint by supplied PDF and page.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 main PDF pp. 1-10; DOC-002 supplement 1 PDF pp. 1-25; DOC-003 supplement 2 PDF pp. 1-9 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | DOC-001 PDF pp. 1-10; fresh native text and coordinate layout for all 10 pages | evidence_asset_inventory.md | COMPLETE |
| evidence_assets | assets-002 | DOC-002 PDF pp. 1-25; fresh native text and coordinate layout for all 25 pages | evidence_asset_inventory.md | COMPLETE |
| evidence_assets | assets-003 | DOC-003 PDF pp. 1-9; fresh native text and coordinate layout for all 9 pages | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10; MN001-MN030 and MS001-MS027 complete evidence | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 PDF pp. 1-10; provisional MN001-MN030 index | relationships/parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 PDF pp. 1-10; provisional MS001-MS027 records | statistics/parts/main_statistical_relationships.md | COMPLETE |
| main_evidence_mapping | main-004 | Canonical N001-N061 merged mapping | relationships/numeric_relationship_inventory.md | COMPLETE |
| main_evidence_mapping | main-005 | Canonical S001-S067 merged mapping | statistics/relationship_inventory.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-25 and DOC-003 PDF pp. 1-9; UN001-UN031 and US001-US040 complete evidence | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 PDF pp. 1-25 and DOC-003 PDF pp. 1-9; provisional UN001-UN031 records | relationships/parts/support_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 PDF pp. 1-25 and DOC-003 PDF pp. 1-9; provisional US001-US040 records | statistics/parts/support_statistical_relationships.md | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | stat1-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | N001-N061 and S001-S067 matched across DOC-001, DOC-002, and DOC-003 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stat2-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067; C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011; every source and coverage row; both statistical executions | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011 | ../final_report_1_5_2.md | COMPLETE |
| report_generation | report-002 | Complete 11-card Markdown assembly handoff | report_generation.md | COMPLETE |
