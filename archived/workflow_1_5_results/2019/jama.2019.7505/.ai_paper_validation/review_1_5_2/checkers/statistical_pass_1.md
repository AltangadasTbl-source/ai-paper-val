# Statistical Consistency Review — Pass 1

## Independent-pass scope

Fresh independent statistical pass 1 covered every assigned relationship in the canonical inventory: S001–S038 and S200–S214 (53 total). Sources used were the supplied six PDFs and current-run native/layout text and renders under `review_1_5_2/preprocessing/`, plus the current fresh mapper artifacts. No web source, preserved prior-run derivative, old candidate list, or adjudication was used.

The durable per-relationship records, including `PASS_1_COMPLETE`, are in `statistics/relationship_inventory.md`. This checker records the pass rules, candidate proposals, and definitions that prevent a stricter mechanical test. It does not assign C IDs, severity, validity, verification, acceptance, or correction.

## Applied pass-1 checks

- Point estimate within its displayed interval; lower endpoint no greater than upper endpoint.
- Direction/sign agreement among displayed group values, absolute differences, RR/HR/mean-difference labels, CIs, and prose/figure repetitions.
- Effect-measure, scale, reference-direction, and model labels where printed.
- Cross-location identity only after matching outcome, population, time horizon, contrast, and analysis type.
- Interval/P/test/statistic/SE compatibility only when the supplied source specifies a compatible model and inferential rule. Calculations described as diagnostic are approximations, not substitutes for the printed analysis.
- No literal `P = 0`, `p = 0.000`, or equivalent P-value display zero occurred in this assigned scope. Thus no display-zero candidate was generated and no threshold was reconstructed.

## Candidate proposals for coordinator merge

### P1 — Hypoxemia absolute-difference interval differs and reverses direction across abstract and Table 3

- **Relationship ID:** S002
- **Category proposed:** Cross-document numeric inconsistency; Statistical reporting inconsistency.
- **Exact source locations:** DOC-001, `jama_bluth_2019_oi_190055_16092.pdf`, PDF p.1 abstract and PDF p.9 Table 3.
- **Printed comparator:** Both locations report high versus low hypoxemia difference `−8.6%` and `P < .001`. The abstract prints `95% CI, −11.1% to 6.1%`; Table 3 prints `−8.6 (−11.1 to −6.1)`, with RR `0.51 (0.40 to 0.65)`.
- **Rule/calculation:** Both printed intervals contain the matched high-minus-low difference of `−8.6%`. However, the abstract's positive upper endpoint conflicts with the same-result Table 3 upper endpoint, and it crosses the null while the matched Table 3 interval, RR interval, and `P < .001` do not. The Table 3 comparator is internally coherent: `−11.1 ≤ −8.6 ≤ −6.1`.
- **Direct observation versus inference:** Direct observation is the differing sign at the upper endpoint. The inference that one endpoint is likely a sign/transcription error is not treated as a correction.
- **Alternative interpretation / missing definition:** No population, time, or contrast qualifier differentiating the abstract and Table 3 result is printed. A human should check the publisher correction history and production source.
- **Duplicate key:** `DOC001|hypoxemia|ITT_989_vs_987|absolute_difference_-8.6|abstract_CI_-11.1_to_+6.1|table3_CI_-11.1_to_-6.1`.

### P2 — DIC risk-ratio display is not reconciled with its displayed zero-event comparator under the supplied RR rule

- **Relationship ID:** S027
- **Category proposed:** Statistical reporting inconsistency; Measure, label, or scale inconsistency.
- **Exact source location:** DOC-001, `jama_bluth_2019_oi_190055_16092.pdf`, PDF p.9 Table 3; applicable method/footnote on PDF p.10 and method text on PDF p.4.
- **Printed comparator:** The DIC row reports high PEEP `1 (0.1)` and low PEEP `0`, absolute difference `.1 (−.1 to .3)`, `Risk Ratio 2.00 (1.91 to 2.09)`, `P > .99`. Table 3 says its data are risk ratios unless otherwise indicated and says RR/95% CIs use the Wald likelihood-ratio approximation; P values use chi-square.
- **Rule/calculation:** Under the printed uncorrected risks, the high risk is `1/989` and the low risk is `0/987`; their ratio has a zero denominator and therefore is not the finite printed RR `2.00`. The exceptionally narrow printed interval is centred on that finite RR. This is a direct counts-versus-measure reconciliation check, not a reconstructed P-value test.
- **Direct observation versus inference:** Direct observation is the zero low-group event count alongside a finite RR and CI. No claimed replacement effect estimate or P value is derived.
- **Alternative interpretation / missing definition:** A zero-cell correction, alternative estimator, or a non-displayed denominator/analysis population could have been used, but none is specified in the supplied Table 3 method/footnote. The printed `P > .99` could also depend on an unstated chi-square continuity convention; this proposal does not rely on a P reconstruction.
- **Duplicate key:** `DOC001|table3|DIC|high_1_of_989|low_0_of_987|RR_2.00_CI_1.91_2.09`.

