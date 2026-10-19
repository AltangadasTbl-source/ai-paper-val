# Conversation record: C001–C003

Recorded UTC: 2026-10-19 06:03:58

Scope: User-facing discussion of C001, C002 and C003, including user requests, assistant progress messages and assistant answers through the request to save this record. Project setup instructions, system/developer instructions, tool calls and tool outputs are excluded. The original languages and source links are preserved. This record does not change the existing review artifacts or candidate classifications.

---

## User — Initial request

Tell me in CN, what happened to C001? if it were stat_results, does it affect downstream meta analysis (if not, skip this). Make sure you first scan the original document and the proceeded files inside the ./ai_paper_validation/* then give answer

## Assistant — Progress

我会先检查原始文档和审查文件，追踪 C001 的证据、分类及后续状态，再用中文说明。

## Assistant — Progress

审查记录显示，C001 一直保留为 `statistical_results`，复核确认的是 PROMIS-29 单一分数的计算方式和方向未说明，状态仍为待人工裁定。我正在对照原文页面，确认它具体影响哪项结果的提取。

## Assistant — Answer

我已核对原文对应页面影像（正文第3、6页，结果补充材料第15页、方案第70页），并查看 `.ai_paper_validation/` 中的候选台账、筛选、复核、审计及最终报告。

**C001 被保留为 `statistical_results`，目前仍是“待人工裁定”。** 它关注的是：**PROMIS-29 报告的单一分数如何计算、分数高低代表什么，没有说明清楚。**

- 正文描述7个领域，每个领域原始分数为4–20，且不同领域的评分方向不同。
- 结果却只报告一个 PROMIS-29 分数，以及调整后均值差 **−0.37（95% CI −3.34～2.61）**。补充表也给出相同效应，但未说明选用了哪些领域、如何汇总或转换、是否反向计分。[正文定义](/home/juliz/ai-paper-val/2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3)；[补充表](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=15)

它由 `F-ST1-007` 经独立筛选后登记，证据复核为 `reproduced`，审计确认符合纳入条件。**这不代表已经判定数值有问题**；复核特别指出，不能直接拿单领域上限20与报告均值约65比较，认定分数越界。[复核记录](/home/juliz/ai-paper-val/2025/jama.2025.15185/.ai_paper_validation/review_1_6_2/verification/evidence_recheck.md:35)

**对下游 Meta 分析有潜在影响，范围是这个 PROMIS-29 结局。** 合并均值差时，无法确认它与其他研究是否采用相同评分；判断获益方向时，也无法确定负值代表改善还是恶化。换成标准化均值差（SMD）仍不能解决“具体测量什么、方向如何”的不明确。因此，在评分规则澄清前，这项结果的合并依据不足。

现有材料没有显示它已改变某项 Meta 分析结果，也没有显示 C001 影响主要 FMA 结局。

---

## User — Request for details

you need to show the details and original key sentences, and the reasoning.

## Assistant — Progress

我会补上原文关键句、对应数值，以及从这些证据到 C001 和 Meta 分析影响的逐步推理，并区分原文事实与推断。

## Assistant — Answer

**C001 的核心是：论文给出一个 PROMIS-29 效应值，却没有把这个单一分数的构成、单位和评分方向说明清楚。** 现有记录将它保留为 `statistical_results`，证据状态为 `reproduced`，但仍然**待人工裁定**。

下面结合原文和处理文件说明。

**1．原文定义了多个领域，而且这些领域的评分方向不同**

正文 PDF 第3页，Secondary Outcomes 中写道：

> “PROMIS-29; 7 domains with 4 items each; raw score range, 4-20 points per domain, with higher scores reflecting better functioning in some domains and worse in others”

意思是：7个领域，每个领域4个条目，每个领域的原始分数范围为4–20；某些领域高分表示功能较好，另一些则表示较差。[原文第3页](/home/juliz/ai-paper-val/2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3)

这段说明让读者知道**各领域分别如何计分**，但没有说明如何得到后面报告的那个单一分数，例如：

- 使用某一个领域，还是多个领域？
- 如果合并，是否求和、加权或转换？
- 不同方向的领域是否经过反向计分？
- 最终分数越高，究竟表示越好还是越差？

**2．结果只给出一个分数和一个调整后效应**

正文 PDF 第6页写道：

> “At 3 months, the mean (SD) PROMIS-29 score was 66 (14) points in the levodopa group and 65 (14) points in the placebo group, with an adjusted mean difference of −0.37 points (95% CI, −3.34 to 2.61).”

也就是：3个月时，左旋多巴组均值66、安慰剂组65，调整后均值差为 **−0.37分，95% CI −3.34至2.61**。[原文第6页](/home/juliz/ai-paper-val/2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6)

结果补充材料第15页，eTable 4 对应行提供：

| 项目 | 报告数值 |
|---|---:|
| 安慰剂组，均值（SD） | 65.11（13.79） |
| 左旋多巴组，均值（SD） | 64.74（14.33） |
| 报告的调整后效应及区间 | −0.37［−3.34，2.61］ |
| 分析人数 | 582 |

补充表重复了同一个单一结局及效应，**没有补充其评分公式**。[原始补充表第15页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=15)

方案第70页还写道：

> “The mean of each scale is 50, reflecting the mean of the general population, and the standard deviation is 10.”

这提供了标准化量表的背景，但没有明确把报告的约65分对应到某一个领域或某一种汇总方式，因此仍不能确定这里实际分析了哪个变量。[方案第70页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp1_prod_1761597796.4601.pdf#page=70)

**3．为什么这些证据支持 C001？**

推理分三步：

1. **原文起点是多个不同方向的领域分数。** 因此，仅凭“PROMIS-29”这个名称，无法唯一确定一个单一数值。
2. **报告终点却是一个单一均值和一个回归效应。** 要从多个领域得到这个结局，必须存在选取、汇总、转换或反向计分等规则。
3. **提供的材料没有把这一步连接起来。** 所以可以抄录“−0.37”，却不能确定“降低0.37分”对应什么健康变化。

这也是它被归入 `statistical_results` 的依据：涉及**产生已报告数值的评分方法及其解释**；比较发生在正文自身，所以关系类型为 `S_W`。

这里需要明确两个边界：

- **不能因为65超过单领域上限20，就认定分数越界。** 例如，假设将7个领域原始分数相加，理论范围就是28–140，65完全可能出现；但这只是说明某种汇总“可能”，并不证明作者采用了它。
- **这不是置信区间与显著性的冲突。** −0.37位于区间内，区间跨越0。C001 关注的是这个效应的测量含义没有确定下来。

**4．处理文件中，C001 经历了什么？**

| 阶段 | 记录 |
|---|---|
| 首次发现 | 统计检查提出 `F-ST1-007` |
| 独立筛选 | `INCLUDE`，按 Route B 纳入 |
| 登记 | 编为 `C001`，归入 `statistical_results / S_W` |
| 证据复核 | `reproduced`，确认的是“领域定义到单一分数的连接缺失” |
| 第二轮统计检查及审计 | 保留；审计为 `CONFIRMED` |
| 最终状态 | `Pending Human Adjudication` |

**复核还收紧了早期论证：明确不把“66与20比较”的计算作为纳入依据。** 最终保留的是评分定义不完整这一点，而不是越界主张。[复核记录](/home/juliz/ai-paper-val/2025/jama.2025.15185/.ai_paper_validation/review_1_6_2/verification/evidence_recheck.md:35)；[审计记录](/home/juliz/ai-paper-val/2025/jama.2025.15185/.ai_paper_validation/review_1_6_2/quality/evidence_quality_audit.md:241)

`CONFIRMED` 在这里表示审计确认其**符合候选纳入条件**，不是人工最终裁定。

**5．它怎样影响下游 Meta 分析？**

以下是根据上述缺失作出的推断，**不是材料已经证明发生的传播后果**。

- **合并均值差（MD）：** 必须确认其他研究使用相同的评分定义和单位。一个未明确构成的总分，不能仅因为也叫 PROMIS-29，就与某个领域分数直接合并。
- **统一获益方向：** 无法确定高分好还是低分好，就无法确定是否需要翻转效应符号。例如，若需要反向统一，−0.37［−3.34，2.61］会变为＋0.37［−2.61，3.34］。这是方向转换示例，并非建议修改本文结果。
- **采用标准化均值差（SMD）：** 标准化可以消除单位差异，但不能确定一个未知的汇总分究竟测量哪个构念，也不能自动解决评分方向问题。

因此，**C001 会限制这项 PROMIS-29 结果在 Meta 分析中的可比性和方向编码；是否改变合并结果、改变多少，目前无法确定。** 需要先澄清具体评分变量、汇总或转换规则及高低分含义。现有材料也没有显示 C001 影响主要 FMA 结局。

---

## User — C002

C002

## Assistant — Progress

我会按同样方式核对 C002 的原文、审查记录和关键数值，说明其推理及对 Meta 分析的潜在影响。

## Assistant — Answer

**C002 关注的是主要分析人群的规定发生了变化：方案把主要分析安排在“所有随机化患者”的全集中，后续 SAP 和论文则明确排除3个月前死亡者，主要分析人数为582。** 它被归为 **`protocol_report`**，目前仍是**待人工裁定**。

我已对照原始 PDF 的对应页面影像，并查看候选台账、证据复核、审计及最终报告。

**1．原方案如何规定？**

方案 PDF 第86页，§11.4.1 写道：

> “The full analysis set (FAS) consists of all patients who were randomized.”

即：**全分析集 FAS 包括所有随机化患者。**

同页最后又写道：

> “All analyses except analysis (c and d) will be performed on the full analysis set.”

即：除指定的两项敏感性分析外，所有分析均在 FAS 上进行；其中包括 §11.4.2 的主要分析。[方案第86页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp1_prod_1761597796.4601.pdf#page=86)

第87页，§11.5 还规定：

> “Missing data will be addressed using multiple imputation techniques by chained equations according to Van Buuren et al. (2011).”

这里规定使用链式方程多重插补处理缺失数据，**但没有明确规定死亡后的 FMA 应如何处理**。[方案第87页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp1_prod_1761597796.4601.pdf#page=87)

因此，原方案的明确内容是“全随机化 FAS 承担主要分析”，但不能进一步断言它要求给死亡者插补某个特定分数。

**2．后续 SAP 如何规定？**

SAP 第4页保留了 FAS 包括所有随机化患者的定义，同时写道：

> “Patients who died before Visit 3 will not be imputed except for the analysis Treatment policy strategy III.”

页脚进一步明确：

> “Patients who died before Visit 3 are part of the FAS but will not contribute to any analysis but the Treatment policy strategy III and the Composite strategy.”

意思是：**死亡者在名义上仍属于 FAS，但只参与指定的两类分析，不参与主要分析。**[SAP 第4页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp2_prod_1761597796.4701.pdf#page=4)

SAP 第6页又说明：

> “The primary analysis will be the treatment policy strategy. The other estimands help to better understand the data and should be interpreted as supportive analyses only.”

所以，包含死亡者的 strategy III 和 composite strategy 是**支持性分析**，并没有被指定为主要分析。[SAP 第6页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp2_prod_1761597796.4701.pdf#page=6)

**关键区别在于：两份文件都用了 FAS 这个名称，但实际对主要估计有贡献的患者不同。**

**3．论文实际执行了什么？**

正文 PDF 第4页直接写道：

> “Participants who died before the 3-month assessment were excluded from this analysis (full analysis set).”

紧接着：

> “For survivors with missing or incomplete FMA scores at 3 months, multiple imputations with chained equations were applied.”

即：**死亡者从主要分析中排除；存活者的缺失或不完整 FMA 才进行插补。**[正文第4页](/home/juliz/ai-paper-val/2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4)

正文第5页的流程图给出了完整人数：

| 人群 | 左旋多巴组 | 安慰剂组 | 合计 |
|---|---:|---:|---:|
| 随机化 | 307 | 303 | 610 |
| 3个月前死亡 | 11 | 17 | 28 |
| 主要分析 | 296 | 286 | 582 |
| 其中完整病例 | 282 | 269 | 551 |
| 其中采用插补 | 14 | 17 | 31 |

人数全部能够对上：

\[
610-(11+17)=582,\qquad 551+31=582.
\]

所以，**C002 没有指出人数加总不一致，也没有把主要分析理解成完整病例分析**；它是“存活者＋存活者缺失数据插补”的分析。[正文第5页](/home/juliz/ai-paper-val/2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5)

**4．包含死亡者的结果是否报告了？**

报告了。结果补充材料第13页列出：

| 分析 | 死亡者处理 | 人数 | FMA 均值差［95% CI］ |
|---|---|---:|---|
| Estimand 1：主要分析 | 排除死亡者 | 582 | −0.90［−3.78，1.98］ |
| Estimand 3：支持性分析 | 包括死亡者并插补 FMA | 610 | −0.98［−3.77，1.81］ |

第二项原文明确写着：

> “FMAs of participants who died were imputed.”

因此，不能把 C002 描述成“没有报告包含死亡者的分析”。**实际差别是，包含死亡者的分析被放在支持性位置，主要结果仍来自582名存活者。**[补充表第13页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=13)

**5．为什么登记 C002？又有哪些解释边界？**

登记推理是：

1. 原方案定义 FAS 为全部随机化患者，并将主要分析安排在 FAS。
2. 后续 SAP 和报告明确规定，死亡者不参与主要估计。
3. 包含死亡者的分析虽然存在，但属于支持性分析。
4. 因而，原方案与最终主要分析的**参与规则及主要／支持性地位**存在可直接核对的差异；按本工作流 Route A 第5类登记。

**不过，这些证据不足以认定该变化未经预先安排。** 原方案本身已说明，详细方法会写入数据库关闭前定稿的 SAP。正文第5页也写道：

> “Prespecified analyses were performed as outlined in the statistical analysis plan, which was finalized before database closure.”

这支持另一种解释：**后续 SAP 可能是在前瞻性地澄清死亡这一特殊事件的处理，而不是事后改变分析。** 原方案没有清楚规定死亡处理，提供的材料也未完全说明这次澄清或替换的决策历史。[正文第5页](/home/juliz/ai-paper-val/2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5)

数值上，上述两项估计相差 **0.08分**，两个区间均跨越0；这些结果没有显示纳入死亡者后结论发生反转。但这不能消除主要分析人群规定不同这一事实，也不能证明支持性插补结果就是原方案原本意图的分析。

**6．审查记录最后如何处理？**

`F-XS-102` 和 `F-ST1-002` 被合并登记为 C002；独立筛选纳入，证据复核为 `reproduced`，审计为 `CONFIRMED`。分类保留为：

- **领域：** `protocol_report`
- **主要关系：** `P_R`，方案与报告的比较
- **全部关系：** `P_R, P_P`，也包括原方案与 SAP 的比较
- **状态：** `Pending Human Adjudication`

这里的审计确认是确认**符合候选纳入条件**。最终需要人工回答的是：**“存活者主要分析”究竟是对原方案的前瞻性澄清，还是正式替换；原方案原本打算怎样处理死亡？**[完整复核记录](/home/juliz/ai-paper-val/2025/jama.2025.15185/.ai_paper_validation/review_1_6_2/verification/evidence_recheck.md:64)

---

## User — C002 (repeated request)

C002

## Assistant — Answer

**C002 是“原方案与最终主要分析人群的差异”，分类为 `protocol_report`。关键是死亡患者是否参与主要分析，而人数本身能够核对一致。**

我已核对原文页面影像，以及 `.ai_paper_validation/` 中的台账、复核和审计记录。

**① 原方案：主要分析使用包含所有随机化患者的 FAS**

方案第86页写道：

> “The full analysis set (FAS) consists of all patients who were randomized.”

同页又规定：

> “All analyses except analysis (c and d) will be performed on the full analysis set.”

两句结合，表示主要分析安排在**全随机化人群**中。[原方案第86页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp1_prod_1761597796.4601.pdf#page=86)

但需要保留一个边界：**原方案没有明确规定死亡后的 FMA 如何处理。** 不能由“所有随机化患者”直接推导出死亡者必须赋0分，或必须按某种方式插补。

**② 后续 SAP：死亡者仍属于 FAS，但不参与主要估计**

SAP 第4页脚注明确写道：

> “Patients who died before Visit 3 are part of the FAS but will not contribute to any analysis but the Treatment policy strategy III and the Composite strategy.”

即：死亡者虽然名义上仍在 FAS 中，但只参与 strategy III 和 composite strategy。SAP 第6页将这些其他 estimands 定为支持性分析。[SAP 第4页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp2_prod_1761597796.4701.pdf#page=4)；[第6页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp2_prod_1761597796.4701.pdf#page=6)

所以，**名称都叫 FAS，不代表对主要结果有贡献的患者相同。**

**③ 论文：明确排除死亡者，主要分析582人**

正文第4页写道：

> “Participants who died before the 3-month assessment were excluded from this analysis (full analysis set).”

随后说明，仅对存活者的缺失或不完整 FMA 进行多重插补。[正文第4页](/home/juliz/ai-paper-val/2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4)

人数为：

\[
610\text{名随机化患者}-28\text{名死亡者}=582\text{名主要分析患者}.
\]

| 分析 | 人数 | FMA 均值差［95% CI］ |
|---|---:|---|
| 主要分析：排除死亡者 | 582 | −0.90［−3.78，1.98］ |
| 支持性分析：包括死亡者并插补 | 610 | −0.98［−3.77，1.81］ |

**包含死亡者的分析已经报告，只是它不是主要分析。** 两个估计相差0.08分，区间均跨越0，现有结果未显示结论反转。[补充表第13页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=13)

**④ 为什么保留 C002，又为什么仍需人工裁定？**

保留的推理是：**原方案规定全随机化 FAS 承担主要分析；最终主要估计排除死亡者；死亡者被纳入的结果则处于支持性位置。** 工作流将这一主要分析参与规则的差异按 Route A 第5类登记。

但论文同时写道：

> “Prespecified analyses were performed as outlined in the statistical analysis plan, which was finalized before database closure.”

而且原方案本身就把详细方法交给后续 SAP。因此，**这些材料支持“后续 SAP 在数据库关闭前澄清死亡处理”的可能性，不能据此认定是未经预先安排的变更。**[正文第5页](/home/juliz/ai-paper-val/2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5)

现有审查将 C002 标为 `reproduced`、纳入审计 `CONFIRMED`，但仍为 **`Pending Human Adjudication`**。确认的是上述文件差异及其纳入资格。真正待回答的是：**这是对原方案的前瞻性澄清，还是主要分析人群的正式替换？原方案原本如何处理死亡？**[证据复核记录](/home/juliz/ai-paper-val/2025/jama.2025.15185/.ai_paper_validation/review_1_6_2/verification/evidence_recheck.md:64)

---

## User — C003

C003

## Assistant — Progress

我会核对 C003 涉及的方案、SAP、正文和分析代码，列出原文关键句及模型差异，再说明审查记录的推理和边界。

## Assistant — Answer

**C003 记录的是主要分析模型的变化：最终方案规定“基线 FMA＋治疗组＋卒中类型＋研究中心随机截距”的混合模型；SAP、正文和提供的代码则采用“基线 FMA＋治疗组”的线性回归。** 分类为 **`protocol_report`**，仍待人工裁定。

我已核对原始 PDF 对应页面影像，以及 `.ai_paper_validation/` 中的最终报告、证据复核和审计记录。

**① 原方案明确规定了哪些模型项？**

最终方案 PDF 第86页，§11.4.2 写道：

> “It will be analyzed by a mixed effects model, with FMMA-score at baseline as covariate to adjust for differences at baseline and treatment as two-level factor (‘levodopa’ vs. ‘placebo’) as well as type of event (acute ischemic vs hemorrhagic stroke) as fixed effects. Furthermore, for each center a random intercept will be estimated.”

也就是：

- 基线 FMA：协变量；
- 治疗组：固定效应；
- 卒中类型（缺血性／出血性）：固定效应；
- 研究中心：随机截距。[方案第86页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp1_prod_1761597796.4601.pdf#page=86)

将这段规定写成示意公式：

\[
Y_{ij}=\beta_0+\beta_T T_{ij}+\beta_B B_{ij}
+\beta_S S_{ij}+u_j+\varepsilon_{ij},
\]

其中 \(Y\) 是3个月 FMA，\(B\) 是基线 FMA，\(S\) 是卒中类型，\(u_j\) 是中心随机截距。**这是对文字规定的表达，没有重新拟合模型。**

**② SAP 和正文如何描述最终模型？**

SAP 第10页，§5.2 写道：

> “Fugl-Meyer Motor Assessment at Visit 3 will be analyzed by a linear model, with Fugl-Meyer Motor Assessment at baseline as covariate to adjust for differences at baseline and treatment as two-level factor (‘Levodopa’ vs. ‘placebo’) as variable of interest.”

这里列出基线 FMA 和治疗组，没有列出卒中类型或中心随机截距。[SAP 第10页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp2_prod_1761597796.4701.pdf#page=10)

正文第4页与之对应：

> “A linear regression model was used to analyze the primary outcome, adjusting for baseline FMA total scores and including the treatment group (levodopa vs placebo) as the primary variable of interest.”

即：使用线性回归，调整基线 FMA，治疗组为主要关注变量。[正文第4页](/home/juliz/ai-paper-val/2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4)

**③ 会不会只是正文把模型写简略了？代码提供了更直接的证据**

补充材料5，第1页第22–23行：

```r
model <- with(mice0,
  lm(fma_affected.Visit_3 ~ fma_affected.Visit_1.cent + medication))
```

第26行：

```r
summary(pool(model))
```

模型公式只有基线 FMA 和治疗组，之后汇总各插补数据集的模型结果。[原始代码第1页](/home/juliz/ai-paper-val/2025/jama.2025.15185/joi250066supp5_prod_1761597796.4751.pdf#page=1)

特别需要区分：代码第20行将 `fma_affected.Visit_1.cent` 注释为 **“baseline value (centered)”**。这里的 `.cent` 表示**基线数值经过中心化**，不表示模型已经纳入“研究中心”。

因此，提供的代码支持的模型是：

\[
Y_i=\alpha_0+\alpha_T T_i+\alpha_B(B_i-c)+\varepsilon_i.
\]

基线中心化只是改变基线变量的表达方式，不能代替卒中类型项或研究中心随机截距。

| 模型组成 | 最终方案 | SAP／正文／提供的代码 |
|---|---|---|
| 基线 FMA | 有 | 有 |
| 治疗组 | 有 | 有 |
| 卒中类型固定效应 | 有 | 未纳入所示公式 |
| 中心随机截距 | 有 | 未纳入所示公式 |

**④ 为什么登记 C003？**

推理是：

1. 最终方案明确指定了主要模型，包含卒中类型和中心随机截距。
2. SAP、正文与代码一致指向另一个模型，少了上述两项。
3. 因为有明确代码，这个比较不只依赖“正文没有提到某项”的推测。
4. 提供的报告未识别出原方案混合模型的对应结果。

因此，工作流按 **Route A 第5类：计划中的主要分析被替换或未报告** 登记。它不是基于“多中心研究应该采用什么模型”的建议，而是比较**文件明确承诺的模型与最终提供的模型**。

关联的主要结果为：

\[
\text{调整后均值差}=-0.90,\quad
95\%\,CI=[-3.78,1.98],\quad P=.54.
\]

这个估计、区间和 P 值本身没有显示冲突。**现有材料不能确定加入卒中类型和中心随机截距后，估计或标准误会改变多少，更不能确定结论是否改变。** 没有原始／插补数据及原模型输出，无法作这种数值比较。

**⑤ 为什么仍需人工裁定？**

正文第5页说明：

> “Prespecified analyses were performed as outlined in the statistical analysis plan, which was finalized before database closure.”

原方案也把详细统计方法交给后续 SAP。因此，**后续 SAP 可能是在数据库关闭前有意替换了原模型**；不能仅凭模型差异认定这是事后或未经安排的变更。[正文第5页](/home/juliz/ai-paper-val/2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5)

但文章关于一般一致性、术语和 estimand 的说明，没有具体交代为何移除卒中类型项及中心随机截距。

记录中，`F-XS-101` 与 `F-ST1-001` 合并为 C003；证据复核为 `reproduced`，纳入审计为 `CONFIRMED`，关系为 `P_R, P_P`。**确认的是模型规定存在差异及其候选资格，状态仍为 `Pending Human Adjudication`。** 待澄清的问题是：哪份前瞻性文件正式替换了这些模型项，以及原混合模型是否有可提供的结果。[完整复核记录](/home/juliz/ai-paper-val/2025/jama.2025.15185/.ai_paper_validation/review_1_6_2/verification/evidence_recheck.md:98)

---

## User — Save conversation

write your conversation into a created-by-you subfolder ./review_records/* into a md file

## Assistant — Progress

我会在 `review_records/` 下新建子文件夹，将目前关于 C001、C002、C003 的用户消息和我的答复按顺序保存为 Markdown。
