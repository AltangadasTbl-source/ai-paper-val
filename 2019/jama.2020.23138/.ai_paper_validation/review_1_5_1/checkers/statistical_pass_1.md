# Statistical Consistency Review — Pass 1

- **Runtime agent ID:** `/root/statistical_pass_1`
- **Execution:** fresh statistical-pass agent; `gpt-5.6-terra`, high reasoning effort.
- **Scope:** all 90 registered inferential relationships: S001-S025, S1001-S1013, S2001-S2018, and S3001-S3034.
- **Evidence used:** the canonical statistical inventory; its four source-specific parts; the four quantitative-extraction parts; and targeted direct-PDF confirmation against DOC-001 through DOC-004. DOC-005 contains no statistical relationship.
- **Boundary:** no legacy candidate, checker, verifier, critic, or report content was consulted. No candidate ID, severity, validity, or adjudication was assigned here.

## Applied checks and compatibility limits

For every realized estimate, I checked point-estimate containment, endpoint order, null/sign/direction, effect-measure and scale labels, matched repetitions, and duplicate-value implications. Where a reported effect, two-sided 95% CI, and P value belonged to the same expressly described adjusted model, a normal-approximation calculation from CI width was used only as a **diagnostic**; it was consistent with the printed P-value precision. It does not recreate the fitted model.

No model-based P/test/SE/statistic reconstruction was performed when the source did not supply a compatible model, confidence level, sidedness, variance estimator, degrees of freedom, covariance, adjustment rule, or estimand mapping. In particular, the protocol/SAP blank templates and the end-uptitration 24-hour comparison do not establish all such definitions. No coherent `P = 0`, `p = 0.000`, or equivalent finite-precision display-zero occurs in this scope. The printed `P < .001` values are threshold displays, not display zeros.

## Candidate proposals for coordinator-led duplicate merge

These are distinct candidate proposals, not C IDs and not adjudications.

### P1-PROP-01 — Primary-endpoint measure label differs within the protocol

- **Relationships:** S1001, S1005; matched to S002/S023.
- **Direct observations:** DOC-002 p. 21 calls the primary QoL measure the SF-36 “physical functioning domain”; DOC-002 pp. 22 and 54 name the primary objective/outcome the SF-36 “physical component summary”; DOC-002 p. 56 again calls the primary outcome the “physical functioning domain score.” DOC-001 pp. 1 and 6 report the realized primary result as SF-36 physical component summary (PCS).
- **Consistency rule:** physical functioning is an SF-36 domain, whereas PCS is a distinct summary measure; the protocol assigns both labels to the same six-month primary endpoint.
- **Reproducible question:** which measure was the prespecified primary endpoint, and should the two physical-functioning references be corrected or explicitly reconciled with PCS?

### P1-PROP-02 — AFEQT template footnote names the wrong instrument

- **Relationship:** S2009.
- **Direct observations:** DOC-003 p. 19 identifies the outcome as the AFEQT overall score; its Appendix D6 AFEQT table on p. 36 labels the row “AFEQT overall score” but footnote `£` says, “The range for visual analogue score is from 0=worst score to 100=best score.”
- **Consistency rule:** the footnote is attached to the AFEQT table but names the EQ-5D visual analogue score, a separate instrument in the preceding table.
- **Reproducible question:** is the p. 36 footnote a copied VAS label that should identify AFEQT instead?

### P1-PROP-03 — E/e′ direction statement reverses the planned favorable direction

- **Relationships:** S2011; cross-source implication S017.
- **Direct observations:** DOC-003 p. 20 says lower E/e′ values indicate a better outcome for digoxin. Its E/e′ template on p. 37 states, “Higher values indicate better scores so a positive mean difference favours Digoxin arm.” DOC-001 p. 7 reports the E/e′ adjusted difference as -0.1 (95% CI -1.1 to 0.9), so the definition is relevant to interpreting the reported direction.
- **Consistency rule:** for the same named E/e′ measure and Digoxin-minus-bisoprolol contrast, the two supplied direction labels cannot both be correct.
- **Reproducible question:** should the p. 37 E/e′ direction statement be made measure-specific and changed to lower values/negative difference favoring digoxin?

