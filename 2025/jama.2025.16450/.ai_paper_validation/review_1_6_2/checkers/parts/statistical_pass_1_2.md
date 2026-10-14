# Statistical pass 1 — disjoint shard 2

Runtime agent ID: `/root/statistics_pass_1_2`. Fresh spawn; run model `gpt-6.1-sol`; reasoning effort `high`. Scope: 89 assigned relationships in `statistics/parts/assigned_s_2.md`. The explicit S-ID completion records are in `statistics/parts/pass_1_status_2.md`. Source content controls; extraction and OCR are locators. No legacy findings, screening records, dispositions, or reports were read; no external material was used. Four findings and eleven excluded observations follow. These are observations for independent screening, without candidate IDs or adjudications.

Every applicable relationship was checked for count/denominator arithmetic, effect-measure identity, estimate containment and endpoint order, inferential direction, method logic, and plan/report implications. Prospective operational definitions have no observed estimate, CI, P value, standard error or test statistic to pair. No noninferiority or equivalence margin is specified in this assigned trial scope. For the historical tables, P-value checks used only supplied test labels; unavailable contributor sizes, degrees of freedom and variance choices were not inferred. Normal approximations below are explicitly diagnostic.

## Findings

### F-ST1-1001

**Title:** Historical Grade 3 BPD count, percentage and test do not reconcile within one display.

**Relationships:** S276; P_P. **Focus area:** A, B. **Proposed review domain:** `plan_material`.

**Exact locations and document roles:** PLAN [protocol PDF p12, Table 2, NICHD BPD Workshop Grading 2018, Grade 3, Surfactant column and P-value column](../../../../joi250072supp1_prod_1761000786.68881.pdf#page=12). On that same page the Death and Grade 3 or Death rows corroborate the relevant components; they do not change the relationship type.

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

**Exact locations and document roles:** PLAN [SAP PDF p29 §7.7](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=29) and [p38 §§9.4–9.4.2](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=38); REPORT [main article PDF p7, Table 2 and Sensitivity and Subgroup Analyses](../../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7), [p9 Figure 2](../../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=9), and REPORT [results supplement PDF pp1–16, eight eTables](../../../../joi250072supp4_prod_1761000786.6988.pdf#page=1). The complete current results map was searched for each named analysis; no matching primary-outcome result is present.

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

**Exact locations and document roles:** PLAN [SAP PDF p39 §9.5](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=39); REPORT [main article PDF p8, Table 3, BPD severity rows and footnote a](../../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=8).

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

**Exact locations and document roles:** PLAN [SAP PDF p29 §7.7](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=29) and [p36 §9.3, binary response coding](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=36); REPORT [main article PDF p9 Figure 2, title, caption and footnote a](../../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=9), with [p7 subgroup narrative](../../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7).

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

