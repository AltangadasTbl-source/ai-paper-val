# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12c36-2c51-7b62-9b83-4e0a98e4d0d3 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_mapping_sap_shard | root/sap_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap.md |
| support_mapping_manual_a_shard | root/manual_mapper_a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/manual_001_054.md |
| support_mapping_manual_b_shard | root/manual_mapper_b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/manual_055_108.md |
| support_mapping_manual_c_shard | root/manual_mapper_c | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/manual_109_162.md |

| numeric_consistency_reviewer | root/numeric_reviewer | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_checks_shard_2 | root/numeric_reviewer_2 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_2.md |
| numeric_checks_shard_3 | root/numeric_reviewer_3 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_3.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_shard_2 | root/statistics_pass_1_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_2.md |
| cross_source_consistency_reviewer | root/cross_source_reviewer | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| cross_source_manual_shard | root/cross_source_manual | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/cross_source_manual.md |

| inclusion_screener | root/inclusion_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |

| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |

| statistics_pass_2 | root/statistics_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_shard_2 | root/statistics_pass_2_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_2.md |

| quality_control_auditor | root/quality_control_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |

| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Runtime identifiers are the fresh agent task names exposed by the collaboration tool, normalized without the leading slash. Each identifies exactly one spawned runtime; no stage reuses an agent. The support canonical artifact merges the mandatory mapper's protocol/results part and four disjoint support shard artifacts; every part is separately recorded in coverage_manifest.md.
