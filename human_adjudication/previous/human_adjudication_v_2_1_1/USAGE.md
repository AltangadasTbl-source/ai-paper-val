# v.2.1.1：精简 XLSX 人工审阅流程

当前修订：**v.2.1.1**。四个年度文件名仍为 v.2.1.1；原年度 `Primary` 已拆成每篇论文一张 `P_<paper>` 工作表，XLSX 的可见与隐藏内容全部使用英文。中文仅用于本 Markdown 和外部说明文档。

目前尚未开始人工 adjudication；本版提供待使用的工作表，不包含任何真实人工判断。旧 HTML 方案已舍弃，v.2.1.* 开始全部使用 XLSX。审阅者只需 Excel；Python 是管理者可选的校验和汇总工具。

## 打开哪份文件

| 文件 | 论文数 | 候选数 |
|---|---:|---:|
| `human_adjudication_v_2_1_1_2018.xlsx` | 10 | 119 |
| `human_adjudication_v_2_1_1_2019.xlsx` | 10 | 71 |
| `human_adjudication_v_2_1_1_2024.xlsx` | 10 | 91 |
| `human_adjudication_v_2_1_1_2025.xlsx` | 15 | 131 |

同一个年度 XLSX 同时有初审和复核表，不需要切换软件或导入 JSON。建议从年度模板另存一份带姓名或日期的工作副本，避免混淆模板和正在填写的文件。

| 工作表 | 用途 |
|---|---|
| `Start` | 内置简要说明 |
| `Setup` | 初审人 ID、复核人 ID；姓名可选 |
| `Papers` | 论文、对应初审表名称、候选数的清单，无跳转链接 |
| `P_<paper>` | 每篇论文各自的初审表，一条候选一行，黄色格可填写；共 45 张 |
| `Checker` | 第二人复核；保留初审，在这里写复核意见和修改值 |
| `Candidates` | 候选描述、论文编号、原文位置、原始关系码和 AI 预填值 |
| `Evidence` | 完整候选证据、比较对象、计算、替代解释；按 key 筛选 |
| `Codebook` | 下拉选项的英文代码与英文释义 |

隐藏工作表及隐藏元数据列只用于来源核对。工作簿**没有超链接、文档页码跳转、宏、浏览器存储或外部数据连接**。原文按论文编号和位置直接查共享的 `2018/2019/2024/2025` 文件夹；XLSX 可单独共享，不需要保持文件夹相对位置。

## 初审：只填写适用字段

1. 在 `Setup` 填稳定的 `primaryReviewerId`。所有记录初始都是未完成，**disposition 留空，不默认 retain 或任何其他判断**。领域仍提供可修改的 AI 建议；历史 AI disposition 只在 `Candidates` 中作为参考。
2. 在 `Papers` 找到论文对应的工作表名，例如 `P_jama.2017.21906`，通过底部标签打开该论文初审表，阅读候选标题与原文位置；需要更完整上下文时查看 `Candidates` 和 `Evidence`，或查共享原文。
3. 用下拉框选择 `Disposition` 和 `Review domain`。每条候选都可选全部四个领域，原始关系码不会随领域选择改写。
4. 只有保留 (`retain`) 时，填写相应模块。灰色模块不适用；如果改过领域，可清除不再适用的旧值。
5. 关联组和备注可留空。确认本行已审阅后把 `Complete` 从 `no` 改为 `yes`，用 Ctrl+S 保存。

| 保留时的领域 | 必填判断 |
|---|---|
| `statistical_results` | 统计错误状态、实质性、潜在下游影响 |
| `internal_nonstatistical` | 内部不一致判断 |
| `protocol_report` | 变更记录、变更理由、方案差异解释 |
| `plan_material` | 内部或计划材料判断 |

`exclude`（不保留）、`out_of_scope`（范围外）、`discuss`（待讨论）只需有效的 disposition 和 domain，不要求填领域模块。`discuss` 可以表示“本轮初审已做完，但结论待讨论”；不能进入已解决的最终计数。

