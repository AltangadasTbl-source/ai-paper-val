# Statistical Consistency Review — Pass 2

## Scope, independence, and evidence basis

- **Reviewer execution:** fresh `gpt-5.6-terra`, high reasoning effort; runtime agent ID: `/root/statistical_pass_2`. This execution is distinct from the pass-1 runtime ID `/root/statistical_pass_1`.
- **Assigned scope completed:** all 34 canonical inferential relationships, `S001` through `S034`; the complete cross-lane stable ledger `C001`, `C002`, and `C003`; and every mechanical fact in `verification/evidence_recheck.md`.
- **Authority and method:** direct supplied PDFs were treated as authority; current native/layout extraction, mapper records, numeric and cross-source checks, the ledger, and mechanical recheck were used to locate and reconcile evidence. Direct confirmation included DOC-001 Table 2/Figure 3 and the Oxygen Exposure narrative, DOC-003 eFigure 5/eFigure 7/eTable 7, and the cited SAP materials. No web or legacy-review conclusion was used.
- **Checks applied:** point-estimate containment; endpoint order; sign and contrast direction; effect-measure, model, population, and scale labels; duplicate/matched-location agreement; denominator and arithmetic implications; and P-value/test/interval compatibility only when the same compatible inferential mapping was supplied. A diagnostic approximation was never substituted for an unreported model, variance estimator, sidedness, degrees of freedom, covariance, multiplicity, or estimand mapping.
- **Display-zero rule:** no coherent finite-precision `P = 0` / `P = .000` result was a candidate basis. The prospective `P < .05` and `P < .001` conventions in S026/S031 are thresholds, not display-zero results.

## Relationship-level pass-2 completion record

