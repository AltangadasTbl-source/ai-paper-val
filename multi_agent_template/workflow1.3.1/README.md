# Workflow 1.3.1：复用既有抽取资产，重新做完整质量控制审阅

适用于已有 OCR、native/layout text、表格或 workbook 抽取、页图、document map 的论文包。
它不会沿用旧版的 top-10 候选边界，而是把这些既有资产当作证据缓存，重新覆盖全部结果相关
内容并重新发现候选。

核心变化：

- 不设候选数上限，也不再创建最多 10 条的 review queue；
- 最终 Markdown/HTML 报告包含全部稳定候选；
- 审阅重点收窄到数值、分母/比例/加总、统计报告、跨文档数值、统计量标签/尺度以及
  rate-versus-count 一致性；
- 语调定位为发表前或发表后质量控制，不宣称“揭露严重错误”；
- 保留“细小错误可能进入 systematic review/meta-analysis”的下游证据链价值，但不夸大影响；
- agent 负责清点、覆盖规划、抽取、核查和合成；Python 只保留可选 Office 抽取、HTML
  fallback 渲染和最终机械校验。

复制本目录全部内容（包括隐藏的 `.codex`）到单篇论文包根目录，保留原始来源和已有
`.ai_paper_validation/`。在新 Codex 会话中发送 `START_PROMPT.md` 全文。

主要新输出：

```text
.ai_paper_validation/
├── final_report_1_3_1.md
├── final_report_1_3_1.html
└── review_1_3_1/
    ├── evidence_asset_inventory.md
    ├── coverage_manifest.md
    ├── candidate_ledger.md
    ├── verification/evidence_recheck.md
    ├── quality/evidence_quality_audit.md
    └── review_validation.json
```

旧报告和旧抽取均不覆盖。只有验证结果为 `PASS` 才算完成。
