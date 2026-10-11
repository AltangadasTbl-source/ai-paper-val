# Workflow 1.6 Agent Execution Manifest
Runtime IDs are actual collaboration canonical task paths with the leading slash omitted for the validator identifier grammar. The interface exposes task paths rather than UUIDs.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_recheck_append_001 | root/recheck_append_001 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_append_001.md |
| support_quantitative_mapper_visual_repair | root/support_visual_repair | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_p26_visual_repair.md |
| numeric_consistency_reviewer_visual_repair | root/numeric_visual_repair | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_visual_repair.md |
| evidence_recheck_append_002 | root/recheck_append_002 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_append_002.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
