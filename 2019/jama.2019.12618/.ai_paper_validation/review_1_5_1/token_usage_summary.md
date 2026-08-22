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
| runtime:/root/cross_candidate_consolidator | candidate_registration | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/cross_checker_scope_1 | cross_source_checker | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/cross_checker_scope_2 | cross_source_checker | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/cross_checker_scope_3 | cross_source_checker | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/cross_checker_scope_4 | cross_source_checker | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/data_sharing_mapper | support_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/evidence_rechecker | evidence_recheck | gpt-5.6-sol | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/main_mapper | main_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/numeric_checker_001_094 | numeric_checker | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/numeric_checker_095_188 | numeric_checker | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/numeric_checker_189_282 | numeric_checker | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/numeric_checker_consolidator | numeric_checker_consolidator | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/protocol_mapper_001_032 | support_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/protocol_mapper_033_064 | support_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/protocol_mapper_065_096 | support_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/protocol_mapper_097_128 | support_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/protocol_mapper_129_153 | support_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/quality_control_auditor | evidence_quality | gpt-5.6-sol | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/relationship_consolidator | relationship_consolidator | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/report_generator | report_generation | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/reuse_asset_curator | reuse_asset_curator | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/sap_mapper_001_032 | support_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/sap_mapper_033_064 | support_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/sap_mapper_065_083 | support_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/statistics_pass_1 | statistics_pass_1 | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/statistics_pass_2 | statistics_pass_2 | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| runtime:/root/supp_results_mapper | support_quantitative_mapper | gpt-5.6-terra | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

## By model

| Model | Agents | Exact records | Totals-only records | Unavailable records | Input | Known cached input | Known cache writes | Output | Known reasoning | Total | Known cost USD | Complete estimated cost USD | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| gpt-5.6-sol | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 25 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

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
