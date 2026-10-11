# Workflow 1.6.2 Coverage Manifest

Created before scientific mapping. Source scopes are disjoint; all 64 source pages require mapping even though each has reusable extraction. Later relationship and candidate scopes will enumerate every stable ID explicitly.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 pp. 1-11; DOC-002 pp. 1-33; DOC-003 pp. 1-19; DOC-004 p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Every reusable source-linked text, metadata and rendered-page asset for the four direct PDFs | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11, reusable-backed; no fresh-required pages | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-33, DOC-003 PDF pp. 1-19, DOC-004 PDF p. 1, reusable-backed; no fresh-required pages | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | All result-relevant numeric relationships in complete main and support maps | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-inventory-001 | Complete stable N relationship inventory | relationships/numeric_relationship_inventory.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082 | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | statistics-inventory-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082 | statistics/relationship_inventory.md | COMPLETE |
| cross_source_checks | cross-source-001 | Every matched report result and planned-versus-reported design element across all four sources | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screening-001 | Every finding from numeric, cross-source and statistical pass 1 | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | registration-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018 | candidate_ledger.md | COMPLETE |
| candidate_registration | card-metadata-projection | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018; exact canonical classification and card metadata for bounded report handoff | candidate_card_metadata.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018; every screening decision, checker exclusion and coverage row | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018 | ../final_report_1_6_2.md | COMPLETE |
| report_generation | report-limitations-001 | Complete source, tooling and statistical definition limitations | limitations.md | COMPLETE |
| numeric_checks | numeric-render-018 | DOC-003 PDF p. 18 direct-source visual confirmation | preprocessing/numeric_checker/supp2-18.png | COMPLETE |
| numeric_checks | numeric-render-019 | DOC-003 PDF p. 19 direct-source visual confirmation | preprocessing/numeric_checker/supp2-19.png | COMPLETE |
| statistics_pass_1 | statistics-text-plan-017 | DOC-002 PDF pp. 17-23 source confirmation | preprocessing/statistical_pass_1/plan17-23.txt | COMPLETE |
| statistics_pass_1 | statistics-text-plan-031 | DOC-002 PDF pp. 31-33 source confirmation | preprocessing/statistical_pass_1/plan31-33.txt | COMPLETE |
| statistics_pass_1 | statistics-text-supp-002 | DOC-003 PDF pp. 2-4 source confirmation | preprocessing/statistical_pass_1/supp2-4.txt | COMPLETE |
| inclusion_screening | screening-text-001 | DOC-001 PDF p. 1 direct-source screening confirmation | preprocessing/inclusion_initial/main-1.txt | COMPLETE |
| inclusion_screening | screening-text-002 | DOC-001 PDF p. 10 direct-source screening confirmation | preprocessing/inclusion_initial/main-10.txt | COMPLETE |
| inclusion_screening | screening-text-003 | DOC-001 PDF p. 11 direct-source screening confirmation | preprocessing/inclusion_initial/main-11.txt | COMPLETE |
| inclusion_screening | screening-text-004 | DOC-001 PDF p. 2 direct-source screening confirmation | preprocessing/inclusion_initial/main-2.txt | COMPLETE |
| inclusion_screening | screening-text-005 | DOC-001 PDF p. 3 direct-source screening confirmation | preprocessing/inclusion_initial/main-3.txt | COMPLETE |
| inclusion_screening | screening-text-006 | DOC-001 PDF p. 4 direct-source screening confirmation | preprocessing/inclusion_initial/main-4.txt | COMPLETE |
| inclusion_screening | screening-text-007 | DOC-001 PDF p. 5 direct-source screening confirmation | preprocessing/inclusion_initial/main-5.txt | COMPLETE |
| inclusion_screening | screening-text-008 | DOC-001 PDF p. 6 direct-source screening confirmation | preprocessing/inclusion_initial/main-6.txt | COMPLETE |
| inclusion_screening | screening-text-009 | DOC-001 PDF p. 7 direct-source screening confirmation | preprocessing/inclusion_initial/main-7.txt | COMPLETE |
| inclusion_screening | screening-text-010 | DOC-001 PDF p. 8 direct-source screening confirmation | preprocessing/inclusion_initial/main-8.txt | COMPLETE |
| inclusion_screening | screening-text-011 | DOC-001 PDF p. 9 direct-source screening confirmation | preprocessing/inclusion_initial/main-9.txt | COMPLETE |
| inclusion_screening | screening-text-012 | DOC-002 PDF p. 11 direct-source screening confirmation | preprocessing/inclusion_initial/plan-11.txt | COMPLETE |
| inclusion_screening | screening-text-013 | DOC-002 PDF p. 12 direct-source screening confirmation | preprocessing/inclusion_initial/plan-12.txt | COMPLETE |
| inclusion_screening | screening-text-014 | DOC-002 PDF p. 14 direct-source screening confirmation | preprocessing/inclusion_initial/plan-14.txt | COMPLETE |
| inclusion_screening | screening-text-015 | DOC-002 PDF p. 15 direct-source screening confirmation | preprocessing/inclusion_initial/plan-15.txt | COMPLETE |
| inclusion_screening | screening-text-016 | DOC-002 PDF p. 17 direct-source screening confirmation | preprocessing/inclusion_initial/plan-17.txt | COMPLETE |
| inclusion_screening | screening-text-017 | DOC-002 PDF p. 19 direct-source screening confirmation | preprocessing/inclusion_initial/plan-19.txt | COMPLETE |
| inclusion_screening | screening-text-018 | DOC-002 PDF p. 21 direct-source screening confirmation | preprocessing/inclusion_initial/plan-21.txt | COMPLETE |
| inclusion_screening | screening-text-019 | DOC-002 PDF p. 31 direct-source screening confirmation | preprocessing/inclusion_initial/plan-31.txt | COMPLETE |
| inclusion_screening | screening-text-020 | DOC-002 PDF p. 32 direct-source screening confirmation | preprocessing/inclusion_initial/plan-32.txt | COMPLETE |
| inclusion_screening | screening-text-021 | DOC-002 PDF p. 33 direct-source screening confirmation | preprocessing/inclusion_initial/plan-33.txt | COMPLETE |
| inclusion_screening | screening-text-022 | DOC-002 PDF p. 4 direct-source screening confirmation | preprocessing/inclusion_initial/plan-4.txt | COMPLETE |
| inclusion_screening | screening-text-023 | DOC-002 PDF pp. 28-30 direct-source screening confirmation | preprocessing/inclusion_initial/plan-references-28-30.txt | COMPLETE |
| inclusion_screening | screening-text-024 | DOC-003 PDF p. 10 direct-source screening confirmation | preprocessing/inclusion_initial/supp-10.txt | COMPLETE |
| inclusion_screening | screening-text-025 | DOC-003 PDF p. 11 direct-source screening confirmation | preprocessing/inclusion_initial/supp-11.txt | COMPLETE |
| inclusion_screening | screening-text-026 | DOC-003 PDF p. 12 direct-source screening confirmation | preprocessing/inclusion_initial/supp-12.txt | COMPLETE |
| inclusion_screening | screening-text-027 | DOC-003 PDF p. 13 direct-source screening confirmation | preprocessing/inclusion_initial/supp-13.txt | COMPLETE |
| inclusion_screening | screening-text-028 | DOC-003 PDF p. 16 direct-source screening confirmation | preprocessing/inclusion_initial/supp-16.txt | COMPLETE |
| inclusion_screening | screening-text-029 | DOC-003 PDF p. 18 direct-source screening confirmation | preprocessing/inclusion_initial/supp-18.txt | COMPLETE |
| inclusion_screening | screening-text-030 | DOC-003 PDF p. 19 direct-source screening confirmation | preprocessing/inclusion_initial/supp-19.txt | COMPLETE |
| inclusion_screening | screening-text-031 | DOC-003 PDF p. 2 direct-source screening confirmation | preprocessing/inclusion_initial/supp-2.txt | COMPLETE |
| inclusion_screening | screening-text-032 | DOC-003 PDF p. 3 direct-source screening confirmation | preprocessing/inclusion_initial/supp-3.txt | COMPLETE |
| inclusion_screening | screening-text-033 | DOC-003 PDF p. 4 direct-source screening confirmation | preprocessing/inclusion_initial/supp-4.txt | COMPLETE |
| inclusion_screening | screening-text-034 | DOC-003 PDF p. 6 direct-source screening confirmation | preprocessing/inclusion_initial/supp-6.txt | COMPLETE |
| inclusion_screening | screening-text-035 | DOC-003 PDF p. 7 direct-source screening confirmation | preprocessing/inclusion_initial/supp-7.txt | COMPLETE |
| inclusion_screening | screening-text-036 | DOC-003 PDF p. 9 direct-source screening confirmation | preprocessing/inclusion_initial/supp-9.txt | COMPLETE |
| inclusion_screening | screening-derivative-record | Exact source windows and producing engines for 36 independent source confirmations | preprocessing/inclusion_initial/derivative_record.md | COMPLETE |
| statistics_pass_2 | exclusions-projection | Every excluded observation from numeric, cross-source and statistical pass 1 checkers | checkers/complete_excluded_observations.md | COMPLETE |
| evidence_recheck | recheck-derivative-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018; DOC-001 PDF pp. 1-11 source confirmation | preprocessing/evidence_recheck/main-full.txt | COMPLETE |
| evidence_recheck | recheck-derivative-002 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018; DOC-002 PDF pp. 1-33 source confirmation | preprocessing/evidence_recheck/plan-full.txt | COMPLETE |
| evidence_recheck | recheck-derivative-003 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018; DOC-003 PDF pp. 1-19 source confirmation | preprocessing/evidence_recheck/supp-full.txt | COMPLETE |
| evidence_recheck | recheck-derivative-004 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018; DOC-004 PDF p. 1; report-wide absence check source confirmation | preprocessing/evidence_recheck/sharing-full.txt | COMPLETE |
| evidence_recheck | recheck-derivative-005 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018; DOC-002 PDF p. 32 model equations source confirmation | preprocessing/evidence_recheck/plan-32.png | COMPLETE |
| evidence_recheck | recheck-derivative-006 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018; DOC-001 PDF p. 8 table/figure columns source confirmation | preprocessing/evidence_recheck/main-8.png | COMPLETE |
| evidence_recheck | recheck-derivative-007 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018; DOC-003 PDF p. 17 biomarker plot content source confirmation | preprocessing/evidence_recheck/supp-17.png | COMPLETE |
| main_evidence_mapping | main-structured-projection | DOC-001 PDF pp. 1-11 complete structured map and registers; full page appendix preserved canonically | extraction/main_quantitative_structured.md | COMPLETE |
| evidence_quality | quality-source-coverage-part | No assigned C IDs; all 64 direct source units, extraction/map coverage, inventory ID/status closure, paths and provenance | quality/parts/source_coverage_audit.md | COMPLETE |
| statistics_pass_2 | pass2-source-1 | DOC-001 PDF pp. 1-11; complete second-pass source confirmation | preprocessing/statistical_pass_2/main-full.txt | COMPLETE |
| statistics_pass_2 | pass2-source-2 | DOC-002 PDF pp. 1-33; complete second-pass source confirmation | preprocessing/statistical_pass_2/plan-full.txt | COMPLETE |
| statistics_pass_2 | pass2-source-3 | DOC-003 PDF pp. 1-19; complete second-pass source confirmation | preprocessing/statistical_pass_2/supp-full.txt | COMPLETE |
