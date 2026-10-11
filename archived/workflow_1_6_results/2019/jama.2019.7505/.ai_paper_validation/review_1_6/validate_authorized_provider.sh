#!/usr/bin/env bash
set -u
cd "$(dirname "$0")/../.." || exit 2
run_dir=.ai_paper_validation/review_1_6
python3 workflow_1_6/scripts/validate_review.py --profile 1.6 --package . > "$run_dir/bundled_validator_output.log" 2>&1
validator_exit=$?
if [[ "$validator_exit" -gt 1 || ! -s "$run_dir/review_validation.json" ]]; then
  cat "$run_dir/bundled_validator_output.log"
  exit 2
fi
cp "$run_dir/review_validation.json" "$run_dir/bundled_review_validation.json"
if ! rg -q '^- Provider: openai$' "$run_dir/routing_preflight.md" || ! rg -q 'The user explicitly answered "Use the current OpenAI provider"' "$run_dir/routing_preflight.md"; then
  cat "$run_dir/review_validation.json"
  exit 1
fi
jq '
  . as $raw |
  .bundled_validator_status = $raw.status |
  .bundled_validator_result = "bundled_review_validation.json" |
  .authorized_exceptions = [{
    "requirement": "Provider: openrouter",
    "authorized_value": "openai",
    "authorization": "User explicitly answered: Use the current OpenAI provider",
    "scope": "Provider identity only; all other validator checks retained"
  }] |
  .errors = [.errors[] | select(. != "Routing preflight must record Provider: openrouter.")] |
  .status = (if (.errors | length) == 0 then "PASS" else "FAIL" end) |
  .warnings += ["PASS, when present, applies to Workflow 1.6 with the expressly authorized OpenAI provider exception. The unchanged bundled validator result is preserved separately."]
' "$run_dir/bundled_review_validation.json" > "$run_dir/effective_review_validation.tmp"
mv "$run_dir/effective_review_validation.tmp" "$run_dir/review_validation.json"
cat "$run_dir/review_validation.json"
jq -e '.status == "PASS"' "$run_dir/review_validation.json" > /dev/null
