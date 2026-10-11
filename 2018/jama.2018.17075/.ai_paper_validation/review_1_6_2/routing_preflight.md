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
- Checked UTC: 2026-10-11T06:39:51Z

Current-session turn metadata confirms model gpt-6.1-sol and reasoning effort high. The coordinator has completed an inference response. Package configuration contains no provider or authentication settings. Named roles are exposed by the current session with the required fixed pairs. Launch command above is the required workflow invocation; session metadata reports approval policy on-request, with the managed auto-review sandbox supplied by this session.

First mandatory specialist inference: PASS. The fresh named reuse-asset curator returned a substantive response under runtime thread ID 01a129b0-f753-7063-bd19-d468d23f6caf.

| Named preset | Model | Required effort | Observed effort | Verification |
|---|---|---|---|---|
| qc162_reuse_asset_curator | gpt-6.1-sol | medium | medium | PASS |
| qc162_main_quantitative_mapper | gpt-6.1-sol | medium | medium | PASS |
| qc162_support_quantitative_mapper | gpt-6.1-sol | medium | medium | PASS |
| qc162_numeric_consistency_reviewer | gpt-6.1-sol | medium | medium | PASS |
| qc162_cross_source_consistency_reviewer | gpt-6.1-sol | medium | medium | PASS |
| qc162_statistical_consistency_reviewer | gpt-6.1-sol | high | high | PASS |
| qc162_inclusion_screener | gpt-6.1-sol | high | high | PASS |
| qc162_evidence_rechecker | gpt-6.1-sol | high | high | PASS |
| qc162_quality_control_auditor | gpt-6.1-sol | high | high | PASS |
| qc162_report_generator | gpt-6.1-sol | medium | medium | PASS |
