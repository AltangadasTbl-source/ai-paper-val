# Workflow 1.6 Coverage Manifest

Assignments cover every direct-source page. Status is finalized only after a durable stage handoff. Reuse is an extraction optimization, not a scientific scope boundary.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | All five direct PDFs; exact identity, role, page count and source hashes | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | All eligible existing text, OCR, rendered pages and source-location maps | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pages 1-11; all reusable-backed units | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 PDF pages 1-60; all fresh-required units | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-003 PDF pages 1-5; all fresh-required units | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-004 | DOC-004 PDF pages 1-25; reusable pages 1-2 and 16-23; fresh pages 3-15 and 24-25 | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-005 | DOC-005 PDF page 1; fresh-required unit | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-plan-transcriptions | DOC-002 PDF pages 1-60 and DOC-003 pages 1-5; complete direct-source transcription part | extraction/parts/support_plan_transcriptions.md | COMPLETE |
| support_evidence_mapping | support-report-transcriptions | DOC-004 PDF pages 1-25 and DOC-005 page 1; complete source transcription part | extraction/parts/support_report_transcriptions.md | COMPLETE |
| numeric_checks | numeric-001 | All applicable main M001-M120 and support U001-U064 numeric, denominator, label and arithmetic relationships | checkers/numeric_consistency.md | COMPLETE |
| cross_source_checks | cross-001 | Every matched quantitative key across all five documents and main-paper locations | checkers/cross_source_consistency.md | COMPLETE |
| numeric_checks | numeric-main-inventory | N001-N120; every M001-M120 mapping group | relationships/parts/numeric-main.md | COMPLETE |
| numeric_checks | numeric-support-inventory | N121-N184; every U001-U064 mapping family | relationships/parts/numeric-support.md | COMPLETE |
| statistics_pass_1 | stats1-part-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117 | statistics/parts/stats1-relationships-001.md | COMPLETE |
| statistics_pass_1 | stats1-part-002 | S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137, S138, S139, S140 | statistics/parts/stats1-relationships-002.md | COMPLETE |
| candidate_registration | registration-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stats2-part-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117 | statistics/parts/stats2-relationships-001.md | COMPLETE |
| statistics_pass_2 | stats2-part-002 | S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137, S138, S139, S140 | statistics/parts/stats2-relationships-002.md | COMPLETE |
| candidate_registration | registration-append-001 | C021 | candidate_ledger.md | COMPLETE |
| statistics_pass_2 | stats2-new-candidate-001 | C021; descriptive N175/U055 association, no additional inferential S relationship | checkers/statistical_pass_2_new_candidates.md | COMPLETE |
| evidence_recheck | recheck-append-001 | C021 | verification/parts/evidence_recheck_append_001.md | COMPLETE |
| support_evidence_mapping | support-p26-visual-repair | DOC-002 physical p26 two raster product labels omitted from native text; complete support-raster gap check | extraction/parts/support_plan_p26_visual_repair.md | COMPLETE |
| numeric_checks | numeric-visual-repair | U065.a-h; DOC-002 physical p26 product-label quantities and all relevant supplied dose/package comparisons | checkers/numeric_visual_repair.md | COMPLETE |
| numeric_checks | numeric-visual-inventory | N185 only; all U065.a-h product-label numeric relationships | relationships/parts/numeric-visual-repair.md | COMPLETE |
| candidate_registration | registration-append-002 | C022 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-append-002 | C022 | verification/parts/evidence_recheck_append_002.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020, C021, C022 | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020, C021, C022 | ../final_report_1_6.md | COMPLETE |
| report_generation | report-limitations | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020, C021, C022; complete bounded source and definition limits | limitations.md | COMPLETE |
