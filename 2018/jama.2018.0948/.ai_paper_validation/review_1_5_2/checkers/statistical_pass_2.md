# Statistical Consistency Review — Pass 2

## Independent scope and method

- **Reviewer runtime agent ID:** `root/statistics_pass_2`.
- **Configuration:** newly spawned `gpt-5.6-terra`, high reasoning effort; distinct from the recorded pass-1 reviewer.
- **Complete assigned scope:** all 45 registered statistical relationships (`S001`–`S045`), stable candidate ledger `C001`–`C005`, and every fact in `verification/evidence_recheck.md`.
- **Evidence boundary:** supplied PDFs, fresh native/layout extracts, fresh page renders, fresh mapping artifacts, the current candidate ledger, and the mechanical recheck only. No legacy audit derivative, external source, or web material was used.
- **Check rule:** point estimate containment and endpoint ordering; denominator/arithmetic/population identity; direction; effect measure/scale/reference label; cross-location repetition; duplicate-value implications; and interval/P/test/SE compatibility only where the supplied source defines compatible inference. Crude arithmetic was not substituted for adjusted GEE, clustered, or weighted estimates.

Every record below is **PASS_2_COMPLETE**. This is coverage status, not a validity, severity, correction, acceptance, or disposition.

## Relationship-level pass-2 records