空白 disposition 表示尚未选择；`discuss` 表示审阅后主动决定需要讨论，两者不同。未选择 disposition 不能标记初审完成。`Codebook` 的 meaning 现在逐项说明适用情形及重要边界，例如保留候选不自动等于确认错误、未找到变更记录不等于证明不存在记录。

不重新收集复现日志、重复候选判定、通用后果、逐项查证记录或必填初审理由。统计模块的下游影响仍保留。关联组仅连接相关但不同的候选，不自动去重或合并计数。

## 复核：同意时只填两个选项

初审结束后，另存带日期的初审备份，把工作副本交给第二人。第二人在 `Setup` 填不同的 `checkerId`，读取对应论文的 `P_<paper>` 初审表，在年度 `Checker` 填写；不要修改任何论文的初审表。复核按 candidate key 对应初审，不依赖工作表顺序或行号。

- 完全同意：选择 `agree`，把 `Complete` 设为 `yes`。其余判断格留空，表示沿用初审。
- 同意但需澄清：选择 `agree_clarification`，填写复核意见；只有需要修改的判断格才填值。
- 不同意：选择 `disagree`，说明原因，在后面的判断格填写拟修改值。
- 无法解决：选择 `unable`，说明待讨论内容。

复核页的 disposition、domain 和各模块是**修改项**，空白代表沿用同一 candidate key 的初审值，不代表删掉初审判断。改判时也必须满足对应领域的必填条件。若要清空继承的备注或关联组，填 `<clear>`；此标记只适用于这两个自由文本字段。

任何非 `agree` 结果都要填写 `Checker comment`。选择 `agree` 时不能同时修改判断，否则应使用澄清或不同意。

`disagree` / `unable` 默认保留 `Discussion resolution=pending`。共同讨论解决后填 `resolved`，并在 `Resolution note` 简述参与人及结论，再确认 `Complete=yes`。初审 `discuss` 后改成确定结论，也需要记录讨论解决。未解决的分歧不计入最终结果；“复核完成”和“分歧解决”是两回事。

同一候选完成复核后，若必须修改初审，应保留旧副本，并重新核对相应复核行。普通无宏 XLSX 不会自动锁定已完成人工记录、记录逐格修改时间或把完成标记自动改回 `no`。

## Excel 操作约定

下拉菜单限定代码，`Codebook` 解释含义。初审和复核表都只冻结 **A 列候选编号及标题行**（`B2`），B 列之后可自由横向滚动。初审已删除 `Paper` 列：A/B/C/D 依次为候选编号、标题、原文位置、disposition，列宽为 22/28/22/18。年度 `Checker` 保留便于筛选的 `Paper` 列，A/B/C/D 宽度为 22/20/28/18。其余判断列也采用紧凑宽度。长文本自动换行，完整标题或位置可选中单元格后在编辑栏查看。工作表保护防止误改编号和证据；黄色格仍可输入。保护没有密码，不是防篡改或审计签名。

XLSX 中不允许出现中文，包括姓名、备注、批注、选项提示、隐藏数据和文件属性。请用英文或姓名拼音填写。生成器也将默认主题中的本地化字体名改为英文名称；保存输出前和读取校验时检查整个 XLSX 文件包。科学符号（如 β、≤）仍可正常保留。这是内容检查，不是语言翻译；若人工输入中文，校验会报错，程序不会擅自删除或翻译答案。Excel 自身的语言和菜单由本机设置决定。

可直接使用筛选来定位论文、未完成记录和待讨论项。Excel 对受保护区域的排序有限制；通常使用筛选即可。如确需排序，可取消工作表保护后对**整个数据区域**排序，不要仅排序某个回答列。程序按 candidate key 对应初审和复核，仍会检查重复、缺失和错配。

保存即续接。交接用 XLSX 工作副本及初审备份即可，不需要运行脚本。多人协作建议按初审、复核顺序交接，避免同时修改同一年度工作副本。

