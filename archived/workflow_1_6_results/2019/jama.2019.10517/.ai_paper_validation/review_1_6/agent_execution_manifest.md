# Workflow 1.6 Agent Execution Manifest

Actual runtime provider: openai, expressly authorized by the user in place of the configured openrouter provider. All agents retain the fixed model and effort requirements.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12860-cec4-7f22-bd5d-22a027867aab | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12862-ddad-7a52-8190-b8730a1cfe2e | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12865-5284-7fd3-8b3b-5e3162260ca4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12865-7761-7463-94e9-82162135e72a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_plan_second_shard | 01a12865-9452-7e81-82ac-345be361fa05 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_second.md |
| numeric_consistency_reviewer | 01a1286a-6645-7930-8d1b-45686ffab070 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_report_last_shard | 01a1286a-814f-7b12-a00b-e90ab6064dbe | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_report_last.md |
| numeric_plan_first_shard | 01a1286a-9bc9-7b92-a717-2777aa292dbf | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_plan_first.md |
| numeric_plan_last_shard | 01a1286a-b71f-73c2-90f9-22d2fd35e362 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_plan_last.md |
| statistics_pass_1 | 01a1286a-d824-7281-a62a-c73b450e930c | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_consistency_reviewer | 01a1286a-f59b-7f01-8800-04b775b11953 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| evidence_rechecker | 01a12872-9b72-7460-86ab-0229340c9851 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12878-d12a-7d81-a8cf-041b2a0b54f7 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a1287d-2993-7d60-a161-d4cc0ebd7edd | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12881-d989-7242-8223-53733c47a31a | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
