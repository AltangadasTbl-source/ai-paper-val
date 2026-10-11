# Coverage manifest

Each Artifact cell is one plain path relative to this run directory. Mapping covers all direct-source pages; reuse is a preprocessing optimization. Relationship and candidate scopes are enumerated after inventories and screening stabilize.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-001 | All three direct PDFs and all 44 PDF pages | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Every eligible existing source-linked extraction and rendered page | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10, reusable-backed and fresh-required units | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-25 and DOC-003 PDF pp. 1-9, reusable-backed and fresh-required units | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | All mapped numeric relationships, partitioned main N001–N080 and support N081–N156 | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-main | N001–N080, DOC-001 main evidence | relationships/numeric_main.md | COMPLETE |
| numeric_checks | numeric-support | N081–N156, DOC-002 and DOC-003 support evidence | relationships/numeric_support.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100 | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | statistics-001-design | S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129 | checkers/parts/statistical_pass_1_design.md | COMPLETE |
| statistics_pass_1 | statistical-results | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100 | statistics/relationship_results.md | COMPLETE |
| statistics_pass_1 | statistical-design | S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129 | statistics/relationship_design.md | COMPLETE |
| evidence_assets | st1-main-render | DOC-001 PDF p.3, primary definition | preprocessing/st1-main-p3.png | COMPLETE |
| evidence_assets | st1-plan-render | DOC-002 PDF p.16, planned definition | preprocessing/st1-plan-p16.png | COMPLETE |
| cross_source_checks | cross-001 | All matched report and plan relationships | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screen-001 | Every checker finding from initial three review lanes | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | candidates-001 | C001 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002-results | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100 | checkers/parts/statistical_pass_2_results.md | COMPLETE |
| statistics_pass_2 | statistics-002-design | S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129 | checkers/parts/statistical_pass_2_design.md | COMPLETE |
| statistics_pass_2 | statistics-002-merge | Both disjoint statistical pass 2 parts merged without loss | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001; every screening decision, exclusion, relationship and coverage row | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001; full coverage and limitations | ../final_report_1_6_1.md | COMPLETE |
| evidence_assets | recheck-main-text | DOC-001 PDF pp.1–5, exact cited source locations | preprocessing/recheck-main-p1-p5-layout.txt | COMPLETE |
| evidence_assets | recheck-main-table | DOC-001 PDF p.7, all Table 2 inputs | preprocessing/recheck-main-p7-layout.txt | COMPLETE |
| evidence_assets | recheck-plan-definition | DOC-002 PDF p.16, planned composite definition | preprocessing/recheck-plan-p16-layout.txt | COMPLETE |
| evidence_assets | recheck-plan-model | DOC-002 PDF pp.18–19, opportunity-model context | preprocessing/recheck-plan-p18-p19-layout.txt | COMPLETE |
| evidence_assets | recheck-supp-definition | DOC-003 PDF p.2, randomized-phase definition | preprocessing/recheck-report-supp-p2-layout.txt | COMPLETE |
| evidence_assets | recheck-main-render | DOC-001 PDF p.7, visual count confirmation | preprocessing/recheck-main-p7.png | COMPLETE |
| evidence_assets | recheck-supp-render | DOC-003 PDF p.2, visual definition confirmation | preprocessing/recheck-report-supp-p2.png | COMPLETE |
