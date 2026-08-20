# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_evidence_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/main_doc001.md |
| support_evidence_mapper_doc002 | root/support_mapper_doc002 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc002.md |
| support_evidence_mapper_doc003 | root/support_mapper_doc003 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003.md |
| support_evidence_mapper_doc004_005 | root/support_mapper_doc004_005 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc004_doc005.md |
| numeric_checks | root/numeric_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_checks | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_recheck | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | limitations.md |
