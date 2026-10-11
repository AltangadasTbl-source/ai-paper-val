# Workflow 1.5.1 Coverage Manifest

Created before scientific mapping. Each row assigns one disjoint scope to exactly one durable artifact; planned rows are updated to `COMPLETE` after the assigned work is merged and verified.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001, DOC-002, and DOC-003 identities and 134 PDF pages | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All 60 pre-existing source-linked artifacts under document_outputs | evidence_asset_inventory.md | COMPLETE |
| evidence_assets | assets-002 | SHA-256 snapshot of all 60 pre-existing source-linked artifacts | reused_artifact_hashes_before.sha256 | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-9, reusable-backed | parts/main_evidence_DOC-001_pp001-009.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-32, fresh direct-source visual mapping | parts/support_evidence_DOC-002_pp001-032.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 PDF pp. 33-64, fresh direct-source visual mapping | parts/support_evidence_DOC-002_pp033-064.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 PDF pp. 65-96, fresh direct-source visual mapping | parts/support_evidence_DOC-002_pp065-096.md | COMPLETE |
| support_evidence_mapping | support-004 | DOC-002 PDF pp. 97-109 and DOC-003 PDF pp. 1-16; DOC-002 and DOC-003 pp. 1-2 fresh, DOC-003 pp. 3-16 reusable-backed | parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md | COMPLETE |
| main_evidence_mapping | main-merge | Complete DOC-001 quantitative evidence map | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-merge | Complete DOC-002 and DOC-003 quantitative evidence map | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-all | N001,N002,N003,N004,N005,N006,N007,N008,N009,N010,N011,N012,N013,N014,N015,N016,N017,N018,N019,N020,N021,N022,N023,N024,N025,N026,N027,N028,N029,N030,N031,N032,N033,N034,N035,N036,N037,N038,N039,N040,N041,N042,N043,N044,N045,N046,N047,N048,N049,N050,N051,N052,N053,N054,N055,N056,N057,N058,N059,N060,N061,N062,N063,N064,N065,N066,N067,N068,N069,N070,N071,N072,N073,N074,N075,N076,N077,N078,N079,N080,N081,N082,N083,N084,N085,N086,N087,N088 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | stat1-all | S001,S002,S003,S004,S005,S006,S007,S008,S009,S010,S011,S012,S013,S014,S015,S016,S017,S018,S019,S020,S021,S022,S023,S024,S025,S026,S027,S028,S029,S030,S031,S032,S033,S034,S035,S036,S037,S038,S039,S040,S041 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-all | All matched quantitative results across DOC-001, DOC-002, and DOC-003 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-all | C001,C002,C003,C004,C005,C006,C007,C008,C009,C010,C011,C012,C013 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-all | C001,C002,C003,C004,C005,C006,C007,C008,C009,C010,C011,C012,C013 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stat2-all | S001,S002,S003,S004,S005,S006,S007,S008,S009,S010,S011,S012,S013,S014,S015,S016,S017,S018,S019,S020,S021,S022,S023,S024,S025,S026,S027,S028,S029,S030,S031,S032,S033,S034,S035,S036,S037,S038,S039,S040,S041 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-all | C001,C002,C003,C004,C005,C006,C007,C008,C009,C010,C011,C012,C013 and every coverage/source-coverage/statistical-execution row | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-all | C001,C002,C003,C004,C005,C006,C007,C008,C009,C010,C011,C012,C013 and all required metadata | ../final_report_1_5_1.md | COMPLETE |