### P3 — Protocol sentence combines distinct effect-measure labels for a logistic-regression analysis

- **Relationship ID:** S202
- **Category proposed:** Measure, label, or scale inconsistency.
- **Exact source location:** DOC-002, `joi190055supp1_prod_16092.pdf`, physical PDF p.23 (footer p.22), section 8.2 Analysis.
- **Printed comparator:** “the odds ratio relative risks with corresponding 95% confidence levels interval will be calculated using logistic regression analysis.” The same protocol uses `relative risk` for its sample-size target; the final SAP (DOC-004 PDF pp.1-3) explicitly calls the final primary effect a `risk ratio`.
- **Rule/calculation:** `odds ratio` and `risk ratio` are separately named effect-measure labels in the supplied documents. One output phrase labels the same planned logistic-regression result as both, without a separator, estimand definition, or conversion rule; the label cannot be uniquely mapped from the supplied text.
- **Direct observation versus inference:** The direct observation is the compound label. It is not assumed that logistic regression necessarily fixes the intended estimand, link, or conversion.
- **Alternative interpretation / missing definition:** The sentence could be an editing/grammar error, could intend alternative analyses, or could use a conversion not described. A human should identify the intended effect measure for this superseded protocol plan.
- **Duplicate key:** `DOC002|p22|primary_efficacy|odds_ratio_relative_risks|logistic_regression`.

### P4 — Per-protocol effect-estimate column has no effect-measure label

- **Relationship ID:** S208
- **Category proposed:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-005, `joi190055supp4_prod_16092.pdf`, PDF p.29 eTable 8; related primary-analysis labels in DOC-004 PDF pp.1-3 and DOC-001 PDF p.9 Table 3.
- **Printed comparator:** eTable 8 heads the numeric column `Effect Estimate 95% CI`, then prints values such as PPC `0.92 (0.82–1.04)`. Its column does not say RR, OR, HR, mean ratio, or another effect measure. The final SAP labels the primary analysis RR, while the main Table 3 identifies its ITT effects as risk ratios.
- **Rule/calculation:** The table's estimate and interval are supplied but its scale/measure label is absent. The source does not expressly state that the final-SAP ITT risk-ratio definition applies unchanged to this per-protocol component table. Therefore the numeric column cannot be unambiguously identified from its own label and source-grounded comparator.
- **Direct observation versus inference:** The missing eTable 8 label is direct. Treating the values as RRs based only on numerical resemblance or convention would be an unsupported estimand mapping and is not done here.
- **Alternative interpretation / missing definition:** The omitted label may have been intended as risk ratio, given nearby documents, but the supplied package does not explicitly map it. Human review should confirm the effect measure and whether a table-header omission occurred.
- **Duplicate key:** `DOC005|p29|eTable8|per_protocol|effect_estimate_CI|missing_measure_label`.

### P5 — eFigure 11 narrative names extra-pulmonary complications while the figure and effect label identify mortality

- **Relationship ID:** S214
- **Category proposed:** Cross-document numeric inconsistency; Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-005, `joi190055supp4_prod_16092.pdf`, PDF p.41 eFigure 11; comparator DOC-001, `jama_bluth_2019_oi_190055_16092.pdf`, PDF p.10 Table 3.
- **Printed comparator:** eFigure 11 is headed `Probability of death in the first 5 postoperative days`; it reports `.5%`/`.3%` and “hazard ratio for 5-day mortality, 1.67; 95% confidence interval 0.40 to 6.97; P=0.484.” Its preceding narrative sentence calls those same rates “postoperative extra-pulmonary complications.” Main Table 3 labels the matched 5-day row `Mortality at 5 d`, HR `1.67 (0.40 to 6.97)`, P `.48`.
- **Rule/calculation:** The identical HR, CI, time horizon, and group rates match the mortality result, while the same eFigure's narrative uses a different outcome name. No arithmetic approximation is needed.
- **Direct observation versus inference:** Direct observation is the conflicting outcome label within eFigure 11 and against Table 3. Calling one label an error would be a human correction decision and is not made here.
- **Alternative interpretation / missing definition:** The narrative could be a carry-forward label from eFigure 10, but no source statement identifies it as such. A human should verify the intended outcome name in the source figure.
- **Duplicate key:** `DOC005|p41|eFigure11|death_vs_extrapulmonary_label|HR_1.67_CI_0.40_6.97`.

