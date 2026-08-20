# Statistical Consistency Review — PASS 1

## Scope and method

PASS 1 reviewed every stable relationship in `statistics/relationship_inventory.md` (`S001-S054`).  For each applicable result it checked estimate containment and endpoint ordering; sign/direction and effect-measure/scale labels; repeated/cross-location values; and interval/P/SE compatibility only where the supplied definition permits it.  This repair adds the protocol and analysis-plan rules from DOC-002, DOC-003, and eAppendix 7.  Rounding, effect coding, multiple imputation, different analysis populations, and prospective-versus-reported status were retained rather than silently treated as mismatches.  Candidate observations below have no `C` identifier and remain pending human adjudication.

| Stable ID | PASS 1 check record | Status |
|---|---|---|
| S001 | Model labels are internally coherent: logistic primary model, effect coding, site/history adjustment, 100 imputations, and Rubin pooling are stated.  No estimate/interval is printed here to test.  Missing: imputation variables and precise logistic parameterization. | PASS_1_COMPLETE |
| S002 | Cox/HR label, event-or-last-measurement time rule, and PH statement are coherent.  The omnibus `P>.05` does not identify an individual test statistic; no further compatibility calculation is defined. | PASS_1_COMPLETE |
| S003 | GEE/ANCOVA, baseline adjustment, time points, two-sided `.05` threshold, and no-MI sensitivity label are coherent.  Missing: working-correlation estimate and individual test details. | PASS_1_COMPLETE |
| S004 | All ORs are positive, lie within ordered CIs, and have null value 1 in their CIs consistently with non-small P values.  The abstract, Table 2, and Results repeat all three OR/CI pairs; the abstract prints only the interaction P value, while Table 2 and Results print all three P values.  OR labels and the effect-coded model agree. | PASS_1_COMPLETE |
| S005 | All HRs are positive, lie within ordered CIs, and have null value 1 in their CIs consistently with reported P values.  Table 2 and Results match; HR/person-month time-to-event labels agree. | PASS_1_COMPLETE |
| S006 | PHQ B values lie in ordered CIs; positive direction is consistent with worse PHQ for supplements.  P values are compatible with CIs excluding 0.  Narrative 2× translations reproduce Table 3 under its explicit rule. | PASS_1_COMPLETE |
| S007 | PHQ F-BA B values lie in ordered CIs containing 0; P values exceed .05.  Negative direction denotes lower/worse-score reduction under the stated PHQ scale.  No label conflict. | PASS_1_COMPLETE |
| S008 | IDS B values lie in ordered CIs; only overall CI excludes 0 and its P=.01 is compatible.  Positive direction/IDS scale and Table 3 labels agree. | PASS_1_COMPLETE |
| S009 | IDS F-BA B values lie in ordered CIs containing 0; P values exceed .05.  Negative direction is scale-consistent. | PASS_1_COMPLETE |
| S010 | GAD B values lie in ordered CIs; overall CI excludes 0 with P=.004, T12 contains 0 with P=.13.  Positive direction and GAD scale agree. | PASS_1_COMPLETE |
| S011 | GAD F-BA overall CI includes 0/P=.06; T12 CI excludes 0/P=.01.  Negative B means lower GAD under stated scale.  Narrative translation is consistent after effect-code multiplier. | PASS_1_COMPLETE |
| S012 | Utility B values lie in ordered CIs.  Overall interval ends at printed `.000` and P=.052, compatible with rounding around null; T12 contains 0/P=.61.  Negative direction is lower utility under stated scale. | PASS_1_COMPLETE |
| S013 | Utility B values lie in ordered CIs containing 0; P=.44/.23 is compatible.  Positive direction denotes higher utility. | PASS_1_COMPLETE |
| S014 | The reported interaction-P range `.41-.98` is only a range, without individual coefficients or tests.  Its all-above-.05 description agrees with the stated no-significant-interaction conclusion.  Missing: individual interaction results. | PASS_1_COMPLETE |
| S015 | Each narrative adjusted difference and CI is twice the Table 3 effect-coded coefficient/CI at displayed precision; P values match.  This is an expressly defined conversion, not a cross-scale mismatch. | PASS_1_COMPLETE |
| S016 | CACE F-BA OR `.78` is within ordered `.64-.95` CI and is identical to DOC-004 S036.  Main text does not print P/model detail needed for further compatibility. | PASS_1_COMPLETE |
| S017 | Both PHQ B values lie within ordered CIs containing 0 and have P=.841/.203.  B label and PHQ direction are coherent. | PASS_1_COMPLETE |
| S018 | Each site B lies within its ordered CI containing 0 and has P=.168/.405/.468.  Netherlands reference label is explicit; no direction conflict. | PASS_1_COMPLETE |
| S019 | History PHQ B and baseline-PHQ B both lie in ordered CIs excluding 0 and have P=.036/<.001.  Signs and PHQ scale are coherent. | PASS_1_COMPLETE |
| S020 | Both interaction Bs lie in ordered CIs; F-BA×baseline PHQ excludes 0/P=.020 and supplement interaction contains 0/P=.259.  Narrative direction matches the negative F-BA interaction under higher=worse PHQ. | PASS_1_COMPLETE |
| S021 | GAD main-effect Bs lie in ordered CIs containing 0; P=.45/.703 is compatible.  Sign and GAD direction labels agree. | PASS_1_COMPLETE |
| S022 | All GAD site Bs lie in ordered CIs containing 0 with P=.694/.637/.804.  Reference label and directions are coherent. | PASS_1_COMPLETE |
| S023 | History and baseline-GAD Bs lie within ordered CIs; history contains 0/P=.102, baseline excludes 0.  The printed baseline-GAD `P=0` is recorded separately below because it is not a valid literal probability display. | PASS_1_COMPLETE |
| S024 | F-BA×baseline-GAD CI contains 0/P=.554; supplements×baseline-GAD CI excludes 0/P=.022.  Direction agrees with the narrative statement of higher follow-up anxiety at higher baseline severity. | PASS_1_COMPLETE |
| S025 | Utility main-effect Bs lie in ordered CIs containing 0; P=.952/.313 is compatible.  B and utility-scale labels are coherent. | PASS_1_COMPLETE |
| S026 | Utility site Bs lie in ordered CIs containing 0; P=.548/.097/.198 is compatible.  Netherlands reference is explicit. | PASS_1_COMPLETE |
| S027 | Utility history CI contains 0/P=.148; baseline CI excludes 0/P<.001.  Signs and higher-is-better utility direction agree. | PASS_1_COMPLETE |
| S028 | F-BA×site CIs/order and P values agree: only UK excludes 0 and has P=.041.  Positive UK interaction matches the narrative statement that the F-BA utility effect is larger in UK than Netherlands. | PASS_1_COMPLETE |
| S029 | All supplements×site CIs contain 0 and P values are .499/.907/.850.  Labels/reference and directions are coherent. | PASS_1_COMPLETE |
| S030 | UK subgroup CIs/order and P values agree: F-BA `.013 (.001-.024), .033` and baseline utility `.738 (.62-.856), <.001` exclude 0; remaining terms contain 0. | PASS_1_COMPLETE |
| S031 | Netherlands subgroup CIs/order and P values agree: baseline utility excludes 0/P<.001; all other CIs contain 0 with P>.05.  The repeated `C2` heading is a display label, not an inferential inconsistency by itself. | PASS_1_COMPLETE |
| S032 | No-MI PHQ overall CIs/Ps are compatible.  T12 B/SE diagnostic ratios are approximately 2.55, 2.00, and .18, compatible with displayed P=.013/.052/.84 after robust-model/rounding allowance.  Model/time labels distinguish this from imputed Table 3. | PASS_1_COMPLETE |
| S033 | No-MI IDS overall CIs/Ps are compatible.  T12 B/SE ratios are about 1.00, -1.29, and .43, compatible with P=.30/.20/.66 at displayed precision. | PASS_1_COMPLETE |
| S034 | No-MI GAD overall CIs/Ps are compatible.  T12 B/SE ratios are about 1.89, -2.89, and .33, compatible with P=.07/.005/.74 after robust-model/rounding allowance. | PASS_1_COMPLETE |
| S035 | No-MI utility overall CIs/Ps are compatible.  T12 B/SE ratios are about -.33, 1.33, and .33, compatible with P=.66/.23/.65; unit is the stated 0-1 utility scale. | PASS_1_COMPLETE |
| S036 | CACE ORs are positive and contained in ordered CIs.  F-BA CI excludes 1 and is marked `*`; supplement CI includes 1 and is unmarked.  Main-text S016 repeats the F-BA value exactly. | PASS_1_COMPLETE |
| S037 | CACE PHQ Bs lie within ordered CIs.  Supplement CI excludes 0 and is marked `*`; F-BA CI contains 0 and is unmarked.  B/ANCOVA and PHQ labels are coherent. | PASS_1_COMPLETE |
| S038 | CACE IDS Bs lie within ordered CIs containing 0 and are unmarked.  B/ANCOVA and IDS labels are coherent. | PASS_1_COMPLETE |
| S039 | CACE GAD Bs lie within ordered CIs.  F-BA CI excludes 0 and is marked `*`; supplement CI contains 0 and is unmarked.  Direction agrees with lower GAD for negative B. | PASS_1_COMPLETE |
| S040 | Omnibus `P<.001` matches the identical main-text citation.  Test identity, degrees of freedom, and exact comparison rule are absent, so no calculation is applicable. | PASS_1_COMPLETE |
| S041 | The protocol clearly labels pooled ITT main analyses, supplementary per-protocol analyses, and baseline tests.  The published primary model retains randomization-group analysis; no per-protocol result is printed to compare. | PASS_1_COMPLETE |
| S042 | The protocol's Cox/HR time-to-event rule is compatible with S002/S005.  Kaplan-Meier/log-rank outputs and a separate four-way result are not printed, so no repetition or compatibility calculation applies. | PASS_1_COMPLETE |
| S043 | The protocol describes an additional mixed model for MDD/IDS, whereas the supplied analysis plan and article describe logistic/GEE analyses.  The protocol does not state that no later analysis plan or amendment may change the model; no source-supported inconsistency is inferred. | PASS_1_COMPLETE |
| S044 | The protocol lists broad secondary-outcome mixed models and country clustering but prints no estimate, interval, or P value.  The article's reported GEE outcomes are separately labelled; no direct same-result conflict is available. | PASS_1_COMPLETE |
| S045 | Bootstrapped mediation and blood-subgroup regression are planned without printed result values in the supplied report.  Their nonappearance is not converted into a candidate. | PASS_1_COMPLETE |
| S046 | Protocol effect-modification variables and model families are explicit.  They are prospective rules rather than repeated reported estimates; no compatible statistic is printed for a containment/P check. | PASS_1_COMPLETE |
| S047 | The analysis-plan effect-coded logistic/OR/CI/P rule agrees with the reported primary logistic model and S004.  Labels, null value, and interaction structure are coherent. | PASS_1_COMPLETE |
| S048 | The analysis plan permits mixed models or GEE and specifies coefficient/CI/P reporting.  The reported Table 3 GEE/robust-regression coefficients satisfy those labels; its point Cohen d values are not presented as the plan's standardized-difference CIs, so no unreported CI is inferred. | PASS_1_COMPLETE |
| S049 | Direct visual confirmation shows the printed sentence `the 2-sided significance threshold will be set at p 0.05`.  It contains no `<`, `<=`, `=`, or other comparison operator; the threshold therefore cannot be mechanically applied as printed.  Candidate observation emitted below. | PASS_1_COMPLETE |
| S050 | The plan distinguishes multiplicative logistic interaction from additive RERI sensitivity analysis and supplies no RERI result.  The article's reported logistic interaction is not mislabeled as RERI. | PASS_1_COMPLETE |
| S051 | The planned Cox HR/CI/P output agrees with the reported post hoc Cox block S005.  Estimates lie in ordered CIs and all displayed labels are HR rather than risk or count. | PASS_1_COMPLETE |
| S052 | Planned history/centre logistic interaction rules are distinguishable from the article's reported secondary-outcome modifiers.  No individual primary-outcome modifier statistic is printed that would permit an unsupported discrepancy claim. | PASS_1_COMPLETE |
| S053 | The plan's 100-MI/MAR/Rubin rule agrees with reported S001.  FIML/outlier/transform contingencies are alternatives or sensitivities, not contradictory reported results. | PASS_1_COMPLETE |
| S054 | eAppendix 7 distinguishes CACE from per-protocol analysis and identifies a full-sample IV/SEM approach.  Its ratio wording cannot be numerically applied to reported ORs without a compatible effect scale and the model's unrounded estimate; no unsupported calculation is made. | PASS_1_COMPLETE |

