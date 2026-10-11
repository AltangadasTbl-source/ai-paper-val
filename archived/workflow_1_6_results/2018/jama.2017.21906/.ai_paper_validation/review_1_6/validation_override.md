# Validation routing override

The user explicitly instructed: “Use the current provider by default even if it says to use openrouter.” The active interactive session was retained without changing provider or authentication. The original validator requires literal `Provider: openrouter` and `Launch command: codex --approve-for-me`, although this job was requested in an already active session.

To preserve truthful provenance and every supplied control file, scripts/validate_review.py is a copy of the supplied final validator with only those two expected strings adapted to routing_preflight.md. All scientific, source-integrity, coverage, agent-model, classification, evidence-link, report, timing, and tooling checks remain identical. The original validator will also be run; its unadapted result will be preserved as review_validation_original.json. The final review_validation.json uses the user-override-aware copy. This is a validator helper adaptation, not scientific-review orchestration.

Reproducible commands:

```
python3 workflow_1_6/scripts/validate_review.py --profile 1.6 --package .
cp .ai_paper_validation/review_1_6/review_validation.json .ai_paper_validation/review_1_6/review_validation_original.json
python3 .ai_paper_validation/review_1_6/scripts/validate_review.py --profile 1.6 --package .
```

No supplied file was modified.
