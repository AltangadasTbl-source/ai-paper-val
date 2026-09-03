# Coverage Manifest

This manifest was created before scientific mapping. Rows are updated to `COMPLETE` only after their exact scopes are documented.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-001 | DOC-001 pp. 1-10; DOC-002 pp. 1-94; DOC-003 pp. 1-18; DOC-004 pp. 1-27; DOC-005 pp. 1-8; DOC-006 p. 1; DOC-007 p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Every eligible existing document-output asset: DOC-001 pp. 1-10 and DOC-004 pp. 10-27 source-linked derivatives; historical status assets for DOC-002, DOC-003, DOC-005, DOC-006, and DOC-007 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10 | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-relationships-numeric | DOC-001 provisional numeric relationship families MN001-MN015 | extraction/parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-relationships-statistical | DOC-001 provisional statistical relationship families MS001-MS009 | extraction/parts/main_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 pp. 1-94; DOC-003 pp. 1-18; DOC-004 pp. 1-27; DOC-005 pp. 1-8; DOC-006 p. 1; DOC-007 p. 1 | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-relationships-numeric | DOC-002 through DOC-007 provisional numeric relationship families UN001-UN018 | extraction/parts/support_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-relationships-statistical | DOC-002 through DOC-007 provisional statistical relationship families US001-US012 | extraction/parts/support_statistical_relationships.md | COMPLETE |
| numeric_checks | numeric-inventory | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033 | relationships/numeric_relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | stat1-inventory | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021 | statistics/relationship_inventory.md | COMPLETE |
| statistics_pass_1 | stat1-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | N001-N033 and S001-S021 matched across DOC-001 through DOC-007 with 24 documented match families | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012 | verification/evidence_recheck.md | COMPLETE |
| evidence_recheck | recheck-c010-visual | C010 direct visual confirmation from DOC-004 PDF p. 23 | preprocessing/coordinator_confirmations/doc004-p23.png | COMPLETE |
| statistics_pass_2 | stat2-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021 plus C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012 and all recheck facts | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012 plus every source-coverage, relationship, statistical-execution, integrity, and coverage-manifest row | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012 plus all required provenance, coverage, performance, and token metadata | ../final_report_1_5_1.md | COMPLETE |
| report_generation | report-limitations | Bounded package, extraction, source-definition, graphical, and statistical limitations | limitations.md | COMPLETE |
| report_generation | report-token-ledger | Coordinator and every manifested specialist through Finished UTC | token_usage_ledger.csv | COMPLETE |
| report_generation | report-token-summary-md | Deterministic per-agent, per-model, and package token summary | token_usage_summary.md | COMPLETE |
| report_generation | report-token-summary-json | Deterministic machine-readable token summary | token_usage_summary.json | COMPLETE |
| report_generation | report-html | Standalone HTML5 report with embedded CSS and table of contents | ../final_report_1_5_1.html | COMPLETE |