| S ID | Pass-2 reconciliation record | Status |
|---|---|---|
| S001 | DOC-001 p. 4: rate denominators, GEE clustering, model families, and links remain explicitly separated; no unlabelled exchange of discharge, patient-day, or ICU-discharge scales. | PASS_2_COMPLETE — no new candidate. |
| S002 | DOC-001 pp. 4-5: hospital- versus individual-level analyses, two-sided testing, and Holm adjustment are stated; no result was compared across unmatched analysis units. | PASS_2_COMPLETE — no new candidate. |
| S003 | DOC-001 p. 4 planning mortality inputs were matched to DOC-002 pp. 1, 14, 29 and DOC-004 p. 14. The unit conflict is already C002; clustered power inputs do not permit a separate mechanical power check. | PASS_2_COMPLETE — C002 implication reviewed; no new candidate. |
| S004 | DOC-001 p. 6 Table 2 heart-rate and respiratory-rate adjusted differences have ordered CIs containing their estimates; signs and printed P values agree diagnostically with the stated linear GEE contrasts. | PASS_2_COMPLETE — no new candidate. |
| S005 | DOC-001 p. 6 systolic-BP and saturation adjusted differences have ordered, containing CIs and compatible directions/P values; their measure-frequency labels remain distinct. | PASS_2_COMPLETE — no new candidate. |
| S006 | DOC-001 p. 6 respiratory-effort and capillary-refill differences have ordered, containing CIs and compatible positive directions. | PASS_2_COMPLETE — no new candidate. |
| S007 | DOC-001 p. 6 oxygen-therapy and complete-observation-set results reconcile with the four displayed numerators/assessment denominators after rounding; the identity-binomial GEE label is supplied. | PASS_2_COMPLETE — no new candidate. |
| S008 | DOC-001 pp. 1, 7: mortality counts/rates reproduce from discharge denominators; adjusted difference and OR labels, CIs, directions, and abstract/Table repetition agree. | PASS_2_COMPLETE — no new candidate. |
| S009 | DOC-001 p. 7: mortality-without-DNR difference and OR have ordered, containing CIs; no-DNR counts do not exceed all deaths and use the defined subset. | PASS_2_COMPLETE — no new candidate. |
| S010 | DOC-001 pp. 1, 7: SCDE counts and patient-day rates reproduce; rate difference and RR are consistently labelled and repeated. C001's fluid-threshold boundary is a definition conflict, not a separate inferential discrepancy. | PASS_2_COMPLETE — C001 implication reviewed; no new candidate. |
| S011 | DOC-001 p. 7: the two ICU-mortality ORs use explicitly different ICU-discharge and hospital-discharge rate scales. Neither CI/P bundle conflicts; ICU-discharge denominators are not printed. | PASS_2_COMPLETE — no new candidate. |
| S012 | DOC-001 p. 7: cardiac-arrest and potentially-preventable-arrest RR bundles have ordered, containing CIs and compatible directions. The preventability-definition conflict is C004, not a new effect-estimate contradiction. | PASS_2_COMPLETE — C004 implication reviewed; no new candidate. |
| S013 | DOC-001 p. 7: immediate-team and immediate-physician-call RRs have ordered, containing CIs and compatible P/direction; patient-day scale is consistent. | PASS_2_COMPLETE — no new candidate. |
| S014 | DOC-001 pp. 7-8: urgent-consultation and urgent-admission RRs are on the stated patient-day scale. The 828/1,178 SCD narrative denominators are admission counts and were not conflated with patient-days. | PASS_2_COMPLETE — no new candidate. |
| S015 | DOC-001 p. 7: ICU and hospital readmission ORs retain their separately footnoted ICU- and hospital-discharge scales; CIs/P values are compatible. | PASS_2_COMPLETE — no new candidate. |
| S016 | DOC-001 p. 7: exploratory Holm notation and weighted-kappa CI are internally labelled; no compatible kappa test/variance inputs are supplied for recalculation. | PASS_2_COMPLETE — no new candidate. |
| S017 | DOC-001 p. 8 and DOC-004 pp. 12-13: urgent-ICU patient analysis is distinguished from admissions; 42+67=109, displayed percentages match 686/967 denominators, and adjusted CIs/P values are compatible. | PASS_2_COMPLETE — no new candidate. |
| S018 | DOC-001 p. 8 Figure 2: slopes .57 and .53 with P=.94 have coherent stated direction. No CI, SE, df, or slope-test rule is supplied, so no numerical P reconstruction is supportable. | PASS_2_COMPLETE — no new candidate. |
| S019 | DOC-002 pp. 1, 16: descriptive hospital-period summaries are a plan, not a fitted inferential bundle; no result/variance is printed. | PASS_2_COMPLETE — no new candidate. |
| S020 | DOC-002 pp. 1, 16: planned weighted hospital-level logit mortality model identifies contrast, baseline logit, size stratum, and standard-care reference, but no fitted coefficient/CI/P. | PASS_2_COMPLETE — no new candidate. |
| S021 | DOC-002 p. 16: the same planned model is separately named for ICU, DNR, and readmission outcomes; no numerical equality is asserted. | PASS_2_COMPLETE — no new candidate. |
| S022 | DOC-002 pp. 1, 16: planned hospital Poisson rate models identify patient-day denominators; no fitted effect, dispersion, or test is supplied. | PASS_2_COMPLETE — no new candidate. |
| S023 | DOC-002 p. 16: planned weighted within-hospital mean analyses keep their distinct outcome units; no coefficient/SE is printed. | PASS_2_COMPLETE — no new candidate. |
| S024 | DOC-002 p. 16: unweighted documentation regressions are explicitly justified by equal records per hospital; no achieved effect is presented. | PASS_2_COMPLETE — no new candidate. |
| S025 | DOC-002 pp. 16-17: survey/subgroup plan identifies weighting and one-outcome/no-interim constraints, without a numeric interaction to reconcile. | PASS_2_COMPLETE — no new candidate. |
| S026 | DOC-002 pp. 7-9: concealed hospital randomisation and the <200/at-least-200-bed strata are clear; no randomized-result statistic conflicts. | PASS_2_COMPLETE — no new candidate. |
| S027 | DOC-002 pp. 7-8: competence threshold and historical ICC values are performance descriptions. ICC convention and CI are absent, precluding an unsupported test check. | PASS_2_COMPLETE — no new candidate. |
| S028 | DOC-002 p. 8: three run-in targets are distinct targets, not achieved inferential estimates. | PASS_2_COMPLETE — no new candidate. |
| S029 | DOC-002 pp. 11-12: two-reviewer/pre-discussion kappa plan lacks weighting/calculation specification. The scale/category and preventability-threshold conflicts remain C003 and C004; no separate statistical candidate arises. | PASS_2_COMPLETE — C003/C004 implications reviewed; no new candidate. |
| S030 | DOC-002 p. 20: all listed AUC CIs are ordered and contain the AUC; all-control counts 772+616=1,388 and all-case counts 381+305=686. `<.0001` is a threshold display, not a finite-precision zero and not a candidate. | PASS_2_COMPLETE — no new candidate. |
| S031 | DOC-002 pp. 1, 14, 29: 18% mortality RRR is expressed as .9/1,000 or .09% at two locations but .9% at p. 29. This is the already registered C002; no duplicate candidate. | PASS_2_COMPLETE — C002 implication reviewed; no new candidate. |
| S032 | DOC-002 p. 29: .178×5.1=.9078/1,000 and .199×3.2=.6368/1,000 preserve their stated per-1,000 scale. The .9% printed statement is C002, not a second distinct comparison. | PASS_2_COMPLETE — C002 implication reviewed; no new candidate. |
| S033 | DOC-002 pp. 14-15, 30: .31×2=.62 per 1,000 is arithmetically compatible. The unchanged 1,052 count with annual versus two-year labels remains C005; no distinct statistical inference conflict. | PASS_2_COMPLETE — C005 implication reviewed; no new statistical candidate. |
| S034 | DOC-002 p. 30: .41×.75=.3075 per 1,000 is compatible with the printed .3 per 1,000 after rounding. | PASS_2_COMPLETE — no new candidate. |
| S035 | DOC-002 p. 30: 8.13×.181=1.47153 per 1,000, conventionally 1.47 rather than printed 1.45. The displayed-input rounding bounds (approximately 1.4666 to 1.4765) do not include 1.45. This is C006; no compatible variance/test is supplied. | PASS_2_COMPLETE — C006 implication reviewed; no duplicate candidate. |
| S036 | DOC-003 p. 1: binary x/n and count x/patient-day outcome definitions remain separated under exchangeable GEE; plan only. | PASS_2_COMPLETE — no new candidate. |
| S037 | DOC-003 pp. 1-2: logit and identity-binomial GEE models separately define odds and probability/risk contrasts and baseline transforms; no fitted result. | PASS_2_COMPLETE — no new candidate. |
| S038 | DOC-003 pp. 2-3: log-Poisson rate-ratio and identity-Poisson rate-difference models define time at risk and scale; no coefficient/CI/test is printed. | PASS_2_COMPLETE — no new candidate. |
| S039 | DOC-003 p. 3: prose identifies patient-days as the log-link offset while displayed code appears to place intervention/baseline terms within `offset(...)` and has unmatched punctuation. Without executable source, output, or version provenance, this is not a reproducible reporting contradiction. | PASS_2_COMPLETE — diagnostic notation issue only; no new candidate. |
| S040 | DOC-003 p. 4: Gaussian GEE continuous-outcome model, clustering, and baseline mean are stated; no observed estimate. | PASS_2_COMPLETE — no new candidate. |
| S041 | DOC-003 pp. 4-5: sensitivity methods name distinct GEE/GLMER, interaction, weighting, and quasi-family analyses; the source does not claim numerical equality between methods. | PASS_2_COMPLETE — no new candidate. |
| S042 | DOC-003 p. 5: probability/rate sensitivity methods have distinct identity-link weighting and variance structures; no fitted values permit comparison. | PASS_2_COMPLETE — no new candidate. |
| S043 | DOC-003 p. 6: service-presence subgroups and treatment-by-subgroup interaction are specified, without an interaction result. | PASS_2_COMPLETE — no new candidate. |
| S044 | DOC-003 p. 7: ICU selection and first/sum/mean/any-day aggregation rules distinguish per-patient quantities; no numerical effect is stated. | PASS_2_COMPLETE — no new candidate. |
| S045 | DOC-004 pp. 12-13 eTable 4: denominators 393/686/531/967 give displayed binary percentages after rounding; each adjusted-difference CI is ordered and contains its estimate. GEE/identity-binomial and Gaussian labels support the stated sign/CI/P interpretation, but not replacement with crude differences. | PASS_2_COMPLETE — no new candidate. |

