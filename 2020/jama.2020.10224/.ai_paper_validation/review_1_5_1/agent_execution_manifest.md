# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curation | root/reuse_asset_curation | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_evidence_mapping | root/main_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/main_doc001.md |
| support_evidence_mapping | root/support_mapping_doc002 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc002.md |
| support_evidence_mapping | root/support_mapping_doc003a | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003_p01_p24.md |
| support_evidence_mapping | root/support_mapping_doc003b_doc004 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003_p25_p48_doc004.md |
| numeric_checks | root/numeric_review | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_checks | root/cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | root/evidence_quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | root/report_generation | gpt-5.6-terra | medium | FRESH_SPAWN | limitations.md |
