# v.2.4.1 人工复核工作指南（Excel independent primary review）

适用版本：v.2.4.1 primary-review workbook，2018、2019、2024、2025 四个年度。
编写日期：2026-10-11。字段与选项的定义以各 workbook 内的 `Codebook` sheet 为准；本指南与 `Codebook` 不一致时，以 `Codebook` 为准。

术语约定：sheet 名、列名、选项代码（如 `retain`、`statistical_results`、`primary_done`）、关系代码（`S_W`、`S_C`、`P_R`、`P_P`）以及 candidate、paper package 等专门术语保留英文，正文用中文说明。

---

## 1. 任务

AI pipeline（workflow 1.6.2）对每篇 JAMA 论文的 paper package 做了数值与统计报告一致性检查，提出若干 candidate。candidate 是 AI 标记的“可能问题”，**不是已确认的错误**。

你的任务是对分配给你的年度 workbook 做 **independent primary review**：

1. 逐条对照原始 PDF，独立判断 candidate 应 `retain`、`exclude` 还是 `discuss`；
2. 确认或修改 AI 建议的 review domain，并回答该 domain 要求的判断；
3. 用 workbook 内置检查确认录入完整，然后交回 workbook。

每个年度有两位 reviewer（`R_A`、`R_B`），各自独立完成同一批 candidate。**不与另一位 reviewer 协商**；分歧由协调人在收齐两份 workbook 后统一处理。

### 本版的复核量

| 年度 | 论文 | 每位 reviewer 的 candidate | statistical_results | report_internal_inconsistency | plan_material | protocol_report |
|---|---:|---:|---:|---:|---:|---:|
| 2018 | 10 | 115 | 49 | 4 | 7 | 55 |
| 2019 | 9 | 79 | 26 | 0 | 4 | 49 |
| 2024 | 10 | 113 | 51 | 2 | 15 | 45 |
| 2025 | 15 | 133 | 49 | 3 | 11 | 70 |

domain 计数为 AI 建议，不是人工判断。约一半 candidate 属于 `protocol_report`，原因见第 6.4 节。

---

## 2. 开始前的准备

### 2.1 文件

| 内容 | 位置 |
|---|---|
| 你的空白 workbook | `human_adjudication/human_adjudication_v_2_4_1/<year>/human_adjudication_v_2_4_1_<year>_<R_A 或 R_B>.xlsx`（只用协调人分配给你的那一个） |
| paper packages | 仓库根目录下 `<year>/<paper-id>/`，例如 `2019/jama.2019.10517/` |
| AI 最终报告 | `<year>/<paper-id>/.ai_paper_validation/final_report_1_6_2.html`（或 `.md`） |
| domain 与关系代码的 pipeline 定义（参考） | 各 package 根目录的 `QUALITY_CONTROL_SCOPE.md`，“The four review domains” 与 “Relationship types” 两节 |

### 2.2 工具

- 桌面版 Excel（下拉菜单、公式与条件格式需要 Excel）；
- 能按页跳转的 PDF 阅读器；
- R 或计算器，用于复算（第 9 节）。

### 2.3 独立性规则（必须遵守）

1. **只打开分配给你的 workbook。** 不要打开另一 role 的文件。
2. **不要打开含有既往答案或 AI 判断的位置：**
   - `human_adjudication/human_adjudication_v_2_3_1/` 下的全部 workbook，尤其是 `ai_reviewer_runs/` 与 `Bulun_version/`（部分 candidate 与本版重叠，那里有已填写的判断）；
   - `human_adjudication/previous/`；
   - `meta_report/` 下的 `review_<year>.md`、`spot_review_*.md`、`reclassified_candidates.*`；
   - `2024/jama.2024.2302/Detailed_Errors_On_C1_C3_C5.docx`。
3. **只使用 1.6.2 的报告。** package 中的 `review_1_5_*`、`review_1_6_1` 以及不带 `1_6_2` 的旧版 `final_report*.md` 属于早期 pipeline，不要用作依据。
4. **先独立判断，再看 AI 推理。** 先依据原始 PDF 形成判断，再按需查看 final report 的卡片（第 4 节）。若查看后改变判断，在 R 列注明。
5. 不要在 final report 中填写任何内容，也不要修改 paper package 中的任何文件。各 package 根目录的 `AGENTS.md`、`START_PROMPT.md` 等是 pipeline 运行说明，与人工复核无关。

