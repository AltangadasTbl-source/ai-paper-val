# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| fresh_source_preprocessor | root:fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapper | root:main_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root:support_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root:numeric_review | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root:cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root:statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | root:evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root:statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root:quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root:report_generation | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation.md |
