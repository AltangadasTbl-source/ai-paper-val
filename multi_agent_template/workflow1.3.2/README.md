# Workflow 1.3.2：从源文件开始完整重跑

适用于需要完全摆脱旧版 top-10 发现边界的论文包。即使目录中存在旧 OCR、抽取、候选和报告，
本版本也只从原始 PDF/Office/CSV 等来源建立新的证据资产，再重新做完整审阅；旧记录保留但不作为
本轮证据输入。

核心变化：

- 从 source inventory、文本/表格准备、页图/OCR 判断开始重做；
- 不设候选数上限，也不再创建最多 10 条的 review queue；
- 最终 Markdown/HTML 报告包含全部稳定候选；
- 重点收窄到数值、分母/比例/加总、统计报告、跨文档数值、统计量标签/尺度以及
  rate-versus-count 一致性；
- 语调定位为质量控制，并说明避免小错误进入 systematic review/meta-analysis 的价值；
- agent 主导科学工作，Python 仅用于可选 Office 结构抽取、HTML fallback 渲染和机械验证。

复制本目录全部内容（包括隐藏的 `.codex`）到单篇论文包根目录，在全新 Codex 会话中发送
`START_PROMPT.md` 全文。

主要新输出：

```text
.ai_paper_validation/
├── final_report_1_3_2.md
├── final_report_1_3_2.html
└── review_1_3_2/
    ├── evidence_asset_inventory.md
    ├── preprocessing/
    ├── coverage_manifest.md
    ├── candidate_ledger.md
    ├── verification/evidence_recheck.md
    ├── quality/evidence_quality_audit.md
    └── review_validation.json
```

旧来源和旧审阅产物均不覆盖。只有验证结果为 `PASS` 才算完成。
