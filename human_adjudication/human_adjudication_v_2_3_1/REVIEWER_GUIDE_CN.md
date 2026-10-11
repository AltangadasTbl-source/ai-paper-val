# v.2.3.1 人工复核工作指南（新 reviewer）

适用版本：v.2.3.1 primary-review workbook（schema `xlsx-adjudication-independent-primary-2.3.1`），2018、2019、2024、2025 四个年度。
编写日期：2026-10-10。本指南以各 workbook 内的 `Codebook` 为准；两者不一致时，以 `Codebook` 的选项定义为准。

术语约定：sheet 名、列名、选项代码（如 `retain`、`statistical_results`、`primary_done`）、关系代码（`S_W`、`S_C`、`P_R`、`P_P`）以及 candidate、paper package 等专门术语一律保留英文，正文用中文说明。

---

## 1. 任务是什么

AI pipeline 对每篇 JAMA 论文的 paper package 做了数值和统计报告一致性检查，并提出若干 candidate。每个 candidate 只是 AI 标记的“可能问题”，**不是已确认的错误**。

你的任务是对分配给你的年度 workbook 做 **independent primary review**：

- 逐条对照原始 PDF，独立判断该 candidate 应 `retain`、`exclude` 还是 `discuss`；
- 确认或修改 AI 建议的 review domain，并回答该 domain 下要求的判断；
- 用 Excel 内置的检查确认填写完整，然后交回 workbook。

每个年度有两位 reviewer（role 为 `R_A` 和 `R_B`），各自独立完成同一批 candidate。**不需要、也不允许与另一位 reviewer 协商**；分歧由协调人在之后统一处理。

---

## 2. 开始前的准备

### 2.1 需要的文件

| 内容 | 位置 |
|---|---|
| 你的空白 workbook | `human_adjudication/human_adjudication_v_2_3_1/<year>/release/human_adjudication_v_2_3_1_<year>_<R_A 或 R_B>.xlsx`（只用协调人分配给你的那一个） |
| paper packages | 仓库根目录下 `<year>/<paper-id>/`，例如 `2019/jama.2019.10517/` |
| 关系代码规则（参考） | `meta_report/consistency_reclassification_2026-09-04/CODING_RULES.md` |

注意，2025 年度包含两篇 ID 为 `jama.2024.*` 的论文（`jama.2024.24764`、`jama.2024.27643`），它们位于 `2025/` 目录下。年度归属以 workbook 为准，不以 DOI 年份推断。

### 2.2 工具

- 桌面版 Excel（下拉菜单、公式和条件格式需要 Excel 才能正常工作）；
- PDF 阅读器（能按页跳转）；
- 用于复算的 R 或计算器（见第 8 节示例代码）。

### 2.3 独立性规则（必须遵守）

1. **只打开分配给你的 workbook。** 不要打开另一 role 的文件，也不要打开以下包含他人或 AI 已完成答案的位置：
   - `human_adjudication/human_adjudication_v_2_3_1/ai_reviewer_runs/`
   - `human_adjudication/human_adjudication_v_2_3_1/Bulun_version/`
   - `human_adjudication/previous/`
2. **先独立判断，后看 AI 推理。** 对每个 candidate，先根据原始 PDF 形成自己的判断，再按需查看 pipeline 的推理（第 4 节）。AI 的推理可以帮助你定位证据，但不能代替你的核对。
3. **以下文件在完成本人判断之前不要打开**，因为它们可能包含早期版本的结论或他人标注：
   - 各 package 中的 `.ai_paper_validation/human_adjudication_report.md`、`human_adjudication_submission.md`；
   - `2024/jama.2024.2302/Detailed_Errors_On_C1_C3_C5.docx`；
   - `meta_report/` 下的 `review_<year>.md`、`spot_review_*.md`、`reclassified_candidates.*`（其中含 AI 建议的 disposition）。
4. **不要在 final report 的 “Human adjudication fields” 中填写**（Validity、Importance、Action、Initials、Notes 等）。全部判断只记录在 Excel workbook 中。
5. 不要修改 paper package 中的任何文件。

---

## 3. Workbook 结构

### 3.1 Sheet 一览

