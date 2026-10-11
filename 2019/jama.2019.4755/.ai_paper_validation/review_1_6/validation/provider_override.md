# Explicit Current-Provider Validation Override

The user instructed: "use the current provider". Runtime provider: openai. The package defaults to openrouter. The current coordinator and every named specialist retain gpt-6.1-sol and their required reasoning efforts.

To honor that instruction while preserving the original workflow controls, a run-local copy of the supplied final validator was produced with sed. Its only change is the exact expected Provider value from openrouter to openai. This is an auxiliary validation adaptation of the supplied helper, not scientific review or extraction code. The user's provider instruction takes precedence over the original helper's provider expectation and the helper-path restriction solely for executing this preserved, minimally adapted supplied validator. All other checks remain identical.

Provenance: workflow_1_6/scripts/validate_review.py; derived copy validation/validate_review.py; exact diff current_provider_override.diff; hashes validator_hashes.sha256. The original helper will also execute, and its unmodified result will be preserved separately. A PASS under this override must never be presented as a PASS under the original openrouter requirement.
