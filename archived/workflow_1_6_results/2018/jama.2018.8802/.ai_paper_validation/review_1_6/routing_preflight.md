# Workflow 1.6 Routing Preflight

- Status: PASS
- Provider: current session provider (explicit user override)
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
- Checked UTC: 2026-10-11T00:44:03Z

The active interactive session successfully produced the initial response. The package coordinator configuration specifies gpt-6.1-sol/high. Specialist presets exposed by the runtime match all nine local presets. Provider selection remains inherited from this session; the user's current-provider instruction overrides the workflow's OpenRouter default. No credentials were read and no provider settings were changed. A selective check for user-level provider-name fields returned no explicit provider name; current-session inheritance is therefore recorded without guessing a provider identity. The launch command above records the workflow launch contract; no nested CLI was launched.

| Named preset | Required model | Required effort | Result |
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

Mandatory first specialist response: PASS. Fresh curator runtime root/curator completed the artifact handoff under the named gpt-6.1-sol/medium preset. Runtime identifiers in the manifest omit only the leading slash of canonical task names to satisfy the validator's identifier syntax.
