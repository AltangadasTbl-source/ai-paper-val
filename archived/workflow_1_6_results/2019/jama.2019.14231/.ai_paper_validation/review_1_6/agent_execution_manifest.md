# Workflow 1.6 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a1287e-6025-7ab1-bc15-d6d8c40ceebd | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a1287f-6a5d-7b22-829b-dc1eace1af13 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12882-140f-7461-abff-e4b82f713701 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12882-33e4-7cd2-9bdd-f27b095e87fc | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a12886-0eb9-7ba0-bdcd-bccaf6412cd7 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12886-30d5-7c72-ad44-dd0cfbe300b9 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12886-5cb4-74b3-b751-c0153f581281 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support_a | 01a12886-83ee-7ac0-afea-c841f69920e7 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support_a.md |
| statistics_pass_1_support_b | 01a12886-ab23-7d51-9109-ce84b0abfc61 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support_b.md |
| statistics_pass_1_graph | 01a12886-d3a5-7901-bcca-fa2475b4b9ee | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_graph.md |
| evidence_rechecker | 01a1288e-8403-7051-b0a2-9dde819d0e0a | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| numeric_consistency_tail | 01a1288f-6d3c-7061-8f37-fde691f58c4c | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_tail_N121_N123.md |
| statistics_pass_2 | 01a12893-27ee-7b01-8b06-12a270139f0a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_support_a | 01a12893-5344-7fb2-a4f4-e1a8e8ac9e7c | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support_a.md |
| statistics_pass_2_support_b | 01a12893-81b4-72f3-b8a7-0148d9978ace | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support_b.md |
| statistics_pass_2_graph | 01a12893-ae96-73e1-b2e5-d1025d6d004a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_graph.md |
| quality_control_auditor | 01a12897-ea72-7dc3-a2e8-fa4228d5574f | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a1289d-9b30-70f0-b3f7-2b5d937c986c | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
