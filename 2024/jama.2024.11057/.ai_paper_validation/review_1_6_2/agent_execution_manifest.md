# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/inclusion_screen_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime IDs are canonical task names returned by the collaboration runtime, with the leading slash omitted to meet validator syntax. Each root/name represents returned /root/name; root represents the current /root coordinator. The spawn interface supplies no hidden UUID.
