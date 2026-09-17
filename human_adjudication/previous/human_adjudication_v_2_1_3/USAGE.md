# Human adjudication v.2.1.3

本版分为 **8 份年度审阅文件：4 份 Primary + 4 份 Checker**。两类文件均为每篇论文一张审阅表，并自带 Start、Setup、Papers、Candidates、Evidence 和 Codebook。XLSX 内全部使用英文。

| 年份 | 论文 | 候选 | Primary | Checker 模板 |
|---|---:|---:|---|---|
| 2018 | 10 | 119 | [2018 Primary](human_adjudication_v_2_1_3_2018_primary.xlsx) | [2018 Checker](human_adjudication_v_2_1_3_2018_checker.xlsx) |
| 2019 | 10 | 71 | [2019 Primary](human_adjudication_v_2_1_3_2019_primary.xlsx) | [2019 Checker](human_adjudication_v_2_1_3_2019_checker.xlsx) |
| 2024 | 10 | 91 | [2024 Primary](human_adjudication_v_2_1_3_2024_primary.xlsx) | [2024 Checker](human_adjudication_v_2_1_3_2024_checker.xlsx) |
| 2025 | 15 | 131 | [2025 Primary](human_adjudication_v_2_1_3_2025_primary.xlsx) | [2025 Checker](human_adjudication_v_2_1_3_2025_checker.xlsx) |

`resources/source_catalog_v_2_1_3.xlsx` 是维护程序的冻结来源，放在子目录，不属于上述 8 份人工审阅文件。

## 相同的呈现方式

Primary 使用 `P_<paper>`，Checker 使用 `C_<paper>`，例如 `P_jama.2019.2210` 和 `C_jama.2019.2210`。每年分别有 10、10、10、15 张审阅表。没有年度混排的 Checker 表，也不在 Checker 文件中另外放一套可见的 Primary 论文表。

两类论文表的前 14 列完全一致：候选编号、标题、原文位置、Disposition、Review domain、Complete、Validation hint，随后是五个领域判断、关联组和备注。对应列的宽度、表头颜色、行高、换行和冻结位置相同。Checker 在后面追加复核结果、复核意见、讨论状态、讨论说明和只读 `Primary assessment (read only)` 摘要。

Codebook 字段名与表头逐字一致。模块用深色居中条带，字段用浅色粗体父行，选项用缩进子行；边框、字号和行分组显示上下级。黄色为必填/通用输入，浅蓝色为可选输入，灰色为不适用，红色为切换领域后需要清理的旧答案。

## 初审

1. 将相应年度 Primary 另存工作副本，在 Setup 填初审人 ID。
2. 根据 Papers 清单打开论文的 `P_<paper>` 表，查看候选、位置和必要证据。
3. 人工选择 Disposition、确认 Review domain，仅填写适用必填项。
4. 审阅完毕设 Complete=yes，保存。每个论文表均完成后交接。

| 保留候选的领域 | 必填判断 | 可选判断 |
|---|---|---|
| `statistical_results` | Statistical error、Substantiveness | Downstream impact |
| `internal_nonstatistical` | Internal or plan assessment | 无 |
| `plan_material` | Internal or plan assessment | 无 |
| `protocol_report` | 无额外必填项 | Protocol interpretation |

`internal_nonstatistical` 对应递交正文/非 protocol 补充材料内部或彼此之间的非统计不一致；`plan_material` 对应 protocol、SAP 等计划材料之间的不一致。计划材料与最终报告的差异属于 `protocol_report`，不会混用 Internal or plan assessment。

Documentation 和 Justification 继续删除。协议描述和下游影响继续可选，协议差异不进入时间比较的统计结局。非保留 disposition 不要求领域判断；discuss 可以完成本轮初审，但最终仍需讨论解决。

## 将 Primary 交接给 Checker

**发布的四份 Checker 是空白布局模板，显示 AWAITING PRIMARY HANDOFF。** 初审尚未完成时没有可继承的人工答案，因此不能直接把模板当作已经准备好的复核文件。维护者在初审完成后运行一次 `prepare-checker`，生成同样布局的独立 Checker 工作副本。日常填写仍只使用 Excel；这一步是管理者的交接操作。