### P1-PROP-04 — NT-proBNP template time heading conflicts with its displayed rows

- **Relationship:** S2015.
- **Direct observations:** DOC-003 p. 21 specifies NT-proBNP collection at baseline, 6 months, and 12 months, with separate 6- and 12-month analyses. The Appendix D6 table on p. 40 is headed “Change in ... NTproBNP levels at 6 months” yet displays baseline, 6-month, and 12-month rows. DOC-001 pp. 6-7 reports both 6- and 12-month NT-proBNP results.
- **Consistency rule:** a table titled only “at 6 months” does not match its own 12-month row or the stated two-time-point analysis.
- **Reproducible question:** should the p. 40 template heading name both 6 and 12 months (or otherwise delimit the displayed rows)?

### P1-PROP-05 — EHRA example uses a category absent from the stated scale

- **Relationship:** S2014.
- **Direct observations:** DOC-003 p. 18 defines the modified EHRA categories as 1, 2a, 2b, 3, and 4, then illustrates a two-class improvement with baseline “3a” to 2a.
- **Consistency rule:** `3a` is not among the categorical values defined immediately above the example.
- **Reproducible question:** is “3a” a typographic error (for class 3) in the binary-improvement specification?

### P1-PROP-06 — Heart-rate table footnote labels its direction as quality of life

- **Relationship:** S3016.
- **Direct observations:** DOC-004 p. 14 is eTable 2, “Resting and exertional heart rate,” measured in beats/min. Its footnote `a` states that the adjusted differences are relative to beta-blockers and “hence higher values represent better quality of life in the digoxin arm.” DOC-004 p. 15 eTable 3 uses the same covariate wording for actual quality-of-life scores.
- **Consistency rule:** eTable 2 contains heart-rate outcomes, not a quality-of-life scale; the attached wording assigns a different measure/interpretive label to the table.
- **Reproducible question:** should the eTable 2 footnote omit the quality-of-life clause or give a heart-rate-specific directional interpretation?

## Relationship dispositions

`PASS_1_COMPLETE` is a coverage disposition only. `NO_CANDIDATE_ON_THIS_CHECK` means no independent contradiction was found for the stated relationship. `MISSING_DEFINITION_LIMIT` identifies a precisely missing supplied definition; it is not a candidate. `CANDIDATE_PROPOSAL` points only to the proposal above.

