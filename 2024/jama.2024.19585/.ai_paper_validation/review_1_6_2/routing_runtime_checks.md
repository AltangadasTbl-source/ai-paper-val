# Fresh Runtime Routing Confirmation

Only runtime IDs and model/effort fields were read from local session turn metadata. The latest actual turn is used, excluding inherited earlier coordinator contexts. Provider and authentication remain CURRENT_SESSION; no credentials are recorded.

| Stage | Runtime ID | Actual model | Actual effort | Result |
|---|---|---|---|---|
| coordinator | 01a129ab-d869-7862-8674-5be7c3ea3ce3 | gpt-6.1-sol | high | PASS |
| reuse_asset_curator | 01a129ae-95bc-7d71-a296-14fdb6208bc0 | gpt-6.1-sol | medium | PASS |
| main_quantitative_mapper | 01a129b1-193e-71e0-bfc4-ffd8db937dad | gpt-6.1-sol | medium | PASS |
| support_quantitative_mapper | 01a129b1-36ec-7cb2-ba29-5f29a1a78ec6 | gpt-6.1-sol | medium | PASS |
| numeric_consistency_reviewer | 01a129b5-e322-7ff1-a198-947ffd0e507e | gpt-6.1-sol | medium | PASS |
| cross_source_consistency_reviewer | 01a129b6-079a-7e33-a3bd-a948d6575855 | gpt-6.1-sol | medium | PASS |
| statistics_pass_1 | 01a129b6-3a3f-7742-b588-3b9736635a69 | gpt-6.1-sol | high | PASS |
| inclusion_screener | 01a129bc-b625-7260-9a1e-c110b1a90be7 | gpt-6.1-sol | high | PASS |
| evidence_rechecker | 01a129c2-9398-7d72-a901-f965a97cdd81 | gpt-6.1-sol | high | PASS |
| statistics_pass_2 | 01a129c7-e5ad-70f3-ad51-87e5ed913bb7 | gpt-6.1-sol | high | PASS |
| quality_control_auditor | 01a129cd-34db-7163-800a-23321bca57df | gpt-6.1-sol | high | PASS |
| report_generator | 01a129d2-fee4-78c1-926a-4123de7d7814 | gpt-6.1-sol | medium | PASS |
