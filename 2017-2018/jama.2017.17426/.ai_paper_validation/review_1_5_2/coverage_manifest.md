# Coverage Manifest

Created before scientific extraction. Every source unit and later relationship/candidate unit is assigned once within its stage; planned rows are updated to `COMPLETE` only after their artifacts are finished.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-001 | DOC-001 PDF pp. 1-10; DOC-002 PDF pp. 1-69; DOC-003 PDF pp. 1-2 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Fresh native and layout text for DOC-001 pp. 1-10, DOC-002 pp. 1-69, DOC-003 pp. 1-2; 64 selected renders; targeted OCR for DOC-002 p. 66 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10 complete quantitative evidence map | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 numeric relationships MN001 through MN031, merged as N001 through N031 | relationships/parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 statistical relationships MS001 through MS033, merged as S001 through S033 | statistics/parts/main_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-69 and DOC-003 PDF pp. 1-2 complete quantitative evidence map | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 and DOC-003 numeric relationships UN001 through UN029; duplicate sample-size records UN021 and UN029 merged in stable N052; stable support scope N032 through N059 | relationships/parts/support_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 and DOC-003 statistical relationships US001 through US019; duplicate sample-size records US009 and US019 merged in stable S042; stable support scope S034 through S051 | statistics/parts/support_statistical_relationships.md | COMPLETE |
| numeric_checks | numeric-001 | N001 N002 N003 N004 N005 N006 N007 N008 N009 N010 N011 N012 N013 N014 N015 N016 N017 N018 N019 N020 N021 N022 N023 N024 N025 N026 N027 N028 N029 N030 N031 N032 N033 N034 N035 N036 N037 N038 N039 N040 N041 N042 N043 N044 N045 N046 N047 N048 N049 N050 N051 N052 N053 N054 N055 N056 N057 N058 N059 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042 S043 S044 S045 S046 S047 S048 S049 S050 S051 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | Every matched quantitative result and definition across DOC-001, DOC-002, and DOC-003, including N001-N059 and S001-S051 where a comparator exists | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001 C002 C003 C004 C005 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001 C002 C003 C004 C005 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042 S043 S044 S045 S046 S047 S048 S049 S050 S051 plus C001 C002 C003 C004 C005 and all evidence-recheck facts | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001 C002 C003 C004 C005; every coverage and source-coverage row; N001-N059; S001-S051; both statistical passes and execution records | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001 C002 C003 C004 C005 plus complete run provenance, coverage, limitations, execution, performance, token usage, and cost metadata | ../final_report_1_5_2.md | COMPLETE |
