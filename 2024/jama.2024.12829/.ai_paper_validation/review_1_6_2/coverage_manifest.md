# Coverage Manifest

Source and mapping assignments were created before scientific mapping. Review-stage assignments were added before each stage. Status reflects durable artifacts. Every source unit is mapped; the final source-unit partition is 201 reusable and 2 fresh-required.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-001 | DOC-001 pp. 1-11; DOC-002 pp. 1-25; DOC-003 pp. 1-167 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All eligible source-linked reusable assets for 203 PDF pages | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11 | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | report-support-001 | DOC-002 PDF pp. 1-25 | extraction/parts/support_doc002_pp001-025.md | COMPLETE |
| support_evidence_mapping | plan-001 | DOC-003 PDF pp. 1-32 | extraction/parts/support_doc003_pp001-032.md | COMPLETE |
| support_evidence_mapping | plan-002 | DOC-003 PDF pp. 33-64 | extraction/parts/support_doc003_pp033-064.md | COMPLETE |
| support_evidence_mapping | plan-003 | DOC-003 PDF pp. 65-96 | extraction/parts/support_doc003_pp065-096.md | COMPLETE |
| support_evidence_mapping | plan-004 | DOC-003 PDF pp. 97-128 | extraction/parts/support_doc003_pp097-128.md | COMPLETE |
| support_evidence_mapping | plan-005 | DOC-003 PDF pp. 129-160 | extraction/parts/support_doc003_pp129-160.md | COMPLETE |
| support_evidence_mapping | plan-006 | DOC-003 PDF pp. 161-167 | extraction/parts/support_doc003_pp161-167.md | COMPLETE |
| support_evidence_mapping | support-merge | Lossless merge of all DOC-002 and DOC-003 evidence parts | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-all | All numeric relationships from main and seven support mappings; exact N IDs enumerated in numeric-ids rows | relationships/numeric_relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-findings | All numeric findings and self-screened observations | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistical-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120 | statistics/relationship_inventory.md | COMPLETE |
| statistics_pass_1 | statistical-002 | S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132 | statistics/relationship_inventory.md | COMPLETE |
| statistics_pass_1 | statistical-findings | F-ST1-001, F-ST1-002, F-ST1-003, F-ST1-004, F-ST1-005, F-ST1-006, F-ST1-007 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-all | All matched REPORT locations and PLAN design comparisons across 203 mapped pages | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screening-initial | F-NUM-001, F-NUM-002, F-NUM-003, F-NUM-004, F-XS-001, F-XS-002, F-XS-003, F-XS-004, F-ST1-001, F-ST1-002, F-ST1-003, F-ST1-004, F-ST1-005, F-ST1-006, F-ST1-007 | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | stable-candidates | C001, C002, C003, C004, C005, C006, C007 | candidate_ledger.md | COMPLETE |
| evidence_recheck | stable-candidates | C001, C002, C003, C004, C005, C006, C007 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistical-part-1 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120 | checkers/statistical_pass_2.md | COMPLETE |
| statistics_pass_2 | statistical-part-2 | S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | stable-candidates | C001, C002, C003, C004, C005, C006, C007 | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | stable-candidates | C001, C002, C003, C004, C005, C006, C007 | ../final_report_1_6_2.md | COMPLETE |
| numeric_checks | numeric-ids-1 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061, N062, N063, N064, N065, N066, N067, N068, N069, N070, N071, N072, N073, N074, N075, N076, N077, N078, N079, N080, N081, N082, N083, N084, N085, N086, N087, N088, N089, N090, N091, N092, N093, N094, N095, N096, N097, N098, N099, N100, N101, N102, N103, N104, N105, N106, N107, N108, N109, N110, N111, N112, N113, N114, N115, N116, N117, N118, N119, N120 | relationships/numeric_relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-ids-2 | N121, N122, N123, N124, N125, N126, N127, N128, N129, N130, N131 | relationships/numeric_relationship_inventory.md | COMPLETE |
