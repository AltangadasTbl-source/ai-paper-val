# Workflow 1.2.0：只有论文与支持文件时的全新运行

适用场景：一个论文包里只有主论文和支持文件，还没有 1.0/1.1 的
`.ai_paper_validation/` 运行记录。支持的直接来源包括 PDF、DOCX、XLSX，也兼容 DOC、XLS
和 CSV；其中旧式 DOC/XLS 若本机没有 LibreOffice，会作为明确的人工核验限制记录下来。

本版本从零开始，但吸收了 1.0 与 1.1 的修正：发现台账不限数量、人工 review 队列最多
10 个；不作 AI 有效性/严重性裁决；强制两轮统计核对；XLSX 不再被“只允许 PDF link”
排除；校验器真正检查源哈希、候选守恒、coverage unit 和两轮统计状态；Linux 默认
CPU-only；Pandoc 缺失时有本地 HTML fallback。

## 给每篇论文安装

将本目录的全部内容（包括隐藏 `.codex`）复制到该论文包根目录：

```bash
cp -a /absolute/path/to/workflow1.2.0/. <paper>/
```

复制后：

```text
<paper>/
├── AGENTS.md
├── START_PROMPT.md
├── CONTRADICTIONS_RESOLVED.md
├── .codex/
├── workflow_1_2_0/
├── main-paper.pdf              # 名称不固定，也可为 DOCX
├── support.pdf                 # 可选
├── support.docx                # 可选
└── support.xlsx                # 可选
```

单独启动一个全新 Codex 会话，不使用 `resume`：

```bash
codex --cd <paper> --ask-for-approval never --sandbox workspace-write
```

把 `START_PROMPT.md` 作为第一条请求。项目配置已经采用 `approval_policy = "never"`，所以
不会询问是否执行、是否继续或是否启用“turbo”；无法执行的越权/缺工具动作会被记录，
不会变成现场选择题。

## 不适用场景

- 已有 1.0 记录、未跑 endetail：使用 workflow 1.2.1。
- 已有 1.0 记录、已跑 endetail：使用 workflow 1.2.2。
- 预检会自动阻止把 1.2.0 用在旧记录包上。

## 主要输出

```text
.ai_paper_validation/
├── source_inventory.json
├── package_manifest.md
├── coverage_manifest.json
├── candidate_ledger.md             # 不限数量
├── verification/evidence_recheck.md
├── quality/evidence_quality_audit.md
├── review_queue.md                 # 最多 10 个
├── final_report_1_2_0.md
├── final_report_1_2_0.html
└── audit_validation_1_2_0.json     # 必须 PASS
```
