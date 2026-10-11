# Workflow 1.6 Routing Preflight

- Status: PASS
- Provider: current session provider
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
- Checked UTC: 2026-10-11T00:43:43Z

The user overrides the workflow's provider selection: use the current provider. No provider or credential configuration was changed. Coordinator model/effort are those configured in package .codex/config.toml; inference is evidenced by this active responding session. The execution mode and launch command above describe the required interactive workflow contract; this review is executed in the supplied active session, without invoking a shell launcher or codex exec.

| Named agent preset | Model | Reasoning effort | Result |
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

First mandatory specialist inference: PASS. The fresh qc16_reuse_asset_curator returned complete durable artifacts using its configured gpt-6.1-sol/medium preset; five support mapping agents and one main mapping agent were then spawned under their named presets. Runtime handles returned by the collaboration API are retained verbatim, including their leading slash.
