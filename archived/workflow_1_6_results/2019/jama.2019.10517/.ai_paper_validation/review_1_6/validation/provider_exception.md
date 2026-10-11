# Authorized Provider Exception and Validation Basis

The user explicitly authorized: "Use the current provider and document the deviation." Actual CLI coordinator and specialist runtime metadata reports provider `openai`; all model and effort requirements remain unchanged.

The supplied validator hard-codes the routing preflight Provider field to `openrouter` in validate_routing_preflight. The original validator and all workflow controls remain unchanged. A local copy of that supplied auxiliary validation helper is stored at validation/validate_review.py. Its sole diff changes the expected Provider string from `openrouter` to `openai`; no scientific, coverage, agent, source-integrity, classification, report, performance, or tooling check is changed. This narrowly applies the user's provider authorization to validation. It is a derivative of the supplied validation helper, not new scientific-review or extraction code.

At final validation, run the original helper first and preserve its unamended JSON and log in this directory. Then run the local copy against the same package. The canonical review_validation.json records the user-amended provider contract; the original validator outcome remains available as validation/original_review_validation.json. Report both outcomes honestly. Never claim the original provider contract was satisfied.

## Actual final outcomes

The original supplied validator was executed after standalone HTML rendering and tooling finalization. Its preserved JSON reports FAIL with exactly one error: `Routing preflight must record Provider: openrouter.` It confirms15 stable candidates,108 statistical relationships and15 actual agents. The user-authorized copied validator then reports PASS, with no errors or warnings, on the same package. Source coverage, integrity, fresh distinct fixed model/effort routing, classification equality, complete reports and performance checks all pass. Both outputs and their logs are retained. The original provider requirement is not claimed to have passed.
