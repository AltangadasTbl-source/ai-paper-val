# Coverage Manifest

This manifest is initialized before scientific extraction. Each planned shard is disjoint and will be marked complete only after its artifact exists and its exact scope has been fully processed.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | inventory-001 | DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-33; DOC-003 PDF pp. 1-19; DOC-004 PDF p. 1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | Fresh PDF metadata, native text, layout text, and result-relevant render/OCR decisions for DOC-001 through DOC-004 | evidence_asset_inventory.md | COMPLETE |
| evidence_assets | assets-002 | Fresh direct-tool command log for DOC-001 through DOC-004 | preprocessing/extraction_log.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11 | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 provisional numeric relationships | relationships/parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 provisional statistical relationships | statistics/parts/main_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-33; DOC-003 PDF pp. 1-19; DOC-004 PDF p. 1 | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002, DOC-003, and DOC-004 provisional numeric relationships | relationships/parts/support_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 and DOC-003 provisional statistical relationships; DOC-004 documented no applicable statistical result | statistics/parts/support_statistical_relationships.md | COMPLETE |
| main_evidence_mapping | merge-001 | Canonical union of 62 mapped numeric/reporting relationships | relationships/numeric_relationship_inventory.md | COMPLETE |
| support_evidence_mapping | merge-002 | Canonical union of 39 mapped statistical relationships | statistics/relationship_inventory.md | COMPLETE |
| numeric_checks | numeric-001 | N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061, N062 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | statistics-001 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-001 | Matched occurrences across N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048, N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061, N062; S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039 | checkers/cross_source_consistency.md | COMPLETE |
| candidate_registration | candidates-001 | C001, C002, C003, C004, C005, C006, C007 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | C001, C002, C003, C004, C005, C006, C007 | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039; cross-lane ledger C001, C002, C003, C004, C005, C006, C007; all recheck facts | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | quality-001 | C001, C002, C003, C004, C005, C006, C007; every coverage row; every source-coverage row; both statistical pass execution records | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | C001, C002, C003, C004, C005, C006, C007 | report_generation.md | COMPLETE |
