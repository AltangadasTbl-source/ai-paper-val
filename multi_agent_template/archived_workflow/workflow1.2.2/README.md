# Workflow 1.2.2：给“已经运行 endetail”的 1.0 论文包打补丁

这个目录是一个可复制到单篇论文包根目录的补丁包。它不会从头重跑 1.1，也不会删除或
覆盖 1.0 的 `.ai_paper_validation/` 记录。它会复用既有 OCR、页图、抽取记录、checker
输出、`candidate_set.md`、verifier/critic 记录和已经扩写的 endetail 报告。

## 它修复什么

1.0 把三件不同的事混在了一起：候选发现、证据核验、AI 裁决。`Uncertain` 本来只表示
某个解释或统计定义还不确定，却可能在 “verified -> accepted -> final report” 的传递中被
直接隐藏。与此同时，10 个上限同时限制了证据保留和人工 review。

1.2.2 的处理方式是：

- 恢复台账不限数量，所有旧候选及其来源关系都保留；
- 最终人工 review 队列仍然最多 10 个；
- 旧 `Verified / Uncertain / Rejected / Major / Minor` 仅作历史记录；
- 最多 10 个候选全部以 `Pending Human Adjudication` 进入新报告；
- 原始 1.0 报告不覆盖，新报告名为 `final_report_1_2_2.md/html`。
- endetail 报告中已经完成的逐项计算、替代解释和 source link 会先被收割并核验，不会无故
  重做；但它的 `Verified / Uncertain / Rejected` 结论不作为新报告的裁决。

## 每篇论文的复制与启动

假设论文包是 `<paper>`，将 **本目录的内容（包括隐藏的 `.codex`）** 合并复制到论文包
根目录。必须保留论文包原有的 `.ai_paper_validation/`，不要复制成它的子目录。

建议先保存旧的项目管理文件，再复制补丁（把模板路径换成实际绝对路径）：

```bash
mkdir -p <paper>/.workflow1.0_management_backup
cp -a <paper>/AGENTS.md <paper>/.workflow1.0_management_backup/AGENTS.md
cp -a <paper>/.codex <paper>/.workflow1.0_management_backup/.codex
cp -a /absolute/path/to/workflow1.2.2/. <paper>/
```

这只会替换工作流管理文件；`.ai_paper_validation/` 和原始论文文件不会被复制命令触碰。
旧 `.codex/agents/` 中未同名的 1.0 agent 可能仍保留，但 1.2.2 的 `AGENTS.md` 只会调用本
补丁的唯一角色名。

复制后应当看到：

```text
<paper>/
├── AGENTS.md
├── START_PROMPT.md
├── .codex/
├── legacy_patch/
├── .ai_paper_validation/       # 原有 1.0 记录，原样保留
└── 原始 PDF / 补充材料
```

在该论文包单独启动一个全新 Codex 会话，不要使用 `resume`：

```bash
codex --cd <paper> --ask-for-approval never --sandbox workspace-write
```

然后把 `START_PROMPT.md` 的内容作为第一条请求发送。该提示已经明确授权立即使用最快的
安全并行执行；这里的 “turbo” 是“不向用户询问是否执行或如何选择”的全面自主模式，
不是某个模型名称。补丁会自行采用安全默认值。

目标 Linux 环境按 **CPU-only** 处理：不会运行 `nvidia-smi` 或尝试 CUDA。流程首先复用
旧 OCR；只有某个候选的指定页面确实无法核验时，才尝试单页 CPU OCR。没有可用 CPU OCR
后端时会把限制写入报告并继续其他工作，不会暂停询问。

## 何时不要用 1.2.2

如果旧 `.ai_paper_validation/final_report.md` **没有**由
`final_report_endetail_prompt.md` 二次改写，请改用 workflow 1.2.1。预检脚本会自动识别并
停止错误版本，不能强行绕过。

## 主要输出

```text
.ai_paper_validation/
├── final_report.md                 # 旧文件，不修改
├── final_report.html               # 旧文件（如有），不修改
├── final_report_1_2_2.md             # 新的人审报告，最多 10 个候选
├── final_report_1_2_2.html
└── patch_1_2_2/
    ├── legacy_inventory.json
    ├── endetail_harvest.md
    ├── legacy_source_coverage.md
    ├── lineage_map.md
    ├── recovered_candidate_ledger.md   # 不限数量
    ├── review_queue.md                 # 最多 10 个
    ├── evidence_recheck.md
    ├── statistical_reconciliation.md
    ├── quality_audit.md
    ├── recovery_log.md
    └── patch_validation.json
```

只有 `patch_validation.json` 为 `PASS` 才算完成。补丁不会替你作最终的有效性或严重性
判断；这些字段留给人工 review。
