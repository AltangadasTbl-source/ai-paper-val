# Workflow 1.2.2 使用方式

## 1. 先判定适用性

用于已经完成 workflow 1.0，并且 `.ai_paper_validation/final_report.md` **已经**经过
`final_report_endetail_prompt.md` 二次扩写的论文包。保留原始来源、整个旧
`.ai_paper_validation/`、endetail Markdown 和 HTML。

若报告还没有 endetail 的 disposition/verified/uncertain/rejected 结构，请用 1.2.1。

## 2. 备份旧管理文件

```bash
mkdir -p /absolute/path/to/<paper>/.workflow1.0_management_backup
cp -a /absolute/path/to/<paper>/AGENTS.md /absolute/path/to/<paper>/.workflow1.0_management_backup/AGENTS.md
cp -a /absolute/path/to/<paper>/.codex /absolute/path/to/<paper>/.workflow1.0_management_backup/.codex
```

不要移动或改写 `.ai_paper_validation/`。1.2.2 会对其全部既有文件做哈希并在结束时复核。

## 3. 复制 1.2.2 内容

```bash
cp -a /absolute/path/to/workflow1.2.2/. /absolute/path/to/<paper>/
```

必须复制隐藏 `.codex`，并在复制之后才启动 Codex，使新的 `AGENTS.md` 在会话初始化时被
加载。

## 4. 启动全新 Linux CPU 会话

```bash
codex --cd /absolute/path/to/<paper> --ask-for-approval never --sandbox workspace-write
```

不要使用 `resume`。流程为全面自主执行，不会询问是否执行、是否继续或如何处理候选，
也不会探测/使用 GPU。

## 5. 发送第一条请求

把 `START_PROMPT.md` 全文作为第一条请求。预检必须返回 `ENDDETAIL_DETECTED`。流程会先
生成 `endetail_harvest.md`，复用已经完成且能与来源匹配的计算、替代解释和限制，再扫描
checker/candidate/verifier/critic 记录恢复 endetail 当时禁止新增的候选。旧 disposition
只保存在 lineage 中，不参与新队列排序。

DOCX/XLSX/CSV 若缺少旧抽取，流程使用内置结构化提取脚本；DOC/XLS 或需要页码定位时尝试
本机 LibreOffice。缺少 LibreOffice 只会形成限制记录，不会请求人工选择。

## 6. 检查成功标志

旧 endetail 报告不应改变。新输出为：

- `.ai_paper_validation/final_report_1_2_2.md`
- `.ai_paper_validation/final_report_1_2_2.html`
- `.ai_paper_validation/patch_1_2_2/endetail_harvest.md`
- `.ai_paper_validation/patch_1_2_2/recovered_candidate_ledger.md`
- `.ai_paper_validation/patch_1_2_2/patch_validation.json`

`patch_validation.json` 的 `status` 必须为 `PASS`。最终报告最多 10 个候选，恢复台账不设
数量上限。

## 7. 错误版本自动停止

若预检没有检测到 endetail，1.2.2 会明确记录“应使用 1.2.1”并停止，不会改写旧报告或
询问你是否切换。
