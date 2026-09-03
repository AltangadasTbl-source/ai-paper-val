# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_evidence_mapper_001 | root/main_mapper_001 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/main_DOC001_p001-p011.md |
| support_evidence_mapper_d2a | root/support_mapper_d2a | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/support_DOC002_p001-p030.md |
| support_evidence_mapper_d2b | root/support_mapper_d2b | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/support_DOC002_p031-p060.md |
| support_evidence_mapper_d2c | root/support_mapper_d2c | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/support_DOC002_p061-p090.md |
| support_evidence_mapper_d3a | root/support_mapper_d3a | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/support_DOC003_p001-p030.md |
| support_evidence_mapper_d3b | root/support_mapper_d3b | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/support_DOC003_p031-p060.md |
| support_evidence_mapper_d3c | root/support_mapper_d3c | gpt-5.6-terra | medium | FRESH_SPAWN | parts/mapping/support_DOC003_p061-p069.md |
| mapping_integrator | root/mapping_integrator | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_checks | root/numeric_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_checks | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| evidence_recheck | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation.md |
