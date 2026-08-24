# Coverage Manifest

| Stage | Shard ID | Exact scope | Artifact | Status |
|---|---|---|---|---|
| source_inventory | source-001 | DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-37; DOC-003 PDF pp. 1-7; DOC-004 PDF pp. 1-14 | source_inventory.md | COMPLETE |
| evidence_assets | assets-001 | DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-37; DOC-003 PDF pp. 1-7; DOC-004 PDF pp. 1-14 | evidence_asset_inventory.md | COMPLETE |
| evidence_assets | assets-002 | Fresh per-page preprocessing status for all 69 PDF pages | preprocessing/tool_and_page_status.md | COMPLETE |
| main_evidence_mapping | main-001 | DOC-001 PDF pp. 1-11 | extraction/main_quantitative_evidence.md | COMPLETE |
| main_evidence_mapping | main-002 | DOC-001 PDF pp. 1-11 numeric relationship part | relationships/parts/main_numeric_relationships.md | COMPLETE |
| main_evidence_mapping | main-003 | DOC-001 PDF pp. 1-11 statistical relationship part | statistics/parts/main_statistical_relationships.md | COMPLETE |
| support_evidence_mapping | support-001 | DOC-002 PDF pp. 1-37; DOC-003 PDF pp. 1-7; DOC-004 PDF pp. 1-14 | extraction/support_quantitative_evidence.md | COMPLETE |
| support_evidence_mapping | support-002 | DOC-002 PDF pp. 1-37; DOC-003 PDF pp. 1-7; DOC-004 PDF pp. 1-14 numeric relationship part | relationships/parts/support_numeric_relationships.md | COMPLETE |
| support_evidence_mapping | support-003 | DOC-002 PDF pp. 1-37; DOC-003 PDF pp. 1-7; DOC-004 PDF pp. 1-14 statistical relationship part | statistics/parts/support_statistical_relationships.md | COMPLETE |
| numeric_checks | numeric-001 | Complete empty N set after all 69 source pages were mapped under source-access limitation | checkers/numeric_consistency.md | COMPLETE |
| numeric_checks | numeric-002 | Complete empty numeric candidate part | checkers/candidate_parts/numeric_candidates.md | COMPLETE |
| statistics_pass_1 | statistics-001 | Complete empty S set after all 69 source pages were mapped under source-access limitation | checkers/statistical_pass_1.md | COMPLETE |
| statistics_pass_1 | statistics-001-candidates | Complete empty statistical pass-1 candidate part | checkers/candidate_parts/statistical_pass_1_candidates.md | COMPLETE |
| cross_source_checks | cross-001 | Complete empty matched-result set across DOC-001, DOC-002, DOC-003, and DOC-004 | checkers/cross_source_consistency.md | COMPLETE |
| cross_source_checks | cross-002 | Complete empty cross-source candidate part | checkers/candidate_parts/cross_source_candidates.md | COMPLETE |
| candidate_registration | candidates-001 | Empty stable candidate set; no C identifiers | candidate_ledger.md | COMPLETE |
| evidence_recheck | recheck-001 | Empty stable candidate set; no C identifiers; 0 of 0 mechanically rechecked | verification/evidence_recheck.md | COMPLETE |
| statistics_pass_2 | statistics-002 | Complete empty S set plus empty stable candidate ledger and 0-of-0 recheck facts | checkers/statistical_pass_2.md | COMPLETE |
| statistics_pass_2 | statistics-002-candidates | Complete empty statistical pass-2 new-candidate part | checkers/candidate_parts/statistical_pass_2_new_candidates.md | COMPLETE |
| evidence_quality | quality-001 | Empty stable candidate set; no C identifiers; every coverage row, all four source rows, and both statistical executions | quality/evidence_quality_audit.md | COMPLETE |
| report_generation | report-001 | Empty stable candidate set; no C identifiers; complete review narrative and finalized metadata | ../final_report_1_5_2.md | COMPLETE |
| report_generation | report-002 | Report assembly provenance for empty stable candidate set and all required sections | report_generation/report_generation_record.md | COMPLETE |