| Relationship ID | PASS 1 disposition | Concise source-grounded result |
|---|---|---|
| S001 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Design arithmetic 144/(1-.10)=160; two-sided alpha and planned PCS effect stated. |
| S002 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Adjusted PCS difference lies within ordered CI; CI includes 0 and P=.28; main/abstract/editorial match. |
| S003 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Unnormalized PCS result is a separate scale; estimate/CI/P internally coherent. |
| S004 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Six-month resting-HR difference is contained in ordered CI and matches P=.40/direction. |
| S005 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Twelve-month resting-HR difference is contained in ordered CI and matches P=.87. |
| S006 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | End-uptitration 24-hour-HR difference/CI/P=.02 agree; distinct time/measure from resting HR. |
| S007 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Binary-improvement OR and CI are >1 with P<.001; direction and arm percentages agree. |
| S008 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Twelve-month binary-improvement OR/CI/P and 50/73 vs 21/72 counts agree. |
| S009 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Ordinal-EHRA ORs <1 have ordered CIs excluding 1; coding differs explicitly from S007/S008. |
| S010 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Geometric-mean ratios use null 1; CIs/P values and 6-/12-month directions agree. |
| S011 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Twelve-month PCS difference/CI/P=.29 coherent. |
| S012 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Borderline printed CIs and P values are compatible at display precision; no false exact-null inference. |
| S013 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | EQ-5D index and VAS are distinct scales; their directions, CIs, and P values agree. |
| S014 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | AFEQT overall/subscale effects have ordered CIs and matching P directions; post-hoc labels retained. |
| S015 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Negative NYHA differences accord with lower class being better; CIs/P<.001 coherent. |
| S016 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Walk geometric-mean ratio uses null 1 and CI contains 1 with P=.25. |
| S017 | PASS_1_COMPLETE — CANDIDATE_PROPOSAL | E/e′ result itself is contained/ordered with P=.81, but direction must be read with P1-PROP-03. |
| S018 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Diastolic-composite OR CI includes 1 and P=.73; measure remains distinct from E/e′. |
| S019 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | Counts and chi-square/P<.001 are repeated consistently; df/variance details are not supplied for exact compatibility calculation. |
| S020 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Incidence-rate ratio is correctly distinguished from patient proportion; stated negative-binomial/offset model supports its scale. |
| S021 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Narrative 8 significant plus 12 null equals the stated 20 twelve-month outcomes. |
| S022 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Model/complete-case/two-tailed threshold definitions align with reported result descriptions. |
| S023 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | PCS scale and six-month endpoint definition agrees with the reported PCS result. |
| S024 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Ordinal model/coding and proportional bars distinguish Figure 2 from binary-improvement results. |
| S025 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Editorial P=.28 and P=.005 repetitions agree at matched precision; no omitted-interval conflict. |
| S1001 | PASS_1_COMPLETE — CANDIDATE_PROPOSAL | Primary endpoint is labeled physical functioning on p.21 but PCS on pp.22/54; see P1-PROP-01. |
| S1002 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Planned power/attrition arithmetic and main planning statement agree. |
| S1003 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Protocol ITT versus main received-dose full set produces no observed count conflict because all 160 received therapy. |
| S1004 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Threshold definition only; no display-zero or realized P value. |
| S1005 | PASS_1_COMPLETE — CANDIDATE_PROPOSAL | ANCOVA is attached to the protocol’s differing physical-functioning label; see P1-PROP-01. |
| S1006 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | OR/RR alternatives are not treated as interchangeable; realized binary results identify their measure. |
| S1007 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Planned continuous-outcome model has no conflicting realized definition. |
| S1008 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Available-data/no-imputation plan agrees with main complete-case statement; no different printed denominator. |
| S1009 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | DMC charter/stopping rule, test, sidedness, and model are expressly unresolved; no calculation permitted. |
| S1010 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Final-analysis timing is compatible with reported 12-month follow-up. |
| S1011 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | Reproducibility method has no stated inferential model or matched statistic. |
| S1012 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | Exploratory correlations lack a stated test/model/threshold and no realized result is supplied. |
| S1013 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | Economic plan gives no uncertainty model or realized effect for statistical compatibility. |
| S2001 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Planning power and attrition quantities match S001/S1002; no realized estimate. |
| S2002 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | Superiority/interim threshold has no interim result or specified test/sidedness for compatibility. |
| S2003 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Two-sided 95% CI/test convention agrees with analyzed main relationships. |
| S2004 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | Alternative binary-model routes/convergence outcome are not reported; no model route inferred. |
| S2005 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Planned PCS model/reference/direction agrees with main PCS result; template is blank. |
| S2006 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | No repeated-model interaction/result or covariance realization is supplied. |
| S2007 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Planned SF-36 scale/reference and main reported domain results agree. |
| S2008 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Planned EQ-5D scales and reference agree with main index/VAS reporting. |
| S2009 | PASS_1_COMPLETE — CANDIDATE_PROPOSAL | AFEQT table footnote calls its range visual analogue score; see P1-PROP-02. |
| S2010 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | LVEF definition/covariates have no source conflict with the reported 12-month effect. |
| S2011 | PASS_1_COMPLETE — CANDIDATE_PROPOSAL | E/e′ p.20 lower-is-better conflicts with p.37 positive-is-better; see P1-PROP-03. |
| S2012 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | One-time 24-hour measure is specified but no exact realized timing/model definition links every table placement. |
| S2013 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Walk distance, unit, and linear-model plan have no label or cross-source contradiction. |
| S2014 | PASS_1_COMPLETE — CANDIDATE_PROPOSAL | The defined EHRA categories exclude illustrative `3a`; see P1-PROP-05. |
| S2015 | PASS_1_COMPLETE — CANDIDATE_PROPOSAL | p.40 says “at 6 months” but displays baseline/6-/12-month rows; see P1-PROP-04. |
| S2016 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | Blank safety templates provide no realized P/statistic; counts and events remain separate measures. |
| S2017 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | Subgroup interaction template is blank; no interaction statistic/model output to compare. |
| S2018 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | Sensitivity/MI specifications have no realized sensitivity result. |
| S3001 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | 24-hour HR P=.020 is distinct from no-difference 12-lead series; test/model/variance not supplied. |
| S3002 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Sex subgroup estimates lie in ordered CIs; interaction P=.644 has no contradictory matched result. |
| S3003 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | EHRA subgroup estimates lie in ordered CIs; interaction P=.845 is compatible in stated direction. |
| S3004 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Prior-beta-blocker subgroup estimates/CI and interaction P=.575 are coherent. |
| S3005 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Age subgroup estimates/CI and interaction P=.431 are coherent. |
| S3006 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | LVEF subgroup estimates/CI and interaction P=.637 are coherent. |
| S3007 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | Only interaction P=.80 is printed; subgroup effects/test details are absent. |
| S3008 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | NYHA -0.55 CI/P<.001 agrees with lower-is-better and main -0.6 at rounding precision. |
| S3009 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | NYHA -0.58 CI/P<.001 agrees with lower-is-better and main -0.6 at rounding precision. |
| S3010 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Both adjusted 12-lead-HR effects lie in ordered CIs; P values and main repetitions agree. |
| S3011 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Apex-HR effects are contained in ordered CIs with compatible displayed P values. |
| S3012 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Radial-HR effects are contained in ordered CIs with compatible displayed P values. |
| S3013 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Pulse-deficit effects are contained in ordered CIs; post-hoc and derived-measure labels retained. |
| S3014 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Post-walk radial-HR effects are contained in ordered CIs with compatible displayed P values. |
| S3015 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Exertion-minus-rest effects are contained in ordered CIs with compatible P values. |
| S3016 | PASS_1_COMPLETE — CANDIDATE_PROPOSAL | Heart-rate table footnote says higher values mean better quality of life; see P1-PROP-06. |
| S3017 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | PCS estimates/CIs/P values match main table/abstract and scale labels. |
| S3018 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | MCS estimates/CIs/P values are internally coherent. |
| S3019 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Physical-function effects/ordered CIs/P values agree across table and main narrative. |
| S3020 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Role-physical effects/ordered CIs/P values agree across locations. |
| S3021 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Bodily-pain effects/ordered CIs/P values are coherent. |
| S3022 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Figure .049 rounds to table .05; effect/CI direction matches. |
| S3023 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Figure .013 rounds to table .01; effect/CI direction matches. |
| S3024 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Social-function effects/ordered CIs/P values are coherent. |
| S3025 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Role-emotional effects/ordered CIs/P values are coherent. |
| S3026 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Mental-health effects/ordered CIs/P values are coherent. |
| S3027 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | EQ-5D index scale/effects/CI/P agree; null is 0. |
| S3028 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Figure .038 rounds to table .04; VAS effect/CI direction matches. |
| S3029 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | AFEQT-overall effects/ordered CIs/P values are coherent. |
| S3030 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Post-hoc AFEQT-symptoms effects/ordered CIs/P values are coherent. |
| S3031 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Post-hoc daily-activities effects/ordered CIs/P values are coherent. |
| S3032 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Post-hoc treatment-concern effects/ordered CIs/P values are coherent. |
| S3033 | PASS_1_COMPLETE — NO_CANDIDATE_ON_THIS_CHECK | Post-hoc treatment-satisfaction effects/ordered CIs/P values are coherent. |
| S3034 | PASS_1_COMPLETE — MISSING_DEFINITION_LIMIT | Patient counts/percentages match main; chi-square P<.001 is repeated, but df/test computation details are not supplied. |

## Counts and limitations

- **Relationships reviewed:** 90/90.
- **Candidate proposals:** 6 (P1-PROP-01 through P1-PROP-06); none has a stable C ID in this pass.
- **Coherent display zeros:** 0; `P < .001` threshold notation was not treated as `DISPLAY_ZERO_NOT_CANDIDATE` because it is not a displayed zero.
- **Main limitation:** exact numerical P/CI/test reconciliation was deliberately withheld where compatible model and inferential definitions were not supplied. The marked missing-definition rows identify the unavailable definition rather than filling it from convention.
