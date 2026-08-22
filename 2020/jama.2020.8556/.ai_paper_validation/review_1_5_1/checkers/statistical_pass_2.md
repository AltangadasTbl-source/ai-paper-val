# Statistical Consistency Review — Pass 2

## Scope, independence, and method

- **Reviewer runtime:** `root/statistical_pass_2` (fresh, distinct from pass 1; `gpt-5.6-terra`, high effort; `FRESH_SPAWN`).
- **Assigned relationship scope:** `S001` through `S093` (93/93), revisited after the complete stable candidate ledger (`C001`–`C008`), numeric and cross-source checker artifacts, pass-1 artifact, and mechanical evidence recheck.
- **Checks revisited:** denominator and arithmetic implications; estimate containment; endpoint order; named contrast/direction; measure, scale, rate/count, population, and duplicate-value labels; matched-source repetitions; and inference compatibility only when the supplied model and inferential definitions support it. I did not infer sidedness, degrees of freedom, covariance, variance estimator, multiplicity method, denominator, model selection, or estimand mapping from convention.
- **Display-zero rule:** no `P = 0`, `p = 0.000`, or equivalent display-zero result occurs in this scope. `P < .001` is an inequality display, not a display zero, and did not generate a proposal.
- **Outcome:** no genuinely new provisional candidate is proposed. Existing stable candidates are neither adjudicated nor changed here; they remain `Pending Human Adjudication` in the ledger.

## Stable-candidate implication check

| Stable ID | Pass-2 relationship implication | PASS 2 result |
|---|---|---|
| C001 | The person-day/mean issue is numeric (`N010`). `S001` uses the stated primary-analysis population and rate-model result but supplies no day-definition or participant-set link that reconciles the two displayed arm means with person-days. | Retained implication; no separate inferential contradiction. |
| C002 | The administration-route percentage issue is numeric (`N011`). `S069`, `S070`, `S074`, and `S080` define adherence/CACE but do not equate route-of-administration counts with the CACE exposure or provide a route-specific denominator. | Retained implication; no new relationship-level proposal. |
| C003 | `S080` repeats the 97.8% adherence median/IQR and CACE N=305, whereas the main summary names 302 initiators. The sources do not state that the CACE analysis N is the median's denominator; the identical IQR and differing median remain the ledger's cross-source issue. | Retained implication; denominator mapping remains explicitly missing. |
| C004 | The nonprophylactic-antibiotic percentage issue is numeric (`N014`). No `S` relationship provides an outcome-specific arm denominator that resolves the displayed fractions/percentages. | Retained implication; no new statistical proposal. |
| C005 | `S042` and `S088` cover the three-month oral-candidiasis odds ratio/P value and the matched supplement result. They do not label the main ARD estimator or direction; raw fractions and supplement difference retain the recorded reconciliation question. | Retained implication; no new proposal beyond C005. |
| C006 | `S004` and `S085` are the matched B. animalis result. Their lower 95% CI endpoints remain printed as 5.94 and 5.95 respectively, with matched counts, odds ratio, upper endpoint, and P display. | Retained implication; no additional discrepancy. |
| C007 | `S082` contains the eTable 4 `20/119 (16.0)` cell. The semi-quantitative categories make the printed percentage/fraction mismatch a ledger issue; the same cell also accounts for the apparent category-total tension, so it is not a distinct new candidate. | Retained implication; no separate proposal. |
| C008 | `S069`, `S074`, and `S080` establish 2SLS, cluster-robust SE, ×100 presentation, two-sided 95% convention, and the printed coefficient/CI/P. The CI construction, test distribution, degrees of freedom, unrounded outputs, and common-output status remain absent. | Retained conditional diagnostic; no new proposal. |

## Relationship-by-relationship pass-2 records