## Diagnostic approximations and missing definitions

- S211–S213: log-HR/rounded-CI Wald diagnostics are approximately P=.18, .20, and .32, versus printed .190, .197, and .314. These are not candidates because the source does not identify a common effect-test statistic, interval construction, or full-precision inputs. The separate Schoenfeld P values test a different stated quantity.
- S005–S019: Table 2 supplies values, CIs, and P values but does not name the table-specific test, interval method, variance estimator, repeated-time handling, or degrees of freedom. Containment, ordering, displayed direction, and coherent finite rounding were checked; no strict P/CI reconstruction was performed.
- S200–S201: group-sequential sample-size and boundary calculations depend on the named spending/software implementation and sidedness details not fully printed. Exact repeated source values were checked, but no convention was imported.
- S207 and S210: support tables/figures do not supply all test, variance, coordinate, or repeated-measures definitions required to calculate their P values from printed summaries.
- S027: the candidate proposal is limited to the counts-versus-finite-RR display. It deliberately does not reconstruct or criticize `P > .99`, as a zero-cell correction/continuity convention is not defined.

## Explicit pass-1 relationship completion index

This index makes the uncapped per-relationship coverage mechanically explicit; detailed relationship records are in `statistics/relationship_inventory.md`.

| Relationship ID | Pass-1 coverage |
|---|---|
| S001 | PASS_1_COMPLETE |
| S002 | PASS_1_COMPLETE |
| S003 | PASS_1_COMPLETE |
| S004 | PASS_1_COMPLETE |
| S005 | PASS_1_COMPLETE |
| S006 | PASS_1_COMPLETE |
| S007 | PASS_1_COMPLETE |
| S008 | PASS_1_COMPLETE |
| S009 | PASS_1_COMPLETE |
| S010 | PASS_1_COMPLETE |
| S011 | PASS_1_COMPLETE |
| S012 | PASS_1_COMPLETE |
| S013 | PASS_1_COMPLETE |
| S014 | PASS_1_COMPLETE |
| S015 | PASS_1_COMPLETE |
| S016 | PASS_1_COMPLETE |
| S017 | PASS_1_COMPLETE |
| S018 | PASS_1_COMPLETE |
| S019 | PASS_1_COMPLETE |
| S020 | PASS_1_COMPLETE |
| S021 | PASS_1_COMPLETE |
| S022 | PASS_1_COMPLETE |
| S023 | PASS_1_COMPLETE |
| S024 | PASS_1_COMPLETE |
| S025 | PASS_1_COMPLETE |
| S026 | PASS_1_COMPLETE |
| S027 | PASS_1_COMPLETE |
| S028 | PASS_1_COMPLETE |
| S029 | PASS_1_COMPLETE |
| S030 | PASS_1_COMPLETE |
| S031 | PASS_1_COMPLETE |
| S032 | PASS_1_COMPLETE |
| S033 | PASS_1_COMPLETE |
| S034 | PASS_1_COMPLETE |
| S035 | PASS_1_COMPLETE |
| S036 | PASS_1_COMPLETE |
| S037 | PASS_1_COMPLETE |
| S038 | PASS_1_COMPLETE |
| S200 | PASS_1_COMPLETE |
| S201 | PASS_1_COMPLETE |
| S202 | PASS_1_COMPLETE |
| S203 | PASS_1_COMPLETE |
| S204 | PASS_1_COMPLETE |
| S205 | PASS_1_COMPLETE |
| S206 | PASS_1_COMPLETE |
| S207 | PASS_1_COMPLETE |
| S208 | PASS_1_COMPLETE |
| S209 | PASS_1_COMPLETE |
| S210 | PASS_1_COMPLETE |
| S211 | PASS_1_COMPLETE |
| S212 | PASS_1_COMPLETE |
| S213 | PASS_1_COMPLETE |
| S214 | PASS_1_COMPLETE |

## Pass-1 totals

- **Relationship scope completed:** 53 (S001–S038; S200–S214).
- **Candidate proposals:** 5 (P1–P5); no stable C ID assigned.
- **Literal P-value display-zero cases:** 0; `DISPLAY_ZERO_NOT_CANDIDATE` applicable cases: 0.
- **Primary durable artifact:** `checkers/statistical_pass_1.md`.
