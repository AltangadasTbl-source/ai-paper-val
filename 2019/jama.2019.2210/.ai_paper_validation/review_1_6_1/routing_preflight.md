# Workflow 1.6.1 Routing Preflight

- Status: PASS
- Provider: CURRENT_SESSION
- Coordinator model: gpt-6.1-sol
- Coordinator reasoning effort: high
- Ordinary specialist model: gpt-6.1-sol
- Ordinary specialist reasoning effort: medium
- Statistical specialist model: gpt-6.1-sol
- Statistical specialist reasoning effort: high
- Screening, recheck, and audit specialist model: gpt-6.1-sol
- Screening, recheck, and audit specialist reasoning effort: high
- Fixed model matrix: PASS
- Named agent presets: PASS
- Named agent preset count: 10
- Mandatory specialist stages: 11
- Mandatory agent start contract: FRESH_DISTINCT
- Coordinator inference: PASS
- Execution mode: INTERACTIVE_CLI
- Launch command: codex --approve-for-me
- Checked UTC: 2026-10-11T02:44:55Z

Runtime session metadata confirms originator codex-tui, source cli, current model gpt-6.1-sol, and effort high. Coordinator inference succeeded in this interactive session. The launch command above is the prescribed workflow command; session metadata does not independently expose command-line flags. Project configuration and all ten presets were read without modification. Mandatory specialist inference must succeed before scientific mapping.

| Named preset | Model | Reasoning effort | Verification |
|---|---|---|---|
| qc161_reuse_asset_curator | gpt-6.1-sol | medium | PASS |
| qc161_main_quantitative_mapper | gpt-6.1-sol | medium | PASS |
| qc161_support_quantitative_mapper | gpt-6.1-sol | medium | PASS |
| qc161_numeric_consistency_reviewer | gpt-6.1-sol | medium | PASS |
| qc161_cross_source_consistency_reviewer | gpt-6.1-sol | medium | PASS |
| qc161_statistical_consistency_reviewer | gpt-6.1-sol | high | PASS |
| qc161_inclusion_screener | gpt-6.1-sol | high | PASS |
| qc161_evidence_rechecker | gpt-6.1-sol | high | PASS |
| qc161_quality_control_auditor | gpt-6.1-sol | high | PASS |
| qc161_report_generator | gpt-6.1-sol | medium | PASS |

First mandatory specialist inference succeeded: qc161_reuse_asset_curator, runtime 01a128d9-d279-7230-bdc2-0057dee243ae, gpt-6.1-sol/medium. No fixed model rejection occurred.

Runtime routing confirmation: the latest own-agent turn_context metadata for the coordinator and the first eight specialists was inspected. All use exact model gpt-6.1-sol; curator, mappers, numeric and cross-source reviewers use medium, and statistical pass1 uses high. Inherited parent-history contexts were excluded from this check.

Final runtime routing confirmation: latest own-agent turn_context metadata was inspected for every manifest runtime, comprising the coordinator and all thirteen fresh specialists, including the report generator. All fourteen model/effort pairs match the fixed role contract: exact gpt-6.1-sol, medium for ordinary specialists and report generation, and high for the coordinator, both statistical passes, screening, recheck and audit. Runtime routing: PASS. Each mandatory specialist stage has a distinct fresh runtime ID.
