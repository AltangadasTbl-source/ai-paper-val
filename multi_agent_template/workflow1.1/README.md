# Agent-first Multi-paper Validation

The user always starts with a Codex agent. The repository may contain many paper packages, but there
is one shared workflow, one set of model roles, and one operator configuration. The agent decides how
to execute the requested audit.

For a multi-paper request, the interactive collection agent invokes a thin worker-pool launcher. That
launcher provides process isolation and concurrency only. Every paper decision, including DOCX
conversion, page selection, OCR, checking, verification, and reporting, belongs to the isolated paper
agent and the shared `$ai-validation` skill.

## Layout

```text
2020/
├── .git/
├── AGENTS.md
├── ai-validation.toml
├── .codex/
│   ├── config.toml
│   ├── agents/
│   └── rules/ai-validation.rules
├── .agents/
│   └── skills/ai-validation/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── assets/report.css
│       ├── references/
│       └── scripts/
├── batch/
│   ├── prompt.md
│   ├── result.schema.json
│   └── run_batch.py
├── jamam.2024.12345/
│   ├── main.pdf
│   ├── supplement.pdf
│   └── audit/
├── jamam.2024.67890/
└── any-other-package-name/
```

The collection root must be the Git root. Do not copy shared files into paper directories. Codex loads
root `AGENTS.md`, project configuration, agent roles, and repository skills for work performed in a
child package.

## Start from WSL CLI

Open an interactive agent at the collection root:

```bash
cd /mnt/c/path/to/2020
git init                         # only once, if .git does not already exist
codex --approve-for-me
```

The selected Python environment must be Python 3.11 or newer.

Then ask naturally:

```text
Use $ai-validation. Audit all paper packages with four isolated workers.
```

Or select packages:

```text
Use $ai-validation. Audit only jamam.2024.12345 and jamam.2024.67890 with two isolated workers.
```

The interactive agent discovers package names and invokes the thin launcher. You do not need to run
the launcher, OCR scripts, or specialist agents manually.

To work directly inside one paper package:

```bash
codex --cd /mnt/c/path/to/2020/jamam.2024.12345 --approve-for-me
```

Then ask:

```text
Use $ai-validation. Audit the current paper package and produce the complete HTML report.
```

Start a new CLI session and do not use `resume` when manually moving to another paper.

## Start from Codex on Windows

Open the `2020` collection folder as the project and give the same request. The collection agent reads
the same `AGENTS.md`, `ai-validation.toml`, skill, and agent definitions. Native Windows commands use
`runtime.windows_python` and PowerShell; WSL commands use `runtime.wsl_python` and Bash.

Strict multi-paper process isolation requires the configured `codex` command to be available to the
agent environment. If it is unavailable, the agent must report that limitation instead of silently
analyzing several papers in one context. A single package can still be opened and audited interactively.

## Operator settings

Normal machine-specific changes belong only in `ai-validation.toml`. The defaults are:

```toml
[runtime]
platform = "auto"
wsl_shell = "bash"
wsl_python = "~/venvs/stt/bin/python"
windows_shell = "powershell"
windows_python = "python"
codex = "codex"

[launcher]
workers = 4
retries = 1
existing_audit = "fail"

[context]
max_normalized_text_chars_per_shard = 160000
max_rendered_pages_per_shard = 24
max_candidates_per_shard = 40
specialist_return_max_lines = 12

[ocr]
mode = "gpu"
required_backend = "rapidocr-cuda"
allow_implicit_fallback = false
nvidia_smi = "nvidia-smi"
```

On a machine without a compatible GPU, keep the same skill and change only:

```toml
[ocr]
mode = "cpu"
required_backend = "rapidocr-cpu"
allow_implicit_fallback = false
nvidia_smi = "nvidia-smi"
```

`tesseract-cpu` may be selected deliberately instead. `auto` is not permitted. A configured GPU task
never runs on CPU, and one CPU engine never changes to another implicitly. The OCR backend is validated
only if the paper agent determines that OCR is actually needed.

## What each isolated paper agent does

1. Inventory direct sources and create SHA-256-backed document records.
2. Convert direct DOC/DOCX supplements to derived PDFs when present.
3. Extract native PDF text and render only needed pages.
4. Use the exact configured OCR backend only for pages that require OCR.
5. Record complete context coverage and shard large stages into disjoint artifact-backed assignments.
6. Extract main-article and result-supplement evidence in parallel.
7. Run table arithmetic, figure/flow, and first-pass statistical checks in parallel.
8. Preserve an unbounded candidate registry and mechanically recheck every candidate.
9. Run the mandatory second statistical reconciliation pass.
10. Audit evidence-card completeness without deleting or adjudicating candidates.
11. Generate detailed Markdown and standalone HTML with exact relative PDF page links.
12. Validate artifacts, complete shard coverage, links, candidate preservation, and source integrity.

Every Terra specialist uses `gpt-5.6-terra` with `ultra` reasoning. Evidence rechecking and evidence
quality auditing use `gpt-5.6-sol` with `high` reasoning. The coordinator uses Sol/high. Luna is
forbidden.

Each outer worker is a separate Codex process and session with its own full context window; four
concurrent workers do not split one context window. `--ephemeral` prevents session rollout persistence
and `--cd` sets the package workspace, but this is not a separate virtual machine. Filesystem isolation
is enforced by the package-only rules and audit-only write policy.

No finite model context is unlimited. For large packages, the worker uses the configurable `[context]`
thresholds to divide pages, relationships, or candidate IDs into disjoint specialist calls. Complete
results are written to `audit/`, specialists return only compact summaries, and all shards are merged
and checked before the HTML report. These thresholds limit one call, never the paper coverage or the
number of retained findings.

## Outputs

Each worker writes only below its own `audit/` directory. Every requested package must independently
produce this human-facing output:

```text
<paper>/audit/final_report.html
```

It includes every candidate, detailed reasoning, a table of contents, and relative links such as:

```text
../main.pdf#page=8
```

The report is always marked `Pending Human Adjudication`. Models do not assign severity, validity,
acceptance, rejection, or uncertainty.

The thin launcher marks a package failed unless its own HTML file is nonempty and its own
`audit/audit_validation.json` reports `PASS`. One package's report can never satisfy another package.

## Thin launcher boundary

`batch/run_batch.py` may discover direct child package names, archive a previous `audit/` directory,
limit concurrency to two through four, retry a failed process, and launch fresh `codex exec --ephemeral`
workers. It must not inspect article content, select pages, convert documents, choose OCR dynamically,
filter candidates, or generate reports.

The launcher passes `--approve-for-me` without a separate `--sandbox workspace-write` argument. In
Codex CLI versions where `--approve-for-me` selects the workspace-write sandbox itself, supplying both
flags is a configuration conflict. Keep `--approve-for-me`; it provides automatic approval review and
the required workspace-write sandbox while the project rules pre-approve recurring reviewed commands.

The architecture follows the official OpenAI documentation for
[AGENTS.md inheritance](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
[repository skills](https://learn.chatgpt.com/docs/build-skills),
[Codex CLI](https://learn.chatgpt.com/docs/codex/cli), and
[Windows/WSL use](https://learn.chatgpt.com/docs/windows/wsl).