| Sheet | 用途 |
|---|---|
| `Setup` | 填写本人身份。B2 为 reviewer ID 或姓名（必填），B3 为全名（可选）。B4 的 role 和 B5 的年度已预设，**不要修改**。 |
| `Checks` | 全表汇总：candidate 总数、`PRIMARY READY` 行数、未完成行数、`discuss` 行数，以及 `Workflow status`。 |
| `Papers` | 论文列表与各论文 candidate 数。点击 `Review worksheet` 列跳到对应 `C_` sheet；也可直接点击底部的 sheet 标签。 |
| `C_<paper-id>` | 每篇论文一个 sheet，每行一个 candidate，是主要工作区。 |
| `Codebook` | 所有字段和选项的英文定义，判断时以此为准。 |

workbook 不包含结果汇总表。reviewer 只负责逐条录入判断；结果汇总由协调人在收齐 workbook 后另行完成。

### 3.2 `C_` sheet 的列

| 列 | 名称 | 你要做什么 |
|---|---|---|
| A | Candidate key | 只读。格式为 `<year>::<paper-id>::Cxxx`，**不要修改**。 |
| B | Candidate title | 只读。AI 对 candidate 的简短描述。 |
| C | Source location | 只读。原始文件名与 PDF 页码，即你需要核对的位置。 |
| D | Disposition | 必填：`retain`、`exclude` 或 `discuss`。 |
| E | Review domain | 预填为 AI 建议，可编辑。确认或修改为四个 domain 之一。 |
| F | Complete | 起草时为 `no`；完成人工核对后改为 `primary_done`。 |
| G | Validation hint | 公式自动计算，只读。显示该行的检查结果。 |
| H | Statistcal_or_numerical issue（部分年度表头拼写如此） | 依 domain 决定是否必填。 |
| I | Substantiveness | 依 domain 决定是否必填。 |
| J | Downstream impact | 可选。 |
| K | Report-internal or planning-material inconsistency | 依 domain 决定是否必填。 |
| L | Protocol interpretation | 可选。 |
| M–Q | （隐藏的空白间隔列） | 不使用。 |
| R | Notes (optional) | 可选，**用英文**记录证据位置、复算过程和理由。 |

颜色约定：黄色为通用或必填字段，蓝色为可选字段，灰色为当前不适用字段。

### 3.3 H–L 的默认公式

H–L 未被填写时含有公式：当某字段可能适用（D 为空或 `retain`，且 E 属于对应 domain）时显示为空白；否则显示 `not_applicable`。

- 从下拉菜单选择答案会**覆盖**该公式，这是正常的。
- 之后修改 D 或 E，**已填写的答案不会自动清除**。需要手动删除不再适用的答案（删除后为空白即可），否则 G 会提示 `CLEAR INACTIVE VALUES`。
- 不要对适用字段选择 `not_applicable`：它表示“不适用”，不是“无问题”或“不确定”。

---

## 4. Paper package 的结构与使用

每个 package 位于 `<year>/<paper-id>/`，包含原始文件和 AI pipeline 的处理记录。

### 4.1 原始文件（判断依据）

- 主论文 PDF，通常为 `jama_<author>_<year>_oi_<id>.pdf`；
- supplements，通常为 `joi<id>supp1_prod.pdf`、`supp2`、……，可能是 protocol、SAP、eTables/eFigures、data sharing statement 等，有时含 `.xlsx`；
- 文件的角色（protocol、SAP 或 results supplement）按内容判断，不按文件序号判断。

**一切判断以原始 PDF 为准**。pipeline 的文字提取或 OCR 可能出错，尤其在表格、上下标、负号和扫描页上。

### 4.2 AI pipeline 处理记录（`.ai_paper_validation/`）

