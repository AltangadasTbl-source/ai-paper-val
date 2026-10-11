# Workflow 1.6.2 Agent Execution Manifest

The runtime API exposes canonical task identities rather than separate opaque identifiers. Rows record those exact identities with the leading slash omitted for validator syntax; `root` denotes the current coordinator. Every specialist identity was freshly spawned once for the listed stage.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_extra | root/support_mapper_extra | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_002.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_results_extra | root/numeric_results_extra | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_results_extra.md |
| numeric_consistency_reviewer_plan_extra | root/numeric_plan_extra | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_plan_extra.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_extra | root/statistical_pass1_extra | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass1_extra.md |
| inclusion_screener | root/inclusion_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_main_extra | root/statistical_pass2_main_extra | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass2_02.md |
| statistics_pass_2_extra_a | root/statistical_pass2_extra_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass2_03.md |
| statistics_pass_2_extra_b | root/statistical_pass2_extra_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass2_04.md |
| statistics_pass_2_extra_c | root/statistical_pass2_extra_c | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass2_05.md |
| statistics_pass_2_extra_d | root/statistical_pass2_extra_d | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass2_06.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
