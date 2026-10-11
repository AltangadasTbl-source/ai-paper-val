# Workflow 1.6 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_reviewer | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_reviewer | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support | root/statistics_pass_1_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2_main_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_main_b | root/statistics_pass_2_main_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_main_b.md |
| statistics_pass_2_support | root/statistics_pass_2_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support.md |
| quality_support_coverage_auditor | root/quality_support_coverage | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/support_relationship_coverage_audit.md |
| quality_main_coverage_auditor | root/quality_main_coverage | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/main_relationship_coverage_audit.md |
| quality_control_auditor | root/quality_control_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime identifiers are the collaboration tool's actual canonical task names with only the leading `/` omitted to satisfy the validator's alphanumeric-first syntax. Thus root is coordinator `/root`, and root/asset_curator is `/root/asset_curator`. This runtime exposes canonical task IDs rather than separate UUIDs. All mandatory specialists use their installed named custom preset with fixed model/effort; no agent is reused for another mandatory stage or promoted through follow-up. The user's current-provider override applies throughout.
