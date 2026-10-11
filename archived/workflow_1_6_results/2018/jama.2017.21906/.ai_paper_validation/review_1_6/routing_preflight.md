# Workflow 1.6 Routing Preflight

- Status: PASS
- Provider: current session provider (user override; no provider change)
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
- Launch command: current interactive session (user authorized continuation)
- Checked UTC: 2026-10-11T00:43:38Z

The package config fixes the coordinator model and effort. The current interactive response succeeded. The user explicitly requests the current provider rather than the provider named in workflow settings. No authentication or provider configuration was changed. Configured named roles are available in this runtime; each mandatory stage will use a fresh named role.

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

Runtime confirmation: the first mandatory qc16_reuse_asset_curator returned a successful complete model response under its named preset; main and support named mappers have also returned substantive progress responses. The fixed-model specialist inference check therefore succeeded.
