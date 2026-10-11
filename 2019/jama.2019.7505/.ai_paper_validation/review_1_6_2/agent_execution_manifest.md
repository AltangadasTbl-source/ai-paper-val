# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a1294f-a238-7102-ba12-2a47f70500b4 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12951-4413-7920-9cd3-819456285203 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12953-79b8-7ef2-9d11-54bb3662d6a4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12953-9a0b-7d70-809d-2684b6fa0b34 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a12959-5a05-7980-8b19-ced046b9cf42 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12959-801d-7763-b4b6-80ba61b5f412 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12959-b34f-7793-ae97-9dece6336e61 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a12968-bd54-7e42-add6-25f56ec40245 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a1296f-944f-75b1-9a85-459ba68c6feb | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12976-52fb-70f1-b0b8-5613697ae6a0 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a1297e-2ec3-7fb3-877c-703890291f7c | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12985-28c4-7602-8515-5ff9125ecbcf | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
