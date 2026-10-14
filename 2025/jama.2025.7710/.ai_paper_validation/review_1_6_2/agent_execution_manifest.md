# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12bb5-8314-7543-b42e-d51a4b546cc9 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | agent:/root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | agent:/root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | agent:/root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | agent:/root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_support_shard | agent:/root/numeric_support | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| statistics_pass_1 | agent:/root/statistics_one_main_plan | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support_shard | agent:/root/statistics_one_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support_pass_1.md |
| cross_source_consistency_reviewer | agent:/root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| inclusion_screener | agent:/root/inclusion_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | agent:/root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | agent:/root/statistics_two_main_plan | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_support_shard | agent:/root/statistics_two_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support_pass_2.md |
| quality_control_auditor | agent:/root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | agent:/root/report_assembly | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
