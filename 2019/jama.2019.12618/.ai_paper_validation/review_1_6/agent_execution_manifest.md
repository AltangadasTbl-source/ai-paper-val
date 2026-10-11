# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |

All agents use the current provider; user instruction overrides the package's OpenRouter-specific template. Named runtime presets establish specialist model and effort.

| reuse_asset_curator | root/reuse_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |

Runtime specialist IDs are the canonical task identifiers returned by the collaboration service, with the leading slash removed only to satisfy the bundled validator's identifier syntax. For example, `root/reuse_curator` records runtime `/root/reuse_curator`. The service exposes canonical task IDs, not additional UUIDs.

| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_protocol_early_shard | root/protocol_early_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/protocol_001_032.md |
| support_protocol_middle_shard | root/protocol_middle_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/protocol_065_096.md |
| support_sap_early_shard | root/sap_early_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/sap_001_032.md |
| support_plan_tail_shard | root/plan_tail_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/protocol_129_153.md |
| numeric_consistency_reviewer | root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_results_shard | root/numeric_results | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_results.md |
| numeric_protocol_shard | root/numeric_protocol | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_protocol.md |
| numeric_plan_tail_shard | root/numeric_plan_tail | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_plan_tail.md |
| statistics_pass_1 | root/statistics_pass1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_consistency_reviewer | root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| evidence_rechecker | root/recheck_report | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| evidence_recheck_plan_shard | root/recheck_plans | gpt-6.1-sol | high | FRESH_SPAWN | verification/recheck_plan_part.md |
| evidence_recheck_cross_stat_shard | root/recheck_cross_stats | gpt-6.1-sol | high | FRESH_SPAWN | verification/recheck_cross_stats_part.md |
| statistics_pass_2 | root/statistics_pass2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
