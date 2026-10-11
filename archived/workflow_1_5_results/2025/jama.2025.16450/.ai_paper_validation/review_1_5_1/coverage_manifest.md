# Coverage Manifest

Created before scientific mapping. Each row assigns a disjoint source/evidence scope and exactly one durable artifact path.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 pp. 1-11; DOC-002 pp. 1-35; DOC-003 pp. 1-162; DOC-004 pp. 1-48; DOC-005 pp. 1-16 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All 63 reused evidence assets linked to DOC-001 through DOC-005 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11 | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 relationship records from PDF pp. 1-11 | parts/main_relationships.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-35 | parts/support_protocol.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-003 PDF pp. 1-81 | parts/support_manual_001_081.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-003 PDF pp. 82-162 | parts/support_manual_082_162.md | COMPLETE |
| support_evidence_mapping | support-004 | DOC-004 PDF pp. 1-48 and DOC-005 PDF pp. 1-16 | parts/support_sap_results.md | COMPLETE |
| support_evidence_mapping | support-004-repair | DOC-004 PDF pp. 16-48 direct visual semantic coverage repair | parts/support_sap_016_048_repair.md | COMPLETE |
| support_evidence_mapping | support-merge | Union of support-001, support-002, support-003, support-004, and support-004-repair | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-all | N001 N002 N003 N004 N005 N006 N007 N008 N009 N010 N011 N012 N013 N014 N015 N016 N017 N018 N019 N020 N021 N022 N023 N024 N025 N026 N027 N028 N029 N030 N031 N032 N033 N034 N035 N036 N037 N038 N039 N040 N041 N042 N043 N044 N045 N046 N047 N048 N049 N050 N051 N052 N053 N054 N055 N056 N057 N058 N059 N060 N061 N062 N063 N064 N065 N066 N067 N068 N069 N070 N071 N072 N073 N074 N075 N076 N077 N078 N079 N080 N081 N082 N083 N084 N085 N086 N087 N088 N089 N090 N091 N092 N093 N094 N095 N096 N097 N098 N099 N100 N101 N102 N103 N104 N105 N106 N107 N108 N109 N110 N111 N112 N113 N114 N115 N116 N117 N118 N119 N120 N121 N122 N123 N124 N125 N126 N127 N128 N129 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-1 | S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042 S043 S044 S045 S046 S047 S048 S049 S050 S051 S052 S053 S054 S055 S056 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-all | All matched quantitative results across DOC-001 through DOC-005 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | ledger-all | C001 C002 C003 C004 C005 C006 C007 C008 C009 C010 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-all | C001 C002 C003 C004 C005 C006 C007 C008 C009 C010 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-2 | S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042 S043 S044 S045 S046 S047 S048 S049 S050 S051 S052 S053 S054 S055 S056 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-all | C001 C002 C003 C004 C005 C006 C007 C008 C009 C010 | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-all | C001 C002 C003 C004 C005 C006 C007 C008 C009 C010 | ../final_report_1_5_1.md | COMPLETE |