---

## 3. Workbook 结构

### 3.1 Sheet

| Sheet | 用途 |
|---|---|
| `Setup` | B2 填 reviewer ID 或姓名（必填），B3 全名（可选）。B4 的 role 和 B5 的年度已预设，**不要修改**。 |
| `Checks` | 汇总：candidate 总数、`PRIMARY READY` 行数、`discuss` 行数、未完成行数及 `Workflow status`。 |
| `Papers` | 论文列表与各论文 candidate 数。点击 `Review worksheet` 列的链接跳到对应 `C_` sheet。 |
| `C_<paper-id>` | 每篇论文一个 sheet，每行一个 candidate，是主要工作区。 |
| `Codebook` | 所有字段与选项的英文定义。 |

workbook 不含证据 sheet 和结果汇总表：证据在原始 PDF 和 final report 卡片中，结果汇总由协调人完成。

**2025 年度特别说明：** 2025 年度还包含两篇 ID 为 `jama.2024.*` 的论文（`jama.2024.24764`、`jama.2024.27643`），它们位于仓库的 `2025/` 目录下；年度归属以 workbook 为准，不以 ID 推断。

### 3.2 `C_` sheet 的列

| 列 | 名称 | 操作 |
|---|---|---|
| A | Candidate key | 只读，格式 `<year>::<paper-id>::Cxxx`，**不要修改**。`Cxxx` 与 final report 卡片编号一一对应。 |
| B | Candidate title | 只读，与 final report 卡片标题相同。 |
| C | Source location | 只读，原始文件名与 PDF 页码。报告中未写文件名的位置已补成 `<文件名> — <位置>`。 |
| D | Disposition | 必填：`retain`、`exclude` 或 `discuss`。初始为空。 |
| E | Review domain | 预填 AI 建议，可编辑。 |
| F | Complete | 起草时为 `no`，完成人工核对后改为 `primary_done`。 |
| G | Validation hint | 公式，只读。 |
| H | Statistical_or_numerical issue | 依 domain 而定。 |
| I | Substantiveness | 依 domain 而定。 |
| J | Downstream impact | 可选。 |
| K | Report-internal or planning-material inconsistency | 依 domain 而定。 |
| L | Protocol interpretation | 可选。 |
| M–Q | 隐藏的空白列 | 不使用。 |
| R | Notes (optional) | 可选，**用英文**记录核对位置、复算与理由。 |

### 3.3 H–L 的默认公式

H–L 未填写时含公式：若该字段可能适用（D 为空或 `retain`，且 E 属于对应 domain），显示空白；否则显示 `not_applicable`，并以底纹标示为不适用。

- 从下拉菜单选择答案会**覆盖**公式，这是正常的。
- 之后修改 D 或 E，**已填写的答案不会自动清除**。请手动删除不再适用的答案（删成空白即可），否则 G 显示 `CLEAR INACTIVE VALUES`。
- 不要对适用字段选择 `not_applicable`。它表示“不适用”，不是“无问题”或“不确定”。

---

## 4. Final report 卡片（辅助材料）

每篇论文的 `final_report_1_6_2.html` 中，`Candidate Evidence Cards` 下每个 candidate 有一张卡片，标题为 `Cxxx — <title>`。常用字段：

| 字段 | 用途 |
|---|---|
| Candidate statement | AI 对差异的一句话陈述，比 B 列标题完整 |
| Exact source locations / Source evidence | 带页码链接的原文位置与摘录 |
| Reported-versus-comparator、Calculation | 比较对象与 AI 的复算 |
| Relationship type / All relationships / Compared document roles | 涉及哪些文档（第 5 节） |
| Qualifying route | AI 纳入该 candidate 的理由：`Route A, category N`（固定纳入类别）或 `Route B`（一般标准） |
| Alternative source-grounded interpretations | AI 考虑过的替代解释 |
| Classification rationale / ambiguity | AI 对 domain 归类的理由与不确定之处 |
| Affected result or extracted value | 可能受影响的结果或可提取数值 |

卡片中的 “reproduced”“CONFIRMED” 只表示 AI 自身复核与纳入审核的状态，**不是人工结论**，也不意味着应选 `confirmed_issue`。

