# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12bb5-8e9a-7c13-9d8e-be103f4ff6f5 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_plan_b_mapping | root/plan_b_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/plan-b.md |
| support_plan_c_mapping | root/plan_c_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/plan-c.md |
| support_plan_d_mapping | root/plan_d_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/plan-d.md |
| support_plan_e_mapping | root/plan_e_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/plan-e.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |

| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |

| statistics_pass_2 | root/statistical_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |

| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |

| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

## Runtime identifiers

Specialist IDs are the canonical runtime task identifiers returned by the collaboration tool, recorded without the leading slash for the manifest identifier syntax. Every listed specialist was freshly spawned under the named preset; none was reused for another mandatory stage.


The current coordinator also performed final metadata formatting and the initial-validator repair: an explicit195-ID pass1 registry was merged from already completed specialist parts. No new agent or scientific inference was introduced; the existing coordinator runtime remains recorded exactly once, and final timing was refreshed.
