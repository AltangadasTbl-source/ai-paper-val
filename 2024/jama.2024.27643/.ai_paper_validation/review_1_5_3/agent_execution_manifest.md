# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper_shard_001 | root/support_mapper_001 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc002_p001_p076.md |
| support_quantitative_mapper_shard_002 | root/support_mapper_002 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc002_p077_p152.md |
| support_quantitative_mapper_shard_003 | root/support_mapper_003 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc002_p153_p229.md |
| support_quantitative_mapper_shard_004 | root/support_mapper_004 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003_p001_p065.md |
| support_quantitative_mapper_shard_005 | root/support_mapper_005 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003_p066_p130.md |
| support_quantitative_mapper_shard_006 | root/support_mapper_006 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc004_doc005_doc006.md |
| support_quantitative_mapper | root/support_mapper_merge | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | limitations.md |

Every mandatory specialist stage used a fresh runtime ID and exactly one primary durable artifact in this manifest. Shard agents have disjoint scopes and unique artifacts.
