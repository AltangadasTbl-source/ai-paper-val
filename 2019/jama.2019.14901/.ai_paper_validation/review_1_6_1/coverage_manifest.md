# Workflow 1.6.1 Coverage Manifest

Each mapping scope is disjoint and exhaustive. Subsequent relationship and candidate scopes will be enumerated after discovery; no count target controls selection.

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | sources-all | DOC-001 pp.1-11; DOC-002 pp.1-48; DOC-003 pp.1-9; DOC-004 p.1 | source_inventory.md | COMPLETE |
| evidence_assets | assets-all | 128 eligible reusable evidence/provenance assets; all 69 pages assessed | evidence_asset_inventory.md | COMPLETE |
| main_evidence_mapping | main-all | DOC-001 pp.1-11, all reusable-backed | extraction/main_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-all | DOC-002 pp.1-48; DOC-003 pp.1-9; DOC-004 p.1; DOC-002 p.42 fresh-required | extraction/support_quantitative_evidence.md | COMPLETE |
| numeric_checks | numeric-all | N001 through N118; every mapped value in M-N001 through M-N097 and U-N001 through U-N021 | checkers/numeric_consistency.md | COMPLETE |
| statistics_pass_1 | stats-first | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049 | checkers/statistical_pass_1.md | COMPLETE |
| cross_source_checks | cross-all | All 69 pages and every mapped report-result and applicable report-plan or plan-internal design comparison | checkers/cross_source_consistency.md | COMPLETE |
| inclusion_screening | screen-initial | All 12 initial checker findings; 10 included rows consolidated to C001, C002, C003, C004, C005; two excluded findings | screening/inclusion_screen.md | COMPLETE |
| candidate_registration | ledger-all | C001, C002, C003, C004, C005 | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-all | C001, C002, C003, C004, C005; every affected source location | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | stats-second | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049 | checkers/statistical_pass_2.md | COMPLETE |
| evidence_quality | audit-all | C001, C002, C003, C004, C005; all 12 screening decisions and all 71 checker excluded observations | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-all | C001, C002, C003, C004, C005; complete report sections and metadata | ../final_report_1_6_1.md | COMPLETE |
| support_evidence_mapping | support-p42-layout | DOC-002 p.42 fresh direct layout extraction | preprocessing/support/protocol-p42-layout.txt | COMPLETE |
| support_evidence_mapping | support-p42-render | DOC-002 p.42 fresh direct rendering and full visual inspection | preprocessing/support/protocol-p42.png | COMPLETE |
| support_evidence_mapping | support-p42-ocr | DOC-002 p.42 targeted CPU OCR with visual transcription precedence | preprocessing/support/protocol-p42-ocr.txt | COMPLETE |
| numeric_checks | numeric-inventory | N001 through N118; complete source-linked row crosswalk and calculations | relationships/numeric_relationship_inventory.md | COMPLETE |
| cross_source_checks | source-confirm-main-p1 | Exact supplied page main-p1 directly rendered and visually read; source mapping in checker | preprocessing/cross_source/main-p1.png | COMPLETE |
| cross_source_checks | source-confirm-main-p4 | Exact supplied page main-p4 directly rendered and visually read; source mapping in checker | preprocessing/cross_source/main-p4.png | COMPLETE |
| cross_source_checks | source-confirm-main-p6 | Exact supplied page main-p6 directly rendered and visually read; source mapping in checker | preprocessing/cross_source/main-p6.png | COMPLETE |
| cross_source_checks | source-confirm-main-p8 | Exact supplied page main-p8 directly rendered and visually read; source mapping in checker | preprocessing/cross_source/main-p8.png | COMPLETE |
| cross_source_checks | source-confirm-protocol-p31 | Exact supplied page protocol-p31 directly rendered and visually read; source mapping in checker | preprocessing/cross_source/protocol-p31.png | COMPLETE |
| cross_source_checks | source-confirm-protocol-p33 | Exact supplied page protocol-p33 directly rendered and visually read; source mapping in checker | preprocessing/cross_source/protocol-p33.png | COMPLETE |
| cross_source_checks | source-confirm-protocol-p34 | Exact supplied page protocol-p34 directly rendered and visually read; source mapping in checker | preprocessing/cross_source/protocol-p34.png | COMPLETE |
| cross_source_checks | source-confirm-results-p2 | Exact supplied page results-p2 directly rendered and visually read; source mapping in checker | preprocessing/cross_source/results-p2.png | COMPLETE |
| statistics_pass_1 | stats-inventory | S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049 | statistics/relationship_inventory.md | COMPLETE |
| statistics_pass_1 | stats-source-main-p01.txt | Exact supplied page(s) main-p01.txt; source/engine mapping in statistical inventory | preprocessing/statistics_pass1/main-p01.txt | COMPLETE |
| statistics_pass_1 | stats-source-main-p04.txt | Exact supplied page(s) main-p04.txt; source/engine mapping in statistical inventory | preprocessing/statistics_pass1/main-p04.txt | COMPLETE |
| statistics_pass_1 | stats-source-plan-p33-p34.txt | Exact supplied page(s) plan-p33-p34.txt; source/engine mapping in statistical inventory | preprocessing/statistics_pass1/plan-p33-p34.txt | COMPLETE |
| statistics_pass_1 | stats-source-results-p02.txt | Exact supplied page(s) results-p02.txt; source/engine mapping in statistical inventory | preprocessing/statistics_pass1/results-p02.txt | COMPLETE |
| statistics_pass_1 | stats-source-results-p06-p07.txt | Exact supplied page(s) results-p06-p07.txt; source/engine mapping in statistical inventory | preprocessing/statistics_pass1/results-p06-p07.txt | COMPLETE |
| statistics_pass_1 | stats-source-results-p07.png | Exact supplied page(s) results-p07.png; source/engine mapping in statistical inventory | preprocessing/statistics_pass1/results-p07.png | COMPLETE |
| evidence_recheck | recheck-source-data-sharing-p1-layout.txt | No assigned candidate IDs; DOC-004 p.1 administrative confirmation | preprocessing/evidence_recheck/data-sharing-p1-layout.txt | COMPLETE |
| evidence_recheck | recheck-source-main-all-layout.txt | C001, C002, C003, C004, C005; exact page(s) main-all-layout.txt, crosswalk in recheck | preprocessing/evidence_recheck/main-all-layout.txt | COMPLETE |
| evidence_recheck | recheck-source-main-p7.png | C003, C004; DOC-001 p.7 exact source rendering | preprocessing/evidence_recheck/main-p7.png | COMPLETE |
| evidence_recheck | recheck-source-protocol-p30-p34-layout.txt | C002, C003, C004; DOC-002 pp.30-34 source confirmation | preprocessing/evidence_recheck/protocol-p30-p34-layout.txt | COMPLETE |
| evidence_recheck | recheck-source-protocol-p30.png | C002; DOC-002 p.30 exact source rendering | preprocessing/evidence_recheck/protocol-p30.png | COMPLETE |
| evidence_recheck | recheck-source-results-all-layout.txt | C001, C002, C003, C004, C005; exact page(s) results-all-layout.txt, crosswalk in recheck | preprocessing/evidence_recheck/results-all-layout.txt | COMPLETE |
| evidence_recheck | recheck-source-results-p6.png | C001, C004; DOC-003 p.6 exact source rendering | preprocessing/evidence_recheck/results-p6.png | COMPLETE |
| evidence_recheck | recheck-source-results-p9.png | C003; DOC-003 p.9 exact source rendering | preprocessing/evidence_recheck/results-p9.png | COMPLETE |
| evidence_quality | quality-coverage | No assigned candidate IDs; all 69 source units, 128 reused assets, extraction maps and relationship-coverage/provenance records | quality/coverage_integrity_audit.md | COMPLETE |
| report_generation | report-limitations | C001, C002, C003, C004, C005; complete package and candidate limitations | limitations.md | COMPLETE |
