# Statistical Consistency Review — Pass 1

## Scope and method

**Assigned and completed scope:** `S001-S031`, `S200-S215`, and `S400-S410` (58/58 relationships). Sources were the freshly prepared direct-source text/layout assets and rendered pages for DOC-001, DOC-002, and DOC-003. This pass checked printed point estimates, interval containment and ordering, sign/direction, effect-measure/scale/model/population/time/contrast labels, repeated locations, supplied denominator arithmetic, and inferential compatibility only where the source stated a compatible rule.

`PASS_1_COMPLETE` means the relationship received the stated checks; it is not a validity, severity, or adjudication decision. A missing definition is named rather than inferred. Any diagnostic calculation below is explicitly labelled and is not substituted for the reported analysis. No `P = 0`, `P = 0.000`, or equivalent display-zero result occurred in this scope; **DISPLAY_ZERO_NOT_CANDIDATE count: 0**.

## Provisional candidates emitted in this pass

### STAT1-001 — Figure 3 HIV-negative subgroup relative-risk point estimate does not reconcile with its displayed counts

- **Category:** Statistical reporting inconsistency.
- **Exact source location:** DOC-001, `jama_andrews_2017_oi_170091.pdf`, PDF p. 7, Figure 3, HIV-negative row.
- **Printed evidence:** Sepsis protocol: 3 deaths/9 (33.3%); usual care: 5 deaths/9 (55.6%); printed relative risk `0.75 (95% CI, 0.23-2.44)`.
- **Rule and observation:** For the displayed subgroup counts and denominators, the unadjusted risk ratio is `(3/9)/(5/9) = 0.60`, not the printed `0.75`. The row point estimate is inside its printed interval and its below-1 direction agrees with the displayed risks; the inconsistency is the numerical point-estimate mismatch.
- **Inference boundary:** The figure labels the quantity `Relative Risk`; DOC-001 methods state that Mantel-Haenszel was used for subgroup *interaction* tests but do not state that these row-specific relative risks used an adjusted, weighted, or otherwise non-crude estimator.
- **Alternative source-grounded interpretations:** An unstated row-specific estimator may have been used; otherwise either the displayed usual-care death count/percentage/denominator or the printed relative-risk point estimate may need confirmation. Finite display rounding cannot change `3/9` or `5/9` into a crude RR of `0.75`.
- **Human question:** Which exact estimator generated the HIV-negative Figure 3 relative risk, and do the displayed counts, denominators, point estimate, and CI all belong to the same subgroup analysis?
- **Status:** Pending Human Adjudication.

### STAT1-002 — Protocol Table 2 arm headers and printed percentages do not reconcile with the printed total

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** DOC-002, `joi170091supp1_prod.pdf`, PDF p. 9, Table 2, “Baseline characteristics in SSSP participants.”
- **Printed evidence:** Table headers are total `n=76`, SSSP `n=36`, and control `n=44`. The header arms sum to `36 + 44 = 80`, not 76. In the control column, examples include HIV positive `31 (78)`, confusion `27 (68)`, respiratory rate >40 `14 (35)`, and acidotic or hypotensive `17 (42)`; these percentages correspond to a denominator of approximately 40 (for example, `31/40 = 77.5%`), not 44. The row counts nevertheless sum to the printed total counts (for example, `26 + 31 = 57`).
- **Rule and observation:** A total-column baseline table with two mutually exclusive arm columns requires its arm denominators to sum to the printed total, and each printed arm percentage should use its stated header denominator absent a stated row-specific exception. Neither condition reconciles as printed.
- **Inference boundary:** The nearby narrative states that 89 participants were enrolled and primary-outcome data were available for 74; those may describe distinct populations and are not required for this header-versus-row candidate.
- **Alternative source-grounded interpretations:** The control header may be a transcription error for `n=40`, which would reconcile `36 + 40 = 76` and the listed control percentages after rounding; alternatively, the total/row labels may represent an unstated subset. No such subset footnote appears in the table.
- **Human question:** What are the intended Table 2 arm denominators, and were the control header, total header, or row percentages transcribed incorrectly?
- **Status:** Pending Human Adjudication.