## Candidate observation for later registration (no C ID)

**Statistical reporting inconsistency — DOC-004 eAppendix 10B baseline GAD-7 row.**  At [DOC-004 PDF p. 19](<../../../joi190007supp3_prod.pdf#page=19>), the baseline GAD-7 coefficient is printed as `B=0.464`, 95% CI `0.409 to 0.52`, and `p=0`.  A literal P value cannot equal zero.  The supplied page gives no stated rounding convention, test statistic, degrees of freedom, or unrounded P value.  The narrow positive CI supports a very small P value but does not establish the intended display (for example, `<0.001`).  Human question: does the source PDF intentionally use `0` as a rounded display, and if so, what reporting convention or corrected P notation should apply?

**Statistical reporting inconsistency — DOC-003 analysis-plan significance threshold lacks an operator.** At [DOC-003 PDF p. 3](<../../../joi190007supp2_prod.pdf#page=3>), the plan states, `For all statistical tests the 2-sided significance threshold will be set at p 0.05.` Direct rendering confirms that no comparison symbol is printed between `p` and `0.05`. A threshold must state a relation such as `<` or `<=` to identify which P values meet it; no comparator can be recovered from this sentence alone. The likely intended notation is not supplied-source fact. Human question: was the intended rule `P<.05`, `P<=.05`, or another explicitly defined convention?

## PASS 1 completion and limitations

- All 54 stable statistical relationships, `S001-S054`, have an explicit `PASS_1_COMPLETE` record.
- Two candidate observations are emitted without a candidate ID: the literal `p=0` at DOC-004 PDF p. 19 (already registered as C004) and the operator-free significance threshold at DOC-003 PDF p. 3.
- Compatibility checks were not extended beyond source-supported definitions where test family, sidedness, degrees of freedom, covariance estimator, unrounded values, or omnibus-test specification was absent.
- Coverage repair incorporated every mapped statistical rule from DOC-002, DOC-003, and DOC-004. DOC-005 contains no statistical relationship; no uncovered mapped statistical scope remains.
