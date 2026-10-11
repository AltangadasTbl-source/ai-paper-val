# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129ab-bade-7253-b313-f5ed29533c7c | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a129ae-7eab-78d0-9d49-82bbb364e226 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a129b0-fc95-70f0-9813-251d72f97be6 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a129b1-1c9d-7bd2-a90b-b0403d8cb593 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a129b4-c3f5-7492-bb6b-2461f3c7811e | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a129b4-ed97-7e21-94ff-d13c39bd4cee | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a129b5-1c4b-7ed3-955e-c6ca5e85d0b6 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| numeric_consistency_support_shard | 01a129b5-97cf-7843-9ca2-d5d4de552d64 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support_consistency.md |
| inclusion_screener | 01a129be-effc-76d0-a857-3dce2161cd4a | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a129c8-65ac-77a3-bd94-7df0e00a6fb0 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a129ce-662d-78e3-ae0a-28ba82dc65c9 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| inclusion_screener_pass_2 | 01a129d7-7723-7a51-85ed-fef5e15acf20 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_pass_2 | 01a129d8-cbb2-7722-9cd1-850c8005a09c | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck_pass_2.md |
| quality_control_auditor | 01a129dc-bfaa-7f43-a2c8-6a41229edb68 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a129e6-b4ad-7a31-b78f-6e86f26a68a9 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Coordinator closeout repair: the first final-validator call found one prohibited vocabulary token in an audit bookkeeping sentence about initial/current screening counts. The current coordinator replaced it with neutral wording and refreshed the finish/performance fields before rerendering and validation. No new agent, source value, candidate ID, evidence state, classification or screening decision was introduced.