## Relationship records

### S001 — PASS_1_COMPLETE

Design inputs at DOC-001 p. 3 are internally stated as 65% control mortality, 20-percentage-point absolute reduction, and 30.8% relative reduction; arithmetic check `20/65 = 30.769...%` supports the rounded 30.8%. The 50% interim `P<.001` and final two-sided `.05` are distinct prespecified decision rules, not duplicate results. The exact sample-size calculation, allocation-loss convention, and alpha-spending derivation are not supplied; no reconstruction or candidate.

### S002 — PASS_1_COMPLETE

DOC-001 pp. 1, 5, and 7 repeat the same primary population/contrast and values: 51/106 versus 34/103, RR 1.46 (1.04-2.05), P=.03. Crude arithmetic gives `(51/106)/(34/103) = 1.457`, consistent with 1.46; 1.46 is contained in the increasing CI and direction agrees with higher protocol mortality. The chi-square primary test is named, but CI construction, exact test variant, and confidence/P compatibility rule are not supplied; no inferential reconstruction or candidate.

### S003 — PASS_1_COMPLETE

DOC-001 p. 5 reports matched 28-day mortality with 97 known-status participants per arm, RR 1.48 (1.14-1.91), difference 21.6% (8.0%-35.3%), and P=.002. Point estimates lie within ordered intervals and all direct results indicate higher protocol mortality. The percentages and difference are compatible at displayed precision (67.0%-45.3%=21.7 percentage points before rounding). Counts, CI construction, and test rule are not supplied for an exact P/CI check; no candidate.

### S004 — PASS_1_COMPLETE

DOC-001 p. 5 reports SAPS-3-adjusted in-hospital RR 1.45 (1.04-2.02), P=.03; interval containment/order and harmful-direction wording agree. The main article does not identify the adjusted RR model, coefficient, SE, CI construction, or P-test rule. It is therefore not mechanically comparable to differently adjusted logistic OR analyses in DOC-003; no candidate.

### S005 — PASS_1_COMPLETE

DOC-001 p. 5 reports SAPS-3-adjusted 28-day RR 1.41 (1.08-1.84), P=.01; interval containment/order and direction agree. The adjusted model, 28-day analysis denominator/counts, CI construction, and P-test rule are not supplied at this location; no candidate.

### S006 — PASS_1_COMPLETE

DOC-001 pp. 5-6 consistently labels the time-to-event analysis as survival and reports log-rank P=.02 with lower protocol survival in Figure 2. This P value is not being compared to a CI or coefficient because none is printed. Follow-up/censoring detail sufficient to reproduce the log-rank test is absent; no candidate.

### S007 — PASS_1_COMPLETE

DOC-001 pp. 1, 4, and 6 consistently report greater 6-hour protocol fluid volume (medians 3.5 versus 2.0 L) and a mean difference 1.2 L (1.0-1.5), P<.001. The estimate is contained in ordered endpoints and direction agrees; the differing mean/median summaries are explicitly different scales. Individual values, test selection for the mean difference, and CI construction are absent; no candidate.

### S008 — PASS_1_COMPLETE

DOC-001 p. 6 reports 24-hour fluid medians and P<.001. Direction is 4.0 versus 3.0 L; no effect estimate/CI or named row-specific test is supplied for additional compatibility checking. `P<.001` is not a display zero; no candidate.

### S009 — PASS_1_COMPLETE

DOC-001 p. 6 reports 72-hour fluid medians 5.0 versus 4.0 L and P=.33. No effect estimate/CI or row-specific test rule is supplied; no candidate.

### S010 — PASS_1_COMPLETE

DOC-001 pp. 1, 4, and 6 report the same first-6-hour dopamine counts/percentages, 15/106 (14.2%) versus 2/103 (1.9%), with a prose difference 12.3% (5.1%-19.4%). The displayed difference direction and interval are compatible with the counts at display precision. Table 2 prints P=.001 whereas prose prints P<.001; these are compatible finite-precision displays of a value that rounds to .001 while remaining below .001, and are not an independent contradiction. No display-zero notation occurs; no candidate.

