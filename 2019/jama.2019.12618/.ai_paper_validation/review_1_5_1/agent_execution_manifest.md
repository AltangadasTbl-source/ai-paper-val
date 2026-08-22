# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | runtime:/root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapper | runtime:/root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | runtime:/root/supp_results_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_supp_results_pp001_016.md |
| support_quantitative_mapper | runtime:/root/protocol_mapper_001_032 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_protocol_pp001_032.md |
| support_quantitative_mapper | runtime:/root/protocol_mapper_033_064 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_protocol_pp033_064.md |
| support_quantitative_mapper | runtime:/root/protocol_mapper_065_096 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_protocol_pp065_096.md |
| support_quantitative_mapper | runtime:/root/protocol_mapper_097_128 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_protocol_pp097_128.md |
| support_quantitative_mapper | runtime:/root/protocol_mapper_129_153 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_protocol_pp129_153.md |
| support_quantitative_mapper | runtime:/root/sap_mapper_001_032 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_sap_pp001_032.md |
| support_quantitative_mapper | runtime:/root/sap_mapper_033_064 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_sap_pp033_064.md |
| support_quantitative_mapper | runtime:/root/sap_mapper_065_083 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_sap_pp065_083.md |
| support_quantitative_mapper | runtime:/root/data_sharing_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | parts/support_data_sharing_p001.md |
| relationship_consolidator | runtime:/root/relationship_consolidator | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_checker | runtime:/root/numeric_checker_001_094 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/numeric_checks_N001_N094.md |
| numeric_checker | runtime:/root/numeric_checker_095_188 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/numeric_checks_N095_N188.md |
| numeric_checker | runtime:/root/numeric_checker_189_282 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/numeric_checks_N189_N282.md |
| cross_source_checker | runtime:/root/cross_checker_scope_1 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/cross_source_N001_N094_S001_S025.md |
| cross_source_checker | runtime:/root/cross_checker_scope_2 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/cross_source_N095_N188_S026_S051.md |
| statistics_pass_1 | runtime:/root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_checker | runtime:/root/cross_checker_scope_3 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/cross_source_N189_N248_S052_S080.md |
| cross_source_checker | runtime:/root/cross_checker_scope_4 | gpt-5.6-terra | medium | FRESH_SPAWN | parts/cross_source_N249_N282_S081_S101.md |
| numeric_checker_consolidator | runtime:/root/numeric_checker_consolidator | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| candidate_registration | runtime:/root/cross_candidate_consolidator | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| evidence_recheck | runtime:/root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | runtime:/root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | runtime:/root/quality_control_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | runtime:/root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation.md |

