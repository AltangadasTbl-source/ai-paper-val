# Workflow 1.5.2 Coverage Manifest

Created before scientific extraction from the fresh asset inventory. Each stage assignment is disjoint within its stage; canonical merge artifacts are listed separately when produced.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-25; DOC-003 PDF pp. 1-13 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-25; DOC-003 PDF pp. 1-13 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11; provisional MN001-MN032 and MS001-MS024 merged to canonical inventories | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-25; DOC-003 PDF pp. 1-13; provisional UN001-UN015 and US001-US013 merged to canonical inventories | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001-N047 complete; discoveries NC-01, NC-02, NC-03, NC-04 retained for duplicate merge | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | N001-N047 and S001-S037; 118 matched occurrence comparisons | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037; C001, C002, C003, C004 reconciled | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004; all three source-coverage rows; all 12 coverage stages; N001-N047; S001-S037 in both passes; all manifested agents through quality audit | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004 plus complete provenance, coverage, execution, performance, and token metadata | report_generation_summary.md | COMPLETE |
