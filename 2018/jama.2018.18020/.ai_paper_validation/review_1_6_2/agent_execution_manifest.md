# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_plan_a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_mapper_plan_b | root/support_plan_b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_b.md |
| support_mapper_results | root/support_results | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_results.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_plan_shard | root/statistical_pass_1_plan | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_plan.md |
| inclusion_screener | root/inclusion_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_plan_shard | root/statistical_pass_2_plan | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_plan.md |
| inclusion_screener_pass_2 | root/inclusion_screen_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_append | root/evidence_recheck_append | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_C022.md |
| quality_control_auditor | root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
