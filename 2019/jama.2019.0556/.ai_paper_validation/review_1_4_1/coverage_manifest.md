# Workflow 1.4.1 Coverage Manifest

This manifest was created before scientific extraction. `ASSIGNED` records an exhaustive disjoint assignment that has not yet produced its canonical artifact. Rows are updated to `COMPLETE` only after the stated artifact documents the full scope.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-60; DOC-003 PDF pp. 1-5; DOC-004 PDF pp. 1-25; DOC-005 PDF p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All 72 eligible reused native-text, OCR-text, OCR-metadata, rendered-page, page-manifest, document-status, preprocessing-manifest, and OCR-backend artifacts; reusable coverage gaps explicitly mapped | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 main article PDF pp. 1-11, using complete reusable normalized text and page-linked OCR/rendered assets; 36 numeric/reporting and 16 inferential relationships mapped | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-004 results supplement PDF pp. 1-2 and 16-23 represented by reusable normalized text/OCR/rendered assets; 31 numeric and 24 inferential relationships mapped; DOC-002, DOC-003, DOC-004 pp. 3-15 and 24-25, and DOC-005 recorded as reusable-evidence gaps with no discovery sampling | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | Quality-audit repair: DOC-002 protocol PDF pp. 1-60, direct native-text extraction; 11 numeric/design and 6 statistical rules mapped | extraction/parts/protocol_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-003 | Quality-audit repair: DOC-003 statistical analysis plan PDF pp. 1-5; DOC-004 results supplement PDF pp. 3-15 and 24-25; DOC-005 administrative PDF p. 1, direct native-text extraction; 17 numeric/reporting and 8 statistical relationships mapped | extraction/parts/remaining_support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061, N062, N063, N064, N065, N066, N067, N068, N069, N070, N071, N072, N073, N074, N075, N076, N077, N078, N079, N080, N081, N082, N083, N084, N085, N086, N087, N088, N089, N090, N091, N092, N093, N094, N095 | relationships/numeric_relationship_inventory.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054 | statistics/relationship_inventory.md | COMPLETE |
| cross_source_checks | cross-001 | Eighteen matched or explicitly no-applicable families across all four mapping artifacts and all five direct PDFs | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | ledger-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054; plus C001, C002, C003, C004, C005, C006, C007, C008, C009 and all recheck facts | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009; every coverage row | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009; complete provenance, coverage, limitations, integrity, and timing metadata | ../final_report_1_4_1.md | COMPLETE |

## Coverage Constraints

- Candidate discovery uses only the eligible source-linked reusable evidence assets listed in `evidence_asset_inventory.md`; legacy candidate and disposition artifacts are excluded.
- Missing reusable page text is an explicit limitation, not authorization to infer that the uncovered source pages contain no quantitative content.
- Candidate recheck may use targeted direct source-page extraction or rendering when required to confirm an exact printed location.
