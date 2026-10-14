# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12bca-f8be-7990-b302-add1cf92d810 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12bce-61a7-79a2-9c05-65a67995cd6f | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12bd1-5944-7041-a266-c6607322b47b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12bd1-91aa-79d2-ac19-868b32be429f | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_a | 01a12bd1-c250-7cb2-b334-17a55afb35ea | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_doc003_pp001-032.md |
| support_quantitative_mapper_shard_b | 01a12bd1-eed7-7561-a3a6-7a9961ceea5f | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_doc003_pp065-096.md |
| support_quantitative_mapper_shard_c | 01a12bd2-0db1-7382-a67c-feeabceff738 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_doc003_pp129-160.md |
| numeric_consistency_reviewer | 01a12bd6-46ce-7101-aa0e-61b820f40eb1 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12bd6-75c0-7d23-80cf-cb43aa47bcbe | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12bd6-b838-7691-a3a4-d96d154fa89c | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a12bda-b512-7c60-aec2-49d5c05b840c | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a12bec-c5b0-7313-9bb5-ec38ca43b6fe | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12bfa-a0fa-7f83-ab7f-56520b3f2690 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a12c01-a608-7bc0-b71b-7490dfdfa493 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12c07-d477-7e42-b839-68c04bcb8eef | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Coordinator packaging repair after initial validation: expanded each completed statistical-pass range into an explicit 132-ID index from the already-complete canonical inventory, and formatted quoted clinical source terminology as a quotation in the quality audit. These are mechanical record repairs; no new scientific findings, screening decisions, classifications or agents were introduced. Finish and report timing were refreshed before final rendering and validation.
