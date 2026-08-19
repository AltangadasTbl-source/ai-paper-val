# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper_doc002 | root/support_protocol_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc002.md |
| support_quantitative_mapper_doc003 | root/support_results_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003.md |
| support_quantitative_mapper | root/support_merge | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_rechecker_append | root/evidence_recheck_append | gpt-5.6-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_C021_C022.md |
| quality_control_auditor | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| evidence_rechecker_c023 | root/evidence_recheck_c023 | gpt-5.6-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_C023.md |
| evidence_rechecker_c024 | root/evidence_recheck_c024 | gpt-5.6-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_C024.md |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | limitations.md |
