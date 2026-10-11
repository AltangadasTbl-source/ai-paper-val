# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_mapper_protocol_a | root/protocol_mapper_a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_001_032.md |
| support_mapper_protocol_b | root/protocol_mapper_b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_033_064.md |
| support_mapper_protocol_c | root/protocol_mapper_c | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_065_077.md |
| support_mapper_sap | root/sap_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap_001_029.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_checker_estimates | root/numeric_estimates_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_estimates.md |
| cross_source_consistency_reviewer | root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_reports | root/statistics_pass_1_reports | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_reports.md |
| statistics_pass_1_plans | root/statistics_pass_1_plans | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_plans.md |
| statistics_pass_1_raw | root/statistics_pass_1_raw | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_raw.md |
| inclusion_screener | root/inclusion_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
