# Workflow 1.5.3 Coverage Manifest

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001, DOC-002, and DOC-003; 203 PDF pages | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | 61 reusable source-linked artifacts covering 29 unique PDF pages | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11 | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-25 | extraction/parts/support_doc002_pp001-025.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-003 PDF pp. 1-32 | extraction/parts/support_doc003_pp001-032.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-003 PDF pp. 33-64 | extraction/parts/support_doc003_pp033-064.md | COMPLETE |
| support_evidence_mapping | support-004 | DOC-003 PDF pp. 65-96 | extraction/parts/support_doc003_pp065-096.md | COMPLETE |
| support_evidence_mapping | support-005 | DOC-003 PDF pp. 97-128 | extraction/parts/support_doc003_pp097-128.md | COMPLETE |
| support_evidence_mapping | support-006 | DOC-003 PDF pp. 129-160 | extraction/parts/support_doc003_pp129-160.md | COMPLETE |
| support_evidence_mapping | support-007 | DOC-003 PDF pp. 161-167 | extraction/parts/support_doc003_pp161-167.md | COMPLETE |
| support_evidence_mapping | support-merge | Complete union of support-001 through support-007 | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | 68 matched result clusters across DOC-001, DOC-002, and DOC-003 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017 | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017 | ../final_report_1_5_3.md | COMPLETE |

Each row contains exactly one plain package-review-relative artifact path. Support page shards are
disjoint and their union covers every support-source page without sampling.
