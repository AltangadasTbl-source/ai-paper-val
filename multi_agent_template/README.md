# Codex Agent Workflow Template

This folder is inert. Codex does not load it as project configuration.

Use one project for one article package. Place the article files directly in the project root:

```text
<article-project>/
├── main.pdf
├── supplement_1.pdf
├── supplement_2.pdf
└── codex_agent_workflow_template/
```

The root thread identifies the main article and supplementary files from the package inventory.
It does not require a fixed filename, but `main.pdf` and `supplement_<n>.pdf` are recommended.

To activate the workflow in a new project, copy:

```text
codex_agent_workflow_template/config.toml
    -> <article-project>/.codex/config.toml

codex_agent_workflow_template/agents/
    -> <article-project>/.codex/agents/

codex_agent_workflow_template/AGENTS.md
    -> <article-project>/AGENTS.md

codex_agent_workflow_template/scripts/
    -> <article-project>/scripts/
```

The workflow writes derived text, page images, and agent artifacts only under
`<article-project>/.ai_paper_validation/`. It must not modify source PDFs.

It also creates a retained output record for every supplied document. The record includes document
classification, selected audit scope, extraction/OCR status, agent outputs, and an `AI Training
Restriction` screen. The screen checks only supplied materials and is a compliance flag, not a legal
opinion or a scientific reporting finding.

The root thread acts as `Coordinator`. Do not copy these files to `C:\Users\juliz\.codex`.

## OCR acceleration and fallback

The template includes `scripts/detect_ocr_backend.py` and `scripts/ocr_page.py`. Run them with
`~/venvs/stt/bin/python` when it exists. The backend selector detects the RTX 5070 Laptop GPU and
other usable NVIDIA GPUs, then uses RapidOCR with ONNX Runtime CUDA only after validating the
detector, classifier, and recognizer sessions. On a computer without a usable GPU, it automatically
uses RapidOCR CPU or, if RapidOCR is unavailable, Tesseract CPU. The resulting JSON metadata must
be retained in `.ai_paper_validation/`; never describe a CPU fallback as GPU OCR.
