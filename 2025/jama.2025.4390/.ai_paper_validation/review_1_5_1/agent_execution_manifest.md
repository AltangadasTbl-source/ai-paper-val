# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curation | task:/root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_evidence_mapping | task:/root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_evidence_mapping | task:/root/support_protocol_sap_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_protocol_sap.md |
| support_evidence_mapping | task:/root/support_results_a_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_results_001_024.md |
| support_evidence_mapping | task:/root/support_results_b_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_results_025_049.md |
| numeric_checks | task:/root/numeric_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_checks | task:/root/cross_source_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | task:/root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_recheck | task:/root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | task:/root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | task:/root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | task:/root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | limitations.md |
