# Codex Setup for Workflow 1.6.2

Workflow 1.6.2 runs on the provider and authentication that the current Codex session already uses.
Do not configure, change, or name a provider for this workflow, and never put credentials in a paper
package. The routing preflight records the provider as `CURRENT_SESSION`.

Every role uses one run model, by default `gpt-6.1-sol`. Roles differ only in reasoning effort:

- coordinator: `gpt-6.1-sol` / `high`;
- ordinary specialist roles: `gpt-6.1-sol` / `medium`;
- statistical passes 1 and 2: distinct fresh `gpt-6.1-sol` / `high` agents;
- inclusion screening, mechanical evidence recheck with classification confirmation, and final
  evidence-quality and classification audit: fresh `gpt-6.1-sol` / `high` agents.

If `gpt-6.1-sol` is unavailable, or you want a later model, the coordinator stops and asks you for the
exact model ID; it never picks a substitute. To set it yourself before starting, replace the model in
the project config and all ten presets, for example:

```bash
sed -i 's/"gpt-6.1-sol"/"NEW-MODEL-ID"/' .codex/config.toml .codex/agents/qc162-*.toml
```

The preflight then records `Run model: NEW-MODEL-ID` and `Run model source: USER_SELECTED`. Do not use
`~openai/gpt-latest` or another moving alias: exact model IDs keep repeated reviews comparable.

Rendering and OCR run on the CPU by default, and the coordinator says so before the first rendering or
OCR step. Ask for GPU OCR in the session if you want it; the device is recorded in
`tooling_record.md`. The package-level `.codex/config.toml` fixes the
coordinator model, and the ten package-level `.codex/agents/` presets fix specialist models and
reasoning efforts.

From the paper-package root, start an interactive session directly:

```bash
codex --approve-for-me
```

Then send this as the first request:

```text
Read START_PROMPT.md completely and execute Workflow 1.6.2 now.
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
python3 workflow_1_6_2/scripts/bootstrap_tooling.py create --ocr
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
