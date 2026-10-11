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
- Checked UTC: 2026-10-11T00:35:10Z

## User-authorized provider override

The user explicitly instructed: "use the current provider". Active runtime metadata records provider `openai`, model `gpt-6.1-sol`, effort `high`, originator `codex-tui`, source `cli`, and session ID `01a1285e-f91a-72f0-948c-939d2c0abf5e`. The provider override supersedes the workflow's `openrouter` requirement for this run only. All scientific, model, effort, coverage, integrity, and fresh-agent requirements remain applicable. Runtime evidence is stored in `routing_runtime_evidence.json`.

The launch-command field records the workflow-required command; runtime metadata independently establishes interactive CLI execution but does not preserve shell launch flags. The supplied validator hardcodes `openrouter`; its unmodified result will be preserved separately, and any provider-aware validation will disclose its sole authorized adjustment.

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
