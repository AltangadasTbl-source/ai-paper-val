# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| fresh_source_preprocessing | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapping | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapping_a | root/support_mapper_a | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_a_quantitative_evidence.md |
| support_quantitative_mapping_b | root/support_mapper_b | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_b_quantitative_evidence.md |
| numeric_checks | root/numeric_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_checks | root/cross_source_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_recheck | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| evidence_quality_repair | root/quality_audit_repair | gpt-5.6-sol | high | FRESH_SPAWN | limitations.md |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation.md |

Every review agent is listed exactly once. Runtime usage is recorded separately in `token_usage_ledger.csv` after Markdown assembly.
