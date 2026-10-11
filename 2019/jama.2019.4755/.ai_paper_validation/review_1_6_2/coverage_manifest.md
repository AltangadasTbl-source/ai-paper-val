# Workflow 1.6.2 Coverage Manifest

All source assignments are disjoint. Reusable evidence is a locator; the supplied source remains authoritative. Runtime IDs in the execution manifest are the tool-provided canonical agent task identifiers with the leading slash removed.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-001 | DOC-001 pp.1-7; DOC-002 pp.1-62; DOC-003 pp.1-10; DOC-004 pp.1-8; DOC-005 p.1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Every eligible reusable evidence asset for all five direct PDFs | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp.1-7; reusable-backed seven pages | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-protocol | DOC-002 PDF pp.1-62; fresh-required pp.20 and 49; reusable-backed other 60 pages | extraction/support_protocol_part.md | COMPLETE |
| support_evidence_mapping | support-other | DOC-003 PDF pp.1-10; DOC-004 pp.1-8; DOC-005 p.1; reusable-backed 19 pages | extraction/support_other_part.md | COMPLETE |
| support_evidence_mapping | support-merged | DOC-002 pp.1-62; DOC-003 pp.1-10; DOC-004 pp.1-8; DOC-005 p.1; lossless concatenation of disjoint mapped parts | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | All 56 mapped numeric groups; every displayed count/percentage and matching result | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-inventory | Complete source-linked numeric relationship inventory | relationships/numeric_relationship_inventory.md | COMPLETE |
| statistics_pass_1 | statistical-001 | S001,S002,S003,S004,S005,S006,S007,S008,S009,S010,S011,S012,S013,S014,S015,S016,S017,S018,S019,S020,S021,S022,S023,S024,S025,S026,S027,S028,S029,S030,S031,S032,S033,S034,S035,S036,S037,S038,S039,S040,S041,S042,S043,S044,S045,S046,S047,S048,S049,S100,S101,S102,S103,S104,S105,S106,S107,S108,S109,S110,S111,S112,S113,S114,S115,S116,S117,S118,S119,S120,S121,S122,S123,S124,S125,S126,S127,S128,S129,S130,S131,S132,S133,S200,S201,S202,S203,S204,S205,S206,S207,S208,S209,S210,S211,S212,S213,S214,S215,S216,S217,S218,S219,S220,S221 | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | statistical-inventory | S001,S002,S003,S004,S005,S006,S007,S008,S009,S010,S011,S012,S013,S014,S015,S016,S017,S018,S019,S020,S021,S022,S023,S024,S025,S026,S027,S028,S029,S030,S031,S032,S033,S034,S035,S036,S037,S038,S039,S040,S041,S042,S043,S044,S045,S046,S047,S048,S049,S100,S101,S102,S103,S104,S105,S106,S107,S108,S109,S110,S111,S112,S113,S114,S115,S116,S117,S118,S119,S120,S121,S122,S123,S124,S125,S126,S127,S128,S129,S130,S131,S132,S133,S200,S201,S202,S203,S204,S205,S206,S207,S208,S209,S210,S211,S212,S213,S214,S215,S216,S217,S218,S219,S220,S221 | statistics/relationship_inventory.md | COMPLETE |
| cross_source_checks | cross-source-001 | All matched REPORT/REPORT and PLAN/REPORT and PLAN/PLAN relationships across five PDFs | checkers/cross_source_consistency.md | COMPLETE |
| statistics_pass_1 | statistical-arithmetic | Complete 90-row interval and visible point reproduction record supporting all result-bearing S groups | statistics/stat1_calculation_record.md | COMPLETE |
| inclusion_screening | inclusion-initial | F-XS-001, F-ST1-001, F-ST1-002 | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | candidates-initial | C001 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-initial | C001 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistical-second | S001,S002,S003,S004,S005,S006,S007,S008,S009,S010,S011,S012,S013,S014,S015,S016,S017,S018,S019,S020,S021,S022,S023,S024,S025,S026,S027,S028,S029,S030,S031,S032,S033,S034,S035,S036,S037,S038,S039,S040,S041,S042,S043,S044,S045,S046,S047,S048,S049,S100,S101,S102,S103,S104,S105,S106,S107,S108,S109,S110,S111,S112,S113,S114,S115,S116,S117,S118,S119,S120,S121,S122,S123,S124,S125,S126,S127,S128,S129,S130,S131,S132,S133,S200,S201,S202,S203,S204,S205,S206,S207,S208,S209,S210,S211,S212,S213,S214,S215,S216,S217,S218,S219,S220,S221 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-initial | C001; all three findings and screening decisions; all 24 checker exclusions including pass2 reconsideration; all 88 pages and complete relationship/execution maps | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-complete-ledger | C001 | ../final_report_1_6_2.md | COMPLETE |
| report_generation | report-limitations | Complete source and analysis-definition limitations for C001 and the full review | limitations.md | COMPLETE |
