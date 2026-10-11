# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curation | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapping | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapping | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_2 | root/support_appendix_mapping | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_appendix.md |
| numeric_consistency_reviewer | root/numeric_main_review | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_support_shard | root/numeric_support_review | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| cross_source_consistency_reviewer | root/cross_source_review | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_one | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/initial_inclusion_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_two | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_inclusion_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_coverage_shard | root/quality_coverage_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_process_audit.md |
| report_generator | root/report_generation | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime agent IDs are the collaboration service's unique canonical task names, with the leading slash omitted to satisfy the artifact ID syntax. They refer to the same runtime agents returned by spawn_agent and list_agents; no separate UUID is exposed by this session.
