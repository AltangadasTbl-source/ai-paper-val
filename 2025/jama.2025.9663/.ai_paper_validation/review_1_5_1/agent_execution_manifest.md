# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| source_inventory_and_reuse | root/reuse_asset_curation | gpt-5.6-terra | medium | FRESH_SPAWN | source_inventory.md |
| main_evidence_mapping | root/main_mapping_doc001 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/main_mapping_doc001.md |
| support_evidence_mapping | root/support_doc002_a | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_mapping_doc002_pp001_028.md |
| support_evidence_mapping | root/support_doc002_b | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_mapping_doc002_pp029_056.md |
| support_evidence_mapping | root/support_doc002_c | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_mapping_doc002_pp057_084.md |
| support_evidence_mapping | root/support_doc002_d | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_mapping_doc002_pp085_112.md |
| support_evidence_mapping | root/support_doc002_e | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_mapping_doc002_pp113_136.md |
| support_evidence_mapping | root/support_doc003 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_mapping_doc003.md |
| relationship_consolidation | root/relationship_consolidation | gpt-5.6-terra | medium | FRESH_SPAWN | relationships/numeric_relationship_inventory.md |
| numeric_checks | root/numeric_consistency | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_checks | root/cross_source_consistency | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| evidence_recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | root/evidence_quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | root/report_generation | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation_record.md |
