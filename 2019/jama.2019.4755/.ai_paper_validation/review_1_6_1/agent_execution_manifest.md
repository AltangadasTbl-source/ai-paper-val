# Workflow 1.6.1 Agent Execution Manifest
 
| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a128d8-ef89-7251-8e09-114b0845654c | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/protocol_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_other_shard | root/other_support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_other.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/inclusion_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor_mapping_numeric_shard | root/audit_mapping_numeric | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/mapping_numeric_audit.md |
| quality_control_auditor_cross_source_shard | root/audit_cross_screening | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/cross_source_screening_audit.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Specialist runtime IDs are the distinct canonical names returned by the collaboration runtime, recorded without the leading slash for manifest token syntax. The current coordinator uses its session UUID. Every actual review runtime is listed exactly once; all mandatory specialists were fresh spawns under their named fixed presets. The optional support shard and two optional quality shards retain their role's required effort.