### S011 — PASS_1_COMPLETE

DOC-001 p. 6 reports dopamine during hospitalization, 22/106 (20.8%) versus 7/103 (6.8%), P=.004. Counts, percentages, and direction agree at display precision; exact test rule/CI are absent. No candidate.

### S012 — PASS_1_COMPLETE

DOC-001 p. 6 reports first-6-hour transfusion, 17/106 (16.0%) versus 13/103 (12.6%), P=.48. Counts and percentages agree at display precision; no CI/test rule is supplied. No candidate.

### S013 — PASS_1_COMPLETE

DOC-001 p. 6 reports hospitalization transfusion, 37/106 (34.9%) versus 31/103 (30.1%), P=.46. Counts and percentages agree at display precision; no CI/test rule is supplied. No candidate.

### S014 — PASS_1_COMPLETE

DOC-001 pp. 4 and 6 consistently reports time to antibiotics of 2.0 versus 1.5 h, P=.15, with matching median/IQR display in Table 2. No effect estimate/CI or row-specific test rule is supplied; no candidate.

### S015 — PASS_1_COMPLETE

DOC-001 p. 6 reports 2-hour SBP medians 89 versus 88 mm Hg, P=.09. No interval/effect estimate or row-specific test distribution is supplied; no candidate.

### S016 — PASS_1_COMPLETE

DOC-001 p. 6 reports 2-hour DBP medians 55 versus 54 mm Hg, P=.99. No interval/effect estimate or row-specific test distribution is supplied; no candidate.

### S017 — PASS_1_COMPLETE

DOC-001 p. 6 reports 6-hour SBP medians 95 versus 96 mm Hg, P=.95. No interval/effect estimate or row-specific test distribution is supplied; no candidate.

### S018 — PASS_1_COMPLETE

DOC-001 p. 6 reports 6-hour DBP medians 61 versus 61 mm Hg, P=.82. No interval/effect estimate or row-specific test distribution is supplied; no candidate.

### S019 — PASS_1_COMPLETE

DOC-001 p. 6 reports 6-hour whole-blood lactate medians 3.3 versus 3.9 mmol/L, P=.25. No interval/effect estimate or row-specific test distribution is supplied; no candidate.

### S020 — PASS_1_COMPLETE

DOC-001 pp. 4 and 6 consistently reports median signed lactate changes of -1.2 versus -0.5 mmol/L and a mean difference 1.45 (0.4-2.5), P=.02. The mean-difference estimate is within ordered endpoints. The source does not define the sign/orientation of the separately reported mean-difference/clearance calculation or provide group means, so it cannot be reconciled mechanically to the median signed changes; no candidate.

### S021 — PASS_1_COMPLETE

DOC-001 pp. 4 and 6 consistently reports respiratory compromise 35.8% versus 22.3%, difference 13.5% (1.4%-25.7%), P=.03. Counts in Table 2 (38/106 and 23/103) reproduce the displayed percentages and yield a crude difference about 13.5 points. Estimate containment, endpoint order, and direction agree; CI/test construction absent. No candidate.

### S022 — PASS_1_COMPLETE

DOC-001 p. 6 reports resolved respiratory compromise 20/106 (18.9%) versus 8/103 (7.8%), P=.02. Counts and percentages agree at display precision; post-hoc classification is labelled. No CI/test rule is supplied; no candidate.

### S023 — PASS_1_COMPLETE

DOC-001 p. 6 reports persistent respiratory compromise 18/106 (17.0%) versus 15/103 (14.6%), P=.63. Counts and percentages agree at display precision; post-hoc classification is labelled. No CI/test rule is supplied; no candidate.

### S024 — PASS_1_COMPLETE

DOC-001 p. 5 reports hospital stay medians 5 versus 7 days, P=.01. Direction is clear, but no interval/effect estimate or row-specific test rule is supplied; no candidate.

### S025 — PASS_1_COMPLETE

