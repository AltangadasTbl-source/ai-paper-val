# Workflow 1.6.2 Coverage Manifest

Scopes partition every supplied source page. All relative artifact paths are based on this review directory. Status is finalized after the assigned stage completes.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-001 | DOC-001 pp. 1-10; DOC-002 pp. 1-25; DOC-003 pp. 1-9 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All source-linked reusable derivatives for DOC-001, DOC-002, DOC-003 | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10, all reusable-backed units; no fresh-required units | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-25 and DOC-003 PDF pp. 1-9, all reusable-backed units; no fresh-required units | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | All 150 stable N relationships in two bounded partitions | checkers/numeric_consistency.md | COMPLETE |
| cross_source_checks | cross-001 | Complete matched report/report, plan/report, and plan/plan relationships | checkers/cross_source_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120 | checkers/statistical_pass_1.md | COMPLETE |
| inclusion_screening | screening-001 | F-NUM-001, F-NUM-002, F-XS-001, F-XS-002, F-XS-003, F-XS-004, F-ST1-001, F-ST1-002, F-ST1-003, F-ST1-004 | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005; every screening decision, checker exclusion, relationship, source unit, and execution | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005 | ../final_report_1_6_2.md | COMPLETE |
| report_generation | report-002 | C001, C002, C003, C004, C005; complete package limitations | limitations.md | COMPLETE |
| numeric_checks | numeric-part-001 | N001 through N120, first bounded inventory partition | relationships/parts/numeric_001_120.md | COMPLETE |
| numeric_checks | numeric-part-002 | N121 through N150, second bounded inventory partition | relationships/parts/numeric_121_150.md | COMPLETE |
| numeric_checks | numeric-tail-review | N121 through N150, fresh bounded coverage repair | checkers/parts/numeric_tail.md | COMPLETE |
| numeric_checks | numeric-inventory | All 150 stable N relationships, with two bounded partitions | relationships/numeric_relationship_inventory.md | COMPLETE |
| statistics_pass_1 | statistics-inventory | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120 | statistics/relationship_inventory.md | COMPLETE |
| evidence_assets | recheck-derivative-log | DOC-001 pp.1,3,4,5,6,7,8; DOC-002 pp.16,18,19; DOC-003 p.2; 22 direct CPU derivatives | preprocessing/recheck_derivative_record.md | COMPLETE |
| evidence_assets | direct-recheck-main-p1.txt | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p1.txt | COMPLETE |
| evidence_assets | direct-recheck-main-p3.txt | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p3.txt | COMPLETE |
| evidence_assets | direct-recheck-main-p4.txt | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p4.txt | COMPLETE |
| evidence_assets | direct-recheck-main-p5.txt | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p5.txt | COMPLETE |
| evidence_assets | direct-recheck-main-p6.txt | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p6.txt | COMPLETE |
| evidence_assets | direct-recheck-main-p7.txt | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p7.txt | COMPLETE |
| evidence_assets | direct-recheck-main-p8.txt | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p8.txt | COMPLETE |
| evidence_assets | direct-recheck-plan-p16.txt | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-plan-p16.txt | COMPLETE |
| evidence_assets | direct-recheck-plan-p18.txt | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-plan-p18.txt | COMPLETE |
| evidence_assets | direct-recheck-plan-p19.txt | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-plan-p19.txt | COMPLETE |
| evidence_assets | direct-recheck-supp-p2.txt | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-supp-p2.txt | COMPLETE |
| evidence_assets | direct-recheck-main-p1.png | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p1.png | COMPLETE |
| evidence_assets | direct-recheck-main-p3.png | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p3.png | COMPLETE |
| evidence_assets | direct-recheck-main-p4.png | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p4.png | COMPLETE |
| evidence_assets | direct-recheck-main-p5.png | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p5.png | COMPLETE |
| evidence_assets | direct-recheck-main-p6.png | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p6.png | COMPLETE |
| evidence_assets | direct-recheck-main-p7.png | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p7.png | COMPLETE |
| evidence_assets | direct-recheck-main-p8.png | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-main-p8.png | COMPLETE |
| evidence_assets | direct-recheck-plan-p16.png | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-plan-p16.png | COMPLETE |
| evidence_assets | direct-recheck-plan-p18.png | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-plan-p18.png | COMPLETE |
| evidence_assets | direct-recheck-plan-p19.png | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-plan-p19.png | COMPLETE |
| evidence_assets | direct-recheck-supp-p2.png | Exact source/page recorded in recheck_derivative_record.md; CPU Poppler 25.03.0 | preprocessing/recheck-supp-p2.png | COMPLETE |
| main_evidence_mapping | main-structured | DOC-001 pp.1-10; complete structured mapping preceding duplicate raw-text locator appendix | extraction/main_relationship_map.md | COMPLETE |
| inclusion_screening | screening-002 | F-ST2-001, independent fresh pass-2 screen | screening/inclusion_screen_pass_2.md | COMPLETE |
| candidate_registration | candidates-002 | C005, independently included pass-2 issue appended without renumbering | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-002 | C005, complete appended issue and empirical comparison pattern | verification/parts/evidence_recheck_appended.md | COMPLETE |
| evidence_assets | direct-recheck5-supp-p6.txt | C005 results supplement exact source page recorded in appended recheck; CPU Poppler 25.03.0 | preprocessing/recheck5-supp-p6.txt | COMPLETE |
| evidence_assets | direct-recheck5-supp-p7.txt | C005 results supplement exact source page recorded in appended recheck; CPU Poppler 25.03.0 | preprocessing/recheck5-supp-p7.txt | COMPLETE |
| evidence_assets | direct-recheck5-supp-p6.png | C005 results supplement exact source page recorded in appended recheck; CPU Poppler 25.03.0 | preprocessing/recheck5-supp-p6.png | COMPLETE |
| evidence_assets | direct-recheck5-supp-p7.png | C005 results supplement exact source page recorded in appended recheck; CPU Poppler 25.03.0 | preprocessing/recheck5-supp-p7.png | COMPLETE |