已知限制：`2018::jama.2018.18020::C022` 的 C 列没有具体文件与页码（报告原文只写“见下方表格”），请直接使用该卡片中的 source-evidence 表。部分 C 列内容较长（列表或表格被合并为一段，以 `; ` 分隔）。

一切判断以原始 PDF 为准。pipeline 的文字提取或 OCR 可能丢失负号、小数点、上下标，或混淆相邻行。

---

## 5. 关系代码与四个 domain 的对应

| 代码 | 比较对象 | 对应 domain |
|---|---|---|
| `S_W` | 同一份报告文件内部（主论文内部，或同一份非计划类 supplement 内部） | `statistical_results` 或 `report_internal_inconsistency` |
| `S_C` | 两份不同的报告文件之间（主论文与非计划类 supplement，或两份 supplement） | `statistical_results` 或 `report_internal_inconsistency` |
| `P_R` | 报告（主论文或结果 supplement）与计划（protocol、SAP）之间 | `protocol_report` |
| `P_P` | 仅在计划材料内部，或不同计划文件、版本之间 | `plan_material` |

同时涉及多种关系时，pipeline 按 `P_R` > `P_P` > `S_C` > `S_W` 选主关系。只“佐证”一方的文件不算关系：例如 protocol 仅印证报告内部矛盾中的正确值，该 candidate 仍属报告内部问题。

关系代码不在 workbook 中显示，修改 E 也不会改变它。E 应按**你实际判断时比较的材料与问题性质**选择（第 6 节）。

---

## 6. 四个 review domain：含义与典型例子

> 说明：以下例子均为**虚构的示意**，不取自本次任何 candidate，以免影响独立判断。每类列出常见形态和一般的判断思路，实际判断以原文和 `Codebook` 为准。

### 6.1 `statistical_results`（统计结果）

**含义：** 报告材料中的数字、估计值、置信区间、分母、检验或统计方法逻辑本身是否有误，可通过复算或统计定义判断。只要问题涉及计数、估计、区间、检验或统计方法，pipeline 一律归入此类，即使它出现在两份报告文件之间。

**必填：** H（是否存在问题）与 I（是否实质）；J 可选。

**典型形态：**

| 形态 | 虚构示例 | 判断思路 |
|---|---|---|
| 计数、分母与百分比不符 | 表中印 “27/180 (21.0%)”，而 27/180 = 15.0% | 先排除分母为另一人群（如有完整数据者）；若仍不符，通常 `confirmed_issue`；数值若会被提取，I 多为 `substantive` |
| 区间与 P 值不相容 | “HR 0.82 (95% CI 0.70–0.96); P = .21” | 由区间反推的 P 约为 .01，与 .21 冲突。先确认二者是否来自同一模型；若是，通常 `confirmed_issue` |
| 点估计在区间外或端点顺序颠倒 | “RD 4.6 (95% CI 5.1 to 9.8)” | 多为排印或抄录错误；是否 `substantive` 取决于是否影响显著性或提取值 |
| 摘要与正文数值不一致 | 摘要 “OR 1.45”，正文表格 “OR 1.54” | 超出舍入范围即为差异；读者无法确定取哪个值时通常 `substantive` |
| 无法复现的计算 | 同一表中其余行均按 Wald 法复现，唯独一行的 CI 偏窄 | 先确认方法；方法不明时可用 `probable_issue` 或 `indeterminate`，并在 R 列写明需要的信息 |
| 方法逻辑缺口 | 文中称数据为配对设计，表注却写独立样本 t 检验 | 判断报告是否自相矛盾，而不是你偏好哪种方法 |

**常见陷阱：** 舍入（先确认原文保留几位小数）；校正与未校正估计；ITT 与 per-protocol；连续性校正与否；多选题或竞争风险下各类别之和不必等于总数。差异仅由舍入造成时，选 `exclude`，或 `retain` + `not_issue`（见第 7 步第 3 小节）。

### 6.2 `report_internal_inconsistency`（报告内部不一致）

**含义（以 `Codebook` 为准）：** 主论文内部、更新后的 supplement 内部，或两者之间的不一致；不限于非统计内容，但若具体在判断数值或统计报告错误，应改用 `statistical_results`。

