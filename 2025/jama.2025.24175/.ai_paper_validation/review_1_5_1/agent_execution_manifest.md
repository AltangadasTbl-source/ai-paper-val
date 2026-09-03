# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_inventory | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapper | root/map_main | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper_doc002_pp001_032 | root/map_doc2_a | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/doc002_pp001_032.md |
| support_quantitative_mapper_doc002_pp033_064 | root/map_doc2_b | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/doc002_pp033_064.md |
| support_quantitative_mapper_doc002_pp065_072 | root/map_doc2_c | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/doc002_pp065_072.md |
| support_quantitative_mapper_doc003 | root/map_doc3 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/doc003_pp001_054.md |
| support_quantitative_mapper_doc004_005 | root/map_doc45 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/doc004_005.md |
| mapping_consolidation | root/mapping_consolidation | gpt-5.6-terra | medium | FRESH_SPAWN | relationships/numeric_relationship_inventory.md |
| numeric_checks | root/numeric_checks | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_checks | root/cross_source_checks | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| candidate_registration | root/candidate_registration | gpt-5.6-terra | medium | FRESH_SPAWN | candidate_ledger.md |
| evidence_recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | root/evidence_quality | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | root/report_generation | gpt-5.6-terra | medium | FRESH_SPAWN | parts/report_generation_record.md |
