# Human adjudication v.2.1.5

本版基于 v.2.1.4，发布 **4 份年度工作簿，每年一份**。初审和复核继续使用同一套 19 列 Checker 布局，每篇论文一张 `C_<paper>` 表。工作副本在交接后同时保存初审快照和复核记录。XLSX 内全部为英文。

本次删除 `out_of_scope`，Disposition 只保留 `retain`、`exclude`、`discuss`。领域 `internal_nonstatistical` 改为 **`report_internal_inconsistency`**，指 main paper 内部、updated supplement 内部，以及两者之间的不一致；名称不再将其限定为“非统计”。上述改动同时应用于下拉选项、Codebook、默认公式、初审摘要、校验和导出。

| 年份 | 论文表 | 候选 | 年度工作簿 |
|---|---:|---:|---|
| 2018 | 10 | 119 | [2018](human_adjudication_v_2_1_5_2018.xlsx) |
| 2019 | 10 | 71 | [2019](human_adjudication_v_2_1_5_2019.xlsx) |
| 2024 | 10 | 91 | [2024](human_adjudication_v_2_1_5_2024.xlsx) |
| 2025 | 15 | 131 | [2025](human_adjudication_v_2_1_5_2025.xlsx) |

来源目录位于 `resources/source_catalog_v_2_1_5.xlsx`，基于 v.2.1.4 的冻结 XLSX，只将 130 条 AI 建议中的旧领域名统一为新名称，并记录上版来源摘要。412 条候选的编号、内容、证据及关系不变；来源目录不属于四份人工工作簿。未导入或预填人工作答，AI 候选不等于人工确认错误。

另提供 [2019 Checker 测试样例](examples/README.md)：71 条模拟初审已全部完成，复核副本已经准备好，可直接打开测试。样例独立放在 examples 子目录，不属于四份正式模板。

## 相同布局、两个阶段

每份文件自带 Start、Setup、Papers、Candidates、Evidence 和分层 Codebook。两阶段均使用 `C_<paper>`，表头、列宽、行高、颜色分组、换行和 B2 冻结位置沿用 v.2.1.4。C_ 表示共用布局；当前阶段以 Start 的 File status 为准。

| 列 | 内容 | 初审阶段 | 复核阶段 |
|---|---|---|---|
| A–C | 候选编号、标题、原文位置 | 只读 | 只读 |
| D–E | Disposition、Review domain | 初审答案 | 只填修改项，空白继承初审 |
| F | Complete | 初审是否完成 | 复核是否完成；交接时重置为 no |
| G | Validation hint | 初审提示 | 复核提示 |
| H–N | 五个领域判断、关联组、备注 | 初审答案 | 只填修改项，适用空白继承初审 |
| O–R | Checker result、Checker comment、Discussion resolution、Resolution note | 灰色锁定，保持空白 | 开放填写 |
| S | Primary assessment (read only) | 显示交接说明 | 显示同一候选的初审快照摘要 |

## 初审与交接

1. 将相应年度文件另存为工作副本，在 Setup 填初审人 ID。
2. 从 Papers 打开各论文 C_ 表，核对候选和证据，填写 disposition、domain 及适用判断。
3. 每行人工核对后设 Complete=yes。初审不填写 O–R；四列在此阶段锁定。
4. 所有初审完成后保存备份。管理者运行以下命令，生成下一阶段工作副本。该文件内保留初审和复核两轮记录，论文表布局不变。

```bash
python3 human_adjudication/human_adjudication_v_2_1_5/build_v_2_1_5.py prepare-checker annual_2019_primary_complete.xlsx --checker-id checker_name --output annual_2019_checking.xlsx
```

交接命令是必需的一次管理者操作：检查初审完成状态，将逐 key 初审答案保存到 veryHidden 的 `_Primary` 表，锁定初审身份，记录原文件 SHA256，在 S 列写入只读摘要，并将复核输入和 Complete 重置。日常审阅在 Excel 中进行，无宏、无外部工作簿链接、无需手动抄录答案。

