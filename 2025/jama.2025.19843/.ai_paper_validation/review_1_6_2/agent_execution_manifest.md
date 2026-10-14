# Agent execution manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12c36-c3f5-7e80-904c-40dfa4343c9d | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_inventory | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapping | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapping | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_protocol_001 | root/protocol_mapping_001 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_001.md |
| support_protocol_002 | root/protocol_mapping_002 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_002.md |
| support_protocol_003 | root/protocol_mapping_003 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_003.md |
| numeric_consistency_reviewer | root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_support_checker | root/numeric_support | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| cross_source_consistency_reviewer | root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_remaining_checker | root/cross_source_remaining | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/cross_source_remaining.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| inclusion_screener | root/inclusion_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| audit_mapping_main_protocol | root/audit_mapping_main_protocol | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_main_protocol.md |
| audit_mapping_support | root/audit_mapping_support | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_support.md |
| audit_cross_relationships | root/audit_cross_relationships | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/cross_source_audit.md |
| audit_statistical_relationships | root/audit_statistical_relationships | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/statistical_audit.md |
| statistics_pass_2 | root/statistics_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_control_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generation | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

The collaboration runtime exposes canonical task IDs rather than UUIDs. Runtime task IDs are recorded with their initial slash omitted to satisfy the manifest schema; for example root/main_mapping denotes /root/main_mapping. Every specialist was freshly spawned with its named role preset. The mandatory support mapping artifact is the coordinator's complete lossless merge of support_core and the three protocol parts; the named support mapper owns the core part and each additional mapper owns its disjoint protocol part.
