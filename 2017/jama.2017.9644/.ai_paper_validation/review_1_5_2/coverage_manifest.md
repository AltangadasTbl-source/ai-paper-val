# Coverage Manifest

This manifest was created before scientific extraction. Rows are updated to `COMPLETE` only after the assigned durable artifact covers the exact stated scope. Each artifact cell contains one plain relative path.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 PDF pp. 1-10; DOC-002 PDF pp. 1-14; DOC-003 PDF pp. 1-6 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Fresh native and layout extraction, metadata, rendering and OCR decisions for DOC-001 pp. 1-10; DOC-002 pp. 1-14; DOC-003 pp. 1-6 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10; stable mappings N001-N063 and S001-S020 | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-14; DOC-003 PDF pp. 1-6; stable mappings N064-N081 and S021-S031 | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001 through N081, each explicitly checked | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001; S002; S003; S004; S005; S006; S007; S008; S009; S010; S011; S012; S013; S014; S015; S016; S017; S018; S019; S020; S021; S022; S023; S024; S025; S026; S027; S028; S029; S030; S031 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-source-001 | All matched results across DOC-001, DOC-002, and DOC-003, including 18 documented match groups | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | registration-001 | C001; C002; C003; C004; C005; C006; C007; C008; C009; C010; C011; C012; C013 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001; C002; C003; C004; C005; C006; C007; C008; C009; C010; C011; C012; C013 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001; S002; S003; S004; S005; S006; S007; S008; S009; S010; S011; S012; S013; S014; S015; S016; S017; S018; S019; S020; S021; S022; S023; S024; S025; S026; S027; S028; S029; S030; S031 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001; C002; C003; C004; C005; C006; C007; C008; C009; C010; C011; C012; C013; every source-coverage row; every coverage row; both statistical executions | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001; C002; C003; C004; C005; C006; C007; C008; C009; C010; C011; C012; C013; all required provenance, coverage, integrity, performance, agent, and token metadata | ../final_report_1_5_2.md | COMPLETE |
