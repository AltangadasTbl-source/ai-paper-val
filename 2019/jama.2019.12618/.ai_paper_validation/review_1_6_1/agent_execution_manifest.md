# Workflow 1.6.1 Agent Execution Manifest

Runtime IDs are the actual canonical task identifiers returned by this session, with the initial slash omitted: root/NAME denotes /root/NAME. Every mandatory specialist stage used a fresh distinct named preset; no agent was promoted or reused across mandatory stages. The mandatory support mapper primary artifact is the lossless canonical merge of its part and four disjoint support parts. Additional bounded mapping and numeric shards are listed separately.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_sap_shard | root/sap_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap_001_064.md |
| support_protocol_a_shard | root/protocol_a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_001_064.md |
| support_protocol_b_shard | root/protocol_b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_065_128.md |
| support_protocol_c_shard | root/protocol_c | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_129_153.md |
| support_sap_formula_repair | root/sap_formula_repair | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap_formula_visual_confirmation.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_one | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| numeric_supplement_shard | root/numeric_supplement_shard | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_supplement.md |
| inclusion_screener | root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_two | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| support_protocol_b1_context_repair | root/protocol_b1_confirmation | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_065_096_bounded_confirmation.md |
| support_protocol_b2_context_repair | root/protocol_b2_confirmation | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_097_128_bounded_confirmation.md |
| support_protocol_a1_context_repair | root/protocol_a1_confirmation | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_001_032_bounded_confirmation.md |
| support_protocol_a2_context_repair | root/protocol_a2_confirmation | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_033_064_bounded_confirmation.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Final local coordinator formatting repair copied the existing77 pass-1 inventory records into the pass-1 checker to make every ID explicit. No new agent or scientific review stage was used; the coordinator remains recorded exactly once.
