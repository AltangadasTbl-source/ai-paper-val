# Workflow 1.6.1 Coverage Manifest

Assignments established before scientific mapping. Physical PDF pages are one-based. Every page is assigned exactly once to a mapper; reusable assets locate evidence, and DOC-002 page 134 requires fresh direct rendering. Later relationship and candidate scopes will be enumerated after their inventories exist. Each artifact cell contains one plain path relative to this review directory.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 pages 1-9; DOC-002 pages 1-134; DOC-003 pages 1-3 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All 104 inventoried reusable assets; exact paths A001-A104 in asset inventory | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 pages 1-9; all reusable-backed | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-original | DOC-002 pages 1-56; all reusable-backed | extraction/parts/support_original_plan.md | COMPLETE |
| support_evidence_mapping | support-final | DOC-002 pages 57-134; reusable-backed 57-133; fresh-required 134; DOC-003 pages 1-3 reusable-backed | extraction/parts/support_final_plan_results.md | COMPLETE |
| support_evidence_mapping | support-merged | Lossless union of support-original and support-final scopes | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | DOC-001 complete mapped numeric scope N001-N098 and numeric implications of its statistical tuples | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-inventory | N001-N155 complete union of 98 main and 57 support relationships | relationships/numeric_relationship_inventory.md | COMPLETE |
| statistics_pass_1 | stats-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033 | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | stats-inventory | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033 | statistics/relationship_inventory.md | COMPLETE |
| cross_source_checks | cross-001 | All matched report and plan quantitative/design relationships | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screen-001 | F-NUM-001, F-XS-001, F-XS-002, F-ST1-001, F-ST1-002, F-ST1-003 | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stats-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004; all coverage and screening decisions; all checker exclusions | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004; complete review metadata and screening summaries | ../final_report_1_6_1.md | COMPLETE |
| numeric_checks | numeric-support | All DOC-002 and DOC-003 numeric support relationships; up to 71 mapped relationship groups | checkers/parts/numeric_support.md | COMPLETE |
| numeric_checks | numeric-support-inventory | All DOC-002 and DOC-003 numeric support relationships | relationships/parts/numeric_support_inventory.md | COMPLETE |