| 位置 | 内容 | 用法 |
|---|---|---|
| `final_report_<wf>.md` / `.html` | 最终报告。`## Candidate Evidence Cards` 下每个 candidate 有一张卡片，标题为 `## Cxxx — <title>`。 | workbook key 末尾的 `Cxxx` 与卡片编号一一对应。卡片含 Candidate statement、Exact source locations（带页码链接）、Source evidence、Reported-versus-comparator、Calculation、Alternative source-grounded interpretations、Mechanical evidence recheck 和 Human verification steps。 |
| `review_<wf>/candidate_ledger.md` | candidate 台账 | 查 candidate 的产生过程与状态。 |
| `review_<wf>/verification/`、`quality/` | 证据复查与质量审核 | 查 AI 是否已复核原文。 |
| `review_<wf>/statistics/`、`relationships/`、`extraction/`、`checkers/` | 统计复算、文档关系映射、抽取与各 checker 输出 | 查 AI 的具体计算与比较对象。 |
| `review_<wf>/limitations.md`、`source_coverage.md`、`coverage_manifest.md` | 局限与覆盖范围 | 了解哪些页面或内容未被可靠处理。 |
| `document_outputs/<DOC-ID>/`、`preprocessing/` | 各文件的抽取文本、OCR、渲染页面 | 原 PDF 难以阅读时作辅助，但仍需回到 PDF 核对。 |

`<wf>` 为 workflow 版本，按 package 不同：

| 年度 | workflow |
|---|---|
| 2018 | `1_5_2` |
| 2019 | `1_5_1`；`jama.2019.17380` 和 `jama.2019.7505` 为 `1_5_2` |
| 2024 | `1_5_3` |
| 2025 | `1_5_1`；`jama.2024.24764` 和 `jama.2024.27643` 为 `1_5_3` |

部分 package 另有不带版本号的旧版 `final_report.md`，**请使用带版本号的那一份**。

各 package 根目录的 `AGENTS.md`、`START_PROMPT.md`、`README.md` 是 pipeline 的运行说明，与人工判断无关。

### 4.3 关系代码（relationship code）

AI 对每个 candidate 记录了它涉及哪些文档之间的比较（定义见 `CODING_RULES.md`）：

| 代码 | 含义 | 通常对应的 review domain |
|---|---|---|
| `S_W` | 同一份主论文内部，或同一份非计划类 supplement 内部（算术、统计、标签、定义不一致） | `statistical_results` 或 `report_internal_inconsistency` |
| `S_C` | 主论文与非计划类 supplement 之间，或两份非计划类 supplement 之间 | `statistical_results` 或 `report_internal_inconsistency` |
| `P_R` | 已报告的论文或结果 supplement 与 protocol/SAP 之间（不意味着已证实违反 protocol） | `protocol_report` |
| `P_P` | 仅在 protocol/SAP 内部，或在不同计划文件、版本之间 | `plan_material` |

关系代码不在 workbook 中显示。你可以根据 C 列和卡片中涉及的文件自行判断。关系代码本身不会因你修改 E 而改变。

---

## 5. 逐步操作流程

### 第 1 步：建立工作副本并填写身份

1. 在 Excel 中打开分配给你的 workbook，**另存为**（Save As）工作副本，例如 `human_adjudication_v_2_3_1_<year>_<role>_<你的ID>.xlsx`。
2. 在 `Setup` B2 填写你本人的 ID 或姓名，不要填 role 标签（`R_A`/`R_B`），前后不要留空格（2019 年度会检查空格）。B3 可选。
3. 此时 G 列应从 `CHECK REVIEWER ID`（2024 年度为 `ENTER REVIEWER ID`）变为 `PRIMARY DRAFT` 或其他字段提示。

### 第 2 步：逐篇、逐条核对

建议按 `Papers` 的顺序逐篇进行，每篇从第一个 candidate 开始：

1. 读 B 列的 title 和 C 列的 source location。
2. **打开原始 PDF 到对应页**，找到被引用的文字、表格或图，确认 AI 描述的数值和文字确实存在、页码正确。
3. 找到比较对象（同表其他行、正文、abstract、supplement、protocol/SAP），确认两者描述的是**同一人群、同一时间点、同一定义、同一模型**。
4. 对数值类 candidate，**亲自复算**（第 8 节）。
5. 考虑是否有合理的替代解释：舍入规则、不同的分母或分析人群、不同的统计检验、多选题、竞争风险或首次事件分析、文中已披露的近似或调整等。
6. 形成自己的判断后，如有需要，再打开 final report 中对应的 `Cxxx` 卡片，对照 AI 的计算与替代解释，检查自己是否遗漏证据。若因此改变判断，请在 R 列注明原因。

### 第 3 步：选择 D（Disposition）

