# Workflow 1.6.2 Agent Execution Manifest

The coordinator ID is its current session UUID. Specialist IDs are their actual CODEX_THREAD_ID values, returned by each fresh specialist. Every specialist task is newly spawned for its named stage.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129af-70e5-7f72-80a0-6613a01bbb24 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a129b0-f753-7063-bd19-d468d23f6caf | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a129b4-045d-7910-b98e-2eeafcaa15c0 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_plan_mapper_a | 01a129b4-3f17-7c51-9f95-75431d8b2433 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_plan_a.md |
| support_plan_mapper_b | 01a129b4-6407-7290-94af-d95244e7d3bc | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_plan_b.md |
| support_plan_mapper_c | 01a129b4-83d9-7a20-a3fa-5232fa737f12 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_plan_c.md |
| support_plan_mapper_d | 01a129b4-a84d-7ea2-a4e0-6654dc94857b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_plan_d.md |
| support_quantitative_mapper | 01a129b4-c709-70b1-9d71-591188a0a35a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a129ba-7aa6-77c0-9fab-ab97751545fe | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_support | 01a129ba-a075-7e40-8815-b16cd5e4d1ad | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| statistics_pass_1 | 01a129ba-d0ae-7972-ad30-ec98db09c65f | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support | 01a129ba-f6dd-7cd3-ac0d-591be72882c8 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support_pass_1.md |
| statistics_pass_1_plan | 01a129bb-2346-7d93-89e3-266a9f7a3f14 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_plan_pass_1.md |
| cross_source_consistency_reviewer | 01a129bb-6a63-7c90-8382-58982d46908a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1_monitoring | 01a129be-d2f9-73e3-94d5-a2df0a75cd43 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_monitoring_pass_1.md |
| inclusion_screener | 01a129c4-9c36-7e01-be3f-8b97966c8822 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a129cf-7c7a-7882-8c5f-12ba5ca391b4 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a129d9-0afb-7071-a4ab-bc2c2e152fc2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_support | 01a129d9-3869-7ef2-bdca-396e4635945a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_report_support_pass_2.md |
| statistics_pass_2_plan | 01a129d9-67a8-73b1-896f-eabbacc1a39a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_plan_pass_2.md |
| statistics_pass_2_monitoring | 01a129d9-9035-77c3-b829-b5118f5f2bd9 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_monitoring_pass_2.md |
| inclusion_screener_pass_2 | 01a129e1-b558-7331-b786-a24a51c7f784 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_pass_2 | 01a129e4-f611-7510-9c03-ccbe60dedc0d | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck_appended.md |
| quality_control_auditor | 01a129e9-8c39-7691-945e-b490f062019c | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_support | 01a129ea-c9cd-7963-af96-35c47b46ef8d | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/audit_support.md |
| report_generator | 01a129f7-1283-7ce3-8e08-59d0c5a16f05 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
| report_generator_support | 01a129f7-5ba3-7ea0-b777-3fb3752dbc06 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/support.md |
