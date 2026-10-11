# Workflow 1.6.2 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129af-68b6-7e42-a754-cf9af7ad7441 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a129b0-e282-71e3-a1f6-409da964d142 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a129b4-3791-7603-a1a4-8c610dfdecaf | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a129b4-5b29-7571-a033-f4edc42e6311 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_1 | 01a129b4-7c84-7f70-89f1-d9e06894b991 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_001_032.md |
| support_quantitative_mapper_shard_2 | 01a129b4-9407-7911-8acb-78005de23e07 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_033_064.md |
| support_quantitative_mapper_shard_3 | 01a129b4-ab4c-7ca2-8493-423476e266b5 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_065_094.md |
| numeric_consistency_reviewer | 01a129b8-e16e-7732-8986-717ce7785e24 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a129b9-0d28-70a3-a6a4-0dc8194fcb34 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a129b9-3c75-7c50-8787-4de976dc68d0 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a129ca-c991-7a90-b0ad-3686288f164b | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a129d3-409c-71e2-ad6d-92edf3038cd4 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a129db-13d2-7fe1-a704-4db0b539bac8 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_shard_support | 01a129db-42fe-7702-a208-6cf2e0d12816 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_s061_s099.md |
| quality_control_auditor | 01a129e2-d0f7-7da1-8dc5-7c2d0b2ec94b | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_shard_support | 01a129e3-1015-7543-8dd4-18036273576e | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/evidence_quality_c009_c016.md |
| report_generator | 01a129ec-e15a-73b1-98b8-a4d29010abef | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
