# Agent execution manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_plan_1 | root/plan_mapper_1 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/plan_pages_001_032.md |
| support_quantitative_mapper_plan_2 | root/plan_mapper_2 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/plan_pages_033_064.md |
| support_quantitative_mapper_plan_3 | root/plan_mapper_3 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/plan_pages_065_072.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/inclusion_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| evidence_rechecker_results_shard | root/evidence_recheck_results | gpt-6.1-sol | high | FRESH_SPAWN | verification/results_candidates_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_results_cards_shard | root/report_results_cards | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/candidate_cards_008_014.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
