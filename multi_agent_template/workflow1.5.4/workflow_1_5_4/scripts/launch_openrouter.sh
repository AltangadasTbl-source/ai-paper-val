#!/usr/bin/env bash
set -euo pipefail

expected_provider="openrouter"
expected_model="~openai/gpt-latest"
coordinator_effort="high"
default_subagent_effort="medium"
mandatory_specialist_stages="10"

agent_contracts=(
  "qc15-fresh-source-preprocessor.toml|medium"
  "qc15-main-quantitative-mapper.toml|medium"
  "qc15-support-quantitative-mapper.toml|medium"
  "qc15-numeric-consistency-reviewer.toml|medium"
  "qc15-cross-source-consistency-reviewer.toml|medium"
  "qc15-statistical-consistency-reviewer.toml|high"
  "qc15-evidence-rechecker.toml|high"
  "qc15-quality-control-auditor.toml|high"
  "qc15-report-generator.toml|medium"
)

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
package_root="$(cd -- "$script_dir/../.." && pwd)"
review_dir="$package_root/.ai_paper_validation/review_1_5_4"
preflight_artifact="$review_dir/routing_preflight.md"

if [[ $# -gt 1 || ( $# -eq 1 && "$1" != "--preflight-only" ) ]]; then
  echo "Usage: $0 [--preflight-only]" >&2
  exit 2
fi

if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
  echo "OPENROUTER_API_KEY is not set in the environment that launches Codex." >&2
  exit 1
fi

for contract in "${agent_contracts[@]}"; do
  IFS='|' read -r preset expected_effort <<<"$contract"
  preset_path="$package_root/.codex/agents/$preset"
  if [[ ! -f "$preset_path" ]]; then
    echo "Missing named agent preset: $preset_path" >&2
    exit 1
  fi
  model_lines="$(grep -Fxc "model = \"$expected_model\"" "$preset_path" || true)"
  effort_lines="$(grep -Fxc "model_reasoning_effort = \"$expected_effort\"" "$preset_path" || true)"
  if [[ "$model_lines" != "1" || "$effort_lines" != "1" ]]; then
    echo "Named agent preset has the wrong model or effort: $preset ($expected_model/$expected_effort)" >&2
    exit 1
  fi
done

codex_args=(
  --strict-config
  -C "$package_root"
  -m "$expected_model"
  -c 'model_provider="openrouter"'
  -c 'model_reasoning_effort="high"'
  -c 'agents.default_subagent_model="~openai/gpt-latest"'
  -c 'agents.default_subagent_reasoning_effort="medium"'
)

doctor_output="$(codex "${codex_args[@]}" doctor --json 2>/dev/null || true)"
config_block="$(printf '%s\n' "$doctor_output" | sed -n '/"config.load"/,/"git.environment"/p')"

if ! grep -Fq '"model": "~openai/gpt-latest"' <<<"$config_block"; then
  echo "Codex did not resolve the coordinator model to $expected_model." >&2
  exit 1
fi
if ! grep -Fq '"model provider": "openrouter"' <<<"$config_block"; then
  echo "Codex did not resolve the model provider to $expected_provider." >&2
  exit 1
fi
if [[ -e "$preflight_artifact" ]]; then
  echo "Refusing to overwrite the existing routing preflight: $preflight_artifact" >&2
  exit 1
fi

mkdir -p "$review_dir"
checked_utc="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
codex_version="$(codex --version 2>/dev/null)"
{
  printf '# Runtime Routing Preflight\n\n'
  printf -- '- Status: PASS\n'
  printf -- '- Provider: %s\n' "$expected_provider"
  printf -- '- Coordinator model: %s\n' "$expected_model"
  printf -- '- Default subagent model: %s\n' "$expected_model"
  printf -- '- Coordinator reasoning effort: %s\n' "$coordinator_effort"
  printf -- '- Default subagent reasoning effort: %s\n' "$default_subagent_effort"
  printf -- '- Named agent presets: PASS\n'
  printf -- '- Named agent preset count: %s\n' "${#agent_contracts[@]}"
  printf -- '- Mandatory specialist stages: %s\n' "$mandatory_specialist_stages"
  printf -- '- Mandatory agent start contract: FRESH_DISTINCT\n'
  printf -- '- Enforcement: CLI_OVERRIDES\n'
  printf -- '- Codex version: %s\n' "$codex_version"
  printf -- '- Checked UTC: %s\n' "$checked_utc"
} >"$preflight_artifact"

if [[ $# -eq 1 ]]; then
  printf 'Routing preflight PASS: %s\n' "$preflight_artifact"
  exit 0
fi

workflow_prompt="$(<"$package_root/START_PROMPT.md")"
exec codex "${codex_args[@]}" "$workflow_prompt"
