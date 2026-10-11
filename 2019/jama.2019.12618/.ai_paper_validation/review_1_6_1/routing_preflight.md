# Workflow 1.6.1 Routing Preflight

- Status: PASS
- Provider: CURRENT_SESSION
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
- Checked UTC: 2026-10-11T02:45:41Z

The package project configuration fixes the coordinator pair. The current interactive response supplies the coordinator inference check. All ten local presets were read and compared with the required matrix; the ten named role tools are available. Provider configuration is unchanged.

| Named preset | Model | Reasoning effort | Verification |
|---|---|---|---|
| qc161_reuse_asset_curator | gpt-6.1-sol | medium | PASS |
| qc161_main_quantitative_mapper | gpt-6.1-sol | medium | PASS |
| qc161_support_quantitative_mapper | gpt-6.1-sol | medium | PASS |
| qc161_numeric_consistency_reviewer | gpt-6.1-sol | medium | PASS |
| qc161_cross_source_consistency_reviewer | gpt-6.1-sol | medium | PASS |
| qc161_statistical_consistency_reviewer | gpt-6.1-sol | high | PASS |
| qc161_inclusion_screener | gpt-6.1-sol | high | PASS |
| qc161_evidence_rechecker | gpt-6.1-sol | high | PASS |
| qc161_quality_control_auditor | gpt-6.1-sol | high | PASS |
| qc161_report_generator | gpt-6.1-sol | medium | PASS |

First mandatory specialist inference confirmation: PASS. The fresh qc161_reuse_asset_curator returned its completed durable source and evidence inventory under canonical runtime task /root/curator.
