#!/usr/bin/env bash
set -euo pipefail

expected_provider="openrouter"
expected_model="~openai/gpt-latest"
expected_effort="high"
credential_env_name="OPENROUTER_API_KEY"
mandatory_specialist_stages="10"

agent_contracts=(
  "qc15-fresh-source-preprocessor.toml|high"
  "qc15-main-quantitative-mapper.toml|high"
  "qc15-support-quantitative-mapper.toml|high"
  "qc15-numeric-consistency-reviewer.toml|high"
  "qc15-cross-source-consistency-reviewer.toml|high"
  "qc15-statistical-consistency-reviewer.toml|high"
  "qc15-evidence-rechecker.toml|high"
  "qc15-quality-control-auditor.toml|high"
  "qc15-report-generator.toml|high"
)

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
package_root="$(cd -- "$script_dir/../.." && pwd)"
review_dir="$package_root/.ai_paper_validation/review_1_5_4"
preflight_artifact="$review_dir/routing_preflight.md"
probe_log=""
probe_dir=""
preflight_tmp=""

cleanup() {
  if [[ -n "$probe_log" && -e "$probe_log" ]]; then
    rm -f -- "$probe_log"
  fi
  if [[ -n "$probe_dir" && -d "$probe_dir" ]]; then
    rmdir -- "$probe_dir" 2>/dev/null || true
  fi
  if [[ -n "$preflight_tmp" && -e "$preflight_tmp" ]]; then
    rm -f -- "$preflight_tmp"
  fi
}
trap cleanup EXIT

if [[ $# -gt 1 || ( $# -eq 1 && "$1" != "--preflight-only" ) ]]; then
  echo "Usage: $0 [--preflight-only]" >&2
  exit 2
fi

if ! command -v codex >/dev/null 2>&1; then
  echo "codex is not available on PATH." >&2
  exit 1
fi
if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
  echo "OPENROUTER_API_KEY is not set in the environment that launches Codex." >&2
  exit 1
fi
if ! codex exec --help 2>/dev/null | grep -Fq -- "--ignore-user-config"; then
  echo "This Codex release lacks 'codex exec --ignore-user-config'; update Codex before using this workflow." >&2
  exit 1
fi

for contract in "${agent_contracts[@]}"; do
  IFS='|' read -r preset preset_effort <<<"$contract"
  preset_path="$package_root/.codex/agents/$preset"
  if [[ ! -f "$preset_path" ]]; then
    echo "Missing named agent preset: $preset_path" >&2
    exit 1
  fi
  model_lines="$(grep -Fxc "model = \"$expected_model\"" "$preset_path" || true)"
  effort_lines="$(grep -Fxc "model_reasoning_effort = \"$preset_effort\"" "$preset_path" || true)"
  if [[ "$model_lines" != "1" || "$effort_lines" != "1" ]]; then
    echo "Named agent preset has the wrong model or effort: $preset ($expected_model/$preset_effort)" >&2
    exit 1
  fi
done

# Ignore the base user config for these invocations so a stale command-backed auth table,
# cached OpenAI login, or gpt-5.6-sol/low default cannot override this workflow. The API key
# remains in the launcher environment and Codex reads it directly through env_key.
codex_config_args=(
  --strict-config
  -m "$expected_model"
  -s workspace-write
  -c 'approval_policy="never"'
  -c 'model_provider="openrouter"'
  -c 'model_reasoning_effort="high"'
  -c 'plan_mode_reasoning_effort="high"'
  -c 'agents.default_subagent_model="~openai/gpt-latest"'
  -c 'agents.default_subagent_reasoning_effort="high"'
  -c 'model_providers.openrouter.name="openrouter"'
  -c 'model_providers.openrouter.base_url="https://openrouter.ai/api/v1"'
  -c 'model_providers.openrouter.env_key="OPENROUTER_API_KEY"'
  -c 'model_providers.openrouter.requires_openai_auth=false'
  -c 'model_providers.openrouter.wire_api="responses"'
)

# doctor validates configuration but does not authenticate a model request. This small ephemeral
# request is the routing/authentication preflight; no PASS artifact is written unless it succeeds.
probe_log="$(mktemp -t workflow-1-5-4-openrouter-probe.XXXXXX)"
probe_dir="$(mktemp -d -t workflow-1-5-4-openrouter-probe-dir.XXXXXX)"
if ! codex exec --ignore-user-config --ephemeral --json --skip-git-repo-check \
  -C "$probe_dir" "${codex_config_args[@]}" \
  "Reply with exactly OPENROUTER_AUTH_OK. Do not use tools." >"$probe_log" 2>&1; then
  echo "OpenRouter authentication probe failed; no review was started." >&2
  sed -n '1,120p' "$probe_log" >&2
  exit 1
fi
if ! grep -Fq "OPENROUTER_AUTH_OK" "$probe_log"; then
  echo "OpenRouter probe returned successfully but did not confirm the expected model response." >&2
  sed -n '1,120p' "$probe_log" >&2
  exit 1
fi

mkdir -p "$review_dir"
preflight_tmp="$(mktemp "$review_dir/.routing_preflight.XXXXXX")"
checked_utc="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
codex_version="$(codex --version 2>/dev/null)"
{
  printf '# Runtime Routing Preflight\n\n'
  printf -- '- Status: PASS\n'
  printf -- '- Provider: %s\n' "$expected_provider"
  printf -- '- Coordinator model: %s\n' "$expected_model"
  printf -- '- Default subagent model: %s\n' "$expected_model"
  printf -- '- Coordinator reasoning effort: %s\n' "$expected_effort"
  printf -- '- Default subagent reasoning effort: %s\n' "$expected_effort"
  printf -- '- Named agent reasoning effort: %s\n' "$expected_effort"
  printf -- '- Named agent presets: PASS\n'
  printf -- '- Named agent preset count: %s\n' "${#agent_contracts[@]}"
  printf -- '- Mandatory specialist stages: %s\n' "$mandatory_specialist_stages"
  printf -- '- Mandatory agent start contract: FRESH_DISTINCT\n'
  printf -- '- Authentication probe: PASS\n'
  printf -- '- Credential source: %s via env_key\n' "$credential_env_name"
  printf -- '- User config: IGNORED\n'
  printf -- '- Enforcement: CLI_OVERRIDES_PLUS_IGNORED_USER_CONFIG\n'
  printf -- '- Execution mode: CODEX_EXEC\n'
  printf -- '- Codex version: %s\n' "$codex_version"
  printf -- '- Checked UTC: %s\n' "$checked_utc"
} >"$preflight_tmp"
mv -f -- "$preflight_tmp" "$preflight_artifact"
preflight_tmp=""

if [[ $# -eq 1 ]]; then
  printf 'Routing and authentication preflight PASS: %s\n' "$preflight_artifact"
  exit 0
fi

workflow_prompt="$(<"$package_root/START_PROMPT.md")"
cleanup
trap - EXIT
exec codex exec --ignore-user-config -C "$package_root" "${codex_config_args[@]}" "$workflow_prompt"
