# Coverage Manifest

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001, DOC-002, DOC-003 complete direct-source inventory | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | DOC-001 pp. 1-9; DOC-002 pp. 1-134; DOC-003 pp. 1-3 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-9 | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 shard-local numeric relationships MN001-MN029 | relationships/parts/main_numeric.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 shard-local statistical relationships MS001-MS017 | statistics/parts/main_statistical.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-134 and DOC-003 PDF pp. 1-3 canonical merge | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 PDF pp. 1-50 | extraction/parts/support_001_pp001_050.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 pp. 1-50 numeric relationships S1N001-S1N017 | relationships/parts/support_001_numeric.md | COMPLETE |
| support_evidence_mapping | support-004 | DOC-002 pp. 1-50 statistical relationships S1S001-S1S014 | statistics/parts/support_001_statistical.md | COMPLETE |
| support_evidence_mapping | support-005 | DOC-002 PDF pp. 51-100 | extraction/parts/support_002_pp051_100.md | COMPLETE |
| support_evidence_mapping | support-006 | DOC-002 pp. 51-100 numeric relationships S2N001-S2N038 | relationships/parts/support_002_numeric.md | COMPLETE |
| support_evidence_mapping | support-007 | DOC-002 pp. 51-100 statistical relationships S2S001-S2S014 | statistics/parts/support_002_statistical.md | COMPLETE |
| support_evidence_mapping | support-008 | DOC-002 PDF pp. 101-134 and DOC-003 PDF pp. 1-3 | extraction/parts/support_003_pp101_134_doc003.md | COMPLETE |
| support_evidence_mapping | support-009 | DOC-002 pp. 101-134 and DOC-003 pp. 1-3 numeric relationships S3N001-S3N014 | relationships/parts/support_003_numeric.md | COMPLETE |
| support_evidence_mapping | support-010 | DOC-002 pp. 101-134 and DOC-003 pp. 1-3 statistical relationships S3S001-S3S010 | statistics/parts/support_003_statistical.md | COMPLETE |
| main_evidence_mapping | main-004 | N001-N098 canonical numeric relationship inventory | relationships/numeric_relationship_inventory.md | COMPLETE |
| support_evidence_mapping | support-011 | S001-S055 canonical statistical relationship inventory | statistics/relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-001 | All N001-N098 relationships in the completed numeric inventory | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | All N001-N098 and S001-S055 matched main/support relationships | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055; complete cross-lane ledger C001, C002, C003, C004 and recheck facts | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004; all coverage rows, all source rows, and execution manifest | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004 and complete provenance metadata | ../final_report_1_5_2.md | COMPLETE |
