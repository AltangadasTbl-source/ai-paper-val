# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12bb5-88b9-7b72-a590-57777c02553b | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12bba-0183-74c1-bdfc-5e047937cdf0 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12bbd-a933-7df3-bfb9-5026d04ab9b8 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12bbd-de8a-7c62-994b-2a5e0f69af86 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_plan_mapping_shard | 01a12bbe-14e2-79f1-9684-db2e906f567e | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_plans_part.md |
| numeric_consistency_reviewer | 01a12bc3-f416-7280-b2e8-d1659e444786 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12bc4-2f48-7c51-9f05-5bc5a8635034 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12bc4-75ca-7762-89f7-0276d9ba0568 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a12bd2-58a6-7751-9c34-56a3c6d72244 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a12bd9-0312-71a2-a567-4af3c979ae63 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| coverage_audit_shard | 01a12bdc-3fe3-7e32-aa95-cc6d30f56bf0 | gpt-6.1-sol | high | FRESH_SPAWN | quality/coverage_audit_part.md |
| statistics_pass_2 | 01a12bdf-f1cd-7f80-8adf-61011518d880 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| screening_audit_shard | 01a12be3-6df6-7e52-b775-ff1d016c7e2c | gpt-6.1-sol | high | FRESH_SPAWN | quality/screening_audit_part.md |
| quality_control_auditor | 01a12be7-3d83-7b10-8a22-d0cc3ec18b4d | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12bec-dae3-7471-9311-a31a1b2199b3 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
