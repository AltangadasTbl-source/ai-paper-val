# Codex Setup for Workflow 1.6.1

Workflow 1.6.1 runs on the provider and authentication that the current Codex session already uses.
Do not configure, change, or name a provider for this workflow, and never put credentials in a paper
package. The routing preflight records the provider as `CURRENT_SESSION`.

Every role uses the fixed model `gpt-6.1-sol`. Roles differ only in reasoning effort:

- coordinator: `gpt-6.1-sol` / `high`;
- ordinary specialist roles: `gpt-6.1-sol` / `medium`;
- statistical passes 1 and 2: distinct fresh `gpt-6.1-sol` / `high` agents;
- inclusion screening, mechanical evidence recheck with classification confirmation, and final
  evidence-quality and classification audit: fresh `gpt-6.1-sol` / `high` agents.

Do not use `~openai/gpt-latest` or another moving alias. Exact model IDs are required so repeated
paper reviews use the same experimental conditions. The package-level `.codex/config.toml` fixes the
coordinator model, and the ten package-level `.codex/agents/` presets fix specialist models and
reasoning efforts.

From the paper-package root, start an interactive session directly:

```bash
codex --approve-for-me
```

Then send this as the first request:

```text
Read START_PROMPT.md completely and execute Workflow 1.6.1 now.
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
python3 workflow_1_6_1/scripts/bootstrap_tooling.py create --ocr
```

If no environment can be created, the run records `INSTALL_FAILED`, continues with the reusable
extraction assets and available tools, and lists the affected units as limitations.

`--approve-for-me` requires Codex CLI 0.147.0 or newer. It keeps the workspace-write sandbox and
routes eligible approval requests through automatic review; it does not grant additional network or
filesystem access.

The coordinator's first response is the real inference check for the current session. Before
scientific work, it must verify the fixed model matrix and all ten named presets, write
`routing_preflight.md`, and successfully start the required fresh reuse-asset curator. If the
orchestration API rejects the fixed model ID or the specialist cannot obtain a model response, stop
and record the runtime blocker. No shell launcher or `codex exec` fallback is part of this workflow.
