# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129ab-a588-7aa3-91e6-cbd30267412e | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/initial_inclusion_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| inclusion_screener_pass_2 | root/pass_2_inclusion_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_pass_2 | root/extension_evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck_pass_2.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Specialist runtime IDs are the unique canonical task identities returned by the collaboration runtime, with the initial slash omitted for validator syntax. These identify actual fresh spawned executions, rather than inferred process environment IDs.
