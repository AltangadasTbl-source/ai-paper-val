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
- Checked UTC: 2026-10-11T00:35:27Z

The user explicitly authorized the current provider with "use the current provider" after the runtime provider mismatch was reported. The current provider is openai, established by the current session's session_meta record. This authorization overrides the package's openrouter provider requirement. The current turn_context records model gpt-6.1-sol and reasoning effort high. The successful current response supplies the coordinator inference check. Runtime session ID: 01a1285f-83e8-7ef3-b9e5-9fcd3cdb90c9. Actual approval policy is on-request with approvals_reviewer auto_review and workspace-write sandbox; `codex --help` confirms this is the operating mode selected by --approve-for-me. The launch-command field records that mode-equivalent command; literal original launch arguments are not observable in the sandbox. First mandatory specialist inference: PASS, runtime 01a12863-2f29-7e90-89c6-5dacc138b8f9, successfully completed curation at gpt-6.1-sol/medium.

The supplied validator hard-codes openrouter. The user's explicit current-provider instruction is applied mechanically to a run-local copy of that same supplied auxiliary helper at validation/validate_review.py: the sole change is the expected Provider value from openrouter to openai. All scientific, coverage, integrity, classification, model, effort, fresh-agent, timing, report, and link checks remain identical. The original workflow helper and all package controls remain unchanged. The exact one-line diff and both validator hashes are retained. Final validation will run the original helper first and preserve its result as validation/strict_default_provider_validation.json, then run the provider-adapted supplied helper to produce review_validation.json. Any non-provider defect must be repaired; a strict-default-provider failure is not represented as a strict-profile PASS.

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