发布物只有四份年度模板。初审备份和交接副本是同一年度流程的阶段存档，不是另外四份发布模板。命令不覆盖输入或已有输出；Checker 使用嵌入快照，后续初审改动不会自动同步，需要重新交接并核对复核结果。

## 复核

在交接后的工作副本填写不同的 checker ID，继续使用同名 C_ 论文表。完全同意只填 Checker result=agree 和 Complete=yes。适用判断留空继承初审，自动 not_applicable 不算修改；需要变更才填写新值。

非 agree 必须有 Checker comment。disagree、unable，或初审 discuss 后变为确定决定，需要共同讨论，填 Discussion resolution=resolved 和包含参与人及结论的 Resolution note。未解决候选不进入确定计数。

改变领域或 disposition 后，新启用的必填判断不能继承初审原本不适用的值。`<clear>` 可清除继承的备注、关联组、Downstream impact 和 Protocol interpretation。修改已完成行后手动设 Complete=no，重新核对再设 yes。

## 判断规则

| 保留候选的领域 | 必填判断 | 可选判断 |
|---|---|---|
| statistical_results | Statistical error、Substantiveness | Downstream impact |
| report_internal_inconsistency | Internal or plan assessment | 无 |
| plan_material | Internal or plan assessment | 无 |
| protocol_report | 无额外必填判断 | Protocol interpretation |

`report_internal_inconsistency` 对应 main paper 与 updated supplement 组成的报告材料内部的不一致：可以发生在任一文件内部，也可以发生在两者之间。若具体判断的是统计报告错误，使用 `statistical_results` 并填写 Statistical error 与 Substantiveness。`plan_material` 对应 protocol/SAP 等计划材料之间的不一致，`protocol_report` 对应计划与最终报告差异。实质性判定和分析归类沿用 v.2.1.4；Documentation 和 Justification 不恢复。P_R/P_P 只作描述，不进入时间比较。

适用判断默认空白，不适用判断由公式显示 not_applicable。下拉选择会替换默认公式；以后改领域不会自动删除已填字面值，红色和 CLEAR INACTIVE VALUES 提示清理。空白不是 indeterminate/unknown，也不是不适用。可选 restore-defaults 可在新副本恢复合格的空白或不适用默认格。

## 管理者命令

需要 Python 3.10+ 与 requirements.txt 中的依赖。从仓库根目录运行：

```bash
python3 -m pip install -r human_adjudication/human_adjudication_v_2_1_5/requirements.txt
python3 human_adjudication/human_adjudication_v_2_1_5/build_v_2_1_5.py validate annual_2019_primary_complete.xlsx --require-complete
python3 human_adjudication/human_adjudication_v_2_1_5/build_v_2_1_5.py validate annual_2019_checking.xlsx --report validation.xlsx
python3 human_adjudication/human_adjudication_v_2_1_5/build_v_2_1_5.py restore-defaults annual_2019_checking.xlsx --output annual_2019_restored.xlsx
python3 human_adjudication/human_adjudication_v_2_1_5/build_v_2_1_5.py export annual_2018_done.xlsx annual_2019_done.xlsx annual_2024_done.xlsx annual_2025_done.xlsx --output adjudicated_results.xlsx
python3 human_adjudication/human_adjudication_v_2_1_5/build_v_2_1_5.py build --output-dir /tmp/adjudication-v215-new-build
python3 -m unittest discover -s human_adjudication/human_adjudication_v_2_1_5 -p test_v_2_1_5.py -v
```

校验自动识别 primary 或 checker 阶段。初审完成状态 primary_complete 不代表最终结果；导出只接受已交接的 checker 阶段，每年一份。`--allow-incomplete` 生成明确标记的临时导出，未完成论文的完整计数保持空白。

版本/revision 为 v.2.1.5，schema 为 `xlsx-adjudication-7`。v.2.1.4 原文件保留；旧版人工作答文件不直接作为新版输入，粘贴已删除的 disposition 或旧领域代码也会校验失败。见 [设计说明](DESIGN.md)、[验证记录](VALIDATION.md)、[双语与中文文档](../../ignorance_documents/human_adjudication_v_2_1_5/README.md)。
