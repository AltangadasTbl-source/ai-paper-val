# Workflow 1.6.2 coverage manifest

This plan was created before scientific mapping. Mapping scopes partition all 194 supplied PDF pages. Reusable extraction is a locator; every assigned unit is mapped anew. Stage rows are completed only after their artifacts exist. Each artifact cell contains one plain path, relative to this review directory.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 pp. 1-10; DOC-002 pp. 1-153; DOC-003 pp. 1-9; DOC-004 pp. 1-18; DOC-005 pp. 1-3; DOC-006 p. 1 | source_inventory.md | COMPLETE |
| source_inventory | coverage-001 | All six direct sources, 194 PDF_PAGE units | source_coverage.md | COMPLETE |
| evidence_assets | integrity-closure | All six direct-source and116 existing-asset before/after identities | integrity_record.md | COMPLETE |
| evidence_assets | assets-001 | All eligible legacy extraction, maps and rendered pages | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10, reusable-backed | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | core-001 | DOC-003 pp. 1-9; DOC-004 pp. 1-18; DOC-005 pp. 1-3; DOC-006 p. 1, reusable-backed | extraction/parts/support_core.md | COMPLETE |
| support_evidence_mapping | protocol-001 | DOC-002 pp. 1-51; reusable-backed except fresh-required pp. 4,49 | extraction/parts/protocol_001.md | COMPLETE |
| support_evidence_mapping | protocol-002 | DOC-002 pp. 52-102, reusable-backed except fresh-required p.95 closed by coverage audit | extraction/parts/protocol_002.md | COMPLETE |
| support_evidence_mapping | protocol-003 | DOC-002 pp. 103-153, reusable-backed | extraction/parts/protocol_003.md | COMPLETE |
| support_evidence_mapping | support-merge | Complete disjoint support union: DOC-002 to DOC-006 | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | DOC-001 N001-N095 | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-inventory | Complete N001-N095 and N201-N310 numeric union | relationships/numeric_relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-support-001 | DOC-002 to DOC-006 numeric relationships, disjoint from main | checkers/parts/numeric_support.md | COMPLETE |
| numeric_checks | numeric-support-inventory | DOC-002 to DOC-006 numeric relationships, disjoint from main | relationships/parts/numeric_support.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107 | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | statistics-inventory | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107 | statistics/relationship_inventory.md | COMPLETE |
| cross_source_checks | cross-source-001 | Complete matched REPORT/REPORT, REPORT/PLAN and PLAN/PLAN relationships | checkers/cross_source_consistency.md | COMPLETE |
| cross_source_checks | cross-source-remaining | Protocol exclusion25; administrative calendar/site/safety-interval comparisons; DOC-005 roster and DOC-006 sharing statement | checkers/parts/cross_source_remaining.md | COMPLETE |
| inclusion_screening | screening-001 | All15 initial checker findings independently screened | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | registration-001 | C001, C002, C003, C004, C005, C006, C007 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007; all screening/exclusions; appended three cross-source groups and coverage/manifest audit | quality/evidence_quality_audit.md | COMPLETE |
| evidence_quality | quality-candidate-part | C001, C002, C003, C004, C005, C006, C007; complete primary audit preserved before lossless shard merge | quality/parts/candidate_quality_audit.md | COMPLETE |
| evidence_quality | quality-coverage-main-protocol | DOC-001 all10 pages; DOC-002 all153 pages; N001-N095; no candidate assignment in this coverage shard | quality/parts/coverage_main_protocol.md | COMPLETE |
| evidence_quality | quality-coverage-support | DOC-003 all9 pages; DOC-004 all18 pages; DOC-005 all3 pages; DOC-006 p1; N201-N310; no candidate assignment in this coverage shard | quality/parts/coverage_support.md | COMPLETE |
| evidence_quality | quality-cross-relationships | First120 cross-source groups, seven findings,13 exclusions; no candidate assignment in this relationship shard | quality/parts/cross_source_audit.md | COMPLETE |
| evidence_quality | quality-statistical-relationships | All107 S relationships and both statistical passes; no candidate assignment in this relationship shard | quality/parts/statistical_audit.md | COMPLETE |
| evidence_quality | quality-bounded-handoff | Source/relationship audit conclusions and all scope decisions from four fresh disjoint audit parts | quality/audit_handoff.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007 | ../final_report_1_6_2.md | COMPLETE |
| report_generation | limitations-001 | Package-wide missing definitions and tooling limitations | limitations.md | COMPLETE |
