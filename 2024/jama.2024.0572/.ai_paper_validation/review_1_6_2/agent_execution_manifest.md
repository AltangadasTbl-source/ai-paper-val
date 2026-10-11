# Agent execution manifest

Runtime IDs use the tool-returned canonical task names with the leading slash omitted for the manifest schema. Each name identifies its fresh runtime in this session. The coordinator identifier follows the required current-session convention.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_results_b | root/support_results_b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_parts/results_b_admin.md |
| support_quantitative_mapper_protocol | root/support_protocol | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_parts/protocol.md |
| support_quantitative_mapper_trial_a | root/support_trial_a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_parts/trial_sap_a.md |
| support_quantitative_mapper_trial_b | root/support_trial_b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_parts/trial_sap_b.md |
| numeric_consistency_reviewer | root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_plans | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/stat1_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_forest_a | root/stat1_forest_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_parts/pass1_forest_a.md |
| statistics_pass_1_forest_b | root/stat1_forest_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_parts/pass1_forest_b.md |
| statistics_pass_1_tables_a | root/stat1_tables_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_parts/pass1_tables_a.md |
| numeric_consistency_reviewer_results_a | root/numeric_results_a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_parts/results_a.md |
| cross_source_consistency_reviewer_reports | root/cross_reports | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_parts/reports.md |
| statistics_pass_1_tables_b_plan | root/stat1_tables_b_plan | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_parts/pass1_tables_b_plan.md |
| statistics_pass_1_remaining_a | root/stat1_remaining_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_parts/pass1_remaining_a.md |
| numeric_consistency_reviewer_results_b | root/numeric_results_b | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_parts/results_b.md |
| inclusion_screener | root/inclusion_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/stat2_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_forest_a | root/stat2_forest_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_parts/pass2_forest_a.md |
| statistics_pass_2_forest_b | root/stat2_forest_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_parts/pass2_forest_b.md |
| statistics_pass_2_remaining_a | root/stat2_remaining_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_parts/pass2_remaining_a.md |
| statistics_pass_2_tables_a | root/stat2_tables_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_parts/pass2_tables_a.md |
| statistics_pass_2_tables_b | root/stat2_tables_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_parts/pass2_tables_b.md |
| statistics_pass_2_plan_methods | root/stat2_plan_methods | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_parts/pass2_plan_methods.md |
| inclusion_screener_pass_2 | root/inclusion_pass2 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_appended_C019 | root/recheck_c019 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/appended_C019.md |
| quality_control_auditor | root/audit_a | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_candidates_b | root/audit_b | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/candidates_b.md |
| report_generator | root/report_a | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
| report_generator_candidates_b | root/report_b | gpt-6.1-sol | medium | FRESH_SPAWN | report/parts/cards_b.md |
