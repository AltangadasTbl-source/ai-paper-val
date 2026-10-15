# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a13b36-d6d1-7af3-825d-70597a244893 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| superseded_asset_curation | task:/root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | execution/superseded_curator.md |
| main_quantitative_mapper | task:/root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| superseded_support_mapping | task:/root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | execution/superseded_support_mapper.md |
| support_mapper_protocol_a | task:/root/support_mapper/protocol_a | gpt-6.1-sol | medium | FRESH_SPAWN | execution/superseded_protocol_a.md |
| support_mapper_protocol_b | task:/root/support_mapper/protocol_b | gpt-6.1-sol | medium | FRESH_SPAWN | execution/superseded_protocol_b.md |
| support_mapper_protocol_c | task:/root/support_mapper/protocol_c | gpt-6.1-sol | medium | FRESH_SPAWN | execution/superseded_protocol_c.md |
| reuse_asset_curator | task:/root/curator_fresh | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| support_quantitative_mapper | task:/root/support_fresh | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_mapper_protocol_a_fresh | task:/root/support_fresh/protocol_a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/fresh_support_protocol_a.md |
| support_mapper_protocol_b_fresh | task:/root/support_fresh/protocol_b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/fresh_support_protocol_b.md |
| support_mapper_protocol_c_fresh | task:/root/support_fresh/protocol_c | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/fresh_support_protocol_c.md |
| numeric_consistency_reviewer | task:/root/numeric | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | task:/root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | task:/root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| numeric_support_a | task:/root/numeric/support_a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_support_a.md |
| numeric_support_b | task:/root/numeric/support_b | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_support_b.md |
| cross_plan_comparisons | task:/root/cross_source/cross_plan | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_plan_current.md |
| statistics_pass_1_protocol_confirmation | task:/root/statistics_protocol_confirmation | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1_protocol_confirmation.md |
| inclusion_screener | task:/root/inclusion_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | task:/root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | task:/root/statistics_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_numeric_coverage_a | task:/root/audit_numeric_a | gpt-6.1-sol | high | FRESH_SPAWN | quality/numeric_coverage_a.md |
| quality_numeric_coverage_b | task:/root/audit_numeric_b | gpt-6.1-sol | high | FRESH_SPAWN | quality/numeric_coverage_b.md |
| quality_numeric_coverage_c | task:/root/audit_numeric_c | gpt-6.1-sol | high | FRESH_SPAWN | quality/numeric_coverage_c.md |
| quality_control_auditor | task:/root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | task:/root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime identifier encoding: `task:` prefixes the exact canonical runtime task name returned by the collaboration tool. For example, `task:/root/statistics_pass_1` denotes the actual `/root/statistics_pass_1` runtime. This transparent namespace encoding preserves each tool-returned name and gives the identifier an alphanumeric start required by the supplied validator. It does not replace, invent or merge runtimes. The coordinator retains its current-session UUID. Model, effort, start mode and distinctness are unchanged.
