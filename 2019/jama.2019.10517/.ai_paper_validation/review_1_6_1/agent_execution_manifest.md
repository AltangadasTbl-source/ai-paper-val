# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a128d9-a47a-7bc0-923d-93b713cb413d | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a128da-514a-7621-aecc-501c34ed647e | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a128dc-926b-7a82-afaf-ecf5979714d5 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a128dc-b0b1-7732-a436-11caded5ed10 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_part_2 | 01a128dc-c8fe-7331-af32-86f9549a95bd | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_part_2.md |
| numeric_consistency_reviewer | 01a128e0-2fbf-77f3-984e-57bcaa473d9b | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a128e0-4895-7462-a9b3-56b2a6829db4 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a128e0-66b3-7712-a4ca-02deb3251b1f | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a128e6-6a07-77c2-b638-35eb9cc1bf9d | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a128e9-2d33-7973-9e79-24863cbc6ab4 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a128ec-6356-7b23-be7b-9115db681a2b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor_mapping_coverage | 01a128ed-a118-7e10-acc8-30a8588fcb41 | gpt-6.1-sol | high | FRESH_SPAWN | quality/mapping_coverage_audit.md |
| quality_control_auditor | 01a128f1-d646-7e31-a992-ec2915bbbead | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a128f5-b60f-7283-aaa7-c589054ee727 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
