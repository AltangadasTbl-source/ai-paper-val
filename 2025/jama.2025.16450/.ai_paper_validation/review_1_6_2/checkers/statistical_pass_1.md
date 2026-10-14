# Statistical pass 1 — complete disjoint union

All 209 relationships have explicit PASS_1_COMPLETE receipts. Fresh specialist records and individual completion receipts follow without loss.

# Statistical pass 1 — shard 1

Runtime agent ID: `/root/statistics_pass_1`. Model: `gpt-6.1-sol`; reasoning effort: `high`; start mode: `FRESH_SPAWN`. This agent performs pass 1 only. Exact scope is the 120 S IDs enumerated in `statistics/parts/assigned_s_1.md`: S001–S048 and S201–S272. The individual completion records are in `statistics/parts/pass_1_status_1.md`; every assigned relationship is `PASS_1_COMPLETE`.

Read `QUALITY_CONTROL_SCOPE.md`, `workflow_1_6_2/review_contract.md`, the statistical role preset, current tooling and source inventories completely. Read the complete assigned inventories, main result/method extraction, protocol prospective specifications, complete results eTables 3–4 and their footnotes, and relevant SAP method/revision/population context. Visually checked source-linked main Tables 2–3 and Figure 2; results-supplement pages 5–8; protocol pages 4, 5, 7, 17, 18, 20–23, 25–29; and SAP pages 29, 38–39. Existing source-linked renders were read without alteration. Existing native/layout/OCR text is a locator, not final authority. No new extraction, rendering or OCR was needed, and no web or historical scientific conclusions were used.

All assigned result estimates lie between ordered interval endpoints. No assigned row supplies an estimate-associated numerical P value or test statistic in conflict with its interval. The five Figure 2 P values are factor-level values, not assigned to individual subgroup estimates. No noninferiority or equivalence conclusion is stated. Counts, percentages, component totals, observed-outcome denominators, odds-ratio exceptions, and result direction were also checked for every applicable S row. Four consolidated findings and eight excluded observations follow. Findings are proposals for independent inclusion screening; no candidate ID or adjudication is assigned.

## Findings

### F-ST1-001

**Title:** Reported BPD-severity model differs from the planned ordinal model.

**Relationships:** S006, S007, S008, S011, S012, S013, S046, S205, S212. **Focus area:** D, with statistical-method logic in C. **Proposed review domain:** `protocol_report`. **Proposed primary relationship type:** `P_R`; **All relationships:** `P_R`.

