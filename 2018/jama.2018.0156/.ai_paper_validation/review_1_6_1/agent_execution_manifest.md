# Workflow 1.6.1 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a128db-a3c6-7261-9791-160147d8210f | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a128e0-859a-7782-a0da-af74d73251b5 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a128e3-1e2a-7950-a6d7-1160d6b11d44 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a128e3-42f0-7731-8b6d-bc260f7e36ea | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_final_shard | 01a128e3-668f-7150-ae14-6e0af41971ad | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_final_plan_results.md |
| numeric_consistency_reviewer | 01a128e7-cc36-7d53-98bd-05dedeb36905 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_support_shard | 01a128e7-f3a0-7770-a947-d62dbe760872 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| cross_source_consistency_reviewer | 01a128e8-1808-73e3-9497-1d402cbb902e | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a128e8-4022-7ff0-8a20-57d007b2fa27 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a128ef-16e2-7623-82e2-2df3868acfc6 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a128f3-ae65-7bf1-85c2-2809027f8172 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a128f7-8354-7f82-b8fd-4c65c1fbd3e2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a128fb-ee7f-7593-b991-821cf04614d2 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12903-6527-7393-b172-810de9923caf | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
