# 候选问题讨论记录：C001–C016

记录日期：2026-10-17。本文汇总本次聊天中的问题、原文依据、解释及影响判断，不是逐字聊天转录，也不替代正式质量控制报告。所有候选仍为 **Pending Human Adjudication（待人工裁定）**；下文影响判断是基于所提供材料的讨论判断。

用户要求：用中文解释，提供英文原文及来源，最后用1–2句总结；后续明确要求每次回到原始材料核对，并对候选的实际分析影响及主要结论影响作出有边界的判断。页码均为 PDF 页码。

## 来源索引

- [论文正文](../jama_berry_2025_oi_240158_1742927563.7361.pdf)
- [补充材料1：试验方案](../joi240158supp1_prod_1742927563.7611.pdf)
- [补充材料2：统计分析计划（SAP）](../joi240158supp2_prod_1742927563.7711.pdf)
- [补充材料3：结果补充材料](../joi240158supp3_prod_1742927563.7911.pdf)
- [正式候选台账](../.ai_paper_validation/review_1_6_2/candidate_ledger.md)

## C001：肌力结局从次要终点到探索性指标

**原文依据**

- [方案第112页](../joi240158supp1_prod_1742927563.7611.pdf#page=112)，在 “Secondary Efficacy Endpoints” 下列出：
  > “Change in muscle strength as measured isometrically using hand-held dynamometry (HHD) and grip strength.”
- [SAP第112页](../joi240158supp2_prod_1742927563.7711.pdf#page=112)：
  > “HHD lower extremity average percentage, HHD upper extremity average percentage, HHD global average percentage, HHD0, and HHD02 are exploratory measures.”
- [正文第3页](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3)将 handheld dynamometry 列入 “Other exploratory measures”。

**讨论及澄清**

用户追问 RCT 中 secondary 与 exploratory 是否等效。回答：不能直接等效，但两者并非完全互斥；secondary 描述终点层级，exploratory 描述探索性定位，一个预设次要终点也可以按探索性方式分析。是否支持确证性结论，还取决于检验层级和多重性控制。

[SAP第104页](../joi240158supp2_prod_1742927563.7711.pdf#page=104)规定部分分析事项以 SAP 为准，可能解释有意细化。不能仅凭标签变化认定发生实质性证据等级降低。

**总结：**已观察到文件间分类变化，需要修订依据及适用版本解释；现有引文不足以认定该变化影响确证性推断或数值结果。

## C002：血浆 NfL 是预设还是事后分析

**原文依据**

- [正文第3页](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3)：
  > “Serum NfL analysis was prespecified to occur in the full analysis set (including placebo participants from other regimens), while plasma NfL was prespecified to occur in samples from this regimen only.”
- [结果补充材料第6页](../joi240158supp3_prod_1742927563.7911.pdf#page=6)：
  > “Plasma NfL was added later as a post-hoc analysis.”
- [同补充材料第11页](../joi240158supp3_prod_1742927563.7911.pdf#page=11)：
  > “The plasma analysis was pre-specified in Clene Nanomedicine’s Pharmacodynamic SAP originally as UCH-L1 alone, but due to non-availability of the UCH-L1 assay the Neurology 4 Plex-A (including NfL) was analyzed, thus it is considered post-hoc for the purposes of this manuscript.”

**解释与限制**

预设采集血浆或分析 UCH-L1，不能自动证明预设了血浆 NfL 分析。正文与补充材料对同一血浆 NfL 分析使用不同状态标签；独立药效学 SAP 及完整修订时间线未在包内提供，无法确定全部预设过程。

**总结：**需带日期的药效学 SAP 和修订文件澄清预设状态，不能从现有材料推断所有可能计划中均未预设该分析。

用户另要求的英文两句总结：

> The main article describes plasma NfL analysis as prespecified, whereas Supplement 3 states that it was added post hoc following an assay substitution. The dated pharmacodynamic SAP and any amendments are needed to clarify its prespecification status.

## C003：部分预设分析未找到可对应的定量结果

**原文依据**

- [SAP第117页](../joi240158supp2_prod_1742927563.7711.pdf#page=117)，接续前页主要模型说明：
  > “…applied to the FAS analysis set as the primary analysis, to the ECM and ERO analysis sets as sensitivity analyses, and to the EPP analysis set as a supportive analysis.”
- [SAP第119页](../joi240158supp2_prod_1742927563.7711.pdf#page=119)：
  > “SVC will be analyzed as a joint-rank test by substituting the change from baseline of SVC in place of ALSFRS-R total score as an additional supportive analysis,”
- [SAP第125页](../joi240158supp2_prod_1742927563.7711.pdf#page=125)：
  > “Placebo multiple imputation analyses will be applied to ALSFRS-R total score, HHD upper and lower extremity percentages, and SVC.”
- [结果补充材料第9页](../joi240158supp3_prod_1742927563.7911.pdf#page=9)：
  > “Prespecified sensitivity analyses, including CAFS, which was employed as a sensitivity analysis, in addition to a secondary endpoint, were performed to assess the sensitivity of the results to the primary analysis population, modeling assumptions, and missing data assumptions as described in Statistical Analysis Plan (available as a Supplement).”

**讨论范围**

台账列出未找到明确对应输出的分析家族：ECM/EPP DRR；SVC 联合秩；CAFS/SVC 失访多重插补联合秩；仅死亡的联合秩变体；基线 NfL 调整的 SVC 秩分析；ALSFRS-R/SVC 安慰剂参考多重插补；部分仅死亡及较长期生存输出；部分早期病情、尿酸、延髓起病和中心亚组输出。聊天选取上列原句说明代表性项目，完整逐项对应见正式台账及复核记录。

报告已提供 FAS/ERO DRR、部分 SVC 模型及第24周死亡/PAV结果，不能把它们全部说成缺失；一般性的“已实施敏感性分析”也不能替代每项定量结果。

**总结：**这是预设分析与发表输出的可追溯性问题，不证明分析未实施，也不证明缺少的结果会改变结论。

## C004：CAFS 调整分析与 Wilcoxon 检验的版本差异

**原文依据**

- [SAP第3版第118页](../joi240158supp2_prod_1742927563.7711.pdf#page=118)代码：
  ```sas
  model Rank = sx2bl dFRS rlz edv trtrnd / solution clparm;
  ```
- [第119页](../joi240158supp2_prod_1742927563.7711.pdf#page=119)：
  > “Primary inference from the joint-rank CAFS analyses will compare survival by time to death or death equivalent, will compare change in function to the last jointly observed time point, and will adjust for the specified covariates.”
- [正文第3页](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3)：
  > “A Wilcoxon rank-sum statistical test was used to compare the groups.”
- [正文第4页](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4)：
  > “CAFS showed a shared placebo mean rank of 143.9 and combined CNM-Au8 dosage group mean rank of 140.5 (P = .51).”
- [SAP第1版第84页](../joi240158supp2_prod_1742927563.7711.pdf#page=84)确实规定：
  ```sas
  proc npar1way data=work.cafs wilcoxon;
  ```

**版本背景与影响边界**

第1版日期为2022年3月17日；第3版日期为2022年7月22日，[修订记录第97页](../joi240158supp2_prod_1742927563.7711.pdf#page=97)明确说明主要 CAFS 为调整分析并增加相应代码。正文另报基线 NfL 敏感性分析 P=.88，不能直接证明四协变量主要分析已呈现。

**总结：**需确认 P=.51 依据哪版 SAP，并定位新版指定的调整分析输出；不能据现有材料推断调整后结论会改变。

## C005：预设 log-rank 与报告调整 Cox 的对应关系

**原文依据**

- [SAP第117页](../joi240158supp2_prod_1742927563.7711.pdf#page=117)明确使用 “Kaplan-Meier product-limit estimates and log-rank test for the primary survival endpoint”。此处是关键次要生存终点的主要分析，并非整个试验主要终点。
- [SAP第121页](../joi240158supp2_prod_1742927563.7711.pdf#page=121)：
  > “In the presence of a significant different by the logrank test, inference on whether active treatment extended survival will be based on the hazard ratio estimated from an unadjusted Cox proportional hazards regression.”
- [正文第7页 Table 2](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7)列标题为 “Adjusted Cox regression, HR (95% CI)”，合并治疗组对共享安慰剂：HR=.46，95% CI .12–1.49，P=.22。

**解释**

调整 Cox 的 P 值不能直接当作预设未调整 log-rank 检验的结果；KM 曲线本身不提供 log-rank 统计量或 P 值。[SAP第118页](../joi240158supp2_prod_1742927563.7711.pdf#page=118)允许报告名义次要终点 P 值，因此主要终点未达显著性不能单独解释该结果未呈现。

**总结：**需定位 log-rank 输出或说明方法替换依据；未明确呈现不证明未实施，也不证明结论会变化。

## C006：生存模型是否调整性别

**原文依据**

- [正文第3页](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=3)的 Cox 协变量为：
  > “…prebaseline ALSFRS-R slope, months since symptom onset, riluzole and edaravone use at baseline, and age at baseline.”
- [第7页 Table 2 脚注b](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7)：
  > “Models adjusted for age, sex, time since symptom onset, prebaseline ALSFRS-R slope, riluzole use at baseline, and edaravone use at baseline.”
- [结果补充材料第10页](../joi240158supp3_prod_1742927563.7911.pdf#page=10)也列出前述五项，没有列性别。

**解释与影响边界**

正文和补充材料是五项，表格是六项，差异在 sex。可能是方法段省略、表格描述最终模型，也可能对应不同拟合；没有模型输出不能判断。表脚注适用于六项生存 HR 比较。

**总结：**需确认产生各 HR、区间和 P 值的实际调整集，不能推断加入性别后结果的变化方向或大小。

## C007：主要模型的每月死亡事件率数值不一致

**原文依据**

- [正文第4页](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4)：
  > “The bayesian shared parameter model estimated that the mortality event rate was 0.007 events per month for the shared placebo group and 0.006 events per month for the combined CNM-Au8 dosage groups (Figure 2) (eTable 2 in Supplement 3).”
- [结果补充材料第15页 eTable 2](../joi240158supp3_prod_1742927563.7911.pdf#page=15)，标题为 “Primary Efficacy Analysis of Function and Mortality with Bayesian Shared Parameter Model”，死亡事件率如下：

| 组别 | 中位数 | 均值（SD） | 95%可信区间 |
|---|---:|---:|---:|
| Shared placebo | .010 | .010（.0026） | .0054–.0154 |
| Pooled CNM-Au8 | .009 | .009（.0025） | .0052–.0150 |

**解释与影响边界**

同模型、组别及每月单位分别出现 .007/.006 与 .010/.009；均值/中位数选择或通常显示精度不能直接解释。可能存在未注明的条件/边际估计或不同拟合，但材料未明确区分。

**总结：**需确认死亡模型参数的定义与对应输出；这不是通过粗事件比例重算模型，也不足以判断主要疗效结论受影响。

## C008：SVC 的24周变化与每月变化率标签不一致

**原文依据**

- [正文第4页](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4)：
  > “The estimate of the mean change in SVC over 24 weeks was −9.32 PPN per month in the combined CNM-Au8 group (30 mg, −7.84; 60 mg, −10.79) vs −8.53 PPN per month in the shared placebo group (difference, −0.78 PPN/month [95% CI, −4.25 to 2.68])…”
- [结果补充材料第16页 eTable 3A](../joi240158supp3_prod_1742927563.7911.pdf#page=16)在 “24-week Change Estimate” 下列相同数值：合并治疗 −9.32、共享安慰剂 −8.53，差异 −.78，95% CI −4.25至2.68。
- 正文同段另报基线 NfL 调整敏感性分析为 −1.73 对 −1.55 PPN/month。

**解释与影响边界**

累计变化和月斜率不是同一个量。24周累计 −9.32 粗略折合每月 −1.69，仅用以说明单位差异，不能替代拟合的随机斜率估计。补充表支持24周变化的解释，需要明确各输出的模型身份。

**总结：**数值一致，但标签可能让读者提取出不同时间尺度的量；尚未显示拟合计算或主要结论因此变化。

## C009：事件数与排除人数的归属不清

用户在要求持续核对原文后再次询问 C009；后一次回答直接重新提取原始 PDF，并进一步收紧了影响判断。

**原文依据**

- [正文第4页](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4)：
  > “Of those, 4 of the 41 participants in the regimen placebo group and 2 in the shared placebo group were excluded due to having no follow-up time (1 had PAV at baseline and 1 terminated early at baseline visit).”
- [第7页 Table 2](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7)“Observed proportions”列：本方案安慰剂4/41，共享安慰剂9/162。同页正文明确写 “regimen placebo group (4 events [9.8%])”。
- 同表脚注a：
  > “Two shared placebo participants were not included due to having no follow-up time; 1 had PAV at baseline and the other terminated early at baseline.”

**后续澄清及影响判断**

第4页按句法将4人及2人一起归于排除；第7页明确把4称为事件，只把2名共享安慰剂参与者列为无随访排除。更有原文支持的解释是：4/41本意为事件比例，但被连接到排除句中。

不能直接主张实际生存分析分母应为37：观察比例的分母不必自动等于 Cox 拟合人数，且实际排除身份未知。没有证据证明模型使用了不一致人数。

**总结：**最稳妥的描述是正文中事件数与排除人数归属不清；需澄清句意和实际分析集，而非据此断言分析人数发生实质变化。

## C010：预设亚组分界与报告分组不同

**原文依据**

- [SAP第126页](../joi240158supp2_prod_1742927563.7711.pdf#page=126)：
  > “Baseline delta-FRS score (less than 0.47 points/year, 0.47 to less than 1.11 points/year, 1.11 points/year or greater)”
- [结果补充材料第13页](../joi240158supp3_prod_1742927563.7911.pdf#page=13)在预设亚组说明中写：
  > “…pre-baseline rate of progression by delta-FRS (fast vs. slow with median split)…”
- [eTable 4第20页](../joi240158supp3_prod_1742927563.7911.pdf#page=20)显示 “dFRS < Median” 和 “dFRS >= Median”，交互 P=.70。
- SAP同页体重分组：
  > “Weight (less than 43 kg, 43 to less than 56 kg, 56 to less than 77 kg, 77 to less than 150 kg, 150 kg or more)”
- [eTable 4第19页](../joi240158supp3_prod_1742927563.7911.pdf#page=19)显示＜56、56至＜77、77至＜150 kg。

**解释与影响边界**

delta-FRS 三个固定阈值组与两个中位数组不能通过单位或舍入等同。体重＜56标签覆盖两个原计划组，但若无人＜43 kg，实际成员可能没有变化；≥150 kg未显示也可能因为无人，不能独立视为结果缺失。

**总结：**需预设修订记录解释 delta-FRS 分组，以及确认体重标签是否改变实际成员；现有材料不能量化对亚组推断的影响。

## C011：六分下降终点的比例定义与死亡复合时间定义不同

**原文依据**

- [方案第112页](../joi240158supp1_prod_1742927563.7611.pdf#page=112)，探索性终点：
  > “Difference in the proportion of patients experiencing a ≥ 6-point decline in the ALSFRS-R between active treatment and placebo from Baseline to Week 24.”
- [SAP第111页](../joi240158supp2_prod_1742927563.7711.pdf#page=111)：
  > “Time to first occurrence of a ≥ 6-point decline in ALSFRS-R total score is a composite endpoint with death or death equivalent, whichever occurs first, and will be censored at the last date at which an ALSFRS-R assessment was performed up to the end of the Week 24 Visit window.”

**解释与影响边界**

差异包括分析量（24周发生比例 vs 首次事件时间）和组成（功能下降 vs 加入死亡/死亡等同事件）。若先死亡后未观察到六分下降，SAP将其计为复合事件，而方案这条未明确处理方式。可能是 SAP 正式细化，需适用版本及修订依据。

**总结：**这是计划文件之间的终点定义变化；没有对应数值重分析，不能判断实际结果或主要结论的变化。

## C012：NfL 区间与 P 值的显示精度

**原表依据**

[结果补充材料第17页 eTable 3B](../joi240158supp3_prod_1742927563.7911.pdf#page=17)：

| 行 | 差异估计 | 95% CI | P |
|---|---:|---:|---:|
| 合并剂量血浆 | −9.5 | −18.0, 0 | .04 |
| 60 mg血浆 | −10.5 | −20, 0 | .04 |
| 60 mg血清 | −27.4 | −45.1, −.7 | .05 |

[正文第8页 Figure 3A](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8)：

> “Week 24 least-squares mean difference, −9.5% (95% CI, −17.8% to −0.5%); P = .04”

**解释与影响判断**

印刷上前两行区间包含0而P＜.05，第三行区间排除0而P显示.05。但上限显示0可能掩盖略负值；P显示.05也可能由.047等数舍入而来。正文更精细的合并血浆区间支持显示精度解释，不能据此认定底层检验和区间不相容。

**总结：**这是临界结果的显示精度与可读性问题；需未舍入输出和推断方法确认，其本身不证明统计计算存在冲突。

## C013：血清 NfL 的组间差异尺度不清

**原文依据**

[结果补充材料第17页](../joi240158supp3_prod_1742927563.7911.pdf#page=17)脚注：

> “Serum and plasma NfL was modeled as log-transformed and exponentiated back to the original scale to present results.”

该表 “Serum NfL (% change)” 的治疗变化、安慰剂变化、组间差异依次为：

| 组别 | 治疗变化 | 安慰剂变化 | 差异 |
|---|---:|---:|---:|
| 合并剂量 | .4 | 26.8 | −26.4 |
| 30 mg | 1.4 | 26.8 | −25.5 |
| 60 mg | −.5 | 26.8 | −27.4 |

[正文第8页 Figure 3B](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8)：

> “Week 24 least-squares mean difference, −23.2% (95% CI, −39.5% to −2.5%); P = .03”

同页安慰剂血清几何均值增幅为30.8%。

**推导比较（不是原文数值）**

若各组变化是同一模型反变换后的几何均值变化率，合并血清相对差异为 `100 × (1.004 / 1.268 − 1) ≈ −20.8%`，不能对应−26.4%；后者等于 .4−26.8。同表血浆用 `100 × (.977 / 1.079 − 1) ≈ −9.5%` 则能对应表列结果。

若26.8、−26.4实际上是对数变化乘100，指数反变换约为30.7%、−23.2%，接近正文。该解释来自推导，并非原表明确声明；也不能在未确认估计量时直接把推导值作为更正。

**总结：**需确认血清各组变化、组间差异及区间的尺度与定义；现有数值提示尺度可能混用，但不能确定生成过程或实际疗效推断影响。

## C014：设计模拟中 DRR 变化方向的说明

**原文依据**

[SAP第50页 §6.2](../joi240158supp2_prod_1742927563.7711.pdf#page=50)：

> “Under scenarios when the treatment effect for mortality is null or worse (true HR=1.0 or HR=1.3) and there is a 30% slowing in ALSFRS-R (true DRR=0.70), the power and estimated DRR decrease as the rate of mortality increases.”

同页 Table 6.2.1 在功能真实DRR=.70、死亡HR=1.3下：

| 6个月死亡率 | 效能 | 平均估计DRR |
|---|---:|---:|
| 5% | .68 | .72 |
| 10% | .57 | .75 |
| 20% | .35 | .81 |

同段随后写：

> “…the average estimated DRR equals 0.75 and 0.81 when the true mortality HR equals 1.0 and 1.3, respectively, thereby decreasing the estimated functional treatment effect…”

**用户特别追问：严重影响的可能性，是否不影响主要结论**

文字称 DRR 下降，但表格 DRR 上升、效能下降；随后的获益下降说明与表格一致。DRR接近1意味着获益减小，可能是把“获益下降”写成“DRR下降”。

这是设计模拟解释，未显示改变模型、程序、数据或实际试验结果。现有证据更支持直接分析影响较低，不能给出可靠概率百分比；没有依据认为这一项会推翻试验主要结论。

**总结：**方向表述影响模拟解释，但同页数值及后续说明相互一致；尚无实际分析或主要结论受影响的证据。

## C015：模拟示例 CAFS P 值前的短横线

**原文及视觉依据**

直接渲染并查看[原始SAP第59页](../joi240158supp2_prod_1742927563.7711.pdf#page=59)，页首保留换行：

> “When matched regimen-specific controls are only used, both the Bayesian shared parameter analysis and the CAFS analysis lead to a null result, (treatment effect estimate of 1.0, posterior probability DRR<1 of 0.51 and CAFS p-value of -
> .3675).”

同页 Figure 6.3.2 下排右图明确写：

> “Post. DRR<1: 0.51”
>
> “CAFS P-value: 0.3675”

图注明确为 “Example Trial 4. Null Treatment Effect (DRR = 1.00).”

**影响判断**

短横线可能被连续读作负号，但P不能为负；图中正值、正文null result及其他匹配参数强烈支持排版/标点多余字符的解释。这是模拟示例，不是实际 CNM-Au8 试验 CAFS 结果，没有证据显示计算生成负P或改变模型和决策。

**总结：**这一项极不可能单独造成严重分析影响，没有依据认为影响主要结论；保留为待人工裁定的印刷歧义，不应升级为实质分析问题。

## C016：低于定量限的血清 NfL 用 LOQ 还是 LOD 替代

**原文依据**

- [SAP第112页 §5.6](../joi240158supp2_prod_1742927563.7711.pdf#page=112)：
  > “Levels of serum and CSF NfL and urinary p75[ECD] that are reported to be below the limit of quantitation will be imputed at the limit of quantitation. Levels of serum and CSF NfL will be log-transformed in all analyses.”
- [结果补充材料第11页](../joi240158supp3_prod_1742927563.7911.pdf#page=11)：
  > “If a serum sample value was <LOQ, the value was imputed by using the assay LOD. For the primary analysis, no outliers were omitted.”

同样是低于LOQ，计划替代为LOQ，报告替代为LOD。二者是不同检测阈值概念，材料未说明该检测中二者数值相等。

**影响判断**

这项可能实际改变血清NfL的分析输入。若存在替代数值且LOD/LOQ不同，对数输入、效应估计及P可能改变；方向取决于组别及时间点分布。若没有受影响数值或两个阈值相同，则可能无数值影响。

[正文第8页](../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8)显示血清结果对一个安慰剂基线低值敏感：原差异−23.2%、P=.03；排除后−9.7%，95% CI −18.5%至.1%，P=.05。原文写：

> “This result suggests that the magnitude but not directionality of the analysis of serum NfL was sensitive to the effect of an outlier.”

但没有说明该低值低于LOQ或经过替代，不能把排除低值的敏感性分析当作LOQ与LOD替代规则的直接比较。

缺少实际阈值、替代值数量及分布，不能量化影响或给出严重影响概率。C016直接涉及探索性血清NfL，未显示它改变主要疾病进展模型，因此不能据此认为试验主要结论被推翻。

**总结：**相比纯印刷歧义，这项值得核实实际处理代码，可能影响探索性生物标志物效应量及名义显著性；现有证据不支持它改变主要结论。

## 本次讨论形成的判断边界

- 数值、标签、模型或计划定义不一致，不自动等于实际计算受到影响。
- C009的后续复核强调事件数与排除人数的句法归属，不能直接推断实际风险集人数。
- C012的印刷区间/P组合可以由四舍五入解释，正文对合并血浆结果提供了支持。
- C014、C015涉及设计模拟的说明；现有证据不支持其直接影响实际主要结果。
- C016可能影响探索性血清NfL输入和推断，但需实际替代记录才能量化。
- 所有“未显示影响主要结论”的判断仅限相应候选及现有材料，不是对整个试验全部分析的最终裁定。

## 原文复核记录

本次聊天前段使用已有来源提取文本核对引句；用户明确强调持续查阅原文后，第二次C009及C010–C016均用项目允许的 `pdf_tools.py` 从原始PDF重新提取相应页。C015另经CPU渲染原页并直接视觉核对短横线及图中P值。未使用外部文献，未修改原始PDF或既有正式台账。
