# Human adjudication v.2.1.2 使用说明

版本统一为 **v.2.1.2**。人工填写、交接和结果导出均使用 XLSX；工作簿内全部使用英文，包括 Codebook、批注、提示、隐藏内容和属性。外部 Markdown、TeX 和 PDF 可以使用中文。历史版本统一称为 v.2.1.1，不增加第四段版本号。

## 打开工作簿

| 年份 | 论文 / 初审表 | 候选 | 工作簿 |
|---|---:|---:|---|
| 2018 | 10 | 119 | [2018 XLSX](human_adjudication_v_2_1_2_2018.xlsx) |
| 2019 | 10 | 71 | [2019 XLSX](human_adjudication_v_2_1_2_2019.xlsx) |
| 2024 | 10 | 91 | [2024 XLSX](human_adjudication_v_2_1_2_2024.xlsx) |
| 2025 | 15 | 131 | [2025 XLSX](human_adjudication_v_2_1_2_2025.xlsx) |

先另存工作副本，在 `Setup` 填初审人 ID，在 `Papers` 找到论文对应的 `P_<paper>` 表。每条 candidate 占一行；原始内容和证据在 `Candidates`、`Evidence`，原文按编号查看共享论文文件夹。

## 最少需要填什么

每条候选都需要人工选择 `Disposition`、确认 `Review domain`，完成审阅后设 `Complete=yes`。Disposition 初始为空，领域提供可修改的 AI 建议。AI 候选和自动默认值均不计为人工判断。

| 保留候选的 Review domain | 必填判断 | 可选补充 |
|---|---|---|
| `statistical_results` | `Statistical error`、`Substantiveness` | `Downstream impact` |
| `internal_nonstatistical` | `Internal or plan assessment` | 无 |
| `plan_material` | `Internal or plan assessment` | 无 |
| `protocol_report` | 无额外必填判断 | `Protocol interpretation` |

`exclude`、`out_of_scope`、`discuss` 都不需要填写领域模块。`discuss` 是审阅后决定待讨论，可以完成本轮初审，但不能进入已解决的结果。

**Documentation 和 Justification 已删除**：初审表、Checker、Codebook 和结果导出均不再收集这两项。协议候选只需决定是否保留；可选 `Protocol interpretation` 仅描述现有比较证据中的实质性差异、措辞差异、版本时间不清、无实际差异或无法判断，不要求查找变更记录或理由。协议差异作描述性记录，不进入时间比较的统计结局。

## 条件默认值与颜色

- 黄色：必填或通用输入。是否必填以 Codebook 的条件说明为准。
- 浅蓝色：可选输入，如 `Downstream impact`、`Protocol interpretation`、备注和关联组。
- 灰色：当前领域或 disposition 下不适用；未被覆盖的默认公式显示 `not_applicable`。
- 红色：已填过的答案在切换领域后变得不适用，需要清理。

默认公式根据本行 `Review domain` 和 `Disposition` 计算：适用时显示空白，不适用时显示 `not_applicable`。Disposition 尚未选择时，按建议领域显示适用空白，仍不代表已审阅。`not_applicable` 与 `indeterminate` / `unknown` 不同：前者不需要判断，后者表示适用但无法判断。可选格空白表示未评估，不能解释为无影响。

**先确定领域，再填写判断。** 无宏 Excel 中，在下拉框选答案会覆盖该格公式。后来改领域，未覆盖的公式继续更新，已填写的字面答案不会自动删除。红色提示和 `CLEAR INACTIVE VALUES` 会指出这些旧答案；清空或选 `not_applicable`，再检查新领域的必填项。程序保留原始作答用于追溯，但最终分析字段将不适用项规范为 `not_applicable`，不使用旧答案。

删除内容不会自动恢复公式。需要重新获得动态默认值时，可以用下面的可选 `restore-defaults` 命令生成新副本；它只恢复空白或不适用的 N/A 格，不替换已有有效判断，也不覆盖输入文件。`Complete` 不会自动复位；修改已完成记录后应手动设为 `no`，重新核对后设为 `yes`。

