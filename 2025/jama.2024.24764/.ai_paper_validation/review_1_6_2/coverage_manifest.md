# Workflow 1.6.2 Coverage Manifest

Created before scientific mapping. Reusable extraction is provenance; all supplied pages receive fresh scientific mapping. Support scopes are disjoint because their combined reusable text exceeds the 200000-character shard bound. Each row contains one artifact path. Pending relationship and candidate scopes will be replaced by explicit IDs after their inventories exist.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | All four direct package PDFs; DOC-001 pp. 1-11; DOC-002 pp. 1-46; DOC-003 pp. 1-9; DOC-004 pp. 1-48 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All 69 reused native/layout/OCR text, rendered page, extraction map, and locator metadata assets for all 114 PDF pages | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11; all reusable-backed units; zero fresh-required units | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-sap-results | DOC-002 PDF pp. 1-46 and DOC-003 PDF pp. 1-9; DOC-002 p. 32 fresh visual mapping; other 54 units reusable-backed | extraction/support_sap_results_part.md | COMPLETE |
| support_evidence_mapping | support-sap-p32-render | DOC-002 PDF p. 32 fresh-required assessment-schedule source render; PyMuPDF 1.26.4 CPU 200dpi | preprocessing/support_mapper/DOC-002-p32.png | COMPLETE |
| support_evidence_mapping | support-protocol | DOC-004 PDF pp. 1-48; all reusable-backed units; zero fresh-required units | extraction/support_protocol_part.md | COMPLETE |
| support_evidence_mapping | support-merged | Complete disjoint union DOC-002 pp. 1-46; DOC-003 pp. 1-9; DOC-004 pp. 1-48 | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001-N255 across all four PDFs; full counts/denominator/totals/percentage/effect-identity checks in bounded display batches | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-inventory | N001-N255; complete canonical union of bounded numeric parts | relationships/numeric_relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-part-001 | N001-N120; bounded complete numeric evidence/check records | relationships/parts/numeric_001_120.md | COMPLETE |
| numeric_checks | numeric-part-002 | N121-N240; bounded complete numeric evidence/check records | relationships/parts/numeric_121_240.md | COMPLETE |
| numeric_checks | numeric-part-003 | N241-N255; bounded complete numeric evidence/check records | relationships/parts/numeric_241_255.md | COMPLETE |
| statistics_pass_1 | stat1-checker | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137 | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | stat1-inventory | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137 | statistics/relationship_inventory.md | COMPLETE |
| statistics_pass_1 | stat1-part-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120 | statistics/parts/relationships_001_120.md | COMPLETE |
| statistics_pass_1 | stat1-part-002 | S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137 | statistics/parts/relationships_121_137.md | COMPLETE |
| cross_source_checks | cross-001 | All matched report/report, report/plan and plan/plan result-relevant relationships across four PDFs; F-XS-001, F-XS-002, F-XS-003, F-XS-004, F-XS-005 and 10 excluded observations | checkers/cross_source_consistency.md | COMPLETE |
| cross_source_checks | cross-main-p4 | DOC-001 PDF p. 4 exact-source native text confirmation | preprocessing/cross_source/main-p4.txt | COMPLETE |
| cross_source_checks | cross-main-p8 | DOC-001 PDF p. 8 exact-source native text confirmation | preprocessing/cross_source/main-p8.txt | COMPLETE |
| cross_source_checks | cross-sap-p23-26 | DOC-002 PDF pp. 23-26 exact-source native text confirmation | preprocessing/cross_source/sap-p23-26.txt | COMPLETE |
| cross_source_checks | cross-protocol-p17 | DOC-004 PDF p. 17 exact-source native text confirmation | preprocessing/cross_source/protocol-p17.txt | COMPLETE |
| inclusion_screening | screen-001 | F-XS-001, F-XS-002, F-XS-003, F-XS-004, F-XS-005, F-ST1-001, F-ST1-002, F-ST1-003, F-ST1-004, F-ST1-005 | screening/inclusion_screen.md | COMPLETE |
| inclusion_screening | screen-handoff | All ten initial finding decisions and five consolidated groups | screening/registration_handoff.md | COMPLETE |
| candidate_registration | ledger-001 | C001, C002, C003, C004, C005 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005 | verification/evidence_recheck.md | COMPLETE |
| evidence_recheck | recheck-main-p1-txt | C001, C002; DOC-001 PDF p. 1 direct-source native text | preprocessing/recheck/main-p1.txt | COMPLETE |
| evidence_recheck | recheck-main-p1-png | C001, C002; DOC-001 PDF p. 1 direct-source visual render | preprocessing/recheck/main-p1.png | COMPLETE |
| evidence_recheck | recheck-main-p2-txt | C003; DOC-001 PDF p. 2 direct-source native text | preprocessing/recheck/main-p2.txt | COMPLETE |
| evidence_recheck | recheck-main-p2-png | C003; DOC-001 PDF p. 2 direct-source visual render | preprocessing/recheck/main-p2.png | COMPLETE |
| evidence_recheck | recheck-main-p4-txt | C002, C004; DOC-001 PDF p. 4 direct-source native text | preprocessing/recheck/main-p4.txt | COMPLETE |
| evidence_recheck | recheck-main-p4-png | C002, C004; DOC-001 PDF p. 4 direct-source visual render | preprocessing/recheck/main-p4.png | COMPLETE |
| evidence_recheck | recheck-main-p6-txt | C001, C002; DOC-001 PDF p. 6 direct-source native text | preprocessing/recheck/main-p6.txt | COMPLETE |
| evidence_recheck | recheck-main-p6-png | C001, C002; DOC-001 PDF p. 6 direct-source visual render | preprocessing/recheck/main-p6.png | COMPLETE |
| evidence_recheck | recheck-main-p8-txt | C002, C004; DOC-001 PDF p. 8 direct-source native text | preprocessing/recheck/main-p8.txt | COMPLETE |
| evidence_recheck | recheck-main-p8-png | C002, C004; DOC-001 PDF p. 8 direct-source visual render | preprocessing/recheck/main-p8.png | COMPLETE |
| evidence_recheck | recheck-main-p10-txt | C003; DOC-001 PDF p. 10 direct-source native text | preprocessing/recheck/main-p10.txt | COMPLETE |
| evidence_recheck | recheck-main-p10-png | C003; DOC-001 PDF p. 10 direct-source visual render | preprocessing/recheck/main-p10.png | COMPLETE |
| evidence_recheck | recheck-sap-p12-txt | C001; DOC-002 PDF p. 12 direct-source native text | preprocessing/recheck/sap-p12.txt | COMPLETE |
| evidence_recheck | recheck-sap-p12-png | C001; DOC-002 PDF p. 12 direct-source visual render | preprocessing/recheck/sap-p12.png | COMPLETE |
| evidence_recheck | recheck-sap-p15-txt | C002; DOC-002 PDF p. 15 direct-source native text | preprocessing/recheck/sap-p15.txt | COMPLETE |
| evidence_recheck | recheck-sap-p15-png | C002; DOC-002 PDF p. 15 direct-source visual render | preprocessing/recheck/sap-p15.png | COMPLETE |
| evidence_recheck | recheck-sap-p25-txt | C002; DOC-002 PDF p. 25 direct-source native text | preprocessing/recheck/sap-p25.txt | COMPLETE |
| evidence_recheck | recheck-sap-p25-png | C002; DOC-002 PDF p. 25 direct-source visual render | preprocessing/recheck/sap-p25.png | COMPLETE |
| evidence_recheck | recheck-sap-p26-txt | C004, C005; DOC-002 PDF p. 26 direct-source native text | preprocessing/recheck/sap-p26.txt | COMPLETE |
| evidence_recheck | recheck-sap-p26-png | C004, C005; DOC-002 PDF p. 26 direct-source visual render | preprocessing/recheck/sap-p26.png | COMPLETE |
| evidence_recheck | recheck-sap-p42-txt | C002; DOC-002 PDF p. 42 direct-source native text | preprocessing/recheck/sap-p42.txt | COMPLETE |
| evidence_recheck | recheck-sap-p42-png | C002; DOC-002 PDF p. 42 direct-source visual render | preprocessing/recheck/sap-p42.png | COMPLETE |
| evidence_recheck | recheck-results-p3-txt | C004; DOC-003 PDF p. 3 direct-source native text | preprocessing/recheck/results-p3.txt | COMPLETE |
| evidence_recheck | recheck-results-p3-png | C004; DOC-003 PDF p. 3 direct-source visual render | preprocessing/recheck/results-p3.png | COMPLETE |
| evidence_recheck | recheck-results-p4-txt | C001, C004; DOC-003 PDF p. 4 direct-source native text | preprocessing/recheck/results-p4.txt | COMPLETE |
| evidence_recheck | recheck-results-p4-png | C001, C004; DOC-003 PDF p. 4 direct-source visual render | preprocessing/recheck/results-p4.png | COMPLETE |
| evidence_recheck | recheck-protocol-p2-txt | C003; DOC-004 PDF p. 2 direct-source native text | preprocessing/recheck/protocol-p2.txt | COMPLETE |
| evidence_recheck | recheck-protocol-p2-png | C003; DOC-004 PDF p. 2 direct-source visual render | preprocessing/recheck/protocol-p2.png | COMPLETE |
| evidence_recheck | recheck-protocol-p8-txt | C003; DOC-004 PDF p. 8 direct-source native text | preprocessing/recheck/protocol-p8.txt | COMPLETE |
| evidence_recheck | recheck-protocol-p8-png | C003; DOC-004 PDF p. 8 direct-source visual render | preprocessing/recheck/protocol-p8.png | COMPLETE |
| evidence_recheck | recheck-protocol-p17-txt | C003; DOC-004 PDF p. 17 direct-source native text | preprocessing/recheck/protocol-p17.txt | COMPLETE |
| evidence_recheck | recheck-protocol-p17-png | C003; DOC-004 PDF p. 17 direct-source visual render | preprocessing/recheck/protocol-p17.png | COMPLETE |
| evidence_recheck | recheck-protocol-p24-txt | C002; DOC-004 PDF p. 24 direct-source native text | preprocessing/recheck/protocol-p24.txt | COMPLETE |
| evidence_recheck | recheck-protocol-p24-png | C002; DOC-004 PDF p. 24 direct-source visual render | preprocessing/recheck/protocol-p24.png | COMPLETE |
| evidence_recheck | recheck-protocol-p39-txt | C002; DOC-004 PDF p. 39 direct-source native text | preprocessing/recheck/protocol-p39.txt | COMPLETE |
| evidence_recheck | recheck-protocol-p39-png | C002; DOC-004 PDF p. 39 direct-source visual render | preprocessing/recheck/protocol-p39.png | COMPLETE |
| evidence_recheck | recheck-main-full | C001, C002, C003, C004; DOC-001 PDF pp. 1-11 full source text for bounded absence and context checks | preprocessing/recheck/main-full.txt | COMPLETE |
| evidence_recheck | recheck-results-full | C001, C002, C004; DOC-003 PDF pp. 1-9 full source text for bounded absence and context checks | preprocessing/recheck/results-full.txt | COMPLETE |
| evidence_recheck | recheck-protocol-full | C002, C003; DOC-004 PDF pp. 1-48 full source text for bounded absence and context checks | preprocessing/recheck/protocol-full.txt | COMPLETE |
| statistics_pass_2 | stat2-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | audit-001 | C001, C002, C003, C004, C005; all coverage, screening, excluded observations, classification and agent provenance | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005 | ../final_report_1_6_2.md | COMPLETE |
