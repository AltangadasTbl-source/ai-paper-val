# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| statistics_pass_1_repair | root/statistics_pass_1_repair | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1_repair.md |
| cross_source_repair | root/cross_source_repair | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency_repair.md |
| statistics_pass_2_repair | root/statistics_pass_2_repair | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2_repair.md |
| quality_control_auditor_final | root/quality_auditor_final | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit_final.md |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation_record.md |
