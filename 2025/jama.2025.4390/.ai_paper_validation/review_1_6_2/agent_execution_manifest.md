# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12bb5-744c-75d0-8603-7d2ccb5b6631 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12bb9-f5b3-73a3-8e07-0cd0adccbc02 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12bbc-5da9-7d42-af3f-0d5325decd82 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12bbc-89d0-7212-83f3-af724f1a019a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_results_a | 01a12bbc-b231-73f0-826a-30815634b6da | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_results_001_024.md |
| support_quantitative_mapper_results_b | 01a12bbc-d26c-7380-a8cf-40bfd4b5f2e4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_results_025_049.md |
| numeric_consistency_reviewer | 01a12bc2-c4ca-7963-bbef-5b49f8963c59 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12bc2-f62f-7690-92dd-2374810a7228 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12bc3-34f6-7a90-9ccf-69efae0c63b2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a12bcf-3c84-72a3-8667-fcaaa0aecdfa | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a12bd9-199c-79b3-ad30-d9f4cbcb0965 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12be3-797f-7a41-97f5-fe8093d565ce | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a12beb-ba4e-7280-9114-0dfca0e1cd60 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12bf3-79ae-7cf0-a5ed-a9ce0c457895 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
