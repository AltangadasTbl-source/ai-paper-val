# Workflow 1.6 Agent Execution Manifest

Model/effort pairs are the package coordinator contract and tool-defined named specialist presets. Runtime coordinator model attestation is unavailable. The current provider is retained by explicit user instruction.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | task:/root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | task:/root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | task:/root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | task:/root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | task:/root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_support_shard | task:/root/numeric_support | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| statistics_pass_1 | task:/root/statistics_one | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_consistency_reviewer | task:/root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| evidence_rechecker | task:/root/rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | task:/root/statistics_two | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| coverage_quality_support | task:/root/coverage_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_audit.md |
| quality_control_auditor | task:/root/final_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | task:/root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime IDs use the task: namespace followed by the exact canonical task identifier returned by the collaboration tool (for example task:/root/statistics_one). The tool exposes canonical task identifiers rather than opaque numeric runtime IDs. Each corresponds to one actual fresh spawn; no identifier is invented or reused.
