# Workflow 1.6 validation outcomes

Final mechanical checks completed on 2026-10-11 after standalone HTML rendering and the prescribed fallback-environment cleanup.

| Validator | Result | Errors | Interpretation |
|---|---|---:|---|
| Unchanged bundled helper | FAIL | 1 | Only the literal OpenRouter provider requirement differs from the user's current-provider instruction |
| Preserved copy with one provider-expectation string changed | PASS | 0 | All scientific, coverage, role, routing, report, timing, link and integrity checks pass; no warnings |

The baseline's sole error is `Routing preflight must record Provider: openrouter.` No provider or authentication configuration was changed, and the original helper remains unchanged. The [one-string diff](provider_override.diff) documents the complete authorized adjustment.

Preserved results: [baseline JSON](baseline_review_validation.json), [baseline log](baseline_validation.log), [adjusted log](adjusted_validation.log), and [canonical adjusted JSON](../review_validation.json). Both runs report 18 candidates, 438 statistical relationships, 39 mapped source units, 18 actual agents, unchanged sources and reused assets, complete classification, no fallback environment, and 36.47 review minutes within the selected 25–40 minute target.

Commands:

```bash
python3 workflow_1_6/scripts/validate_review.py --profile 1.6 --package .
python3 .ai_paper_validation/review_1_6/validation_override/validate_review.py --profile 1.6 --package .
```

PASS is the provider-adjusted result. It is not represented as an unmodified-baseline PASS or as human adjudication of any scientific candidate.
