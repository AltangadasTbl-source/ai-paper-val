# Workflow 1.6 Routing Preflight

- Status: PASS_WITH_USER_OVERRIDE
- Provider: CURRENT_SESSION_PROVIDER
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
- Execution mode: CURRENT_INTERACTIVE_SESSION
- Launch command: Current user-provided interactive session
- Checked UTC: 2026-10-11T00:43:54Z

The user explicitly directs use of the current provider even where workflow controls specify openrouter. No provider or authentication configuration was changed. The coordinator model/effort above are the package configuration contract; this API interface does not expose independent runtime model attestation. The interactive session launch command cannot be independently established and is not fabricated. Named specialist presets are exposed by the collaboration tool with the exact following pairs. The original validator hard-codes openrouter and INTERACTIVE_CLI and may reject this authorized execution-context override; preserve and disclose any such result.

| Named preset | Required model | Required effort | Package preset | Tool preset | Result |
|---|---|---|---|---|---|
| qc16_reuse_asset_curator | gpt-6.1-sol | medium | matched | matched | PASS |
| qc16_main_quantitative_mapper | gpt-6.1-sol | medium | matched | matched | PASS |
| qc16_support_quantitative_mapper | gpt-6.1-sol | medium | matched | matched | PASS |
| qc16_numeric_consistency_reviewer | gpt-6.1-sol | medium | matched | matched | PASS |
| qc16_cross_source_consistency_reviewer | gpt-6.1-sol | medium | matched | matched | PASS |
| qc16_statistical_consistency_reviewer | gpt-6.1-sol | high | matched | matched | PASS |
| qc16_evidence_rechecker | gpt-6.1-sol | high | matched | matched | PASS |
| qc16_quality_control_auditor | gpt-6.1-sol | high | matched | matched | PASS |
| qc16_report_generator | gpt-6.1-sol | medium | matched | matched | PASS |

Inference evidence: the current coordinator produced tool/model responses, and the first mandatory named specialist task /root/asset_curator successfully returned complete curation artifacts. Every subsequently recorded named-role spawn also returned a model response. No fixed named specialist model was rejected. Provider configuration was never changed.
