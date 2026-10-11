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
- Checked UTC: 2026-10-11T02:44:22Z

Current session ID: 01a128d7-ced6-7203-913d-d0bb174814ae. The session turn-context record confirms model gpt-6.1-sol and effort high; the coordinator has returned successful responses. All ten presets were read from .codex/agents and agree with the exposed named runtime roles. Provider configuration was preserved. The launch command above is the workflow launch contract; process launch arguments are not exposed by this execution sandbox.

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

First mandatory specialist inference: PASS. Fresh curator runtime 01a128d9-3d06-70d2-a1d0-5ccead0a7851 completed its assigned artifact handoff successfully under the configured named preset. No fixed model was rejected.
