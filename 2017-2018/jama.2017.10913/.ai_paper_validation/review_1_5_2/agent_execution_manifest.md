# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| fresh_source_preprocessor | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper_protocol | root/support_protocol_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_protocol_quantitative_evidence.md |
| support_quantitative_mapper_results | root/support_results_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_results_quantitative_evidence.md |
| numeric_consistency_main_protocol | root/numeric_main_protocol | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/parts/numeric_main_protocol.md |
| numeric_consistency_support_results | root/numeric_support_results | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/parts/numeric_support_results.md |
| cross_source_checks | root/cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | root/quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation_summary.md |
