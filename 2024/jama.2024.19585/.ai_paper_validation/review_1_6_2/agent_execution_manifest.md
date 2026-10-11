# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129ab-d869-7862-8674-5be7c3ea3ce3 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a129ae-95bc-7d71-a296-14fdb6208bc0 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a129b1-193e-71e0-bfc4-ffd8db937dad | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a129b1-36ec-7cb2-ba29-5f29a1a78ec6 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a129b5-e322-7ff1-a198-947ffd0e507e | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a129b6-079a-7e33-a3bd-a948d6575855 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a129b6-3a3f-7742-b588-3b9736635a69 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a129bc-b625-7260-9a1e-c110b1a90be7 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a129c2-9398-7d72-a901-f965a97cdd81 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a129c7-e5ad-70f3-ad51-87e5ed913bb7 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a129cd-34db-7163-800a-23321bca57df | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a129d2-fee4-78c1-926a-4123de7d7814 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
