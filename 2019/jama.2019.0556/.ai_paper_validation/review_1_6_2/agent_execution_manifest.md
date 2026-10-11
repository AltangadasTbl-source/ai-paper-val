# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a1294e-b9ae-7b32-a0c9-7e3aa4498fd6 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a1294f-7de7-7a21-9364-2665933d201e | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12952-18dd-7ad1-859f-41f68cf99a98 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12952-31b6-7c21-892d-2f93e15dcf93 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a12955-73e0-70e1-8995-af54c921c97a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12955-9d0e-7423-b6d8-0ca949eeff5c | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12955-bf9a-7752-8bc3-60a9eb6b0913 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a12961-bb12-7b33-9fe3-bfa225512c1c | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a12967-ce19-7870-ab5f-360c3a26c7a7 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a1296e-431b-7372-92ce-7add831babfb | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a12975-19aa-7413-b66d-a700187fc29f | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a1297e-9bb6-7902-be28-1ca4c379e646 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
