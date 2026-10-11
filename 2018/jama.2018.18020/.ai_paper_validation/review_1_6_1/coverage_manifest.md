# Workflow 1.6.1 Coverage Manifest

Scopes partition direct source units by source and page. Every artifact cell contains one relative path. Statistical and candidate scopes will be enumerated after discovery; planned stages remain pending until their durable handoffs close.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-001 | DOC-001 PDF pp.1-10; DOC-002 PDF pp.1-55; DOC-003 PDF pp.1-17; DOC-004 PDF p.1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All reusable source-linked assets for DOC-001 through DOC-004 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp.1-10, all reusable-backed units | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp.1-55; DOC-003 PDF pp.1-17; DOC-004 PDF p.1, all reusable-backed units | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | Complete main/support numeric evidence union | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-inventory-001 | All numeric relationships in the evidence union | relationships/numeric_relationship_inventory.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111 | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | statistics-inventory-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111 | statistics/relationship_inventory.md | COMPLETE |
| cross_source_checks | cross-source-001 | All matched report and plan relationships | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screen-001 | Every numeric, cross-source and pass-1 checker finding | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | ledger-001 | C001, C002, C003, C004 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | audit-001 | C001, C002, C003, C004; all exclusions, screening and coverage | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004 | ../final_report_1_6_1.md | COMPLETE |
| cross_source_checks | xs-render-main-005 | DOC-001 PDF p.5, direct graphical confirmation | preprocessing/xs-main-page5.png | COMPLETE |
| cross_source_checks | xs-render-plan-039 | DOC-002 PDF p.39, direct safety-rule confirmation | preprocessing/xs-plan-page39.png | COMPLETE |
| statistics_pass_1 | stat1-render-main-005 | DOC-001 PDF p.5, direct primary graphical confirmation | preprocessing/stat1-main-page5.png | COMPLETE |
| inclusion_screening | screen-render-main-006 | DOC-001 PDF p.6, direct figure corroboration | preprocessing/screen-main-page6.png | COMPLETE |
| inclusion_screening | screen-render-main-007 | DOC-001 PDF p.7, direct statistical table confirmation | preprocessing/screen-main-page7.png | COMPLETE |
| inclusion_screening | screen-render-main-008 | DOC-001 PDF p.8, direct table/footnote confirmation | preprocessing/screen-main-page8.png | COMPLETE |
| evidence_recheck | render-recheck-main-page3 | DOC-001 PDF p.3; C001, C002, C003 source confirmation aids | preprocessing/recheck-main-page3.png | COMPLETE |
| evidence_recheck | render-recheck-main-page4 | DOC-001 PDF p.4; C002, C003, C004 source confirmation aids | preprocessing/recheck-main-page4.png | COMPLETE |
| evidence_recheck | render-recheck-main-page5 | DOC-001 PDF p.5; C001, C004 source confirmation aids | preprocessing/recheck-main-page5.png | COMPLETE |
| evidence_recheck | render-recheck-plan-page41 | DOC-002 PDF p.41; C002 source confirmation aids | preprocessing/recheck-plan-page41.png | COMPLETE |
| evidence_recheck | render-recheck-results-page10 | DOC-003 PDF p.10; C002 source confirmation aids | preprocessing/recheck-results-page10.png | COMPLETE |
| evidence_recheck | render-recheck-results-page11 | DOC-003 PDF p.11; C002 source confirmation aids | preprocessing/recheck-results-page11.png | COMPLETE |
| evidence_recheck | render-recheck-results-page13 | DOC-003 PDF p.13; C002 source confirmation aids | preprocessing/recheck-results-page13.png | COMPLETE |
| evidence_quality | audit-numeric-coverage | No candidate assignment; all39 N families and all83 page-coverage units | quality/parts/numeric_coverage_audit.md | COMPLETE |
| evidence_quality | audit-statistical-coverage | No candidate assignment; all103 S families and all27 S107 tuples | quality/parts/statistical_coverage_audit.md | COMPLETE |
