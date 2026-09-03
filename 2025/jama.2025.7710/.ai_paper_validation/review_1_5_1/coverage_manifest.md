# Coverage Manifest

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 through DOC-004; 72 PDF pages | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | 43 eligible reusable evidence assets; fitness and coverage | evidence_asset_inventory.md | COMPLETE |
| evidence_assets | assets-002 | Hashes for all 43 eligible reusable evidence assets | reused_artifact_hashes_before.sha256 | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11; fresh direct-source mapping | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 PDF pp. 1-11; fresh native extraction | preprocessing/DOC-001.native.txt | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 PDF pp. 1-11; fresh layout extraction | preprocessing/DOC-001.layout.txt | COMPLETE |
| main_evidence_mapping | main-004 | DOC-001 PDF pp. 1-11; main numeric relationship shard | parts/relationships/main_numeric.md | COMPLETE |
| main_evidence_mapping | main-005 | DOC-001 PDF pp. 1-11; main statistical relationship shard | parts/relationships/main_statistical.md | COMPLETE |
| main_evidence_mapping | main-006 | Stable N001 through N080 relationship registry | relationships/numeric_relationship_inventory.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 pp. 1-26 and DOC-003 pp. 1-29 fresh; DOC-004 pp. 1-6 reusable-backed | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 PDF pp. 1-26; fresh native extraction | preprocessing/DOC-002.native.txt | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 PDF pp. 1-26; fresh layout extraction | preprocessing/DOC-002.layout.txt | COMPLETE |
| support_evidence_mapping | support-004 | DOC-003 PDF pp. 1-29; fresh native extraction | preprocessing/DOC-003.native.txt | COMPLETE |
| support_evidence_mapping | support-005 | DOC-003 PDF pp. 1-29; fresh layout extraction | preprocessing/DOC-003.layout.txt | COMPLETE |
| support_evidence_mapping | support-006 | DOC-002 pp. 1-26, DOC-003 pp. 1-29, DOC-004 pp. 1-6; support numeric relationship shard | parts/relationships/support_numeric.md | COMPLETE |
| support_evidence_mapping | support-007 | DOC-002 pp. 1-26, DOC-003 pp. 1-29, DOC-004 pp. 1-6; support statistical relationship shard | parts/relationships/support_statistical.md | COMPLETE |
| support_evidence_mapping | support-008 | Stable S001 through S053 relationship registry | statistics/relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-001 | N001 through N080 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | N001 through N080 and S001 through S053 across DOC-001 through DOC-004 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053; C001, C002, C003, C004 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004 and all coverage/source rows | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004 and complete review metadata | ../final_report_1_5_1.md | COMPLETE |
