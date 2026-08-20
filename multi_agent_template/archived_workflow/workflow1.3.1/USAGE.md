# Workflow 1.3.1 使用方式

1. 确认论文包中存在可复用的 OCR、文本或表格抽取资产；若不存在，使用 workflow 1.3.2。
2. 备份论文包根目录现有的 `AGENTS.md` 与 `.codex/` 管理配置。
3. 将 `workflow1.3.1` 的全部内容（包括 `.codex`）合并复制到论文包根目录，不移动或覆盖
   `.ai_paper_validation/` 中已有科学记录。
4. 在论文包根目录启动全新 Codex 会话，不使用 `resume`。
5. 将英文 `START_PROMPT.md` 全文作为第一条请求。
6. 完成后检查：

   - `.ai_paper_validation/final_report_1_3_1.md`
   - `.ai_paper_validation/final_report_1_3_1.html`
   - `.ai_paper_validation/review_1_3_1/review_validation.json`

报告中的候选数应当由实际证据决定，不应固定为 10，也不应存在 `DEFERRED_BY_REVIEW_CAP`。
