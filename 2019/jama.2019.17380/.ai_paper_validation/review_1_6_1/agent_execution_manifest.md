# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | agent:/root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | agent:/root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | agent:/root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | agent:/root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | agent:/root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | agent:/root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | agent:/root/statistics_pass1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | agent:/root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | agent:/root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | agent:/root/statistics_pass2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_shard_b | agent:/root/statistics_pass2_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_b.md |
| quality_control_auditor | agent:/root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | agent:/root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime identifiers are the exact unique canonical task names exposed by the collaboration runtime. The `agent:` prefix in ID cells is a serialization prefix; the text following it is the exact runtime identifier, including its leading slash. The coordinator identifier is `/root`. The runtime exposes no separate opaque UUID. Every actual agent appears once: 13 agents comprising the coordinator, 11 mandatory fresh specialists, and one optional fresh statistical shard specialist.
