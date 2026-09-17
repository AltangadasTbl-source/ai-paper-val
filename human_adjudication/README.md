# Human adjudication — XLSX workflow

当前版本为 [v.2.1.5](human_adjudication_v_2_1_5/USAGE.md)：**四份年度工作簿，每年一份，两轮均使用 v.2.1.3 Checker 的 19 列布局**。基于 v.2.1.4 更新，每篇论文一张 C_<paper> 表，自带说明、Codebook、候选和完整证据。XLSX 内全部为英文。

| 年份 | 论文 | 候选 | 年度工作簿 |
|---|---:|---:|---|
| 2018 | 10 | 119 | [2018](human_adjudication_v_2_1_5/human_adjudication_v_2_1_5_2018.xlsx) |
| 2019 | 10 | 71 | [2019](human_adjudication_v_2_1_5/human_adjudication_v_2_1_5_2019.xlsx) |
| 2024 | 10 | 91 | [2024](human_adjudication_v_2_1_5/human_adjudication_v_2_1_5_2024.xlsx) |
| 2025 | 15 | 131 | [2025](human_adjudication_v_2_1_5/human_adjudication_v_2_1_5_2025.xlsx) |

模板从初审阶段开始，复核专用列暂时锁定。初审完成后，由管理者使用 prepare-checker 生成同布局的下一阶段工作副本；文件内保存初审快照、只读摘要和复核记录，Complete 重置为复核完成标记。初审备份保留，已有文件不覆盖。详细命令见 [USAGE.md](human_adjudication_v_2_1_5/USAGE.md)。

四份模板合计 45 张论文表、412 条唯一候选；来源目录位于 resources 子目录。相对于 v.2.1.3，表头、列宽、表头颜色、行高、换行和冻结位置保持 Checker 呈现；不再发布另外四份独立角色模板。[v.2.1.3](human_adjudication_v_2_1_3/USAGE.md) 保留供参考。

需要直接测试复核时，打开 [2019 TEST Checker ready](human_adjudication_v_2_1_5/examples/human_adjudication_v_2_1_5_2019_TEST_checker_ready.xlsx)。71 条模拟初审已完成，复核栏待填；[样例说明](human_adjudication_v_2_1_5/examples/README.md) 包含同意、分歧和改判测试步骤。

[设计说明](human_adjudication_v_2_1_5/DESIGN.md)、[验证记录](human_adjudication_v_2_1_5/VALIDATION.md) 和 [双语 Markdown / 中文 TeX、PDF](../ignorance_documents/human_adjudication_v_2_1_5/README.md) 随版本更新。

Disposition 现仅保留 retain、exclude、discuss，已删除 out_of_scope。internal_nonstatistical 改为 report_internal_inconsistency，明确指 main paper 内部、updated supplement 内部及两者之间的不一致。其余判断与分析规则沿用 v.2.1.4：Documentation、Justification 不恢复，协议解释与下游影响可选。候选关系保持 P_R=45、P_P=50、S_C=65、S_W=252；协议和计划材料仅作描述，不进入时间比较。AI 候选不等于人工确认错误。

Do not use any v_1_0_* build as a methodological reference, codebook source, migration input, or provenance baseline. The valid historical design lineage remains v.2.0.1 → v.2.0.2 → v.2.0.3 → v.2.0.4. New builds read the frozen XLSX catalog and do not depend on the HTML review application.