## Ledger and mechanical-recheck reconciliation

All seven stable IDs were reconsidered against their mechanical recheck facts. No existing ID was deleted, merged, renumbered, ranked, adjudicated, or otherwise dispositioned.

| Stable ID | Pass-2 reconciliation |
|---|---|
| C001 | The direct operator mismatch (`>=60 mL/kg` versus `>60 mL/kg`) remains source-grounded. The corrected Supplement 3 eTable 1 locator is `joi180015supp3_prod.pdf#page=6`, not page 7. Event-level boundary and rounding data are absent. |
| C002 | The matched 18% RRR/baseline support .9 per 1,000 = .09%, whereas protocol p. 29 prints .9%. The direct scale contradiction remains; editorial intent is not supplied. |
| C003 | The protocol's cardiac-arrest scale descriptions place CPR/death at 6/7 while Table 6's event-context legend says 4/5. A different Table-6 scale is not defined; no new statistical result is needed to establish the label conflict. |
| C004 | The p. 11 strict `>4` wording conflicts with its immediate 4-6 list, p. 28 `4 or more`, and Supplement 3's 4-6 definition. The corrected Supplement 3 eTable 1 locator is `joi180015supp3_prod.pdf#page=6`, not page 8. Operational classification data are absent. |
| C005 | The same four-hospital reference count (1,052 urgent ICU/PICU admissions) is labelled annual on p. 14 and a two-year total on p. 30. The supplied two-year values approximately reproduce the stated 2/1,000 planning rate; year-specific data and exact patient-days are absent. |
| C006 | The completed recheck confirms DOC-002 p. 30 prints 8.13 stat calls per 1,000 patient-days, a maximum relative reduction of .181, and an absolute reduction of 1.45 on a common denominator. Their product is 1.47153 (1.47 to two decimals); the displayed-input product range 1.4665625 through values below 1.4765025 does not overlap the 1.445 through values below 1.455 range that displays as 1.45. Unrounded inputs and any nonstandard rounding rule remain unsupplied. |
| C007 | Completed recheck, cross-lane numeric implication: DOC-002 p. 30 prints 1,052 unplanned/urgent PICU admissions, 7,300 PICU discharges, 55,963 hospital discharges, 14.5%, and 18 per 1,000 for the same four-hospital cohort. The direct values are 14.4109589% (14.4% conventionally) and 18.7977778 per 1,000 (19 conventionally); the recheck confirms both display-rounding intervals exclude the printed count/denominator results, and one truncation rule does not reconcile both. C007 belongs to numeric relationship N075, not S033. Alternative denominators or display rules are not supplied. |

