# Workflow 1.6.1 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a128d8-cb49-7240-92a9-adae59843ecc | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a128d9-d279-7230-bdc2-0057dee243ae | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a128dc-3976-7463-aa5e-038d3d2d330d | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a128dc-5b16-7843-af87-d303851beb40 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_part_2 | 01a128dc-7805-7842-891f-19685b975600 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_results_22_41.md |
| numeric_consistency_reviewer | 01a128df-e823-7a12-8733-878a92b6489c | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_part_2 | 01a128e0-08d6-7511-a772-13eef531d888 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_results_22_41.md |
| cross_source_consistency_reviewer | 01a128e0-2d88-7c62-9d5a-a1d96220ae24 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a128e0-5440-70a0-b016-2c80b4fdde1e | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a128e7-44e6-7420-bb8e-ffde83b45eed | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a128e9-7924-74c3-a02e-3056552798d7 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a128eb-aa04-7c31-bd00-1a4f6eaf25b2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a128ef-ab79-7e50-a1bf-e4f4f7fd9113 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a128f7-233a-7a11-bc88-69207b363122 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
