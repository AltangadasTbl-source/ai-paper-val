# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129af-1ec4-7720-b6cf-129f70cefd34 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a129b0-1b24-7ef1-a2a1-116873575442 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a129b3-3321-7fb1-bfa9-ab1f615ea3ff | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a129b3-5402-7d02-a860-33eb6970b900 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_sap_results_shard | 01a129b3-7125-73e0-8869-d73f37059c71 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap_results_evidence.md |
| numeric_consistency_reviewer | 01a129b7-ee71-7271-9299-3cf9a52ee2fb | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_support_shard | 01a129b8-0e37-7521-8c6c-85aed6ede96e | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| cross_source_consistency_reviewer | 01a129b8-3f5d-7cd0-8dc6-3c2fc4520907 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a129b8-6855-71c1-b172-2ba0b43344ac | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a129c3-6696-7d12-977a-068c52ecf636 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a129cc-2272-79d1-9061-1f09b51d95da | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a129d4-6f76-7300-8ad1-ce7a40e618ed | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a129d7-9bcf-7790-a704-cb45d937f09c | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_candidates_007_012_shard | 01a129d7-cf6c-7eb2-816d-a0a5052afa02 | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/candidates_007_012_audit.md |
| report_generator | 01a129df-768d-7f52-9c10-15f13ea7e371 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