pipeline 的纳入标准更窄：仅限报告各处对“某个数字属于哪个结局、时间点、分析人群或比较”说法冲突，使读者无法确定适用哪个结果；单纯措辞或标签差异不纳入。因此本版此类很少（2018 年 4 条、2019 年 0 条、2024 年 2 条）。

**必填：** K。

**典型形态：**

| 形态 | 虚构示例 | 判断思路 |
|---|---|---|
| 同一结果对应不同时间起点 | 摘要称结局“自随机化起 90 天”，supplement 同一结果表注为“自出院起 90 天” | 两个起点会改变结果含义，通常 `substantive_inconsistency` |
| 亚组或人群标签无法对应数值 | 森林图标签写“≤6 h / >6 h”，表格只有一组数值，看不出属于哪一组 | 若读者无法确定归属，可为 `substantive_inconsistency` 或 `indeterminate` |
| 结局层级在报告内前后不一 | 方法部分称某结局为 tertiary，讨论部分将其列入 secondary | 是否影响理解决定 `substantive_inconsistency` 还是 `minor_presentation` |
| 措辞不同但含义相同 | “participants” 与 “enrolled patients” 指同一群体 | `non_inconsistency`，通常改选 `exclude` |

### 6.3 `plan_material`（计划材料内部不一致）

**含义：** protocol 或 SAP 自身，或不同计划文件、版本之间，在报告分析所依赖的统计设计要素上不一致。比较对象只有计划材料，不涉及报告。

**必填：** K。

**典型形态：**

| 形态 | 虚构示例 | 判断思路 |
|---|---|---|
| 计划内的数值笔误 | 正文假设事件率 0.08%，附录样本量计算用 0.8% | 判断哪一个实际用于样本量；若影响设计理解，通常 `substantive_inconsistency` |
| 样本量或 power 无法由所给输入复现 | SAP 称“80% power 检出 15% 差异”，按其给出的比例与样本量算得约 60% | 先确认是否有未说明的假设（单侧检验、脱落率、连续性校正）；无法确定时用 `indeterminate` |
| 期中分析、停止或非劣效规则前后矛盾 | 正文的非劣效界值为 −0.10，同一 SAP 的签字版写 +0.10 | 符号或方向冲突会改变决策区域，通常 `substantive_inconsistency` |
| 不同计划版本的定义不同 | protocol 的结局时间起点为“手术开始”，SAP 写“麻醉开始” | 判断差异是否影响报告分析；措辞差异可为 `minor_presentation` |
| 不属于设计要素的内容 | protocol 背景部分引用的既往研究结果自身不一致 | 不影响本试验的设计或分析，一般 `exclude` |

若某个 `plan_material` candidate 实际在比较计划与报告，应改为 `protocol_report`；反之亦然。

### 6.4 `protocol_report`（计划与报告的差异）

**含义：** 报告与 protocol 或 SAP 在统计设计或分析要素上存在差异。这只是**描述差异**，不等于认定违反 protocol 或不当变更。`Codebook` 明确：不要求查找修改记录或变更理由。

**必填：** 无（只需 D 与有效的 E）；L 可选。

**为什么数量多：** 1.6.2 规定以下三种情况一经复现即纳入，不经语境、措辞等筛除：结局地位（primary、secondary、safety 等）或复合结局定义改变；报告称“预先设定”但所给计划中没有；计划的 primary 或 key secondary 分析未报告。另外，protocol 与 SAP 往往很长且有多个版本，每项具体承诺都是一个比较点，而期刊论文篇幅有限。

**典型形态：**

| 形态 | 虚构示例 | 判断思路 |
|---|---|---|
| 计划的分析或结果在报告中找不到 | SAP 规定对主要结局做 complete-case 敏感性分析，论文及 supplement 均无此结果 | 先**在所有提供的报告文件中搜索**（主论文、全部结果 supplement）。找到了，说明 AI 漏看，选 `exclude`；确实没有，选 `retain` |
| 分析方法或模型改变 | 计划为 Cox 模型，报告用 log-binomial 模型；协变量集合不同；多重插补数不同 | 若方法确实不同，选 `retain`，L 通常为 `substantive_difference` |
| 结局定义、时间窗或测量方式改变 | 计划的主要结局在 12 个月评估，报告在 6 个月 | 典型 `substantive_difference`（这正是 `Codebook` 的示例） |
| 人群、纳入标准、随机分层或亚组切点改变 | 计划纳入 ≥65 岁，报告写 ≥60 岁；亚组切点从中位数改为固定值 | 判断是否改变分析人群或亚组归属 |
| 结局层级改变，或“预先设定”无计划依据 | 计划的 secondary 结局在报告中称 post hoc；报告称某亚组“prespecified”，计划中没有 | 先核对所有计划版本；若较早或较晚版本中可以找到，考虑 `version_timing` |
| 等价表述 | 计划写 “week 12”，报告写 “12 weeks after baseline” | `non_inconsistency`，通常选 `exclude` |

