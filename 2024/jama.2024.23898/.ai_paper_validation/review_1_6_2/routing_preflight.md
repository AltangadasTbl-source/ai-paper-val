# Workflow 1.6.2 Routing Preflight

- Status: PASS
- Provider: CURRENT_SESSION
- Run model: gpt-6.1-sol
- Run model source: DEFAULT
- Coordinator model: gpt-6.1-sol
- Coordinator reasoning effort: high
- Ordinary specialist model: gpt-6.1-sol
- Ordinary specialist reasoning effort: medium
- Statistical specialist model: gpt-6.1-sol
- Statistical specialist reasoning effort: high
- Screening, recheck, and audit specialist model: gpt-6.1-sol
- Screening, recheck, and audit specialist reasoning effort: high
- Fixed model matrix: PASS
- Named agent presets: PASS
- Named agent preset count: 10
- Mandatory specialist stages: 11
- Mandatory agent start contract: FRESH_DISTINCT
- Coordinator inference: PASS
- Execution mode: INTERACTIVE_CLI
- Launch command: codex --approve-for-me
- Checked UTC: 2026-10-11T06:37:33Z

Coordinator runtime turn metadata confirms gpt-6.1-sol with high effort in the current package. All ten presets were read and their model/effort pairs verified. First specialist inference confirmed by runtime 01a129ae-ba27-7791-aa58-c6a840206264 using the named curator preset.

| Named preset | Model | Required effort | Verification |
|---|---|---|---|
| qc162_reuse_asset_curator | gpt-6.1-sol | medium | PASS |
| qc162_main_quantitative_mapper | gpt-6.1-sol | medium | PASS |
| qc162_support_quantitative_mapper | gpt-6.1-sol | medium | PASS |
| qc162_numeric_consistency_reviewer | gpt-6.1-sol | medium | PASS |
| qc162_cross_source_consistency_reviewer | gpt-6.1-sol | medium | PASS |
| qc162_statistical_consistency_reviewer | gpt-6.1-sol | high | PASS |
| qc162_inclusion_screener | gpt-6.1-sol | high | PASS |
| qc162_evidence_rechecker | gpt-6.1-sol | high | PASS |
| qc162_quality_control_auditor | gpt-6.1-sol | high | PASS |
| qc162_report_generator | gpt-6.1-sol | medium | PASS |
