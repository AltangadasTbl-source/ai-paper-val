# Workflow 1.2.1 使用方式

## 1. 先判定适用性

用于已经完成 workflow 1.0、但 `.ai_paper_validation/final_report.md` **尚未**经过
`final_report_endetail_prompt.md` 二次扩写的论文包。必须保留原始 PDF/Office 文件和整个
`.ai_paper_validation/`。

若报告已有 `Candidate Disposition Summary`、`Uncertain Candidates`、
`Rejected and Excluded Interpretations` 等 endetail 结构，请用 1.2.2。

## 2. 备份旧管理文件

```bash
mkdir -p /absolute/path/to/<paper>/.workflow1.0_management_backup
cp -a /absolute/path/to/<paper>/AGENTS.md /absolute/path/to/<paper>/.workflow1.0_management_backup/AGENTS.md
cp -a /absolute/path/to/<paper>/.codex /absolute/path/to/<paper>/.workflow1.0_management_backup/.codex
```

这里只备份项目指令和 agent 配置；不要移动、重命名或复制
`.ai_paper_validation/` 到别处。

## 3. 复制 1.2.1 内容

```bash
cp -a /absolute/path/to/workflow1.2.1/. /absolute/path/to/<paper>/
```

必须复制隐藏 `.codex`。旧 `.codex/agents/` 中未同名的 1.0 role 可以保留；新的
`AGENTS.md` 只调度 1.2.1 的唯一角色名。

## 4. 启动全新 Linux CPU 会话

```bash
codex --cd /absolute/path/to/<paper> --ask-for-approval never --sandbox workspace-write
```

不要使用 `resume`。不要预先运行 endetail。流程为全面自主执行，不会询问是否执行、
是否继续或是否进入 “turbo”。它不会运行 `nvidia-smi` 或 GPU OCR。

## 5. 发送第一条请求

把 `START_PROMPT.md` 全文作为第一条请求。预检必须返回 `NOT_DETAILED`。之后流程会扫描
所有 candidate-bearing 旧记录，复用 OCR/页图/抽取，定向重核来源，构建不限量恢复台账，
再选择最多 10 个进入人审报告。

DOCX/XLSX/CSV 若缺少可复用的旧抽取，流程会调用内置结构化提取脚本；DOC/XLS 或需要页码
定位的 Office 文件会尝试本机 LibreOffice。LibreOffice 不存在时只记录限制，不会暂停询问。

## 6. 检查成功标志

旧 `final_report.md/html` 不应改变。新输出为：

- `.ai_paper_validation/final_report_1_2_1.md`
- `.ai_paper_validation/final_report_1_2_1.html`
- `.ai_paper_validation/patch_1_2_1/recovered_candidate_ledger.md`
- `.ai_paper_validation/patch_1_2_1/patch_validation.json`

`patch_validation.json` 的 `status` 必须为 `PASS`，并且 source/legacy artifact integrity 均
未失败。

## 7. 错误版本自动停止

若预检检测到 endetail，1.2.1 会明确记录“应使用 1.2.2”并停止，不会覆盖文件或询问你
是否切换。
