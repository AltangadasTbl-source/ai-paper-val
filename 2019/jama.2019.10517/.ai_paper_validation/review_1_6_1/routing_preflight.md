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
- Checked UTC: 2026-10-11T02:45:51Z

Coordinator model and effort confirmed from the current CLI turn context; successful coordinator response confirms inference. Project config and every bundled named preset were read. No provider configuration was changed.

| Named preset | Model | Reasoning effort | Check |
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

The first mandatory named specialist returned a model response under the verified gpt-6.1-sol/medium preset; its fresh runtime ID is recorded in agent_execution_manifest.md. Subsequent mandatory stages use their corresponding named fixed presets.
