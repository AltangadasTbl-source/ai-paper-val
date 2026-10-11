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
- Checked UTC: 2026-10-11T01:09:26Z

Current session metadata confirms codex-tui, cli, provider openai, model gpt-6.1-sol, effort high. The user explicitly requests the current provider; this overrides the template's openrouter provider. No provider or credential configuration is changed. Launch command above is the prescribed workflow command; current session CLI provenance is verified, but original launch flags are not exposed. Specialist inference will be confirmed by the curator's first response.

| Named preset | Model | Reasoning effort | Verification |
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

First mandatory specialist inference: PASS. Fresh curator runtime 01a12882-442a-79d1-a362-73e7476d942d responded successfully using its named gpt-6.1-sol/medium preset; its session metadata confirms provider openai. Coordinator and mapper runtime IDs are recorded in agent_execution_manifest.md from parent-matched session metadata.
