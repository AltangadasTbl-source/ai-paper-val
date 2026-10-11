# Workflow 1.6 Agent Execution Manifest

All specialist agents use named presets and inherit the current provider as explicitly requested. Coordinator routing is recorded from the package configuration.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12868-d5ea-7421-847e-f4c4da8df21d | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | /root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | /root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | /root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_002 | /root/support_mapper_002 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_part_002.md |
| support_quantitative_mapper_shard_003 | /root/support_mapper_003 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_part_003.md |
| support_quantitative_mapper_shard_004 | /root/support_mapper_004 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_part_004.md |
| support_quantitative_mapper_shard_005 | /root/support_mapper_005 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_part_005.md |
| numeric_consistency_reviewer | /root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | /root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | /root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | /root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| evidence_rechecker_shard_002 | /root/evidence_rechecker_002 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck_part_002.md |
| statistics_pass_2 | /root/statistics_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | /root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | /root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
