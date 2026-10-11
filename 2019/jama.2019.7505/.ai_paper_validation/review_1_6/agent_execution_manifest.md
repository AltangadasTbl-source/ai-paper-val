# Workflow 1.6 Agent Execution Manifest

Actual provider: openai, expressly authorized by the user. All models and efforts retain the fixed Workflow 1.6 contract.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12860-4d9e-7813-a9cd-5dbb5c6af8bd | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12862-f7ad-7551-ab1e-66f2cc059ac9 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12865-83bc-7193-a84f-4b50723c87df | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12865-a268-78b2-a07f-00e0c025a3f4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_results_mapper | 01a12865-c12b-7a31-89c7-c49c23109703 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_results.md |
| statistics_pass_1_tables | 01a12869-c9f0-7231-9b70-dfd2c3c00bcf | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_tables.md |
| statistics_pass_1 | 01a1286a-7f32-78f0-97b4-3d1c28e5d86a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_planplots | 01a1286a-aaa7-7290-810f-a2d4d4fd7c2d | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_planplots.md |
| numeric_consistency_reviewer | 01a1286a-d1a0-78a3-b596-ad02e44f539b | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_outcomes_reviewer | 01a1286a-f70e-7670-b0f7-a0db7e2ab04a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_outcomes.md |
| cross_source_consistency_reviewer | 01a1286b-1eb0-7130-a796-b8279d3825a7 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1_physiology | 01a1286e-45eb-7ef2-8182-8840841190aa | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_physiology.md |
| numeric_support_tables | 01a1286e-c7cc-7cd0-a901-f092deade378 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support_tables.md |
| numeric_planplots | 01a1286f-0335-7023-bd65-6ab8f678399d | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_planplots.md |
| candidate_merge_assistant | 01a12870-972e-7163-b211-c2c7bad04043 | gpt-6.1-sol | medium | FRESH_SPAWN | registration/merged_ledger_draft.md |
| evidence_rechecker | 01a12876-834d-72c3-aa7a-72e0443797df | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| evidence_rechecker_002 | 01a12876-ab30-7b53-8bfc-b7bc2088a3a9 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_002.md |
| evidence_rechecker_003 | 01a12876-d8b5-7051-8ce1-2e81d211e001 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_003.md |
| statistics_pass_2 | 01a1287e-9c64-7632-9439-3c68158cf2a8 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_tables | 01a1287e-ba43-7b21-b1b2-b2d070518e84 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_tables.md |
| statistics_pass_2_planplots | 01a1287e-d520-7c43-b095-ff4a2a023a37 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_planplots.md |
| statistics_pass_2_physiology | 01a1287e-ec48-7660-9bfb-6580f407aaac | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_physiology.md |
| quality_control_auditor | 01a12883-e976-7ed2-b7e6-12b82f985685 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_002 | 01a12884-0826-7953-abc6-b66e49bc9867 | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/evidence_quality_audit_002.md |
| quality_control_auditor_003 | 01a12884-27d8-78e0-9cf7-2f6ace5503dc | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/evidence_quality_audit_003.md |
| quality_control_auditor_004 | 01a12884-46a0-7540-a1ce-6ae64caf97fc | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/evidence_quality_audit_004.md |
| report_cards_001 | 01a12889-1b3f-7ea2-9cb1-75a3e13d3495 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/cards_001.md |
| report_cards_002 | 01a12889-42cd-7782-b77c-75adabac90a5 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/cards_002.md |
| report_cards_003 | 01a12889-621a-7b00-ab47-d0b441e27a72 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/cards_003.md |
| report_cards_004 | 01a12889-8865-73b1-aa1b-031dd60ca7b4 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/cards_004.md |
| report_generator | 01a1288a-1b2a-7372-a4ff-91c17b5e1e75 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
