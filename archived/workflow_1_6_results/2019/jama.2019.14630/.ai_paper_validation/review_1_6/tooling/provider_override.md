# Current-provider validation exception

User authorization: “use the current provider by default”. Session metadata identifies the inherited provider as `openai`; it is unchanged for all review work. Workflow controls hardcode `openrouter` despite the user's overriding instruction. The original helper and every workflow control remain unchanged.

A run-local copy of the supplied final validation helper changes exactly one literal: the expected `Provider` value in `validate_routing_preflight` from `openrouter` to `openai`. Every other check, including source coverage, classification, evidence links, two statistical passes, fresh-agent routing, timing, and source integrity, is unchanged. This remains the supplied final validator as an auxiliary helper; it performs no scientific reasoning or candidate selection.

Reproduction:

1. Run `python3 workflow_1_6/scripts/validate_review.py --profile 1.6 --package .` and preserve its JSON as `review_1_6/strict_review_validation.json`.
2. Run `python3 .ai_paper_validation/review_1_6/tooling/validate_review_current_provider.py --profile 1.6 --package .`. Its `review_validation.json` is the completion result under the user-authorized provider exception.
3. Inspect `tooling/current_provider_validator.patch` and `tooling/validator_hashes.sha256` to verify the exact change.

The final report must disclose that PASS uses this provider-only exception and that strict validation retains the OpenRouter expectation failure. No scientific check is waived.
