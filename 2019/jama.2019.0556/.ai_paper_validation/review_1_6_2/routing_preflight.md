# Workflow 1.6.2 Routing Preflight

- Status: PASS
- Provider: CURRENT_SESSION
- Run model: gpt-6.1-sol
- Run model source: DEFAULT
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
- Checked UTC: 2026-10-11T04:53:35Z

The project configuration pins the coordinator pair. The current interactive coordinator has produced a response using CURRENT_SESSION authentication. All ten configured named roles are available in the collaboration tool. First mandatory specialist inference is checked before scientific mapping.

| Named preset | Model | Reasoning effort | Verification |
|---|---|---|---|
| qc162_reuse_asset_curator | gpt-6.1-sol | medium | PASS |
| qc162_main_quantitative_mapper | gpt-6.1-sol | medium | PASS |
| qc162_support_quantitative_mapper | gpt-6.1-sol | medium | PASS |
| qc162_numeric_consistency_reviewer | gpt-6.1-sol | medium | PASS |
| qc162_cross_source_consistency_reviewer | gpt-6.1-sol | medium | PASS |
| qc162_statistical_consistency_reviewer | gpt-6.1-sol | high | PASS |
| qc162_inclusion_screener | gpt-6.1-sol | high | PASS |
| qc162_evidence_rechecker | gpt-6.1-sol | high | PASS |
| qc162_quality_control_auditor | gpt-6.1-sol | high | PASS |
| qc162_report_generator | gpt-6.1-sol | medium | PASS |

First mandatory specialist inference: PASS. Fresh curator runtime 01a1294f-7de7-7a21-9364-2665933d201e responded under named gpt-6.1-sol/medium preset before scientific mapping.