**Exact locations and document roles:** [Protocol PDF p 25, §5.1](../../../joi250072supp1_prod_1761000786.68881.pdf#page=25), PLAN; [protocol PDF p 21, BPD severity outcome](../../../joi250072supp1_prod_1761000786.68881.pdf#page=21), PLAN; [SAP PDF p 39, §9.5](../../../joi250072supp3_prod_1761000786.6988.pdf#page=39), PLAN; [main PDF p 3, secondary/exploratory outcome descriptions](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3), REPORT; [main PDF p 8, Table 3 severity rows and footnote a](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=8), REPORT.

**Printed statements and values:** Protocol §5.1 assigns proportional-odds models to ordinal outcomes and generalized logits to nominal outcomes. SAP §9.5 explicitly uses BPD severity/grade as its ordinal example, specifies proportional odds, and names partial proportional odds or a Mantel–Haenszel mean-score test if that assumption fails. Generalized logits are specified separately for unordered nominal outcomes. The report calls BPD severity ordinal on p 3, but Table 3 footnote a says its ORs were estimated by logistic regression with generalized logit. The reported no-BPD-reference grade-specific ORs are pragmatic grades 1/2/3: 0.87 (0.54–1.41), 0.88 (0.55–1.42), 0.99 (0.51–1.89); NIH grades 1/2/3: 1.13 (0.59–2.17), 0.63 (0.30–1.34), 0.87 (0.47–1.63).

**Rule and reproduced comparison:** Match the same ordered four-level BPD endpoint, 36-week assessment, treatment contrast and stratifier adjustment. The reported category-versus-no-BPD generalized-logit model is distinct from each model/test listed for ordinal outcomes in the supplied plan. This is a method-specification comparison, not a recomputation of adjusted ORs and not a proposal to use a different analysis. Display-precision arithmetic does not apply to model-family statements. No issue is raised with the individual estimate containment or null conclusions.

**Qualifying route:** Route B. The observation concerns a supplied planned-versus-reported analysis specification, persists after reading the explicit ordinal and nominal alternatives, and changes the statistical quantity attached to the reported grade-specific ORs.

**Affected result or extracted value:** The BPD-severity treatment comparison and the six grade-specific Table 3 ORs, including whether an extracted OR describes a category-versus-no-BPD contrast or a cumulative ordinal contrast.

**Why context does not resolve it:** The report names generalized logit without identifying an amendment or explaining how the planned ordinal analysis and its named fallbacks map to the displayed contrasts. A reader cannot infer that a generalized-logit fit is a proportional-odds or partial-proportional-odds fit merely from the shared logistic terminology.

**Source-grounded alternatives and missing definitions:** A deliberate additional nominal analysis may have been selected; a planned ordinal analysis may have been performed separately; or an analysis change may have been documented outside the supplied package. SAP permits additional ad hoc secondary/exploratory analyses, but the supplied results do not identify the planned ordinal analysis or the displayed model as an additional analysis. Missing: the model actually fitted for severity, the status/results of the planned ordinal fit, and any disclosed amendment authorizing its replacement. The absence of a proportional-odds assumption test is not itself a finding.

**Exact human question:** Which model and contrast produced the six BPD-severity ORs in Table 3, and where are the planned ordinal analysis or the documentation and rationale for replacing it with the reported generalized-logit analysis?

### F-ST1-002

**Title:** Prespecified analyses of the primary outcome are absent from the supplied results.

**Relationships:** S001, S002, S003, S026, S047, S048, S213, with relevant SAP context. **Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed primary relationship type:** `P_R`; **All relationships:** `P_R`.

**Exact locations and document roles:** [Protocol PDF p 25, §5.1, as-received secondary analyses](../../../joi250072supp1_prod_1761000786.68881.pdf#page=25), PLAN; [SAP PDF p 38, §§9.4.1–9.4.2](../../../joi250072supp3_prod_1761000786.6988.pdf#page=38), PLAN; [SAP PDF p 29, §7.7, site/center heterogeneity](../../../joi250072supp3_prod_1761000786.6988.pdf#page=29), PLAN; [main PDF p 4, Figure 1 footnotes f and j](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=4), REPORT; [main PDF p 7, Table 2 and Sensitivity and Subgroup Analyses](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7), REPORT; [main PDF p 9, Figure 2](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=9), REPORT; [results supplement PDF p 2, eTable 1](../../../joi250072supp4_prod_1761000786.6988.pdf#page=2), REPORT. The complete main results and all eight results-supplement tables were searched/read through the current complete source map; none contains the three specified analyses below.

**Printed statements and values:** SAP §9.4.1 says the primary method will be replicated in mITT, PP and SAF populations, with the SAF replication providing an as-treated treatment-effect assessment. §9.4.2 says baseline BPD predictors (examples: birth weight, sex, race/ethnicity) will be included in a secondary robust-Poisson primary-outcome model, and a final adjusted RR and 95% CI will be reported. §7.7 says site/center treatment-effect heterogeneity will be investigated using treatment interaction terms; site grouping is allowed if the site model has overparameterization/convergence issues. Table 2 reports ITT RR 1.00 (0.90–1.11), mITT RR 1.00 (0.90–1.10), and PP RR 1.00 (0.90–1.11), with only gestational stratum and pooled center adjustment; its footnote expressly says randomized treatment assignment is used for all its populations. No SAF primary-outcome estimate, additional-baseline-adjusted primary RR, or site/center heterogeneity result is printed. eTable 1 distinguishes mITT as randomized (320/315) from SAF as treated (322/313); Figure 1 records four participants receiving a treatment different from their allocation.

**Rule and reproduced comparison:** Compare mandatory primary-outcome analysis specifications to the complete supplied REPORT result set. The treated ITT analysis does not implement the distinct SAF contrast: excluding untreated participants retains randomized assignment, whereas SAF reassigns by treatment received. The displayed stratifier-only fit does not implement the additionally baseline-adjusted fit. Figure 2 contains gestational age, chorioamnionitis, baseline FIO2, sex and race results, with no site/center heterogeneity statistic. These are consolidated as one pattern of omitted prespecified primary-outcome analyses. No unreported effect value is imputed. Display precision is not applicable to absence of planned analyses.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The primary BPD/death treatment effect under actual receipt, under additional baseline adjustment, and its planned site/center heterogeneity assessment.

**Why context does not resolve it:** Category 5 registers planned primary analyses that are not reported. Neither an analysis of the same treated infants under randomized assignment nor a table of SAF population counts supplies the planned SAF treatment effect. The baseline-adjustment subsection contains an unconditional named analysis before its separate optional statement about additional imbalanced variables. No site/center test is provided even under the plan's permissible grouping alternatives.

**Source-grounded alternatives and missing definitions:** The analyses may have been performed but omitted from this publication; a fit may have been infeasible; the baseline model may have been interpreted as conditional on imbalance; or a subsequent amendment may have removed an analysis. The supplied report does not identify such a change or provide these results. This finding does not assert that an analysis was never performed, nor does it extend to the conditional missing-data sensitivity (the printed missing fraction is below its 5% trigger).

**Exact human question:** Where are the prespecified primary-outcome SAF/as-treated replication, additional-baseline-adjusted RR with 95% CI, and site/center heterogeneity assessment, or the supplied documentation explaining why each was not reported?

### F-ST1-003

**Title:** Sparse-row confidence intervals described as exact reproduce a log-Wald calculation instead.

**Relationships:** S222, S223, S239, S240, S244, S246, S247, S261. **Focus area:** C and B. **Proposed review domain:** `statistical_results`. **Proposed primary relationship type:** `S_W`; **All relationships:** `S_W`.

**Exact locations and document roles:** [Results supplement PDF p 5, eTable 3 superscript-b sparse AE/SAE rows](../../../joi250072supp4_prod_1761000786.6988.pdf#page=5), REPORT; [PDF p 6, sparse SAE rows and footnote b](../../../joi250072supp4_prod_1761000786.6988.pdf#page=6), REPORT; [PDF p 7, eTable 4 surgical/catheter PDA row](../../../joi250072supp4_prod_1761000786.6988.pdf#page=7), REPORT; [PDF p 8, footnote b and nonmissing-denominator definition](../../../joi250072supp4_prod_1761000786.6988.pdf#page=8), REPORT.

**Printed statements and values:** Both footnotes b describe a crude unadjusted OR with exact 95% confidence intervals used to approximate RR because prevalence is low. The explicit eTable 4 surgical/catheter PDA row gives 5/319 versus 3/308 and 1.62 (0.38–6.83). eTable 3 superscript-b rows print 0.73 (0.16–3.28), 0.65 (0.11–3.90), 0.98 (0.06–15.66), 0.49 (0.04–5.39), 2.64 (0.69–10.05), 1.96 (0.36–10.79), and 2.46 (0.47–12.78), with respective event-count pairs 3/4, 2/3, 1/1, 1/2, 8/3, 4/2, and 5/2. eTable 3's headers show 322/313, but individual nonmissing denominators are not printed.

**Rule and calculation:** For the completely specified surgical/catheter PDA 2×2 table, the crude OR is (5×305)/(314×3)=1.61889597. The log-Wald standard error is sqrt(1/5+1/314+1/3+1/305)=0.73470861. The diagnostic log-Wald 95% interval exp(log(OR)±1.95996398×SE) is [0.38356047, 6.83288387], reproducing both displayed endpoints to their printed precision. A separate diagnostic conditional equal-tail exact inversion of the noncentral-hypergeometric distribution gives [0.31166570, 10.50650442]. Here the distribution weights are choose(319,x)×choose(308,8−x)×theta^x; the lower bound solves Pr_theta(X≥5)=.025 and the upper solves Pr_theta(X≤5)=.025. This inversion is explicitly a diagnostic, not an assertion that the authors used this particular exact tail convention. The source does not name the exact algorithm.

For the seven eTable 3 rows, the same log-Wald diagnostic using 321/313 available participants gives respectively [0.16178217,3.28287673], [0.10751840,3.90370250], [0.06071840,15.65629151], [0.04384042,5.38624529], [0.69422071,10.04788405], [0.35681664,10.78989329], and [0.47381514,12.77667061], again reproducing every printed endpoint. The 321 denominator is a diagnostic reconstruction from the missing treated observation and matched printed percentages, not a silently assigned denominator. Repeating with the printed header 322 produces very similar log-Wald intervals and does not remove the method question. The finding rests on the fully specified eTable 4 row; the repeated eTable 3 pattern is retained as associated evidence.

**Display-precision check:** The exact integer table in the eTable 4 row has only the printed integer values within each half-unit interval. Printed limit intervals are [0.375,0.385] and [6.825,6.835]. The diagnostic conditional exact lower endpoint is 0.06333430 below the lower printed interval (relative gap 0.16667 using 0.38), and its upper endpoint is 3.67150442 above the upper printed interval (relative gap 0.53756 using 6.83). These differences are much larger than display precision. They diagnose the missing method mapping, rather than imposing an unstated exact-CI convention.

**Qualifying route:** Route B. The source explicitly describes its interval method; an observable repeated interval pattern identifies a different reproducible calculation; the unresolved method description bears on the width of an extractable interval. This is not a preference for exact over asymptotic inference, and is not an adjusted-versus-crude comparison.

**Affected result or extracted value:** The 95% confidence interval for surgical/catheter PDA and the associated eight sparse-row odds-ratio approximations and uncertainty intervals.

**Why context does not resolve it:** The footnotes specify exact confidence intervals, not merely an exact P-value test. No software option, exact tail convention, or alternative interval construction is named that explains the printed log-Wald pattern. Choosing to read the footnote as referring only to Fisher testing would change an explicit confidence-interval statement rather than resolve the two pieces of evidence at once.

**Source-grounded alternatives and missing definitions:** An exact test may have been paired with log-Wald intervals; the interval-method description may refer to another implemented procedure; or an exact algorithm not identified in the package may give the displayed endpoints. Missing: the confidence-interval algorithm/options, and the actual nonmissing denominators for the eTable 3 superscript-b rows. All point estimates are contained in their intervals and all non-NA intervals include OR=1; no interval-versus-significance claim is made here.

**Exact human question:** Which confidence-interval procedure and analysis denominators produced the superscript-b intervals in eTables 3–4, and how does the stated exact 95% interval method map to the printed endpoints that reproduce the log-Wald calculation?

### F-ST1-004

**Title:** Planned subgroup model uses the primary adverse outcome, whereas the displayed subgroup RRs use its favorable complement.

**Relationships:** S028, S029, S030, S035, S036, S037, S038, S039, S040, S043, S044, S047. **Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed primary relationship type:** `P_R`; **All relationships:** `P_R`.

**Exact locations and document roles:** [SAP PDF p 29, §7.7](../../../joi250072supp3_prod_1761000786.6988.pdf#page=29), PLAN; [SAP PDF p 37, primary outcome coding/model](../../../joi250072supp3_prod_1761000786.6988.pdf#page=37), PLAN; [main PDF p 3, subgroup analysis description](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3), REPORT; [main PDF p 9, Figure 2 title, rows, P column and caption](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=9), REPORT; [main PDF p 7, subgroup conclusion](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7), REPORT.

**Printed statements and values:** SAP §7.7 prespecifies treatment interactions for gestational age, race and sex (also site/center, whose absence is consolidated in F-ST1-002) in the robust-Poisson model for the primary outcome. SAP p 37 explicitly codes that outcome 1 for BPD/death and 0 for alive without BPD. Figure 2 instead says its robust-Poisson analyses consider RR for the favorable outcome alive without physiologic BPD. Its gestational-age favorable RRs are 0.92 (0.54–1.58) and 1.03 (0.82–1.30), sex RRs 0.88 (0.64–1.22) and 1.12 (0.84–1.48), and race RRs 1.18 (0.86–1.63), 0.84 (0.61–1.15), 0.93 (0.33–2.66). The associated printed P values are .72, .28 and .33. The caption does not identify the outcome or model underlying those P values separately.

**Rule and calculation:** The two binary codings refer to the same participants but not the same relative-risk estimand. If adverse risks are p_A and p_B, RR_adverse=p_A/p_B, while RR_favorable=(1−p_A)/(1−p_B); the latter is not generally the reciprocal of the former. Consequently a treatment×subgroup interaction in an adverse-risk log-link model is not generally the same interaction hypothesis as one in a favorable-risk log-link model. For orientation only, the printed male counts give favorable crude RR=(44/158)/(50/162)=0.90228 and adverse crude RR=(114/158)/(112/162)=1.04363. Female counts give favorable crude RR=(57/163)/(52/156)=1.04908 and adverse crude RR=(106/163)/(104/156)=0.97546. These crude values illustrate the estimand distinction only; they are not compared with the adjusted published RRs as a reproduction test. No covariance, P-test type or model is inferred from the P-value placements. Display precision does not apply to the specified outcome/model mapping.

**Qualifying route:** Route B. The comparison concerns a supplied prespecified primary-outcome subgroup model and an explicitly different reported relative-risk outcome; the report does not map the two analyses or identify which outcome produced its factor P values.

**Affected result or extracted value:** The prespecified subgroup heterogeneity assessment for primary BPD/death, the Figure 2 subgroup RRs, and the interpretation of its factor P values.

**Why context does not resolve it:** The figure clearly identifies its favorable-outcome estimates, but it does not say whether the planned adverse-outcome interaction fits were also performed or whether its P values come from those fits or the favorable-outcome fits. Complementary binary outcomes share a no-treatment-effect null within a stratum, but relative-risk effect modification does not have that invariance. Thus identifying the intended favorable event label does not supply the planned analysis-to-test mapping.

**Source-grounded alternatives and missing definitions:** The planned adverse-outcome interaction tests may have been retained while favorable-outcome RRs were displayed; the favorable model may have replaced the planned model; or the favorable analysis may be additional and the primary interaction results omitted. The source explicitly allows additional exploratory analyses, and the report labels baseline FIO2 post hoc; no assertion is made that FIO2 or chorioamnionitis was prespecified in §7.7. Missing: the outcome coding, fitted model and test attached to each factor P value, the results/status of the planned adverse-outcome interaction fits, and any amendment connecting the two.

**Exact human question:** Were the prespecified gestational-age, sex and race interaction analyses fitted to BPD/death as planned, and which outcome coding/model produced the Figure 2 factor P values and favorable-outcome RRs?

## Excluded observations

Only apparent issues considered and not emitted appear here. Reconciled routine checks are recorded in the individual relationship records, not counted as excluded observations.

| Location | Observation | Reason code |
|---|---|---|
| REPORT results supplement p 5, eTable 3, S220–S234, especially S230 | Several percentages differ from calculations using the full 322/313 headers. The largest remaining interval gap is late sepsis in the surfactant arm: count/header half-unit recomputation [22.16906,22.56000]%, printed interval [23.65,23.75]%, gap 1.09000/23.7=0.0459916. All apparent within-display percentage discrepancies in these assigned rows are screened out by the relative-discrepancy rule; no denominator is silently substituted. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT results supplement p 8, eTable 4 abbreviation line, contextual to S253–S272 | “RR = risk difference” differs from the table heading and immediately following binary-method paragraph, both of which explicitly specify relative risk. The symbol's intended meaning is evident and no printed estimate changes. | TERMINOLOGY_OR_WORDING |
| REPORT main p 8 Table 3 footnote b versus PLAN protocol pp 7/21 and SAP pp 9/32, S006–S009/S205–S206 | Grade 1 uses “less than 2 L/min” versus ≤2 L/min. The same cited Jensen scale and adjacent grade-2 >2 definition identify the boundary; no reported number or participant reassignment is supplied. Doubt about the boundary symbol is screened out. | NOTATION_OR_TYPOGRAPHY |
| REPORT main p 7 Table 2 heading/footnote b; PLAN SAP p 37; S025/S045 | The printed heading says 95% CI while primary alpha is .049 and SAP code links CI level to alpha. No assigned primary interval excludes the null and no P-value conflict results; 95% versus 95.1% is a display-precision difference (0.1/95=0.0010526). | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main pp 2/4 and PLAN protocol pp 28–29, S023–S024/S217–S219 | The actual interim conditional-power estimate, 80% interval endpoints, information fractions and spending calculations are not supplied. No printed stopping statistic conflicts with the stated rule. Absence of these inputs alone does not reproduce a stopping-rule discrepancy. | CONDITIONAL_OR_UNREPORTED |
| REPORT main Tables 2–3/Figure 2 and results eTables 3–4, applicable modeled rows including S001/S039/S270 | Adjusted RDs/RRs/ORs/least-squares mean differences can differ from crude contrasts, including a direction change for the small Other-race subgroup. The source explicitly identifies adjustment; crude estimates are not used to challenge adjusted results. | MODEL_VERSUS_CRUDE |
| PLAN protocol p 25 versus SAP p 39 and REPORT main pp 3/8, S014–S015/S027/S212 | Protocol count-Poisson wording differs from the reported continuous ventilation-day analysis. The later SAP expressly permits linear regression for count outcomes and the report names its normal-identity/robust-variance method. No source-grounded contradiction of a fitted numerical result is reproduced. | CONTEXT_RESOLVES |
| REPORT main p 9 Figure 2, S040–S044 | The figure does not explicitly label P-test type, degrees of freedom or covariance. Missing labels alone, without a printed P/interval conflict, are not a finding. Factor P values are not treated as individual subgroup treatment P values. The separate planned-versus-reported outcome mapping is F-ST1-004. | CONDITIONAL_OR_UNREPORTED |

## Limitations and handoff

The assigned package prints no fitted covariance matrices or estimate-associated numerical test statistics/standard errors for the adjusted main/supplementary result rows. Numeric model re-fitting is unavailable without individual data. Actual conditional-power endpoints and alpha-spending inputs are absent. Figure 2 does not name its P-test estimand. eTable 3 does not print each nonmissing denominator; denominator reconstructions in the sparse-row diagnostic are labeled. The exact confidence-interval algorithm is not named. These limits do not prevent containment, endpoint-order, null-direction, row arithmetic, source-method, prespecification, or interpretation checks.

All 120 assigned S relationships received a complete pass-1 record. Findings: 4. Excluded observations: 8. No scientific scope gap remains in this assigned shard. Sources and reusable assets remain unchanged. Durable artifacts: `checkers/parts/statistical_pass_1_1.md` and `statistics/parts/pass_1_status_1.md`.


---

# Statistical pass 1 — disjoint shard 2

Runtime agent ID: `/root/statistics_pass_1_2`. Fresh spawn; run model `gpt-6.1-sol`; reasoning effort `high`. Scope: 89 assigned relationships in `statistics/parts/assigned_s_2.md`. The explicit S-ID completion records are in `statistics/parts/pass_1_status_2.md`. Source content controls; extraction and OCR are locators. No legacy findings, screening records, dispositions, or reports were read; no external material was used. Four findings and eleven excluded observations follow. These are observations for independent screening, without candidate IDs or adjudications.

Every applicable relationship was checked for count/denominator arithmetic, effect-measure identity, estimate containment and endpoint order, inferential direction, method logic, and plan/report implications. Prospective operational definitions have no observed estimate, CI, P value, standard error or test statistic to pair. No noninferiority or equivalence margin is specified in this assigned trial scope. For the historical tables, P-value checks used only supplied test labels; unavailable contributor sizes, degrees of freedom and variance choices were not inferred. Normal approximations below are explicitly diagnostic.

## Findings

### F-ST1-1001

**Title:** Historical Grade 3 BPD count, percentage and test do not reconcile within one display.

**Relationships:** S276; P_P. **Focus area:** A, B. **Proposed review domain:** `plan_material`.

**Exact locations and document roles:** PLAN [protocol PDF p12, Table 2, NICHD BPD Workshop Grading 2018, Grade 3, Surfactant column and P-value column](../../../joi250072supp1_prod_1761000786.68881.pdf#page=12). On that same page the Death and Grade 3 or Death rows corroborate the relevant components; they do not change the relationship type.

**Printed values:** Grade 3: Surfactant `20% (31/294)`; surfactant+budesonide `12% (21/173)`; `0.02#`. Footnote # denotes a chi-square test. Death: `11% (31/294)` versus `9% (15/173)`; Grade 3 or Death: `31% (91/294)` versus `21% (36/173)`.

**Rule and calculation:** Within-row percentage must reconcile with its numerator and denominator. (100(31/294)=10.5442\%), rather than 20%. Even allowing half-unit intervals to all displayed inputs, (100[30.5/294.5,31.5/293.5]=[10.3565,10.7325]\%). The printed 20% interval is [19.5,20.5]%; gap=8.7675 percentage points; relative discrepancy=8.7675/20=0.4384, above 0.05. Using the displayed counts for a diagnostic Pearson chi-square comparison gives chi-square=0.27984 and two-sided P≈0.59680, rather than .02. The percentage inconsistency requires no assumption about test implementation. If death and surviving Grade 3 are disjoint, the composite counts imply (91-31=60) Grade 3 surfactant infants and (36-15=21) combination infants; 60/294≈20.4%. This is an alternative reconstruction, not a correction.

**Qualifying route:** Route A, category 3; category 2 also describes a possible digit substitution that changes magnitude. The diagnostic test check is supporting evidence, not a substitute for the reproduced category-3 comparison.

**Affected result or extracted value:** The protocol's historical Grade 3 BPD frequency and between-cohort comparison; extracting 31 versus an alternative count implied by the composite gives different risks.

**Why context does not resolve it:** Route A category 3 applies to counts within one display, including historical material. The neighboring composite suggests an alternative count but does not authorize silently replacing the printed numerator.

**Alternatives and missing definitions:** The numerator may differ from the value used for the printed percentage and P value, or the category/composite may use an unreported mapping. Exact chi-square implementation is not supplied. Both alternatives preserve the count–percentage conflict.

**Exact human question:** Which Grade 3 BPD surfactant count and corresponding percentage/test should be extracted from protocol Table 2: the printed 31/294, or the count used for the 20% and .02 display, and how does that count relate to the 91 Grade 3-or-death composite?

### F-ST1-1002

**Title:** Prespecified primary-outcome analyses have no corresponding result in the supplied report.

**Relationships:** S417, S423, S424, S435; P_R. **Focus area:** D. **Proposed review domain:** `protocol_report`.

**Exact locations and document roles:** PLAN [SAP PDF p29 §7.7](../../../joi250072supp3_prod_1761000786.6988.pdf#page=29) and [p38 §§9.4–9.4.2](../../../joi250072supp3_prod_1761000786.6988.pdf#page=38); REPORT [main article PDF p7, Table 2 and Sensitivity and Subgroup Analyses](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7), [p9 Figure 2](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=9), and REPORT [results supplement PDF pp1–16, eight eTables](../../../joi250072supp4_prod_1761000786.6988.pdf#page=1). The complete current results map was searched for each named analysis; no matching primary-outcome result is present.

**Printed statements and results:** SAP §9.4 explicitly calls the following analyses prespecified. §9.4.1 says the primary analysis will be replicated in mITT, PP and SAF to provide an as-treated treatment-effect assessment. §9.4.2 says known BPD baseline factors, e.g. birth weight, sex and race/ethnicity, will be included along with site/GA; an adjusted RR and 95% CI will be reported for the final model. §7.7 says heterogeneity by site/center will be investigated using treatment interactions. Main Table 2 supplies ITT RR 1.00 (0.90–1.11), ITT excluding untreated RR 1.00 (0.90–1.10), and PP RR 1.00 (0.90–1.11); its footnote expressly uses randomized treatment assignment for every population and adjusts for GA strata and pooled center. Main Figure 2 contains GA, chorioamnionitis, baseline FiO2, sex and race, but no site/center interaction result. The supplement's SAF tables provide AE and clinical/growth outcomes, without a primary BPD/death as-treated analysis or an expanded-covariate primary model.

**Rule and calculation:** Match required primary-analysis output by outcome, population, treatment assignment and adjustment. The treated-ITT row matches mITT but remains assigned-arm analysis, so it does not reproduce the distinct SAF as-treated specification. Adjustment for GA and center does not match the additional-baseline-factor model required in §9.4.2. Site/center adjustment does not supply the separately planned treatment-by-site/center interaction. This is a consolidated absence-of-prespecified-primary-analysis pattern, not a numeric recomputation; display precision is not applicable.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Primary BPD/death robustness to actual treatment, expanded baseline adjustment, and site/center effect heterogeneity.

**Why context does not resolve it:** Route A category 5 applies. The supplied plan separately and explicitly names these analyses; the existing mITT/PP models and covariate adjustment do not identify the missing outputs.

**Alternatives and missing definitions:** These analyses may have been performed but omitted, deferred, or superseded by an amendment not supplied. §9.4.2 permits selection when covariates are numerous, but still states that a final adjusted model will be reported. Site grouping is permitted for convergence, without making the analysis conditional on observed interaction. No additional model result, disposition of these analyses, or matching amendment is supplied.

**Exact human question:** Where are the prespecified primary BPD/death SAF as-treated result, additional-baseline-covariate adjusted RR/CI, and site/center interaction result, or what supplied amendment or disclosure explains their omission or replacement?

### F-ST1-1003

**Title:** The reported BPD-severity model differs from the specified ordinal model and its stated alternatives.

**Relationships:** S428, S429; P_R. **Focus area:** D. **Proposed review domain:** `protocol_report`.

**Exact locations and document roles:** PLAN [SAP PDF p39 §9.5](../../../joi250072supp3_prod_1761000786.6988.pdf#page=39); REPORT [main article PDF p8, Table 3, BPD severity rows and footnote a](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=8).

**Printed statements and values:** The SAP specifies proportional odds for ordinal BPD severity/grade, with partial proportional odds or Mantel–Haenszel mean-score test if that assumption fails; generalized logit is specified for nominal outcomes without inherent ordering. Main footnote a says ordinal outcomes report ORs estimated by logistic regression (generalized logit), with no BPD as reference. Pragmatic BPD grade 1/2/3 ORs are 0.87 (0.54–1.41), 0.88 (0.55–1.42), and 0.99 (0.51–1.89); the same generalized-logit footnote applies to NIH severity grade-specific ORs.

**Rule and calculation:** A nominal reference-category generalized-logit comparison produces separate category-versus-no-BPD treatment ORs. These are distinct model outputs from the SAP's specified ordinal proportional-odds analysis or its listed fallbacks. The report explicitly identifies both the ordinal outcome and generalized-logit implementation, so no model choice is inferred from numerical patterns. Display-precision arithmetic does not apply to a method substitution.

**Qualifying route:** Route B.

**Affected result or extracted value:** The category-specific BPD-severity ORs and their interpretation as evidence about the ordered severity outcome, particularly the prespecified secondary pragmatic BPD severity.

**Why context does not resolve it:** B1: the primary/secondary analysis specification comparison is in focus D. B2: neither the table nor supplied SAP explains why the ordered outcome used the separately specified nominal model. B3: cumulative ordinal ORs and category-specific ORs represent different comparisons, affecting extraction and interpretation. This observation does not question the internally coherent reported choice.

**Alternatives and missing definitions:** A disclosed amendment, assumption assessment, or an intended generalized-logit alternative may explain the change. Permission for additional ad hoc secondary analyses does not identify whether these results replace or supplement the specified ordinal analysis. The status and outputs of the planned ordinal model are not supplied.

**Exact human question:** Was the generalized-logit BPD-severity analysis an amendment, replacement, or additional analysis, and where is the specified proportional-odds or stated-fallback result and the explanation of its relationship to the category-specific ORs in Table 3?

### F-ST1-1004

**Title:** The displayed subgroup analysis changes the planned primary-outcome estimand and gestational-age grouping.

**Relationships:** S417, S420; P_R. **Focus area:** D. **Proposed review domain:** `protocol_report`.

**Exact locations and document roles:** PLAN [SAP PDF p29 §7.7](../../../joi250072supp3_prod_1761000786.6988.pdf#page=29) and [p36 §9.3, binary response coding](../../../joi250072supp3_prod_1761000786.6988.pdf#page=36); REPORT [main article PDF p9 Figure 2, title, caption and footnote a](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=9), with [p7 subgroup narrative](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7).

**Printed statements and values:** SAP §7.7 says treatment interactions will be added to the robust Poisson model for the primary outcome and defines GA group as used in randomization. §9.3 codes response 1 for BPD/death and 0 for alive without BPD. Figure 2 explicitly models the favorable outcome, alive without physiologic BPD, and footnote a uses actual best clinical GA regardless of randomization strata. The favorable overall result is 101/321 versus 102/318, RR 1.00 (0.81–1.24); GA <26 is 22/140 versus 22/130, RR 0.92 (0.54–1.58); GA ≥26 is 79/181 versus 80/188, RR 1.03 (0.82–1.30). The main primary adverse-composite RR is separately 1.00 (0.90–1.11).

**Rule and calculation:** Complementary binary outcomes share counts through (n-y), but their risk ratios are not equivalent estimands: (p_A/p_B) differs from ((1-p_A)/(1-p_B)), and robust-Poisson interaction fits do not become the same fitted analysis by relabeling the outcome. The reported GA grouping is expressly different from the specified randomization grouping. This comparison uses printed method and grouping definitions, not a crude-versus-adjusted estimate mismatch. Display precision is not applicable.

**Qualifying route:** Route B.

**Affected result or extracted value:** The planned heterogeneity analysis of the primary BPD/death treatment effect, and the GA-subgroup RR/interaction interpretation.

**Why context does not resolve it:** B1: prespecified primary analysis outcome and subgroup definition are focus D. B2: the favorable-outcome caption explains the displayed result but does not explain its relationship to the specified primary-outcome interaction analysis or the changed GA mapping. B3: the outcome coding and subgroup allocation determine the RR and interaction being extracted. The absence of a site/center result is recorded only in F-ST1-1002.

**Alternatives and missing definitions:** The favorable-outcome analysis may be additional, or may replace the prespecified adverse-outcome analysis; actual GA may be an intended amendment. No corresponding adverse-outcome interaction results, amendment, or mapping between randomization and clinical GA subgroup analysis is provided. The P-value test type in Figure 2 is not inferred from placement.

**Exact human question:** Does Figure 2 replace or supplement the specified primary BPD/death treatment-interaction analysis, and why were favorable-outcome coding and actual clinical GA used instead of the primary outcome and randomization GA groups in SAP §7.7?

## Excluded observations

Only apparent issues consciously not emitted are listed; successful checks are in the S completion records.

| Location | Observation | Reason code |
|---|---|---|
| REPORT results supplement p8 eTable 4 abbreviation line; S273 | “RR = risk difference” contrasts with the relative-risk heading and explicit binary-model paragraph; the immediate context identifies dimensionless relative risks at once, without altering a printed value. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p10 prior-trial description; S274 | Printed total 256 contrasts with arm counts 131+134=265. Half-unit total intervals have gap 7.5; 7.5/256=0.0293, screened by the specified 0.05 rule. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN protocol p10 prior-trial BPD/death; S274 | RR .58 differs from the crude ratio of 55/131 and 89/134; the supplied summary does not say the RR is crude, so no unreported analysis mapping is inferred. | MODEL_VERSUS_CRUDE |
| REPORT main p7 Table 2 versus PLAN SAP p37; S421 | Primary alpha .049 corresponds to 95.1% confidence while the table heading is 95%; the confidence-label difference is within display precision, without an interval–P conflict. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN SAP pp25,38; S406, S425 | The earlier sentence says a missing-data sensitivity will be performed; its explicit cross-reference leads to the >5% condition. The conditional provision resolves the apparent blanket requirement. | CONTEXT_RESOLVES |
| PLAN SAP pp17,24; S401, S404 | Numerical lambda and power simulation inputs/code are absent; no printed probability or achieved-power value is contradicted. | CONDITIONAL_OR_UNREPORTED |
| PLAN SAP pp29–30; S418 | Outside-window sensitivity is conditioned on arm differences; the supplied report does not establish that the trigger occurred. | CONDITIONAL_OR_UNREPORTED |
| PLAN SAP p43 versus REPORT supplied main/results displays; S434 | Planned Kaplan–Meier in-hospital-death curves are not displayed. This clinical safety summary is not a primary/key-secondary analysis and no reported mortality value or planned decision rule conflicts. | PERIPHERAL_COMPARISON |
| PLAN manual pp14,16 versus PLAN SAP pp3,33; S605 | The older severe-NDI example uses GMFCS 3–5 while the final SAP uses 4–5 and explicitly records finalized severe NDI after the Bayley-IV switch; the long-term follow-up is a later reporting stage. | CONTEXT_RESOLVES |
| PLAN manual pp130,148; S820, S828 | Majority is printed >90% in chapter 5 and ≥90% in Appendix J. Only the boundary symbol differs; the clinical majority rule is immediately recognizable, and no actual infant at the exact boundary or observed classification conflict is supplied. Screened conservatively under the instruction to exclude doubtful symbols. | NOTATION_OR_TYPOGRAPHY |
| PLAN manual p148; S828 | The printed “36 +1 weeks” notation sits beside exact-36-week screening and an explicit no-later-than-37-week challenge window. The timing meaning is resolved by the immediate paragraph without altering a trial value. | NOTATION_OR_TYPOGRAPHY |

## Limitations

No individual-level data, fitted covariance matrices, row-specific standard errors, simulation code, actual lambda, achieved conditional-power interval, or full information fractions for the actual interim looks are supplied. These limits prevent independent numerical reconstruction of the adjusted fits and actual stopping calculation; they do not themselves constitute findings. The main report permits recovering unused efficacy alpha after early termination through the supplied SAP, so .049 versus the full-design .044 is not treated as a contradiction. Count percentages in historical displays were checked using all printed input half-unit intervals; historical medians cannot reconstruct rank tests without the underlying distributions. No scientific S coverage gap remains in this shard.



---

# Statistical pass 1 completion — shard 1

Runtime agent ID: `/root/statistics_pass_1`; `gpt-6.1-sol` / `high`, fresh pass-1 spawn. Assigned scope: exactly the 120 IDs in `assigned_s_1.md`, S001–S048 and S201–S272. All source roles, populations, time points, treatment contrasts, models and footnotes were read with the assigned maps and relevant exact source renders. Finding details, exclusion reasons and limitations are in `checkers/parts/statistical_pass_1_1.md`. This status part is for coordinator merge; it does not alter another specialist's inventory.

Every result-row check includes point containment, endpoint order, effect direction, the available estimate/interval/P/test relation, stated decision rule, method identity, and the associated displayed numerator/denominator/percentage or summary. No unreported model, denominator, sidedness, covariance or test type is assigned. Where no numerical P/test/SE accompanies an effect, a synthetic P value is not treated as a reported result. The explicit completion status applies even when individual-data/model or interim inputs are unavailable.

| S ID | Pass 1 | Completed checks and source-grounded result | Finding references |
|---|---|---|---|
| S001 | PASS_1_COMPLETE | Primary composite: 220/321 and 216/318 percentages reconcile; 0.02 lies in −6.81–6.85, RR1.00 in .90–1.11; null/no-reduction interpretation agrees; abstract/Key Points/body match. Adjusted estimates not challenged by crude ratios. | F-ST1-002 |
| S002 | PASS_1_COMPLETE | Treated ITT: 218/319 and 215/315 percentages reconcile; RD−.31 and RR1.00 contained, intervals include null. Model N634 versus full treated N635 is the treated withdrawal with missing primary outcome. Randomized assignment is distinct from SAF assignment. | F-ST1-002 |
| S003 | PASS_1_COMPLETE | PP: 212/309 and 210/308 percentages reconcile, sum617; RD−.14 and RR1.00 contained with null intervals. Full641−6untreated−18major violations=617; source Table2 specifies randomized assignment. | F-ST1-002 |
| S004 | PASS_1_COMPLETE | Death49/321 and42/318 percentages reconcile; RD1.73 in−3.56–7.01, RR1.13 in.78–1.64; non-difference narrative agrees; copies match. | — |
| S005 | PASS_1_COMPLETE | BPD171/272 and174/276 percentages reconcile; denominators321−49=272,318−42=276; BPD+death reproduces primary events220/216. RD−.73 andRR.99 contained, null included. | — |
| S006 | PASS_1_COMPLETE | Pragmatic grade1 72/269,78/270 and reference70/269,66/270 percentages reconcile; OR.87 in.54–1.41 includes1; category contrasts match no-BPD reference. Planned ordinal/model distinction checked. | F-ST1-001 |
| S007 | PASS_1_COMPLETE | Pragmatic grade2 99/269,100/270 percentages reconcile; OR.88 in.55–1.42 includes1; same population/reference/model as grade1. | F-ST1-001 |
| S008 | PASS_1_COMPLETE | Pragmatic grade3 28/269,26/270 percentages reconcile; OR.99 in.51–1.89 includes1; complete category sums269/270. Distinct category OR from binary grade3 RR. | F-ST1-001 |
| S009 | PASS_1_COMPLETE | Binary grade3 repeats28/269,26/270; RD.69 in−4.34–5.71 andRR1.07 in.65–1.77 include null; OR in S008 is a different contrast, not a duplicate estimate conflict. | — |
| S010 | PASS_1_COMPLETE | Additional steroids102/318,109/311 percentages reconcile; RD−3.84 in−10.45–2.77 andRR.89 in.73–1.09 include null. Footnote restricts alive/in-hospital at seven days PLD. | — |
| S011 | PASS_1_COMPLETE | NIH grade1 70/270,57/270 and no-BPD29/270,27/270 percentages reconcile; OR1.13 in.59–2.17 includes1; NIH is distinct from pragmatic definition. | F-ST1-001 |
| S012 | PASS_1_COMPLETE | NIH grade2 32/270,45/270 percentages reconcile; OR.63 in.30–1.34 includes1; no-BPD reference and ordered NIH scale read. | F-ST1-001 |
| S013 | PASS_1_COMPLETE | NIH grade3 139/270,141/270 percentages reconcile; OR.87 in.47–1.63 includes1; category totals270/270; none of six severity contrasts excludes1. | F-ST1-001 |
| S014 | PASS_1_COMPLETE | IMV days before28: medians7(1–26),10(2–28) are ordered; adjusted least-squares MD−1.49 in−2.97–−.01, direction agrees with fewer-days narrative. Median difference is not the model MD; alive/in-hospital restrictions read. | — |
| S015 | PASS_1_COMPLETE | IMV days before36wk: medians10(1–36),13(2–37) ordered; MD−2.04 in−5.32–1.23 includes0; no day36 superiority claim. SAP explicitly permits continuous count modeling. | — |
| S016 | PASS_1_COMPLETE | Intubation after50h before28:192/312,206/302 percentages reconcile; RD−9.09 in−15.48–−2.69 andRR.87 in.78–.96 exclude null in same beneficial direction. | — |
| S017 | PASS_1_COMPLETE | Intubation after50h before36:195/301,211/295 percentages reconcile; RD−9.12 in−15.50–−2.73 andRR.87 in.79–.96 exclude null in same direction. Endpoint-specific missingness/restrictions read. | — |
| S018 | PASS_1_COMPLETE | Additional surfactant13/312,18/299 percentages reconcile; RD−1.87 in−5.29–1.55, relative.69 in.33–1.46 include null. Footnote explicitly identifies MH common OR approximation; no unlabeled OR/RR challenge. | — |
| S019 | PASS_1_COMPLETE | Hyperglycemia66.7%/49.8%, adjustedRR1.33 in1.17–1.51 supports increase. Matched eTable3 events214/156 and identical effect; actual-receipt population consistent. | — |
| S020 | PASS_1_COMPLETE | Any AE75.4%/64.5%, RR1.16 in1.05–1.28 supports reported difference; eTable3 counts242/202 and effect match. Header-based apparent percent differences below display threshold. | — |
| S021 | PASS_1_COMPLETE | PDA49.8%/56.8%, RR.86 in.75–.99 supports lower diagnosis frequency; eTable4 159/319,175/308 percentages/effect match. Composite and intervention-treated PDA contrasts correctly distinguished. | — |
| S022 | PASS_1_COMPLETE | 58%→48% is10percentage points andRR.827586 rounds.83;550×2=1100,1100/.95=1157.89 compatible approximate target1160; simulation details unavailable, no supplied conflicting simulation result. | — |
| S023 | PASS_1_COMPLETE | Reported first40/25%/50% milestones read against safety/efficacy/futility rules. Planned75% look was not reached after termination. No numerical interim treatment test supplied. | — |
| S024 | PASS_1_COMPLETE | 641/1160=55.2586% rounds55.3%; enrollment at termination is distinct from interim information milestone50%. Report says80% conditional-power CI below.50; actual endpoints unreported, no contradiction reproduced. | — |
| S025 | PASS_1_COMPLETE | Robust-Poisson fixed GA/center primary method agrees with protocol/SAP pooling options. Finalalpha.049 is compatible with SAP recovery of unused interim spending; exact actual spending inputs absent. Primary intervals include null. | — |
| S026 | PASS_1_COMPLETE | ITT efficacy and actual-receipt safety/clinical/growth assignments read; crossover treatment classification and full versus available-case populations distinguished. SAF primary sensitivity remains separately prespecified. | F-ST1-002 |
| S027 | PASS_1_COMPLETE | Binary robust-Poisson and MH/crude-OR fallbacks explicitly named; adjusted MD and continuous robust-count method read. Later SAP permits linear count model; no preferred-model criticism. | — |
| S028 | PASS_1_COMPLETE | Favorable overall101/321,102/318 percentages reconcile and complement primary220/216; RR1.00 in.81–1.24 includes1. Favorable RR distinguished from adverse composite RR despite same rounded point. | F-ST1-004 |
| S029 | PASS_1_COMPLETE | GA<26 favorable22/140,22/130 percentages reconcile; RR.92 in.54–1.58 includes1; favorable event/model and actual GA footnote read. | F-ST1-004 |
| S030 | PASS_1_COMPLETE | GA≥26 favorable79/181,80/188 percentages reconcile; RR1.03 in.82–1.30 includes1; GA subgroup sums reproduce overall events101/102 and denominators321/318. | F-ST1-004 |
| S031 | PASS_1_COMPLETE | No chorioamnionitis51/174,61/177 percentages reconcile; RR.91 in.68–1.21 includes1. Factor missing observations not assumed zero; source adjustment read. | — |
| S032 | PASS_1_COMPLETE | Chorioamnionitis45/129,38/127 percentages reconcile; RR1.12 in.81–1.55 includes1; known-factor subgroup totals smaller than ITT due missing factor information, not an internal total failure. | — |
| S033 | PASS_1_COMPLETE | BaselineFIO2<.50 favorable62/142,64/150 percentages reconcile; RR1.04 in.81–1.33 includes1; exploratory post-hoc status, baseline time and model read. | — |
| S034 | PASS_1_COMPLETE | BaselineFIO2≥.50 favorable19/86,13/81 percentages reconcile; RR1.35 in.72–2.51 includes1. Combined modelN459=641−182; source missing-baseline explanation read. | — |
| S035 | PASS_1_COMPLETE | Male44/158,50/162 percentages reconcile; RR.88 in.64–1.22 includes1; same favorable coding and adjusted model as Figure2 caption. | F-ST1-004 |
| S036 | PASS_1_COMPLETE | Female57/163,52/156 percentages reconcile; RR1.12 in.84–1.48 includes1; sex categories reproduce total events101/102 and denominators321/318. | F-ST1-004 |
| S037 | PASS_1_COMPLETE | Black40/101,43/122 percentages reconcile; RR1.18 in.86–1.63 includes1; maternal-race definition and adjusted favorable-outcome model retained. | F-ST1-004 |
| S038 | PASS_1_COMPLETE | White47/183,53/168 percentages reconcile; RR.84 in.61–1.15 includes1; counts do not assume race is complete for every ITT infant. | F-ST1-004 |
| S039 | PASS_1_COMPLETE | Other7/21,4/17 percentages reconcile; adjustedRR.93 in.33–2.66 includes1. CrudeRR differs/direction shifts, screened as model-versus-crude; source definition and adjustment explicit. | F-ST1-004 |
| S040 | PASS_1_COMPLETE | GA factorP.72 read in grouped position, not as either individual stratum treatment test; no CI/test significance conflict. Outcome/test mapping of planned interaction versus figure examined. | F-ST1-004 |
| S041 | PASS_1_COMPLETE | Chorioamnionitis factorP.35 read in grouped position; both subgroup intervals include1 and narrative no subgroup difference reconciles. Test type/df absent, not inferred. | — |
| S042 | PASS_1_COMPLETE | BaselineFIO2 factorP.45 read in grouped position; no null-significance conflict; subgroup explicitly described post hoc in discussion. Missing type/covariance not itself a finding. | — |
| S043 | PASS_1_COMPLETE | Sex factorP.28 grouped across strata, not individual effectP; both CIs contain1. Planned adverse-model versus favorable-display mapping examined without inventing test specification. | F-ST1-004 |
| S044 | PASS_1_COMPLETE | Race factorP.33 grouped across three categories, all CIs contain1; no df inferred. Planned adverse-model/favorable-display mapping examined. | F-ST1-004 |
| S045 | PASS_1_COMPLETE | Table2 full model/CI/population/oxygen-challenge footnotes read; adjusted RD/RR and randomized assignment identifiable. Nominal95% heading versus.049alpha screened for display precision, no CI-versus-P conflict. | — |
| S046 | PASS_1_COMPLETE | Table3 all footnotes/references/eligibility windows read; modeled MD versus medians and MH OR versus RR approximation clear. Source names generalized logit for ordered severity. | F-ST1-001 |
| S047 | PASS_1_COMPLETE | Figure2 all captions/footnotes, favorable coding, GA-specific center adjustment and factor-levelP positions read; planned subgroup interaction specification differs; site/center test absent. | F-ST1-002, F-ST1-004 |
| S048 | PASS_1_COMPLETE | All matched narrative conclusions agree with printed null/direction: no primary/components benefit, exploratory day28/intubation decrease, hyperglycemia increase and PDA decrease. No equivalence/NI claim; omitted primary analyses tracked separately. | F-ST1-002 |
| S201 | PASS_1_COMPLETE | Protocol primaryphysiologicBPD/death36wk, ITT and lower-incidence hypothesis match main primary definition/population/time and superiority direction; no margin claim. | — |
| S202 | PASS_1_COMPLETE | Protocol infant-level1:1 block-urn allocation, site×GA strata, independently randomized multiples and kit-opening definition agree with report. No cluster-level design assumed. | — |
| S203 | PASS_1_COMPLETE | Protocol secondarydeath36wk remains secondary/component in main;49/321 and42/318 and associated effects matched in S004. No outcome-status/time replacement. | — |
| S204 | PASS_1_COMPLETE | Protocol secondary physiologicBPD36wk matches main survivor analysis;171/272,174/276 and BPD definition read. No outcome-status/time replacement. | — |
| S205 | PASS_1_COMPLETE | Protocol ordered Jensen four-level severity remains stated secondary at36wk; cutoff-symbol observation screened, but ordered-model plan/report distinction persists. | F-ST1-001 |
| S206 | PASS_1_COMPLETE | Protocol grade3BPD36wk binary status matches main secondary28/269,26/270; pragmatic/Jensen terminology resolves, no count/interval failure. | — |
| S207 | PASS_1_COMPLETE | Protocol additional steroids from7daysPLDthrough36wk aligns report steroid endpoint and source survivor/in-hospital restriction; no threshold/window contradiction reproduced. | — |
| S208 | PASS_1_COMPLETE | Protocol secondaryNDI/death/composite22–26mo retained; SAP staged data locks explain later follow-up publication, and definition was prospectively delegated pendingBayley-IV transition. No status replacement inferred from this early-outcome report. | — |
| S209 | PASS_1_COMPLETE | Protocol exploratoryNIHseverity,ventilationdays28/36wk,intubationafter50h and surfactantafter50hto7daysPLD match main exploratory rows. Long-term wheeze/cough belongs later staged follow-up. | — |
| S210 | PASS_1_COMPLETE | AE7days/168h,SIP/PVL30days/720h,ICHgrace and growth36wk checked through complete safety definitions. Clinical120day outcomes distinguished from AE window; source-directed population/time logic read. | — |
| S211 | PASS_1_COMPLETE | Protocol primary robustPoisson/sandwichfixedNICU/GA matches report strata+pooled-center specification through protocol/SAP allowed pooling. Source offers computational alternatives, not evidence of omitted stratification. | — |
| S212 | PASS_1_COMPLETE | Protocol model families and SAP detailed alternatives checked. Generalized-logit severity differs from explicit ordinal plan; continuous ventilation counts permitted by SAP. | F-ST1-001 |
| S213 | PASS_1_COMPLETE | ITT efficacy/as-received safety align report. Prespecified primary SAF replication distinct from mITT randomized-assignment sensitivity and absent from reported effect displays. | F-ST1-002 |
| S214 | PASS_1_COMPLETE | Protocol missing-data details delegated to SAP before unmaskedreview; SAP available-case primary and >5%MI trigger applied to2/641=.312%. No unconditional imputation falsely imposed. | — |
| S215 | PASS_1_COMPLETE | All6Table5cells reproduced: alpha.044 raw n405.083/538.993/663.971→406/539/664; alpha.009 raw n592.791/752.780/899.295→593/753/900 at80/90/95%power. Formula [zαsqrt(2pbar(1−pbar))+zpower sqrt(.58×.42+.48×.52)]²/.10². Simulation550/arm not independently refitted;5%attrition target1160 compatible. | — |
| S216 | PASS_1_COMPLETE | Secondary descriptive rule agrees with report; fixed10point difference atcontrol>.58 moves pooledrisk farther above.5, decreasing paired-binomial variance under stated large-sample two-proportion power setup. No contradicted power assertion reproduced. | — |
| S217 | PASS_1_COMPLETE | SafetyPocock/Lan–DeMets milestone40/~3%,25/50/75% and printed.0033/.0196/.0212/.0214 boundaries read; actual-information dependence and earlyfit alternatives explicitly stated. No actual conflicting safety interimP supplied. | — |
| S218 | PASS_1_COMPLETE | EfficacyOF/Lan–DeMets.000015/.0030/.0183/final.044 at25/50/75/final read; actualinformation/priorlooks acknowledged. SAP explicitly allows recovered unused spending after earlystop; reportfinal.049 not contradicted by illustrative.044. | — |
| S219 | PASS_1_COMPLETE | Futilityupper80%CPbound fails>.50at50% or>.30at75% read; report50%criterion compatible, no actual CPendpoints printed. Discretionary slow-recruitment provision not used to invent a different stopping reason. | — |
| S220 | PASS_1_COMPLETE | AnyAE242(75.4)/202(64.5), RR1.16 in1.05–1.28; counts/percentage displayrule checked, favorable-to-harm direction matches main. Adjusted estimate not compared to crudeRR as contradiction. | — |
| S221 | PASS_1_COMPLETE | AnyAEofinterest240(74.8)/193(61.7), RR1.20 in1.09–1.33; counts belowanyAE242/202, displaypercentages compatible under rule; increase direction coherent. | — |
| S222 | PASS_1_COMPLETE | AEtubeblockage3(.9)/4(1.3), crudeOR.73 in.16–3.28 includes1; lowprevalence ORapproximation explicit, diagnosticWald endpoints replicated and statedexactCI method checked. | F-ST1-003 |
| S223 | PASS_1_COMPLETE | AEhypoxemia/bradycardia2(.6)/3(1.0), crudeOR.65 in.11–3.90 includes1; displayedpercentages checked; sparse exact-CI description versus replicatedinterval pattern examined. | F-ST1-003 |
| S224 | PASS_1_COMPLETE | AEairleak16(5.0)/18(5.8), adjustedRR.86 in.45–1.66 contains1; percentages reconcile under displayrule; not inferred crude. | — |
| S225 | PASS_1_COMPLETE | AEhypotension56(17.4)/59(18.8), RR.92 in.67–1.27 contains1; counts/percentages checked; sourcedefaultadjustment retained. | — |
| S226 | PASS_1_COMPLETE | AEhypertension28(8.7)/21(6.7), RR1.28 in.75–2.10 contains1; counts/percentages compatible. Confidence algorithm not inferred solely from interval asymmetry. | — |
| S227 | PASS_1_COMPLETE | AEhyperglycemia214(66.7)/156(49.8), RR1.33 in1.17–1.51 supports mainincrease; displayedpercentage intervals compatible even without substituting a denominator. | — |
| S228 | PASS_1_COMPLETE | AEICH40(12.5)/37(11.8), RR1.03 in.69–1.54 includes1; countpercentages checked, within7daywindow with source3dayultrasoundgrace distinguished. | — |
| S229 | PASS_1_COMPLETE | AEearlysepsis9(2.8)/8(2.6), RR1.06 in.41–2.75 includes1; countpercentage displayrule and defaultmodel checked; participant counts not mistaken for all-GDBevent counts. | — |
| S230 | PASS_1_COMPLETE | AElatesepsis70(22.4)/70(23.7), RR.93 in.70–1.24 includes1. Largest header-based percentgap1.09/23.7=.0459916≤.05; excluded under displayrule, denominator not inferred. | — |
| S231 | PASS_1_COMPLETE | AEPVL15(4.8)/13(4.3), RR1.09 in.52–2.26 includes1; count/header halfunit recomputations overlapprintedpercentages;30daywindow sourceexplicit. | — |
| S232 | PASS_1_COMPLETE | AESIP17(5.3)/9(2.9), RR1.82 in.83–4.02 includes1; percentages compatible;30daywindow and adjustedmodel retained. | — |
| S233 | PASS_1_COMPLETE | AEOther27(8.4)/32(10.2), RR.80 in.50–1.30 includes1; pulmonaryhemorrhage is subordinate category, not an extra disjointtotal; countpercentages checked. | — |
| S234 | PASS_1_COMPLETE | AEpulmonaryhemorrhage11(3.4)/14(4.5), RR.75 in.35–1.62 includes1; counts≤Other27/32 andpercentagescompatible; source subcategory relationship read. | — |
| S235 | PASS_1_COMPLETE | AEburdenmean1.6(SD1.5)/1.3(SD1.4), median1(1–2)/1(0–2), P.004 fromWilcoxon not meancontrast; noCI pairing. 500/321≈1.558 and403/313≈1.288 supportprintedmeans; ranks unavailable, nosyntheticP imposed. | — |
| S236 | PASS_1_COMPLETE | AnySAE64(19.9)/54(17.3), RR1.13 in.82–1.55 includes1; counts≤anyAE242/202, percentdisplaycheck supports noSAEdifference. | — |
| S237 | PASS_1_COMPLETE | AnySAEofinterest53(16.5)/42(13.4), RR1.20 in.83–1.73 includes1; counts≤anySAE64/54 andpercentdisplaycompatible. | — |
| S238 | PASS_1_COMPLETE | FatalSAE22(6.9)/25(8.0), RR.84 in.49–1.44 includes1; fatalities withinmonitoring or laterfromserious-window events perfootnote, distinct fromall120daydeaths50/44. | — |
| S239 | PASS_1_COMPLETE | SAEtubeblockage1(.3)/1(.3), crudeOR.98 in.06–15.66 includes1; percentdisplaycompatible; diagnosticWald.060718–15.656292 reproducesstatedexactinterval pattern. | F-ST1-003 |
| S240 | PASS_1_COMPLETE | SAEhypoxemia/bradycardia1(.3)/2(.6), crudeOR.49 in.04–5.39 includes1; percentdisplaycompatible, sparseinterval construction checked beyond symmetry. | F-ST1-003 |
| S241 | PASS_1_COMPLETE | SAEairleak5(1.6)/12(3.8), .37 in.13–1.06 includes1; footnote explicitly MHcommonOR stratifiedGA×center approximatingRR, no crudeOR substitution. | — |
| S242 | PASS_1_COMPLETE | SAEhypotension13(4.0)/8(2.6), RR1.53 in.64–3.63 includes1; percentagescompatible; same sourceadjustedmodel/timecontext. | — |
| S243 | PASS_1_COMPLETE | SAEhypertension0(0.0)/1(.3), NAcontrast explicitlyprinted; percentagezero consistent withzerocount, no CI/test manufactured forNA. | — |
| S244 | PASS_1_COMPLETE | SAEhyperglycemia8(2.5)/3(1.0), crudeOR2.64 in.69–10.05 includes1; logWald.694221–10.047884 reproduceslimits withlabeledavailable-denominator diagnostic. | F-ST1-003 |
| S245 | PASS_1_COMPLETE | SAEICH17(5.3)/19(6.1), RR.85 in.45–1.58 includes1; percentdisplaycompatible, SAEsubsetcounts≤AEICH40/37. | — |
| S246 | PASS_1_COMPLETE | SAEearlysepsis4(1.2)/2(.6), crudeOR1.96 in.36–10.79 includes1; percentagescompatible; repeatedexactCI/logWaldmethod question retained. | F-ST1-003 |
| S247 | PASS_1_COMPLETE | SAElatesepsis5(1.6)/2(.6), crudeOR2.46 in.47–12.78 includes1; percentagescompatible; repeatedexactCI/logWaldmethod question retained. | F-ST1-003 |
| S248 | PASS_1_COMPLETE | SAEPVL0(0.0)/0(0.0), NAcontrast; zerocount percentagesconsistent, no estimate/test forced. | — |
| S249 | PASS_1_COMPLETE | SAESIP15(4.7)/9(2.9), RR1.61 in.72–3.61 includes1; counts≤AE17/9, percentdisplaycompatible,30daymonitoringwindow explicit. | — |
| S250 | PASS_1_COMPLETE | SAEOther18(5.6)/20(6.4), RR.84 in.46–1.55 includes1; percentagescompatible; subordinatepulmonaryhemorrhage notadded asdisjoint. | — |
| S251 | PASS_1_COMPLETE | SAEpulmonaryhemorrhage8(2.5)/8(2.6), RR.94 in.35–2.48 includes1; counts≤Other18/20 andAE11/14, percentdisplaycompatible. | — |
| S252 | PASS_1_COMPLETE | SAEburdenmean.3(SD.6)/.3(SD.6), median0(0–0)/0(0–0), WilcoxonP.42;90/321≈.2804 and80/313≈.2556 supportroundedmeans. NoCI supplied, ranks unavailable. | — |
| S253 | PASS_1_COMPLETE | Death120day50/321(15.6)/44/313(14.1) percentagesreconcile; RR1.09 in.76–1.57 includes1; clinical120daydeath distinctfrom36weekendpoint; missing321 versusSAF322 explicitlynonmissingdenominator. | — |
| S254 | PASS_1_COMPLETE | NEC/death77/320(24.1)/72/313(23.0) percentagesreconcile; RR1.04 in.79–1.37 includes1; composite event totalswithincombineddeath/NEC bounds and distinct missingness allowed. | — |
| S255 | PASS_1_COMPLETE | NEC35/319(11.0)/40/308(13.0) percentagesreconcile; RR.85 in.56–1.29 includes1; death<12h/clinicalstatus exclusionsread, not forcedsame denominator asdeathcomposite. | — |
| S256 | PASS_1_COMPLETE | PDA/death182/320(56.9)/197/313(62.9) percentagesreconcile; RR.89 in.79–1.00 includesprintednullboundary; no compositebenefitclaim orP conflict. | — |
| S257 | PASS_1_COMPLETE | PDA159/319(49.8)/175/308(56.8) percentagesreconcile; RR.86 in.75–.99 excludes1 andmatchesmainlowerPDAclaim. Default robustPoisson adjustment retained. | — |
| S258 | PASS_1_COMPLETE | MedicalPDA/death121/316(38.3)/128/311(41.2) percentagesreconcile; RR.91 in.76–1.09 includes1; compositecount>=medicalevent countand<=event+death counts. | — |
| S259 | PASS_1_COMPLETE | MedicalPDA84/315(26.7)/98/306(32.0) percentagesreconcile; RR.80 in.64–1.01 includes1, consistentno treatedPDA difference. Missingdenominator explicit. | — |
| S260 | PASS_1_COMPLETE | Surgical/catheterPDA/death54/320(16.9)/47/313(15.0) percentagesreconcile; RR1.11 in.78–1.57 includes1. Combined5+50≥54 and3+44=47, composite logicalbounds hold. | — |
| S261 | PASS_1_COMPLETE | Surgical/catheterPDA5/319(1.6)/3/308(1.0) percentagesreconcile; crudeOR1.62 in.38–6.83 includes1. Fully specified2×2 OR1.618896/logWald.383560–6.832884 reproducesprintedlimits; diagnosticconditionalexact.311666–10.506504 differswellabovedisplayprecision. | F-ST1-003 |
| S262 | PASS_1_COMPLETE | Stage3ROP/death87/318(27.4)/83/310(26.8) percentagesreconcile; RR1.02 in.80–1.29 includes1; eventcountbounds37+50=87,40+44≥83compatible. | — |
| S263 | PASS_1_COMPLETE | Stage3ROP37/277(13.4)/40/270(14.8) percentagesreconcile; RR.87 in.60–1.28 includes1; observationdenominators distinctfromcomposite allowedbysourceclinicaltiming. | — |
| S264 | PASS_1_COMPLETE | WeightZ−1.1(SD.9)/−1.2(SD.8), adjustedMD.07 in−.08–.22 includes0; scale/timecorrect. AdjustedMD not forcedtocrude roundedmeandifference. | — |
| S265 | PASS_1_COMPLETE | Lowweight107/261(41.0)/113/259(43.6) percentagesreconcile; RR.95 in.78–1.15 includes1; growth36wk/populationrulesread. | — |
| S266 | PASS_1_COMPLETE | Lowweight/death155/309(50.2)/154/300(51.3) percentagesreconcile; RR.98 in.84–1.14 includes1. Counts107+48=155,113+41=154 anddenominators261+48=309,259+41=300reconcile. | — |
| S267 | PASS_1_COMPLETE | LengthZ−2.0(SD1.0)/−2.0(SD1.0), MD.04 in−.12–.21 includes0; nonzeroadjustedMDcompatiblewithroundedmeans, no crudecontrastimposed. | — |
| S268 | PASS_1_COMPLETE | Lowlength201/261(77.0)/201/259(77.6) percentagesreconcile; RR.99 in.90–1.08 includes1; samegrowthtime andsourcefixedadjustments. | — |
| S269 | PASS_1_COMPLETE | Lowlength/death249/309(80.6)/242/300(80.7) percentagesreconcile; RR1.00 in.93–1.08 includes1;201+48=249,201+41=242 andgrowthdenominatoradditionsreconcile. | — |
| S270 | PASS_1_COMPLETE | HCZ−1.5(SD1.0)/−1.6(SD1.0), MD.04 in−.132–.203 includes0; mixeddecimalprecisionretained, modeladjustedMD not challengedbycrude difference. | — |
| S271 | PASS_1_COMPLETE | LowHC141/261(54.0)/140/258(54.3) percentagesreconcile; RR1.00 in.85–1.16 includes1; differingnonmissingdenominators stated explicitly, not totalSAFheader. | — |
| S272 | PASS_1_COMPLETE | LowHC/death189/309(61.2)/181/299(60.7) percent intervalscompatible; RR1.01 in.89–1.14 includes1;141+48=189,140+41=181;261+48=309,258+41=299. For181/299printed60.7, halfunit recomputation[60.2671,60.8040]overlaps[60.65,60.75]. | — |

Summary: 120/120 assigned relationships `PASS_1_COMPLETE`; 4 findings; 8 excluded observations. No source-coverage gap. Mechanical limitations are the absence of individual data/covariance matrices, actual interim conditional-power/spending values, Figure 2 test mapping, each eTable 3 nonmissing denominator and the exact confidence-interval algorithm. No limitation is replaced by an assumed method or value. The coordinator merges these records into the canonical relationship inventory; a different fresh runtime agent must perform pass 2.


---

# Statistical pass 1 completion records — shard 2

Runtime agent ID: `/root/statistics_pass_1_2`; fresh `gpt-6.1-sol`/`high` spawn. Exact scope: S273, S274, S275, S276, S277, S278, S279, S401, S402, S403, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419, S420, S421, S422, S423, S424, S425, S426, S427, S428, S429, S430, S431, S432, S433, S434, S435, S601, S602, S603, S604, S605, S606, S607, S608, S609, S610, S611, S612, S613, S701, S801, S802, S803, S804, S805, S806, S807, S808, S809, S810, S811, S812, S813, S814, S815, S816, S817, S818, S819, S820, S821, S822, S823, S824, S825, S826, S827, S828, S829, S830, S831, S832, S833.

All 89 relationships have explicit PASS_1_COMPLETE records. Four findings are documented in `checkers/parts/statistical_pass_1_2.md`: F-ST1-1001 through F-ST1-1004. No new S IDs were necessary because every assigned relationship already has a stable source-linked S ID; their definitions are preserved in `statistics/parts/assigned_s_2.md`. Pass 2 requires a different runtime agent. No pass-2 status is assigned here.

The checks apply point-estimate containment, interval order, effect direction, interval/test logic where quantities exist; source-grounded methods and plan/report matching apply to all prospective relationships. “No observed estimate/test” is an applicability record, not an omitted check. No confidence level, sidedness, variance estimator, covariance, subgroup P-test type, denominator, or estimand was invented. Primary efficacy is superiority; no noninferiority or equivalence margin applies in this scope.

| S ID | Pass 1 | Applicability, source-grounded check and result |
|---|---|---|
| S273 | PASS_1_COMPLETE | REPORT DOC-005 p8: RR/MD labels, binary robust Poisson and continuous normal-identity least-squares difference are explicit. Abbreviation slip self-screened; modeled estimates are not compared to crude ratios. |
| S274 | PASS_1_COMPLETE | PLAN DOC-002 p10: historical RR/OR/NNT intervals ordered and contain their estimates; null/direction narratives agree. Prior arm-total and crude-RR observations self-screened. No stated test/SE permits a unique adjusted-fit reconstruction. |
| S275 | PASS_1_COMPLETE | PLAN DOC-002 p11 Table 1: all 14 descriptive rows and displayed P values checked. Counts and percentages meet the display rule; continuous/rank-test reconstruction lacks actual contributor counts/distributions, not inferred. |
| S276 | PASS_1_COMPLETE | PLAN DOC-002 p12 Table 2: all 22 rows, percentages, tests, support/category totals and footnotes checked. Grade 3 20% (31/294) and P .02 do not reconcile; F-ST1-1001. Other rows have no reproduced route-A conflict. |
| S277 | PASS_1_COMPLETE | PLAN DOC-002 p13 Tables 3–4: 16 morbidity and 16 discharge/growth rows checked. Counts/percentages reconcile within display rule. Rank statistics and time-specific contributor sizes absent; no test reconstruction from medians assumed. |
| S278 | PASS_1_COMPLETE | PLAN DOC-002 p14: historical SIP 13% versus 4%, P .02 has compatible direction; denominator/test/CI not supplied. Dose-ranging statements descriptive with no inferential comparison to reconstruct. |
| S279 | PASS_1_COMPLETE | PLAN DOC-002 p24: seven historical RR/CI/P triples checked for containment, order and null significance. All nonboundary triples agree; .86 (.75–1.00), P .05 is a printed boundary case, with no significant-versus-nonsignificant contradiction inferred. Adjusted methods/SE absent. |
| S401 | PASS_1_COMPLETE | PLAN SAP p17: block-urn allocation formula checked algebraically using allocation-count sum i−1. At balanced strata probability=1/2; at limiting imbalance arm probability=0 or 1. Lambda absent but no observed allocation contradicts it. |
| S402 | PASS_1_COMPLETE | PLAN SAP pp22,31: all-randomized ITT exception for the unconsented infant is explicit, along with SAF/mITT/PP. REPORT exclusion and randomized primary assignment match; complete-case primary denominators distinguish missing outcomes. |
| S403 | PASS_1_COMPLETE | PLAN SAP p23: six large-sample entries checked against stated 58%→48%, final alpha .044/.009 and power 80/90/95%. Diagnostic standard two-proportion expression yields about 539/arm at 90%, .044; simulation 550 distinct; 1100/.95=1157.89 rounds to planned 1160. No simulation-code inference. |
| S404 | PASS_1_COMPLETE | PLAN SAP p24: 33×2 strata imply maximum total imbalance 66 lambda and 550±33 lambda. Actual lambda and simulation unavailable; achieved 90% imbalance-power claim not independently reconstructed. |
| S405 | PASS_1_COMPLETE | PLAN SAP pp24–25: two-sided default, GA/site adjustment and continuous-model alternatives compared with REPORT main p3 and table footnotes. Site pooling and robust variance permitted; no coherent method choice challenged. |
| S406 | PASS_1_COMPLETE | PLAN SAP p25: available-case exclusion and MCAR/MAR sensitivity cross-reference checked against conditional >5% rule in p38. REPORT 2/641 primary missing=0.312%, below trigger; no automatic MI requirement inferred. |
| S407 | PASS_1_COMPLETE | PLAN SAP p25: masked investigator adjudication applies incomplete long-term NDI data. Two-stage locks and pending follow-up explain no corresponding current NDI result; no current estimate/test applies. |
| S408 | PASS_1_COMPLETE | PLAN SAP pp25–26: SAE-or-death SAF actual-treatment interim estimand, milestone and decision authority checked. Actual interim fit/result not supplied; no harmful-effect boundary conclusion is claimed. |
| S409 | PASS_1_COMPLETE | PLAN SAP p26: interim sparse-model options distinguish robust-Poisson RR from MH/Fisher OR. REPORT fallback disclosures are consistent in measure mapping; crude OR is not silently treated as fitted RR. |
| S410 | PASS_1_COMPLETE | PLAN SAP p26: four Pocock-type safety thresholds and two-sided .05 rule checked; exact boundaries explicitly depend on actual information/prior looks. No observed stopping statistic to compare. |
| S411 | PASS_1_COMPLETE | PLAN SAP pp26–27: 25/50/75% efficacy looks and OF boundaries checked; REPORT stops after 50% milestone. Final alpha recovery is explicitly allowed, so .049 versus full-design .044 is coherent. |
| S412 | PASS_1_COMPLETE | PLAN SAP pp3,26,37: revised recovery of unused interim alpha reconciles REPORT final .049 with full-design .044. Actual information/timing needed for independent spending reconstruction is absent. |
| S413 | PASS_1_COMPLETE | PLAN SAP p27: printed CP/80%-interval formula checked algebraically; Φ is monotone and plus/minus term orders limits. Formula simplification Z1/sqrt[f(1−f)]−Zalpha/sqrt(1−f) reproduces illustrative table under displayed quantile rounding. |
| S414 | PASS_1_COMPLETE | PLAN SAP pp27–28: all 16 illustrative Z1 rows at both information fractions checked; CP within bounds, CPU monotone. Diagnostic at f=.5,Z=.8 gives CP≈.107,CPU≈.515 using rounded quantiles, within display rule of .106/.513. Optional stopping CPU<.50/.30 matches approximate CP .10. |
| S415 | PASS_1_COMPLETE | PLAN SAP pp24,28–29,37: low-site/center pooling and convergence alternatives checked. REPORT seven-level pooled center fits specified pooling flexibility; no fixed-site versus pooled-center mismatch emitted. |
| S416 | PASS_1_COMPLETE | PLAN SAP pp23,29,39: one formal primary efficacy family, repeated-look adjustment, descriptive secondary intervals and possible selection P thresholds are consistent with REPORT interpretation; no unreported multiplicity procedure inferred. |
| S417 | PASS_1_COMPLETE | PLAN SAP p29: prespecified treatment interactions for primary BPD/death, randomization GA, race/sex/site checked against REPORT Figure 2. Site-result omission F-ST1-1002; favorable-outcome/actual-GA replacement F-ST1-1004. Figure P tests not inferred from row position. |
| S418 | PASS_1_COMPLETE | PLAN SAP pp29–30: allowed 36–37-week window and conditional outside-window sensitivity checked. Actual arm timing imbalance absent; no triggered sensitivity claimed missing. |
| S419 | PASS_1_COMPLETE | PLAN SAP p31: unadjusted baseline t/rank/chi-square choices are internally coherent and distinct from efficacy models. REPORT baseline summaries supply no efficacy inference requiring reconstruction. |
| S420 | PASS_1_COMPLETE | PLAN SAP pp36–37: log-link Poisson response, robust sandwich/GEE and fixed GA/site code produce adjusted adverse-outcome RR, not OR/RD. REPORT primary model agrees; subgroup complement contrast differs as F-ST1-1004. |
| S421 | PASS_1_COMPLETE | PLAN SAP p37: beta1=0 two-sided test, stage alpha and exponentiated interval logic coherent. No printed primary P/statistic/SE to reconstruct; 95% heading versus 95.1% confidence self-screened. |
| S422 | PASS_1_COMPLETE | PLAN SAP p37: individual-infant SUBJID/independent working correlation, reference coding and ITT filter checked against explicit independently randomized multiples. No cluster method preference proposed. |
| S423 | PASS_1_COMPLETE | PLAN SAP p38: primary-method replication mITT/PP/SAF matched to REPORT Table 2 and all supplement tables. mITT and PP present; distinct actual-treatment SAF primary result absent; F-ST1-1002. |
| S424 | PASS_1_COMPLETE | PLAN SAP pp24–25,38: required added BPD-factor primary robust-Poisson model and optional imbalance selection distinguished. REPORT models specify only GA/center and no matching expanded model; F-ST1-1002. |
| S425 | PASS_1_COMPLETE | PLAN SAP pp25,38–39: >5% MI trigger, minimum 10, M=100×missing fraction, separate fits and Rubin pooling coherent; 25% example→25. Current missing-primary rate below trigger; no gap alleged. |
| S426 | PASS_1_COMPLETE | PLAN SAP p39: secondary binary ITT robust-Poisson fixed strata model matches REPORT death/BPD component models and survivor/nonmissing denominators. |
| S427 | PASS_1_COMPLETE | PLAN SAP p39: continuous fixed-strata linear-regression model matches REPORT normal-identity adjusted MD; least-squares MD need not equal differences between printed medians. |
| S428 | PASS_1_COMPLETE | PLAN SAP p39: proportional/partial-proportional/MH ordinal alternatives compared to explicit REPORT generalized-logit severity ORs. Model replacement F-ST1-1003; no preferred method advocated. |
| S429 | PASS_1_COMPLETE | PLAN SAP p39: nominal generalized-logit/association fallback defined separately from ordinal model. REPORT uses generalized-logit for severity; same F-ST1-1003, not another finding. |
| S430 | PASS_1_COMPLETE | PLAN SAP p39: count Poisson/dispersion/zero-inflated options and permitted continuous approximation checked; REPORT robust continuous count analysis fits allowed choice, with no normality assumption inferred. |
| S431 | PASS_1_COMPLETE | PLAN SAP pp39–40: SAF as-treated binary RR and missing-data handling match REPORT safety tables; optional PP safety repeat depends on violations affecting safety, which source does not establish. |
| S432 | PASS_1_COMPLETE | PLAN SAP p40: site-random/MH/Fisher safety fallback and OR reporting checked against REPORT disclosures. No method-generated result compared as though crude. |
| S433 | PASS_1_COMPLETE | PLAN SAP pp40,42: participant experience versus event-number summaries, onset and fatal/non-SAE-death distinctions checked against results eTables 2–3,6–8. No event count equated to participant numerator. |
| S434 | PASS_1_COMPLETE | PLAN SAP pp43–44: clinical death censoring/growth composites checked against REPORT eTable 4; stage-3 ROP specified explicitly in SAP matches table. Growth death additions and nonmissing denominators coherent. Unshown KM is peripheral clinical summary. |
| S435 | PASS_1_COMPLETE | PLAN SAP pp45,48: no protocol-impacting analysis changes assertion and conditional display-list flexibility checked. Required primary text analyses, not merely potential display formats, ground F-ST1-1002. |
| S601 | PASS_1_COMPLETE | PLAN manual pp7,11,22: randomized 1:1 site/GA strata, independent multiples and 1160 target match REPORT design. 580 planned/arm distinguished from actual unequal accrual; no randomization-level contradiction. |
| S602 | PASS_1_COMPLETE | PLAN manual pp12,25,28: opened-kit randomization and records for untreated infants agree with REPORT enrolled/treated distinction. Unconsented infant exclusion explicitly supplied; unopened-kit inventory not a participant count. |
| S603 | PASS_1_COMPLETE | PLAN manual pp14,52: primary physiological BPD/death and separate Jensen assessment agree with REPORT outcome hierarchy; routed physiological appendix inspected through S817–S832. |
| S604 | PASS_1_COMPLETE | PLAN manual pp8,14: component, Jensen, grade-3, steroid and long-term secondary statuses matched; pending long-term stage disclosed in SAP. No unperformed future stage treated as omitted current primary analysis. |
| S605 | PASS_1_COMPLETE | PLAN manual pp14,16: severe-NDI alternative components and provisional agreement statement compared with finalized SAP revision. Earlier GMFCS 3–5 versus final 4–5 self-screened as disclosed endpoint-finalization context. |
| S606 | PASS_1_COMPLETE | PLAN manual pp14–15: exploratory NIH severity, ventilation/intubation/repeat-surfactant windows match REPORT Table 3. Report distinguishes living/in-hospital contributors and descriptive analysis; no window value contradicted. |
| S607 | PASS_1_COMPLETE | PLAN manual pp15,35,38: treated safety forms, 168-h window and 30-day SIP/PVL match REPORT supplement definitions. Actual treatment distinguished from ITT efficacy. |
| S608 | PASS_1_COMPLETE | PLAN manual pp38–40: event-specific repeated thresholds/conjunctions read and matched to REPORT hyperglycemia and AE definitions. No actual safety value contradicts thresholds; AE severity is not confused with seriousness. |
| S609 | PASS_1_COMPLETE | PLAN manual pp41–42,44: continuous episode highest grade, recurrence separation, serious grades and relatedness checked against REPORT participant/event displays. No summation assumes mutually exclusive unexpected/interest categories. |
| S610 | PASS_1_COMPLETE | PLAN manual pp30–32: repeated collection/tolerances/measurement preference and permanent-missing versus not-expected fields coherent; no analysis imputation rule inferred from collection instructions. |
| S611 | PASS_1_COMPLETE | PLAN manual pp53–54: withdrawal/discontinuation and retained prior data distinguish treatment cessation from study withdrawal. REPORT complete outcome counts consistent; absent outcome-handling formula supplied separately by SAP. |
| S612 | PASS_1_COMPLETE | PLAN manual p16: periodic DSMC review statement carries no numeric rule; detailed SAP formal rules supply those definitions. REPORT 50% futility rule checked through S414. |
| S613 | PASS_1_COMPLETE | PLAN manual pp7,12–13,50–51: birth-weight budesonide .25 mg/kg, two doses≤50h and concomitant restrictions match REPORT treatment; deviation codes do not themselves specify PP exclusion. |
| S701 | PASS_1_COMPLETE | PLAN manual p62: all-randomized physiological BPD/death by 36 weeks and GDB routing agree with REPORT primary composite; no estimate/test printed on this operational page. |
| S801 | PASS_1_COMPLETE | PLAN manual pp109–111: cystic versus noncystic lesion definitions, closest-36-week imaging and laterality distinguish cPVL from other cysts. MRI PCA/PMA wording immediately recognizable; no observed denominator/estimate conflict. |
| S802 | PASS_1_COMPLETE | PLAN manual p111: first full-enteral date uses current-weight 120 ml/kg/day; explicit unit/threshold internally coherent. No corresponding inferential value printed. |
| S803 | PASS_1_COMPLETE | PLAN manual pp111–112: first-28-day milk/fortification/probiotic exposure definitions checked; generic trial coding does not specify a BiB treatment dose or effect. |
| S804 | PASS_1_COMPLETE | PLAN manual pp112–113: proven NEC Bell IIA or above, surgery/autopsy and first-date rules checked against S824 and REPORT clinical NEC; stage1 not included as proven. |
| S805 | PASS_1_COMPLETE | PLAN manual p113: spontaneous perforation excludes NEC and remains separate from short gut; REPORT SIP versus NEC clinical outcomes accordingly distinguished. |
| S806 | PASS_1_COMPLETE | PLAN manual pp113–114: hearing screen, diagnostic ABR, loss and laterality before status are distinct fields; not substituted for long-term severe-NDI hearing endpoint. |
| S807 | PASS_1_COMPLETE | PLAN manual pp114–116: ROP stage/zone/plus and status-treatment rules coherent. Generic severe-status category differs from SAP explicit stage3 clinical outcome by definition, not a matching-result conflict. |
| S808 | PASS_1_COMPLETE | PLAN manual p117: clinical AKI/HTN field differs from adverse-event repetition/severity thresholds; no numerical AKI threshold supplied here and no reported value assumed to use one. |
| S809 | PASS_1_COMPLETE | PLAN manual pp118–119: early≤72h/late>72h, ≥5-day antibiotics and episode rules coherent. GDB infections and AE severity >5-day criteria address distinct coded purposes; no matched statistic falsely compared. |
| S810 | PASS_1_COMPLETE | PLAN manual pp119–120: UTI≥5-day, meningitis≥7-day/intended-course and LP definitions coherent; paper-entry versus EDC capacity differs explicitly, not participant counts. |
| S811 | PASS_1_COMPLETE | PLAN manual pp121–123: ≤12-hour early-death form is generic collection, not trial eligibility or mortality-analysis denominator. Cause finalization can lag submitted record; no contradiction. |
| S812 | PASS_1_COMPLETE | PLAN manual p122: masked-trial T exposure code preserves concealment and points to trial rules; no dose/group assignment imputed from code alone. |
| S813 | PASS_1_COMPLETE | PLAN manual pp123,127: single contributory death cause grounded in proximate disease and clinical/autopsy evidence; REPORT primary death is all-cause, so causes not treated as components of a different death estimand. |
| S814 | PASS_1_COMPLETE | PLAN manual pp123–124,126–127: >120-day late-form population and seven-day transfer return convention distinct from current trial clinical outcomes through GDB status; no analysis population enlarged from generic late records. |
| S815 | PASS_1_COMPLETE | PLAN manual pp124–126: post120-day ROP/hearing/care fields are later generic follow-up, not current 36-week endpoints; no reported inferential result to pair. |
| S816 | PASS_1_COMPLETE | PLAN manual pp126–127: home-oxygen/discharge medication fields and masked Trial coding coherent; inhaled versus systemic steroids not conflated with randomized dose. |
| S817 | PASS_1_COMPLETE | PLAN manual p128: Jensen general definition routing explicitly excepts trials using physiology; BiB primary physiology and secondary Jensen therefore agree, with no primary status replacement. |
| S818 | PASS_1_COMPLETE | PLAN manual pp128–129: highest-mode hierarchy, fixed snapshots/highest oxygen, temporary-increase/feed exclusions and endpoint support dates coherent. Day counts obey 4+2+1=7 example; no person-time rate inferred. |
| S819 | PASS_1_COMPLETE | PLAN manual pp130–131: mode5/6 challenge selection, effective versus actual oxygen and threshold strata align REPORT Table2 note and AppendixJ; documented not-performed reasons not assumed missing-at-random. |
| S820 | PASS_1_COMPLETE | PLAN manual p130: majority>90% reading boundary compared with AppendixJ≥90%; doubtful boundary-symbol observation self-screened and explicitly listed, not hidden. |
| S821 | PASS_1_COMPLETE | PLAN manual pp137–139: etiologic death categories and subtypes checked against single-cause coding; none redefine the all-cause primary death component. |
| S822 | PASS_1_COMPLETE | PLAN manual p139: renal stage3 chart lists SCr and urine columns with absent footnote definitions/operator. No reported renal result or decision conflicts; no AND/OR or reference-SCr value inferred. |
| S823 | PASS_1_COMPLETE | PLAN manual p140: ROP schematic stages/zones/extent are classification labels, not observed trial counts or severity-group distributions. |
| S824 | PASS_1_COMPLETE | PLAN manual p144: all Bell stage rows checked; IIA definite NEC matches clinical threshold and IIIB perforation distinct from spontaneous non-NEC perforation. |
| S825 | PASS_1_COMPLETE | PLAN manual p145: generic major-malformation categories/exclusions checked; no independent analysis-exclusion rule inferred, and no randomized size contradicted. |
| S826 | PASS_1_COMPLETE | PLAN manual p146: all four infection/NEC rows use positive culture and proven NEC separately with ≥5-day antibiotics; logical four-cell classification coherent. |
| S827 | PASS_1_COMPLETE | PLAN manual p147: histologic chorioamnionitis definitions distinct from REPORT combined clinical-or-histologic subgroup; combined label is explicit and no input-count mismatch follows. |
| S828 | PASS_1_COMPLETE | PLAN manual p148: explicit BiB physiology, screening36wk/challenge≤37wk, effective-oxygen rules and room-air cannula eligibility coherent. 36+1 and majority boundary symbols self-screened as noted. |
| S829 | PASS_1_COMPLETE | PLAN manual p149: oxygen/flow reduction steps, preparation and failure criteria checked; continuation/failure operational rules do not supply actual patient-result estimates. |
| S830 | PASS_1_COMPLETE | PLAN manual p150: 30-minute pass, 15-minute rapid pass, sustained<90% or short<80% failure and return-to-baseline instructions checked; no point estimate or CI applies. |
| S831 | PASS_1_COMPLETE | PLAN manual pp152,154–155: lookup/nearest-value/midpoint-up method checked; 2kg,.15lpm→factor8 and 100% source oxygen→effective27% reproduces example. No unprinted algebraic oxygen formula assumed. |
| S832 | PASS_1_COMPLETE | PLAN manual pp156–158: every worksheet repeated reduction/stop/rapid-pass rule checked against pp149–150; minute grids are blank collection forms, not participant denominators. |
| S833 | PASS_1_COMPLETE | PLAN manual p162: Jensen grade0/1/2/3, ≤2 versus >2 lpm, noninvasive versus invasive criteria checked against SAP ordinal endpoint and REPORT severity labels; primary physiology routing remains distinct. |

## Diagnostic calculation details

For sample size S403, the source states a large-sample two-proportion method and separately robust-Poisson simulation. Using the former, (n=[z_{.978}\sqrt{2\bar p(1-\bar p)}+z_{.90}\sqrt{.58(.42)+.48(.52)}]^2/.10^2\), with \(\bar p=.53\), gives about 539 per arm. The other five displayed entries are consistent with changing final alpha and power. These normal approximations are diagnostics; the simulation's code, distribution of covariates and allocation imbalance parameter are absent. 1100/(1−.05)=1157.89, consistent with approximately5% attrition and target1160.

For S413–S414, simplifying the stated CP expression yields (CP=\Phi[Z_1/\sqrt{f(1-f)}-Z_\alpha/\sqrt{1-f}]\) and (CPU=\Phi[Z_1/\sqrt{f(1-f)}-Z_\alpha/\sqrt{1-f}+Z_\gamma\sqrt{(1-f)/f}]\). The table has16 rows for each f=.5/.75, with CP and CPU. The rounded quantile values2.01/1.28 have their own half-unit intervals; small reconstructed differences do not exceed the display rule. No actual CP estimate, 80% bound, interim information fraction or actual test statistic is supplied for independent verification of the stopping calculation.

For S274–S279 historical studies, point estimates lie within all printed intervals and limits increase. No interval excludes the null alongside a stated nonsignificant test, or vice versa. S276's Grade3 count/percentage conflict and corresponding diagnostic test are emitted even though the table is historical. The printed .86 (.75–1.00), P=.05 is a boundary triple rather than an opposite-significance claim.

## Evidence and limits

Fresh current maps used: `extraction/parts/protocol_results.md`, `extraction/parts/sap.md`, `extraction/parts/sap_025_048.md`, `extraction/parts/manual_001_054.md`, `extraction/parts/manual_055_081.md`, `extraction/parts/manual_109_162.md`, `extraction/parts/results_001_016.md`, `extraction/main_statistics_01.md` and the main quantitative-context map. All cited findings were visually confirmed in source-linked rendered PDF pages. OCR-only omissions were not treated as source omissions. Historical source images and native text were reused strictly as evidence assets, with no old scientific conclusions read. No source files or shared canonical inventories were edited. No scientific relationship gap remains; numerical fitted-model reconstruction is limited by absent individual data, covariance matrices and simulation/interim inputs.

