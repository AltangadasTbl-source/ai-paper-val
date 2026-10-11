# Workflow 1.6 Agent Execution Manifest

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12881-59bb-7f73-88ea-16d7dd7cfaf4 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12882-442a-79d1-a362-73e7476d942d | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12883-d57f-7c71-afc2-45ba2ef3d25a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12883-face-7d10-8ccd-96852e30c3df | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a12888-5c92-71d2-9763-3716e9393a45 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_support_shard | 01a12888-7c16-7dd0-9025-60bef7a65323 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| cross_source_consistency_reviewer | 01a12888-9815-7372-8d01-64e2a33d7342 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12888-bf44-7802-9727-2a37b25482c1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_supp_other_shard | 01a12888-e292-76a0-adff-3db29980b844 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_supp_other.md |
| statistics_pass_1_supp_acr_shard | 01a12888-fe72-7423-9b67-f0c70a5477af | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_supp_acr.md |
| statistics_pass_1_plan_extension_shard | 01a1288b-cbda-7140-94f6-958da8f7a6b8 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_plan_extension.md |
| numeric_support_extension_shard | 01a1288d-2e0d-7711-a552-7ca1f3e4f9f1 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support_extension.md |
| registration_formatter_main_support | 01a1288f-70c0-7d03-a947-120c507880f7 | gpt-6.1-sol | medium | FRESH_SPAWN | parts/registration_main_support_draft.md |
| registration_formatter_remaining | 01a12892-3ca0-7862-a7a0-38b12521399c | gpt-6.1-sol | medium | FRESH_SPAWN | parts/registration_remaining_draft.md |
| evidence_rechecker | 01a12896-f5ad-7e32-ba28-f907d951f8b9 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| evidence_recheck_supplement_shard | 01a12897-1665-7fd2-b19f-cacd2dfc232d | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/recheck_supplement.md |
| evidence_recheck_cross_shard | 01a12897-3671-7d40-8234-28f2193a4cc3 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/recheck_cross_remaining.md |
| statistics_pass_2 | 01a1289e-6e1d-7102-a306-c3a856a83436 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_supp_other_shard | 01a1289e-9909-78e1-a972-3d82d576e889 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_supp_other.md |
| statistics_pass_2_supp_acr_shard | 01a1289e-bba3-7b20-af6a-c5d5dbe3c9de | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_supp_acr.md |
| statistics_pass_2_plan_extension_shard | 01a1289e-db62-7391-9891-4f6621590337 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_plan_extension.md |
