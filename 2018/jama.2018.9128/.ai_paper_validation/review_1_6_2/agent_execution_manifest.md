# Agent Execution Manifest

Runtime IDs are unique collaboration-tool canonical identities with the leading slash omitted; the coordinator uses its session UUID. Each mandatory stage is a separate fresh spawn.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129af-50e5-7bc0-98b0-ca3e986836d2 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_late | root/support_mapper_late | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_late_plan.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| numeric_consistency_reviewer_support | root/numeric_support_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| inclusion_screener | root/inclusion_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_stats_count | root/quality_audit_stats_count | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/candidate_stats_count_audit.md |
| quality_control_auditor_main_map | root/quality_audit_main_map | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/main_mapping_audit.md |
| quality_control_auditor_support_map | root/quality_audit_support_map | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/support_mapping_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
