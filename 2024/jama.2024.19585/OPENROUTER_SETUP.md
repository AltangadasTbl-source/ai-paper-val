# OpenRouter and Direct Codex Setup for Workflow 1.6

Workflow 1.6 uses one fixed model, `gpt-6.1-sol`, for every role. Roles differ only in reasoning
effort:

- coordinator: `gpt-6.1-sol` / `high`;
- ordinary specialist roles: `gpt-6.1-sol` / `medium`;
- statistical passes 1 and 2: distinct fresh `gpt-6.1-sol` / `high` agents;
- mechanical evidence recheck with classification confirmation, and final evidence-quality and
  classification audit: fresh `gpt-6.1-sol` / `high` agents.

Do not use `~openai/gpt-latest` or another moving alias. Exact model IDs are required so repeated
paper reviews use the same experimental conditions.

Configure the provider only in the user-level `~/.codex/config.toml`:

```toml
model_provider = "openrouter"

[model_providers.openrouter]
name = "openrouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"
requires_openai_auth = false
wire_api = "responses"
```

Export `OPENROUTER_API_KEY` in the shell that launches Codex. Do not put a literal key in a paper
package or TOML file. The package-level `.codex/config.toml` fixes the coordinator model, and the nine
package-level `.codex/agents/` presets fix specialist models and reasoning efforts.

From the paper-package root, start an interactive session directly:

```bash
codex --approve-for-me
```

Then send this as the first request:

```text
Read START_PROMPT.md completely and execute Workflow 1.6 now.
```

## Network access for the temporary fallback environment

When poppler or tesseract is missing, the run installs pinned Python packages into a temporary
package-local environment, which needs network access for `pip`. The workspace-write sandbox disables
network access by default. To allow it, add this to the user-level `~/.codex/config.toml`:

```toml
[sandbox_workspace_write]
network_access = true
```

On macOS this setting has been reported to have no effect in some Codex versions. If the bootstrap
reports `FAILED` there, pre-create the environment yourself from the package root before starting
Codex; the run then reuses it:

```bash
python3 workflow_1_6/scripts/bootstrap_tooling.py create --ocr
```

If no environment can be created, the run records `INSTALL_FAILED`, continues with the reusable
extraction assets and available tools, and lists the affected units as limitations.

`--approve-for-me` requires Codex CLI 0.147.0 or newer. It keeps the workspace-write sandbox and
routes eligible approval requests through automatic review; it does not grant additional network or
filesystem access.

The coordinator's first response is the real provider/authentication inference check. Before
scientific work, it must verify the fixed model matrix and all nine named presets, write
`routing_preflight.md`, and successfully start the required fresh reuse-asset curator. If the
orchestration API rejects the fixed model ID or the specialist cannot obtain a model response, stop
and record the runtime blocker. No shell launcher or `codex exec` fallback is part of this workflow.