| Stable ID | `PASS_2_COMPLETE` record |
|---|---|
| S001 | **PASS_2_COMPLETE.** The two-sided 95% CI/no-multiplicity convention and site/covariate context are coherent and agree with the SAP convention. No observed estimate is supplied, so no test/interval reconciliation is applicable. |
| S002 | **PASS_2_COMPLETE.** Logistic, Fine-Gray, ordered-logistic, Cox, marginal-RD, and imputation labels remain distinct and compatible with the reported outcome families. The source supplies no universal test/variance mapping across measures; none was assumed. |
| S003 | **PASS_2_COMPLETE.** The OR-scale interaction definition agrees with Figure 3 and post-hoc subgroup labelling. No within-subgroup estimate was conflated with an interaction test. |
| S004 | **PASS_2_COMPLETE.** The adjusted imputed RD `0.7` is contained in `-0.7` to `2.0`; RR/OR intervals are ordered and contain their nulls. Abstract, narrative, and Table 2 repeat the matched imputed RD and `.28`; contrast and population agree. C001 is a duplicate unit-label observation in associated oxygen-exposure narrative, not a primary-effect contradiction. |
| S005 | **PASS_2_COMPLETE.** ICU survivor-duration sHR `1.00 (0.96-1.04), P=.97` is ordered, contains estimate/null, and is directionally neutral. The Fine-Gray label matches the stated competing-risk context. |
| S006 | **PASS_2_COMPLETE.** Acute-hospital survivor-duration sHR `.98 (.94-1.02), P=.27` is ordered, contains estimate/null, and is compatible with conservative-versus-usual direction. A log-scale check is diagnostic only and shows no printed conflict. |
| S007 | **PASS_2_COMPLETE.** Available and imputed DAWOS PORs are ordered and contain estimate/null; the ordinal death=`-1` scale and outcome-specific denominators are supplied. The one P-value column is not explicitly mapped to one displayed POR scale, so exact P/CI reconstruction remains unavailable. |
| S008 | **PASS_2_COMPLETE.** ICU-discharge available/imputed RDs are ordered, contain estimate/null, and retain conservative-minus-usual direction. `P=.94` has no explicit RD-scale test mapping; no unsupported contradiction is emitted. |
| S009 | **PASS_2_COMPLETE.** Hospital-discharge RDs are ordered and directionally labelled. The exact effect scale, variance, and test represented by `P=.46` are not identified; interval/P equality was not inferred. |
| S010 | **PASS_2_COMPLETE.** Sixty-day RDs are ordered and contain estimate/null. A rounded Wald-style diagnostic is compatible with `.25`, but the exact imputation/test mapping is unreported and is not reconstructed. |
| S011 | **PASS_2_COMPLETE.** One-year RDs are ordered and contain estimate/null; linkage-qualified denominators are explicitly distinct. `P=.34` is displayed beside available/imputed columns without a stated effect-scale/test mapping, so no P-versus-RD incompatibility is supportable from the supplied source. |
| S012 | **PASS_2_COMPLETE.** Table 2 adjustment/imputation/censoring footnote is compatible with DOC-001 methods and SAP primary-analysis covariate/model framing. The only linked candidate implication is C001’s extraneous unit after a SpO2 value, mechanically rechecked and not a model-label contradiction. |
| S013 | **PASS_2_COMPLETE.** Diagnosis-subgroup RDs/ORs have ordered intervals containing estimates; strata totals reconcile to the stated primary outcome. `.67` is explicitly an OR-scale interaction P value, not a stratum-effect P value. |
| S014 | **PASS_2_COMPLETE.** COVID-subgroup intervals contain estimates and align with conservative-minus-usual event differences; the two strata reconcile to the primary totals. `.11` is explicitly an OR-scale interaction test. |
| S015 | **PASS_2_COMPLETE.** Ethnicity-subgroup intervals contain estimates; displayed `-0` RD is a rounded signed estimate, not a P-value display zero. Outcome-available denominators are explicitly narrower than linkage denominators; `.64` is the stated OR-scale interaction P value. |
| S016 | **PASS_2_COMPLETE.** Main article and supplement match adjusted one-year HR `1.01 (.96-1.05)`; the supplement’s `.82`, censoring, 66-removal, and 342 undated-death qualifiers identify a compatible but non-exactly reconstructable Cox analysis. No cross-location conflict. |
| S017 | **PASS_2_COMPLETE.** Predicted-risk-tertile ORs lie within ordered CIs and retain adjusted OR and interaction labels. `.18` is not a within-tertile effect P value. |
| S018 | **PASS_2_COMPLETE.** APACHE-II-tertile ORs lie within ordered CIs; `.98` is the stated adjusted OR-scale interaction P value. No duplicate or scale conflict. |
| S019 | **PASS_2_COMPLETE.** PaO2/FIO2 subgroup ORs lie within ordered CIs; `.36` is an adjusted OR-scale interaction P value. No denominator or label inconsistency found. |
| S020 | **PASS_2_COMPLETE.** Data-collection stratum ORs and intervals are ordered and contained. The first-10 `1.43 (1.08-1.90)` is directionally consistent with its positive RD; `.03` and `.18` are interaction-column values under the supplied footnote, not individual-effect P values. |
| S021 | **PASS_2_COMPLETE.** eTable 7’s imputation/censoring definitions agree with primary missingness and outcome-qualified totals. Missingness count distinctions do not create a duplicated population or effect-estimate conflict. |
| S022 | **PASS_2_COMPLETE.** The v1.1 sample-size scenario is prospective only. Its formula, event-rate variance assumptions, and attrition implementation are not supplied; no observed-result or cross-version contradiction is claimed. |
| S023 | **PASS_2_COMPLETE.** Historical RR/OR estimates have ordered intervals containing estimates and retain distinct effect-measure labels. They are external context, not UK-ROX observed effects. |
| S024 | **PASS_2_COMPLETE.** Version-specific prospective sample-size and primary-model scenarios remain explicitly versioned. No same-version observed comparator supports a conflict. |
| S025 | **PASS_2_COMPLETE.** Prospective binary, continuous, duration, and survival methods retain distinct scales. No completed effect/CI/P relationship is supplied for mechanical reconciliation. |
| S026 | **PASS_2_COMPLETE.** Prospective subgroup/interim descriptions distinguish the Peto-Haybittle `P<.001` stopping threshold from a reported P value. It is not a display-zero candidate. |
| S027 | **PASS_2_COMPLETE.** Prospective ITT economic definitions retain 90-day/lifetime, mean, QALY, NMB, and multilevel labels. No observed economic effect or interval is supplied. |
| S028 | **PASS_2_COMPLETE.** Traffic-light rules are prospective operational criteria, not an inferential effect. C003’s broken reference is a duplicate of the ledger’s quantitative-definition reference observation, not a new statistical observation. |
| S029 | **PASS_2_COMPLETE.** SHEAP opening material is prospective and contains no observed inferential result or matched result repetition. |
| S030 | **PASS_2_COMPLETE.** Version/outcome wording identifies an amendment and a SHEAP/version linkage, rather than an unqualified same-estimand contradiction. |
| S031 | **PASS_2_COMPLETE.** Global `P<.05` and interim `P<.001` rules have explicitly distinct roles, remain prospective thresholds, and are not display-zero results. |
| S032 | **PASS_2_COMPLETE.** SAP endpoint, ITT, adjustment, CI/P, and no-futility definitions are compatible with the reported primary analysis after matching scope/version. No unexplained estimand or model-label conflict appears. |
| S033 | **PASS_2_COMPLETE.** Initial-assignment/known-primary-outcome and re-randomisation rules explicitly define, rather than contradict, the analysis population. |
| S034 | **PASS_2_COMPLETE.** Planned subgroup, sensitivity, and economic/lifetime analyses contain no observed estimate, interval, test, or cross-location result to reconcile. |

