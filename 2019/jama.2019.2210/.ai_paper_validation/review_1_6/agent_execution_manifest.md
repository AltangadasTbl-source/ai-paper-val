# Workflow 1.6 Agent Execution Manifest

Current provider: openai, explicitly authorized by the user. All roles retain the fixed gpt-6.1-sol model and required effort.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a1285e-f91a-72f0-948c-939d2c0abf5e | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12863-2648-7f93-810c-dab43d6aa39d | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12865-6081-79f1-b75e-7630d977e2a1 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12865-82e1-73f0-9079-eba0a604c91d | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a12868-d20d-7603-b09d-5a1375e78ae9 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12869-2b05-7b33-8375-ced02e4b8999 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12869-5568-7b03-ad14-728b9a27f354 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| numeric_support_shard | 01a12869-0016-7623-8936-bbcb5dbab14a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_support_consistency.md |
| statistics_pass_1_subgroups_shard | 01a1286a-1a24-7f92-8ff0-5dbc424e0a2b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat1-subgroups.md |
| evidence_rechecker | 01a12871-ca61-7202-ac02-70750e754741 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12879-149b-7932-b43b-ecb0574c8c9d | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_subgroups_shard | 01a12879-3236-7643-9db8-9feeafeb4227 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2-subgroups.md |
| quality_control_auditor | 01a1287e-9d22-7262-ab75-67bc0bbc91b9 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12884-74cc-7691-841a-20c995829672 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

The report specialist assembles ../final_report_1_6.md and owns limitations.md as its required canonical manifest handoff. All fourteen actual runtime agents, including the coordinator and three bounded optional shards, are recorded exactly once.