DOC-001 p. 7 Figure 3 reports HIV interaction P=.09. Positive-stratum counts reproduce RR 1.57 at displayed precision, CI endpoints are ordered and contain it, and direction agrees. The negative-stratum RR/count mismatch is emitted separately as `STAT1-001`; its CI is ordered and contains the printed 0.75. Interaction-test statistic, degrees of freedom, and exact method details are absent, so P=.09 is not independently reconstructed.

### S026 — PASS_1_COMPLETE

DOC-001 p. 7 Figure 3 GCS-stratum displayed count ratios reproduce RRs 1.92, .97, and .91 at displayed precision; every estimate lies within ordered endpoints and directions agree with displayed risks. Interaction P=.01 has no supplied statistic/df/test calculation details; no candidate.

### S027 — PASS_1_COMPLETE

DOC-001 p. 7 Figure 3 hemoglobin-stratum displayed count ratios reproduce RRs 1.37 and 1.36 at displayed precision; endpoints/order and directions agree. Interaction P=.99 lacks supplied statistic/df/test details; no candidate.

### S028 — PASS_1_COMPLETE

DOC-001 p. 7 Figure 3 SAPS-3-stratum displayed count ratios reproduce RRs 1.28 and 1.65 at displayed precision; endpoints/order and directions agree. Interaction P=.47 lacks supplied statistic/df/test details; no candidate.

### S029 — PASS_1_COMPLETE

DOC-001 p. 7 Figure 3 lactate-stratum displayed count ratios reproduce RRs 1.55 and 1.38 at displayed precision; endpoints/order and directions agree. Interaction P=.75 lacks supplied statistic/df/test details; no candidate.

### S030 — PASS_1_COMPLETE

DOC-001 p. 7 Figure 3 JVP-stratum displayed count ratios reproduce RRs 1.75 and 1.22 at displayed precision; endpoints/order and directions agree. Interaction P=.29 lacks supplied statistic/df/test details; no candidate.

### S031 — PASS_1_COMPLETE

DOC-001 p. 3 supplies analysis-family labels: t test, Mann-Whitney, chi-square, log-rank, and Mantel-Haenszel subgroup-interaction testing. These labels are consistent with the applicable relationship descriptions above, but they do not specify row-level test selection, sidedness, CI construction, or variance estimators for every result. No candidate.

### S200 — PASS_1_COMPLETE

DOC-002 p. 4 prespecifies Mantel-Haenszel comparisons and adjusted mortality by multivariable logistic regression. It is a plan, not a matched final estimate; final model/population/adjustment definitions are required before compatibility testing. No candidate.

### S201 — PASS_1_COMPLETE

DOC-002 p. 9 reports preliminary original-SSSP mean 6-hour fluid 2.7 versus 1.8 L, P<.001. It is explicitly a distinct preliminary study; no SD, test statistic, variance, or analysis denominator is supplied. `P<.001` is not a display zero; no candidate.

### S202 — PASS_1_COMPLETE

DOC-002 p. 9 reports preliminary original-SSSP mortality 68.6% versus 64.1%. Component counts, denominators, and model/test rule are not supplied for this result; it must not be matched to SSSP-2 final results. No candidate.

### S203 — PASS_1_COMPLETE

DOC-002 p. 15 specifies planned display/test families (mean [SD] with t test/ANOVA; proportions with chi-square/Fisher exact/Mantel-Haenszel). These are general plan definitions, not row-level executed inferential outputs. No candidate.

### S204 — PASS_1_COMPLETE

DOC-002 p. 15 prespecifies Kaplan-Meier/log-rank/Cox time-to-event analyses and adjusted hazard ratios using SAPS-3 quartiles, with P<.05 threshold. It is a plan; execution population, CI/test construction, and final model specification cannot be inferred from it. No candidate.

### S205 — PASS_1_COMPLETE

DOC-002 p. 15 and DOC-001 p. 3 agree on the planning inputs: 65% control mortality, two-sided alpha .05, 80% power, n=212, 20-point absolute reduction, 1:1 allocation. The 20/65=30.8% relation is compatible. Exact sample-size formula, accrual/loss assumptions, and rounding convention are absent; no candidate.

### S206 — PASS_1_COMPLETE

