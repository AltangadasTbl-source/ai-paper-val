# Human adjudication v.2.2.1 — Markdown 使用指南

每篇论文一个 `.md` 文件，按目录年份分组：2018、2019、2024、2025。基于 v.2.1.5.3，共 45 篇论文、412 条候选。审阅、交接、复核和交付均使用 Markdown；判断表和 Codebook 保持英文。

[论文索引](README.md) · [Codebook](CODEBOOK.md) · [设计与来源](DESIGN.md) · [迁移检查](VALIDATION.md)

## 开始

1. 从论文索引打开相应年份下的论文文件。编辑 Markdown 源码中的空白表格单元格；保存为 UTF-8 `.md`。
2. 在 Review setup 填 Primary reviewer ID 和姓名；Stage 保持 `primary`，Paper status 改为 `in_progress`。Checker ID/name 留空。
3. 从 Candidate index 跳到候选。查看 statement、rationale、完整 evidence 和 source links，再核对原文。AI 建议仅供参考，不代表人工结论。
4. 在 Human assessment 的 Primary 列填写初审，Checker / final 列及 Checker record 暂不填写。初始 Complete=`no` 是未完成标记，不是判断。

Markdown 不提供下拉菜单、公式或自动校验。请使用 [Codebook](CODEBOOK.md) 中的原样代码。空白表示未填写；`indeterminate` / `unknown` 表示明确的不确定判断；`not_applicable` 只用于不适用项。没有“空白自动继承初审”的规则。

## 初审

每条候选必填 Disposition 和 Review domain。领域默认留空，请参照 AI suggested domain 后自行确认；这不改变 frozen relationship。

| Disposition=retain 的领域 | 必填判断 | 可选判断 |
| --- | --- | --- |
| statistical_results | Statistcal_or_numerical issue；Substantiveness | Downstream impact |
| report_internal_inconsistency | Report-internal or planning-material inconsistency | 无 |
| plan_material | Report-internal or planning-material inconsistency | 无 |
| protocol_report | 无额外必填判断 | Protocol interpretation |

对于 `exclude` 或 `discuss`，五个领域判断均不适用，留空或填 `not_applicable`。适用的必填判断不能填 `not_applicable`；适用的可选判断可留空。Notes 为可选英文备注。

初审前检查：身份已填写、候选 key 未改动、必填字段齐全、代码合法、不适用项已清空。逐条核对后把 Primary 的 Complete 改为 `primary_done`。初审 `discuss` 可以交接，但最终必须解决。

全篇初审完成后，Paper status=`primary_ready`，填写 Primary completed on。此时不要填写 Final outcome 或任何 Final candidate count。

## Handoff

1. 保存一份完整初审备份，或保存可恢复的版本历史。备份放在活动审阅目录之外，保留相同年份结构；活动目录仍然每篇一份权威文件。
2. 在 Primary backup or revision reference 记录备份位置或修订号。后续保留 Primary 的八项答案及 `primary_done`，不再改写。
3. 对每条候选，将 Primary 的八项答案逐项复制到 Checker / final。不要复制完成标记；Checker / final 的 Complete 仍为 `no`。
4. Stage 改为 `checker`，填另一位审阅人的 Checker ID/name，Paper status 改为 `in_progress`。两人的 ID 去除首尾空格后必须不同，大小写差异不算不同 ID。

此后只编辑 Checker / final 和 Checker record。若初审存在错误，也保留初审原貌，在最终列中改正并解释。若复核已开始而交接有误，先备份当前文件，再从真实初审备份恢复 Primary；不要把复核答案冒充初审记录。

## 复核与讨论

| Checker result | 操作 |
| --- | --- |
| agree | 八项最终有效答案与 Primary 一致，包括 Notes；可不填 Checker comment |
| agree_clarification | 在最终列更新必要说明或判断，Checker comment 解释原因 |
| disagree | 填 Checker comment，提出改判；共同讨论后填写 resolved 和 Resolution note |
| unable | 填 Checker comment 说明不确定处；共同讨论后填写 resolved 和 Resolution note |

只要初审 Disposition=`discuss`，即使 Checker result 不是 disagree/unable，也必须共同讨论并标记 `resolved`。所有 resolved 必须有 Resolution note，记载参与人和共同结论。讨论后更新最终答案；最终 Disposition 不得仍为 `discuss`。讨论未完成时可填 `pending`，不能交付。

比较 agree 时：五个领域判断中的不适用字段，无论空白还是 `not_applicable`，都按 `not_applicable` 比较；适用的可选空白仍为空白。其余答案必须相同。清空最终列不会继承初审答案。

每条复核完成后，将 Checker / final 的 Complete 改为 `checker_done`。`primary_done` 不能代表复核完成。任何已完成答案发生修改时，先将相应 Complete 改为 `no`，清空过时的 Final outcome 和论文最终计数，将 Paper status 设为 `in_progress`，重新核对后再完成。

## 最终检查与交付

每条候选必须同时满足以下条件，才能填 Final outcome：

- 初审完整且 Primary Complete=`primary_done`，备份或版本历史可追溯。
- Checker 是另一人；最终判断符合必填、合法代码及适用性规则。
- Checker result 已填写；非 agree 有 Checker comment；agree 与初审有效答案一致。
- 所需讨论已 resolved 且有参与人和结论；最终 disposition 不为 discuss。
- Checker / final Complete=`checker_done`。

按 [Codebook 的最终分类顺序](CODEBOOK.md#relationships-and-final-outcomes) 填一个 Final outcome。P_R/P_P 始终为描述性分类，不进入时间比较。候选未完成时，该字段保持空白。

全篇所有候选完成后，手动统计 Paper results 的五类 outcome，填写 total_final，并核对五类之和 = total_final = 该论文候选数。未完成时保留空白；完成后没有发现才填 0。这是候选计数，不是额外合并去重后的独立问题数。

勾选文件末尾 Completion checklist，填 Checker completed on，Paper status=`final_ready`。检查框和状态不会自动更新，不能替代逐项核对。

交付时保留年份目录结构以及 README、USAGE、CODEBOOK、DESIGN、VALIDATION 五份共享 Markdown 文件。每篇保留一份最终权威 `.md`；初审备份另存归档，提供访问位置。原始论文 PDF 等继续通过仓库相对链接访问；单独转发 `.md` 时仍需保留原文访问条件。

| 年份 | 论文文件 | 候选 |
| --- | --- | --- |
| 2018 | 10 | 119 |
| 2019 | 10 | 71 |
| 2024 | 10 | 91 |
| 2025 | 15 | 131 |
| 总计 | 45 | 412 |

协议／计划材料的描述结果保留在各候选正文中：statement、关系、最终 disposition、interpretation、inconsistency、notes 和讨论记录。无需另建第二份可编辑结果表。

## Markdown 编辑提示

- 在表格中输入字面竖线时写成 `\|`，避免破坏列结构。
- 长备注可写在对应候选 Human assessment 下的独立段落中，使用 `Primary notes:`、`Checker / final notes:`、`Checker comment:` 或 `Resolution note:` 标签，并在表格中指向该段落。交接时复制完整备注，agree 比较时也包含完整备注。
- 保留 Candidate key、证据文字、关系和 Source metadata。按 key 识别候选，不依赖显示顺序。
- 2019 的 jama.2019.14901 有六条候选未附 catalog evidence 摘录。其文件已逐条标明，请使用 Source links 查阅原文。
- 本版没有锁或密码。人工检查只确认流程与记录完整，不自动验证科学判断；可见初审答案的复核不属于盲法一致性测量。
