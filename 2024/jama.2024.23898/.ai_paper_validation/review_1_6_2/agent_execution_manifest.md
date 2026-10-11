# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129ab-e5c1-7891-8d9d-9c92bcbd3fd1 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a129ae-ba27-7791-aa58-c6a840206264 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a129b1-cb3d-7fc1-9d95-25851de705dd | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a129b1-ea28-7e81-9673-8ce3a298af75 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_sap_shard | 01a129b2-16bf-7c30-8d77-14210371e14a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_sap_results_evidence.md |
| numeric_consistency_reviewer | 01a129b6-9549-7683-b008-830f8e57970b | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_support_shard | 01a129b6-b5e9-7d52-bfde-e8d7b31f3a04 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| statistics_pass_1 | 01a129b6-dd28-7c32-bf59-a2509c3c5d7d | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_consistency_reviewer | 01a129b6-fc00-7351-bd76-e5d3e4f6b89b | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| inclusion_screener | 01a129c2-36f7-71d0-acc6-f76cb4e358b4 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a129c7-19ce-7d42-98a6-ce817ff70ca8 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a129cd-e852-7de3-b1c8-49555ee06fb1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| inclusion_screener_pass_2 | 01a129d2-3673-7190-9f7f-2968671df59f | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_pass_2_occurrences | 01a129d5-bf52-7880-a0a5-f7b594975e8d | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/pass_2_occurrence_recheck.md |
| quality_control_auditor_coverage_shard | 01a129d8-1162-7c23-bf91-074472eb3f22 | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_quality_audit.md |
| quality_control_auditor | 01a129dd-cf8b-70b3-ac56-9d4a7cde1731 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_tail_shard | 01a129dd-facd-79a3-8254-517af72ee357 | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/candidate_audit_tail.md |
| report_generator | 01a129e4-3109-7183-a791-2c3a0882127d | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
| report_generator_tail_cards | 01a129e3-e4fb-7521-86e1-9de39329558f | gpt-6.1-sol | medium | FRESH_SPAWN | report/parts/tail_cards.md |
