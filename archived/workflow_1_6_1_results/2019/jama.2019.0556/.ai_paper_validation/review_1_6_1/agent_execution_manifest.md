# Workflow 1.6.1 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a128d7-ced6-7203-913d-d0bb174814ae | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a128d9-3d06-70d2-a1d0-5ccead0a7851 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a128dc-0958-7843-9e64-b1c2e7717e86 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a128dc-2bf3-7ca2-aea2-96572b17b6a6 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a128e0-854d-7331-83cd-8bd180d1e2b7 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a128e0-a2d6-7b50-be69-41a055ba6b47 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a128e0-c784-7a33-87ba-81b76f900a82 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a128e5-2413-7142-a2ea-ee880aee0ed9 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a128e9-9623-7823-b691-4b423018a8b4 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a128ed-614f-7511-81f2-7bfca2b8d7fb | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a128f2-2c90-7a32-9beb-7e6e34e8d448 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a128f9-255f-7fb3-b284-6ed8c63b70c1 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
