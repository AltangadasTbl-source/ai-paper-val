# Workflow 1.6.2 Agent Execution Manifest
| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a1294f-634f-7bb3-a0ec-5f572bfe674e | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_figures_a | root/support_figures_a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_figures_a.md |
| support_quantitative_mapper_figures_b | root/support_figures_b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_figures_b.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_coverage_auditor | root/coverage_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_audit.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| inclusion_screener_pass_2 | root/pass_2_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_pass_2 | root/pass_2_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_pass_2.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime task IDs are returned by collaboration.spawn_agent as canonical names beginning with /root/. Specialist Agent ID cells encode the exact canonical runtime identifier with its leading slash removed, because the validator requires an alphanumeric first character. Prefixing each specialist ID with / recovers its exact runtime task identifier. The coordinator ID is its session UUID.
