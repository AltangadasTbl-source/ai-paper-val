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
- Checked UTC: 2026-10-11T02:52:35Z

Coordinator routing is pinned by the supplied project configuration; the current interactive coordinator has produced a response. All ten local presets and matching callable custom agent types are available. First-specialist inference will be checked before scientific mapping.

| Named preset | Model | Required effort | Preset effort | Verification |
|---|---|---|---|---|
| qc161_cross_source_consistency_reviewer | gpt-6.1-sol | medium | medium | PASS |
| qc161_evidence_rechecker | gpt-6.1-sol | high | high | PASS |
| qc161_inclusion_screener | gpt-6.1-sol | high | high | PASS |
| qc161_main_quantitative_mapper | gpt-6.1-sol | medium | medium | PASS |
| qc161_numeric_consistency_reviewer | gpt-6.1-sol | medium | medium | PASS |
| qc161_quality_control_auditor | gpt-6.1-sol | high | high | PASS |
| qc161_report_generator | gpt-6.1-sol | medium | medium | PASS |
| qc161_reuse_asset_curator | gpt-6.1-sol | medium | medium | PASS |
| qc161_statistical_consistency_reviewer | gpt-6.1-sol | high | high | PASS |
| qc161_support_quantitative_mapper | gpt-6.1-sol | medium | medium | PASS |

First mandatory specialist inference: PASS. The fresh configured asset curator root/curator completed its response and durable curation artifacts under gpt-6.1-sol/medium. No fixed model rejection occurred.
