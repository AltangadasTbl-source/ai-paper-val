# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapper | main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_protocol_1_mapper | support_protocol_1 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_protocol_pp01-32.md |
| support_protocol_2_mapper | support_protocol_2 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_protocol_pp33-40.md |
| support_sap_mapper | support_sap | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_sap_pp01-31.md |
| support_results_1_mapper | support_results_1 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_results_supp_pp01-32.md |
| support_results_2_mapper | support_results_2 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_results_supp_pp33-34.md |
| numeric_consistency_reviewer | numeric_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | cross_source_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality_auditor | quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation.md |
