# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_evidence_mapping | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_evidence_mapping | root/support_mapper_001 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_001.md |
| support_evidence_mapping | root/support_mapper_002 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_002.md |
| support_evidence_mapping | root/support_mapper_003 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_003.md |
| support_evidence_mapping | root/support_mapper_004 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_004.md |
| support_evidence_mapping | root/support_mapper_005 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_005.md |
| numeric_checks | root/numeric_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_checks | root/cross_source_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_recheck | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | limitations.md |
