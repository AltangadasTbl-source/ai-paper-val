# Human adjudication — XLSX workflow

当前版本为 [v.2.1.5.2](human_adjudication_v_2_1_5_2/USAGE.md)：**四份年度工作簿，每年一份，两轮均使用 新版 18 列布局**。基于 v.2.1.5.1 更新，Primary assessment 在初审阶段默认留空，复核交接后显示初审快照摘要，每篇论文一张 C_<paper> 表，自带说明、Codebook、候选和完整证据。XLSX 内全部为英文。

| 年份 | 论文 | 候选 | 年度工作簿 |
|---|---:|---:|---|
| 2018 | 10 | 119 | [2018](human_adjudication_v_2_1_5_2/human_adjudication_v_2_1_5_2_2018.xlsx) |
| 2019 | 10 | 71 | [2019](human_adjudication_v_2_1_5_2/human_adjudication_v_2_1_5_2_2019.xlsx) |
| 2024 | 10 | 91 | [2024](human_adjudication_v_2_1_5_2/human_adjudication_v_2_1_5_2_2024.xlsx) |
| 2025 | 15 | 131 | [2025](human_adjudication_v_2_1_5_2/human_adjudication_v_2_1_5_2_2025.xlsx) |

模板从初审阶段开始，复核专用列暂时锁定。初审完成后，由管理者使用 prepare-checker 生成同布局的下一阶段工作副本；文件内保存初审快照、只读摘要和复核记录，Complete 重置为复核完成标记。初审备份保留，已有文件不覆盖。详细命令见 [USAGE.md](human_adjudication_v_2_1_5_2/USAGE.md)。

四份模板合计 45 张论文表、412 条唯一候选；来源目录位于 resources 子目录。沿用 v.2.1.5.1 的 18 列布局和判断术语；本版将初审阶段的 Primary assessment 改为默认空白；两轮使用同一布局。[v.2.1.3](previous/human_adjudication_v_2_1_3/USAGE.md) 保留供参考。

需要直接测试复核时，打开 [2019 TEST Checker ready](human_adjudication_v_2_1_5_2/examples/human_adjudication_v_2_1_5_2_2019_TEST_checker_ready.xlsx)。71 条模拟初审已完成，复核栏待填；[样例说明](human_adjudication_v_2_1_5_2/examples/README.md) 包含同意、分歧和改判测试步骤。

[设计说明](human_adjudication_v_2_1_5_2/DESIGN.md)、[验证记录](human_adjudication_v_2_1_5_2/VALIDATION.md) 随版本更新。

Statistcal_or_numerical issue 替代 Statistical error。Report-internal or planning-material inconsistency 明确区分报告材料内部及计划材料之间的问题。该字段与 Protocol interpretation 均以 minor_presentation 和 non_inconsistency 吸收原 wording_only。Primary assessment 位于 M 列，Notes 位于 R 列。候选关系保持 P_R=45、P_P=50、S_C=65、S_W=252；协议和计划材料只作描述，不进入时间比较。旧版和已有编辑均保留，未导入旧版人工作答。

Do not use any v_1_0_* build as a methodological reference, codebook source, migration input, or provenance baseline. The valid historical design lineage remains v.2.0.1 → v.2.0.2 → v.2.0.3 → v.2.0.4. New builds read the frozen XLSX catalog and do not depend on the HTML review application.
