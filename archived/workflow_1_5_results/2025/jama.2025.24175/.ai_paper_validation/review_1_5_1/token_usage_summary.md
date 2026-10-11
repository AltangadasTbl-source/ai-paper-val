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
| COORDINATOR-CURRENT-SESSION | coordinator | gpt-5.6-sol | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/candidate_registration | candidate_registration | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/cross_source_checks | cross_source_checks | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/evidence_quality | evidence_quality | gpt-5.6-sol | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/evidence_recheck | evidence_recheck | gpt-5.6-sol | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/map_doc2_a | support_quantitative_mapper_doc002_pp001_032 | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/map_doc2_b | support_quantitative_mapper_doc002_pp033_064 | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/map_doc2_c | support_quantitative_mapper_doc002_pp065_072 | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/map_doc3 | support_quantitative_mapper_doc003 | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/map_doc45 | support_quantitative_mapper_doc004_005 | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/map_main | main_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/mapping_consolidation | mapping_consolidation | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/numeric_checks | numeric_checks | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/report_generation | report_generation | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/reuse_inventory | reuse_asset_curator | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/statistics_pass_1 | statistics_pass_1 | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| root/statistics_pass_2 | statistics_pass_2 | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

## By model

| Model | Agents | Exact records | Totals-only records | Unavailable records | Input | Known cached input | Known cache writes | Output | Known reasoning | Total | Known cost USD | Complete estimated cost USD | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| gpt-5.6-sol | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 14 | 0 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

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
