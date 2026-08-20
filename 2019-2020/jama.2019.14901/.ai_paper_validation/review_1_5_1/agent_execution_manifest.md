# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curation | root/reuse_asset_curation | gpt-5.6-terra | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapping | root/main_quantitative_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapping | root/support_quantitative_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_review | root/numeric_consistency_review | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_review | root/cross_source_consistency_review | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality_audit | root/evidence_quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | root/report_generation | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation_handoff.md |

Spawned-agent IDs use the validator-safe canonical task form without the orchestration display's leading slash; each maps one-to-one to the `/root/...` runtime identity reported at spawn.
