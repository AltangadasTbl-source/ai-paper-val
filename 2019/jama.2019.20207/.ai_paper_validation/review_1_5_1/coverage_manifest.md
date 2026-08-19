# Coverage Manifest

This manifest was created before scientific mapping. Each row assigns a disjoint source/evidence scope to one durable artifact. Later checker and candidate-stage rows are appended as stable relationship and candidate identifiers become available.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 PDF pp. 1-9; DOC-002 PDF pp. 1-60; DOC-003 PDF pp. 1-11; DOC-004 PDF pp. 1-3; DOC-005 PDF p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All 62 hashed pre-existing reusable source-linked assets covering DOC-001 pp. 1-9 and DOC-004 pp. 1-3, plus documented gaps for DOC-002 pp. 1-60, DOC-003 pp. 1-11, and DOC-005 p. 1 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-9, reusable-backed direct-source mapping | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-30, fresh native/layout direct-source mapping | parts/support_doc002_p001_p030.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 PDF pp. 31-60, fresh native/layout direct-source mapping | parts/support_doc002_p031_p060.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-003 PDF pp. 1-11; DOC-004 PDF pp. 1-3; DOC-005 PDF p. 1, fresh/reusable-backed direct-source mapping | parts/support_docs003_005.md | COMPLETE |
| support_evidence_mapping | support-merge | Union of support-001, support-002, and support-003 without source-unit duplication | extraction/support_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-numeric | DOC-001 pp. 1-9 provisional numeric relationships | parts/relationships_main_numeric.md | COMPLETE |
| main_evidence_mapping | main-statistics | DOC-001 pp. 1-9 provisional statistical relationships | parts/statistics_main.md | COMPLETE |
| support_evidence_mapping | support-001-numeric | DOC-002 pp. 1-30 provisional numeric relationships | parts/numeric_doc002_p001_p030.md | COMPLETE |
| support_evidence_mapping | support-001-statistics | DOC-002 pp. 1-30 provisional statistical relationships | parts/statistics_doc002_p001_p030.md | COMPLETE |
| support_evidence_mapping | support-002-numeric | DOC-002 pp. 31-60 provisional numeric relationships | parts/numeric_doc002_p031_p060.md | COMPLETE |
| support_evidence_mapping | support-002-statistics | DOC-002 pp. 31-60 provisional statistical relationships | parts/statistics_doc002_p031_p060.md | COMPLETE |
| support_evidence_mapping | support-003-numeric | DOC-003 pp. 1-11; DOC-004 pp. 1-3; DOC-005 p. 1 provisional numeric relationships | parts/numeric_docs003_005.md | COMPLETE |
| support_evidence_mapping | support-003-statistics | DOC-003 pp. 1-11; DOC-004 pp. 1-3; DOC-005 p. 1 provisional statistical relationships | parts/statistics_docs003_005.md | COMPLETE |
| main_evidence_mapping | numeric-canonical | Complete canonical N001-N031 relationship inventory from all main and support mapping parts | relationships/numeric_relationship_inventory.md | COMPLETE |
| support_evidence_mapping | statistics-canonical | Complete canonical S001-S017 relationship inventory from all main and support mapping parts | statistics/relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-001 | N001; N002; N003; N004; N005; N006; N007; N008; N009; N010; N011; N012; N013; N014; N015; N016; N017; N018; N019; N020; N021; N022; N023; N024; N025; N026; N027; N028; N029; N030; N031 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001; S002; S003; S004; S005; S006; S007; S008; S009; S010; S011; S012; S013; S014; S015; S016; S017 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | N001; N002; N003; N004; N005; N006; N007; N008; N009; N010; N011; N012; N013; N014; N015; N016; N017; N018; N019; N020; N021; N022; N023; N024; N025; N026; N027; N028; N029; N030; N031; S001; S002; S003; S004; S005; S006; S007; S008; S009; S010; S011; S012; S013; S014; S015; S016; S017 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001; C002; C003; C004; C005; C006; C007; C008; C009; C010; C011; C012; C013 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001; C002; C003; C004; C005; C006; C007; C008; C009; C010; C011; C012 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001; S002; S003; S004; S005; S006; S007; S008; S009; S010; S011; S012; S013; S014; S015; S016; S017 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_recheck | recheck-002 | C013 | verification/evidence_recheck.md | COMPLETE |
| evidence_quality | quality-001 | C001; C002; C003; C004; C005; C006; C007; C008; C009; C010; C011; C012; C013 | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001; C002; C003; C004; C005; C006; C007; C008; C009; C010; C011; C012; C013 | ../final_report_1_5_1.md | COMPLETE |
