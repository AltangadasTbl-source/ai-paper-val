# Statistical Consistency Review — Pass 1

## Scope, method, and completion

- **Reviewer runtime:** `root/statistical_pass_1` (fresh specialist runtime; `gpt-5.6-terra`, high effort; FRESH_SPAWN).
- **Assigned scope:** the canonical inferential relationship inventory, `S001` through `S093`, inclusive (93 relationships).
- **Sources checked:** supplied main article `jama_butler_2020_oi_200054.pdf` (pp. 1, 5-8); supplied protocol/SAP `joi200054supp1_prod.pdf` (pp. 33-36 and 51-67); and supplied online supplement `joi200054supp2_prod.pdf` (pp. 2-11). Page-matched mapper records were used as locators and transcription aids; the printed source text was checked directly with layout extraction.
- **Checks applied where source definitions permit:** estimate containment; interval endpoint order; sign/direction against named contrast or data; effect-measure, scale, and reference labels; source-matched repetitions; and CI/P/test/statistic/SE compatibility only where a compatible reported model and inferential convention exists. The SAP supplies 95% two-sided CI and test conventions (DOC-002 p. 52); the online supplement supplies the actual model descriptions (DOC-003 pp. 2-3).
- **Display-zero handling:** no `P = 0`, `p = 0.000`, or equivalent was observed. `P < .001` was not treated as a display zero and did not generate a proposal.
- **Completion:** every assigned relationship below has an explicit `PASS_1_COMPLETE` record. Candidate proposals are not stable candidate IDs and remain for coordinator merging and subsequent exact-source recheck. No severity, validity, disposition, or correction is assigned here.

## Candidate proposals for coordinator merge

### STAT-P1-001 — Different lower 95% CI endpoint for the same B. animalis result

- **Relationships:** S004 and S085.
- **Exact supplied locations:** `jama_butler_2020_oi_200054.pdf#page=5`; `joi200054supp2_prod.pdf#page=8`.
- **Direct observation:** for Bifidobacterium animalis subsp lactis at three months (29/56 vs 2/52), the main article reports adjusted OR 26.90 (95% CI, **5.94** to 121.66), while eTable 5 reports adjusted OR 26.9 (95% CI, **5.95** to 121.66). The point estimate differs only in trailing precision and the upper endpoint is identical, but the lower endpoint differs by 0.01 at the same displayed precision.
- **Consistency rule:** a matched repeated estimate/interval should reproduce the same printed endpoint, allowing only declared precision rounding. The two displayed two-decimal lower endpoints cannot both be the same rounded value.
- **Human question:** which lower CI endpoint is the intended reported value, and whether a source-specific calculation/version explains the difference.

### STAT-P1-002 — eTable 4 percentage does not reproduce from its printed numerator and denominator

- **Relationship:** S082.
- **Exact supplied location:** `joi200054supp2_prod.pdf#page=7`, eTable 4, placebo group at three months, `(+ )` category.
- **Direct observation:** the table prints `20/119 (16.0)`.
- **Consistency rule and calculation:** 20 divided by 119 multiplied by 100 is 16.8067%, which rounds to 16.8% to one decimal, not 16.0%.
- **Human question:** whether the numerator, denominator, or percentage in that printed cell is incorrect, or whether an unreported denominator applies specifically to the percentage.

### STAT-P1-003 — CACE adjusted coefficient, interval, and P value need source-level reconciliation

- **Relationship:** S080.
- **Exact supplied locations:** `joi200054supp2_prod.pdf#page=3` (CACE model: two-stage least squares, sex adjustment, care-home cluster-robust SE, coefficient and CI multiplied by 100 for presentation); `joi200054supp2_prod.pdf#page=5` (eTable 2: adjusted coefficient 0.01, 95% CI -0.20 to 0.41, P=.52); `joi200054supp1_prod.pdf#page=52` (95% two-sided convention).
- **Direct observation:** the stated interval contains 0.01 and is correctly ordered, but its midpoint is 0.105, not 0.01. Distances from the displayed point estimate to its lower and upper endpoints are 0.21 and 0.40, respectively.
- **Diagnostic compatibility check:** conditional on the stated 2SLS/cluster-robust-SE result being presented with a conventional two-sided Wald interval on the displayed coefficient scale, the interval is not centered on the reported coefficient. The displayed P=.52 also does not reproduce from the interval as a conventional symmetric Wald calculation. This is a diagnostic, not a replacement analysis.
- **Missing definitions precisely:** the supplied sources do not name the CI construction, test distribution/degrees of freedom, or whether the displayed CI/P were generated from a differently transformed coefficient. Those missing definitions prevent an exact tail-probability reconstruction; they do not change the direct observation that the printed coefficient and endpoints are asymmetric beyond displayed rounding.
- **Human question:** whether 0.01, either CI endpoint, the P value, the presentation multiplier, or an unreported non-Wald interval/test definition is responsible for the combination.

