# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_mapping_protocol_1 | root/protocol_mapper_1 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_protocol_001.md |
| support_mapping_protocol_2 | root/protocol_mapper_2 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_protocol_002.md |
| support_mapping_protocol_3 | root/protocol_mapper_3 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_protocol_003.md |
| support_mapping_sap | root/sap_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_sap.md |
| support_mapping_protocol_4 | root/protocol_mapper_4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_protocol_004.md |
| numeric_consistency_reviewer | root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_support_shard | root/numeric_support | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_support_part.md |
| cross_source_consistency_reviewer | root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| cross_plan_internal_shard | root/cross_plan | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_plan_part.md |
| statistics_pass_1 | root/statistics_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
