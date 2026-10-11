# Agent execution manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_protocol_shard | root/protocol_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_protocol.md |
| numeric_consistency_reviewer | root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_support_shard | root/numeric_support | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| statistics_pass_1 | root/stat1_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support_a_shard | root/stat1_support_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support_a.md |
| statistics_pass_1_support_b_shard | root/stat1_support_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support_b.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| inclusion_screener | root/inclusion_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/stat2_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_support_a_shard | root/stat2_support_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support_a.md |
| statistics_pass_2_support_b_shard | root/stat2_support_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support_b.md |
| inclusion_screener_pass_2 | root/inclusion_pass2 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| quality_control_auditor_statistical_shard | root/audit_statistics | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/statistical_results.md |
| evidence_rechecker_pass_2_extension | root/recheck_pass2_extension | gpt-6.1-sol | high | FRESH_SPAWN | verification/pass_2_extension_C005.md |
| quality_control_auditor | root/audit_main | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime IDs use canonical task names without the leading slash; root/curator identifies /root/curator in this session's collaboration runtime.
