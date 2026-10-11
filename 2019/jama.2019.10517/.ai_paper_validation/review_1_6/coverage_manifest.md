# Workflow 1.6 Coverage Manifest

Mapping assignments cover disjoint direct-source units. Reuse is an extraction optimization; all units receive a new quantitative map. The 42-page plan is split because its combined native text already exceeds 200,000 bytes before results-support content is added. Every artifact cell contains one plain path relative to this run directory.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 PDF pp. 1-10; DOC-002 PDF pp. 1-42; DOC-003 PDF pp. 1-10; DOC-004 PDF p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All eligible source-linked reusable extraction and page assets | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10 | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-21; DOC-003 PDF pp. 1-10; DOC-004 PDF p. 1 | extraction/parts/support_first_and_results.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 PDF pp. 22-42 | extraction/parts/support_plan_second.md | COMPLETE |
| support_evidence_mapping | support-merged | Complete union of support-001 and support-002 | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-report-first | DOC-001 pp. 1-6 printed quantities and definitions; counterparts used only to match these quantities | checkers/parts/numeric_report_first.md | COMPLETE |
| numeric_checks | numeric-report-last | DOC-001 pp. 7-10 and DOC-003 pp. 1-10 printed quantities; counterparts used only to match these quantities | checkers/parts/numeric_report_last.md | COMPLETE |
| numeric_checks | numeric-plan-first | DOC-002 pp. 1-21 printed quantities and rules; counterparts used only to match these quantities | checkers/parts/numeric_plan_first.md | COMPLETE |
| numeric_checks | numeric-plan-last | DOC-002 pp. 22-42 printed quantities and rules; DOC-004 p. 1 no-applicable quantitative content | checkers/parts/numeric_plan_last.md | COMPLETE |
| numeric_checks | numeric-merged | Complete union of four disjoint numeric origins | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | stats-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | Every matched quantitative source relationship | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stats-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015 | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015 | ../final_report_1_6.md | COMPLETE |
| numeric_checks | inventory-report-first | DOC-001 pp. 1-6; N001 through N096 with complete individual rows in inventory | relationships/parts/numeric_report_first.md | COMPLETE |
| numeric_checks | inventory-report-last | DOC-001 pp. 7-10 and DOC-003 pp. 1-10; 83 relationship origins | relationships/parts/numeric_report_last.md | COMPLETE |
| numeric_checks | inventory-plan-first | DOC-002 pp. 1-21; 105 relationship origins | relationships/parts/numeric_plan_first.md | COMPLETE |
| numeric_checks | inventory-plan-last | DOC-002 pp. 22-42 and DOC-004 p. 1; 116 relationship origins | relationships/parts/numeric_plan_last.md | COMPLETE |
| numeric_checks | inventory-merged | All 400 numeric relationships with contiguous stable IDs and preserved aliases | relationships/numeric_relationship_inventory.md | COMPLETE |
| evidence_assets | recheck-derivative-001 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p1-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-002 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p1-native.txt | COMPLETE |
| evidence_assets | recheck-derivative-003 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p4-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-004 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p5-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-005 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p5.png | COMPLETE |
| evidence_assets | recheck-derivative-006 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p6-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-007 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p6.png | COMPLETE |
| evidence_assets | recheck-derivative-008 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p7-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-009 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p8-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-010 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p8-native.txt | COMPLETE |
| evidence_assets | recheck-derivative-011 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p8.png | COMPLETE |
| evidence_assets | recheck-derivative-012 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p9-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-013 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-main-p9.png | COMPLETE |
| evidence_assets | recheck-derivative-014 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p10-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-015 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p11-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-016 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p12-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-017 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p13-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-018 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p14-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-019 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p15-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-020 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p17-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-021 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p21-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-022 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p29-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-023 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p29.png | COMPLETE |
| evidence_assets | recheck-derivative-024 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p4-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-025 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p40-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-026 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p41-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-027 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p7-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-028 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-plan-p9-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-029 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-results-p10-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-030 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-results-p10.png | COMPLETE |
| evidence_assets | recheck-derivative-031 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-results-p9-layout.txt | COMPLETE |
| evidence_assets | recheck-derivative-032 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-results-p9.png | COMPLETE |
| evidence_assets | recheck-derivative-033 | Exact-source selected page named in artifact; provenance in evidence_asset_inventory.md | preprocessing/recheck-sharing-p1-layout.txt | COMPLETE |
