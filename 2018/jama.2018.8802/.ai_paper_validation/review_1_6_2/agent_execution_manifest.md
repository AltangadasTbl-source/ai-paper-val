# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_map | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_map | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/stat1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| numeric_consistency_tail | root/numeric_tail | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_tail.md |
| inclusion_screener | root/screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/stat2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| inclusion_screener_pass_2 | root/screen2 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_appended | root/recheck5 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_appended.md |
| quality_control_auditor | root/audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime IDs use the collaboration task path with its leading slash omitted; root/screen corresponds to /root/screen. Each path identifies a distinct fresh runtime. The coordinator is the current interactive session.