DOC-002 p. 16 states five planned subgroups and threshold P<.01 as .05/5. Arithmetic reproduces .01; it is a prospective threshold rather than a reported P value. No candidate.

### S207 — PASS_1_COMPLETE

DOC-002 p. 16 prespecifies an as-treated >=3 L versus <3 L six-hour contrast adjusted for SAPS-3 and infection site. The contrast/time anchor/adjustment labels are consistent with DOC-003 eTable 4 as-treated descriptions; no supplied final coefficient or inferential rule permits further compatibility checking. No candidate.

### S208 — PASS_1_COMPLETE

DOC-002 p. 19 is an economic-sensitivity plan specifying directly measured ranges, 95% CIs for all-patient variables, and a Tornado diagram. It reports no result/interval pair; no candidate.

### S209 — PASS_1_COMPLETE

DOC-002 p. 20 reports parent n=342, 68% HIV prevalence, and expected TBASS n=233. Arithmetic `342 x .68 = 232.56` supports rounding to 233. The named precision margins have no supplied confidence-interval method; no candidate.

### S210 — PASS_1_COMPLETE

DOC-002 p. 21 supplies planned diagnostic-score logistic-selection and ROC/AUC rules, not an executed result. No candidate.

### S211 — PASS_1_COMPLETE

DOC-002 p. 21 supplies planned sensitivity/specificity/AUC/kappa definitions and any-site culture truth standard, not an executed estimate. No candidate.

### S212 — PASS_1_COMPLETE

DOC-002 p. 23 prespecifies midpoint stopping if an arm is superior at P<.001; DOC-001 p. 3 has the same threshold. Interim test statistic, sidedness, and alpha-spending details are not supplied. No candidate.

### S213 — PASS_1_COMPLETE

DOC-002 pp. 6-8 gives background/context values, including 46/91 (50.5%) and 36/161 (22.3%). Arithmetic supports rounded percentages; they are not SSSP-2 inferential results. No candidate.

### S214 — PASS_1_COMPLETE

DOC-002 p. 9 Table 2's header/percentage contradiction is emitted as `STAT1-002`. The nearby preliminary fluid P<.001 cannot be reconstructed because its analysis denominator/test/variance are absent. The 89 enrolled and 74 primary-outcome-data statements may identify different populations and are not treated as a direct contradiction with the baseline-table candidate.

### S215 — PASS_1_COMPLETE

DOC-002 p. 24 planned budget component sums reconcile to USD 45,800 and Kwacha 229,000,000. No inferential statistic applies; no candidate.

### S400 — PASS_1_COMPLETE

DOC-003 p. 9 eTable 4 unadjusted logistic primary analysis reports OR 1.88 (1.07-3.30), P=.03, n=209, protocol versus usual care. The OR is inside ordered endpoints and OR>1 direction is explicitly defined as higher protocol death odds. The raw DOC-001 counts reproduce an unadjusted odds ratio about 1.88. CI construction, coefficient/SE, P-test basis, and sidedness are absent; no candidate.

### S401 — PASS_1_COMPLETE

DOC-003 p. 9 eTable 4 worst-case as-randomized logistic analysis reports OR 1.75 (1.00-3.04), P=.047, n=212, with explicit imputation of one protocol survivor and two usual-care deaths. Point estimate is within ordered endpoints; direction/measure/model are labelled. The imputed counts reproduce the reported OR at display precision. CI construction, P-test basis, and sidedness are absent; no candidate.

### S402 — PASS_1_COMPLETE

DOC-003 p. 9 eTable 4 adjusted logistic analysis reports OR 1.93 (1.09-3.43), P=.03, n=209, adjusted for continuous SAPS-3 and lactate. Point estimate is within ordered endpoints and direction/model/adjustments are explicit. It is not the same model as DOC-001's SAPS-3-only adjusted RR, so differing estimates/measures do not establish a contradiction. Coefficient/SE, CI construction, P-test basis, and sidedness are absent; no candidate.

### S403 — PASS_1_COMPLETE