## P-value display-zero handling

No printed `P = 0`, `p = 0.000`, or equivalent finite-precision display zero was identified in the reviewed inferential bundles. DOC-002 Table 2 uses `<.0001`, which is a threshold display and was not treated as a candidate. No display notation produced a candidate.

## New-candidate outcome and limitations

**Pass-2 discovery before the quality-audit append: 0 new distinct candidates.** The later append-only quality audit registered C006 and C007 from DOC-002 p. 30; this amendment reconciles both records without assigning a disposition. The complete current cross-lane set is C001–C007.

Limitations: adjusted GEE/clustered estimates usually lack raw model inputs, covariance/variance estimators, degrees of freedom, exact multiplicity implementation, and complete estimand mappings. The protocol/SAP often specifies analysis without reporting a fitted result. No sidedness, denominator, variance, covariance, model, or correction rule was inferred from convention, and diagnostic approximations were not used to contradict a printed result.

## Completion counts

- Statistical relationships reviewed: **45/45** (`S001`–`S045`), each explicitly `PASS_2_COMPLETE` in this artifact.
- Stable ledger IDs reconciled against completed mechanical recheck: **7/7** (`C001`, `C002`, `C003`, `C004`, `C005`, `C006`, `C007`).
- New distinct candidates in original pass-2 discovery: **0**; later quality-audit append-only candidates reconciled here: **2** (`C006`, `C007`).
- Corrected Supplement 3 locators reaffirmed: **C001 p. 6; C004 p. 6**.
