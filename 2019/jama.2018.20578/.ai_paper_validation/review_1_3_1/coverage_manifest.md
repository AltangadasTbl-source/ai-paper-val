# Workflow 1.3.1 Coverage Manifest

This manifest was created after source/evidence-asset inventory and before scientific extraction.
Scopes are complete and disjoint. `ASSIGNED` rows will be changed to `COMPLETE` only after their
canonical artifacts document the full assigned scope.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 PDF pp. 1-10; DOC-002 PDF pp. 1-7; DOC-003 PDF pp. 1-29 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | A001-A047: every registered reusable document map, manifest, native/normalized/OCR text, OCR metadata, rendered page, and full-document layout-text asset | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-10, including abstract, narrative, Figures 1-2, Tables 1-5, captions, footnotes, and 73 mapped result-relevant numeric/statistical relationships | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-7 and DOC-003 PDF pp. 1-29, including protocol definitions, eMethods, eTables 1-6, eFigures 1-4, captions, footnotes, and all mapped cross-document keys | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061, N062, N063, N064, N065, N066, N067, N068, N069, N070, N071, N072, N073, N074, N075, N076 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | 30 checked-match groups covering every matchable result/definition across DOC-001, DOC-002, and DOC-003 after population/time/contrast/model/measure matching | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020, C021, C022, C023, C024 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020, C021, C022, C023, C024 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020, C021, C022, C023, C024; every coverage row | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020, C021, C022, C023, C024; complete package, reused-evidence, relationship, coverage, limitation, adjudication, and source-integrity provenance | ../final_report_1_3_1.md | COMPLETE |
| report_generation | report-header | Package/reused-evidence provenance, scope, relationship coverage, candidate index, and report introduction | report_parts/report_header.md | COMPLETE |
| report_generation | report-cards | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020, C021, C022, C023, C024 | report_parts/candidate_cards.md | COMPLETE |
| report_generation | report-footer | Downstream evidence-chain considerations, limitations, human checklist, and reproducibility metadata | report_parts/report_footer.md | COMPLETE |
| report_generation | report-builder | Deterministic AWK assembly rules used to transform the conserved ledger cards into the exact report-card field schema | report_parts/build_cards.awk | COMPLETE |
