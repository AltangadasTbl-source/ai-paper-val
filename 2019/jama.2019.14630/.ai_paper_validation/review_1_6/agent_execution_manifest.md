# Workflow 1.6 Agent Execution Manifest

Current provider is inherited unchanged (`openai`), as requested by the user. Model/effort pairs follow the package role presets.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a1287f-b412-7fb1-b2c3-e896d5c46b5c | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12882-b157-7e53-b8e7-60587b3f254a | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12885-02ae-71e3-b93b-a0935c310f99 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12885-24f9-76d1-b5d3-6f538344f85b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_protocol_mapper_shard | 01a12885-41eb-7861-84d1-b6ce1eeb0192 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_protocol_evidence.md |
| numeric_consistency_reviewer | 01a1288b-3a49-73b2-83e0-4741b4787eba | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_protocol_reviewer_shard | 01a1288b-5961-7503-bb4e-91e7e573c6e0 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_protocol.md |
| numeric_support_reviewer_shard | 01a1288b-7ea4-7e11-a311-a35c8ef28abd | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| cross_source_consistency_reviewer | 01a1288b-a18b-78f2-becc-b113149608ba | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a1288b-cce9-71c1-95f3-6666ddbc1f12 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | 01a12892-aa42-7020-a2ff-9fdae4fce05a | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a1289d-2ec2-73a1-bcae-13562fddd276 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a1289d-7380-7d80-911e-f81d75cc88c1 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| append_evidence_rechecker | 01a1289f-367f-7593-a248-cbc9d74f3fa5 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck_appendix.md |
