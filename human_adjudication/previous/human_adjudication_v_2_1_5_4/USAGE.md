# Human adjudication v.2.1.5.4

本版修复 v.2.1.5.3 的 Excel 打开／内容恢复错误。只修正文件内部格式元素顺序及版本号；候选、证据、已有答案、公式、下拉菜单和 Excel-only 交接流程不变。所有年度文件及 TEST 样例已在桌面 Excel 打开验证。

**审阅、交接、复核、检查、交付，全程只用 Excel。无需 Python、终端、宏或依赖安装。所有工作表、单元格和工作簿结构均不加锁。**

[中文分步操作指南（PDF）](human_adjudication_v_2_1_5_4_step_by_step_CN.pdf) 在本版本目录：第 2–5 页初审，第 6–7 页交接，第 8–9 页复核与讨论，第 10 页交付，第 11 页解释旧版锁图标及新版恢复方法。

| 年份 | 论文 | 候选 | 模板 |
|---|---:|---:|---|
| 2018 | 10 | 119 | [2018](human_adjudication_v_2_1_5_4_2018.xlsx) |
| 2019 | 10 | 71 | [2019](human_adjudication_v_2_1_5_4_2019.xlsx) |
| 2024 | 10 | 91 | [2024](human_adjudication_v_2_1_5_4_2024.xlsx) |
| 2025 | 15 | 131 | [2025](human_adjudication_v_2_1_5_4_2025.xlsx) |

412 条候选、来源文本、证据、AI 建议及关系保持不变；未导入人工作答。AI 候选不等于人工确认的问题。工作簿保持英文，使用相同的 18 列 C_ 论文表。

## 初审

1. 将年度模板另存为工作副本。
2. Setup B2 填 primaryReviewerId，B6 保持 primary；checker ID/name 暂时留空。
3. 从 Papers 找到 C_ 论文表。按 Candidate key 对照 Candidates、Evidence 和共享原文。
4. 填 D（Disposition）、确认 E（Review domain），填写适用的 H–L 判断。R 可写英文备注。N–Q 保持空白。M（Primary assessment）显示空白。
5. 每行人工核对后，F（Complete）选 **primary_done**。G 应显示 PRIMARY READY。
6. Checks B7 显示 PRIMARY READY 后保存初审备份。初审 discuss 可以交接，但最终交付前必须解决。

## 交接：备份 + 可编辑复核副本

1. 保留已保存、已关闭的初审备份，例如 2019_primary_complete.xlsx。
2. 打开它，立即另存为 2019_checking.xlsx。后续只改复核副本。
3. **Setup B6 仍为 primary 时**，打开 Primary_snapshot。在名称框选择整个快照：2018 A1:L120；2019 A1:L72；2024 A1:L92；2025 A1:L132。
4. 复制选区，再在**同一选区**使用 Home → Paste → Paste Special → **Values**（选择性粘贴 → 值）。这把实时公式变成固定初审记录。保存。
5. 然后将 Setup B6 改为 checker，在 B4 填另一人的 checkerId。
6. 确认 M 显示初审摘要，G 没有 FREEZE SNAPSHOT 或 CHECK KEY / SNAPSHOT。D/E/H–L/R 保留现有答案，供复核人直接修改。

必须先粘贴值，再切换阶段。尚未复核而顺序错误时，从初审备份重新建立复核副本。若已有复核修改，先另存当前文件保留工作，再从初审备份恢复正确快照；不要把复核后的答案作为初审快照。

## 复核

- 完全同意：保留现有答案，N=agree，F=**checker_done**。
- 补充说明：N=agree_clarification，O 写说明，直接修改需要调整的答案。
- N=disagree / unable 或初审 D=discuss：共同讨论；P=resolved；Q 写参与人和共同结论；更新最终答案，D 不得仍为 discuss。
- 所有非 agree 结果需要 O；所有 resolved 需要 Q。
- 空白不再继承初审。清除可选答案就直接删掉该格；不要使用旧版的清除控制词。
- 修改已完成行后先把 F 设为 **no**，重新核对再设 checker_done。完成标记不会自动重置。

primary_done 不算复核完成。每行 G=FINAL READY，且 Checks B7=FINAL READY 后，才作为最终工作簿交付。

## 判断规则

| D=retain 的领域 | 必填 | 可选 |
|---|---|---|
| statistical_results | H：Statistcal_or_numerical issue；I：Substantiveness | J：Downstream impact |
| report_internal_inconsistency | K：Report-internal or planning-material inconsistency | 无 |
| plan_material | K：Report-internal or planning-material inconsistency | 无 |
| protocol_report | 无额外必填判断 | L：Protocol interpretation |

report_internal_inconsistency 指 main paper 与 updated supplement 组成的报告材料内部不一致。具体判断统计／数值报告问题时用 statistical_results。plan_material 指计划材料之间；protocol_report 指计划与最终报告的差异，不要求额外寻找变更说明或理由。P_R/P_P 保留描述性结果，不进入时间比较。

未触碰的领域格按适用性显示空白或 not_applicable；选择下拉值会替换该格公式。以后改变领域时旧答案不会自动删除。G=CLEAR INACTIVE VALUES 时，清空不适用答案或选 not_applicable；新启用的必填项重新作答。不需要恢复默认值命令。

## 检查与交付

Checks 汇总进度；Decisions 的 status 可筛选待处理项。检查包含身份、必填项、非法粘贴值、不适用的旧答案、初审快照、同意却改答、讨论及完成阶段。它不代替证据判断，也不能防止手动破坏公式或来源数据。

最终文件自带 Decisions（初审、最终答案、复核记录及分类）、Paper_counts（整篇论文完成后才显示最终计数）、Protocol_plan_table（协议／计划材料的描述性结果）。未完成不是零。

直接另存 年份_final.xlsx，与初审备份一起交付，无需运行导出程序。管理者需要合并四年时，在新汇总工作簿按相同列顺序合并结果表，用“选择性粘贴 → 值”；表头只保留一次，每年只用一个权威 final 文件，不混入 TEST 样例。四年应有 412 条候选、45 篇论文。

## 编辑与恢复

全部单元格可编辑，**没有密码或解锁步骤**。日常只改 Setup 和 C_ 输入列；保留编号、来源、G/M 与结果表公式。误改先撤销，必要时从自己的备份恢复。旧版锁图标源于曾启用的 Excel 保护；下载警告、文件只读权限或多人占用是不同情况。

版本仍为 v.2.1.5.4；schema 为 xlsx-adjudication-excel-9。本次改变了交接方式和 Complete 选项，旧脚本流程不与本版混用。旧版本目录保留。[测试样例](examples/README.md)、[设计说明](DESIGN.md)、[验证记录](VALIDATION.md) 随版本更新。maintenance 中的 JavaScript 仅用于开发维护，不属于审阅流程。
