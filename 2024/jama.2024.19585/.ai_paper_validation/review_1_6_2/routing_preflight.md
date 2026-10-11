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
- Checked UTC: 2026-10-11T06:37:23Z

The current interactive CLI turn context records model gpt-6.1-sol and effort high. The coordinator has obtained an inference response. Project configuration and each of the ten named preset files were inspected directly; all agree with the fixed matrix. First mandatory specialist inference will be checked before scientific mapping. The launch command above is the workflow-required command; session metadata confirms CLI execution but does not independently retain launch arguments.

| Named preset | Model | Reasoning effort | Verification |
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

First mandatory specialist inference: PASS. The fresh asset curator responded successfully using the named gpt-6.1-sol/medium preset, runtime thread 01a129ae-95bc-7d71-a296-14fdb6208bc0. Scientific mapping may proceed after its inventories and before-hash records are complete.

Runtime routing confirmation: the latest specialist turn contexts for curator 01a129ae-95bc-7d71-a296-14fdb6208bc0, main mapper 01a129b1-193e-71e0-bfc4-ffd8db937dad, and support mapper 01a129b1-36ec-7cb2-ba29-5f29a1a78ec6 each record gpt-6.1-sol/medium. Inherited coordinator contexts were distinguished from actual fresh specialist turns.

Checker runtime routing confirmation: the latest fresh turn contexts record numeric reviewer 01a129b5-e322-7ff1-a198-947ffd0e507e and cross-source reviewer 01a129b6-079a-7e33-a3bd-a948d6575855 at gpt-6.1-sol/medium, and statistical pass 1 reviewer 01a129b6-3a3f-7742-b588-3b9736635a69 at gpt-6.1-sol/high.

Actual fresh runtime model/effort checks through the quality-audit stage: PASS for every recorded coordinator and specialist thread. Full per-runtime evidence is in routing_runtime_checks.md. The report-generator runtime will be appended after its fresh spawn.