| 选项 | 何时使用 |
|---|---|
| `retain` | 该 candidate 经你核对后应作为一个发现保留，包括确认存在问题，或存在需要记录的差异。之后需回答该 domain 的判断字段。保留 protocol 差异不等于确认存在错误。 |
| `exclude` | 已核对，不应保留。例如表面上的不一致有令人满意的解释、AI 读错了原文，或比较对象并不可比。 |
| `discuss` | 已认真核对，但仅凭现有材料无法确定 disposition，需要后续讨论。这是一个“暂缓”的决定，不是未处理。请在 R 列写明卡在哪里。 |

D 为空表示“未处理”，不等于 `discuss`。

关于 `exclude` 与“`retain` + 无问题”：若你确认根本不存在问题（例如差异完全由定义不同所致），一般选 `exclude`。若该 candidate 值得保留记录，但你对“是否构成问题”的判断是否定或不确定，可选 `retain`，再在 H 或 K 中选择 `not_issue`、`non_inconsistency` 或 `indeterminate`。对 `protocol_report`，若 L 为 `non_inconsistency`，`Codebook` 建议通常改选 `exclude`。

### 第 4 步：确认或修改 E（Review domain）

E 预填的是 AI 建议，**这不是人工判断**。请按实际比较的材料选择：

| Domain | 选择条件 | 必填 | 可选 | 不适用 |
|---|---|---|---|---|
| `statistical_results` | 判断的核心是报告中的数字、估计值、置信区间、分母、P 值或统计表述是否有误，即可以通过复算或统计定义来判断 | H、I | J | K、L |
| `report_internal_inconsistency` | 主论文内部、更新后的 supplement 内部，或两者之间的不一致（不限于非统计内容；若具体在判断数值或统计报告错误，改用 `statistical_results`） | K | — | H、I、J、L |
| `plan_material` | 计划材料自身的不一致，如 protocol 与 protocol、protocol 与 SAP、不同版本计划之间 | K | — | H、I、J、L |
| `protocol_report` | 计划（protocol/SAP）与最终报告之间的差异 | — | L | H、I、J、K |

当 D 为 `exclude` 或 `discuss` 时，H–L 全部不适用，应保持空白或 `not_applicable`。但 D 和有效的 E 仍然必填。

修改 E 后，请删除新 domain 下不适用字段中的旧答案。

### 第 5 步：回答 H–L

#### H：Statistcal_or_numerical issue（`statistical_results` 必填）

问题是：是否存在统计或数值报告问题？**确定程度与重要程度分开判断**，重要程度由 I 回答。

| 选项 | 含义 |
|---|---|
| `confirmed_issue` | 证据确立存在报告问题或矛盾，即使不知道正确值 |
| `probable_issue` | 证据倾向于存在问题，但仍有未排除的限制或合理替代解释 |
| `not_issue` | 表面差异可由有效的计算、定义、分析方法或报告语境解释 |
| `indeterminate` | 现有证据不足以判断是否存在问题 |

#### I：Substantiveness（`statistical_results` 必填）

问题是：该问题是否可能实质性地影响解读或数据使用？问题可以是 `confirmed_issue` 但只是 `minor_presentation`。

| 选项 | 含义 |
|---|---|
| `substantive` | 可能实质性地改变解读、数据提取或后续分析，而不仅是呈现方式 |
| `minor_presentation` | 原意仍清楚，只是格式、标签或排印上的小问题 |
| `indeterminate` | 信息不足，无法判断是否实质 |

参考思路：被 systematic review 或 meta-analysis 直接提取的估计值、置信区间或计数出错，或效应方向、显著性结论被改变，通常是 `substantive`；舍入差 0.1 个百分点、单位符号缺失但原意清楚，通常是 `minor_presentation`。

#### J：Downstream impact（`statistical_results` 可选）

只在你有有用信息时填写；留空表示未评估，不等于 `unlikely`。

| 选项 | 含义 |
|---|---|
| `direct` | 受影响的数值或定义本身可能被直接提取或用于后续分析（描述潜在影响，不代表已造成损害） |
| `possible` | 存在影响后续解读、提取或分析的合理途径，但较间接或不确定 |
| `unlikely` | 结果仍清楚可用，不太可能改变提取或分析 |
| `unknown` | 材料不足以判断 |

