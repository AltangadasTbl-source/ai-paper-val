# Coverage Manifest

Created before scientific extraction. Each row has one disjoint scope and exactly one plain relative artifact path.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 PDF pp. 1-9; DOC-002 PDF pp. 1-134; DOC-003 PDF pp. 1-3 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Fresh metadata, native text, layout text, and result-relevant rendering/OCR decisions for DOC-001 PDF pp. 1-9; DOC-002 PDF pp. 1-134; DOC-003 PDF pp. 1-3 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-9 complete quantitative evidence mapping | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 PDF pp. 1-9 numeric relationship part | relationships/parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 PDF pp. 1-9 statistical relationship part | statistics/parts/main_statistical_relationships.md | COMPLETE |
| main_evidence_mapping | canonical-numeric-001 | Canonical fresh union N001 N002 N003 N004 N005 N006 N007 N008 N009 N010 N011 N012 N013 N014 N015 N016 N017 N018 N019 N020 N021 N022 N023 N024 N025 N026 N027 N028 N029 N030 N031 N032 N033 N034 N035 N036 N037 N038 N039 N040 N041 N042 N043 N044 N045 N046 N047 N048 N049 N050 N051 | relationships/numeric_relationship_inventory.md | COMPLETE |
| main_evidence_mapping | canonical-statistical-001 | Canonical fresh union S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 | statistics/relationship_inventory.md | COMPLETE |
| support_evidence_mapping | support-a-001 | DOC-002 PDF pp. 1-67 complete quantitative evidence mapping | extraction/parts/support_a_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-a-002 | DOC-002 PDF pp. 1-67 numeric relationship part | relationships/parts/support_a_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-a-003 | DOC-002 PDF pp. 1-67 statistical relationship part | statistics/parts/support_a_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-b-001 | DOC-002 PDF pp. 68-134 and DOC-003 PDF pp. 1-3 complete quantitative evidence mapping | extraction/parts/support_b_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-b-002 | DOC-002 PDF pp. 68-134 and DOC-003 PDF pp. 1-3 numeric relationship part | relationships/parts/support_b_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-b-003 | DOC-002 PDF pp. 68-134 and DOC-003 PDF pp. 1-3 statistical relationship part | statistics/parts/support_b_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-merged-001 | Canonical union of DOC-002 PDF pp. 1-134 and DOC-003 PDF pp. 1-3 evidence | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001 N002 N003 N004 N005 N006 N007 N008 N009 N010 N011 N012 N013 N014 N015 N016 N017 N018 N019 N020 N021 N022 N023 N024 N025 N026 N027 N028 N029 N030 N031 N032 N033 N034 N035 N036 N037 N038 N039 N040 N041 N042 N043 N044 N045 N046 N047 N048 N049 N050 N051 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | N001 N002 N003 N004 N005 N006 N007 N008 N009 N010 N011 N012 N013 N014 N015 N016 N017 N018 N019 N020 N021 N022 N023 N024 N025 N026 N027 N028 N029 N030 N031 N032 N033 N034 N035 N036 N037 N038 N039 N040 N041 N042 N043 N044 N045 N046 N047 N048 N049 N050 N051 and S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 across DOC-001 DOC-002 DOC-003 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001 C002 C003 C004 C005 C006 C007 C008 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001 C002 C003 C004 C005 C006 C007 C008 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 with C001 C002 C003 C004 C005 C006 C007 C008 and complete recheck facts | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001 C002 C003 C004 C005 C006 C007 C008; every coverage row; DOC-001 DOC-002 DOC-003 source rows; statistics_pass_1 and statistics_pass_2 execution records; N001-N051; S001-S038 | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001 C002 C003 C004 C005 C006 C007 C008 and all finalized run metadata | ../final_report_1_5_2.md | COMPLETE |
