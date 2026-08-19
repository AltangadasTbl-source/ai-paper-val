# OpenRouter Prerequisite for Workflow 1.5.3

This profile routes the coordinator, every named custom agent, and default or repair subagents through
the model slug `~openai/gpt-latest`. The provider and its bearer-token command must remain in the
machine-level file `~/.codex/config.toml`:

```toml
model_provider = "openrouter"
model_reasoning_effort = "high"
model = "~openai/gpt-latest"

[model_providers.openrouter]
name = "openrouter"
base_url = "https://openrouter.ai/api/v1"

[model_providers.openrouter.auth]
command = "sh"
args = ["-c", "echo $OPENROUTER_API_KEY"]
```

Export `OPENROUTER_API_KEY` in the environment that launches Codex. Do not copy the key into a paper
package. Codex intentionally ignores `model_provider` and `model_providers` in project-scoped
`.codex/config.toml`; the bundled project preset therefore contains only the model slug, reasoning,
permissions, and subagent defaults.

Do not rely on the package `.codex/config.toml` as the runtime enforcement point. A paper package may
be nested below a larger repository root, or project configuration may be unavailable to the active
client. Start the workflow only through the bundled launcher, whose CLI overrides have higher
precedence than project and user configuration:

```bash
bash workflow_1_5_3/scripts/launch_openrouter.sh
```

The launcher verifies the resolved provider and coordinator model with `codex doctor`, forces the
coordinator and default subagent route to `~openai/gpt-latest`, verifies all nine named presets against
their role-specific model/effort contracts, writes
`.ai_paper_validation/review_1_5_3/routing_preflight.md`, and then starts a fresh session with
`START_PROMPT.md`. Do not use `resume` or start the workflow with a plain `codex` command.