**L 的选项提示：**

- 报告自己已披露的变更（例如注明 post hoc，或说明因模型不收敛而改用 GEE）仍然是计划与报告的差异；披露本身不消除差异。可在 R 列注明 “disclosed in report, p. x”。
- 若差异可能源于比较了不同版本的 protocol 或 SAP，且无法从材料判断先后，选 `version_timing`。
- 留空不影响完成；留空表示未描述，不等于无差异。

---

## 7. 逐步操作流程

### 第 1 步：建立工作副本并填写身份

1. 用 Excel 打开分配给你的 workbook，**另存为**工作副本，例如 `human_adjudication_v_2_4_1_<year>_<role>_<你的ID>.xlsx`。
2. 在 `Setup` B2 填写本人 ID 或姓名（不要填 `R_A`/`R_B`）。B3 可选。
3. G 列应从 `CHECK REVIEWER ID` 变为 `PRIMARY DRAFT` 或其他字段提示。

### 第 2 步：逐篇、逐条核对

按 `Papers` 顺序逐篇进行，每篇从 C001 开始：

1. 读 B 列标题与 C 列位置。标题较短，需要完整陈述时看卡片的 Candidate statement。
2. **打开原始 PDF 到对应页**，确认被引用的文字、表格或图确实存在，数值与 AI 描述一致。
3. 找到比较对象（同表其他行、正文、摘要、supplement、protocol 或 SAP），确认两者指**同一结局、人群、时间点、定义和模型**。
4. 数值类 candidate **亲自复算**（第 9 节）。
5. 考虑替代解释：舍入、不同分母或分析人群、不同检验、校正与未校正、已披露的近似或修改等。
6. 形成判断后，可打开对应卡片核对 AI 的计算与替代解释，检查是否遗漏证据。

### 第 3 步：选择 D（Disposition）

| 选项 | 何时使用 |
|---|---|
| `retain` | 核对后应作为发现保留：确认存在问题，或存在需要记录的差异。随后回答该 domain 的字段。保留 protocol 差异不等于确认错误。 |
| `exclude` | 已核对，不应保留：表面不一致有令人满意的解释、AI 读错原文、比较对象不可比，或计划的结果其实已报告。 |
| `discuss` | 已认真核对，但仅凭现有材料无法确定 disposition。这是“暂缓”而非“未处理”，请在 R 列写明卡在哪里。 |

D 为空表示未处理，不等于 `discuss`。

`exclude` 与 “`retain` + 无问题” 的区别：确认根本不存在问题时，一般选 `exclude`。若值得保留记录，但对“是否构成问题”的判断是否定或不确定，可选 `retain`，再在 H 或 K 中选 `not_issue`、`non_inconsistency` 或 `indeterminate`。

### 第 4 步：确认或修改 E（Review domain）

E 预填的是 AI 建议，**不是人工判断**。按第 5、6 节选择：

| Domain | 必填 | 可选 | 不适用 |
|---|---|---|---|
| `statistical_results` | H、I | J | K、L |
| `report_internal_inconsistency` | K | — | H、I、J、L |
| `plan_material` | K | — | H、I、J、L |
| `protocol_report` | — | L | H、I、J、K |

D 为 `exclude` 或 `discuss` 时，H–L 全部不适用（保持空白或 `not_applicable`），但 D 与有效的 E 仍必填。修改 E 后，删除新 domain 下不适用字段中的旧答案。

### 第 5 步：回答 H–L

**H：Statistical_or_numerical issue**（`statistical_results` 必填）：是否存在统计或数值报告问题。只回答确定程度，重要程度由 I 回答。

