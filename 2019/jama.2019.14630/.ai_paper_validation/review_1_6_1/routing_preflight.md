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
- Checked UTC: 2026-10-11T02:46:06Z

Coordinator configuration is read from .codex/config.toml, as required by settings.toml. The successful interactive coordinator response establishes the current-session inference check. All ten presets are available as named collaboration roles and their model and effort declarations agree with the supplied preset files. The first mandatory specialist response will confirm specialist inference; any rejection will withdraw PASS before scientific mapping.

| Named preset | Model | Required effort | Preset effort | Result |
|---|---|---|---|---|
| qc161_reuse_asset_curator | gpt-6.1-sol | medium | medium | PASS |
| qc161_main_quantitative_mapper | gpt-6.1-sol | medium | medium | PASS |
| qc161_support_quantitative_mapper | gpt-6.1-sol | medium | medium | PASS |
| qc161_numeric_consistency_reviewer | gpt-6.1-sol | medium | medium | PASS |
| qc161_cross_source_consistency_reviewer | gpt-6.1-sol | medium | medium | PASS |
| qc161_statistical_consistency_reviewer | gpt-6.1-sol | high | high | PASS |
| qc161_inclusion_screener | gpt-6.1-sol | high | high | PASS |
| qc161_evidence_rechecker | gpt-6.1-sol | high | high | PASS |
| qc161_quality_control_auditor | gpt-6.1-sol | high | high | PASS |
| qc161_report_generator | gpt-6.1-sol | medium | medium | PASS |

First mandatory specialist inference: PASS. The fresh qc161_reuse_asset_curator agent root/asset_curator returned complete source/evidence inventories under the fixed named role, with specialist inference PASS. No fixed model rejection occurred.
