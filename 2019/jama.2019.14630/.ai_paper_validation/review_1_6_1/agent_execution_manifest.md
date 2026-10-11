# Workflow 1.6.1 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |

Agent IDs use the canonical runtime task names returned by the collaboration service, normalized by omitting the leading slash to meet the validator's identifier syntax. They identify distinct actual agents, not synthetic placeholders. The service does not expose an additional UUID. Coordinator configuration source is the package config, per workflow settings.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/protocol_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_results_shard | root/sap_results_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_sap_results_part.md |
| numeric_consistency_reviewer | root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_support_a | root/numeric_support_a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support_a.md |
| numeric_support_b | root/numeric_support_b | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support_b.md |
| statistics_pass_1 | root/statistics_one_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support_a | root/statistics_one_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support_a.md |
| statistics_pass_1_support_b | root/statistics_one_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support_b.md |
| cross_source_consistency_reviewer | root/cross_plan | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| cross_source_report_shard | root/cross_report | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/cross_source_report.md |
| inclusion_screener | root/inclusion_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_two_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_support_a | root/statistics_two_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support_a.md |
| statistics_pass_2_support_b | root/statistics_two_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support_b.md |
| quality_control_auditor | root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