#### K：Report-internal or planning-material inconsistency（`report_internal_inconsistency` 或 `plan_material` 必填）

| 选项 | 含义 |
|---|---|
| `substantive_inconsistency` | 相互冲突的陈述、数值、标签或描述，可能实质性地改变对研究、人群、程序或结果的理解 |
| `minor_presentation` | 确有差异，但主要影响呈现方式，原意仍清楚 |
| `non_inconsistency` | 考虑定义、人群、时间点或语境后，两者并不矛盾（包括措辞不同但含义相同） |
| `indeterminate` | 材料不足，无法确定是否矛盾或矛盾有多重要 |

#### L：Protocol interpretation（`protocol_report` 可选）

只在有助于描述时填写，留空不影响完成。`retain` 的 protocol 差异只作描述，不进入时间趋势分析。无需另行查找修改记录或变更理由。

| 选项 | 含义 |
|---|---|
| `substantive_difference` | 计划与报告在结局、人群、程序或分析上存在有意义的差异（仅描述差异，不等于认定违规或不合理变更） |
| `minor_presentation` | 措辞、标签或呈现上的小问题，计划与报告的含义仍清楚 |
| `version_timing` | 差异可能源于所比较的 protocol 版本或日期不同，现有材料无法判断先后 |
| `non_inconsistency` | 经核对两者相容（通常应改为 D = `exclude`） |
| `indeterminate` | 证据不足以作出更具体的解释 |

### 第 6 步：写 R 列备注（建议，英文）

R 列可选，但强烈建议对每个 `retain`、`discuss` 以及改动了 E 的行写一句英文备注，包括：

- 实际核对的文件与页码；
- 复算结果（例如 `9/64 - 6/62 = 4.39 pp; printed 4.3`）；
- 关键理由，或与 AI 判断不同之处。

不要在备注中写入参与者层面的数据。

### 第 7 步：标记完成并检查 G

1. 填写完一行并确认无误后，把 F 改为 `primary_done`。
2. G 应显示 `PRIMARY READY`。若显示其他信息，按第 6 节处理后再确认。
3. 只有真正完成人工核对后才能标 `primary_done`；起草时保持 `no`。

### 第 8 步：修改已完成的行

1. 先把 F 改回 `no`；
2. 修改 D、E 或判断，并删除不再适用字段中的旧答案；
3. 重新核对后再把 F 改为 `primary_done`。

公式**不会**自动撤销已填写的完成标记，所以必须手动改回 `no`。

### 第 9 步：交付

1. 在 `Checks` 中确认 `Workflow status` 为 `PRIMARY READY`，`Unfinished` 为 0。
2. `discuss` 行可以是 `PRIMARY READY`，但仍属未解决（unresolved），会在 `Checks` 中单独计数。完成录入不代表科学上的不确定性已解决。
3. 保存并把**你本人的 workbook** 交给协调人，同时保留一份普通备份。不要合并或转发另一位 reviewer 的文件。

---

## 6. G 列（Validation hint）提示信息与处理方法

各年度的 workbook 由不同构建器生成，提示文字略有差异：

| 提示 | 含义 | 处理 |
|---|---|---|
| `CHECK REVIEWER ID` / `ENTER REVIEWER ID` | `Setup` B2 为空、只有空白，或（2019）前后有空格 | 在 B2 填写本人 ID |
| `CHECK SETUP`（2019） | `Setup` 的 role 或年度被改动 | 恢复 B4、B5 原值 |
| `CHECK KEY` | A 列 key 为空、重复，或不属于该论文 | 撤销对 A 列的修改；排序时须整行（A:R，含隐藏列）一起移动 |
| `CHECK COMPLETE` / `CHECK COMPLETE FLAG` | F 不是 `no` 或 `primary_done`（例如粘贴了其他值） | 从下拉菜单重选 |
| `MISSING D / E`、`INVALID D / E`（2019） | D 或 E 为空或无效 | 从下拉菜单选择 |
| `CLEAR INACTIVE VALUES` | 当前 D/E 下不适用的字段中残留旧答案 | 删除这些单元格内容 |
| `MISSING REQUIRED JUDGMENT`（2019） | 必填判断为空，或误选了 `not_applicable` | 回答 H、I 或 K |
| `INVALID ACTIVE JUDGMENT`（2019）/ `CHECK FIELDS` | 适用字段中的值无效（含粘贴的值），或必填项缺失 | 从下拉菜单重选，补齐必填项 |
| `PRIMARY DRAFT` | 字段有效，但 F 还不是 `primary_done` | 完成核对后把 F 改为 `primary_done` |
| `PRIMARY READY` | 该行录入完整、有效且已标记完成 | 无需处理 |
| `CHECK INPUT ERROR` / `CHECK INPUT / KEY` / `CHECK KEY / INPUT` | 公式遇到意外输入 | 检查该行是否有粘贴的异常值或被改动的 key |