## Cross-lane ledger and recheck reconciliation

- **C001:** Recheck confirms the exact main-text `95.1% (2.4%) mm Hg` placement and eTable 5’s separate percent/mm Hg labels. This is the existing C001 source-grounded unit-label observation; no new candidate observation is emitted.
- **C002:** Recheck confirms contents-page eTable 1-4 titles do not identify the actual same-numbered eTables. This is existing C002 document-identity evidence; it creates no additional inferential relationship contradiction.
- **C003:** Recheck confirms the SAP’s literal unresolved-reference string after quantitative separation/adherence text. This is existing C003 reference evidence; the intended target and whether it adds necessary detail remain unavailable, so no new statistical contradiction is inferred.

## New-observation determination

**Genuinely new source-grounded candidate observations: 0.** All source-grounded implications found in this pass are either no-candidate checks or duplicates of C001-C003 as specified above. No stable ID is assigned, deleted, merged, renumbered, adjudicated, or otherwise disposed of here.

## Limitations and unavailable definitions

- For the Table 2 shared P-value column (especially S007-S011), the supplied article does not identify the exact test/effect scale, variance estimator, covariance, degrees of freedom, or imputation-combination rule corresponding to each displayed P value. Approximate RD/CI comparisons therefore cannot establish an inconsistency.
- Exact reconstruction of time-to-event P values is unavailable without the Cox/Fine-Gray implementation details, including tie and variance handling; diagnostic log-scale checks were not treated as reported-analysis replacements.
- Prospective protocol/SAP plans and documented amendments lack observed effects where noted and were not treated as mismatched results across versions.
- No figure-only ordinate was digitized as an exact value; no web or external evidence was used.

## Pass-2 totals

- **Relationships assigned/completed:** 34/34 (`S001`-`S034`), each explicitly `PASS_2_COMPLETE`.
- **Stable ledger/recheck IDs reconciled:** 3/3 (`C001`, `C002`, `C003`).
- **Genuinely new candidate observations:** 0.
- **Duplicate existing candidate implications noted:** 3 (`C001`, `C002`, `C003`).
- **Display-zero P-value-only candidates:** 0.
