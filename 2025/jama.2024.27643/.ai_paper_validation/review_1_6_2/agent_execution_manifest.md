# Agent execution manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper_1 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_2 | root/support_mapper_2 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_002.md |
| support_quantitative_mapper_shard_3 | root/support_mapper_3 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_003.md |
| support_quantitative_mapper_shard_4 | root/support_mapper_4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_004.md |
| support_quantitative_mapper_shard_5 | root/support_mapper_5 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_005.md |
| support_quantitative_mapper_shard_6 | root/support_mapper_6 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_006.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_plan_shard | root/statistical_pass_1_plan | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_plan.md |
| inclusion_screener | root/inclusion_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_plan_shard | root/statistical_pass_2_plan | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_plan.md |
| inclusion_screener_pass_2 | root/inclusion_screener_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_pass_2 | root/evidence_rechecker_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_pass_2.md |
| quality_control_auditor | root/quality_control_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Agent IDs use the tool-returned canonical runtime task names with the leading slash omitted to satisfy the bundled validator syntax. For example root/curator records the fresh runtime returned as /root/curator. Each spawned runtime has a distinct canonical name and exactly one manifest row. Named roles enforce the recorded model/effort pairs; no fallback, role promotion or provider change is used.
