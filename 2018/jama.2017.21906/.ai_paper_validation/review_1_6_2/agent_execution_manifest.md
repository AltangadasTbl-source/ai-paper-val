# Workflow 1.6.2 Agent Execution Manifest

Runtime identifier representation: the collaboration API exposes canonical runtime task names rather than opaque thread IDs. Each Agent ID cell uses `task:` followed by the exact returned canonical name, including its leading slash; the prefix identifies the transport namespace and satisfies the validator's alphanumeric-first ID syntax. `task:/root` denotes the current coordinator. Distinct returned canonical names remain distinct fresh runtime agents; no thread identifier was invented. Each actual runtime has exactly one execution row.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | task:/root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | task:/root/reuse_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | task:/root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | task:/root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | task:/root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | task:/root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | task:/root/stat1_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support_shard | task:/root/stat1_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support.md |
| inclusion_screener | task:/root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | task:/root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | task:/root/stat2_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_support_shard | task:/root/stat2_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support.md |
| inclusion_screener_pass_2 | task:/root/pass2_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_appended | task:/root/appended_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck_appended.md |
| quality_control_auditor | task:/root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | task:/root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
