# OpenRouter Prerequisite for Workflow 1.5.4

This profile routes the coordinator, every named custom agent, and every default or repair subagent
through `~openai/gpt-latest` at `high` reasoning effort.

For ordinary Codex sessions, place the provider in the machine-level `~/.codex/config.toml`:

```toml
model_provider = "openrouter"
model = "~openai/gpt-latest"
model_reasoning_effort = "high"
plan_mode_reasoning_effort = "high"

[agents]
default_subagent_model = "~openai/gpt-latest"
default_subagent_reasoning_effort = "high"

[model_providers.openrouter]
name = "openrouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"
requires_openai_auth = false
wire_api = "responses"
```

Export `OPENROUTER_API_KEY` in the same environment that launches Codex. Do not copy the key into a
paper package or put a literal token in TOML. Do not combine `env_key` with
`[model_providers.openrouter.auth]`; Codex supports either source, and this workflow deliberately uses
`env_key` for a fixed API key.

Project-scoped `.codex/config.toml` cannot select or authenticate a provider. Therefore start this
profile only from the package root with:

```bash
bash workflow_1_5_4/scripts/launch_openrouter.sh
```

The launcher uses `codex exec --ignore-user-config`, supplies the complete OpenRouter provider as
highest-precedence CLI configuration, reads the bearer token directly through `env_key`, and pins the
coordinator and all subagents to `~openai/gpt-latest`/`high`. Ignoring the base user config prevents a
cached OpenAI login, a stale command-backed provider, or a `gpt-5.6-sol`/`low` default from leaking
into this run.

Before it writes `routing_preflight.md` or starts the review, the launcher performs one small
ephemeral model request. A `PASS` therefore confirms both configuration and bearer-token
authentication; `doctor` output alone is not accepted. The review itself runs non-interactively to
completion through `codex exec`. Use `--preflight-only` to test routing and authentication without
starting the paper review.
