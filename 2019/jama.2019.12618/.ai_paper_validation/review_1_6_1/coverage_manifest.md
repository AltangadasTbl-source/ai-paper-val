# Workflow 1.6.1 Coverage Manifest

This plan was created before scientific mapping. Units are disjoint by source and PDF page. Shards respect the 200000-character input bound. Runtime agent identifiers are canonical task names with the initial slash omitted for the validator-compatible identifier column.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | All five supplied PDFs, 263 PDF pages | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Every source-linked reusable asset and all uncovered units | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | Main article PDF pp. 1-10 | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | supp1 PDF pp. 1-16; supp3 PDF pp. 65-83; supp4 PDF p. 1 | extraction/parts/support_results_sap_tail.md | COMPLETE |
| support_evidence_mapping | support-002 | supp3 PDF pp. 1-64 | extraction/parts/sap_001_064.md | COMPLETE |
| support_evidence_mapping | support-003 | supp2 PDF pp. 1-64, fresh visual pages 15, 18, 19, 47 | extraction/parts/protocol_001_064.md | COMPLETE |
| support_evidence_mapping | support-004 | supp2 PDF pp. 65-128, fresh visual pages 74, 80, 81, 84, 89, 90, 91, 94, 96, 105, 107, 109, 116, 118, 120 | extraction/parts/protocol_065_128.md | COMPLETE |
| support_evidence_mapping | support-005 | supp2 PDF pp. 129-153, fresh visual pages 129, 133, 134, 136, 150 | extraction/parts/protocol_129_153.md | COMPLETE |
| support_evidence_mapping | support-merged | Lossless merge of all five disjoint support parts | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | All main-report numeric rows, DOC-002 pp. 3-9 and 13, all PLAN arithmetic; merge complete supplement shard | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistical-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | All matched report and plan relationships | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screen-001 | F-NUM-001, F-XS-001, F-XS-002, F-ST1-001, F-ST1-002 | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistical-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002; every finding decision, checker exclusion and complete source coverage | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002; complete review scope | ../final_report_1_6_1.md | COMPLETE |
| support_evidence_mapping | sap-formula-repair | DOC-004 fresh direct visual formula confirmation PDF pp. 22, 23, 24, 26, 34, 63, 64 | extraction/parts/sap_formula_visual_confirmation.md | COMPLETE |
| support_evidence_mapping | checker-map-handoff | All structured mapping sections and page coverage; duplicate transcription appendices omitted | extraction/checker_input_maps.md | COMPLETE |
| numeric_checks | numeric-inventory | Every stable numeric relationship assigned by numeric checker | relationships/numeric_relationship_inventory.md | COMPLETE |
| statistics_pass_1 | statistics-inventory | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077 | statistics/relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-supplement-shard | DOC-002 eTables 4, 5, 6, 8, 9 PDF pp. 10, 11, 12, 14, 15, 16 all rows and percentages | checkers/parts/numeric_supplement.md | COMPLETE |
| numeric_checks | numeric-supplement-inventory | DOC-002 eTables 4, 5, 6, 8, 9 PDF pp. 10, 11, 12, 14, 15, 16 all numeric relationships | relationships/parts/numeric_supplement_inventory.md | COMPLETE |
| inclusion_screening | screen-source-confirmation | Main PDF p.6 direct source visual confirmation for F-ST1-001 and F-XS-002 | screening/preprocessing/main-p6.png | COMPLETE |
| support_evidence_mapping | protocol-b1-context-repair | DOC-003 PDF pp. 65-96 bounded complete confirmation using retained current text/images/OCR | extraction/parts/protocol_065_096_bounded_confirmation.md | COMPLETE |
| support_evidence_mapping | protocol-b2-context-repair | DOC-003 PDF pp. 97-128 bounded complete confirmation using retained current text/images/OCR | extraction/parts/protocol_097_128_bounded_confirmation.md | COMPLETE |
| support_evidence_mapping | protocol-a1-context-repair | DOC-003 PDF pp. 1-32 bounded complete confirmation using retained current text/images/OCR | extraction/parts/protocol_001_032_bounded_confirmation.md | COMPLETE |
| support_evidence_mapping | protocol-a2-context-repair | DOC-003 PDF pp. 33-64 bounded complete confirmation using retained current text/images | extraction/parts/protocol_033_064_bounded_confirmation.md | COMPLETE |
