# Workflow 1.6.2 Agent Execution Manifest

Runtime IDs use the typed identifier `task:<canonical task name>`. The text after `task:` is the exact tool-returned canonical runtime name, including its leading slash. This preserves the runtime identity while meeting the manifest's identifier serialization rule.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | task:/root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | task:/root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | task:/root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | task:/root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_historical_shard | task:/root/plan_mapper_historical | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_plan_historical.md |
| numeric_consistency_reviewer | task:/root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_support_shard | task:/root/numeric_support | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_support_part.md |
| cross_source_consistency_reviewer | task:/root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | task:/root/statistics_first | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | task:/root/inclusion_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| cross_source_consistency_reviewer_rule_repair | task:/root/cross_source_rule_repair | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_rule_repair.md |
| evidence_rechecker | task:/root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | task:/root/statistics_second | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | task:/root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_card_generator_001_008 | task:/root/report_cards_001_008 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/cards_001_008.md |
| report_card_generator_009_015 | task:/root/report_cards_009_015 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/cards_009_015.md |
| report_generator | task:/root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Coordinator closeout at 2026-10-11T07:46:51Z: task:/root mechanically copied the 92 existing first-pass records into explicit checker rows after the initial validator requested individually serialized IDs. No additional agent, scientific stage or inference was substituted. Finish and report timing fields were refreshed before rendering and validation.
