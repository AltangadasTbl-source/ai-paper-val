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
- Checked UTC: 2026-08-19T05:22:40Z
- Dynamic model aliases: NOT USED

The current interactive coordinator is pinned by `.codex/config.toml` to `gpt-5.6-sol` at `high` reasoning effort. Provider selection and credentials are not stored in the package configuration. All nine required named presets were read and verified before scientific review.

| Preset | Required model | Required effort | Verified |
|---|---|---|---|
| qc15_reuse_asset_curator | `gpt-5.6-terra` | `medium` | PASS |
| qc15_main_quantitative_mapper | `gpt-5.6-terra` | `medium` | PASS |
| qc15_support_quantitative_mapper | `gpt-5.6-terra` | `medium` | PASS |
| qc15_numeric_consistency_reviewer | `gpt-5.6-terra` | `medium` | PASS |
| qc15_cross_source_consistency_reviewer | `gpt-5.6-terra` | `medium` | PASS |
| qc15_statistical_consistency_reviewer | `gpt-5.6-terra` | `high` | PASS |
| qc15_evidence_rechecker | `gpt-5.6-sol` | `high` | PASS |
| qc15_quality_control_auditor | `gpt-5.6-sol` | `high` | PASS |
| qc15_report_generator | `gpt-5.6-terra` | `medium` | PASS |

The two mandatory statistical passes will use separate fresh runtimes of the statistical preset. Every other mandatory stage will likewise use a fresh runtime and the fixed pair shown above.