填写提示公式只是辅助：初审提示检查领域必填项；复核提示检查复核选项和意见。它不是完整逻辑校验，尤其不会自动认证初审保留值、判定分歧已解决或检测所有粘贴错误。Excel 下拉也可能被粘贴绕过。正式汇总前可使用下面的可选工具核对实际保存值。

## 可选：管理者校验、冻结备份与汇总

以下命令在仓库根目录运行。**这些命令不属于审阅者必需的日常操作。** Python 3.10+；建议创建独立环境后安装本目录的 `requirements.txt`（openpyxl 3.1.5）。

```bash
python3 -m venv /tmp/adjudication-venv
/tmp/adjudication-venv/bin/python -m pip install -r human_adjudication/human_adjudication_v_2_1_1/requirements.txt
```

下文的 `python` 指安装好依赖的解释器，`reviewed.xlsx` 等是实际工作副本路径的占位符。输出会保存输入文件名用于溯源，因此工作副本请采用英文文件名。

```bash
# 初审交接前：只检查初审全部完成，复核尚未开始不算错误。
python human_adjudication/human_adjudication_v_2_1_1/build_v_2_1_1.py validate reviewed.xlsx --primary-only --require-complete --report primary_validation.xlsx

# 检查当前进度；未完成作为 PENDING 报告，非法答案仍报错。
python human_adjudication/human_adjudication_v_2_1_1/build_v_2_1_1.py validate reviewed.xlsx --report current_validation.xlsx

# 可选强化备份：锁定全部论文初审表，并保存初审摘要校验。
python human_adjudication/human_adjudication_v_2_1_1/build_v_2_1_1.py prepare-checker primary_complete.xlsx --checker-id checker_name --output checker_workbook.xlsx

# 汇总一个或多个已解决的年度工作簿；每年只能指定一份权威工作副本。
python human_adjudication/human_adjudication_v_2_1_1/build_v_2_1_1.py export checked_2018.xlsx checked_2019.xlsx checked_2024.xlsx checked_2025.xlsx --output adjudicated_results.xlsx
```

完整导出要求所有输入候选已完成两轮且已解决。若仅想看阶段性进度，加 `--allow-incomplete`；输出会明确标注临时结果，未完成论文的最终计数留空，不把未知当作零。

输出 `Decisions` 分开保留初审、复核后的有效值、复核意见和讨论结果；`Paper_counts` 包括输入年份的所有 45 篇中的相应论文，也保留符合条件结果为零的论文；`Protocol_plan_table` 提供协议与计划材料的描述性明细。对未解决记录，`Decisions` 中拟定值仍可查，但 `status` 为 `unresolved`，`outcome` 为 `undetermined`，不能作为已确认结论。每份输出均记录输入摘要。

程序拒绝覆盖任何已有输出；需要重做时指定新文件名。`prepare-checker` 仅用于复核开始前的初审副本。普通复制交接并不强制使用它。

## 开发者重建

正常重建只读 `source_catalog_v_2_1_1.xlsx`，不依赖 HTML 审阅程序或 JSON 交接文件。

```bash
python human_adjudication/human_adjudication_v_2_1_1/build_v_2_1_1.py build --output-dir /tmp/adjudication-new-build
python -m unittest discover -s human_adjudication/human_adjudication_v_2_1_1 -p 'test_v_2_1_1.py' -v
```

`freeze-source` 是一次性开发者迁移入口，只读取 v.2.0.4 HTML 中的候选数据，转换为 XLSX 源目录。它不读取用户答案，不导入内嵌测试记录，也不是 v.2.1.* 的人工流程。现已提供冻结目录，日常与常规重建无需再次执行。

当前年度审阅 schema 为 `xlsx-adjudication-3`，记录 `revision=v.2.1.1`；XLSX 候选源目录 schema 仍为 1，源内容不变。schema 3 对应初审删除 Paper 列、disposition 空白起始及扩展 Codebook。旧版表头不作为新版输入。由于人工尚未开始，本次只更新了经确认无人填写的模板，没有迁移人工作答。详见 [v.2.1.1 修订资料](../../ignorance_documents/human_adjudication_v_2_1_1/README.md)。
