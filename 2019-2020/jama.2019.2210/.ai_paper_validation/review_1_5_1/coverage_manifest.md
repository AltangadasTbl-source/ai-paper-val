# Workflow 1.5.1 Coverage Manifest

This manifest was created before scientific mapping. Source/evidence assignments are disjoint by PDF page; relationship and candidate scopes will be replaced with explicit stable IDs after registration. Every artifact cell contains one plain review-directory-relative path.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 PDF pp. 1-9; DOC-002 PDF pp. 1-45; DOC-003 PDF pp. 1-41; DOC-004 PDF p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | reuse-001 | Reusable asset fitness and page coverage for all four direct sources | evidence_asset_inventory.md | COMPLETE |
| evidence_assets | reuse-002 | SHA-256 baseline for 289 reused artifacts | reused_artifact_hashes_before.sha256 | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-9; reusable pp. 1-8 and fresh-required p. 9 | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 numeric relationships | parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 statistical relationships | parts/main_statistical_relationships.md | COMPLETE |
| main_evidence_mapping | relationship-merge-001 | Stable numeric IDs N001 through N089 from the complete mapper union | relationships/numeric_relationship_inventory.md | COMPLETE |
| main_evidence_mapping | relationship-merge-002 | Stable statistical IDs S001 through S083 from the complete mapper union | statistics/relationship_inventory.md | COMPLETE |
| support_evidence_mapping | protocol-001 | DOC-002 PDF pp. 1-45 and DOC-004 PDF p. 1; all fresh-required | parts/support_protocol_evidence.md | COMPLETE |
| support_evidence_mapping | protocol-002 | DOC-002 and DOC-004 numeric relationships | parts/support_protocol_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | protocol-003 | DOC-002 and DOC-004 statistical relationships | parts/support_protocol_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | results-a-001 | DOC-003 PDF pp. 1-21; reusable current native text | parts/support_results_a_evidence.md | COMPLETE |
| support_evidence_mapping | results-a-002 | DOC-003 PDF pp. 1-21 numeric relationships | parts/support_results_a_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | results-a-003 | DOC-003 PDF pp. 1-21 statistical relationships | parts/support_results_a_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | results-b-001 | DOC-003 PDF pp. 22-41; reusable current native text | parts/support_results_b_evidence.md | COMPLETE |
| support_evidence_mapping | results-b-002 | DOC-003 PDF pp. 22-41 numeric relationships | parts/support_results_b_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | results-b-003 | DOC-003 PDF pp. 22-41 statistical relationships | parts/support_results_b_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-merge-001 | Complete union of DOC-002 pp. 1-45, DOC-003 pp. 1-41, and DOC-004 p. 1 | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061, N062, N063, N064, N065, N066, N067, N068, N069, N070, N071, N072, N073, N074, N075, N076, N077, N078, N079, N080, N081, N082, N083, N084, N085, N086, N087, N088, N089 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-source-001 | All matched results and definitions among DOC-001, DOC-002, DOC-003, and DOC-004 across N001-N089 and S001-S083 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | registration-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009 | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009 | ../final_report_1_5_1.md | COMPLETE |
| report_generation | report-002 | C001, C002, C003, C004, C005, C006, C007, C008, C009 | parts/report_generation_status.md | COMPLETE |
