# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_main_a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_continuation_main_b | root/numeric_main_b | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_main_b.md |
| numeric_continuation_support | root/numeric_support | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| cross_source_consistency_reviewer | root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_1_main_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support | root/statistics_1_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support.md |
| statistics_pass_1_main_b | root/statistics_1_main_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_main_b.md |
| statistics_pass_1_support_outcomes | root/statistics_1_outcomes | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support_outcomes.md |
| inclusion_screener | root/screen_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/recheck_initial | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_2_main_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_main_b | root/statistics_2_main_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_main_b_pass_2.md |
| statistics_pass_2_support | root/statistics_2_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support_pass_2.md |
| statistics_pass_2_support_outcomes | root/statistics_2_outcomes | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support_outcomes_pass_2.md |
| quality_control_auditor | root/audit_candidates | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_coverage_provenance_auditor | root/audit_coverage | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_provenance_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
