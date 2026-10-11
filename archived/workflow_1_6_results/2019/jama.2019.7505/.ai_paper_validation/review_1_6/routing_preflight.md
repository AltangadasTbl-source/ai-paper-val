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
- Checked UTC: 2026-10-11T00:35:12Z

## Authorized provider exception

The user explicitly answered "Use the current OpenAI provider" on 2026-10-11. The actual current-session metadata records originator codex-tui, source cli, model_provider openai, model gpt-6.1-sol, and effort high. Provider openai replaces the template's openrouter requirement only. The bundled validator is preserved unchanged; its raw output will be retained, with this exact authorized provider exception separately applied to the effective validation result. No model, effort, coverage, evidence, classification, or specialist-stage requirement is waived. The launch command above is the prescribed workflow launch command; session metadata establishes the interactive CLI origin, but does not retain its original argument list.

| Named preset | Required model | Required effort | Observed model | Observed effort | Result |
|---|---|---|---|---|---|
| qc16_reuse_asset_curator | gpt-6.1-sol | medium | gpt-6.1-sol | medium | PASS |
| qc16_main_quantitative_mapper | gpt-6.1-sol | medium | gpt-6.1-sol | medium | PASS |
| qc16_support_quantitative_mapper | gpt-6.1-sol | medium | gpt-6.1-sol | medium | PASS |
| qc16_numeric_consistency_reviewer | gpt-6.1-sol | medium | gpt-6.1-sol | medium | PASS |
| qc16_cross_source_consistency_reviewer | gpt-6.1-sol | medium | gpt-6.1-sol | medium | PASS |
| qc16_statistical_consistency_reviewer | gpt-6.1-sol | high | gpt-6.1-sol | high | PASS |
| qc16_evidence_rechecker | gpt-6.1-sol | high | gpt-6.1-sol | high | PASS |
| qc16_quality_control_auditor | gpt-6.1-sol | high | gpt-6.1-sol | high | PASS |
| qc16_report_generator | gpt-6.1-sol | medium | gpt-6.1-sol | medium | PASS |

All nine local TOML presets and exposed named agent roles match the required fixed model matrix. A successful coordinator response establishes coordinator inference. The first specialist's response will establish specialist inference before mapping begins.

Specialist inference: PASS. Fresh mandatory curator 01a12862-f7ad-7551-ab1e-66f2cc059ac9 returned a successful complete durable-artifact handoff under its named gpt-6.1-sol/medium preset. Main and support mappers subsequently responded successfully under their corresponding fixed presets.
