# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION-20261014 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| aborted_reuse_asset_curator | root/curator_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/curator_20261014_aborted.md |
| aborted_main_mapping | root/main_mapper_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/main_mapper_20261014_aborted.md |
| aborted_support_mapping | root/support_mapper_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/support_mapper_20261014_aborted.md |
| aborted_protocol_a_mapping | root/protocol_a_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/protocol_a_20261014_aborted.md |
| aborted_protocol_b_mapping | root/protocol_b_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/protocol_b_20261014_aborted.md |
| aborted_protocol_c_mapping | root/protocol_c_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/protocol_c_20261014_aborted.md |
| aborted_sap_mapping | root/sap_mapper_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/sap_mapper_20261014_aborted.md |
| reuse_asset_curator | root/curator_restart | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_mapper_protocol_a | root/protocol_a_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_001_032_restart.md |
| support_mapper_protocol_b | root/protocol_b_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_033_064_restart.md |
| support_mapper_protocol_c | root/protocol_c_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_065_077_restart.md |
| support_mapper_sap | root/sap_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap_001_029_restart.md |
| numeric_consistency_reviewer | root/numeric_review | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_review | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/stat1_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_reports | root/stat1_reports | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat1_reports.md |
| statistics_pass_1_plans | root/stat1_plans | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat1_plans.md |
| statistics_pass_1_raw | root/stat1_raw | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat1_raw.md |
| inclusion_screener | root/initial_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/stat2_main_early | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_main_late | root/stat2_main_late | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_main_late.md |
| statistics_pass_2_reports_early | root/stat2_reports_early | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_reports_early.md |
| statistics_pass_2_reports_late | root/stat2_reports_late | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_reports_late.md |
| statistics_pass_2_plans | root/stat2_plans | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_plans.md |
| statistics_pass_2_raw | root/stat2_raw | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_raw.md |
| inclusion_screener_pass_2 | root/pass2_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_appended | root/recheck_c018 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/append_C018.md |
| statistics_pass_2_plan_a_repair | root/stat2_plan_a_repair | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_plan_a_repair.md |
| statistics_pass_2_plan_b_repair | root/stat2_plan_b_repair | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_plan_b_repair.md |
| statistics_pass_2_plan_c_repair | root/stat2_plan_c_repair | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_plan_c_repair.md |
| quality_audit_main_early | root/qa_main_early | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_main_early.md |
| quality_audit_main_late | root/qa_main_late | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_main_late.md |
| quality_audit_workbook_numeric | root/qa_workbook_numeric | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_workbook_numeric.md |
| quality_audit_reports_early | root/qa_reports_early | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_reports_early.md |
| quality_audit_reports_late | root/qa_reports_late | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_reports_late.md |
| quality_audit_protocol | root/qa_protocol | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_protocol.md |
| quality_audit_sap | root/qa_sap | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_sap.md |
| quality_control_auditor | root/final_candidate_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_complete | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime identifiers are the exact tool-returned canonical task names with the leading root separator omitted in the table so that the bundled validator accepts their syntax. execution/runtime_identifiers.json preserves every literal tool name. Coordinator table alias maps to /root current session. No runtime/model identity is substituted.
