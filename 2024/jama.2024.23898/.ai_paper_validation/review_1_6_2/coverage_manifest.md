# Workflow 1.6.2 Coverage Manifest

Coverage plan created before scientific mapping. Source units are disjoint across main and support assignments. Counts reflect source pages, independently of derivative count.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 pp.1-10; DOC-002 pp.1-66; DOC-003 pp.1-40; DOC-004 pp.1-2; DOC-005 p.1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All eligible source-matched extraction and page assets for the five direct sources | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 pp.1-10, reusable-backed; fresh-required none | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 pp.1-66, reusable-backed; fresh-required none | extraction/parts/support_protocol_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-003 pp.1-40; DOC-004 pp.1-2; DOC-005 p.1, reusable-backed; fresh-required none | extraction/parts/support_sap_results_evidence.md | COMPLETE |
| support_evidence_mapping | support-canonical | Complete union of support-001 and support-002 | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-confirmation-001 | DOC-003 p.32 supplemental direct-source glyph confirmation | preprocessing/sap-results-doc003-page032.png | COMPLETE |
| support_evidence_mapping | protocol-confirmation-027 | DOC-002 p.27 supplemental visual confirmation | preprocessing/protocol/page-27.png | COMPLETE |
| support_evidence_mapping | protocol-confirmation-047 | DOC-002 p.47 supplemental visual confirmation | preprocessing/protocol/page-47.png | COMPLETE |
| support_evidence_mapping | protocol-confirmation-048 | DOC-002 p.48 supplemental visual confirmation | preprocessing/protocol/page-48.png | COMPLETE |
| numeric_checks | numeric-main | DOC-001 N001-N110 all numeric relationships | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-main-inventory | DOC-001 N001-N110 all numeric relationships | relationships/numeric_relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-support | DOC-002/DOC-003/DOC-004/DOC-005 all support numeric relationships | checkers/parts/numeric_support.md | COMPLETE |
| numeric_checks | numeric-support-inventory | All support-only numeric relationship records | relationships/parts/numeric_support_inventory.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105 | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | statistics-inventory | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105 | statistics/relationship_inventory.md | COMPLETE |
| cross_source_checks | cross-001 | All matched report/plan and report/report relationships, all primary/key-secondary design specifications | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screen-initial | Every finding emitted by numeric main/support, statistical pass 1 and cross-source checkers | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | ledger-initial | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-initial | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | audit-initial | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013 | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-complete | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013 | ../final_report_1_6_2.md | COMPLETE |
| evidence_recheck | recheck-render-003 | C002; DOC-001 p.3 source visual confirmation | preprocessing/recheck-main-3.png | COMPLETE |
| evidence_recheck | recheck-render-006 | C001, C003, C006, C007, C008, C010, C011; DOC-001 p.6 | preprocessing/recheck-main-6.png | COMPLETE |
| evidence_recheck | recheck-render-007 | C001, C004, C007, C008, C009; DOC-001 p.7 | preprocessing/recheck-main-7.png | COMPLETE |
| evidence_recheck | recheck-render-008 | C001, C002, C004, C005, C011; DOC-001 p.8 | preprocessing/recheck-main-8.png | COMPLETE |
| evidence_recheck | recheck-render-subgroup | C007, C008, C012, C013; DOC-004 p.2 | preprocessing/recheck-subgroup-2.png | COMPLETE |
| inclusion_screening | screen-pass-2 | F-ST2-001, F-ST2-002 new occurrence groups | screening/inclusion_screen_pass_2.md | COMPLETE |
| candidate_registration | ledger-pass-2-occurrences | C007, C010 additional included occurrences F-ST2-001 and F-ST2-002 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-pass-2-occurrences | C007, C010 every added occurrence location | verification/parts/pass_2_occurrence_recheck.md | COMPLETE |
| evidence_quality | audit-coverage | No candidate assignments; all119 source pages, extraction/unit coverage, N001-N166 coverage metadata, routing/tooling and execution records | quality/parts/coverage_quality_audit.md | COMPLETE |
| evidence_recheck | pass2-render-sap-20 | C007; DOC-003 p.20 | preprocessing/pass2-recheck-sap-20.png | COMPLETE |
| evidence_recheck | pass2-render-sap-21 | C007; DOC-003 p.21 | preprocessing/pass2-recheck-sap-21.png | COMPLETE |
| evidence_recheck | pass2-render-sap-25 | C010; DOC-003 p.25 | preprocessing/pass2-recheck-sap-25.png | COMPLETE |
| evidence_recheck | pass2-render-sap-26 | C007, C010; DOC-003 p.26 | preprocessing/pass2-recheck-sap-26.png | COMPLETE |
| evidence_recheck | pass2-render-protocol-17 | C010; DOC-002 p.17 | preprocessing/pass2-recheck-protocol-17.png | COMPLETE |
| evidence_recheck | pass2-render-protocol-18 | C010; DOC-002 p.18 | preprocessing/pass2-recheck-protocol-18.png | COMPLETE |
| evidence_recheck | pass2-render-protocol-31 | C010; DOC-002 p.31 | preprocessing/pass2-recheck-protocol-31.png | COMPLETE |
| evidence_recheck | pass2-render-main-4 | C010; DOC-001 p.4 | preprocessing/pass2-recheck-main-4.png | COMPLETE |
| evidence_recheck | pass2-render-subgroup-2 | C007, C010; DOC-004 p.2 | preprocessing/pass2-recheck-subgroup-2.png | COMPLETE |
| evidence_quality | audit-candidates-main | C001, C002, C003, C004, C005, C006, C007; all associated screening decisions and 17 numeric exclusions | quality/parts/candidate_audit_main.md | COMPLETE |
| evidence_quality | audit-candidates-tail | C008, C009, C010, C011, C012, C013; all associated screening decisions and 22 cross/statistical exclusions | quality/parts/candidate_audit_tail.md | COMPLETE |
| report_generation | report-cards-tail | C008, C009, C010, C011, C012, C013 | report/parts/tail_cards.md | COMPLETE |
| report_generation | report-limitations | Complete package limitations and missing definitions; no candidate assignments | limitations.md | COMPLETE |