```bash
python human_adjudication/human_adjudication_v_2_1_3/build_v_2_1_3.py prepare-checker primary_2019_complete.xlsx --checker-id checker_name --output checker_2019_ready.xlsx
```

命令验证全部初审记录已完成，把初审答案及初审人身份作为只读快照带入新的 Checker 文件，同时记录原 Primary 文件摘要。原文件不修改，已有输出文件不覆盖。无跨工作簿外部链接，无手工逐条抄录；生成后 Checker 可独立共享和使用。

原始初审快照保存在隐藏的 `_Primary` 表；每条候选的可见只读摘要位于其 `C_<paper>` 行末，包含初审 disposition、领域和相关判断。复核人根据该摘要或原 Primary 文件核对答案，不修改快照。

如果初审文件在交接后发生实质修改，原 Checker 不会自动同步；需要重新交接并重新核对相应复核结果。不要把更新后的初审与旧的 Checker 快照混为同一次交接。

## 复核

在独立 Checker 文件的 Setup 填复核人 ID，打开论文对应的 `C_<paper>`。完全同意只需 `Checker result=agree` 和 `Complete=yes`，适用判断格保持空白，沿用同一 candidate key 的初审答案。

复核修改项才填写新值。改变领域或 disposition 后，原本不适用的初审字段不能提供新领域的答案；需要补齐新启用的必填项。可选项仍可空白。`<clear>` 可以清除继承的备注、关联组和两个可选判断。

非 agree 需要 Checker comment。disagree、unable，或初审 discuss 后变为确定决定，需要共同讨论，填写 Discussion resolution=resolved 和包含参与人及结论的 Resolution note。未解决的分歧不能进入确定结果。

## 条件默认值

适用格默认空白，不适用格的 Excel 公式显示 `not_applicable`。Checker 公式根据嵌入的初审快照和本行修改值计算适用性；自动 N/A 不是复核修改，也不算人工判断。空白、无法判断和不适用的含义见各文件 Codebook。

先确认领域再填答案。下拉选择会替换该格默认公式；以后改领域，尚未覆盖的公式更新，已填写字面值不会自动删除。红色格和 CLEAR INACTIVE VALUES 提示清理旧值；最终分析忽略不适用旧值，原始初审答案保留供追溯。清空不会恢复公式，可选 restore-defaults 可在新副本恢复空白/不适用默认格。修改已完成行后，手动设 Complete=no，重新核对再设 yes。

## 管理者验证与导出

维护环境需要 Python 3.10+ 和 requirements.txt 中的依赖。以下命令从仓库根目录运行。

```bash
python -m pip install -r human_adjudication/human_adjudication_v_2_1_3/requirements.txt
python human_adjudication/human_adjudication_v_2_1_3/build_v_2_1_3.py validate primary_2019_complete.xlsx --require-complete --report primary_validation.xlsx
python human_adjudication/human_adjudication_v_2_1_3/build_v_2_1_3.py validate checker_2019_ready.xlsx --report checker_validation.xlsx
python human_adjudication/human_adjudication_v_2_1_3/build_v_2_1_3.py restore-defaults checker_2019_ready.xlsx --output checker_2019_restored.xlsx
python human_adjudication/human_adjudication_v_2_1_3/build_v_2_1_3.py export checker_2018_done.xlsx checker_2019_done.xlsx checker_2024_done.xlsx checker_2025_done.xlsx --output adjudicated_results.xlsx
python human_adjudication/human_adjudication_v_2_1_3/build_v_2_1_3.py build --output-dir /tmp/adjudication-new-build
python -m unittest discover -s human_adjudication/human_adjudication_v_2_1_3 -p test_v_2_1_3.py -v
```

Primary 文件自动只校验初审，不需要复核字段。最终导出只接受经过交接的 Checker 文件，每年一份；Primary 和空白 Checker 模板即使使用临时导出选项也不能作为最终输入。

版本和 revision 均为 v.2.1.3，schema 为 `xlsx-adjudication-5`；不直接读取旧版混合工作簿。候选全集仍为 45 篇论文、412 条，未迁移或伪造人工作答。详见 [设计说明](DESIGN.md)、[验证记录](VALIDATION.md) 及 [双语与中文文档](../../ignorance_documents/human_adjudication_v_2_1_3/README.md)。
