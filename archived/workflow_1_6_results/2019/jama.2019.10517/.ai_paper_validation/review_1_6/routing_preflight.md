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
- Checked UTC: 2026-10-11T00:35:03Z

The provider deviation is expressly authorized by the user: "Use the current provider and document the deviation." The actual runtime provider is `openai`, confirmed from the current CLI session metadata; the package's configured provider is `openrouter`. This preflight passes the user-amended routing requirement, not the original provider requirement. The bundled validator hard-codes `openrouter`; any resulting provider-only validation failure must be reported honestly, without altering the validator or misreporting runtime provenance. The launch command above is the required workflow launch command; session metadata establishes CLI execution but does not independently establish its command-line arguments.

Runtime provenance: coordinator session `01a12860-cec4-7f22-bd5d-22a027867aab`; originator `codex-tui`; source `cli`; CLI version `0.162.1`; turn-context model `gpt-6.1-sol`; effort `high`. Successful coordinator responses confirm inference. The first specialist inference is checked before scientific mapping.

| Named preset | Required model | Required effort | File model | File effort | Result |
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

Authorized validation implementation: preserve and run the original bundled helper, then run a local copy whose only diff changes its expected Provider to openai. This applies the user's express routing authorization; original workflow controls remain unchanged. See validation/provider_exception.md and preserved final original result.
