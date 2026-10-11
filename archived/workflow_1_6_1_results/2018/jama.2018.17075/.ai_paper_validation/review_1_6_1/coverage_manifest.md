# Complete coverage manifest

Artifacts are relative to this run directory. Each source-unit mapping scope is disjoint. Checker scopes are complete relationship scopes rather than source rediscovery. Exact statistical relationship and candidate scopes are enumerated after complete mapping and independent screening.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-001 | DOC-001 pp. 1-10; DOC-002 pp. 1-194; DOC-003 pp. 1-24; DOC-004 p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All eligible reusable text, image and metadata assets and each direct-source coverage gap | evidence_asset_inventory.md | COMPLETE |
| evidence_assets | coverage-001 | All four source-unit coverage rows | source_coverage.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 pp. 1-10 | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | plan-001 | DOC-002 pp. 1-69 | extraction/parts/plan_001.md | COMPLETE |
| support_evidence_mapping | plan-002 | DOC-002 pp. 70-138 | extraction/parts/plan_002.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 pp. 139-194; DOC-003 pp. 1-24; DOC-004 p. 1 | extraction/parts/support_003.md | COMPLETE |
| support_evidence_mapping | support-merged | Lossless merge of all three support mapping parts | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001 through N084 and N085 through N140; all underlying mapped cells | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | stat-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | All matched REPORT and PLAN result-relevant relationships | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screen-001 | Every emitted finding from all three initial checkers | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | ledger-001 | C001, C002, C003, C004 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stat-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004; all screening decisions, exclusions and coverage units | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004; complete package scope | ../final_report_1_6_1.md | PENDING |
| numeric_checks | numeric-part-001 | N001 through N084; all underlying mapped source cells | checkers/parts/numeric_001.md | COMPLETE |
| numeric_checks | numeric-part-002 | N085 through N140; all underlying mapped source cells | checkers/parts/numeric_002.md | COMPLETE |
| evidence_assets | numeric-inventory | All 140 numeric rows reconstructed from fresh source-linked mapping | relationships/numeric_relationship_inventory.md | COMPLETE |
| evidence_assets | stat-inventory | All 110 statistical rows reconstructed from fresh source-linked mapping | statistics/relationship_inventory.md | COMPLETE |
| evidence_assets | id-crosswalk | All provisional mapper rows transferred without selection | relationships/id_crosswalk.md | COMPLETE |
| inclusion_screening | screen-visual-001 | DOC-001 p.5 exact-source visual confirmation | preprocessing/screening/main-p5.png | COMPLETE |
| inclusion_screening | screen-visual-002 | DOC-003 p.11 exact-source visual confirmation | preprocessing/screening/results-p11.png | COMPLETE |
| evidence_assets | recheck-main-p1-txt | Exact source page main-p1 recheck derivative | preprocessing/recheck/main-p1.txt | COMPLETE |
| evidence_assets | recheck-main-p1-png | Exact source page main-p1 recheck derivative | preprocessing/recheck/main-p1.png | COMPLETE |
| evidence_assets | recheck-main-p3-txt | Exact source page main-p3 recheck derivative | preprocessing/recheck/main-p3.txt | COMPLETE |
| evidence_assets | recheck-main-p3-png | Exact source page main-p3 recheck derivative | preprocessing/recheck/main-p3.png | COMPLETE |
| evidence_assets | recheck-main-p4-txt | Exact source page main-p4 recheck derivative | preprocessing/recheck/main-p4.txt | COMPLETE |
| evidence_assets | recheck-main-p4-png | Exact source page main-p4 recheck derivative | preprocessing/recheck/main-p4.png | COMPLETE |
| evidence_assets | recheck-main-p5-txt | Exact source page main-p5 recheck derivative | preprocessing/recheck/main-p5.txt | COMPLETE |
| evidence_assets | recheck-main-p5-png | Exact source page main-p5 recheck derivative | preprocessing/recheck/main-p5.png | COMPLETE |
| evidence_assets | recheck-main-p7-txt | Exact source page main-p7 recheck derivative | preprocessing/recheck/main-p7.txt | COMPLETE |
| evidence_assets | recheck-main-p7-png | Exact source page main-p7 recheck derivative | preprocessing/recheck/main-p7.png | COMPLETE |
| evidence_assets | recheck-plan-p77-txt | Exact source page plan-p77 recheck derivative | preprocessing/recheck/plan-p77.txt | COMPLETE |
| evidence_assets | recheck-plan-p77-png | Exact source page plan-p77 recheck derivative | preprocessing/recheck/plan-p77.png | COMPLETE |
| evidence_assets | recheck-plan-p101-txt | Exact source page plan-p101 recheck derivative | preprocessing/recheck/plan-p101.txt | COMPLETE |
| evidence_assets | recheck-plan-p101-png | Exact source page plan-p101 recheck derivative | preprocessing/recheck/plan-p101.png | COMPLETE |
| evidence_assets | recheck-results-p10-txt | Exact source page results-p10 recheck derivative | preprocessing/recheck/results-p10.txt | COMPLETE |
| evidence_assets | recheck-results-p10-png | Exact source page results-p10 recheck derivative | preprocessing/recheck/results-p10.png | COMPLETE |
| evidence_assets | recheck-results-p11-txt | Exact source page results-p11 recheck derivative | preprocessing/recheck/results-p11.txt | COMPLETE |
| evidence_assets | recheck-results-p11-png | Exact source page results-p11 recheck derivative | preprocessing/recheck/results-p11.png | COMPLETE |
