# Workflow 1.6.2 Coverage Manifest

Source/evidence scopes are disjoint at the page-mapping stage. Reused extraction is a locator; current-source confirmation remains authoritative. Relationship and candidate scopes will be enumerated when their inventories exist.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | All four supplied PDFs and content-based document roles | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Every eligible legacy extraction, page image and provenance map; exact page fitness and reuse assignment | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 current main article PDF pages 1-11; all fresh-required | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 protocol PDF pages 1-26; DOC-003 SAP PDF pages 1-29; DOC-004 results supplement PDF pages 1-6; reusable-backed and any gaps | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-main-001 | Main mapper locators N001-N100; every main count/denominator/total and population quantity | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-support-001 | Support mapper locators N201-N241; every supplied support results count/denominator/total | checkers/parts/numeric_support.md | COMPLETE |
| numeric_checks | numeric-inventory-main-001 | Main mapper locators N001-N100; canonical numeric inventory | relationships/numeric_relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-inventory-support-001 | Support mapper locators N201-N241; support numeric inventory part | relationships/parts/numeric_support_inventory.md | COMPLETE |
| statistics_pass_1 | statistics-main-plan-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222, S223, S224, S225, S226, S227, S228, S229, S230, S272, S273, S274, S275, S276, S277, S278, S279, S280, S281, S282, S283, S284, S285, S286, S287, S288 | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | statistics-support-results-001 | S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242, S243, S244, S245, S246, S247, S248, S249, S250, S251, S252, S253, S254, S255, S256, S257, S258, S259, S260, S261, S262, S263, S264, S265, S266, S267, S268, S269, S270, S271 | checkers/parts/statistical_support_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | Every matched main/results-supplement primary and key secondary result and every applicable report-plan/plan-plan statistical design element | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screen-initial-001 | F-XS-001, F-XS-002, F-XS-003, F-XS-004, F-XS-005, F-ST1-001, F-ST1-002, F-ST1-003, F-ST1-004 | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | ledger-001 | C001, C002, C003 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-main-plan-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222, S223, S224, S225, S226, S227, S228, S229, S230, S272, S273, S274, S275, S276, S277, S278, S279, S280, S281, S282, S283, S284, S285, S286, S287, S288 | checkers/statistical_pass_2.md | COMPLETE |
| statistics_pass_2 | statistics-support-results-002 | S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242, S243, S244, S245, S246, S247, S248, S249, S250, S251, S252, S253, S254, S255, S256, S257, S258, S259, S260, S261, S262, S263, S264, S265, S266, S267, S268, S269, S270, S271 | checkers/parts/statistical_support_pass_2.md | COMPLETE |
| statistics_pass_1 | inventory-support-pass1 | S231-S271 retained individual pass-1 support records | statistics/parts/support_relationship_inventory.md | COMPLETE |
| statistics_pass_2 | inventory-support-pass2 | S231-S271 independent individual pass-2 support records | statistics/parts/support_pass_2_inventory.md | COMPLETE |
| statistics_pass_2 | inventory-canonical | All 156 relationship identities; complete individual pass-1 and pass-2 facts | statistics/relationship_inventory.md | COMPLETE |
| evidence_quality | audit-all-001 | C001, C002, C003; every screening decision, exclusion row, source and stage coverage row | quality/evidence_quality_audit.md | COMPLETE |
| evidence_quality | audit-statistical-projection | All 156 statistical identities and their per-record completion states, mechanically projected | quality/statistical_coverage_projection.txt | COMPLETE |
| evidence_quality | audit-main | DOC-001 REPORT PDF pages 3-4; exact native source reread, PyMuPDF1.26.4 CPU | quality/audit_main3-4.txt | COMPLETE |
| evidence_quality | audit-protocol | DOC-002 PLAN PDF pages 17-21; exact native source reread, PyMuPDF1.26.4 CPU | quality/audit_protocol17-21.txt | COMPLETE |
| evidence_quality | audit-sap-rules | DOC-003 PLAN PDF pages 11-14; exact native source reread, PyMuPDF1.26.4 CPU | quality/audit_SAP11-14.txt | COMPLETE |
| evidence_quality | audit-sap-shells | DOC-003 PLAN PDF pages 25-26; exact native source reread, PyMuPDF1.26.4 CPU | quality/audit_SAP25-26.txt | COMPLETE |
| report_generation | report-all-001 | C001, C002, C003; complete coverage, screening, classification, limitations and execution metadata | ../final_report_1_6_2.md | COMPLETE |
| report_generation | report-limitations-001 | Complete current-run scientific and tooling limitations | limitations.md | COMPLETE |
