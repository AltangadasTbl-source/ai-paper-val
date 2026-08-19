# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper_shard_doc002 | root/support_mapper_doc002 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc002_pp001-025.md |
| support_quantitative_mapper_shard_001_032 | root/support_mapper_001_032 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003_pp001-032.md |
| support_quantitative_mapper_shard_033_064 | root/support_mapper_033_064 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003_pp033-064.md |
| support_quantitative_mapper_shard_065_096 | root/support_mapper_065_096 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003_pp065-096.md |
| support_quantitative_mapper_shard_097_128 | root/support_mapper_097_128 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003_pp097-128.md |
| support_quantitative_mapper_shard_129_160 | root/support_mapper_129_160 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003_pp129-160.md |
| support_quantitative_mapper_shard_161_167 | root/support_mapper_161_167 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_doc003_pp161-167.md |
| support_quantitative_mapper | root/support_mapper_merge | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | limitations.md |
