# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/plan_mapper_1 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_plan_2 | root/plan_mapper_2 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/plan_002.md |
| support_quantitative_mapper_shard_plan_3 | root/plan_mapper_3 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/plan_003.md |
| support_quantitative_mapper_shard_results_1 | root/results_mapper_1 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/results_001.md |
| support_quantitative_mapper_shard_results_2 | root/results_mapper_2 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/results_002.md |
| numeric_consistency_reviewer | root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_shard_plan | root/numeric_plan | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_plan.md |
| numeric_consistency_reviewer_shard_support | root/numeric_support | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support_report.md |
| cross_source_consistency_reviewer | root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |

| inclusion_screener | root/inclusion_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |

| inclusion_screener_repair_reports | root/screen_repair_reports | gpt-6.1-sol | high | FRESH_SPAWN | screening/parts/bounded_reports.md |
| inclusion_screener_repair_protocol | root/screen_repair_protocol | gpt-6.1-sol | high | FRESH_SPAWN | screening/parts/bounded_protocol.md |

| evidence_rechecker | root/recheck_protocol | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| evidence_rechecker_shard_reports | root/recheck_reports | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/reports.md |

| statistics_pass_2 | root/statistical_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |

| quality_control_auditor | root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |

| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Canonical numeric and support mapping artifacts are mechanical merges of disjoint fresh-agent outputs. The mandatory-stage row identifies the designated leading stage agent and the canonical durable handoff; each additional mapper/checker shard has its own runtime row and authored part path. No stage agent is reused for a different mandatory stage.

Runtime identity representation: this interface exposes canonical task paths, not separate opaque runtime UUIDs. The Agent ID column losslessly represents each tool-returned canonical path without its leading namespace slash, because the bundled validator requires an alphanumeric first character. For each root/name column value, the exact tool-returned runtime identifier is /root/name. These are distinct fresh spawn identities, not invented UUIDs; adding the leading slash recovers the exact identifier. Coordinator identity uses the contract's CURRENT_SESSION marker. Additional shard stage labels are unique so one execution is recorded per actual agent.
