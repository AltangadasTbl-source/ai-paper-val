# Workflow 1.6 Agent Execution Manifest

Coordinator model/effort is the package-configured contract; runtime identity is the current root session. Named specialist pairs are tool-defined. Provider remains the current session provider by user instruction.

Identifier encoding: the collaboration tool returns canonical runtime task paths such as /root/curator, and does not expose opaque UUIDs. The Agent ID column stores those unique paths with the leading slash omitted to satisfy the supplied validator's alphanumeric-first identifier grammar. Prepending / recovers each exact returned identifier; no agent identity is invented or reused. The current coordinator's exact identifier is /root. All named specialist model/effort pairs are tool-defined. The coordinator row reports its package-configured contract; independent runtime model/launch attestation is unavailable.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/stats1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | root/recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/stats2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_rechecker_append | root/recheck_append | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_append.md |
| quality_control_auditor | root/audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
