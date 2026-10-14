# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12c37-1893-74f1-897e-a267d3ec6c91 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12c3a-ad69-7ce3-9b2b-fe66c6bb1a9e | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12c3e-01ad-7673-9de4-6a93ac228f9a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12c3e-2db0-7c93-be73-02205fb46d25 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_002 | 01a12c3e-4cf1-7ae0-abe5-92f8e7eeeb7a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_002.md |
| support_quantitative_mapper_shard_003 | 01a12c3e-6be1-7ae3-bfde-811b576aabdb | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_003.md |
| support_quantitative_mapper_shard_004 | 01a12c3e-9878-7643-ac34-dc470d601834 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_004_results.md |
| numeric_consistency_reviewer | 01a12c43-4b9c-7822-9aac-7a3316381f85 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_support_shard | 01a12c43-8381-77c0-a329-6a6ab73645eb | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| cross_source_consistency_reviewer | 01a12c43-c216-7643-8a0e-dfb48b6c9195 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12c43-fb96-7943-933b-ea7e7d98f89b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a12c4f-b7b6-7203-8c95-cfee2debbcc0 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| inclusion_source_confirmation_shard | 01a12c50-f19c-7ce1-aab5-f9cdca5b913f | gpt-6.1-sol | high | FRESH_SPAWN | screening/source_confirmation_plan.md |
| evidence_rechecker | 01a12c63-86c3-78d0-84d8-ccea451f5769 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| evidence_rechecker_shard_002 | 01a12c63-aaf3-7ea2-b202-3ccc33a45f88 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/recheck_002.md |
| evidence_rechecker_shard_003 | 01a12c63-ca83-7d51-ad07-f4248a018f40 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/recheck_003.md |
| statistics_pass_2 | 01a12c69-56be-71f0-b3ab-86730a0e1482 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_shard_b | 01a12c69-7ef5-7931-8e31-fcfee62a592a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2b.md |
| statistics_pass_2_shard_c | 01a12c69-a5a4-7881-b225-dcd2aeae5d0f | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2c.md |
| quality_control_auditor | 01a12c70-5a35-7fc1-9c30-a421a32d87bf | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_candidates_002 | 01a12c70-9043-7552-8bc3-bac08204fa08 | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/audit_candidates_002.md |
| quality_control_auditor_candidates_003 | 01a12c70-bd04-7fb0-bfda-088b9ae10bfc | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/audit_candidates_003.md |
| quality_control_auditor_source_coverage | 01a12c70-fcf0-7223-bf50-7ba7d37585a9 | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/audit_source_coverage.md |
| quality_control_auditor_statistical_coverage | 01a12c71-3159-7be1-afc7-7b767f8097c0 | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/audit_statistical_coverage.md |
| report_generator | 01a12c78-d931-75e1-90c1-ce1e873a2138 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
