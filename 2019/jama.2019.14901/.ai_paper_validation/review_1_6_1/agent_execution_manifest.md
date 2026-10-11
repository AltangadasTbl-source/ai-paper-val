# Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a128da-3b69-7bb0-9554-2128186ea149 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a128da-f857-7961-9e0d-1495d8ad392c | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a128dc-ff7f-7141-8b09-40baa2432582 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a128dd-1b8f-7d40-98dd-4089fca540b7 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a128e0-6129-7883-87fc-83aefc195357 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a128e0-7bc2-7152-a260-a42c4a4fcd31 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a128e0-9c6c-75b0-bd7b-a4d7840873d2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a128e8-3ee6-74b0-9150-548d0b31afea | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a128ec-690f-7e03-a5dc-029f8535c3c2 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a128f0-78bd-77c1-be66-4735054846bc | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_coverage_auditor | 01a128f4-fe55-7b90-9ca7-0485ea5d80b0 | gpt-6.1-sol | high | FRESH_SPAWN | quality/coverage_integrity_audit.md |
| quality_control_auditor | 01a128f5-2ac8-7143-95a3-8ab7bc6b3e85 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a128f9-2907-7943-8fb5-26efdedbd5f0 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Post-assembly mechanical normalization was performed by the existing coordinator runtime listed above. No additional agent was spawned or repurposed; all scientific stage identities and model/effort pairs remain unchanged.