| Relationship ID | PASS 2 record |
|---|---|
| S001 | **PASS_2_COMPLETE — no new proposal.** Primary CAAD repetition, adjusted IRR 1.13 (0.79–1.63), P=.50, rate label, and ordered/containing interval agree. C001 does not supply the missing person-day mean population. |
| S002 | **PASS_2_COMPLETE — definition-limited, no new proposal.** Counts, AOR 9.19 (3.51–24.07), and P<.001 match eTable 5. The ARD subtraction reference is not stated; no sign is inferred. |
| S003 | **PASS_2_COMPLETE — definition-limited, no new proposal.** Matched counts, AOR 6.41/6.4 (2.14–19.20), and P=.001 agree to precision; ARD reference remains unstated. |
| S004 | **PASS_2_COMPLETE — C006 implication retained; no new proposal.** Ordered and containing OR interval, counts, and P match S085 except lower endpoint 5.94 versus 5.95. |
| S005 | **PASS_2_COMPLETE — definition-limited, no new proposal.** Counts, AOR 21.96/22.0 (2.97–162.43), and P=.002 agree after precision; difference reference is absent. |
| S006 | **PASS_2_COMPLETE — no new proposal.** UTI rate-labelled IRR 1.17 (0.75–1.84), P=.48 is ordered and contains estimate. |
| S007 | **PASS_2_COMPLETE — no new proposal.** Upper-RTI rate IRR 1.13 (0.71–1.78), P=.61 is coherent. |
| S008 | **PASS_2_COMPLETE — no new proposal.** Narrative 1.42 (1.05–1.93) and table 1.4 (1.1–1.9), P=.02 are precision-compatible rate results. |
| S009 | **PASS_2_COMPLETE — no new proposal.** Skin-infection IRR 0.92 (0.54–1.57), P=.76 has coherent label, order, and containment. |
| S010 | **PASS_2_COMPLETE — no new proposal.** Any-infection IRR 1.0 (0.8–1.2), P=.92 is coherent at displayed precision. |
| S011 | **PASS_2_COMPLETE — no new proposal.** UTI incidence IRR 1.1 (0.6–2.1), P=.68 is coherent. |
| S012 | **PASS_2_COMPLETE — no new proposal.** GI-incidence IRR 0.8 (0.2–2.6), P=.68 is coherent. |
| S013 | **PASS_2_COMPLETE — no new proposal.** Upper-RTI-incidence IRR 0.8 (0.5–1.2), P=.31 is coherent. |
| S014 | **PASS_2_COMPLETE — no new proposal.** Lower-RTI-incidence IRR 1.2 (0.8–1.7), P=.41 is coherent. |
| S015 | **PASS_2_COMPLETE — no new proposal.** Skin-incidence IRR 1.2 (0.7–2.0), P=.49 is coherent. |
| S016 | **PASS_2_COMPLETE — no new proposal.** The ≥1-infection comparison is labelled OR 1.4 (0.8–2.4), P=.20, not a rate; interval is ordered and containing. |
| S017 | **PASS_2_COMPLETE — no new proposal.** Table 0.1 (0–0.2) and narrative 0.08 (−0.001–0.16), P=.05 are precision-compatible adjusted mean differences. |
| S018 | **PASS_2_COMPLETE — no new proposal.** Cumulative infection-day rate IRR 1.1 (0.8–1.5), P=.67 retains its rate definition. |
| S019 | **PASS_2_COMPLETE — definition-limited, no new proposal.** EQ-5D adjusted mean −0.1 (−0.1–0), P=.13 is contained and scale-labelled; coarse display prevents CI/P reconstruction. |
| S020 | **PASS_2_COMPLETE — definition-limited, no new proposal.** EQ-5D adjusted mean 0 (−0.1–0), P=.66 is coherent; coarse precision prevents a diagnostic reconstruction. |
| S021 | **PASS_2_COMPLETE — no new proposal.** EQ-5D health adjusted mean −0.3 (−8.0–7.5), P=.95 is contained, ordered, and on the stated 0–100 scale. |
| S022 | **PASS_2_COMPLETE — no new proposal.** EQ-5D health adjusted mean 0.4 (−4.1–4.8), P=.87 is coherent. |
| S023 | **PASS_2_COMPLETE — no new proposal.** Second-follow-up EQ-5D adjusted mean 0 (−0.1–0.1), P=.92 is coherent. |
| S024 | **PASS_2_COMPLETE — no new proposal.** Second-follow-up proxy EQ-5D adjusted mean 0 (−0.1–0.1), P=.79 is coherent. |
| S025 | **PASS_2_COMPLETE — no new proposal.** Power-squared transformed health outcome 24.4 (−1267.9–1316.6), P=.97 is ordered/containing; no back-transformation is inferred. |
| S026 | **PASS_2_COMPLETE — no new proposal.** Second-follow-up health proxy adjusted mean 0.6 (−4.9–6.2), P=.82 is coherent. |
| S027 | **PASS_2_COMPLETE — no new proposal.** Table and narrative ICECAP-O effects agree after rounding; direction and 0–1 scale are named. |
| S028 | **PASS_2_COMPLETE — definition-limited, no new proposal.** Displayed 0 (0–0), P=.85 is a finite-precision near-zero interval, not an endpoint-order defect. |
| S029 | **PASS_2_COMPLETE — no new proposal.** Second-follow-up ICECAP-O adjusted mean −0.1 (−0.2–0), P=.15 is coherent. |
| S030 | **PASS_2_COMPLETE — no new proposal.** Second-follow-up proxy ICECAP-O adjusted mean 0 (−0.1–0), P=.69 is coherent. |
| S031 | **PASS_2_COMPLETE — no new proposal.** Hospitalization OR 1.25 (0.74–2.11), P=.41 matches its binary outcome and 42/152 versus 36/153 counts. |
| S032 | **PASS_2_COMPLETE — no new proposal.** Death OR 1.03 (0.59–1.80), P=.90 is coherent with 33/155 versus 32/155. |
| S033 | **PASS_2_COMPLETE — no new proposal.** Hospital-stay IRR 1.17 (0.72–1.90), P=.53 retains the 152/153 rate population label. |
| S034 | **PASS_2_COMPLETE — no new proposal.** Hospital-days IRR 1.00 (0.43–2.29), P>.99 is coherent; inequality P display is not a display zero. |
| S035 | **PASS_2_COMPLETE — no new proposal.** AAD-incidence IRR 1.39 (0.79–2.46), P=.25 is rate-labelled and coherent. |
| S036 | **PASS_2_COMPLETE — no new proposal.** AAD-days IRR 1.83 (0.95–3.54), P=.07 is rate-labelled and coherent. |
| S037 | **PASS_2_COMPLETE — no new proposal.** All-cause-diarrhea incidence IRR 1.1 (0.7–1.6), P=.80 is coherent. |
| S038 | **PASS_2_COMPLETE — no new proposal.** All-cause-diarrhea days IRR 1.2 (0.78–2.0), P=.39 is coherent. |
| S039 | **PASS_2_COMPLETE — no new proposal.** ≥1 all-cause-diarrhea OR 1.0 (0.6–1.8), P=.89 is distinct from rate outcomes and coherent. |
| S040 | **PASS_2_COMPLETE — no new proposal.** Diarrhea-duration adjusted mean 0.1 (−0.1–0.2), P=.27 is coherent. |
| S041 | **PASS_2_COMPLETE — definition-limited, no new proposal.** Resistant-Enterobacterales main/eTable ORs, CIs, and Ps agree after precision; ARD reference direction remains unnamed. |
| S042 | **PASS_2_COMPLETE — C005 implication retained; no new proposal.** Oral-candidiasis AORs/CIs/Ps match S088. Neither result location defines the main ARD estimator/direction. |
| S043 | **PASS_2_COMPLETE — no new proposal.** C. difficile OR 6.51/6.5 (0.75–56.57), P=.09 matches eTable precision; second follow-up is explicitly not analyzable. |
| S044 | **PASS_2_COMPLETE — no new proposal.** Protocol Poisson plan permits negative-binomial analysis under overdispersion; no result contradiction. |
| S045 | **PASS_2_COMPLETE — no new proposal.** Sample-size/power statement is planning-only; no source-matched observed calculation is supplied. |
| S046 | **PASS_2_COMPLETE — no new proposal.** Mechanistic power statement is planning-only without matched reported inference. |
| S047 | **PASS_2_COMPLETE — no new proposal.** Structural-mean adherence plan is compatible with later CACE model family; no numeric repeated estimate here. |
| S048 | **PASS_2_COMPLETE — no new proposal.** Missing-data/SACE plans do not concretely conflict with reported sensitivity descriptions. |
| S049 | **PASS_2_COMPLETE — no new proposal.** Planned mediation has no matched result estimate. |
| S050 | **PASS_2_COMPLETE — no new proposal.** Protocol count-model contingency and interaction plan are compatible with reported rate outcome families. |
| S051 | **PASS_2_COMPLETE — no new proposal.** Early protocol Cox-frailty duration plan is not asserted to be final; later hurdle/linear analysis cannot be called contradictory on supplied evidence. |
| S052 | **PASS_2_COMPLETE — no new proposal.** Planned and implemented EQ-5D/ICECAP adjusted-mean frameworks are context-compatible. |
| S053 | **PASS_2_COMPLETE — no new proposal.** Planned hospital/death outcome families lack an incompatible matched printed estimate. |
| S054 | **PASS_2_COMPLETE — no new proposal.** Planned mixed-logistic microbiology/candidiasis model aligns with later adjusted OR reporting. |
| S055 | **PASS_2_COMPLETE — no new proposal.** Later ordinal documentation does not establish an error in an early planned mixed-linear model. |
| S056 | **PASS_2_COMPLETE — no new proposal.** Mechanistic logistic plan has no matched reported estimate. |
| S057 | **PASS_2_COMPLETE — no new proposal.** Revised SAP power/target is explicitly planning context, not an observed effect. |
| S058 | **PASS_2_COMPLETE — no new proposal.** ITT/complete-case/imputation definitions are compatible with the reported outcome-data population; no all-randomized-outcome claim is inferred. |
| S059 | **PASS_2_COMPLETE — no new proposal.** Two-sided 95% and no-multiplicity conventions provide context but no conflicting convention. |
| S060 | **PASS_2_COMPLETE — no new proposal.** SAP permits actual negative-binomial primary model; IRR/CI/P labels match. |
| S061 | **PASS_2_COMPLETE — no new proposal.** SAP rate/duration definitions agree with Table 2 labels. |
| S062 | **PASS_2_COMPLETE — no new proposal.** SAP diarrhea rate/IRR definitions agree with Table 3 labels. |
| S063 | **PASS_2_COMPLETE — no new proposal.** SAP's separate self/proxy adjusted mean-difference framework and scales agree with Table 3. |
| S064 | **PASS_2_COMPLETE — no new proposal.** SAP OR for hospital/death and IRR for hospital days agree with reported measure labels. |
| S065 | **PASS_2_COMPLETE — no new proposal.** Gender, overdispersion, transformation, and hurdle contingencies are compatible with implementation notes. |
| S066 | **PASS_2_COMPLETE — no new proposal.** Prespecified sensitivity types match eTable 1 without numeric conflict. |
| S067 | **PASS_2_COMPLETE — no new proposal.** SAP interaction families match eTable 6 subgroups. |
| S068 | **PASS_2_COMPLETE — no new proposal.** SAP missingness/offset conventions and eTable 3 scenario are compatible. |
| S069 | **PASS_2_COMPLETE — C008 implication retained; no new proposal.** CACE plan supplies 2SLS/GMM alternatives and cluster-robust SE, but not CI construction, test distribution, or degrees of freedom. |
| S070 | **PASS_2_COMPLETE — no new proposal.** Daily-adherence/blinding definitions have no matched inferential result. |
| S071 | **PASS_2_COMPLETE — no new proposal.** ICC/Bland-Altman/kappa plan has no matched reported inferential statistic. |
| S072 | **PASS_2_COMPLETE — no new proposal.** Results-supplement reporting convention agrees with main IRR/mean-difference/OR labels. |
| S073 | **PASS_2_COMPLETE — no new proposal.** Online-supplement ITT wording is compatible with outcome-data analysis population. |
| S074 | **PASS_2_COMPLETE — C008 implication retained; no new proposal.** CACE 2SLS, instrument, exposure, sex adjustment, robust SE, and ×100 scale are stated; no contradiction in the definition itself. |
| S075 | **PASS_2_COMPLETE — no new proposal.** Actual primary negative-binomial model, nesting, exposure time, and sex adjustment match results. |
| S076 | **PASS_2_COMPLETE — no new proposal.** Secondary rate model families and robust SE are compatible; result-specific model selection is not supplied and is not inferred. |
| S077 | **PASS_2_COMPLETE — no new proposal.** Hurdle/linear duration and logistic/ordinal microbiology labels agree with results. |
| S078 | **PASS_2_COMPLETE — no new proposal.** Subgroup-by-arm method agrees with eTable 6. |
| S079 | **PASS_2_COMPLETE — no new proposal.** Sensitivity IRRs 1.2 (0.83–1.67), P=.36 and 1.1 (0.74–1.54), P=.73 are ordered/containing and definition-matched. |
| S080 | **PASS_2_COMPLETE — C003 and C008 implications retained; no new proposal.** CACE .01 (−.20–.41), P=.52 has ordered/containing endpoints but an off-centre midpoint. Symmetric-Wald compatibility is only a labelled diagnostic; CI/test construction and df are absent. |
| S081 | **PASS_2_COMPLETE — no new proposal.** Extreme missing-data scenario IRR 1.62 (1.03–2.57), P=.04 has named assumption and coherent interval/direction; descriptive difference need not equal the model result. |
| S082 | **PASS_2_COMPLETE — C007 implication retained; no new proposal.** Ordinal-model/reference labels and OR intervals are coherent; `20/119 (16.0)` remains the already registered printed cell mismatch. |
| S083 | **PASS_2_COMPLETE — no new proposal.** C. difficile eTable result is precision-compatible with main result and second result is not analyzable. |
| S084 | **PASS_2_COMPLETE — definition-limited, no new proposal.** L. rhamnosus OR/CIs/Ps match S002–S003 after precision; ARD subtraction reference absent. |
| S085 | **PASS_2_COMPLETE — C006 implication retained; no new proposal.** B. animalis 3-month lower endpoint 5.95 remains distinct from S004's 5.94; second-follow-up values agree. |
| S086 | **PASS_2_COMPLETE — no new proposal.** Near-complete Enterobacterales/VRE cells are explicitly not analyzable; no estimate is inferred. |
| S087 | **PASS_2_COMPLETE — definition-limited, no new proposal.** Resistant-Enterobacterales OR/CIs/Ps match S041 after precision; no shared ARD reference is supplied. |
| S088 | **PASS_2_COMPLETE — C005 implication retained; no new proposal.** Oral-candidiasis OR/CIs/Ps match S042; source does not define main ARD estimator/direction. |
| S089 | **PASS_2_COMPLETE — no new proposal.** Ordinal-candida ORs, intervals, Ps, probiotic/placebo reference, and gender adjustment are duplicated consistently. |
| S090 | **PASS_2_COMPLETE — no new proposal.** Sex-subgroup main and interaction P values have named model terms; no unreported df are inferred. |
| S091 | **PASS_2_COMPLETE — no new proposal.** Capacity-subgroup labels, references, and P values are coherent. |
| S092 | **PASS_2_COMPLETE — definition-limited, no new proposal.** Frailty-subgroup labels and P values are coherent; multi-level interaction df/distribution is not supplied. |
| S093 | **PASS_2_COMPLETE — no new proposal.** Gender-adjustment exception and no-formal-multiplicity statement agree with SAP convention. |

## Counts and limitations

- **Relationships completed:** 93/93 (`S001`–`S093`), each with an explicit `PASS_2_COMPLETE` record.
- **Stable candidates reviewed for implications:** 8/8 (`C001`, `C002`, `C003`, `C004`, `C005`, `C006`, `C007`, `C008`).
- **New provisional candidate proposals:** 0.
- **Definition-limited records:** S002–S005, S019–S020, S028, S041–S042, S069, S080, S084, S087–S088, and S092. The precise missing inputs are result-specific subtraction/referent definitions, CACE CI construction/test distribution/degrees of freedom/unrounded output linkage, and subgroup test distribution/degrees of freedom.
- **Diagnostic approximation:** C008/S080 retains only the conditional symmetric-Wald midpoint/compatibility diagnostic. It does not reconstruct an unreported P value or substitute for the reported analysis.
- **Display-zero exclusions:** none applicable; no display-zero notation was observed.
