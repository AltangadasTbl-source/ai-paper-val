# Workflow 1.6 Routing Preflight

- Status: PASS
- Provider: openrouter
- Coordinator model: gpt-6.1-sol
- Coordinator reasoning effort: high
- Ordinary specialist model: gpt-6.1-sol
- Ordinary specialist reasoning effort: medium
- Statistical specialist model: gpt-6.1-sol
- Statistical specialist reasoning effort: high
- Recheck and audit specialist model: gpt-6.1-sol
- Recheck and audit specialist reasoning effort: high
- Fixed model matrix: PASS
- Named agent presets: PASS
- Named agent preset count: 9
- Mandatory specialist stages: 10
- Mandatory agent start contract: FRESH_DISTINCT
- Coordinator inference: PASS
- Execution mode: INTERACTIVE_CLI
- Launch command: codex --approve-for-me
- Checked UTC: 2026-10-11T00:34:04Z

The current interactive coordinator produced a successful response. The package configuration pins the coordinator to gpt-6.1-sol/high. All nine supplied presets and available named runtime roles agree with the matrix below. No configuration was rewritten. Specialist inference is confirmed by its first durable handoff; any routing rejection requires this status to be revised.

| Named preset | Model | Reasoning effort | Check |
|---|---|---|---|
| qc16_reuse_asset_curator | gpt-6.1-sol | medium | PASS |
| qc16_main_quantitative_mapper | gpt-6.1-sol | medium | PASS |
| qc16_support_quantitative_mapper | gpt-6.1-sol | medium | PASS |
| qc16_numeric_consistency_reviewer | gpt-6.1-sol | medium | PASS |
| qc16_cross_source_consistency_reviewer | gpt-6.1-sol | medium | PASS |
| qc16_statistical_consistency_reviewer | gpt-6.1-sol | high | PASS |
| qc16_evidence_rechecker | gpt-6.1-sol | high | PASS |
| qc16_quality_control_auditor | gpt-6.1-sol | high | PASS |
| qc16_report_generator | gpt-6.1-sol | medium | PASS |

## User provider override

The user instructed: "use the current provider". The coordinator and every specialist retain the active session's inherited provider and authentication. No provider configuration or credentials are changed. The collaboration runtime does not expose an effective provider name. The `Provider: openrouter` line above records the bundled validator's required workflow schema value, not an independently verified effective provider identity; the user override takes precedence over that workflow preference. Successful runtime inference and fixed model/effort presets are checked independently of provider identity.
