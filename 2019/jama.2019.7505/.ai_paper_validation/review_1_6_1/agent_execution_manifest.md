# Agent execution manifest

The `runtime:` prefix labels the exact canonical runtime name returned by the collaboration API; `runtime:/root/main_mapper` identifies `/root/main_mapper`. This serialization preserves the complete returned name. Named presets set all specialist model/effort pairs directly. Every stage uses a distinct fresh agent. Support mapping has two disjoint shards; the coordinator merges their complete artifacts into the canonical support map.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | runtime:/root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | runtime:/root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | runtime:/root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | runtime:/root/support_plan_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_results_shard | runtime:/root/support_results_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_results_evidence.md |
| numeric_consistency_reviewer | runtime:/root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | runtime:/root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | runtime:/root/statistical_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | runtime:/root/inclusion_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | runtime:/root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | runtime:/root/statistical_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor_statistical_main_shard | runtime:/root/audit_main_statistical_coverage | gpt-6.1-sol | high | FRESH_SPAWN | quality/statistical_main_coverage_audit.md |
| quality_control_auditor_statistical_support_shard | runtime:/root/audit_support_statistical_coverage | gpt-6.1-sol | high | FRESH_SPAWN | quality/statistical_support_coverage_audit.md |
| quality_control_auditor | runtime:/root/quality_control_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | runtime:/root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
