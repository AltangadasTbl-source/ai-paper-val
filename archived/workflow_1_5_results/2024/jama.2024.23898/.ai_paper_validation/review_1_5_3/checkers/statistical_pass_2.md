# Statistical Consistency Review — Pass 2

## Scope, independence, and method

This independent second statistical pass revisited every stable relationship
`S001` through `S033` after the complete candidate ledger (`C001`-`C007`) and
mechanical evidence recheck were available.  It reconciled each relationship
against the mapped source evidence, complete cross-lane candidate ledger, and
the recheck's direct-PDF facts.  The pass covered point-estimate containment,
interval ordering, sign/direction, measure and scale labels, duplicate or
cross-location values, and denominator/population, arithmetic, rate/count,
figure, and cross-source implications when applicable.

Interval/P-value compatibility below is explicitly **diagnostic** and was used
only where the supplied sources state compatible model, 95% CI, and two-sided
framework information.  No sidedness, degrees of freedom, covariance,
variance estimator, multiplicity rule, denominator, model, or estimand mapping
was inferred from convention.  The direct-source recheck facts for every
ledger ID were used as evidence; no old disposition or external source was
used.

No mapped relationship contains `P = 0`, `p = 0.000`, or an equivalent
finite-precision display zero.  Thus no individual `DISPLAY_ZERO_NOT_CANDIDATE`
record was required, and no candidate was created from display notation.

## Relationship-by-relationship pass-2 reconciliation