| 选项 | 含义 |
|---|---|
| `confirmed_issue` | 证据确立存在报告问题或矛盾，即使不知道正确值 |
| `probable_issue` | 证据倾向于存在问题，但仍有未排除的限制或合理替代解释 |
| `not_issue` | 表面差异可由有效的计算、定义、方法或语境解释 |
| `indeterminate` | 证据不足以判断 |

**I：Substantiveness**（`statistical_results` 必填）：是否可能实质性影响解读或数据使用。一个问题可以既是 `confirmed_issue` 又是 `minor_presentation`。

| 选项 | 含义 |
|---|---|
| `substantive` | 可能改变解读、数据提取或后续分析 |
| `minor_presentation` | 原意仍清楚，仅格式、标签或排印的小问题 |
| `indeterminate` | 信息不足以判断 |

**J：Downstream impact**（`statistical_results` 可选）：留空表示未评估，不等于 `unlikely`。`direct`：受影响数值本身可能被提取或用于后续分析（描述潜在影响，不代表已造成损害）；`possible`：存在间接或不确定的影响途径；`unlikely`：结果仍清楚可用；`unknown`：材料不足。

**K：Report-internal or planning-material inconsistency**（`report_internal_inconsistency` 或 `plan_material` 必填）：

| 选项 | 含义 |
|---|---|
| `substantive_inconsistency` | 冲突可能实质性改变对研究、人群、程序或结果的理解 |
| `minor_presentation` | 确有差异，但主要影响呈现，原意清楚 |
| `non_inconsistency` | 考虑定义、人群、时间点或语境后并不矛盾 |
| `indeterminate` | 材料不足以确定是否矛盾或其重要性 |

**L：Protocol interpretation**（`protocol_report` 可选）：

| 选项 | 含义 |
|---|---|
| `substantive_difference` | 计划与报告在结局、人群、程序或分析上有意义地不同（只描述差异） |
| `minor_presentation` | 措辞或标签的小问题，含义仍清楚 |
| `version_timing` | 差异可能源于所比较的版本或日期，材料无法判断先后 |
| `non_inconsistency` | 经核对两者相容（通常改选 D = `exclude`） |
| `indeterminate` | 证据不足以作出更具体的描述 |

### 第 6 步：写 R 列备注（建议，英文）

对每个 `retain`、`discuss` 以及修改过 E 的行，建议写一句英文备注：核对的文件与页码、复算结果（例如 `27/180 = 15.0%; printed 21.0%`）、关键理由或与 AI 不同之处。不要写入参与者层面的数据。

### 第 7 步：标记完成并检查 G

1. 一行填写完毕并确认无误后，把 F 改为 `primary_done`。
2. G 应显示 `PRIMARY READY`；否则按第 8 节处理。
3. 只有真正完成人工核对后才标 `primary_done`。

### 第 8 步：修改已完成的行

先把 F 改回 `no`，再修改 D、E 或判断并删除不再适用的旧答案，重新核对后再标 `primary_done`。公式不会自动撤销完成标记。

### 第 9 步：交付

1. 在 `Checks` 确认 `Workflow status` 为 `PRIMARY READY`，`Unfinished rows` 为 0。
2. `discuss` 行可以是 `PRIMARY READY`，但仍属未解决，在 `Checks` 中单独计数。
3. 保存后把**你本人的 workbook** 交给协调人，并保留备份。不要合并或转发另一位 reviewer 的文件。

---

## 8. G 列（Validation hint）提示

三个年度使用同一套公式，提示文字相同：

| 提示 | 含义 | 处理 |
|---|---|---|
| `CHECK REVIEWER ID` | `Setup` B2 为空或只有空白 | 在 B2 填写本人 ID |
| `CHECK KEY` | A 列 key 为空、重复或不属于该论文 | 撤销对 A 列的修改；排序时须整行（A:R，含隐藏列）一起移动 |
| `CLEAR INACTIVE VALUES` | 当前 D/E 下不适用的字段残留旧答案 | 删除这些单元格内容 |
| `CHECK FIELDS` | D 或 E 为空或无效、必填判断缺失、或适用字段的值无效（含粘贴值、误选 `not_applicable`） | 从下拉菜单重选，补齐必填项 |
| `CHECK COMPLETE` | F 不是 `no` 或 `primary_done` | 从下拉菜单重选 |
| `PRIMARY DRAFT` | 字段有效，F 还不是 `primary_done` | 核对完成后把 F 改为 `primary_done` |
| `PRIMARY READY` | 录入完整、有效且已标记完成 | 无需处理 |
| `CHECK INPUT / KEY` | 公式遇到意外输入 | 检查是否有粘贴的异常值或被改动的 key |

