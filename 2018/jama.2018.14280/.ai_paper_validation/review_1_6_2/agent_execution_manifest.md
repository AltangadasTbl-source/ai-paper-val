# Agent execution manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass1_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support_a | root/statistics_pass1_support_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support_a.md |
| statistics_pass_1_support_b | root/statistics_pass1_support_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support_b.md |
| inclusion_screener | root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass2_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_support_a | root/statistics_pass2_support_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support_a.md |
| statistics_pass_2_support_b | root/statistics_pass2_support_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support_b.md |
| inclusion_screener_pass_2 | root/pass2_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_append_10 | root/append_rechecker_c010 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_C010.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime identifiers are the canonical task names exposed by the collaboration runtime. The table records each without its leading slash to satisfy the validator identifier syntax; for example root/statistics_pass1_main denotes runtime /root/statistics_pass1_main. No opaque UUID is exposed. Each mandatory stage and each optional context shard is a distinct fresh spawn. Canonical statistical artifacts are lossless coordinator merges of the named shard outputs listed in coverage_manifest.md.
