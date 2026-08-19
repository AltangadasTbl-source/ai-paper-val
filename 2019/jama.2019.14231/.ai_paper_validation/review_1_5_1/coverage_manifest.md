# Coverage Manifest

Created before scientific mapping. Every row assigns a disjoint source/evidence scope to one durable artifact. Later checker and candidate-stage rows will enumerate the stable `N`, `S`, and `C` identifiers after those identifiers exist.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 PDF pp. 1-12; DOC-002 PDF pp. 1-20; DOC-003 PDF pp. 1-7 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | 59 actively reused assets covering DOC-001 pp. 1-12 and DOC-002 pp. 6-20; reusable-asset gap DOC-002 pp. 1-5 and DOC-003 pp. 1-7 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-12, reusable-backed with direct-source confirmation | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 PDF pp. 1-12 numeric relationship part | parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 PDF pp. 1-12 statistical relationship part | parts/main_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-20: fresh pp. 1-5 and reusable-backed pp. 6-20; DOC-003 PDF pp. 1-7 fresh | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 PDF pp. 1-20 and DOC-003 PDF pp. 1-7 numeric relationship part | parts/support_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 PDF pp. 1-20 and DOC-003 PDF pp. 1-7 statistical relationship part | parts/support_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-004 | Fresh native extraction for DOC-002 PDF pp. 1-5 | preprocessing/joi190103supp1_prod_pp1-5_native.txt | COMPLETE |
| support_evidence_mapping | support-005 | Fresh layout extraction for DOC-002 PDF pp. 1-5 | preprocessing/joi190103supp1_prod_pp1-5_layout.txt | COMPLETE |
| support_evidence_mapping | support-006 | Fresh native extraction for DOC-003 PDF pp. 1-7 | preprocessing/joi190103supp2_prod_pp1-7_native.txt | COMPLETE |
| support_evidence_mapping | support-007 | Fresh layout extraction for DOC-003 PDF pp. 1-7 | preprocessing/joi190103supp2_prod_pp1-7_layout.txt | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | All matched occurrences in N001, N005, N006, N007, N008, N009, N010, N011, N012, N013, N017, N018, N019, N021, N025, N029, N035, N036, N037, N038 and S001, S002, S003, S004, S005, S006, S007, S008, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S023, S024, S025 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025; cross-lane candidates C001, C002, C003, C004, C005, C006, C007, C008, C009; all recheck facts | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011; every source-coverage and coverage-manifest row; statistics pass 1 and pass 2 execution records | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011 | ../final_report_1_5_1.md | COMPLETE |
| report_generation | report-002 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011 execution record | report_generation_manifest.md | COMPLETE |
