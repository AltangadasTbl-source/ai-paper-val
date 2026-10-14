# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12bb5-7d06-7e53-8626-6674bf5f1f12 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12bba-670c-7de2-bbc2-d54fc0338c04 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12bbd-7fc1-77e2-aba1-6d633239c859 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12bbd-b9c8-7193-ab38-81d4361d11e9 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_other | 01a12bbd-f041-7681-ae2d-1e570d8c0948 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/other_support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a12bc4-5fd4-75e2-83e5-902a2215ae7a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12bc4-a327-7353-973d-873176305f75 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12bc4-da4e-7872-9b54-7504ad4553d6 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a12bd0-1da8-7853-a91b-e1e467622b2b | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a12bd5-58d1-7073-87fa-573d501cd889 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12bda-7e88-79b3-87e9-04b0f5c2fa7b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a12be2-17c4-7ae0-bdd1-fa336db2aeec | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12be9-d67e-7bb3-8e6e-dae568a2c5e0 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
