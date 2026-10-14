# Workflow 1.6.2 Coverage Manifest

Created before scientific mapping. Every direct source page is assigned exactly once to a current mapper. Reusable-backed and fresh-required units partition source coverage; all 115 pages are reusable-backed at inventory. Support scope is split because the preferred complete text is approximately 214079 characters, above the 200000-character context bound. The PLAN shard is approximately 142351 characters and the results shard 71728. Rendered pages are inspected selectively to resolve text or layout; each rendering wave is bounded at 32 pages. Coordinator merges support parts losslessly after both mapping agents finish.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 pp. 1-10; DOC-002 pp. 1-40; DOC-003 pp. 1-31; DOC-004 pp. 1-34 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | 569 reusable extraction and image assets across all 115 pages | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10, all result-relevant content and explicit no-applicable units | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | results-001 | DOC-004 PDF pp. 1-34, all result-relevant content and explicit no-applicable units | extraction/support_results_part.md | COMPLETE |
| support_evidence_mapping | plans-001 | DOC-002 PDF pp. 1-40 and DOC-003 PDF pp. 1-31, complete PLAN definitions including visual mapping of DOC-002 pp. 32-33 | extraction/support_plans_part.md | COMPLETE |
| support_evidence_mapping | support-merge | Lossless assembly of results-001 and plans-001 | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001-N110, complete 110 canonical numeric groups | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-inventory | Complete numeric relationship inventory | relationships/numeric_relationship_inventory.md | COMPLETE |
| cross_source_checks | cross-source-001 | Every in-scope matched result and PLAN-REPORT design relationship | checkers/cross_source_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080 | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | statistical-inventory | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080 | statistics/relationship_inventory.md | COMPLETE |
| inclusion_screening | screening-001 | F-XS-001, F-XS-002, F-XS-003, F-XS-004, F-XS-005, F-ST1-001, F-ST1-002, F-ST1-003, F-ST1-004, F-ST1-005 | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | ledger-001 | C001, C002, C003 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080; every checker exclusion | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | audit-001 | C001, C002, C003; every coverage unit, screening decision and checker exclusion | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003; complete review scope | ../final_report_1_6_2.md | COMPLETE |
| evidence_quality | coverage-audit-shard | All DOC-001 pp. 1-10, DOC-002 pp. 1-40, DOC-003 pp. 1-31, DOC-004 pp. 1-34 and N001-N110 mapping/coverage; candidate audit is assigned separately | quality/coverage_audit_part.md | COMPLETE |
| evidence_quality | screening-audit-shard | Seven screened-out first-pass findings and all 36 checker exclusions; stable candidate inclusion assigned separately | quality/screening_audit_part.md | COMPLETE |