| Stable ID | Pass-2 reconciliation and cross-lane implication | Pass-2 status |
|---|---|---|
| S001 | The abstract difference and RR remain inside ordered 95% CIs with the printed negative direction and RR label. The 160/279 and 164/278 values, percentages, population, and repeated result agree with S002/S013. The unresolved 72-hour clock-origin wording is already C001; it is not a new inferential contradiction. | PASS_2_COMPLETE |
| S002 | Main text and Table 2 reproduce the S001 result and primary denominator. Under the supplied log-link/95%-CI framework, log-RR/normal compatibility with P=.54 remains a diagnostic approximation compatible with displayed precision. C001 remains the distinct clock-origin label issue. | PASS_2_COMPLETE |
| S003 | Per-protocol 154/267 and 158/265 values, percentages, difference, RR, ordered intervals, and negative direction reconcile. The displayed RR interval and P=.49 remain diagnostically compatible after rounding; no cross-lane contradiction beyond the separately labelled population is present. | PASS_2_COMPLETE |
| S004 | The sample-size statement's 60.0% to 73.2% return values equal a 13.2-point increase and are complements of the 40.0% to 26.8% non-return values in S030. No independent power recomputation is possible from supplied inputs. | PASS_2_COMPLETE |
| S005 | HR 0.98 is within ordered 0.83-1.17 limits and Cox/HR labels agree across supplied sources. No P, SE, statistic, or exact common time-origin definition is printed for a further compatibility calculation; no ungrounded comparison was made. | PASS_2_COMPLETE |
| S006 | HR 1.03 is within ordered 0.86-1.23 limits and Cox/HR labels agree. No P, SE, statistic, or complete compatible time-origin/model-output definition is supplied. | PASS_2_COMPLETE |
| S007 | PPOI difference 1.8 and IRR 1.13 are inside their ordered intervals; the failure-by-120-hour event direction and IRR/log-link labels reconcile with the support definition. No P/test/SE is supplied. | PASS_2_COMPLETE |
| S008 | All seven OBAS contrasts remain within ordered intervals; lower-is-better scale direction and repeated mixed-model labels agree. Displayed P values remain diagnostically compatible with stated time-by-treatment 95% contrasts after rounding. Raw means were not substituted for adjusted estimates. | PASS_2_COMPLETE |
| S009 | All QoR-15 contrasts remain within ordered intervals, with 0-150/higher-is-better scale and mixed-model labels consistent. Displayed P values remain diagnostically compatible after rounding; no duplicate or cross-source conflict is shown. | PASS_2_COMPLETE |
| S010 | All EQ-5D contrasts remain within ordered intervals with scale/model labels consistent. The day-5 estimate, CI excluding zero, and P=.04 are diagnostically compatible under the supplied nominal 95% framework. Its conflict with blanket no-significance prose is already C006; the supplied sources lack an endpoint-level narrative decision rule, so no additional candidate was created. | PASS_2_COMPLETE |
| S011 | Both discharge-readiness HRs (0.99) remain within their ordered intervals and labels distinguish clinician-assessed from patient-assessed outcomes. Article Cox wording and support GLM/code wording do not establish one identical estimand for a new P/SE test. | PASS_2_COMPLETE |
| S012 | Length-of-stay IRR 1.03 is within ordered 0.92-1.14 limits, with negative-binomial/IRR label agreement. The support source has planned rather than populated output, and no P/test/SE is supplied. The related readmission-window issue is C003, not an IRR inconsistency. | PASS_2_COMPLETE |
| S013 | The eFigure overall RR 0.97 (0.88-1.07) duplicates S001/S002 at displayed precision. The figure's 99% legend concerns subgroup bars; the overall repeated 95% result is not thereby contradicted. The figure's incompatible subgroup CI labels are already C005. | PASS_2_COMPLETE |
| S014 | Each intended-duration subgroup RR lies in its ordered displayed interval and its Ns total 532, the treatment-recipient population. The 99% legend/95% caption conflict for the same subgroup intervals is C005; interaction P=.401 cannot be recomputed without the interaction covariance/model output. | PASS_2_COMPLETE |
| S015 | Each operation subgroup RR lies in its ordered interval and Ns total 557. C005 applies to the printed subgroup-interval confidence label; P=.773 has no supplied inputs for an independent interaction-test calculation. | PASS_2_COMPLETE |
| S016 | Each sex subgroup RR lies in its ordered interval and Ns total 557. C005 applies to the printed subgroup-interval confidence label; P=.830 has no supplied interaction covariance or test output. | PASS_2_COMPLETE |
| S017 | Each age subgroup RR lies in its ordered interval and Ns total 557. C005 applies to the printed subgroup-interval confidence label; P=.162 has no supplied interaction covariance or test output. | PASS_2_COMPLETE |
| S018 | Each ERAS subgroup RR lies in its ordered interval and high/moderate/low Ns total 557. C005 covers the CI-level conflict; C007 covers the article's two-level wording versus three displayed levels; C004 remains the separate protocol/eFigure category-definition question. No factor coding or interaction covariance is supplied. | PASS_2_COMPLETE |
| S019 | Supplied primary-estimand, binary coding, ITT population, log link, centre random effect, robust variance, and exponentiation agree with the main RR label. The SAP's stated post-analysis correction from logit to log is provenance, not a conflicting final displayed estimate. C001's clock-origin wording remains separately recorded. | PASS_2_COMPLETE |
| S020 | GI-2/GI-3 definitions and Cox planning labels support S005-S006. The supplied sources use nonidentical time-origin wording and do not supply matched HR P values, SEs, statistics, or final model output; no inference beyond that documented limitation is warranted. | PASS_2_COMPLETE |
| S021 | PPOI binary coding, 120-hour failure direction, and adjusted log-link plan agree with S007. No P, statistic, or SE is supplied for additional compatibility testing. | PASS_2_COMPLETE |
| S022 | PONV score threshold, daily denominator definitions, and count labels are supplied, but there is no inferential estimate, interval, or P for these counts. No statistical compatibility rule applies. | PASS_2_COMPLETE |
| S023 | OBAS formula, missing-item rule, lower-is-better direction, and mixed-model definition agree with S008. The supplied plan does not expose enough fitted-model output to reproduce exact time-specific tests. | PASS_2_COMPLETE |
| S024 | QoR-15 range/direction, collection points, and repeated-model definition agree with S009. No additional exact test inputs are supplied. | PASS_2_COMPLETE |
| S025 | EQ-5D time points, repeated-model definition, and distinct health-economic measures agree with S010. The sources do not state an omnibus/endpoint-level narrative rule that resolves C006, and no such rule was inferred. | PASS_2_COMPLETE |
| S026 | The SAP and eFigure identify high/moderate/low ERAS categories, whereas the article says high vs low (C007); the protocol's example percentage bands versus eFigure thresholds are C004. Neither record supplies final factor coding or a different inferential result, so neither generates a new candidate. | PASS_2_COMPLETE |
| S027 | Five medical criteria versus those five plus patient willingness distinguish S011's two outcomes. Article and support model wording do not establish a single identical estimand for an additional P/SE comparison. | PASS_2_COMPLETE |
| S028 | The support source assigns adjusted analysis to total stay and exploratory/descriptive treatment to mortality, readmission, and complications; that aligns with S012's sole printed IRR. The 30-versus-90-day readmission label conflict is already C003 and does not identify a new inferential-statistic mismatch. | PASS_2_COMPLETE |
| S029 | Participant-level 1:1 allocation, ITT, treatment-received, and per-protocol definitions reconcile the denominators used in S001-S004 and S014. No incompatible population was found after distinguishing analysis sets. | PASS_2_COMPLETE |
| S030 | The 562, 90%, two-sided 5%, and 40% to 26.8% non-return basis exactly reconciles with S004 by complement arithmetic. Inputs are insufficient for an independent power calculation. | PASS_2_COMPLETE |
| S031 | The SAP states 95% CIs except subgroups and no secondary multiplicity adjustment. That supports reading the day-5 S010 row as nominal, while not supplying a narrative rule that resolves C006; no multiplicity convention was inferred. | PASS_2_COMPLETE |
| S032 | The SAP's two-sided 1% subgroup threshold and corresponding 99% CIs independently match the eFigure legend and conflict with its 95% caption, already C005. It also supplies the three-level ERAS framework relevant to C007. | PASS_2_COMPLETE |
| S033 | The p-POSSUM formula, component ranges, and missing-item rule are planned/template material only. No populated observed prediction, interval, or P exists for a statistical cross-check. | PASS_2_COMPLETE |

## Pass-2 candidate outcome

No genuinely new candidate observation was identified.  The seven stable
ledger records are the complete cross-lane implications encountered here:

- C001: primary 72-hour clock-origin wording (S001, S002, S019).
- C002: postoperative opioid 24-hour versus 72-hour window (non-inferential
  measure relationship; no new S-level contradiction).
- C003: 90-day versus 30-day readmission window (S012/S028 context).
- C004: ERAS category cut-point question (S018/S026 context).
- C005: eFigure subgroup 99% versus 95% CI label conflict (S013-S018, S032).
- C006: day-5 EQ-5D row versus blanket prose (S010, S025, S031).
- C007: two-level versus three-level ERAS subgroup label (S018, S026, S032).

These entries are referenced rather than reissued because their printed values,
comparators, and consistency rules are unchanged.  No candidate is based on a
display-zero P value.

## Limitations

The supplied package lacks participant-level data, final fitted-model output,
interaction covariance/contrast matrices, degrees of freedom, and several
reported HR/IRR P values, SEs, and statistics.  It also lacks a final endpoint
derivation/amendment record that resolves the clock, opioid, readmission, and
ERAS-definition questions, plus a stated EQ-5D narrative decision rule.  These
missing definitions were recorded as limitations and were not supplied by
convention.

Pass 2 counts: **33 relationships reviewed; 0 new candidate observations; 0
display-zero candidates.**