DOC-003 p. 9 eTable 4 unadjusted as-treated logistic analysis reports OR 1.45 (0.83-2.54), P=.20, n=209, for >=3 L versus <3 L in six hours after ED registration. Estimate is within ordered endpoints; measure, contrast, and time anchor are explicit. Counts by as-treated exposure are absent, as are CI/P construction and sidedness; no candidate.

### S404 — PASS_1_COMPLETE

DOC-003 p. 9 eTable 4 adjusted as-treated logistic analysis reports OR 1.41 (0.80-2.49), P=.24, n=209, adjusted for continuous SAPS-3 and suspected infection site. Estimate is within ordered endpoints; measure, contrast/time anchor, and adjustment labels are explicit. Coefficient/SE, CI/P construction, and sidedness are absent; no candidate.

### S405 — PASS_1_COMPLETE

DOC-003 p. 9 eTable 4 unadjusted Cox analysis reports HR 1.65 (1.12-2.44), P=.01, n=209, protocol versus usual care. Estimate is within ordered endpoints and HR>1 is explicitly defined as shorter protocol survival. The P differs from DOC-001 log-rank P=.02, but they are different named analyses and no contradiction follows. Cox coefficient/SE, CI construction, P-test basis, follow-up/censoring detail, and sidedness are absent; no candidate.

### S406 — PASS_1_COMPLETE

DOC-003 p. 9 eTable 4 adjusted Cox analysis reports HR 1.68 (1.14-2.49), P=.009, n=209, with continuous baseline SAPS-3. Estimate is within ordered endpoints and direction/model/adjustment labels are explicit. CI construction, P-test basis, coefficient/SE, follow-up/censoring, and sidedness are absent; no candidate.

### S407 — PASS_1_COMPLETE

DOC-003 p. 9 eTable 4 adjusted Cox analysis reports HR 1.69 (1.14-2.51), P=.001, n=209, with SAPS-3 categorized by quartile. Estimate is within ordered endpoints and direction/model/adjustment labels are explicit. **Diagnostic approximation only:** treating the printed endpoints as a symmetric Wald 95% log-HR interval gives an approximate SE of `(log(2.51)-log(1.14))/(2 x 1.96) ≈ 0.20` and two-sided normal P near .009, not .001. This is not a candidate because the source does not define CI construction, P-test basis (Wald/score/likelihood-ratio), sidedness, coefficient precision, or variance estimator; those assumptions must not be supplied by convention. Human review may compare the original analysis output if needed.

### S408 — PASS_1_COMPLETE

DOC-003 p. 7 eTable 2 footnote reports antimicrobial additions/changes of 46/103 (44.7%) versus 46/106 (43.4%), P>.85. Counts reproduce percentages at display precision and direction is clear. Named test, exact P, sidedness, and variance/test rule are absent; threshold P cannot be reconstructed. No candidate.

### S409 — PASS_1_COMPLETE

DOC-003 p. 7 eTable 2 footnote reports post-culture antimicrobial changes of 0/103 (0.0%) versus 1/106 (0.9%), P>.99. Counts reproduce percentages at display precision; there is no `P=0` display. Named test, exact P, sidedness, and test rule are absent; no candidate.

### S410 — PASS_1_COMPLETE

DOC-003 p. 5 eMethods D defines 85/209 in-hospital deaths and 109/194 28-day deaths, group assignment/SAPS-3 covariates, no interaction or data reduction, and continuous/quartile SAPS-3 sensitivity analyses. These labels support population/model matching but report no coefficient, CI, SE, statistic, or independent-validation result. No candidate.

## Pass-1 totals and limitations

- **Relationships assigned:** 58.
- **Relationships with explicit PASS_1_COMPLETE records:** 58.
- **Provisional candidates emitted:** 2 (`STAT1-001`, `STAT1-002`).
- **DISPLAY_ZERO_NOT_CANDIDATE records:** 0; no display-zero P value occurred in scope.
- **Main limitations:** Several table rows provide P values without row-specific test/CI definitions; adjusted main-text RR model details are incomplete; Cox P/CI compatibility is definition-limited by unreported CI and P-test construction, sidedness, SEs, and variance estimators. Planning/preliminary protocol values were kept distinct from final SSSP-2 results.