## Codebook 的对应关系

`Field name` 与初审和 Checker 的可见列名逐字一致，保留相同大小写、空格及 `(optional)` 后缀。`Internal key` 单独说明程序字段名，不再用它替代可见表头。只读上下文字段、完成标记、验证提示和复核字段也都有解释。

深色居中条带表示模块；浅色粗体父行表示字段；缩进子行列出下拉选项。边框、字号、颜色和行分组共同显示上下级。长篇解释左对齐并自动换行，字段、代码和适用条件居中。`Requirement / scope` 说明必填/可选及适用领域，`Explanation and example` 说明用途、例子和判断边界。下拉范围只包含选项，不包含模块标题或说明行。

## 第二人复核

初审后保存带日期的备份，交给不同的复核人。复核人在 `Setup` 填 ID，在年度 `Checker` 作答，保留初审表。完全同意时只填 `Checker result=agree` 和 `Complete=yes`。

Checker 的适用空白格沿用同一 candidate key 的初审值；自动显示的 `not_applicable` 仅表示不适用，不是复核修改。复核人改领域或 disposition，使原先不适用的字段变为适用时，不会继承旧的 N/A 或旧领域残留答案；需要补齐新领域必填判断。可选描述仍可空白。

非 `agree` 需要 `Checker comment`。修改项才填写新值；`<clear>` 可清除继承的备注、关联组或两个可选判断。`disagree`、`unable`，或初审 `discuss` 后改为确定决定，需要共同讨论，并填写 `Discussion resolution=resolved` 和包含参与人及结论的 `Resolution note`。

## 可选维护命令

日常审阅只需要 Excel。维护者使用 Python 3.10+ 和本目录的 requirements.txt；以下命令从仓库根目录运行，`python` 指安装依赖后的环境。

```bash
python -m pip install -r human_adjudication/human_adjudication_v_2_1_2/requirements.txt
python human_adjudication/human_adjudication_v_2_1_2/build_v_2_1_2.py validate reviewed.xlsx --primary-only --require-complete --report primary_validation.xlsx
python human_adjudication/human_adjudication_v_2_1_2/build_v_2_1_2.py validate reviewed.xlsx --report validation.xlsx
python human_adjudication/human_adjudication_v_2_1_2/build_v_2_1_2.py restore-defaults reviewed.xlsx --output reviewed_defaults_restored.xlsx
python human_adjudication/human_adjudication_v_2_1_2/build_v_2_1_2.py prepare-checker primary_complete.xlsx --checker-id checker_name --output checker_workbook.xlsx
python human_adjudication/human_adjudication_v_2_1_2/build_v_2_1_2.py export checked_2018.xlsx checked_2019.xlsx checked_2024.xlsx checked_2025.xlsx --output adjudicated_results.xlsx
python human_adjudication/human_adjudication_v_2_1_2/build_v_2_1_2.py build --output-dir /tmp/adjudication-new-build
python -m unittest discover -s human_adjudication/human_adjudication_v_2_1_2 -p test_v_2_1_2.py -v
```

新工作簿 schema 为 `xlsx-adjudication-4`，`version` 和 `revision` 均为 `v.2.1.2`；源目录 schema 保持 1。旧版审阅工作簿不直接作为新版输入。新模板只继承冻结的 412 条候选，没有导入旧作答或生成模拟人工进度。

公式采用 Excel 的 `IF`、`AND`、`OR`、`INDEX`、`MATCH` 和命名范围，不需要宏。程序只识别原样生成的默认公式，并从实际保存的领域/选择重新确定默认值，不信任公式缓存，不执行任意输入公式。工作簿仍无超链接或外部数据连接。验证范围见 [VALIDATION.md](VALIDATION.md)，设计理由见 [DESIGN.md](DESIGN.md)。