G 只检查**录入是否完整有效**，不检查科学判断是否正确。

---

## 9. 常用复算（R）

以下为常规公式，结果需与原文所用方法对照。原文使用模型校正估计、bootstrap 或其他方法时，粗算只作参考。

```r
# Proportion and risk difference (percentage points) with Wald 95% CI
rd <- function(a, n1, c, n2, level = 0.95) {
  p1 <- a / n1; p2 <- c / n2; z <- qnorm(1 - (1 - level) / 2)
  d <- p1 - p2; se <- sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
  round(100 * c(p1 = p1, p2 = p2, rd = d, lower = d - z * se, upper = d + z * se), 2)
}

# Risk ratio with log-scale Wald 95% CI
rr <- function(a, n1, c, n2, level = 0.95) {
  z <- qnorm(1 - (1 - level) / 2)
  est <- (a / n1) / (c / n2); se <- sqrt(1 / a - 1 / n1 + 1 / c - 1 / n2)
  round(c(rr = est, lower = exp(log(est) - z * se), upper = exp(log(est) + z * se)), 3)
}

# Odds ratio with log-scale Wald 95% CI (a, b = events/non-events in group 1; c, d in group 2)
or <- function(a, b, c, d, level = 0.95) {
  z <- qnorm(1 - (1 - level) / 2)
  est <- (a * d) / (b * c); se <- sqrt(1 / a + 1 / b + 1 / c + 1 / d)
  round(c(or = est, lower = exp(log(est) - z * se), upper = exp(log(est) + z * se)), 3)
}

# Approximate two-sided P value implied by an estimate and its 95% CI
# ratio = TRUE for RR/OR/HR (log scale); FALSE for differences
p_from_ci <- function(est, lower, upper, ratio = TRUE) {
  if (ratio) { est <- log(est); lower <- log(lower); upper <- log(upper) }
  se <- (upper - lower) / (2 * qnorm(0.975))
  2 * pnorm(-abs(est / se))
}

# Chi-square test on a 2x2 table, with and without continuity correction
chisq_both <- function(a, n1, c, n2) {
  m <- matrix(c(a, n1 - a, c, n2 - c), nrow = 2, byrow = TRUE)
  c(yates = chisq.test(m, correct = TRUE)$p.value,
    no_correction = chisq.test(m, correct = FALSE)$p.value)
}

# Two-sample power for proportions (compare with a plan's stated power)
# power.prop.test(n = 150, p1 = 0.42, p2 = 0.27, sig.level = 0.05)

# Display-precision check: does a printed value fit the interval implied by
# rounding each displayed input to its last shown digit?
half_unit <- function(x, digits) c(x - 0.5 * 10^-digits, x + 0.5 * 10^-digits)

sessionInfo()
```

---

## 10. 常见问题

**E 预填的 domain 必须保留吗？** 不必。按第 5、6 节自行判断，修改后清除不适用字段中的旧答案。

**卡片写着 “reproduced” 或 “CONFIRMED”，我必须选 `confirmed_issue` 吗？** 不必。那只是 AI 的内部复核状态。

**`protocol_report` 的 candidate 报告里已说明了变更理由，还要 `retain` 吗？** 差异仍然存在，一般 `retain`，并在 R 列注明已披露。`Codebook` 不要求你评判变更是否合理。

**计划的分析“未报告”，但我在某个 supplement 里找到了？** 选 `exclude`，并在 R 列写明位置。

**可以排序吗？** 可以，但必须选中整行 A:R（含隐藏的 M–Q）一起排序。

**workbook 有保护吗？** 没有。请不要修改 A–C 列、G–L 的公式（除非是通过下拉菜单作答）和 `Setup` 的 B4–B5；误改后撤销或从备份恢复。

**扫描页无法搜索文字？** 直接读图像页面；可参考 `.ai_paper_validation/` 下的 OCR 文本定位，但数值必须回到 PDF 核对。

**核对中发现 candidate 之外的疑似错误？** 不要新增行；在相关行的 R 列简要记录，或另行告知协调人。
