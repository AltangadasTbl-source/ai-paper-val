# Token Usage and Token-Only Cost Summary

- **Accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Accounting basis:** TOKEN_ONLY_API_EQUIVALENT_ESTIMATE
- **Pricing as of UTC:** 2026-08-18T00:00:00Z
- **Pricing source:** https://developers.openai.com/api/docs/pricing
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

Cached-input and cache-write tokens are subsets of input tokens. Reasoning tokens are a subset of output tokens. They are shown for auditability and are not added again to total tokens. Totals-only rows retain authoritative input/output/total counts when billing breakdowns are missing. Amounts exclude non-token charges and are not an invoice.

## By agent

| Agent ID | Role | Model | Exact records | Totals-only records | Unavailable records | Input | Known cached input | Known cache writes | Output | Known reasoning | Total | Known cost USD | Complete estimated cost USD | Status |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| root | coordinator | gpt-5.6-sol | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/cross_source_reviewer | cross_source_consistency_reviewer | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/evidence_rechecker | evidence_rechecker | gpt-5.6-sol | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/main_mapper | main_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/numeric_reviewer | numeric_consistency_reviewer | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/quality_auditor | evidence_quality_auditor | gpt-5.6-sol | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/report_generator | report_generator | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/reuse_asset_curator | reuse_asset_curator | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/statistics_pass_1 | statistics_pass_1 | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/statistics_pass_2 | statistics_pass_2 | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/support_mapper | support_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

## By model

| Model | Agents | Exact records | Totals-only records | Unavailable records | Input | Known cached input | Known cache writes | Output | Known reasoning | Total | Known cost USD | Complete estimated cost USD | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| gpt-5.6-sol | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 8 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

## Package total

- **Total-token count status:** INCOMPLETE
- **Input tokens:** 0
- **Cached input tokens (subset):** 0
- **Cache-write tokens (subset):** 0
- **Output tokens:** 0
- **Reasoning tokens (subset):** 0
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __
