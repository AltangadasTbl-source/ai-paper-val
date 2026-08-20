# Workflow 1.3.2 使用方式

1. 备份论文包根目录现有的 `AGENTS.md` 与 `.codex/` 管理配置。
2. 将 `workflow1.3.2` 的全部内容（包括 `.codex`）合并复制到论文包根目录；保留所有原始来源
   和旧 `.ai_paper_validation/` 文件。
3. 在论文包根目录启动全新 Codex 会话，不使用 `resume`。
4. 将英文 `START_PROMPT.md` 全文作为第一条请求。
5. 完成后检查：

   - `.ai_paper_validation/final_report_1_3_2.md`
   - `.ai_paper_validation/final_report_1_3_2.html`
   - `.ai_paper_validation/review_1_3_2/review_validation.json`

报告中的候选数必须由本轮源文件全覆盖审阅决定，不得固定为 10，不得从旧候选集起步。
