# Workflow 1.5.3 Routing Preflight

- Status: PASS
- Provider: openrouter
- Coordinator model: gpt-5.6-sol
- Coordinator reasoning effort: high
- Ordinary specialist model: gpt-5.6-terra
- Ordinary specialist reasoning effort: medium
- Statistical specialist model: gpt-5.6-terra
- Statistical specialist reasoning effort: high
- Sol specialist model: gpt-5.6-sol
- Sol specialist reasoning effort: high
- Fixed model matrix: PASS
- Named agent presets: PASS
- Named agent preset count: 9
- Mandatory specialist stages: 10
- Mandatory agent start contract: FRESH_DISTINCT
- Coordinator inference: PASS
- Execution mode: INTERACTIVE_CLI
- Launch command: codex --approve-for-me
- Checked UTC: 2026-08-19T04:33:27Z

- **Status:** PASS
- **Verified UTC:** 2026-08-19T04:33:27Z
- **Execution mode:** INTERACTIVE_CLI
- **Coordinator model:** gpt-5.6-sol
- **Coordinator reasoning effort:** high
- **Coordinator inference:** PASS
- **Named agent presets:** PASS

The current interactive coordinator produced a successful model response under the package-local
`gpt-5.6-sol`/`high` configuration. Provider selection and authentication remain outside the
package-local configuration.

| Named preset | Required model | Required effort | Configured model | Configured effort | Verification |
|---|---|---|---|---|---|
| qc15_reuse_asset_curator | gpt-5.6-terra | medium | gpt-5.6-terra | medium | PASS |
| qc15_main_quantitative_mapper | gpt-5.6-terra | medium | gpt-5.6-terra | medium | PASS |
| qc15_support_quantitative_mapper | gpt-5.6-terra | medium | gpt-5.6-terra | medium | PASS |
| qc15_numeric_consistency_reviewer | gpt-5.6-terra | medium | gpt-5.6-terra | medium | PASS |
| qc15_cross_source_consistency_reviewer | gpt-5.6-terra | medium | gpt-5.6-terra | medium | PASS |
| qc15_statistical_consistency_reviewer | gpt-5.6-terra | high | gpt-5.6-terra | high | PASS |
| qc15_evidence_rechecker | gpt-5.6-sol | high | gpt-5.6-sol | high | PASS |
| qc15_quality_control_auditor | gpt-5.6-sol | high | gpt-5.6-sol | high | PASS |
| qc15_report_generator | gpt-5.6-terra | medium | gpt-5.6-terra | medium | PASS |

All nine named agent presets were verified against their required fixed model and reasoning-effort
pairs. No moving model alias or shell launcher is used.
