# Coverage Manifest

This manifest was created before scientific extraction. Each row has one plain relative artifact path.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 pp. 1-14; DOC-002 pp. 1-36; DOC-003 pp. 1-3; DOC-004 pp. 1-3; DOC-005 pp. 1-43; DOC-006 p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | DOC-001 pp. 1-14 native text | preprocessing/native_text/DOC-001.txt | COMPLETE |
| evidence_assets | assets-002 | DOC-001 pp. 1-14 layout text | preprocessing/layout_text/DOC-001.txt | COMPLETE |
| evidence_assets | assets-003 | DOC-002 pp. 1-36 native text | preprocessing/native_text/DOC-002.txt | COMPLETE |
| evidence_assets | assets-004 | DOC-002 pp. 1-36 layout text | preprocessing/layout_text/DOC-002.txt | COMPLETE |
| evidence_assets | assets-005 | DOC-003 pp. 1-3 native text | preprocessing/native_text/DOC-003.txt | COMPLETE |
| evidence_assets | assets-006 | DOC-003 pp. 1-3 layout text | preprocessing/layout_text/DOC-003.txt | COMPLETE |
| evidence_assets | assets-007 | DOC-004 pp. 1-3 native text | preprocessing/native_text/DOC-004.txt | COMPLETE |
| evidence_assets | assets-008 | DOC-004 pp. 1-3 layout text | preprocessing/layout_text/DOC-004.txt | COMPLETE |
| evidence_assets | assets-009 | DOC-005 pp. 1-43 native text | preprocessing/native_text/DOC-005.txt | COMPLETE |
| evidence_assets | assets-010 | DOC-005 pp. 1-43 layout text | preprocessing/layout_text/DOC-005.txt | COMPLETE |
| evidence_assets | assets-011 | DOC-006 p. 1 native text | preprocessing/native_text/DOC-006.txt | COMPLETE |
| evidence_assets | assets-012 | DOC-006 p. 1 layout text | preprocessing/layout_text/DOC-006.txt | COMPLETE |
| evidence_assets | assets-013 | DOC-001 through DOC-006 extraction methods and limitations | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-14 | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 PDF pp. 1-14 numeric relationships MN001 through MN037 | relationships/parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 PDF pp. 1-14 statistical relationships MS001 through MS014 | statistics/parts/main_statistical_relationships.md | COMPLETE |
| main_evidence_mapping | main-004 | Canonical N001 through N055 merged from disjoint main/support lanes | relationships/numeric_relationship_inventory.md | COMPLETE |
| main_evidence_mapping | main-005 | Canonical S001 through S031 merged from disjoint main/support lanes | statistics/relationship_inventory.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 pp. 1-36; DOC-003 pp. 1-3; DOC-004 pp. 1-3; DOC-005 pp. 1-43; DOC-006 p. 1 | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 through DOC-006 numeric relationships UN001 through UN018 over 86 PDF pages | relationships/parts/support_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 through DOC-006 statistical relationships US001 through US017 over 86 PDF pages | statistics/parts/support_statistical_relationships.md | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | stat1-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | All matched/repeated N001 through N055 and S001 through S031 occurrences across DOC-001 through DOC-006 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006, C007, C008 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stat2-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008; all source, coverage, relationship, recheck, and statistical-execution rows | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008 | ../final_report_1_5_2.md | COMPLETE |
