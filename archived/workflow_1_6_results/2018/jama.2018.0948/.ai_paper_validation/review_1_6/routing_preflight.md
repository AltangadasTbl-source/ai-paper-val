# Workflow 1.6 Routing Preflight

- Status: PASS
- Provider: current-session-provider
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
- Checked UTC: 2026-10-11T00:43:40Z

Provider follows the explicit current-user override; no provider configuration or credentials changed. Coordinator model/effort and launch command above describe the package's configured interactive contract. The available session does not expose independent runtime model or launch-command attestation; the coordinator has responded successfully. Specialist tools expose the required named role presets and fixed model/effort pairs. The original validator expects openrouter literally and may therefore report a provider-only conflict with the user override. This caveat must remain visible in final metadata.

| Preset | Model | Reasoning effort | Result |
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

First mandatory specialist inference: PASS; fresh named curator /root/curator completed a model response and durable inventory. Named mapper, numeric, cross-source, and statistical-pass-1 roles subsequently completed under their tool-defined fixed presets. Runtime identifiers are exact canonical task paths returned by the collaboration tool; opaque UUIDs are not exposed.
