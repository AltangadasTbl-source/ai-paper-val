# C001–C007 中文审阅问答记录

保存日期：2026-10-20

本文件按顺序保存 C001–C007 的用户提问、助手进度说明及完整答复，并记录本次保存请求。不含工具调用输出、系统指令及项目初始化说明。为便于本地阅读，原答复中的绝对文件链接已调整为相对于本文件的链接；正文内容保留对话时的表述。

## C001

### 用户

Tell me in CN about the issue C001, include the detailed reasoning, key reference sentences and impact to downstream analysis if the review_domain says statistical_results.

### 助手进度说明

我会先查看 C001 的记录、复核结论及对应原文，再用中文解释其推理依据；如果它属于 `statistical_results`，也会说明对下游分析的影响。

### 助手答复

**C001 指的是：论文报告的主要复合终点，比原始方案增加了一项 HbA1c 否决条件。** 即使受试者达到减重或运动目标，只要第 6 或第 12 个月的 HbA1c ≥6.5%，仍被判定为主要终点未达成。

它的 `review_domain` 是 **`protocol_report`（方案与报告之间的差异）**，并非 `statistical_results`。当前状态仍为 **Pending Human Adjudication（待人工裁定）**；复核确认的是定义变化可以从原文复现，不代表已经认定其影响了研究结论。[C001 完整记录](../.ai_paper_validation/final_report_1_6_2.md#c001--added-diabetes-range-hba1c-primary-composite-disqualifier)

**关键原文与推理依据**

1. **原始方案：三项条件满足任一项，即为成功。**

   原方案列出：12 个月减重至少 5%；或减重至少 4%且每周平均运动至少 150 分钟；或 HbA1c 下降至少 0.2 个百分点。随后写道：

   > “defined as 1 if at least one of the CDC ‘success’ outcome measures is achieved and 0 if none are achieved.”

   即至少满足一项记为 1，否则为 0。该主要终点定义没有增加随访 HbA1c ≥6.5%即判失败的条件；“Incident type 2 diabetes (A1C ≥6.5%)”另列为次要终点。[原方案，PDF 第 15 页 §3.2–3.3](../joi250084supp1_prod_1765403089.61351.pdf#page=15)

2. **统计分析计划变更表明确记录了新增规则。**

   “Original Method”栏写道：

   > “Incident diabetes was not prespecified to be treated as grounds for primary outcome failure.”

   “Change”栏则写道：

   > “Participants who had diabetes-range A1C values (≥6.5%) at 6 or 12 months were considered not to have achieved the primary composite outcome, regardless of weight or physical activity improvements”

   这两栏直接证明了定义变化。作者也给出理由：在糖尿病预防项目中，HbA1c 进展至糖尿病范围具有临床意义。**因此，该变更已被披露；C001 本身不能据此推断存在未披露的方案偏离。**[SAP 变更表，PDF 第 86 页](../joi250084supp1_prod_1765403089.61351.pdf#page=86)

3. **正文采用了增加条件后的定义。**

   正文 Outcomes 开头写道：

   > “The primary outcome was defined as maintaining an HbA1c less than 6.5% throughout the study plus 1 or more of the following outcomes at 12 months”

   其中 **“maintaining … less than 6.5% … plus”** 表明：保持 HbA1c <6.5%是必须同时满足的条件。[正文，PDF 第 3 页](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=3)

**为什么这项变化值得记录**

仅考察 C001 这一项变更，设：

- \(B\)：满足原始三个成功分支中的至少一个；
- \(D\)：第 6 或第 12 个月出现 HbA1c ≥6.5%。

则原始规则为 \(B\)，报告规则增加为 \(B\land\neg D\)。例如，一名受试者减重 6%，但第 6 个月 HbA1c 为 6.6%，在原始规则下满足减重分支，在新增规则下则未达成主要终点。这是判定逻辑的变化，与四舍五入无关。

但**能够受该规则影响的人数，不等于已经证明改变分类的人数**。eTable 13 列出 15 名出现糖尿病范围 HbA1c 的受试者：AI 组 8 名、人工教练组 7 名。表中没有提供这些人是否满足原始成功分支的完整交叉信息，因此不能说“15 人由成功改判为失败”。表下注释还明确说明，研究团队没有裁定正式糖尿病诊断；这里应称为“糖尿病范围的 HbA1c”，不能直接等同于确诊糖尿病。[补充材料，PDF 第 56 页](../joi250084supp2_prod_1765403089.61751.pdf#page=56)

**对下游使用的实际含义**

虽然 C001 不属于 `statistical_results`，它仍关系到结果提取：论文的 **58/183 对 59/185**、风险差 **−0.2 个百分点**及单侧 95%置信下限 **−8.2 个百分点**，应与增加条件后的终点定义一起记录。[正文，PDF 第 4 页](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4)

若只提取原始三分支定义，会把这些结果对应到一个不同的结局定义，影响证据表述及研究间可比性的判断。现有材料尚不能量化该条件对两组成功率、风险差或非劣效结论的影响；还需原始定义下的结果、上述受试者的分支达成情况，以及该变更的明确采用日期。

## C002

### 用户

continue on C002

### 助手进度说明

我会继续核对 C002 的记录和对应原文，用中文说明差异、推理依据，以及现有证据能支持到什么程度。

### 助手答复

**C002 关注的是：用于判定主要终点的运动量，究竟取第 6–11 个月的平均值，还是更长随访期间的平均值。现有材料没有明确连接“运动量汇总公式”与“主要终点的达标判定”。**

其 `review_domain` 为 **`protocol_report`**，并非 `statistical_results`。尤其需要注意：C002 的纳入审计为 **`QUESTIONED`（纳入依据受到质疑）**。原文中的不同时间窗口可以复现，但尚不能证明主要终点实际采用了不同于原方案的窗口。当前仍为 **Pending Human Adjudication（待人工裁定）**。[C002 完整记录](../.ai_paper_validation/final_report_1_6_2.md#c002--primary-pa-window-and-endpoint-specific-mapping)

**关键原文**

1. **原方案明确将第 6–11 个月用于主要终点的运动分支。**

   > “At least 4% weight loss at 12 months and at least 150 minutes/week of physical activity on average (over months 6–11 measured using monthly serial Actigraphy)”

   即：12 个月减重至少 4%，并且**第 6–11 个月平均每周运动至少 150 分钟**。这里明确指定了六个月度测量期间。[原方案，PDF 第 15 页 §3.2](../joi250084supp1_prod_1765403089.61351.pdf#page=15)

2. **结果补充材料描述了覆盖更长期间的运动量汇总公式。**

   > “To obtain the average MVPA minutes per week across the study period, the total MVPA minutes per week from all valid wear periods were summed and divided by the number of available wear periods (maximum of 11 post-baseline visits).”

   随后写道：

   > “This approach provided an average estimate of weekly MVPA throughout the 12-month follow-up period.”

   这里描述的是整个随访期间的中高强度身体活动量（MVPA），最多使用 **11 次基线后测量**。eTable 8b 也列出了第 1–11 个月的运动量测量。[补充材料，PDF 第 13 页](../joi250084supp2_prod_1765403089.61751.pdf#page=13)、[第 49 页 eTable 8b](../joi250084supp2_prod_1765403089.61751.pdf#page=49)

3. **修订记录提到了时间范围澄清，但没有写出替代月份。**

   2022 年 3 月 28 日的版本 1.4 写道：

   > “Modified study endpoint to clarify time frame of measurement of physical activity”

   这说明作者披露过相关修订，但这条记录没有明确说明最终采用第几个月至第几个月。[方案修订记录，PDF 第 80–81 页](../joi250084supp1_prod_1765403089.61351.pdf#page=80)

**详细推理：差异在哪里，证据缺在哪里**

原方案的主要终点窗口是 **第 6–11 个月**；补充材料的跨随访汇总最多涵盖 **第 1–11 个月**。这两个窗口可能得到不同的运动量平均值。

但要认定主要终点发生变化，还必须证明：**补充材料的跨随访公式，确实被用来判断主要终点中的“每周至少 150 分钟”是否达标。** 现有原文没有明确提供这一连接。

因此，两种解释都与现有材料相容：

- 跨随访公式仅用于连续运动量的描述性汇总，主要终点仍单独使用第 6–11 个月；
- 修订后的主要终点采用了更长窗口，但完整的最终定义没有在所引位置写明。

这也是独立审计将 C002 标为 `QUESTIONED` 的原因：**窗口描述不同，并不足以证明同一个主要终点采用了相互冲突的规则。** `Evidence state: reproduced` 仅指这些原文描述已复现，不能理解为已确认主要终点实施发生变化。[独立审计意见](../.ai_paper_validation/review_1_6_2/quality/evidence_quality_audit.md#c002--primary-pa-window-and-endpoint-specific-mapping)

**对结果及下游使用的含义**

正文 Figure 2 报告，“减重至少 4%且每周运动至少 150 分钟”这一分支在 AI 组为 **23/183**，人工教练组为 **23/185**；风险差为 **0.1 个百分点**，单侧 95%置信下限为 **−5.5 个百分点**。这些数值本身不能说明采用了哪个时间窗口。[正文，PDF 第 7 页 Figure 2](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=7)

下游提取时，应保留“主要终点的最终运动量窗口未明确”的限定，避免直接把跨随访汇总窗口填成主要终点窗口。如果窗口实际不同，理论上可能改变部分人的运动分支达标状态；是否进一步改变复合终点，还取决于他们是否满足其他成功分支。

**现有证据不能确定有人因此改变分类，也不能量化对风险差或非劣效结论的影响。** 要解决 C002，需要明确的最终修订定义，以及实际用于主要终点判定的月份和计算说明。

## C003

### 用户

C003

### 助手进度说明

我会核对 C003 的原方案、修订记录和正文，重点确认 HbA1c 分支适用人群的变化及其解释边界。

### 助手答复

**C003 指的是：主要复合终点中“HbA1c 下降至少 0.2 个百分点”这一分支，经明确修订后，仅适用于基线 HbA1c 为 5.7%–6.4% 的受试者。论文采用了这一限制。**

其 `review_domain` 为 **`protocol_report`**，并非 `statistical_results`。证据状态为 `reproduced`，纳入审计为 `CONFIRMED`；这表示定义变更已有原文支持。当前仍为 **Pending Human Adjudication（待人工裁定）**，不能据此认定结果受到影响。[C003 完整记录](../.ai_paper_validation/final_report_1_6_2.md#c003--primary-hba1c-branch-restricted-to-baseline-subset)

**关键原文**

1. **原始终点定义没有单独写出基线范围限制。**

   原方案 §3.2 将以下条件列为主要终点的一个成功分支：

   > “At least a 0.2% reduction in hemoglobin A1C by 12 months”

   即 12 个月时 HbA1c 下降至少 **0.2 个百分点**。该条本身没有附加“仅限基线 HbA1c 5.7%–6.4%”的限定。[原方案，PDF 第 15 页](../joi250084supp1_prod_1765403089.61351.pdf#page=15)

2. **2022 年 3 月 28 日的版本 1.4 明确增加了适用人群限制。**

   修订条目跨第 80–81 页，写到：

   > “limiting A1C change measure to subset of study participants who have baseline A1C of 5.7% and 6.4%.”

   同页对 §8.2.2 的说明进一步明确为：

   > “calculate change in A1C only for the subset of study participants who have a baseline A1C in 5.7% to 6.4% range”

   同时，修订扩大了入组标准，允许依据空腹血糖或口服葡萄糖耐量试验的糖尿病前期证据入组。因此，基线 HbA1c 在正常范围的人也可能符合修订后的入组条件。[修订记录，PDF 第 80–81 页](../joi250084supp1_prod_1765403089.61351.pdf#page=80)

3. **正文明确采用修订后的范围。**

   > “The change in HbA1c endpoint was applicable only to participants with baseline HbA1c of 5.7% to 6.4%.”

   Figure 2 的脚注也重复这一限制，并注明 AI 组和人工教练组各有 **130 人**适用于该分支。[正文，PDF 第 3 页](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=3)、[第 7 页 Figure 2](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=7)

**详细推理及解释边界**

从终点文字看，修订增加了一个条件：除了 HbA1c 下降达到阈值，受试者还必须属于指定的基线范围。因此，提取这一分支时，必须同时记录**下降阈值和适用人群**。

但这里有一个重要背景：**原始入组标准本来就要求糖尿病前期范围的 HbA1c。** 随着入组标准扩大，才可能出现“符合试验入组标准，但基线 HbA1c 不在 5.7%–6.4%”的人。

因此，这项修订可能是在扩大试验入组人群的同时，保留 HbA1c 分支原有的适用范围。现有材料不能证明某位原本符合入组标准的受试者，因为这项限制而改变终点分类。C003 记录的是有日期、有说明的定义变更，不应被表述为未披露的分析变动。

**为什么分母 130 不构成计数不一致**

Figure 2 报告：

| 人群或分支 | AI 组 | 人工教练组 |
|---|---:|---:|
| 全体随机分组人数 | 183 | 185 |
| HbA1c 分支适用人数 | 130 | 130 |
| HbA1c 分支达成人数 | 35 | 35 |
| 该分支达成率 | 26.9% | 26.9% |

其中 \(35/130=26.923\%\)，与显示的 **26.9%** 一致。130 是有明确基线条件的分支人群，不能直接解释为随访完成者人数，也不能据此认为其他人被排除出整个主要分析。[正文，PDF 第 7 页](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=7)

**对下游使用的含义**

虽然 C003 不属于 `statistical_results`，它仍影响数据提取和结果解释：

- **35/130 的达成率对应指定的基线亚组**，不能改用 183 或 185 作分母后仍解释为同一结果。
- 不适用于 HbA1c 分支的人，仍可能通过减重或减重加运动分支达成主要复合终点。
- 比较其他研究时，需要保留这一基线限制，才能判断结局定义是否可比。

现有证据支持“分支定义经过明确修订，报告与修订一致”，但尚不能量化该修订对整体成功人数、风险差或非劣效结论的影响。

## C004

### 用户

C004

### 助手进度说明

我会核对 C004 中原方案的排除规则、报告采用的缺失结局处理，以及相关人数，说明这些变化对主要分析的含义。

### 助手答复

**C004 指的是：主要分析从原方案的“排除退出者或缺少 12 个月数据者”，改为“纳入全部随机分组者，并将缺少 12 个月结局者判为未达成主要终点”。** 变化涉及分析人群和缺失结局处理规则；报告中的人数能够相互核对。

其 `review_domain` 为 **`protocol_report`**，并非 `statistical_results`。证据状态为 `reproduced`，纳入审计为 `CONFIRMED`，当前仍为 **Pending Human Adjudication（待人工裁定）**。[C004 完整记录](../.ai_paper_validation/final_report_1_6_2.md#c004--primary-exclusions-replaced-by-all-randomized-failure-assignment)

**关键原文**

1. **原方案虽然使用 ITT 表述，但明确附加了排除条款。**

   §9.3 先说明按初始随机分组分析，不论是否遵循干预，随后写道：

   > “Analyses of effectiveness endpoints, however, will exclude participants who withdraw from the study or withdraw consent.”

   即有效性终点分析将排除退出研究或撤回同意的受试者。因此，不能仅凭“ITT”这个名称，认定原方案已经规定所有随机分组者均保留在分析中。[原方案，PDF 第 37 页 §9.3](../joi250084supp1_prod_1765403089.61351.pdf#page=37)

2. **SAP 变更表直接列出了原规则与新规则。**

   “Original Method”栏：

   > “Primary analysis on population excluding those who withdrew or lacked 12-month data”

   “Change”栏：

   > “Included all randomized participants in ITT and classified those with missing 12-month data as treatment failures in the primary analysis.”

   作者给出的理由是提供保守的有效性估计，并通过避免随机分组后的排除来保持随机化的完整性。**这项变更已经披露，但所引变更表没有给出明确的采用日期。**[SAP 变更表，PDF 第 86 页](../joi250084supp1_prod_1765403089.61351.pdf#page=86)

3. **正文采用了新规则。**

   > “The primary analysis was conducted using an intention-to-treat approach in all randomized participants.”

   > “Those who did not attend the 12-month study visit were classified as not achieving the primary composite outcome.”

   即所有随机分组者进入主要分析，未参加 12 个月访视者被判为主要终点未达成。[正文，PDF 第 4 页](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4)

**详细推理：排除与判失败有什么区别**

两种规则对没有结局数据的受试者采取了不同操作：

- **排除：**不进入该项分析的分母。
- **保留并判失败：**进入分母，但不计入成功人数。

因此，这不是单纯的术语变化。即使观测到的成功人数相同，分母处理不同也可能改变成功率、组间风险差及其置信区间。

同时，“因缺失而判定未达成”是一项分析规则，**不等于实际观测到了该受试者未达成终点**。补充材料 eTable 8c 明确说明，主要分析假定这些人未达成终点，敏感性分析则采用链式方程多重插补。[补充材料，PDF 第 50 页](../joi250084supp2_prod_1765403089.61751.pdf#page=50)

**人数核对及不能越过的解释边界**

| 项目 | AI 组 | 人工教练组 | 合计 |
|---|---:|---:|---:|
| 随机分组并进入主要分析 | 183 | 185 | 368 |
| 未参加 12 个月访视 | 26 | 29 | 55 |
| 完成 12 个月访视并有完整结局 | 157 | 156 | 313 |
| 未访视者中，退出研究 | 19 | 19 | 38 |
| 未访视者中，失去联系 | 7 | 10 | 17 |

这些数字满足 **313＋55＝368**，以及 **38＋17＝55**。[正文，PDF 第 5 页 Figure 1](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=5)

需要区分：**55 名未访视者不等于 55 名退出研究者；退出研究也不能自动等同于撤回同意。** 因此，不能直接断言原方案的分析分母就是 313，也不能把成功人数除以 157、156 后称为“原方案结果”。现有材料没有提供足以完整重建原方案分析人群及结果的信息。

**对下游使用的含义**

虽然 C004 不属于 `statistical_results`，它直接影响结果提取：报告的 **58/183 对 59/185**，以及风险差 **−0.2 个百分点**、单侧 95%置信下限 **−8.2 个百分点**，对应的是“全部随机分组者纳入、缺失结局判未达成”的主要分析。不能给这些数值附上“排除缺失者后的分析”这一描述。[正文，PDF 第 4 页](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4)

两组缺失比例分别为 **14.2% 和 15.7%**，因此该规则对组间比较的作用不能仅凭“双方都判失败”来判断。作者称其为保守处理，但 **C004 本身没有证明它必然使非劣效判断更保守，也没有证明结论发生变化**。量化影响仍需明确的原方案分析人群、对应结果，以及这项修订的采用时间。

## C005

### 用户

C005

### 助手进度说明

我会核对 C005 的原定模型、正文采用的模型及聚类敏感性分析，说明模型变更的依据和已知影响。

### 助手答复

**C005 指的是：原方案计划采用考虑项目内聚类的混合效应 Logistic 回归，报告的主要分析则改用直接估计风险差（RD）的未调整二项回归。聚类处理出现在另列的事后敏感性分析中。**

其 `review_domain` 为 **`protocol_report`**，并非 `statistical_results`。证据状态为 `reproduced`，纳入审计为 `CONFIRMED`；当前仍为 **Pending Human Adjudication（待人工裁定）**。这项候选记录的是已披露的主要模型变更，不代表已经认定某个模型不适用。[C005 完整记录](../.ai_paper_validation/final_report_1_6_2.md#c005--clustered-logistic-primary-model-replaced-by-binomial-rd-regression)

**关键原文**

1. **原方案要求混合效应 Logistic 回归，并说明聚类目的。**

   > “Between-group differences in primary and secondary outcomes will be evaluated in intention-to-treat analyses using mixed effects logistic regression models to account for potential within-program site clustering.”

   即使用混合效应 Logistic 回归，考虑同一干预项目地点内受试者之间可能存在的相关性。这里的聚类指 DPP 项目地点，不应直接等同于两个招募研究中心。[原方案，PDF 第 37 页 §9.4.1](../joi250084supp1_prod_1765403089.61351.pdf#page=37)

2. **SAP 变更表明确记录了模型替换。**

   > “We used a binomial regression (unadjusted) rather than logistic regression to estimate risk difference between study groups in our primary analysis”

   作者给出的理由是：二项回归可以直接估计两组风险差。因此，这项变化已有披露；但材料没有给出该模型变更的明确采用日期。[SAP 变更表，PDF 第 86 页](../joi250084supp1_prod_1765403089.61351.pdf#page=86)

3. **正文将主要分析和聚类敏感性分析分别列出。**

   主要分析写道：

   > “The risk difference was estimated using binomial regression.”

   随后在五项事后敏感性分析中列出：

   > “analyses using cluster-robust standard errors to account for potential intragroup correlation due to shared program exposure.”

   因此，报告确实考虑过聚类，但其位置是**事后敏感性分析**。[正文，PDF 第 4 页](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4)

**详细推理：为什么敏感性分析不能直接视为执行了原模型**

这项比较包含两个层面：

- **模型规格变化：**原定混合效应 Logistic 回归，改为报告的未调整二项回归，直接估计 RD。
- **聚类处理位置变化：**原方案在主要模型中考虑项目内聚类；报告另外提供采用聚类稳健标准误的敏感性分析。

混合效应模型与聚类稳健标准误属于不同的处理方式。即使都涉及组内相关性，后者的结果也不能直接当作原定混合效应模型的结果。

另一个需要澄清的地方是：**“未调整”本身不是这里新增的差异。** 原方案也写明主要分析不作协变量调整，另列协变量敏感性分析。C005 的核心是模型及聚类处理的变更。[原方案，PDF 第 38 页 §9.4.5](../joi250084supp1_prod_1765403089.61351.pdf#page=38)

**报告中的数值是否相互冲突**

| 分析 | 风险差，百分点 | 单侧 95%置信下限，百分点 |
|---|---:|---:|
| 主要分析：二项回归 | −0.2 | −8.2 |
| 敏感性分析：按 DPP 项目地点聚类 | −0.20 | −4.8 |
| 敏感性分析：按项目地点及随机分组月份聚类 | −0.20 | −6.8 |

两项敏感性分析均使用 **58/183 对 59/185** 的成功人数。第一项将四个人工 DPP 分别作为四个聚类，全部 AI 组作为第五个聚类；第二项进一步结合随机分组月份。[补充材料，PDF 第 31 页方法说明](../joi250084supp2_prod_1765403089.61751.pdf#page=31)、[第 62 页 eTables 19a–b](../joi250084supp2_prod_1765403089.61751.pdf#page=62)

**这些不同的置信下限不构成同一结果的数值冲突**，因为它们对应不同的分析。−0.2 与 −0.20 也只是显示精度不同。三项已报告分析的下限均高于 −15 个百分点，但这并不能确定原定混合效应模型会得到什么结果。

**对下游使用的含义**

虽然 C005 不属于 `statistical_results`，它会影响方法编码和证据提取：

- 主要结果应记录为**未调整二项回归估计的 RD**，不能标成混合效应 Logistic 模型结果。
- −8.2 应保留为主要分析的置信下限；−4.8 和 −6.8 应与各自的聚类敏感性分析对应。
- 不能把聚类敏感性结果描述为“原方案模型已经复现”。

现有材料没有提供原定混合效应模型的输出，因此**无法量化模型替换对估计值、置信区间或非劣效判断的影响**。仍待明确的是模型修订的采用时间，以及原定模型的结果是否可获得。

## C006

### 用户

C006

### 助手进度说明

我会核对 C006 中运动量缺失数据的原定处理、报告采用的赋零规则及敏感性分析，重点区分月度运动数据缺失与 12 个月结局缺失。

### 助手答复

**C006 指的是：原方案针对月度运动量缺失，计划在缺失比例超过 5%时采用多重插补，并进行运动数据完全者分析；报告则采用缺失期间运动量赋零，并提供了不同的运动达标假设敏感性分析。**

其 `review_domain` 为 **`protocol_report`**，并非 `statistical_results`。证据状态为 `reproduced`，纳入审计为 `CONFIRMED`；当前仍为 **Pending Human Adjudication（待人工裁定）**。[C006 完整记录](../.ai_paper_validation/final_report_1_6_2.md#c006--primary-pa-missing-data-procedure-and-linked-sensitivity-replaced)

**关键原文**

1. **原方案：超过 5%的运动数据缺失时，主要分析采用多重插补。**

   §9.4.2 在讨论月度 ActiGraph 运动量数据后写道：

   > “If more than 5% of data for this outcome variable is missing, the primary analysis will be based on multiple imputation.”

   随后规定：

   > “A sensitivity analysis will also be done using a complete case analysis (i.e. participants with 100% of PA data)”

   即另做敏感性分析，仅纳入运动数据完整的受试者；如结果明显不同，则结合敏感性分析解释主要结果。[原方案，PDF 第 38 页 §9.4.2](../joi250084supp1_prod_1765403089.61351.pdf#page=38)

2. **SAP 变更表明确将多重插补替换为赋零。**

   > “Instead of imputation, a worst-case assumption was applied: participants with missing actigraphy data during a given interval were assumed to have completed 0 minutes of physical activity during that period.”

   作者说明，这样处理是为了避免高估运动量，并认为反复提醒后仍未佩戴设备可能反映较低参与度或较少运动。**这项变更已有披露，但材料没有提供明确的采用日期。**[SAP 变更表，PDF 第 86 页](../joi250084supp1_prod_1765403089.61351.pdf#page=86)

3. **报告确实采用了月度运动量赋零。**

   eTable 8b 的说明写道：

   > “If no valid wear data were recorded despite this outreach, MVPA was imputed as zero for that month to avoid overestimating physical activity.”

   即没有有效佩戴数据的月份，其中高强度运动量按零处理。[补充材料，PDF 第 49 页 eTable 8b](../joi250084supp2_prod_1765403089.61751.pdf#page=49)

**详细推理：为什么报告中的多重插补不能直接对应原计划**

这里必须区分两种缺失：

| 缺失对象 | 原方案或报告中的处理 |
|---|---|
| 随访期间某些月份的运动量缺失 | 原方案计划在超过阈值时多重插补；报告改为赋零 |
| 12 个月访视结局缺失 | 报告主要分析判为未达成，另用多重插补做敏感性分析 |

报告虽然出现了多重插补，但其方法描述明确写的是：

> “missing 12-month outcome data were addressed using multiple imputation by chained equations”

也就是补充**缺失的 12 个月结局**，并生成 20 个插补数据集后合并。[补充材料，PDF 第 30 页](../joi250084supp2_prod_1765403089.61751.pdf#page=30)

因此，不能因为报告使用了 MICE，就认定原定的“月度运动量多重插补”已经执行。两者补充的对象不同。这也区别于 C004：C004 关注缺失最终结局者是否进入分析及如何判定；C006 关注月度运动数据如何进入运动达标计算。

**敏感性分析也发生了对应变化**

原计划的 complete-case 分析，是**选择运动数据 100%完整的人群**。报告的两项运动敏感性分析则是：

- 对未达到设备佩戴要求者，假定其每周运动达到 150 分钟；
- 对所有受试者，假定其每周运动达到 150 分钟。

它们改变的是运动达标假设，而非筛选运动数据完全者，因此不能视为原定 complete-case 分析。[补充材料，PDF 第 61 页 eTables 18a–b](../joi250084supp2_prod_1765403089.61751.pdf#page=61)

月度运动缺失比例显示为 **9.3%–35.1%**，说明该处理涉及实际存在的缺失。不过，材料没有明确原方案“超过 5%”所用的总体计算口径，不能把各月比例相加后当作该触发比例。C006 的依据主要是变更表明确写出的替换，而非自行重建阈值。[eTable 8b](../joi250084supp2_prod_1765403089.61751.pdf#page=49)

**对结果及下游使用的含义**

月度赋零可能影响平均运动量及“减重至少 4%且每周运动至少 150 分钟”分支的判定；是否进一步影响复合终点，还取决于受试者是否通过其他分支达标。赋零是一项分析假设，不能解释为实际观测到该期间完全没有运动。

已报告的两项运动敏感性分析均得到 **58/183 对 60/185**，风险差 **−0.74 个百分点**，单侧 95%置信下限 **−8.8 个百分点**。这描述了所列替代假设下的结果，**不能替代原定月度多重插补或运动数据完全者分析的结果**。[eTables 18a–b](../joi250084supp2_prod_1765403089.61751.pdf#page=61)

下游提取应分别记录“月度运动量赋零”“最终结局 MICE”及“运动达标假设敏感性分析”。现有材料不能量化原定方法会改变多少人的分类、风险差或非劣效判断；仍缺少原定分析输出、明确的缺失阈值口径及修订采用时间。

## C007

### 用户

c007

### 助手进度说明

我会核对 C007 中原定“项目完成者”分析与报告采用的人群定义，确认两者的纳入条件、人数及解释边界。

### 助手答复

**C007 指的是：原方案计划在“完成干预项目的人群”中进行符合方案分析，报告则改为分析“有完整 12 个月结局、且未开始使用禁用药物的人群”。这两个人群的纳入条件和人数均不同。**

其 `review_domain` 为 **`protocol_report`**，并非 `statistical_results`。证据状态为 `reproduced`，纳入审计为 `CONFIRMED`；当前仍为 **Pending Human Adjudication（待人工裁定）**。[C007 完整记录](../.ai_paper_validation/final_report_1_6_2.md#c007--program-completer-analysis-replaced-by-complete-datano-medication-cohort)

**关键原文**

1. **原方案的符合方案分析，以“项目完成者”为人群。**

   §9.3 写道：

   > “A per-protocol analysis will also be conducted using the population of program completers in each group, as defined in Section 3.3, to benchmark outcomes against CDC standards.”

   §3.3 对项目完成者另有参与度要求：

   - 人工教练组：前 6 个月参加至少 8 次课程，且从所在队列首次课程到本人最后一次出席至少跨越 9 个月。
   - AI 组：前 6 个月至少有 8 周达到参与标准，且从安装应用到最后参与至少跨越 9 个月。

   所以，**“项目完成”指达到干预参与标准，并不等于完成研究的 12 个月访视。**[原方案，PDF 第 37 页 §9.3](../joi250084supp1_prod_1765403089.61351.pdf#page=37)、[第 16 页完成标准](../joi250084supp1_prod_1765403089.61351.pdf#page=16)

2. **SAP 变更表明确替换了人群定义。**

   修订后写道：

   > “We adjusted our per protocol population to be those with available 12 month outcomes data who did not initiate prohibited medications.”

   新条件是有 12 个月结局数据，并且未开始使用禁用药物；这条定义没有要求达到上述课程或应用参与标准。[SAP 变更表，PDF 第 86–87 页](../joi250084supp1_prod_1765403089.61351.pdf#page=86)

3. **正文采用了修订后的限制分析。**

   > “A restricted analysis was conducted in participants with 12-month outcome data who did not initiate prohibited medications during the trial.”

   补充材料的人群定义也采用相同条件，并列出禁用药物类别，包括类固醇、降糖药和减重药。[正文，PDF 第 4 页](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4)、[补充材料，PDF 第 27 页](../joi250084supp2_prod_1765403089.61751.pdf#page=27)

**详细推理：为什么这不只是名称不同**

原方案按**干预参与情况**选人；修订后按**结局数据是否完整及药物使用情况**选人。因此，一个人可能没有达到项目完成标准，但仍符合修订后分析的条件；项目完成者也不一定同时满足完整结局、未使用禁用药物这两个条件。

报告中的人数进一步说明，两者不能视为同一个集合：

| 人群及结果 | AI 组 | 人工教练组 | 总人数 |
|---|---:|---:|---:|
| 项目完成者：达成人数／人数 | 43/117 | 33/93 | 210 |
| 完整结局且未开始禁用药物者：达成人数／人数 | 54/151 | 53/149 | 300 |

项目完成者人数来自 Figure 4；限制分析人数来自 eTable 15。后者也满足 **313 名完整结局者－13 名开始禁用药物者＝300 人**。300 人与 210 人显然不能是同一人群，但材料没有提供两组人群逐人的重叠情况。[正文，PDF 第 9 页 Figure 4](../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=9)、[补充材料，PDF 第 58 页 eTable 15](../joi250084supp2_prod_1765403089.61751.pdf#page=58)

**报告是否完全没有项目完成者结果？**

报告提供了 **43/117 和 33/93** 这些描述性结果。但在所核对的位置，没有找到原计划针对项目完成者的推断模型及相应区间。描述性人数不能直接替代那项计划分析。

实际给出风险差及区间的是 300 人的限制分析：

- AI 组：**54/151＝35.8%**
- 人工教练组：**53/149＝35.6%**
- 风险差：**0.2 个百分点**
- 单侧 95%置信下限：**−8.9 个百分点**

这些比例与人数相符；C007 关注的是它们对应的人群发生了变化。[eTable 15](../joi250084supp2_prod_1765403089.61751.pdf#page=58)

**对下游使用的含义**

提取 **0.2（下限 −8.9）个百分点**时，应记录其人群为“完整结局且未开始禁用药物者”，不能将其描述为“完成干预项目者中的比较”。

作者也明确限定该分析的解释：

> “It does not estimate the causal effect of adherence to a specific treatment strategy.”

因此，不能把这项支持性分析解读为“完全依从干预后的因果效果”，也不能用它代替原计划项目完成者分析的结论。[eTable 15 注释](../joi250084supp2_prod_1765403089.61751.pdf#page=58)

现有证据支持人群定义已被明确替换，且正文与修订后的定义一致；**尚不能量化这一替换对原计划分析结论的影响**。仍待明确的是修订采用时间、两个人群的重叠情况，以及原定项目完成者推断分析的结果是否可获得。

## 保存请求

### 用户

save the conversation into a md file and put it inside ./review_records/

### 助手进度说明

我会将目前关于 C001–C007 的问答按顺序保存为 Markdown，放入 `./review_records/`。

C001–C003 已保存。我会继续写入 C004–C007 的完整答复，并检查记录中的本地证据链接。
