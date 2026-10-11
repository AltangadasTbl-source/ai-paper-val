# Workflow 1.6 Agent Execution Manifest

Runtime provider openai is explicitly authorized by the user. All agents retain the fixed model and reasoning contracts.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a1285f-83e8-7ef3-b9e5-9fcd3cdb90c9 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12863-2f29-7e90-89c6-5dacc138b8f9 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12865-4595-7121-9aa1-b873e7ae3dd8 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12865-691c-7d70-8421-94a8a420e881 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_b | 01a12865-8857-71c2-9bf4-63f6026a57a0 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_part_b.md |
| numeric_consistency_reviewer | 01a12869-4940-75a1-9683-5c660f25dc14 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12869-684f-7cd3-a40a-f4c41d8177a5 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12869-8c20-7fb1-b42a-ba626d66dcf5 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| numeric_consistency_reviewer_plan_shard | 01a12869-f6ef-7c82-8875-cf8b909c098a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_plan.md |
| evidence_rechecker | 01a12871-ed60-7951-bfc9-08725b3b7034 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12878-2f36-79f1-b1a9-e4f616338e59 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_shard_b | 01a12878-53d5-74d0-9f61-494191df4c27 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2_b.md |
| statistics_pass_2_shard_c | 01a12878-77b7-78b1-9595-6991f807c8c2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2_c.md |

| quality_control_auditor_coverage_shard | 01a12879-4ba6-7000-9923-a2946b459279 | gpt-6.1-sol | high | FRESH_SPAWN | quality/coverage_audit.md |

| quality_control_auditor | 01a1287e-762f-77f1-8862-7c6fe0d7959d | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |

| report_generator | 01a12882-252e-7510-af49-2cb567fed131 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Each specialist reports its actual CODEX_THREAD_ID environment value. Each mandatory stage receives a fresh, distinct runtime ID.
