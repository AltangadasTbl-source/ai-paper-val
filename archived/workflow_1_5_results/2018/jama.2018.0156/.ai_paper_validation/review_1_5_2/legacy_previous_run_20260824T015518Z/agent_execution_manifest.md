# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| fresh_source_preprocessing | ec752004-1fe1-53b2-8232-b61a88e90fc1 | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapping | 1ab14919-011a-52bd-8466-6b46d349699d | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapping_001 | f80933af-4be1-59f1-a3a1-249e4965f15b | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_001_pp001_050.md |
| support_quantitative_mapping_002 | fcf1ed1a-48ee-54cc-b67e-b469c1e1920a | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_002_pp051_100.md |
| support_quantitative_mapping_003 | 4451ad83-7d98-5b94-92e6-c0ff6ac951a9 | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_003_pp101_134_doc003.md |
| relationship_inventory_merge | 3605d978-cb09-5b5c-a2c1-d372918b8298 | gpt-5.6-terra | medium | FRESH_SPAWN | relationships/numeric_relationship_inventory.md |
| numeric_consistency_review | d8d97fbf-b16d-578f-882d-50c8e3c2f980 | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_review | 9c8b1144-85b7-594d-a423-3821bcf2dd2f | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 73b64cf4-d780-58b8-b200-d7723373321d | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| candidate_registration | b7f215f2-95c6-5b76-9caf-e193e8bb69d0 | gpt-5.6-terra | medium | FRESH_SPAWN | candidate_ledger.md |
| evidence_recheck | 38085982-19f9-5d61-abf9-4673515661e6 | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 23866370-c384-545f-af7b-e837892be6b0 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality_audit | bb503380-c331-5f67-8566-108424ee529e | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | f7216cee-425c-5269-98c0-50f46806fa65 | gpt-5.6-terra | medium | FRESH_SPAWN | limitations.md |
