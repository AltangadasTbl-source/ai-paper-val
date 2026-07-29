# Migrating the AI Paper Validation Workflow to OpenRouter

Last verified: 2026-07-28  
Local Codex version inspected: `codex-cli 0.145.0`

This guide explains how to keep using the local Codex CLI or the Codex extension
for VS Code while routing model inference through OpenRouter. It also explains
how PDF extraction, page rendering, OCR, visual inspection, provenance, and
privacy should work after the migration.

The short recommendation is:

> Keep Codex as the local agent runtime, use OpenRouter as Codex's custom model
> provider, and keep PDF preprocessing deterministic and local. Do not expect
> changing the model provider to automatically invoke OpenRouter's PDF parser
> or OCR service.

## Contents

1. [Current workflow](#1-current-workflow)
2. [What changes and what does not](#2-what-changes-and-what-does-not)
3. [Important Codex configuration boundaries](#3-important-codex-configuration-boundaries)
4. [Create and protect an OpenRouter API key](#4-create-and-protect-an-openrouter-api-key)
5. [Configure OpenRouter as the Codex provider](#5-configure-openrouter-as-the-codex-provider)
6. [Update the project and agent model names](#6-update-the-project-and-agent-model-names)
7. [Use the configuration from Codex CLI](#7-use-the-configuration-from-codex-cli)
8. [Use the configuration from the VS Code extension](#8-use-the-configuration-from-the-vs-code-extension)
9. [Validate the provider migration](#9-validate-the-provider-migration)
10. [PDF and OCR behavior in the current workflow](#10-pdf-and-ocr-behavior-in-the-current-workflow)
11. [Recommended provider-independent PDF architecture](#11-recommended-provider-independent-pdf-architecture)
12. [Implementing reliable local OCR](#12-implementing-reliable-local-ocr)
13. [Optional OpenRouter-managed PDF parsing and OCR](#13-optional-openrouter-managed-pdf-parsing-and-ocr)
14. [Privacy, retention, routing, and compliance](#14-privacy-retention-routing-and-compliance)
15. [Model and cost strategy](#15-model-and-cost-strategy)
16. [End-to-end migration test plan](#16-end-to-end-migration-test-plan)
17. [Troubleshooting](#17-troubleshooting)
18. [Rollback](#18-rollback)
19. [Migration checklist](#19-migration-checklist)
20. [Documentation references](#20-documentation-references)

## 1. Current workflow

The template implements a coordinator-and-subagent workflow for validating one
article package. The active project contains one main article and zero or more
supplementary PDFs. The root Codex thread acts as the coordinator.

The required execution sequence is defined in [`AGENTS.md`](./AGENTS.md):

1. `package_inventory`
2. `ai_use_restriction_checker`
3. `pdf_preprocessor`
4. `main_text_extractor` and `results_supplement_extractor` in parallel
5. `table_arithmetic_checker`, `figure_flow_checker`, and
   `statistical_consistency_checker` in parallel
6. `evidence_verifier`
7. `critic`
8. `report_generator`
9. Human adjudication

The template contains 11 custom Codex agents under `.codex/agents/`:

| Agent | Current model tier | Main responsibility |
|---|---|---|
| `package_inventory` | Terra | Inventory and classify source PDFs |
| `ai_use_restriction_checker` | Terra | Screen document-level AI-use language |
| `pdf_preprocessor` | Terra | Native extraction, rendering, and selective OCR |
| `main_text_extractor` | Terra | Extract main-article result evidence |
| `results_supplement_extractor` | Terra | Extract result-relevant supplement evidence |
| `table_arithmetic_checker` | Terra | Check table arithmetic and internal consistency |
| `figure_flow_checker` | Sol | Inspect figures, labels, and participant flow |
| `statistical_consistency_checker` | Sol | Check reported statistical relationships |
| `evidence_verifier` | Sol | Reopen cited evidence and verify candidates |
| `critic` | Sol | Remove unsupported or out-of-scope findings |
| `report_generator` | Terra | Format accepted findings for adjudication |

The workflow is intentionally selective:

- It processes the main article and result-relevant supplement pages.
- It does not routinely audit protocol, SAP, administrative, author-list, or
  data-sharing pages.
- It still creates an AI Training Restriction Record for every supplied PDF.
- It preserves source PDFs unchanged.
- It writes derived data only under `.ai_paper_validation/`.
- It requires page-level provenance for every retained scientific finding.

The template directory itself is inert. To activate it for an article package,
the project must contain:

```text
<article-project>/
├── AGENTS.md
├── main.pdf
├── supplement_1.pdf
├── supplement_2.pdf
└── .codex/
    ├── config.toml
    └── agents/
        ├── package-inventory.toml
        ├── pdf-preprocessor.toml
        └── ...
```

Copy the files from this template as follows:

```text
multi_agent_template/AGENTS.md
    -> <article-project>/AGENTS.md

multi_agent_template/.codex/config.toml
    -> <article-project>/.codex/config.toml

multi_agent_template/.codex/agents/
    -> <article-project>/.codex/agents/
```

## 2. What changes and what does not

After migration, responsibility is divided like this:

| Component | Before | After |
|---|---|---|
| Local agent runtime | Codex CLI/extension | Codex CLI/extension |
| Tool execution | Codex local shell/filesystem tools | Same |
| Agent definitions | Project `.codex/agents/*.toml` | Same, with OpenRouter model slugs |
| Workflow rules | Project `AGENTS.md` | Same |
| Model API endpoint | OpenAI/ChatGPT-backed Codex provider | OpenRouter Responses API |
| API credential | ChatGPT/OpenAI authentication | `OPENROUTER_API_KEY` |
| Native PDF extraction | Local Python/Poppler tools | Local Python/Poppler tools |
| Page rendering | Local PyMuPDF/Poppler tools | Local PyMuPDF/Poppler tools |
| OCR | Local OCR engine, if installed | Local OCR engine, if installed |
| OpenRouter PDF parser | Not used | Still not automatic; optional helper only |
| Derived artifacts | `.ai_paper_validation/` | Same |
| Source PDF policy | Never modify source PDFs | Same |

The provider switch changes where model inference runs. It does not install PDF
tools, install an OCR engine, upload workspace PDFs as OpenRouter file inputs,
or inject OpenRouter's `file-parser` plugin into Codex requests.

## 3. Important Codex configuration boundaries

### 3.1 CLI and VS Code share local Codex configuration

The local Codex CLI and the Codex IDE extension use the same configuration
layers. Both can read:

- User-level configuration: `~/.codex/config.toml`
- Trusted project configuration: `<project>/.codex/config.toml`
- Project custom agents: `<project>/.codex/agents/*.toml`
- Project guidance: `<project>/AGENTS.md`

The extension can open the active Codex configuration through:

```text
Codex sidebar
  -> gear icon
  -> Codex Settings
  -> Open config.toml
```

### 3.2 Provider configuration cannot be project-scoped

This is the most important configuration constraint in the migration.

Codex ignores these keys when they appear in a project-local
`.codex/config.toml`:

- `model_provider`
- `model_providers`
- `openai_base_url`
- Provider authentication settings
- Profile selection

Therefore:

- Put the OpenRouter provider definition in `~/.codex/config.toml`.
- Keep workflow and agent settings in the article project's `.codex/` folder.
- Do not put the OpenRouter API key in either file.

This differs slightly from the template's instruction not to copy workflow
files into the global Codex directory. The workflow files should remain
project-scoped, but the machine-local provider definition must be user-scoped.

### 3.3 Codex custom providers use the Responses protocol

Current Codex custom model providers support:

```toml
wire_api = "responses"
```

`responses` is currently the only supported custom-provider wire API. Codex
cannot be switched to Chat Completions by setting:

```toml
wire_api = "chat"
```

or:

```toml
wire_api = "chat_completions"
```

Those values are unsupported.

OpenRouter currently provides an OpenAI-compatible Responses endpoint at:

```text
https://openrouter.ai/api/v1/responses
```

The configured `base_url` should be:

```text
https://openrouter.ai/api/v1
```

Codex appends the Responses endpoint path. Do not place `/responses` at the end
of the configured base URL unless a future Codex version explicitly changes
this behavior.

### 3.4 Local and cloud Codex runs are different

The provider configuration applies to local Codex sessions:

- Codex CLI
- Local Codex IDE extension chats
- Other local Codex clients that read the same configuration

It does not control a task delegated to Codex Cloud or ChatGPT's hosted
environment. If the VS Code extension offers a choice between local work and
cloud delegation, select local work when the run must use OpenRouter.

## 4. Create and protect an OpenRouter API key

Create an API key in the OpenRouter account dashboard. Prefer a dedicated key
for this workflow so that it can have its own:

- Budget
- Model allowlist
- Provider allowlist
- Privacy settings
- Zero Data Retention policy
- Guardrail
- Usage audit trail

Do not place the key in:

- `AGENTS.md`
- `.codex/config.toml`
- An agent TOML file
- A committed `.env` file
- A preprocessing manifest
- `.ai_paper_validation/`
- A command that will be committed into shell history

Codex's provider configuration should refer to the key by environment-variable
name:

```toml
env_key = "OPENROUTER_API_KEY"
```

### 4.1 Linux or macOS

For a temporary shell session:

```bash
export OPENROUTER_API_KEY="replace-with-your-key"
```

Confirm only whether the variable exists; do not print the key:

```bash
if [ -n "${OPENROUTER_API_KEY:-}" ]; then
  echo "OPENROUTER_API_KEY is set"
else
  echo "OPENROUTER_API_KEY is not set"
fi
```

For persistent use, use a secure shell credential loader, operating-system
keychain integration, or another approved secrets manager. Be aware that a VS
Code process launched from a desktop icon may not inherit variables configured
only in an interactive shell.

### 4.2 Windows PowerShell

For the current PowerShell process:

```powershell
$env:OPENROUTER_API_KEY = "replace-with-your-key"
```

Then start VS Code from that PowerShell process:

```powershell
code .
```

For persistent use, store the key through an approved Windows credential or
environment-management method, then completely restart VS Code. Avoid saving
the key in workspace settings or a repository file.

### 4.3 WSL

If the project and Codex run inside WSL:

```bash
export OPENROUTER_API_KEY="replace-with-your-key"
code .
```

If the VS Code extension is configured to run Codex inside WSL, the key must be
available in the WSL environment, not only in the Windows host environment.

## 5. Configure OpenRouter as the Codex provider

Back up the existing user configuration before editing it:

```bash
cp ~/.codex/config.toml ~/.codex/config.toml.before-openrouter
```

Edit:

```text
~/.codex/config.toml
```

Add the following:

```toml
# Route local Codex model requests through OpenRouter.
model_provider = "openrouter"

[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"
env_key_instructions = "Set OPENROUTER_API_KEY in the environment that starts Codex."
wire_api = "responses"
requires_openai_auth = false

# OpenRouter's Responses API currently uses HTTP/SSE rather than the Codex
# Responses WebSocket transport.
supports_websockets = false

# Optional resilience settings.
request_max_retries = 4
stream_max_retries = 5
stream_idle_timeout_ms = 300000

# Optional OpenRouter attribution headers. Remove this table entry if you do
# not have appropriate values.
http_headers = {
  "HTTP-Referer" = "https://your-project.example",
  "X-OpenRouter-Title" = "AI Paper Validation"
}
```

The attribution headers are optional. They do not control privacy, provider
routing, ZDR, or model selection.

Do not use:

```toml
experimental_bearer_token = "your-real-key"
```

Although Codex supports direct bearer-token configuration for development, an
environment variable is safer and is the documented preferred mechanism.

### 5.1 Global switch versus CLI-only profile

Setting:

```toml
model_provider = "openrouter"
```

in `~/.codex/config.toml` changes the default provider for local Codex clients
that use that configuration, including the CLI and IDE extension.

If OpenRouter should be optional for CLI runs only, define the provider in the
base user config but move the provider selection into a separate profile:

```text
~/.codex/openrouter.config.toml
```

Example profile:

```toml
model_provider = "openrouter"
model = "openai/gpt-5.6-sol"
model_reasoning_effort = "high"
```

Invoke it with:

```bash
codex --profile openrouter
```

or:

```bash
codex exec --profile openrouter "Perform a read-only package inventory."
```

Codex profiles are selected from the CLI. Current documentation does not
provide an equivalent normal VS Code setting for selecting a named CLI profile.
For the IDE extension, use the user-level default provider or launch VS Code in
an intentionally separate `CODEX_HOME` environment.

Do not manually override the extension's bundled CLI executable merely to
select a provider. That setting is intended for extension development and can
break extension behavior.

### 5.2 Dual-provider caution

The agent files contain explicit model names. After changing them to OpenRouter
model slugs such as `openai/gpt-5.6-terra`, those files are intended for the
OpenRouter provider.

If the same project must frequently switch between the built-in OpenAI provider
and OpenRouter, consider maintaining:

- Separate template variants, or
- Separate project copies/configurations, or
- Agent files without explicit models, allowing all agents to inherit the
  parent model

Removing explicit models is simpler but eliminates the existing Terra/Sol
cost-and-quality allocation.

## 6. Update the project and agent model names

OpenRouter model identifiers include the model publisher prefix. The current
template uses unprefixed OpenAI model names.

Apply this mapping:

| Current Codex model | OpenRouter model |
|---|---|
| `gpt-5.6-terra` | `openai/gpt-5.6-terra` |
| `gpt-5.6-sol` | `openai/gpt-5.6-sol` |

Both OpenRouter models currently advertise:

- Text input
- Image input
- File input
- Text output
- Tool calling
- Tool choice
- Reasoning controls
- Structured output controls

### 6.1 Root coordinator configuration

Update the active article project's `.codex/config.toml`:

```toml
model = "openai/gpt-5.6-sol"
model_reasoning_effort = "high"

[agents]
max_concurrent_threads_per_session = 6
max_depth = 1
```

`max_threads` is still accepted as a legacy alias:

```toml
[agents]
max_threads = 6
max_depth = 1
```

Using the current descriptive key is preferable for new configurations.

The root coordinator uses Sol because it makes routing, deduplication,
shortlisting, and final consolidation decisions. If cost is a stronger concern,
the root can use Terra, but the change should be validated against completed
article-package runs.

### 6.2 Custom agent files

Change the following files from:

```toml
model = "gpt-5.6-terra"
```

to:

```toml
model = "openai/gpt-5.6-terra"
```

Terra files:

```text
.codex/agents/ai-use-restriction-checker.toml
.codex/agents/main-text-extractor.toml
.codex/agents/package-inventory.toml
.codex/agents/pdf-preprocessor.toml
.codex/agents/report-generator.toml
.codex/agents/results-supplement-extractor.toml
.codex/agents/table-arithmetic-checker.toml
```

Change the following files from:

```toml
model = "gpt-5.6-sol"
```

to:

```toml
model = "openai/gpt-5.6-sol"
```

Sol files:

```text
.codex/agents/critic.toml
.codex/agents/evidence-verifier.toml
.codex/agents/figure-flow-checker.toml
.codex/agents/statistical-consistency-checker.toml
```

### 6.3 Verify that no old model identifiers remain

From the article-project root:

```bash
rg -n 'model = "gpt-5\.6-(terra|sol)"' .codex
```

Expected result:

```text
No matches
```

Confirm the new identifiers:

```bash
rg -n 'model = "openai/gpt-5\.6-(terra|sol)"' .codex
```

Expected result:

- Seven Terra agent matches
- Four Sol agent matches
- One root coordinator model if it is explicitly configured

## 7. Use the configuration from Codex CLI

### 7.1 Start an interactive local run

```bash
export OPENROUTER_API_KEY="replace-with-your-key"
codex -C /absolute/path/to/article-project
```

If using a CLI profile:

```bash
export OPENROUTER_API_KEY="replace-with-your-key"
codex --profile openrouter -C /absolute/path/to/article-project
```

### 7.2 Start a non-interactive smoke test

Use a harmless read-only prompt before processing PDFs:

```bash
codex exec -C /absolute/path/to/article-project \
  "List the configured custom agent names. Do not modify any files."
```

With a profile:

```bash
codex exec --profile openrouter \
  -C /absolute/path/to/article-project \
  "List the configured custom agent names. Do not modify any files."
```

### 7.3 Inspect the active configuration

Inside an interactive Codex session:

```text
/status
```

Check:

- Active model is `openai/gpt-5.6-sol` or the intended model.
- The provider is OpenRouter.
- The expected project root is active.
- Sandbox and approval settings are appropriate.

Then run:

```text
/debug-config
```

Check:

- The user-level provider definition is loaded.
- The project `.codex/config.toml` is loaded.
- The project is trusted.
- The project model is not unexpectedly overridden.

## 8. Use the configuration from the VS Code extension

1. Set `OPENROUTER_API_KEY` in the environment that will start VS Code.
2. Close every VS Code window.
3. Ensure background VS Code processes have exited.
4. Start VS Code from that environment.
5. Open the article project root, not the inert template directory.
6. Open the Codex sidebar.
7. Use the gear icon and select `Codex Settings`.
8. Open `config.toml` and confirm that the user-level provider definition is
   present.
9. Start a new local Codex chat.
10. Inspect the active model/provider through the available status UI or
    `/status`.

If VS Code still uses the OpenAI provider:

- Confirm that it was fully restarted.
- Confirm that the extension is operating locally.
- Confirm that `OPENROUTER_API_KEY` exists in the extension process
  environment.
- Confirm that the OpenRouter provider is in the user-level config, not only
  the project config.
- Confirm that the project is trusted so that project agent files load.
- Use `/debug-config` to see which layer supplied the active value.

Do not choose cloud delegation for a run that must use OpenRouter. Hosted
ChatGPT/Codex work does not read the local provider configuration.

## 9. Validate the provider migration

### 9.1 Parse and health checks

Run:

```bash
codex -C /absolute/path/to/article-project \
  --strict-config doctor --json
```

Look for:

```text
"model provider": "openrouter"
```

and the intended model.

`--strict-config` is useful because it turns unrecognized configuration keys
into errors instead of silently ignoring them.

### 9.2 Authentication smoke test

Run a short request that does not need tools:

```bash
codex exec -C /absolute/path/to/article-project \
  "Reply with exactly: OPENROUTER_PROVIDER_OK"
```

Expected output:

```text
OPENROUTER_PROVIDER_OK
```

### 9.3 Tool-call smoke test

Run:

```bash
codex exec -C /absolute/path/to/article-project \
  "Use a read-only filesystem command to list the project-root PDF filenames, then stop."
```

This checks:

- Responses API request compatibility
- Tool-call compatibility
- Tool-result return compatibility
- Multi-turn continuation after a tool call

### 9.4 Subagent smoke test

Use a small read-only task:

```text
Ask package_inventory to list the source PDF filenames and page counts.
Do not start full-text processing and do not modify source files.
```

Check that:

- The custom agent is discovered.
- The child model uses the OpenRouter slug.
- The child can use the required local tools.
- The result returns to the root coordinator.

### 9.5 Do not begin with a full package

OpenRouter's Responses API is currently described as beta and stateless. A
short smoke test is not enough to establish reliability for a long, parallel,
tool-heavy validation workflow. Test progressively:

1. Text-only request
2. Single tool call
3. Several tool calls
4. One custom subagent
5. Two parallel extractors
6. Three parallel checkers
7. One small article package
8. A representative full article package

Watch for:

- Invalid request fields
- Reasoning-field incompatibilities
- Dropped tool calls
- Malformed tool arguments
- SSE stream interruptions
- Rate limits
- Context-length failures
- Retry storms
- Provider routing changes

## 10. PDF and OCR behavior in the current workflow

### 10.1 What the template promises

The `pdf_preprocessor` agent is instructed to:

1. Use the package manifest.
2. Preserve source PDFs unchanged.
3. Extract native PDF text first.
4. Assess extraction quality per page.
5. Render and OCR missing, sparse, or corrupted pages.
6. Render/OCR pages containing required tables, figures, or flow diagrams.
7. Avoid default OCR of long protocol, SAP, or administrative material.
8. Write page-level manifests.
9. Preserve source-page references.
10. Update document-level processing records.

This is the correct high-level policy.

### 10.2 What the template does not provide

The template currently does not include:

- A reusable preprocessing script
- A dependency file
- An OCR-engine installer
- A PDF-tool health check
- Page-quality thresholds
- A stable page-manifest schema
- A deterministic failure policy
- OCR confidence thresholds
- Automated tests with scanned PDFs
- A check that OCR actually completed before marking preprocessing complete

The agent is therefore responsible for improvising the implementation during
each article run.

### 10.3 Evidence from an existing completed run

One existing run generated:

[`../jama.2025.7583/.ai_paper_validation/preprocessing/run_preprocessing.py`](../jama.2025.7583/.ai_paper_validation/preprocessing/run_preprocessing.py)

That script:

- Uses `pypdf` for native text extraction.
- Uses PyMuPDF (`fitz`) for 300-DPI page rendering.
- Uses Tesseract for OCR.
- Keeps native text, normalized text, OCR text, page images, and manifests.
- Hardcodes document filenames, classifications, page ranges, and visual
  pages for that specific article package.

It demonstrates the intended artifact architecture, but it is not a reusable
template implementation.

### 10.4 Reliability gaps in that generated implementation

The generated implementation contains several important weaknesses:

1. It can classify native extraction as `missing`, `sparse`, or `corrupted`.
2. It only invokes OCR inside the `if visual:` branch.
3. Therefore, a missing-text page not preselected as a visual page can be
   flagged as requiring OCR without actually being OCRed.
4. It always writes a document status saying native extraction is complete.
5. It does not require all necessary OCR operations to succeed before writing
   completion language.
6. It invokes `tesseract` without first checking that the executable exists.
7. If Tesseract is missing, process creation can raise an exception before a
   useful page-level failure record is written.
8. It uses `--psm 6` for all pages, even though a single uniform text-block
   assumption is not ideal for every journal page, table, or flow diagram.

At the time this guide was written, this environment had:

- `pdfinfo`: installed
- `pdftotext`: installed
- `pdftoppm`: installed
- `pdftocairo`: installed
- PyMuPDF: used successfully by prior artifacts
- `pypdf`: used successfully by prior artifacts
- Tesseract: not currently installed
- OCRmyPDF: not currently installed

Previously generated OCR artifacts show that Tesseract was available in the
environment used for that earlier run. Do not assume it remains available in a
new shell, machine, container, VS Code environment, or Codex sandbox.

### 10.5 What happens after only changing the provider

If only the provider and model names are changed:

- Codex still sees local PDF filenames.
- Agents can still call local shell and filesystem tools.
- Native extraction still depends on local tools.
- Rendering still depends on local tools.
- OCR still depends on a local OCR engine.
- OpenRouter does not automatically receive the raw PDF through its
  `file-parser` workflow.
- OpenRouter does not automatically install or call Tesseract.
- A missing OCR executable remains a local workflow failure.

## 11. Recommended provider-independent PDF architecture

Use this architecture:

```text
Source PDFs
    |
    v
Local package inventory
    |
    v
Local rights/compliance preflight
    |
    v
Native page extraction
    |
    v
Page-level quality and content classification
    |
    +-------------------------------+
    |                               |
    | acceptable prose page         | missing/sparse/corrupted/visual page
    |                               |
    v                               v
retain native text             render page at 300 DPI
                                    |
                                    v
                              run selective OCR
                                    |
    +-------------------------------+
    |
    v
Page artifact bundle:
native text + normalized text + OCR text + PNG + manifest
    |
    v
OpenRouter-powered Codex extraction/checking agents
    |
    v
Evidence verifier reopens the original PDF and/or rendered source page
```

The key principle is:

> PDF decoding and OCR are deterministic preprocessing operations. Model
> reasoning should consume their outputs, not own the only implementation of
> those operations.

### 11.1 Where the reusable implementation should live

Add a reusable, version-controlled implementation to the template:

```text
multi_agent_template/
├── scripts/
│   ├── preprocess_pdfs.py
│   ├── check_pdf_dependencies.py
│   └── validate_page_manifest.py
├── requirements-pdf.txt
├── tests/
│   └── pdf_fixtures/
└── ...
```

When copied into an article project:

```text
<article-project>/
├── scripts/
│   ├── preprocess_pdfs.py
│   ├── check_pdf_dependencies.py
│   └── validate_page_manifest.py
├── requirements-pdf.txt
└── ...
```

Scripts may write only beneath:

```text
.ai_paper_validation/
```

They must never rewrite, rename, move, or overwrite a source PDF.

### 11.2 Recommended processing phases

#### Phase A: Dependency preflight

Record:

- Tool name
- Resolved executable path
- Version
- Availability
- Required or optional status

Fail before package processing if a required dependency is missing.

#### Phase B: Source inventory

For every PDF, record:

- Stable document ID
- Filename
- File size
- SHA-256 checksum
- Page count
- PDF metadata
- Whether any native text is present
- Likely document classification
- Intended scientific audit scope

#### Phase C: Native extraction

Extract each page independently. Do not produce only one whole-document text
file because page-level evidence must be retained.

Possible tools:

- `pdftotext`
- `pypdf`
- PyMuPDF

Keep the raw native extraction before normalization.

#### Phase D: Quality classification

Classify each page using explicit, testable criteria such as:

- `acceptable`
- `missing`
- `sparse`
- `corrupted`
- `layout-risk`
- `visual-review-required`

Illustrative signals:

- Extracted character count
- Extracted word count
- Replacement-character frequency
- Nonprinting-character frequency
- Alphanumeric-to-total-character ratio
- Repeated-glyph runs
- Extreme line fragmentation
- Suspected two-column reading-order problems
- Table, figure, flowchart, or eFigure labels
- Page image coverage

Thresholds must be validated against representative journal PDFs rather than
treated as universal constants.

#### Phase E: Selective rendering

Render:

- Every page requiring OCR
- Every result-relevant table page
- Every result-relevant figure page
- Every participant flow page
- Every page needed for exact visual verification

Use approximately 300 DPI for OCR. Higher resolution increases storage and
processing cost and should be justified by small typography or poor scans.

#### Phase F: Selective OCR

OCR:

- Missing native-text pages
- Sparse native-text pages
- Corrupted native-text pages
- Scanned pages
- Required visual pages when OCR helps locate labels and values

Do not replace usable native text with OCR text. Retain both.

#### Phase G: Normalization

Normalization should:

- Normalize Unicode consistently.
- Preserve page boundaries.
- Preserve line breaks where they carry table or list meaning.
- Avoid merging table columns into invented prose.
- Avoid silently correcting numeric values.
- Record every transformation.

#### Phase H: Manifest validation

Before downstream agents start, verify:

- Every in-scope page has a page entry.
- Every entry names its source PDF and page.
- Every declared artifact exists.
- Every required OCR page has `ocr_status = "completed"`.
- Every visual-review page has a rendered image.
- Excluded documents have an explicit `Not Audited by Design` record.
- Source checksums are unchanged.

### 11.3 Example page-manifest entry

```json
{
  "document_id": "DOC-001-MAIN",
  "source_pdf": "main.pdf",
  "source_sha256": "replace-with-real-hash",
  "source_page": 4,
  "scientific_scope": true,
  "content_flags": [
    "table",
    "participant-flow"
  ],
  "native_extraction": {
    "status": "completed",
    "quality": "acceptable",
    "characters": 3990,
    "path": ".ai_paper_validation/preprocessing/DOC-001-MAIN/native_text/page-004.txt",
    "tool": "pypdf",
    "tool_version": "replace-with-real-version"
  },
  "rendering": {
    "required": true,
    "status": "completed",
    "dpi": 300,
    "path": ".ai_paper_validation/preprocessing/DOC-001-MAIN/page_images/page-004.png",
    "tool": "PyMuPDF",
    "tool_version": "replace-with-real-version"
  },
  "ocr": {
    "required": true,
    "status": "completed",
    "path": ".ai_paper_validation/preprocessing/DOC-001-MAIN/ocr_text/page-004.txt",
    "engine": "tesseract",
    "engine_version": "replace-with-real-version",
    "language": "eng",
    "page_segmentation_mode": 3,
    "mean_confidence": null
  },
  "downstream_use": [
    "main_text_extractor",
    "table_arithmetic_checker",
    "figure_flow_checker",
    "evidence_verifier"
  ]
}
```

### 11.4 Completion policy

Do not mark preprocessing complete merely because native extraction was
attempted.

Use a fail-closed policy:

```text
Complete:
  Every in-scope page has acceptable native text, or every required fallback
  rendering/OCR operation completed and the required artifacts exist.

Complete with warnings:
  Processing completed, but one or more pages remain low confidence and are
  explicitly routed for human visual verification.

Failed:
  A required dependency is missing, a required page could not be rendered,
  required OCR failed, or page provenance cannot be established.
```

## 12. Implementing reliable local OCR

### 12.1 Recommended local tools

Native extraction and PDF information:

- Poppler: `pdfinfo`, `pdftotext`, `pdftoppm`, `pdftocairo`
- `pypdf`
- PyMuPDF

OCR:

- Tesseract for local open-source OCR
- OCRmyPDF when a derived searchable PDF is useful

OCRmyPDF must write to a derived PDF under `.ai_paper_validation/`. It must
never write over the supplied source PDF.

### 12.2 Example dependency file

`requirements-pdf.txt`:

```text
pymupdf
pypdf
```

Pin exact versions after validating the workflow in the target environment.
Unpinned lines above illustrate the required packages, not a reproducible lock
file.

### 12.3 Example health checks

POSIX shell:

```bash
pdfinfo -v
pdftotext -v
pdftoppm -v
tesseract --version
ocrmypdf --version
python -c "import fitz, pypdf; print('Python PDF dependencies OK')"
```

The script should distinguish required and optional tools. For example:

- Poppler or a Python PDF library: required
- At least one page renderer: required
- OCR engine: required if any page needs OCR
- OCRmyPDF: optional if Tesseract page OCR is used directly

### 12.4 Installation examples

These are examples only. Use the package-management and security process
approved for the target machine.

Ubuntu/Debian:

```bash
sudo apt-get update
sudo apt-get install poppler-utils tesseract-ocr
python -m pip install -r requirements-pdf.txt
```

macOS with Homebrew:

```bash
brew install poppler tesseract
python -m pip install -r requirements-pdf.txt
```

Windows:

- Install Poppler through an approved Windows package or binary distribution.
- Install Tesseract through an approved package or installer.
- Add their executable directories to `PATH`.
- Restart VS Code after changing `PATH`.
- Install Python dependencies in the environment used by Codex.

### 12.5 OCR strategy for journal pages

Do not assume one Tesseract page segmentation mode is correct for every page.

Examples:

- Automatic full-page layout: consider `--psm 3`.
- A known single uniform block: consider `--psm 6`.
- Sparse figure labels: consider a sparse-text mode.
- Cropped table cells or labels: use region-specific OCR if necessary.

The exact mode should be recorded per page. If multiple OCR passes are used,
retain the chosen output and record why it was selected.

### 12.6 Tables and flow diagrams

OCR is not enough for table or flow-diagram verification because it can lose:

- Column alignment
- Row grouping
- Superscripts
- Footnote markers
- Inequality signs
- Decimal points
- Negative signs
- Confidence-interval punctuation
- Arrow direction
- Box grouping

For these pages:

1. Retain native text.
2. Retain OCR text.
3. Retain a high-resolution rendered page.
4. Have the visual checker inspect the image.
5. Have the evidence verifier reopen the original PDF or source-linked image.
6. Treat unresolved visual ambiguity as `Uncertain`, not `Verified`.

## 13. Optional OpenRouter-managed PDF parsing and OCR

OpenRouter documents PDF input support through its API. A PDF can be provided
as:

- A public URL
- A base64-encoded data URL
- An uploaded file reference, where supported

For local or private PDFs, base64 or an authenticated upload is required.

OpenRouter's documented PDF processing engines currently include:

| Engine | Intended use | Current documented behavior |
|---|---|---|
| `native` | Model natively supports file/PDF input | PDF is passed to the model |
| `cloudflare-ai` | PDF-to-Markdown parsing | Currently documented as free |
| `mistral-ocr` | Scanned or image-heavy PDF | Currently documented at $2 per 1,000 pages |

Pricing and capabilities can change. Verify the live OpenRouter documentation
before production use.

### 13.1 Why the provider switch does not automatically use this feature

The OpenRouter PDF examples explicitly attach a PDF as request content and
configure:

```json
{
  "plugins": [
    {
      "id": "file-parser",
      "pdf": {
        "engine": "mistral-ocr"
      }
    }
  ]
}
```

Codex's custom provider configuration supplies:

- Base URL
- Authentication
- Headers
- Retry behavior
- Responses protocol selection

It does not provide a normal configuration field that means:

```text
For every workspace PDF, attach the file to the request and add the
OpenRouter file-parser plugin.
```

The Responses API schema may expose a `plugins` request field, but Codex's
provider configuration does not expose arbitrary request-body injection for
this workflow. In addition, Codex normally accesses workspace PDFs through
local tools rather than automatically treating each one as an API file
attachment.

### 13.2 When an OpenRouter OCR helper may be appropriate

Use a separate helper only when:

- Local OCR is unavailable or demonstrably inadequate.
- Uploading the document is permitted.
- The rights/compliance screen has been completed.
- OpenRouter and downstream-provider privacy settings are acceptable.
- Cost is acceptable.
- Page-level provenance is reconstructed explicitly.

The helper should be a preprocessing tool called by `pdf_preprocessor`, not an
implicit assumption in the model-provider configuration.

### 13.3 Illustrative Python helper

The following is a conceptual example. It uploads the PDF contents to
OpenRouter and therefore must not be run until compliance, privacy, and
authorization requirements are satisfied.

```python
from __future__ import annotations

import base64
import json
import os
from pathlib import Path

import requests


def parse_pdf_with_openrouter(
    pdf_path: Path,
    output_path: Path,
    *,
    model: str = "openai/gpt-5.6-terra",
    engine: str = "mistral-ocr",
) -> None:
    api_key = os.environ["OPENROUTER_API_KEY"]
    pdf_bytes = pdf_path.read_bytes()
    encoded = base64.b64encode(pdf_bytes).decode("ascii")
    data_url = f"data:application/pdf;base64,{encoded}"

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Extract the document faithfully. Do not infer or "
                            "correct values. Preserve visible headings, table "
                            "labels, figure labels, and page boundaries when "
                            "available."
                        ),
                    },
                    {
                        "type": "file",
                        "file": {
                            "filename": pdf_path.name,
                            "file_data": data_url,
                        },
                    },
                ],
            }
        ],
        "plugins": [
            {
                "id": "file-parser",
                "pdf": {
                    "engine": engine,
                },
            }
        ],
        "stream": False,
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "X-OpenRouter-Title": "AI Paper Validation PDF Preprocessor",
        },
        json=payload,
        timeout=300,
    )
    response.raise_for_status()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(response.json(), indent=2) + "\n",
        encoding="utf-8",
    )
```

Production code must additionally:

- Avoid logging the API key.
- Handle `429`, `502`, and `503`.
- Honor `Retry-After`.
- Record source checksums.
- Validate response content.
- Preserve parsed file annotations.
- Save error-path file annotations when returned.
- Record the OpenRouter model and parser engine.
- Reconstruct source-page provenance.
- Avoid declaring success when page mapping is missing.

### 13.4 Reuse file annotations

OpenRouter may return file annotations containing parsed text and images. Send
those annotations back in later requests to avoid reparsing and duplicate OCR
charges.

Persist them under a document-specific derived path, for example:

```text
.ai_paper_validation/document_outputs/<document_id>/openrouter_file_annotations.json
```

Do not treat OpenRouter's annotation hash as a replacement for the local
source-file SHA-256 checksum.

### 13.5 Eight-image limitation

OpenRouter currently documents that Mistral OCR extracts at most eight images
per PDF for forwarding to the downstream model. Additional extracted images
are dropped, although extracted text is retained.

This is a serious limitation for:

- Long supplements
- Figure-heavy articles
- Multi-page tables
- Flow diagrams
- Page-by-page evidence verification

If OpenRouter OCR is used for these materials, split only the permitted derived
copy into single-page or small page-range PDFs and map each derived file back
to its exact source PDF page. Never split or rewrite the source PDF itself.

### 13.6 Page-level fallback pattern

Recommended fallback:

```text
source.pdf page 12
    -> local rendered page-012.png
    -> optional derived single-page PDF
    -> OpenRouter OCR request
    -> save raw response and annotations
    -> save normalized OCR text
    -> manifest records source.pdf, page 12, parser, model, and paths
```

This reduces ambiguity and avoids depending on whole-document annotation order
for source-page provenance.

## 14. Privacy, retention, routing, and compliance

The source workflow requires an AI Training Restriction screen before
full-text model-mediated processing. Preserve that ordering.

### 14.1 Data path after migration

With local preprocessing:

```text
Raw PDF
  -> local extraction/rendering/OCR
  -> selected text and page images enter Codex model context
  -> Codex sends that context to OpenRouter
  -> OpenRouter routes it to the selected model provider endpoint
```

With OpenRouter-managed PDF parsing:

```text
Raw PDF
  -> OpenRouter
  -> PDF parser/OCR service when applicable
  -> selected model provider
```

The second path exposes the raw PDF to more external processing components and
must be reviewed separately.

### 14.2 OpenRouter and downstream providers are distinct

OpenRouter routes requests to model-provider endpoints. Provider data policies
can differ regarding:

- Prompt logging
- Retention
- Abuse monitoring
- Training
- Model improvement
- Geographic processing

Do not assume that selecting an OpenAI-authored model slug guarantees one
specific hosting provider or data policy unless routing is constrained.

### 14.3 Recommended API-key guardrail

Create a dedicated OpenRouter guardrail for the paper-validation key:

- Allow only the intended model slugs.
- Allow only approved hosting providers.
- Enforce Zero Data Retention where required.
- Disable providers that may train on prompts.
- Disable prompt logging unless explicitly authorized.
- Apply an appropriate budget.
- Consider disabling fallback routing if provider identity must remain fixed.

Account-level or API-key guardrails are especially important because Codex's
custom provider definition does not expose every OpenRouter request-body
routing preference.

### 14.4 Compliance record

For every run, retain:

- Source PDF identifier and checksum
- AI Training Restriction status
- Human Compliance Review flag
- Whether raw PDF bytes left the local environment
- Whether OCR was local or remote
- OCR provider and engine
- Inference model slug
- Routed provider when available
- ZDR/retention policy applied
- Processing timestamp
- Tool and model versions

Do not turn these records into a legal conclusion. They are operational
compliance evidence for human review.

### 14.5 Scientific workflow restrictions remain active

Changing the provider does not relax the workflow's scientific constraints:

- No web search for scientific findings
- No external factual retrieval
- No unstated medical or statistical knowledge as evidence
- No misconduct assessment
- No raw-data validity claims
- No general methodological critique
- No modification of source PDFs
- No more than 10 candidates sent to verification
- No more than two verification rounds per candidate
- No more than 10 final scientific issues

## 15. Model and cost strategy

The current role allocation can be preserved exactly:

### Terra roles

Use:

```text
openai/gpt-5.6-terra
```

for:

- Inventory
- Rights screening
- PDF preprocessing orchestration
- Evidence extraction
- Table arithmetic
- Report formatting

### Sol roles

Use:

```text
openai/gpt-5.6-sol
```

for:

- Figure and flow interpretation
- Statistical consistency
- Evidence verification
- Criticism
- Root coordination, if maximum consolidation quality is desired

### Concurrency

The project currently permits six concurrent subagent threads. OpenRouter
requests are billed independently, and subagents consume more tokens than a
single-agent workflow.

Before retaining six threads, verify:

- OpenRouter API-key rate limits
- Model-provider concurrency limits
- Budget
- Stream stability
- Retry behavior

The workflow's actual parallel stages require only:

- Two simultaneous extractors
- Three simultaneous checkers

A concurrency cap of three or four may be adequate if rate limits or budget are
more important than maximum throughput.

### Reproducibility

For validation work, avoid an automatic model router unless variability is
acceptable. Pin explicit model slugs and, where needed, provider endpoints.

Record:

- Requested model slug
- Canonical model version when available
- Provider route when available
- Reasoning effort
- Date
- Codex version
- OpenRouter request/error identifiers

## 16. End-to-end migration test plan

### Test package A: Native-text article

Include:

- One normal article PDF
- No supplements
- Searchable text
- One table
- One figure

Pass criteria:

- Inventory succeeds.
- No unnecessary whole-document OCR occurs.
- Native page text is retained.
- Table/figure pages are rendered.
- Downstream agents can inspect artifacts.
- Final citations retain exact PDF pages.

### Test package B: Scanned page

Include:

- A PDF with one page lacking a text layer
- The scanned page should not depend on being manually preclassified as visual

Pass criteria:

- Page quality is `missing` or `sparse`.
- OCR is automatically required.
- OCR completes.
- The manifest records the OCR engine and page.
- Preprocessing fails if the OCR engine is intentionally removed.

### Test package C: Table and flow diagram

Include:

- A multi-column table
- A participant flow diagram
- Small footnotes
- Confidence intervals and P values

Pass criteria:

- Native text, OCR text, and images are all retained.
- Agents do not use OCR text as the sole evidence.
- Visual verification catches intentionally ambiguous OCR.
- Unresolved ambiguity is marked `Uncertain`.

### Test package D: Long supplement

Include:

- Results supplement
- Protocol
- SAP
- Administrative supplement

Pass criteria:

- Results pages are processed.
- Protocol/SAP/administrative scientific content is `Not Audited by Design`.
- Every PDF still receives a rights record.
- No full-document OCR is performed on excluded long documents.

### Test package E: OpenRouter failure

Simulate or safely encounter:

- Invalid key
- Rate limit
- Provider unavailable
- Stream interruption
- Unsupported parameter

Pass criteria:

- Errors are retained.
- No partial output is labeled complete.
- Retries are bounded.
- Source PDFs remain unchanged.
- The workflow can resume without repeating completed local preprocessing.

### Test package F: Remote OCR fallback

Use only an authorized non-sensitive fixture.

Pass criteria:

- Raw upload is recorded.
- Parser engine is recorded.
- File annotations are saved.
- Repeated requests reuse annotations.
- Source page mapping is explicit.
- The eight-image limit is tested or avoided through page chunking.

## 17. Troubleshooting

### Codex reports that the API key is missing

Symptoms:

- Missing environment variable
- Authentication error before inference

Checks:

```bash
if [ -n "${OPENROUTER_API_KEY:-}" ]; then
  echo "set"
else
  echo "missing"
fi
```

Fix:

- Set the key in the environment that starts Codex.
- Fully restart VS Code after changing the environment.
- Confirm `env_key = "OPENROUTER_API_KEY"`.

### HTTP 401

Likely causes:

- Invalid OpenRouter key
- Disabled key
- Incorrect bearer token
- Codex process inherited an old value

Fix:

- Rotate or reissue the key.
- Restart the client process.
- Do not print the key into logs while diagnosing.

### HTTP 402

Likely cause:

- Insufficient OpenRouter credits or budget

Fix:

- Check key budget, account credits, and guardrail budget.

### HTTP 404 or model not found

Likely causes:

- Used `gpt-5.6-sol` instead of `openai/gpt-5.6-sol`
- Used `gpt-5.6-terra` instead of `openai/gpt-5.6-terra`
- Model allowlist blocks the requested model
- Model availability changed

Fix:

- Verify the live OpenRouter model catalog.
- Verify the exact slug.
- Review key guardrails.

### `invalid_prompt` or HTTP 400

Likely causes:

- OpenRouter Responses beta rejected a request field
- A tool schema was incompatible
- Context was too large
- A model/provider did not support a required parameter

Fix:

- Reproduce with a minimal prompt.
- Test text-only, then tools, then reasoning.
- Inspect OpenRouter's top-level `error_type`.
- Confirm the selected model supports `tools`, `tool_choice`, and `reasoning`.
- Reduce context or page batches.

### Tool calls do not work

Checks:

- Model catalog lists `tools`.
- Model catalog lists `tool_choice`.
- A basic one-tool smoke test succeeds.
- OpenRouter Responses API is being used.
- The request is not routed to a provider endpoint lacking a parameter.

Fix:

- Pin a compatible model/provider.
- Use a guardrail/provider allowlist.
- Avoid automatic routers during validation.

### VS Code still shows the OpenAI provider

Likely causes:

- Provider was placed only in project config and was ignored.
- VS Code was not restarted.
- The extension process lacks `OPENROUTER_API_KEY`.
- The chat is a cloud task.
- An existing chat retained old session configuration.

Fix:

- Put provider configuration in `~/.codex/config.toml`.
- Restart VS Code.
- Start a new local chat.
- Inspect `/debug-config`.

### Custom agents are missing

Likely causes:

- Project is untrusted.
- `.codex/agents/` was not copied.
- Agent TOML lacks `name`, `description`, or `developer_instructions`.
- VS Code opened the wrong folder.

Fix:

- Open the article-project root.
- Trust the project.
- Validate the agent TOML files.
- Start a new session after config changes.

### OCR executable not found

Symptoms:

- `FileNotFoundError`
- No OCR text file
- Agent improvises around missing OCR

Fix:

- Install and validate an OCR engine before processing.
- Add an explicit dependency preflight.
- Fail the preprocessing stage if OCR is required and unavailable.

### OCR completes but values are wrong

Fix:

- Retain and compare native text.
- Inspect the rendered image.
- Try a more appropriate page segmentation mode.
- Crop and OCR only the relevant region.
- Route ambiguity to visual and human verification.
- Never silently correct values based only on plausibility.

### Rate limits during parallel stages

Fix:

- Lower `max_concurrent_threads_per_session`.
- Reduce simultaneous agents.
- Honor `Retry-After`.
- Use bounded retries.
- Avoid rerunning completed preprocessing.
- Check API-key and provider rate limits.

### Long sessions become expensive

Contributing factors:

- OpenRouter Responses API is stateless.
- Tool and conversation history may be resent.
- Subagents have independent context and token use.
- Large OCR text and page images increase input size.

Mitigations:

- Keep evidence maps compact.
- Process page ranges selectively.
- Do not place whole protocols/SAPs into context.
- Archive preprocessing results locally.
- Reuse remote PDF annotations if remote parsing is used.
- Keep the 10-candidate limit.

### The `openaiDeveloperDocs` MCP server appears in Codex

That MCP server provides documentation lookup. It is unrelated to the model
provider and does not route Codex inference through OpenAI. Its presence does
not prevent OpenRouter from being the configured model provider.

## 18. Rollback

### 18.1 Restore the user configuration

If a backup was created:

```bash
cp ~/.codex/config.toml.before-openrouter ~/.codex/config.toml
```

Or change:

```toml
model_provider = "openrouter"
```

back to:

```toml
model_provider = "openai"
```

### 18.2 Restore model identifiers

Change:

```toml
model = "openai/gpt-5.6-terra"
```

back to:

```toml
model = "gpt-5.6-terra"
```

and:

```toml
model = "openai/gpt-5.6-sol"
```

back to:

```toml
model = "gpt-5.6-sol"
```

### 18.3 Restart clients

After rollback:

- Close and restart Codex CLI sessions.
- Close and restart VS Code.
- Start a new chat.
- Verify `/status`.

Do not delete `.ai_paper_validation/` merely because the provider changed.
Retained preprocessing and audit evidence may still be required.

## 19. Migration checklist

### Provider

- [ ] Create a dedicated OpenRouter API key.
- [ ] Configure budget and guardrails.
- [ ] Set `OPENROUTER_API_KEY` outside the repository.
- [ ] Define `[model_providers.openrouter]` in user-level config.
- [ ] Set `wire_api = "responses"`.
- [ ] Set `requires_openai_auth = false`.
- [ ] Set `supports_websockets = false`.
- [ ] Do not put provider/auth config in project `.codex/config.toml`.

### Models

- [ ] Root model is `openai/gpt-5.6-sol` or the intentionally selected model.
- [ ] All Terra agents use `openai/gpt-5.6-terra`.
- [ ] All Sol agents use `openai/gpt-5.6-sol`.
- [ ] No unprefixed old model names remain.
- [ ] Live model catalog confirms tool, reasoning, image, and file support.

### CLI and IDE

- [ ] `codex doctor --strict-config` parses the configuration.
- [ ] `/status` shows OpenRouter and the intended model.
- [ ] `/debug-config` shows the expected configuration layers.
- [ ] Text-only smoke test passes.
- [ ] Tool-call smoke test passes.
- [ ] Custom subagent smoke test passes.
- [ ] VS Code is using a local, not cloud, run.

### PDF processing

- [ ] Native extraction tool is installed.
- [ ] Page renderer is installed.
- [ ] OCR engine is installed before any page requires OCR.
- [ ] Reusable preprocessor exists outside generated article outputs.
- [ ] Missing/sparse/corrupted nonvisual pages trigger OCR.
- [ ] Tables, figures, and flow diagrams are rendered.
- [ ] Native text, OCR text, and page images are retained separately.
- [ ] Every artifact maps to source PDF and exact page.
- [ ] Required OCR failures prevent a complete status.
- [ ] Source PDF checksums remain unchanged.

### Privacy and compliance

- [ ] Every PDF has an AI Training Restriction Record.
- [ ] Human Compliance Review is performed when required.
- [ ] API-key guardrail restricts models/providers appropriately.
- [ ] ZDR is enabled where required.
- [ ] Prompt logging/training policy is reviewed.
- [ ] Raw-PDF upload is separately recorded and approved.
- [ ] Remote OCR parser/provider is recorded.
- [ ] No scientific web search or external evidence is introduced.

### Validation

- [ ] Native-text fixture passes.
- [ ] Scanned-page fixture passes.
- [ ] Table/flow fixture passes.
- [ ] Long-supplement scoping passes.
- [ ] Provider-failure behavior passes.
- [ ] Remote OCR fallback is tested only with authorized data.
- [ ] Final report preserves page-level evidence and human adjudication.

## 20. Documentation references

### Codex

- Config basics: <https://developers.openai.com/codex/config-basic/>
- Advanced configuration: <https://developers.openai.com/codex/config-advanced/>
- Configuration reference: <https://developers.openai.com/codex/config-reference/>
- Configuration schema: <https://developers.openai.com/codex/config-schema.json>
- Custom subagents: <https://developers.openai.com/codex/subagents/>
- IDE extension: <https://developers.openai.com/codex/ide/>
- IDE/developer settings: <https://developers.openai.com/codex/ide/settings/>

### OpenRouter

- Quickstart: <https://openrouter.ai/docs/quickstart>
- Responses API overview: <https://openrouter.ai/docs/api/reference/responses/overview>
- Responses API request reference: <https://openrouter.ai/docs/api/api-reference/responses/create-responses>
- Tool calling: <https://openrouter.ai/docs/guides/features/tool-calling>
- Model catalog documentation: <https://openrouter.ai/docs/guides/overview/models>
- Live model catalog: <https://openrouter.ai/api/v1/models>
- PDF inputs and parser engines: <https://openrouter.ai/docs/guides/overview/multimodal/pdfs>
- Plugins overview: <https://openrouter.ai/docs/guides/features/plugins/overview>
- Error handling: <https://openrouter.ai/docs/api/reference/errors-and-debugging>
- Provider routing: <https://openrouter.ai/docs/guides/routing/provider-selection>
- Zero Data Retention: <https://openrouter.ai/docs/guides/features/zdr>
- Provider logging and retention: <https://openrouter.ai/docs/guides/privacy/provider-logging/>
- Guardrails: <https://openrouter.ai/docs/guides/features/guardrails/overview>

