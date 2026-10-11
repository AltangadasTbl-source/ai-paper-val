# Workflow 1.6 Routing Preflight

- Status: PASS
- Provider: openai
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
- Checked UTC: 2026-10-11T01:10:00Z

The user's instruction to use the current provider overrides the workflow's OpenRouter provider literal. Runtime session metadata confirms provider `openai`, source `cli`, model `gpt-6.1-sol`, and effort `high`; no provider configuration or authentication was changed. The launch-command field records the workflow's prescribed interactive invocation; actual command-line arguments are not exposed by the session metadata. Successful coordinator responses establish inference. First specialist inference must also succeed before scientific mapping proceeds.

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

All nine package TOML presets were read and their literal model and model_reasoning_effort pairs checked. The active collaboration tool exposes all nine named roles with matching fixed pairs.

First mandatory specialist inference: PASS. Asset curator runtime 01a12882-b157-7e53-b8e7-60587b3f254a produced complete durable inventories under the named gpt-6.1-sol/medium role. All 97 selected reused-artifact hashes and all five source hashes were recorded before mapping.
