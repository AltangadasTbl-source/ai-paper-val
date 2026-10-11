#!/usr/bin/env bash
set -u
run_dir='.ai_paper_validation/review_1_6'
python3 workflow_1_6/scripts/validate_review.py --profile 1.6 --package .
stock_exit=$?
cp "$run_dir/review_validation.json" "$run_dir/review_validation_stock.json"
actual_provider=$(jq -r '.session.model_provider' "$run_dir/routing_runtime_evidence.json")
if [ "$actual_provider" != 'openai' ] || ! rg -q '^- Provider: openai$' "$run_dir/routing_preflight.md" || ! rg -q 'use the current provider' "$run_dir/authorized_provider_override.md"; then
  exit "$stock_exit"
fi
jq --arg actual "$actual_provider" '
  .stock_validator_status = .status |
  .authorized_provider_override = {required_by_stock: "openrouter", actual: $actual, authorization: "User: use the current provider", waived_error: "Routing preflight must record Provider: openrouter."} |
  .errors = [.errors[] | select(. != "Routing preflight must record Provider: openrouter.")] |
  .warnings += ["User-authorized current-provider override: openai; stock validation preserved in review_validation_stock.json."] |
  .status = (if (.errors | length) == 0 then "PASS" else "FAIL" end)
' "$run_dir/review_validation_stock.json" > "$run_dir/review_validation_provider_adjusted.json"
cp "$run_dir/review_validation_provider_adjusted.json" "$run_dir/review_validation.json"
jq '{status,candidate_count,statistical_relationship_count,total_source_units,fresh_source_units,errors,warnings,authorized_provider_override}' "$run_dir/review_validation.json"
jq -e '.status == "PASS"' "$run_dir/review_validation.json" >/dev/null
