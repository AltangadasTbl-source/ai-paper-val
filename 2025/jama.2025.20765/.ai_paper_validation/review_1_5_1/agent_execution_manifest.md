# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curation | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | source_inventory.md |
| main_evidence_mapping | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | parts/main_evidence_DOC-001_pp001-009.md |
| support_evidence_mapping_1 | root/support_mapper_1 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_evidence_DOC-002_pp001-032.md |
| support_evidence_mapping_2 | root/support_mapper_2 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_evidence_DOC-002_pp033-064.md |
| support_evidence_mapping_3 | root/support_mapper_3 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_evidence_DOC-002_pp065-096.md |
| support_evidence_mapping_4 | root/support_mapper_4 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md |
| numeric_checks | root/numeric_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_checks | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_recheck_attempt_1 | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN_INTERRUPTED | verification/evidence_recheck_attempt_1.md |
| evidence_recheck_retry | root/evidence_rechecker_retry | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation_record.md |
