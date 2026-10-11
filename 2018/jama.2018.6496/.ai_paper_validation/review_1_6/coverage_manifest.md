# Workflow 1.6 Coverage Manifest

Created before scientific mapping. Assignments cover every direct-source unit. Candidate and statistical scopes will be replaced with explicit stable IDs after their inventories exist. Planned scopes are not completion claims.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-25; DOC-003 PDF pp. 1-13 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All reusable native/layout text and rendered page assets; exact coverage and fresh-required partition | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11, all reusable-backed and fresh-required units | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-25; DOC-003 PDF pp. 1-13, all reusable-backed and fresh-required units | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-main-001 | M001 through M100, assigned numeric IDs N001 through N100, 100 disjoint relationship groups | checkers/parts/numeric_main.md | COMPLETE |
| numeric_checks | numeric-support-001 | M101 through M124 and U001 through U067, assigned numeric IDs N101 through N191, 91 disjoint relationship groups | checkers/parts/numeric_support.md | COMPLETE |
| numeric_checks | numeric-main-inventory | M001 through M100, N001 through N100 | relationships/parts/numeric_main.md | COMPLETE |
| numeric_checks | numeric-support-inventory | M101 through M124 and U001 through U067, N101 through N191 | relationships/parts/numeric_support.md | COMPLETE |
| numeric_checks | numeric-canonical | Full union of 191 numeric relationship groups, canonical merge | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-inventory-canonical | Full union of 191 numeric relationship groups, canonical inventory | relationships/numeric_relationship_inventory.md | COMPLETE |
| statistics_pass_1 | stat1-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | Every repeated or matched quantitative relationship across REPORT and PLAN sources | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stat2-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | audit-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010; all 49 pages and complete relationship inventories | quality/evidence_quality_audit.md | COMPLETE |
| evidence_quality | coverage-audit-support | All 49 source units, 191 N inventory groups in bounded sections of 100 and 91, and 93 S groups; no candidate-card IDs assigned to this additional shard | quality/parts/coverage_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010; complete scope and classifications | ../final_report_1_6.md | COMPLETE |
