# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | runtime:/root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | runtime:/root/main_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | runtime:/root/support_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | runtime:/root/numeric_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | runtime:/root/cross_source_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | runtime:/root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | runtime:/root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | runtime:/root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_recheck_repair_c006 | runtime:/root/evidence_recheck_c006 | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck_C006.md |
| quality_control_auditor | runtime:/root/quality_control_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | runtime:/root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | limitations.md |

Every mandatory specialist is appended exactly once after fresh spawn. Runtime token metadata is not exposed to this coordinator interface; the final ledger will record `UNAVAILABLE` without estimation unless authoritative counts become available.