G 只检查**录入是否完整有效**，不检查**科学判断是否正确**。

---

## 7. 判断要点与常见陷阱

1. **先核对再判断。** 先确认 AI 引用的数字确实印在 PDF 的那一页。AI 的文字提取可能丢失负号、小数点或上下标，也可能把相邻行混在一起。
2. **确认可比性。** 许多表面上的不一致源于不同的分析人群（ITT 与 per-protocol、有完整数据者）、不同的分母、不同的时间点或不同的模型（校正与未校正）。
3. **舍入。** 先确认原文的舍入规则；按显示的取整值复算和按原始计数复算可能相差 0.1。此类问题通常是 `minor_presentation`。
4. **检验方法。** P 值不一致可能来自不同的检验（如 chi-square 是否做连续性校正、log-rank 与 Cox 模型）。先找出原文用的方法，再判断。
5. **分类变量。** 多选题、亚组首次事件分析、竞争风险下的组分结局，其各类别之和不必等于总数。
6. **置信区间与 P 值的相容性。** 若 95% CI 不含零值（差值为 0，比值为 1）却报告 P > .05，或 CI 包含零值却报告 P < .05，通常提示符号、端点或标签有误。
7. **系统性错误。** 同一表格多行出现同类错误时（如整列比值方向颠倒、2×2 表转置、CI 一律偏窄），每个 candidate 仍需逐条判断；可在 R 列注明“同一系统性错误”。
8. **确定程度与重要程度分开。** H 回答“是不是问题”，I 回答“重不重要”。不要因为问题小而选 `not_issue`。
9. **合理使用 `discuss` 和 `indeterminate`。** 证据确实无法定案时，不要勉强给出确定判断。若 candidate 应保留，但“是否构成问题”无法判断，用 `retain` 加 `indeterminate`；若连是否保留都无法判断，用 `discuss`。
10. **超出 candidate 范围的发现。** 核对中若发现其他疑似错误，不要新增行；在相关行的 R 列简要记录，或另行告知协调人。

---

## 8. 常用复算（R 示例）

以下函数为常规公式，结果应与原文报告的方法对照使用。原文使用模型校正估计、bootstrap 或其他方法时，粗算结果只能作参考。

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

# Example: rd(9, 64, 6, 62); rr(9, 64, 6, 62); p_from_ci(0.93, 0.83, 1.04)
```

---

## 9. 常见问题

**E 预填的 domain 必须保留吗？**
不必。它是 AI 建议，请按第 5 节第 4 步自行判断。修改后删除不适用字段中的旧答案。

**AI 卡片说“confirmed”，我也必须选 `confirmed_issue` 吗？**
不必。卡片顶部注明 “Pending Human Adjudication”，AI 的结论只是待核对的假设。

**我能看 AI 的计算吗？**
可以，但应在形成自己的判断之后再看，并以原始 PDF 为准。若参考 AI 后改变了判断，请在 R 列说明。

**表格排序会出问题吗？**
key 按内容匹配，可以排序，但必须选中整行 A:R（包括隐藏的 M–Q 列）一起排序，否则 G 会提示 `CHECK KEY` 或判断错位。

**workbook 有保护或密码吗？**
没有。所有单元格均可编辑。请不要修改 A–C 列、G 列公式和 `Setup` 的 B4–B5；误改后用撤销或从备份恢复。

**PDF 某页是扫描图像，无法搜索文字怎么办？**
直接读图像页面。也可参考 `.ai_paper_validation/document_outputs/` 或 `preprocessing/` 中的 OCR 文本，但数值必须回到 PDF 页面核对。
