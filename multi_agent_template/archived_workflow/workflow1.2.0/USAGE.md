# Workflow 1.2.0 使用方式

## 1. 先判定适用性

只在下面条件同时成立时使用：

- 论文包根目录只有主论文和支持文件；
- 来源可以是 PDF、DOCX、XLSX、DOC、XLS 或 CSV；
- 没有旧的 `.ai_paper_validation/candidate_set.md`、`checker_outputs/`、`verification/`、
  `critic/` 或旧 `final_report.md`；
- 目标是在该单篇论文内从零开始。

已有 1.0 记录时不要用本版本：未跑 endetail 用 1.2.1，已跑 endetail 用 1.2.2。

## 2. 复制补丁内容

必须复制目录内容，包括隐藏 `.codex`，而不是把 `workflow1.2.0` 整个目录套进论文包：

```bash
cp -a /absolute/path/to/workflow1.2.0/. /absolute/path/to/<paper>/
```

确认论文包根目录现在直接包含 `AGENTS.md`、`START_PROMPT.md`、`.codex/` 和
`workflow_1_2_0/`。不要创建或预填 `.ai_paper_validation/`。

## 3. 在 Linux CPU 环境启动新会话

```bash
codex --cd /absolute/path/to/<paper> --ask-for-approval never --sandbox workspace-write
```

不要使用 `resume`。项目配置会禁止执行确认提示，并把写入范围限制在论文包 workspace。
流程不会探测 GPU；缺少 CPU OCR、LibreOffice 或 Pandoc 时采用记录限制、结构化 Office
抽取或内置 HTML fallback，不会询问你如何选择。

## 4. 发送第一条请求

把 `START_PROMPT.md` 全文作为第一条请求。之后不需要再发送 “turbo”、continue 或确认
指令。Codex 会自行运行预检、并行 specialist、两轮统计核对、最多 10 个的人审队列、
Markdown/HTML 和校验器。

## 5. 检查成功标志

必须同时存在：

- `.ai_paper_validation/final_report_1_2_0.md`
- `.ai_paper_validation/final_report_1_2_0.html`
- `.ai_paper_validation/audit_validation_1_2_0.json`

最后一个文件的 `status` 必须为 `PASS`。`candidate_ledger.md` 可超过 10 个；
`review_queue.md` 和最终报告不得超过 10 个。源文件哈希必须保持不变。

## 6. 预检自动停止的情况

如果检测到旧 1.0 痕迹，1.2.0 会写明应使用恢复版本并停止，不会让你现场选择，也不会
覆盖旧记录。
