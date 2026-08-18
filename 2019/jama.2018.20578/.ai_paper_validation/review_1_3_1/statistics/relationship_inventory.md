# Statistical Relationship Inventory

## Pass 1 scope and method

- Reviewer lane: `qc13_statistical_consistency_reviewer`, pass 1.
- Complete assigned evidence scope: DOC-001 PDF pp. 1-10, DOC-002 PDF pp. 1-7, and DOC-003 PDF pp. 1-29, as reconstructed in the complete main and support quantitative evidence maps.
- Scientific-input boundary: source/evidence inventories, coverage records, direct PDFs, and the two current evidence maps were read. No legacy candidate, queue, verifier, critic, or report output was used.
- Grouping rule: one `S` relationship may contain a displayed inferential vector when all components share an outcome, model, contrast, population family, and source table/figure. Every component row/cell in each vector was checked; grouping is not sampling.
- Checks applied: point-estimate containment, endpoint order, null containment, sign/direction, effect-measure and scale labels, repeated-location agreement, and P-value/test/statistic/SE compatibility only where definitions support it. Diagnostic calculations are explicitly labelled and are not reconstructions of an unreported model.
- Pass 1 status vocabulary is completion only. It is not an adjudication or disposition.

## Stable relationship register

| S ID | Exact statistical relationship and source | Components covered | Pass-1 diagnostic and missing definitions | Candidate proposal(s) | Status |
|---|---|---|---|---|---|
| S001 | DOC-001 prespecified analysis framework: [pp. 4-6](../../../jama_flint_2019_oi_190079.pdf#page=4) | Cox primary model; mixed continuous outcomes; overdispersed Poisson Simpson-Angus model; two-sided 5% tests; post hoc Holm adjustment | Model, covariates, repeated-measure structure, sidedness, and multiplicity labels recorded. Covariance structure, degrees of freedom, coefficient precision, and unadjusted secondary P values are not printed and were not inferred. | None | PASS_1_COMPLETE |
| S002 | DOC-001 primary treatment effect: [p. 1](../../../jama_flint_2019_oi_190079.pdf#page=1), [pp. 6-7](../../../jama_flint_2019_oi_190079.pdf#page=6) | HR 0.25; 95% CI 0.13-0.48; P<.001; all 126 randomized; olanzapine vs placebo; relapse | Estimate is inside ordered positive endpoints; CI excludes 1 in the same beneficial direction as the narrative. Diagnostic Wald calculation from rounded log endpoints is compatible with P<.001, but is not a reconstruction of the Cox test. Exact repetition agrees. | None | PASS_1_COMPLETE |
| S003 | DOC-001 primary-model covariates: [pp. 6-7](../../../jama_flint_2019_oi_190079.pdf#page=6) | Age HR 0.78 (0.42-1.46), P=.44; remission HR 2.45 (0.98-6.13), P=.06; three site HR/CI/P rows | All 5 estimates are contained by ordered positive CIs. Null containment agrees with printed P>.05. Rounded-log-CI diagnostics are compatible; exact coefficient covariance and test implementation are not printed. | None | PASS_1_COMPLETE |
| S004 | DOC-001 Figure 2 log-rank result: [p. 7](../../../jama_flint_2019_oi_190079.pdf#page=7) | Log-rank P<.001; relapse-free curves; 95% CI bands; at-risk series | Direction agrees with relapse counts and Cox HR. The plot supplies no numeric CI-band coordinates and the log-rank statistic/df are absent, so no numerical P-value reconstruction was attempted. | None | PASS_1_COMPLETE |
| S005 | DOC-001 post hoc primary sensitivity: [p. 7](../../../jama_flint_2019_oi_190079.pdf#page=7) | Excludes 7 medication discontinuers; HR 0.22 (0.11-0.43), P<.001 | Estimate is contained; endpoints are ordered; direction agrees with the primary result. Rounded-log-CI diagnostic is compatible with P<.001. Exact exclusion membership and Cox coefficient covariance are not supplied. | None | PASS_1_COMPLETE |
| S006 | DOC-001 secondary treatment-by-linear-time vector: [p. 1](../../../jama_flint_2019_oi_190079.pdf#page=1), [p. 7](../../../jama_flint_2019_oi_190079.pdf#page=7) | 8 estimates/CIs/Holm-adjusted P values: weight, waist, total/LDL/HDL cholesterol, triglyceride, glucose, HbA1c | All estimates are inside ordered intervals. The first 3 intervals exclude 0 and adjusted P values are <.05; the other 5 include 0 and adjusted P values are >.05. Abstract/results numeric repetitions agree. Holm compatibility can only be diagnostic because raw P values and full covariance/test details are absent. HbA1c's abstract unit conflicts with its percent scale elsewhere. | SP1-001 | PASS_1_COMPLETE |
| S007 | DOC-001 Simpson-Angus weekly change: [p. 7](../../../jama_flint_2019_oi_190079.pdf#page=7) | 0.022 points/week (95% CI 0.009-0.036), adjusted P=.009 | Estimate is contained; ordered interval excludes 0; adjusted P is directionally compatible. Diagnostic rounded-CI P value may be smaller before adjustment; raw P and Holm rank are not printed. | None | PASS_1_COMPLETE |
| S008 | DOC-001 Table 4 raw-change interval vector: [p. 8](../../../jama_flint_2019_oi_190079.pdf#page=8) | 16 within-arm change estimates/CIs for 8 anthropometric/metabolic outcomes | Every estimate lies within ordered endpoints. Sign agrees with printed change wording. These raw paired changes are not the adjusted treatment-by-time effects in S006. Paired observations/covariances are absent, and the table warns that missing data prevents simple endpoint subtraction. | None | PASS_1_COMPLETE |
| S009 | DOC-001 Table 5 risk-difference vector: [p. 9](../../../jama_flint_2019_oi_190079.pdf#page=9) | 4 unadjusted percentage-point differences/CIs; 2 marked exact | All estimates are contained in ordered intervals and all CIs include 0, agreeing with the nonsignificance narrative. Exact interval method is not named, so no binomial-method reconstruction was imposed. | None | PASS_1_COMPLETE |
| S010 | DOC-001 missing-data/pattern-mixture analysis: [p. 5](../../../jama_flint_2019_oi_190079.pdf#page=5) | Missing-at-random assumption; early-termination patterns; pattern-mixture averaging for triglycerides | Labels and qualitative result recorded. No alternate numeric estimates, pattern weights, or covariance specification are printed; compatibility cannot be mechanically recomputed. | None | PASS_1_COMPLETE |
| S011 | DOC-001 medication-change sensitivities: [pp. 5, 7](../../../jama_flint_2019_oi_190079.pdf#page=5) | Exclusion after statin/hypoglycemic changes; qualitative similarity statement | No sensitivity estimates, intervals, or P values are printed. The named missing outputs prevent numerical checking, without itself creating a candidate. | None | PASS_1_COMPLETE |
| S012 | DOC-001 power relationship: [p. 4](../../../jama_flint_2019_oi_190079.pdf#page=4) | n=176; 80% power; 20% risk difference; <=15% attrition; revised n=128 | Alpha, control risk, sidedness of calculation, allocation assumptions, and detailed formula are absent, so the power calculation cannot be reproduced from supplied evidence. No convention was inferred. | None | PASS_1_COMPLETE |
| S013 | DOC-001 multiplicity/interpretation: [p. 6](../../../jama_flint_2019_oi_190079.pdf#page=6) | Two-sided 5%; post hoc Holm; secondary analyses exploratory | Labels are internally coherent. Raw secondary P values and Holm ordering are missing, limiting exact recalculation of adjusted P values. | None | PASS_1_COMPLETE |
| S014 | DOC-002 protocol Bayesian primary framework: [p. 6](../../../joi180151supp1_prod.pdf#page=6) | Hierarchical pairwise meta-analysis; DIC model selection; HR with 95% CrI; aspirin vs no aspirin | Effect measure, contrast, and interval type are explicit. Prior distributions and final DIC tie rule are elaborated only in DOC-003 and are cross-referenced in S019-S024. | None | PASS_1_COMPLETE |
| S015 | DOC-002 fallback HR construction: [p. 6](../../../joi180151supp1_prod.pdf#page=6); DOC-003 [p. 3](../../../joi180151supp2_prod.pdf#page=3) | Poisson likelihood/log link from events, totals/person-time, and follow-up when HR unavailable | Repeated model description agrees. Constant event-rate assumption is supplied in DOC-003. Trial-specific choice of reported HR versus reconstructed rate data is not tabulated in the supplied evidence. | None | PASS_1_COMPLETE |
| S016 | DOC-002 frequentist RR-to-ARD rule: [p. 6](../../../joi180151supp1_prod.pdf#page=6) | RR/CI; baseline placebo risk; negative ARD favors aspirin; positive favors no aspirin | Sign direction is explicit and agrees with DOC-003 eMethods. The protocol's prose multiplication/subtraction is interpreted only as written; unrounded pooled RR/baseline inputs are not supplied for exact cell reconstruction. | None | PASS_1_COMPLETE |
| S017 | DOC-002 frequentist significance rule: [p. 6](../../../joi180151supp1_prod.pdf#page=6) | Two-sided P<.05 | Rule is explicit. Most support results use intervals without P values; null-exclusion checks use the interval type actually printed. | None | PASS_1_COMPLETE |
| S018 | DOC-003 estimated 10-year risk: [p. 3](../../../joi180151supp2_prod.pdf#page=3) | Control primary-outcome risk / mean follow-up years x10; Poisson event CI | Direction, time scale, and outcome are defined. Trial-specific follow-up inputs and resulting risk CIs are not displayed in the supplied support, so exact recalculation is unavailable. | None | PASS_1_COMPLETE |
| S019 | DOC-003 Bayesian computation and model labels: [pp. 3-4](../../../joi180151supp2_prod.pdf#page=3) | Logged HR/SE or person-years; fixed/random Poisson models; priors; 5,000 adaptation + 100,000 x4 chains; PSRF 1.05 | Statistical definitions are recorded. Chain outputs, PSRF values by outcome, posterior draws, and trial-level estimand mapping are absent and were not inferred. | None | PASS_1_COMPLETE |
| S020 | DOC-003 all-patient DIC/model vector: [p. 5](../../../joi180151supp2_prod.pdf#page=5) | 11 outcomes; fixed/random DIC; fixed-effect I2; selected model | All 11 rows checked against the printed rule: DIC difference >3 selects lower DIC; within 3 selects random only if I2>25. Ten rows follow the rule. Incident cancer prints DIC 27.06 vs 27.93, I2=25, but selects random. | SP1-002 | PASS_1_COMPLETE |
| S021 | DOC-003 low-risk DIC/model vector: [p. 5](../../../joi180151supp2_prod.pdf#page=5) | 11 outcomes | All 11 selected models follow the printed DIC/I2 rule, including random selection for I2 26, 32, 33, 41, and 42 when DICs are within 3. | None | PASS_1_COMPLETE |
| S022 | DOC-003 high-risk DIC/model vector: [pp. 5-6](../../../joi180151supp2_prod.pdf#page=5) | 11 outcomes | All 11 selected models follow the printed rule. The I2=3 incident-cancer row selects fixed; the I2=26 all-MI row selects random. | None | PASS_1_COMPLETE |
| S023 | DOC-003 diabetes DIC/model vector: [p. 6](../../../joi180151supp2_prod.pdf#page=6) | 11 outcomes | All 11 selected models follow the printed rule. Random selections at I2 34, 39, 51, and 77 are compatible; the lower random DIC for ischemic stroke is also within 3 and I2>25. | None | PASS_1_COMPLETE |
| S024 | DOC-003 Bayesian significance rule: [p. 4](../../../joi180151supp2_prod.pdf#page=4) | 95% CrI excludes 1 | Rule is explicit. Rounded endpoints equal to 1 require unrounded values when provided; no endpoint was treated as excluding 1 merely by convention. | None | PASS_1_COMPLETE |
| S025 | DOC-003 frequentist ARD/NNT framework: [p. 4](../../../joi180151supp2_prod.pdf#page=4) | Random-effects Mantel-Haenszel RR; baseline control risk; ARD/CI; negative favors aspirin; NNT/NNH only for significant ARD | Effect type and direction are explicit. The source does not state the display unit for ARD, integer-rounding convention for NNT/NNH, or unrounded cell values. This affects the scale and reciprocal checks in S026-S036. | SP1-006 | PASS_1_COMPLETE |
| S026 | DOC-003 eTable 3 composite-outcome ARD vector: [p. 15](../../../joi180151supp2_prod.pdf#page=15) | 4 populations; 4 ARDs/CIs; 4 NNTs | All estimates contained; endpoints ordered; all CIs exclude 0 and signs favor aspirin; NNT presence follows the stated rule. Reciprocals are compatible with plausible unrounded two-decimal ARDs. | None | PASS_1_COMPLETE |
| S027 | DOC-003 eTable 3 all-cause mortality ARD vector: [p. 15](../../../joi180151supp2_prod.pdf#page=15) | 4 populations | All estimates contained; ordered CIs include 0; no NNT printed, consistent with the stated rule. | None | PASS_1_COMPLETE |
| S028 | DOC-003 eTable 3 cardiovascular mortality ARD vector: [p. 15](../../../joi180151supp2_prod.pdf#page=15) | 4 populations | All estimates contained; ordered CIs include 0; no NNT printed. | None | PASS_1_COMPLETE |
| S029 | DOC-003 eTable 3 all-MI ARD vector: [p. 15](../../../joi180151supp2_prod.pdf#page=15) | 4 populations; NNTs for all-patient and low-risk rows | Estimates contained and endpoints ordered. The low-risk displayed CI is -0.49 to 0.00, which reaches the null at printed precision, but an NNT is printed under the rule that NNT is only reported for statistically significant ARDs. No unrounded endpoint note is supplied. | SP1-003 | PASS_1_COMPLETE |
| S030 | DOC-003 eTable 3 all-stroke ARD vector: [p. 15](../../../joi180151supp2_prod.pdf#page=15) | 4 populations | Estimates contained; all ordered CIs include 0; no NNT printed. | None | PASS_1_COMPLETE |
| S031 | DOC-003 eTable 3 ischemic-stroke ARD vector: [p. 15](../../../joi180151supp2_prod.pdf#page=15) | 4 populations; 2 NNTs | Estimates contained. All/low-risk CIs exclude 0 and have NNTs; high-risk/diabetes CIs include 0 and do not. Reciprocal diagnostics are compatible with unrounded values. | None | PASS_1_COMPLETE |
| S032 | DOC-003 eTable 3 incident-cancer ARD vector: [p. 15](../../../joi180151supp2_prod.pdf#page=15) | 4 populations | Estimates contained; all ordered CIs include 0; no NNT/NNH printed. | None | PASS_1_COMPLETE |
| S033 | DOC-003 eTable 3 cancer-mortality ARD vector: [p. 15](../../../joi180151supp2_prod.pdf#page=15) | 4 populations | Estimates contained; all ordered CIs include 0; no NNT/NNH printed. | None | PASS_1_COMPLETE |
| S034 | DOC-003 eTable 3 major-bleeding ARD vector: [p. 15](../../../joi180151supp2_prod.pdf#page=15) | 4 populations; 4 NNHs | Positive estimates and CIs consistently favor no aspirin; NNH presence follows significance. However, printed NNHs 210, 152, and 121 do not reciprocally reconcile with printed two-decimal ARDs 0.47, 0.64, and 0.80 under ordinary nearest-two-decimal bounds; low-risk 0.40/249 can reconcile. Unit and integer rounding are unstated. | SP1-007 | PASS_1_COMPLETE |
| S035 | DOC-003 eTable 3 intracranial-bleeding ARD vector: [p. 15](../../../joi180151supp2_prod.pdf#page=15) | 4 populations; 2 NNHs | All estimates contained. All/low-risk CIs exclude 0 and have NNHs; high-risk/diabetes include 0 and do not. Reciprocal diagnostics can reconcile with unrounded two-decimal ARDs. | None | PASS_1_COMPLETE |
| S036 | DOC-003 eTable 3 major-GI-bleeding ARD vector: [p. 15](../../../joi180151supp2_prod.pdf#page=15) | 4 populations; 4 NNHs | All positive estimates contained; all CIs exclude 0; NNH presence and direction agree. Reciprocals are compatible with plausible unrounded values. | None | PASS_1_COMPLETE |
| S037 | DOC-003 eTable 4 total-stroke vector: [p. 16](../../../joi180151supp2_prod.pdf#page=16) | 4 population rows; ARR/95% CI; HR/95% CrI; I2 | Every ARR and HR is contained by ordered intervals. ARR signs and HR<1 agree with fewer aspirin events. Diabetes upper CrI is printed 1.00 with footnote unrounded 1.004, so it includes 1. The footnote calls this a confidence interval although the column is credible interval. | SP1-004 | PASS_1_COMPLETE |
| S038 | DOC-003 eTable 6 <=100-mg sensitivity vector: [p. 18](../../../joi180151supp2_prod.pdf#page=18) | 11 HR/95% CrI cells; 11 studies; N=134,470 | All estimates contained; endpoints ordered and positive. All-MI upper endpoint 1.00 is clarified as unrounded 0.9989, so it excludes 1. The footnote labels that endpoint a confidence interval although the table defines CrI. | SP1-005 | PASS_1_COMPLETE |
| S039 | DOC-003 eTable 6 double-blind sensitivity vector: [p. 18](../../../joi180151supp2_prod.pdf#page=18) | 11 HR/95% CrI cells; 9 studies; N=135,043 | All estimates contained by ordered positive intervals. Null-exclusion directions agree with the printed HR scale. | None | PASS_1_COMPLETE |
| S040 | DOC-003 eTable 6 since-2000 sensitivity vector: [p. 18](../../../joi180151supp2_prod.pdf#page=18) | 11 HR/95% CrI cells; 9 studies; N=113,140 | All estimates contained by ordered positive intervals. Null-exclusion directions agree with the printed HR scale. | None | PASS_1_COMPLETE |
| S041 | DOC-003 eTable 6 exclude-asymptomatic-PAD sensitivity vector: [p. 18](../../../joi180151supp2_prod.pdf#page=18) | 11 HR/95% CrI cells; 11 studies; N=156,874 | All estimates contained by ordered positive intervals. Directions agree with efficacy (<1) and bleeding (>1) labels where CrIs exclude 1. | None | PASS_1_COMPLETE |
| S042 | DOC-003 eFigure 3 Egger test: [p. 21](../../../joi180151supp2_prod.pdf#page=21) | Coefficient -0.47; SE 0.77; t=-0.59; P=.57; 10 plotted studies | Pass-1 sign/P review was expanded in pass 2 using the complete numeric checker and recheck: coefficient/SE is about -0.61, and ordinary two-decimal input bounds give magnitude about 0.600-0.621, excluding a t displayed as -0.59. The printed t/P remain mutually plausible; exact df, implementation, and unrounded inputs are absent. | C019 (registered cross-lane) | PASS_1_COMPLETE |
| S043 | DOC-003 eFigure 4 composite-outcome frequentist forest vector: [p. 22](../../../joi180151supp2_prod.pdf#page=22) | 13 study RRs/CIs; fixed and random pooled RR; 2 weight columns; I2/tau2/Q P | All 15 estimates are inside ordered positive intervals. Direction agrees with event ratios. Fixed=random 0.90 (0.86-0.94), I2=0%, tau2=0 is coherent; heterogeneity P=.75. Totals and 100% weight columns were mapped. | None | PASS_1_COMPLETE |
| S044 | DOC-003 eFigure 4 all-cause-mortality forest vector: [p. 22](../../../joi180151supp2_prod.pdf#page=22) | 13 study rows; 2 pooled rows; heterogeneity | All estimates contained; endpoint order/direction agree with displayed counts. Fixed=random 0.97 (0.93-1.02), I2=0%, tau2=0; P=.60. | None | PASS_1_COMPLETE |
| S045 | DOC-003 eFigure 4 cardiovascular-mortality forest vector: [p. 23](../../../joi180151supp2_prod.pdf#page=23) | 13 study rows; 2 pooled rows; heterogeneity | All estimates contained; endpoint order and event-ratio direction agree. Fixed 0.94 and random 0.95 both include 1; I2=0%, tau2=0; P=.50. | None | PASS_1_COMPLETE |
| S046 | DOC-003 eFigure 4 all-MI forest vector: [p. 23](../../../joi180151supp2_prod.pdf#page=23) | 13 study rows; 2 pooled rows; heterogeneity | All estimates contained and directions agree with counts. Random 0.86 (0.76-0.97) corresponds to the DIC-selected random model; I2=61%, tau2=.0273, P<.01. Test/model definitions do not support deriving the Bayesian HR from this RR. | None | PASS_1_COMPLETE |
| S047 | DOC-003 eFigure 4 total-stroke forest vector: [p. 24](../../../joi180151supp2_prod.pdf#page=24) | 13 study rows; 2 pooled rows; heterogeneity | All estimates contained; endpoint order/direction agree. Fixed 0.94 (0.88-1.02), random 0.94 (0.87-1.01), I2=0%, tau2=0; P=.51. | None | PASS_1_COMPLETE |
| S048 | DOC-003 eFigure 4 ischemic-stroke forest vector: [p. 24](../../../joi180151supp2_prod.pdf#page=24) | 10 study rows; 2 pooled rows; heterogeneity | All estimates contained; endpoint order/direction agree. Fixed=random 0.87 (0.80-0.96), I2=0%, tau2=0; P=.55. Population totals differ from all-outcome totals as expected from omitted studies. | None | PASS_1_COMPLETE |
| S049 | DOC-003 eFigure 4 incident-cancer forest vector: [p. 24](../../../joi180151supp2_prod.pdf#page=24) | 10 study rows; 2 pooled rows; heterogeneity | All estimates contained; direction agrees with event ratios. Fixed 1.01 (0.97-1.05), random 1.00 (0.95-1.06), I2=36%, tau2=.0026; P=.12. DIC-selected random label is tracked in S020, including its rule mismatch. | SP1-002 (cross-reference) | PASS_1_COMPLETE |
| S050 | DOC-003 eFigure 4 cancer-mortality forest vector: [p. 25](../../../joi180151supp2_prod.pdf#page=25) | 12 study rows; 2 pooled rows; heterogeneity | All estimates contained; endpoint order/direction agree. Fixed 1.03 (0.96-1.11), random 1.03 (0.94-1.12), I2=21%, tau2=.0044; P=.24. | None | PASS_1_COMPLETE |
| S051 | DOC-003 eFigure 4 major-bleeding forest vector: [p. 25](../../../joi180151supp2_prod.pdf#page=25) | 11 study rows; 2 pooled rows; heterogeneity | All estimates contained; event-ratio direction agrees. Fixed=random 1.42 (1.30-1.55), I2=0%, tau2=0; P=.54. This relative-risk vector does not supply the unrounded ARD inputs needed to resolve S034. | None | PASS_1_COMPLETE |
| S052 | DOC-003 eFigure 4 intracranial-bleeding forest vector: [p. 25](../../../joi180151supp2_prod.pdf#page=25) | 12 study rows; 2 pooled rows; heterogeneity | All estimates contained; event-ratio direction agrees. Fixed 1.33 (1.14-1.57), random 1.33 (1.13-1.57), I2=0%, tau2=0; P=.93. | None | PASS_1_COMPLETE |
| S053 | DOC-003 eFigure 4 major-GI-bleeding forest vector: [p. 26](../../../joi180151supp2_prod.pdf#page=26) | 10 study rows; 2 pooled rows; heterogeneity | All estimates contained; event-ratio direction agrees. Fixed 1.56 (1.38-1.78), random 1.55 (1.37-1.77), I2=0%, tau2=0; P=.54. | None | PASS_1_COMPLETE |

## Pass 1 coverage totals

- Stable statistical relationships: 53 (`S001`-`S053`).
- Main-paper provisional inferential relationships incorporated: 13/13.
- DIC/model-selection cells checked: 44/44.
- eTable 3 ARD cells checked: 44/44; displayed NNT/NNH cells checked: 18/18.
- eTable 4 total-stroke rows checked: 4/4.
- eTable 6 sensitivity HR/CrI cells checked: 44/44.
- eFigure 3 printed Egger relationships checked: 1/1.
- eFigure 4 study rows checked: 130/130; pooled fixed/random records checked: 22/22.
- Relationships lacking `PASS_1_COMPLETE`: 0.
- Pass-1 candidate proposals cross-referenced: 7 unique proposals (`SP1-001`-`SP1-007`).

## Definitions unavailable for exact compatibility checking

The package does not supply every Cox/mixed-model covariance detail, unrounded model coefficient, raw secondary P value, Holm ordering input, pattern-mixture estimate, medication-change sensitivity estimate, power-calculation input, MCMC output, trial-level HR-versus-person-time choice, posterior draw, unrounded ARD, ARD unit, or NNT/NNH rounding convention. Those absences are named above and no conventional value was silently substituted. Statistical pass 2 revisited all `S001`-`S053` using the complete cross-lane ledger and mechanical recheck; the missing inputs remain limitations.

## Pass 2 completion register

The complete `C001`-`C024` ledger, all checker outputs, and every mechanical recheck record were incorporated in `../checkers/statistical_pass_2.md`. The status pairs below preserve pass-1 completion and add the mandatory pass-2 completion record for every stable relationship.

| S ID | Existing candidate implications incorporated in pass 2 | Combined status |
|---|---|---|
| S001 | C001 framework context only | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S002 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S003 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S004 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S005 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S006 | C001 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S007 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S008 | C001 scale context | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S009 | C008, C009, C010 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S010 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S011 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S012 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S013 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S014 | C022, C023 interval-type context | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S015 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S016 | C011 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S017 | C021 context | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S018 | C017 population context | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S019 | C022, C023 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S020 | C012 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S021 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S022 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S023 | C022 interval context | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S024 | C022, C023 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S025 | C011, C013, C014, C015, C016, C021 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S026 | C013 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S027 | C013 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S028 | C013 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S029 | C013, C021 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S030 | C013 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S031 | C013 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S032 | C012 context, C013 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S033 | C013 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S034 | C013, C014, C015, C016 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S035 | C013 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S036 | C013 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S037 | C017, C020, C022, C024 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S038 | C023 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S039 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S040 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S041 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S042 | C019 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S043 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S044 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S045 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S046 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S047 | C020, C024 | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S048 | C024 comparator | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S049 | C012 context | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S050 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S051 | C014, C015, C016 context | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S052 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |
| S053 | None | PASS_1_COMPLETE; PASS_2_COMPLETE |

## Pass 2 totals

- Stable relationships with `PASS_2_COMPLETE`: 53/53.
- Existing ledger candidates considered: 24/24.
- Genuinely new pass-2 candidate proposals: 0.
