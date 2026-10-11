# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129ae-36a4-7dd1-b706-3785463a1417 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a129af-e908-7e73-af17-8c17952112f3 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a129b2-4e97-7b71-ba67-2a7339b3fab3 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a129b2-7db6-7d30-acec-7d2915ec00eb | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_2 | 01a129b2-a1ff-7160-83f9-947c4281ad93 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_002.md |
| support_quantitative_mapper_shard_3 | 01a129b2-cf6b-7012-a167-043a1a698676 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_003.md |
| numeric_consistency_reviewer | 01a129b8-259b-7a33-80f7-0f3ece30aeba | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a129b8-5c9e-7c92-9c17-7a7021494f5f | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a129b8-92ad-7b63-b00a-a605a8e9f04a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a129c7-b779-7032-a642-4c771d89b0b0 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a129cf-84b6-7100-8632-d270ac1d0646 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a129d5-f792-7cd0-8513-81fd560836b5 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a129dd-b1a8-71d3-9890-7d865e112daf | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a129e5-087a-7262-8048-feac507631de | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

The mandatory support mapper owns support_001.md; its complete output was merged without loss with the disjoint support shards into its canonical primary artifact, extraction/support_quantitative_evidence.md. Shard part paths are each recorded separately in coverage_manifest.md. All 14 actual agents, including the coordinator and two support shards, appear exactly once. Coordinator ownership includes canonical merges, registration, metadata and final validation.
