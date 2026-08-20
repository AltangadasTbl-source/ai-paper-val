# Workflow 1.5.2 Coverage Manifest

This manifest was created before quantitative scientific extraction. Pending rows record disjoint assignments and will be finalized to `COMPLETE` only after the assigned scope and artifact are complete.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-001 | DOC-001 pp. 1-10; DOC-002 pp. 1-55; DOC-003 pp. 1-17; DOC-004 p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Fresh metadata, native text, layout text, and rendered-page/OCR decisions for DOC-001 pp. 1-10; DOC-002 pp. 1-55; DOC-003 pp. 1-17; DOC-004 p. 1 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 pp. 1-10, every result-relevant numeric and statistical relationship; N001-N035 and S001-S022 | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 pp. 1-55; DOC-003 pp. 1-17; DOC-004 p. 1, every result-relevant numeric and statistical relationship; N501-N522 and S501-S534 | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001-N035 and N501-N522; all 57 mapped numeric and reporting relationships | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S501, S502, S503, S504, S505, S506, S507, S508, S509, S510, S511, S512, S513, S514, S515, S516, S517, S518, S519, S520, S521, S522, S523, S524, S525, S526, S527, S528, S529, S530, S531, S532, S533, S534 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | All matched results across DOC-001, DOC-002, DOC-003, and DOC-004; all 57 N and 56 S relationships | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | registration-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S501, S502, S503, S504, S505, S506, S507, S508, S509, S510, S511, S512, S513, S514, S515, S516, S517, S518, S519, S520, S521, S522, S523, S524, S525, S526, S527, S528, S529, S530, S531, S532, S533, S534 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014; all source-coverage, coverage, relationship, and execution rows | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014 | ../final_report_1_5_2.md | COMPLETE |