## Relationship-by-relationship records

| Relationship ID | PASS 1 record |
|---|---|
| S001 | **PASS_1_COMPLETE — no proposal.** Main pp. 1/5/6 repetition agrees: 12.9 vs 12.0 days, difference 0.9 (-3.25 to 5.05), adjusted IRR 1.13 (0.79 to 1.63), P=.50. Estimate is within ordered interval; IRR direction and rate label agree. Two-sided 95% model convention is supplied; displayed precision precludes a stronger CI/P reconstruction. |
| S002 | **PASS_1_COMPLETE — definition-limited, no proposal.** Main p. 5 AOR 9.19 (3.51 to 24.07), P<.001 and counts agree with eTable 5 p. 8 after precision. Main ARD is -47.4% while eTable 5 calls its 0.5 value an absolute difference. Neither location explicitly defines the subtraction/reference direction, so a sign conflict must not be inferred from column order alone. |
| S003 | **PASS_1_COMPLETE — definition-limited, no proposal.** Main p. 5 and eTable 5 p. 8 agree for counts, AOR 6.41/6.4 (2.14 to 19.20), and P=.001 at displayed precision. Absolute-difference signs use no explicit shared reference definition; no sign candidate is emitted. |
| S004 | **PASS_1_COMPLETE — proposal STAT-P1-001.** Main p. 5 and eTable 5 p. 8 match the event counts, OR, upper endpoint, and P<.001; the same lower 95% CI endpoint is printed as 5.94 versus 5.95. Main/eTable absolute-difference directions are not explicitly defined. |
| S005 | **PASS_1_COMPLETE — definition-limited, no proposal.** Main p. 5 and eTable 5 p. 8 agree after displayed precision for counts, AOR 21.96/22.0 (2.97 to 162.43), P=.002. The unsigned/reference convention for absolute difference is absent. |
| S006 | **PASS_1_COMPLETE — no proposal.** Main Table 2 p. 6 reports rate-labelled adjusted IRR 1.17 (0.75 to 1.84), P=.48; estimate is contained and endpoints are ordered. |
| S007 | **PASS_1_COMPLETE — no proposal.** Main Table 2 p. 6 reports rate-labelled IRR 1.13 (0.71 to 1.78), P=.61; interval/order/direction are coherent. |
| S008 | **PASS_1_COMPLETE — no proposal.** Table 2 p. 6 reports IRR 1.4 (1.1 to 1.9), P=.02; p. 5 narrative gives 1.42 (1.05 to 1.93), P=.02. The latter rounds to the table precision; rate label and direction agree. |
| S009 | **PASS_1_COMPLETE — no proposal.** Main Table 2 p. 6: IRR 0.92 (0.54 to 1.57), P=.76; containment, order, and rate direction agree. |
| S010 | **PASS_1_COMPLETE — no proposal.** Main Table 2 p. 6: IRR 1.0 (0.8 to 1.2), P=.92; ordered interval contains the estimate. |
| S011 | **PASS_1_COMPLETE — no proposal.** Main Table 2 p. 6: IRR 1.1 (0.6 to 2.1), P=.68; ordered interval contains the estimate. |
| S012 | **PASS_1_COMPLETE — no proposal.** Main Table 2 p. 6: IRR 0.8 (0.2 to 2.6), P=.68; ordered interval contains the estimate. |
| S013 | **PASS_1_COMPLETE — no proposal.** Main Table 2 p. 6: IRR 0.8 (0.5 to 1.2), P=.31; ordered interval contains the estimate. |
| S014 | **PASS_1_COMPLETE — no proposal.** Main Table 2 p. 6: IRR 1.2 (0.8 to 1.7), P=.41; ordered interval contains the estimate. |
| S015 | **PASS_1_COMPLETE — no proposal.** Main Table 2 p. 6: IRR 1.2 (0.7 to 2.0), P=.49; ordered interval contains the estimate. |
| S016 | **PASS_1_COMPLETE — no proposal.** Main Table 2 p. 6 labels this comparison OR 1.4 (0.8 to 2.4), P=.20; estimate is contained and label is distinct from rate outcomes. |
| S017 | **PASS_1_COMPLETE — no proposal.** Table 2 p. 6 gives adjusted mean difference 0.1 (0 to 0.2), P=.05; narrative gives 0.08 (-0.001 to 0.16), P=.05. The exact narrative result rounds to the coarse table presentation; duration and mean-difference label agree. |
| S018 | **PASS_1_COMPLETE — no proposal.** Main Table 2 p. 6: infection-days-per-person-year IRR 1.1 (0.8 to 1.5), P=.67; rate definition is supplied and interval/order are coherent. |
| S019 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7 labels an adjusted mean -0.1 (-0.1 to 0), P=.13 on the stated EQ-5D index scale. Coarse one-decimal endpoints prevent a reliable CI/P diagnostic. |
| S020 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted mean 0 (-0.1 to 0), P=.66; measure and scale agree; coarse rounding prevents CI/P reconstruction. |
| S021 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted mean -0.3 (-8.0 to 7.5), P=.95; estimate contained, endpoints ordered, and 0-100 health-status scale stated. |
| S022 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted mean 0.4 (-4.1 to 4.8), P=.87; estimate contained and endpoints ordered. |
| S023 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted mean 0 (-0.1 to 0.1), P=.92; containment/order and EQ-5D label are coherent. |
| S024 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted mean 0 (-0.1 to 0.1), P=.79; containment/order and proxy label are coherent. |
| S025 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7 identifies a power-of-2 transformed outcome: adjusted mean 24.4 (-1267.9 to 1316.6), P=.97. Estimate/interval order are coherent; no back-transformation is inferred. |
| S026 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted mean 0.6 (-4.9 to 6.2), P=.82; containment/order are coherent. |
| S027 | **PASS_1_COMPLETE — no proposal.** Table 3 p. 7 -0.1 (-0.1 to -0), P=.05 matches the p. 6 narrative -0.06 (-0.11 to -0.001), P=.05 after table rounding. ICECAP-O 0-1 scale and direction are supplied. |
| S028 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted mean 0 (0 to 0), P=.85. Finite one-decimal display makes the interval a rounded near-zero interval, not an endpoint-order issue. |
| S029 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted mean -0.1 (-0.2 to 0), P=.15; containment/order and ICECAP-O label are coherent. |
| S030 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted mean 0 (-0.1 to 0), P=.69; containment/order are coherent. |
| S031 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted OR 1.25 (0.74 to 2.11), P=.41 for 42/152 versus 36/153; binary-outcome label and interval/order agree. |
| S032 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted OR 1.03 (0.59 to 1.80), P=.90 for deaths 33/155 versus 32/155; label and interval/order agree. |
| S033 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted IRR 1.17 (0.72 to 1.90), P=.53; rate analysis denominator 152/153 is stated. |
| S034 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted IRR 1.00 (0.43 to 2.29), P>.99; rate label, containment, and order agree. |
| S035 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted IRR 1.39 (0.79 to 2.46), P=.25; rate label and interval/order agree. |
| S036 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted IRR 1.83 (0.95 to 3.54), P=.07; rate label and interval/order agree. |
| S037 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted IRR 1.1 (0.7 to 1.6), P=.80; rate label and interval/order agree at displayed precision. |
| S038 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted IRR 1.2 (0.78 to 2.0), P=.39; rate label and interval/order agree. |
| S039 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted OR 1.0 (0.6 to 1.8), P=.89; binary-outcome label and interval/order agree. |
| S040 | **PASS_1_COMPLETE — no proposal.** Main Table 3 p. 7: adjusted mean 0.1 (-0.1 to 0.2), P=.27; duration/mean-difference label, containment, and order agree. |
| S041 | **PASS_1_COMPLETE — definition-limited, no proposal.** Main p. 7 and eTable 5 p. 8 agree for counts, AOR .61/.6 (.24 to 1.56), P=.30 and .76/.8 (.20 to 2.89), P=.68 after precision. ARD signs differ from eTable absolute differences, but neither source defines a shared subtraction/reference direction. |
| S042 | **PASS_1_COMPLETE — definition-limited, no proposal.** Main p. 7 and eTable 5 pp. 8-9 agree for counts, AOR 1.23/1.2 (.54 to 2.83), P=.62 and 1.27/1.3 (.50 to 3.21), P=.62 after precision. Absolute-difference reference direction is unnamed. |
| S043 | **PASS_1_COMPLETE — no proposal.** Main p. 8 and eTable 5 p. 8 agree after precision for 6/55 versus 1/52, OR 6.51/6.5 (.75 to 56.57), P=.09; second-follow-up result is explicitly not analyzable. |
| S044 | **PASS_1_COMPLETE — no proposal.** Protocol p. 33 states planned ITT Poisson CAAD analysis with negative-binomial alternative for overdispersion; later actual negative-binomial result is within that stated contingency. |
| S045 | **PASS_1_COMPLETE — no proposal.** Protocol p. 33 planned n=330/90% power/two-sided 5%/10% reduction/30% dropout is a planning relation, not an observed result; no matched calculation inputs are supplied for re-performance. |
| S046 | **PASS_1_COMPLETE — no proposal.** Protocol p. 33 mechanistic power statement is planning-only; no observed matched mechanistic inference is presented for a consistency comparison. |
| S047 | **PASS_1_COMPLETE — no proposal.** Protocol p. 34 structural-mean-model adherence plan and supplement CACE analysis are directionally/model-label compatible; no numeric matched result is stated here. |
| S048 | **PASS_1_COMPLETE — no proposal.** Protocol p. 34 records missing-data and SACE plans; result sources supply sensitivity analyses without a directly contradictory definition. |
| S049 | **PASS_1_COMPLETE — no proposal.** Protocol p. 34 planned mediation/G-computation is not reported as a matched trial-result estimate. |
| S050 | **PASS_1_COMPLETE — no proposal.** Protocol p. 35 Poisson/negative-binomial contingency and site interaction plan are compatible with later rate outcomes; no isolated estimate/CI/P to reconcile. |
| S051 | **PASS_1_COMPLETE — no proposal.** Protocol p. 35 planned Cox frailty duration analysis differs from later reported hurdle/linear description; source documents do not state that this early protocol model remained final, so no deviation/contradiction is inferred. |
| S052 | **PASS_1_COMPLETE — no proposal.** Protocol p. 35 mixed-linear health-utility plan and later two-level linear reporting both identify adjusted mean differences; later SAP/result definitions control the actual analyses. |
| S053 | **PASS_1_COMPLETE — no proposal.** Protocol p. 35 planned logistic/count/Cox models identify outcome families only; no incompatible matched printed estimate is present. |
| S054 | **PASS_1_COMPLETE — no proposal.** Protocol p. 36 mixed-logistic microbiology/candidiasis plan is compatible with later adjusted OR reporting; no source-grounded conflict is observed. |
| S055 | **PASS_1_COMPLETE — no proposal.** Protocol p. 36 planned mixed-linear amount-of-candidiasis model is superseded by later ordinal model documentation; no statement establishes the original plan as final. |
| S056 | **PASS_1_COMPLETE — no proposal.** Protocol p. 36 mechanistic logistic-regression plan has no matched reported estimate in supplied result sources. |
| S057 | **PASS_1_COMPLETE — no proposal.** SAP p. 51 revised power/target statement is planning-only and explicitly differs from protocol recruitment targets; amendment/revision context is supplied. |
| S058 | **PASS_1_COMPLETE — no proposal.** SAP pp. 54-55 specifies ITT/complete-case/imputed populations. Actual online-supplement ITT wording (randomized with outcome data, no imputation) is compatible with the stated primary-analysis population. |
| S059 | **PASS_1_COMPLETE — no proposal.** SAP p. 52 supplies 95% two-sided CI/test and no-multiplicity conventions used as context; no contradictory convention appears in the result sources. |
| S060 | **PASS_1_COMPLETE — no proposal.** SAP p. 60 gives two-level Poisson primary presentation with negative-binomial option for overdispersion. Actual two-level negative-binomial primary model is explicitly allowed; IRR/CI/P labels match. |
| S061 | **PASS_1_COMPLETE — no proposal.** SAP p. 61 rate and duration model labels are compatible with Table 2's IRR and adjusted mean-difference results. |
| S062 | **PASS_1_COMPLETE — no proposal.** SAP pp. 61-62 defines diarrhea rate/IRR presentation, matching Table 3 labels. |
| S063 | **PASS_1_COMPLETE — no proposal.** SAP p. 62 specifies separate self/proxy EQ-5D/EQ-VAS/ICECAP adjusted mean differences; Table 3 labels and stated scales agree. |
| S064 | **PASS_1_COMPLETE — no proposal.** SAP pp. 62-63 specifies logistic OR for hospitalized/death and Poisson IRR for hospital days; Table 3 measure labels agree. |
| S065 | **PASS_1_COMPLETE — no proposal.** SAP p. 63 gender adjustment, count overdispersion, and transformations/hurdle contingencies are compatible with reported model notes. |
| S066 | **PASS_1_COMPLETE — no proposal.** SAP p. 63 prespecifies the sensitivity types later reported in eTable 1; no matched numerical conflict appears. |
| S067 | **PASS_1_COMPLETE — no proposal.** SAP p. 64 defines sex/capacity/frailty interaction comparisons; eTable 6 reports the same three interaction families. |
| S068 | **PASS_1_COMPLETE — no proposal.** SAP p. 64 defines missingness/offset/sensitivity conventions; eTable 3 identifies its death-during-infection assumption without conflict. |
| S069 | **PASS_1_COMPLETE — no proposal.** SAP p. 65 structural mean/GMM-or-2SLS and robust-SE CACE plan is compatible with online supplement p. 3; exact CI construction/distribution remains unstated (relevant to STAT-P1-003). |
| S070 | **PASS_1_COMPLETE — no proposal.** SAP p. 65 daily-adherence and blinding models have no matched result statistic requiring interval or P reconciliation. |
| S071 | **PASS_1_COMPLETE — no proposal.** SAP pp. 66-67 ICC/Bland-Altman/kappa/descriptive plan has no matching reported inferential result in supplied sources. |
| S072 | **PASS_1_COMPLETE — no proposal.** Online supplement p. 2 declares adjusted IRR, mean difference, or OR with 95% CI/P reporting; main-table effect labels follow this convention. |
| S073 | **PASS_1_COMPLETE — no proposal.** Online supplement p. 2 ITT definition matches result-population wording; it does not claim all randomized persons contributed outcomes. |
| S074 | **PASS_1_COMPLETE — no proposal.** Online supplement p. 3 defines CACE 2SLS/IV, sex adjustment, cluster-robust SE, and multiplication by 100. This model definition is the applicable context for S080; no independent contradiction in the definition itself. |
| S075 | **PASS_1_COMPLETE — no proposal.** Online supplement p. 3 primary two-level negative-binomial model, nesting, observation time, and sex adjustment match the primary result labels. |
| S076 | **PASS_1_COMPLETE — no proposal.** Online supplement p. 3 secondary rate models/robust SE/sex adjustment match reported IRR rate-outcome families; low-rate model selection is not identified result-by-result. |
| S077 | **PASS_1_COMPLETE — no proposal.** Online supplement p. 3 hurdle duration and logistic/ordinal microbiology definitions match the effect-measure labels used in relevant result tables. |
| S078 | **PASS_1_COMPLETE — no proposal.** Online supplement p. 3 subgroup-by-arm interaction method matches eTable 6. |
| S079 | **PASS_1_COMPLETE — no proposal.** eTable 1 p. 4 reports sensitivity IRRs 1.2 (.83 to 1.67), P=.36 and 1.1 (.74 to 1.54), P=.73. Both estimates are contained in ordered intervals and are compatible with their named sensitivity definitions. |
| S080 | **PASS_1_COMPLETE — proposal STAT-P1-003.** eTable 2 p. 5 gives coefficient .01 (-.20 to .41), P=.52 under the CACE model p. 3. Containment/order pass; the printed point/CI/P combination requires reconciliation as documented above. |
| S081 | **PASS_1_COMPLETE — no proposal.** eTable 3 p. 6 gives IRR 1.62 (1.03 to 2.57), P=.04 under a named extreme death-during-infection assumption. Estimate/interval direction/order and P interpretation agree. |
| S082 | **PASS_1_COMPLETE — proposal STAT-P1-002.** eTable 4 p. 7 ordinal model/reference/OR labels are supplied and ORs have ordered, containing intervals. The printed placebo three-month `(+ )` percentage 20/119 (16.0) does not reproduce from its stated denominator. |
| S083 | **PASS_1_COMPLETE — no proposal.** eTable 5 p. 8 gives C. difficile OR 6.5 (.75 to 56.57), P=.09 and explicitly marks second follow-up not analyzable; matches main p. 8 after precision. |
| S084 | **PASS_1_COMPLETE — definition-limited, no proposal.** eTable 5 p. 8 L. rhamnosus ORs/CIs/Ps match S002-S003 after precision; absolute-difference reference direction is not explicitly defined. |
| S085 | **PASS_1_COMPLETE — proposal STAT-P1-001.** eTable 5 p. 8 B. animalis 3-month lower CI endpoint 5.95 conflicts with main p. 5 endpoint 5.94 for the same reported OR/contrast. Second-follow-up values match after precision. |
| S086 | **PASS_1_COMPLETE — no proposal.** eTable 5 p. 8 labels near-complete Enterobacterales/VRE cells not analyzable; no inferential estimate is printed and none is inferred. |
| S087 | **PASS_1_COMPLETE — definition-limited, no proposal.** eTable 5 p. 8 OR/CIs/Ps match S041 after precision; no explicit common subtraction reference supports an ARD-sign contradiction. |
| S088 | **PASS_1_COMPLETE — definition-limited, no proposal.** eTable 5 p. 8 OR/CIs/Ps match S042 after precision; no explicit common subtraction reference supports an absolute-difference-sign contradiction. |
| S089 | **PASS_1_COMPLETE — no proposal.** eTable 4 p. 7 and continuation p. 9 repeat ordinal-candida OR .7 (.20 to 2.17), P=.49 and .5 (.12 to 2.16), P=.36 with probiotic/placebo reference and gender adjustment; intervals/order agree. |
| S090 | **PASS_1_COMPLETE — no proposal.** eTable 6 p. 10 sex subgroup has stated reference categories and trial-arm/gender/interaction P=.95/.76/.41. Interaction P is a named model test; no unreported degrees of freedom are inferred. |
| S091 | **PASS_1_COMPLETE — no proposal.** eTable 6 p. 10 capacity subgroup has stated reference categories and trial-arm/capacity/interaction P=.41/.38/.64; labels and direction are coherent. |
| S092 | **PASS_1_COMPLETE — no proposal.** eTable 6 pp. 10-11 frailty subgroup has stated references and P=.22/.20/.31; the multi-level interaction test distribution/df is not supplied, so no derived P/CI test is attempted. |
| S093 | **PASS_1_COMPLETE — no proposal.** eTable 6 pp. 10-11 states gender adjustment except for sex subgroup and no formal multiplicity adjustment; this matches the SAP convention. |

## Pass-1 counts and limitations

- **Relationships completed:** 93/93 (`S001`-`S093`).
- **Distinct candidate proposals:** 3 (`STAT-P1-001`, `STAT-P1-002`, `STAT-P1-003`).
- **No-proposal records:** 89 relationship records (including definition-limited records). Four relationship records carry a proposal, with STAT-P1-001 represented by both S004 and S085; the three proposals are counted once by printed-value/rule identity.
- **Definition-limited records:** S002-S005, S019-S020, S028, S041-S042, S069, S084, S087-S088, and S092. In particular, source locations do not state a common subtractive reference for several absolute-risk/difference values, and the sources do not state CACE CI construction/test degrees of freedom. No sidedness, degrees of freedom, covariance, multiplicity method, denominator, model selection, or estimand mapping was inferred from convention.
- **Diagnostic approximation:** STAT-P1-003 labels its interval/P check as conditional diagnostic reasoning; it does not replace the reported analysis or reconstruct an exact tail probability.
- **Display-zero exclusions:** none applicable; no candidate was based on finite-precision P-value notation.
