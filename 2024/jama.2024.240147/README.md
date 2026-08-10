# Codex Agent Workflow Template

This folder is inert. Codex does not load it as project configuration.

To activate the workflow in a new project, copy:

```text
codex_agent_workflow_template/config.toml
    -> <new-project>/.codex/config.toml

codex_agent_workflow_template/agents/
    -> <new-project>/.codex/agents/

codex_agent_workflow_template/AGENTS.md
    -> <new-project>/AGENTS.md
```

The root thread acts as `Coordinator`. Do not copy these files to `C:\Users\juliz\.codex`.

