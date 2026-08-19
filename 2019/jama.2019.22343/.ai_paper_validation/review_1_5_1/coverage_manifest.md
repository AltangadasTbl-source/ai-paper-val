# Coverage Manifest

The inventory, asset, and mapping rows are complete and use a disjoint union of all direct-source pages. Each Artifact cell contains exactly one plain relative path.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-15; DOC-003 PDF pp. 1-49 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | 89 existing reusable preprocessing, rendered-page, manifest, document-record, and source-location-map files; mapped to DOC-001 pp. 1-11, DOC-002 no reusable scientific pages, and DOC-003 pp. 17-45 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11; complete quantitative map | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 PDF pp. 1-11; provisional numeric relationships MN001-MN013 | parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 PDF pp. 1-11; provisional statistical relationships MS001-MS043 | parts/main_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-15 and DOC-003 PDF pp. 1-49; complete quantitative map | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 PDF pp. 1-15 and DOC-003 PDF pp. 1-49; provisional numeric relationships SN001-SN014 | parts/support_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 PDF pp. 1-15 and DOC-003 PDF pp. 1-49; provisional statistical relationships SS001-SS014 | parts/support_statistical_relationships.md | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | stat1-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | All 31 matched result sets across DOC-001, DOC-002, and DOC-003 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stat2-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006 | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006 | ../final_report_1_5_1.md | COMPLETE |
