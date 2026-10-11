# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a1294f-d50f-7a62-ab66-e12921e0d045 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12951-45be-76c3-99d7-0b62845a79d3 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| support_quantitative_mapper | 01a12954-8920-7162-b94e-e03ebdc67f17 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_mapper_protocol_002 | 01a12954-c5d7-7741-96c0-704c55754ff2 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_033_064.md |
| main_quantitative_mapper | 01a12954-6cae-71f1-adb6-fb46b0685043 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_mapper_protocol_001 | 01a12954-b115-74d2-9bde-a16449bb5a5f | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_001_032.md |
| support_mapper_sap_001 | 01a12956-69d8-74f3-914e-d550cbd34883 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap_001_032.md |
| support_mapper_protocol_003 | 01a12954-dbd4-7d10-a3f7-3d4599c0b038 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_065_096.md |
| support_mapper_protocol_004 | 01a12954-f28d-7d10-b4e3-3fd6bffaa24f | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_097_128.md |
| support_mapper_protocol_005 | 01a12957-aa8a-7130-b76c-340094d011e5 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_129_153.md |
| support_mapper_sap_003 | 01a12957-945a-7912-a719-17bffa671958 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap_065_083.md |
| support_mapper_sap_002 | 01a12956-c8b0-7b51-aa9d-89506e1885d3 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap_033_064.md |
| numeric_consistency_reviewer | 01a1295b-826f-79f2-8270-a4045d781af1 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a1295b-a831-7e91-9486-86028ddcd6d5 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| cross_source_outcomes_shard | 01a1295b-d22c-7933-b7de-08e9967fa467 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/cross_source_outcomes.md |
| statistics_pass_1 | 01a1295b-f2a5-77e3-ac6d-7bc5bae5cb6a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_protocol_shard | 01a1295c-1392-7e11-b541-53210ee40994 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_protocol.md |
| inclusion_screener | 01a12965-ea5a-7992-b096-515d4d8c13f0 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a1296b-928f-7c80-a47c-146b970052e8 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12973-ed5c-7941-a70e-a5e9d3a1cb6b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_protocol_shard | 01a12974-1579-73b0-b8ab-92623ac9e756 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_protocol.md |
| inclusion_screener_pass_2 | 01a1297a-84be-7ae2-8e92-e70e71758da0 | gpt-6.1-sol | high | FRESH_SPAWN | screening/parts/inclusion_screen_pass_2.md |
| evidence_rechecker_appended | 01a1297c-ff3e-7392-baa9-e3e271241550 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_appended.md |
| quality_control_auditor | 01a1297f-9386-73d0-afe0-f27feccaaced | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_numeric_shard | 01a1297f-c0fb-7e01-811b-4e2bf833ae2d | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/evidence_quality_numeric.md |
| report_generator | 01a12985-2da3-7a90-a05c-40d16203a583 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
