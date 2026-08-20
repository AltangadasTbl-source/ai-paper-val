# Statistical Consistency Review — Pass 1

**Runtime agent ID:** `/root/statistics_pass_1`  
**Execution:** fresh `gpt-5.6-terra`, high reasoning effort; independent pass 1.  
**Scope:** every canonical statistical relationship `S001`--`S032`, checked against the fresh extraction maps, fresh native/layout text, and rendered source pages where layout was material. No legacy audit derivative or external source was used.

## Review rule and limits

For each relationship, this pass checked printed point-estimate containment and endpoint ordering where an interval was supplied; estimate sign/direction, measure/scale/reference labels; matched repeats; and denominators/cross-source occurrences in its assigned scope. A P-value, interval, test, statistic, or SE was mechanically compared only when the package states compatible analysis definitions. Where it does not state the test variant, sidedness, degrees of freedom, variance estimator, covariance, model-to-estimand mapping, or multiplicity rule needed for an exact reconstruction, that absence is recorded rather than inferred. Any arithmetic-style comparison below is explicitly diagnostic and does not replace the reported analysis.

## Complete S-ID records

| S ID | Pass-1 check record | Result / limitation |
|---|---|---|
| S001 | `PASS_1_COMPLETE`. DOC-001 p. 3 defines randomized-group analysis (with consent withdrawals excluded), no imputation, unadjusted chi-square equal-proportion comparisons, RR/RD, and 95% CIs. | Definition-only relationship; no paired reported estimate to reconcile. Test continuity-correction/variance details are not supplied. |
| S002 | `PASS_1_COMPLETE`. DOC-001 p. 4 labels the adjusted analysis as hierarchical multivariable log-binomial regression with stated covariates/random effects; adjusted primary RR 0.98 (95% CI 0.87-1.11), P=.75 is located at DOC-001 p. 7. | Point lies inside ordered positive CI; CI includes RR null 1 and direction/label agree. Exact P/CI reconstruction is not attempted: coefficient, SE, random-effect variance, and inferential rule are absent. |
| S003 | `PASS_1_COMPLETE`. DOC-001 p. 4 supplies ordinal-logistic and Cox/Kaplan-Meier/log-rank labels. DOC-001 p. 5 reports ordinal OR 0.97 (0.71-1.34), P=.88 and time-to-death HR 1.13 (0.76-1.69), P=.54; the HR result repeats in DOC-003 p. 5. | Both points lie in ordered CIs, CIs include 1, and the HR repeat matches exactly. Ordinal-model coefficient/SE and survival-test details needed to reproduce P values are not supplied. |
| S004 | `PASS_1_COMPLETE`. DOC-001 p. 4 defines logistic treatment-by-subgroup interaction and chi-square cooling-time comparison; DOC-001 p. 7 prints subgroup interaction P=.43 and P=.33. | Labels, subgroup direction, and interaction placement are coherent. Interaction coefficients, cell definitions for every tested contrast, and model SEs are not supplied for exact P reconstruction. |
| S005 | `PASS_1_COMPLETE`. DOC-001 p. 4 defines per-protocol/as-treated eligibility and compliance, two-sided P<.05, no multiplicity adjustment, and exploratory secondary outcomes. | Definition-only relationship; no direct contradiction. The package does not supply a full model-to-estimand mapping for every secondary comparison. |
| S006 | `PASS_1_COMPLETE`. Checked unadjusted and adjusted favorable-outcome inference at DOC-001 pp. 1, 5, and 7. | Unadjusted RR 0.99 (0.82-1.19), P=.94 and adjusted RR 0.98 (0.87-1.11), P=.75 have ordered CIs containing estimates and null 1; counts/labels agree. One cross-location sign candidate is recorded as **OBS-01**. |
| S007 | `PASS_1_COMPLETE`. Checked ordinal OR 0.97 (0.71-1.34), P=.88; six-month mortality RR 1.15 (0.80-1.64), P=.45; and HR 1.13 (0.76-1.69), P=.54 at DOC-001 p. 5. | Points are contained in ordered CIs; all ratio CIs include 1, and higher mortality in hypothermia agrees with RR/HR directions. The RR and HR address different supplied estimands; no contradiction. |
| S008 | `PASS_1_COMPLETE`. Checked Table 2 adverse-event RRs/CIs/P values at DOC-001 p. 7 and matching eTable 6 P values at DOC-003 p. 10. | All listed Table-2 points are inside ordered CIs and directions agree with counts. Two matched-result P-value conflicts are recorded as **OBS-02** and **OBS-03**. The stated unadjusted chi-square rule supports only diagnostic compatibility, because its exact variant is not named. |
| S009 | `PASS_1_COMPLETE`. Checked Table-2 subgroup row tests and interaction P values at DOC-001 p. 7. | Each RR is inside an ordered CI and each CI includes 1; P values are attached to the stated rows/interactions. Interaction-model coefficients/SEs are not supplied. |
| S010 | `PASS_1_COMPLETE`. Checked per-protocol pneumonia RR 1.23 (1.04-1.47), P=.02 and as-treated RR 1.29 (1.09-1.53), P=.003 at DOC-001 p. 6, with matched eTables 9 and 11 in DOC-003 pp. 14 and 19. | Points are contained in ordered CIs above 1; repeats, outcome labels, and analysis-population labels agree. Exact P reconstruction lacks model/cell/test-variant detail. |
| S011 | `PASS_1_COMPLETE`. DOC-002 p. 15 defines secondary proportional-odds/sliding-dichotomy estimands. | Definition-only relationship; no result estimate or interval to test. |
| S012 | `PASS_1_COMPLETE`. DOC-002 p. 28 states cumulative-logit reference ln(OR)=0.62, one-sided linear-rank test, 182/arm, and 96% one-sided power. | No internal printed contradiction. The full ordinal distribution, variance rule, allocation/attrition calculation, and power formula are absent, so no independent power reconstruction is made. |
| S013 | `PASS_1_COMPLETE`. DOC-002 pp. 84-86 supplies Version-9 alpha/interim/multiplicity statements. | Protocol-version definitions are not treated as the same estimand as later DSMC or final results. Detailed separately linked SAP material is not embedded; no contradiction is inferred. |
| S014 | `PASS_1_COMPLETE`. DOC-002 p. 188 states DSMC normal-approximation binomial difference, interim |Z|>=3 (approximately P<.001), final |Z|>=1.975 (P=.048), and no other multiplicity adjustment. | Endpoint/direction issue not present. Exact alpha-spending or boundary recalculation needs the sequential design inputs and information fractions, which are not supplied. |
| S015 | `PASS_1_COMPLETE`. Checked DOC-002 p. 189 DSMB 2015 GOS-E/outcome P-value array against its displayed group counts and outcome labels. | P values have stated row association and no duplicated final-study comparator. Exact test type/variance rule for the row array is not supplied; no P reconstruction. |
| S016 | `PASS_1_COMPLETE`. Checked DOC-002 p. 191 DSMB 2016 GOS-E/outcome P-value array and associated figure labels. | Printed denominators distinguish GOS-E=321 from six-month survival=341; values and label placement are coherent. Exact test definitions are absent. |
| S017 | `PASS_1_COMPLETE`. Checked DOC-002 p. 193 DSMB 2017 GOS-E/outcome P-value array and associated figure labels. | Printed denominators distinguish GOS-E=364 from survival=390; proportions/directions and P-row placement are coherent. Exact test definitions are absent. |
| S018 | `PASS_1_COMPLETE`. DOC-003 p. 4 labels eFigure 1 as longitudinal mixed-linear-model least-square means with 95% CIs and participant random effects. | Figure has no printed numeric estimate/CI endpoints to test; visual direction is not converted to invented values. Model covariance/SE details are absent. |
| S019 | `PASS_1_COMPLETE`. DOC-003 p. 5 repeats unadjusted Kaplan-Meier/Cox six-month mortality HR 1.13 (0.76-1.69), P=.54 from DOC-001 p. 5. | Exact matched repeat; point lies inside ordered CI including 1 and direction agrees with the mortality comparison. Cox/log-rank reconstruction inputs are absent. |
| S020 | `PASS_1_COMPLETE`. Checked eTable 2 randomization-place/timing P values at DOC-003 p. 6. | P values are row-aligned with their labelled quantities; control temperature is explicitly NA. Test-family and distributional assumptions for baseline comparisons are not supplied. |
| S021 | `PASS_1_COMPLETE`. Checked eTable 4 P values and layout at DOC-003 p. 8 against rendered page. | The wrapped value is `<.0001`, not a display zero; `P=.16` is aligned to “Adrenaline >5 mcg/min,” and `P=.90` to its duration row. No `DISPLAY_ZERO_NOT_CANDIDATE` record is applicable. Test definitions are not supplied. |
| S022 | `PASS_1_COMPLETE`. Checked eTable 5 P values at DOC-003 p. 9. | Values are in listed outcome order and no paired estimate/CI is supplied. Test/distribution definitions are not supplied. |
| S023 | `PASS_1_COMPLETE`. Checked eTable 6 adverse-event P values at DOC-003 p. 10 against DOC-001 Table 2 p. 7. | Direct matched-result conflicts for the two bleeding rows are recorded as **OBS-02** and **OBS-03**. No display zero: `<.0001` is an inequality. |
| S024 | `PASS_1_COMPLETE`. Checked eTable 7 overall favorable-GOS-E P=.09 at DOC-003 p. 11. | Outcome and temperature-tertile labels are explicit; row proportions have ordered CIs. Test type/trend specification is absent, so no exact P/CI compatibility claim. |
| S025 | `PASS_1_COMPLETE`. Checked eTable 8 per-protocol baseline P values at DOC-003 p. 13. | P values are aligned to defined baseline variables; no compatible test rule is supplied. |
| S026 | `PASS_1_COMPLETE`. Checked eTable 9 per-protocol RR/CIs/P values and interactions at DOC-003 p. 14. | Every RR is inside an ordered positive CI; CIs/patterns agree with null inclusion or exclusion. Primary and pneumonia outcome/population labels agree. Exact P reconstruction is definition-limited. |
| S027 | `PASS_1_COMPLETE`. Checked sensitivity primary RR 1.00 (0.77-1.30), P=.98 at DOC-003 p. 16. | Point is contained in an ordered CI including 1; outcome, sensitivity population, and direction agree. Exact test variant is not supplied. |
| S028 | `PASS_1_COMPLETE`. Checked as-treated eTable 10 baseline P values and displayed No. (%) cells at DOC-003 p. 18. | P values have baseline-row labels; test rules are absent. Two cells under the Normothermia No. (%) column directly contradict their header/count denominator and are recorded as **OBS-04** and **OBS-05**. |
| S029 | `PASS_1_COMPLETE`. Checked eTable 11 as-treated RRs/CIs/P values/interactions at DOC-003 p. 19. | Points are inside ordered CIs. The distinct adjusted row is labelled “unfavorable outcome,” whereas the unadjusted primary row is favorable outcome; no contrary estimand mapping is supplied, so no direction contradiction is inferred. |
| S030 | `PASS_1_COMPLETE`. Checked as-treated sensitivity RR 1.02 (0.80-1.31), P=.85 at DOC-003 p. 20. | Point lies inside ordered CI including 1; outcome/population/measure labels agree. Exact test variant is not supplied. |
| S031 | `PASS_1_COMPLETE`. Checked eTable 12 scenario RRs/RDs/CIs/P values at DOC-003 p. 21 with supplied scenario-specific chi-square/CMH/Miettinen-Nurminen definitions. | Every printed point lies in an ordered CI; RR/RD null inclusion is coherent with stated P values. Exact numerical reconstruction still lacks imputed-data and stratum inputs for scenario 3. |
| S032 | `PASS_1_COMPLETE`. Checked post-hoc adequate-cooling tests/models at DOC-003 pp. 22-23. Unadjusted OR 0.91 (0.59-1.41), P=.68 is internally ordered and labelled. | The adjusted OR string is malformed in the rendered supplied source and is recorded as **OBS-06**. The mean-time P=.01 and median-time P=.02 are distinct supplied estimands, not a conflict. |

## Candidate observations for coordinator registration (no stable C IDs assigned here)

### OBS-01 — Primary risk-difference direction differs across matched main-article locations

- **Related S IDs:** S006.
- **Proposed category:** Cross-document numeric inconsistency / Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-001 PDF p. 1, abstract Results (`jama_cooper_2018_oi_180132.pdf#page=1`); DOC-001 PDF p. 5, Results (`#page=5`); DOC-001 PDF p. 7, Table 2 (`#page=7`).
- **Printed values:** Abstract: “risk difference, **0.4%** [95% CI, **−9.4% to 8.7%**]” after 48.8% hypothermia vs 49.1% normothermia. Results text and Table 2: “absolute risk difference, **−0.4** percentage points [95% CI, −9.4 to 8.7]” / “**−0.4** (−9.4 to 8.7).”
- **Direct observation:** The same outcome, groups, counts, interval, RR, and P value are matched, but the abstract prints an unsigned positive point estimate while the text/table print a negative one.
- **Reproducible reasoning:** With the table’s displayed order (hypothermia 48.8% minus normothermia 49.1%), the displayed difference is −0.3 percentage points before rounding and is compatible with printed −0.4, not +0.4. This subtraction is a **diagnostic approximation**; the candidate is the direct cross-location sign mismatch.
- **Missing definition / human question:** Does the abstract intentionally use the reverse contrast while omitting that contrast label, or is its minus sign missing? Confirm the intended risk-difference direction in the publication record.

### OBS-02 — Intracranial-bleeding P value conflicts between matched Table 2 and eTable 6

- **Related S IDs:** S008, S023.
- **Proposed category:** Cross-document numeric inconsistency / Statistical reporting inconsistency.
- **Exact source locations:** DOC-001 PDF p. 7, Table 2, “New or increased intracranial bleeding” (`jama_cooper_2018_oi_180132.pdf#page=7`); DOC-003 PDF p. 10, eTable 6, same row (`joi180132supp2_prod.pdf#page=10`).
- **Printed values:** Both sources print hypothermia **47/260 (18.1%)** and normothermia **37/240 (15.4%)**. Table 2 prints RR **1.23 (0.43-3.5)** and **P=.70**; eTable 6 prints **P=.43**.
- **Direct observation:** Same population, time window, outcome wording, counts, and arm order have different P values.
- **Reproducible reasoning:** DOC-001 p. 3 states that adverse-event proportions were compared by unadjusted chi-square test for equal proportions. No exact P calculation is substituted because continuity-correction/test-variant details are not supplied; the qualifying issue is the direct supplied-source mismatch.
- **Missing definition / human question:** Which P value belongs to this intracranial-bleeding comparison, and were the Table-2 and eTable-6 values transposed during production?

### OBS-03 — Extracranial-bleeding P value conflicts between matched Table 2 and eTable 6

- **Related S IDs:** S008, S023.
- **Proposed category:** Cross-document numeric inconsistency / Statistical reporting inconsistency.
- **Exact source locations:** DOC-001 PDF p. 7, Table 2, “New significant extracranial bleeding” (`jama_cooper_2018_oi_180132.pdf#page=7`); DOC-003 PDF p. 10, eTable 6, “New significant extra-cranial bleeding” (`joi180132supp2_prod.pdf#page=10`).
- **Printed values:** Both sources print hypothermia **8/260 (3.1%)** and normothermia **6/240 (2.5%)**. Table 2 prints RR **1.17 (0.79-1.74)** and **P=.43**; eTable 6 prints **P=.70**.
- **Direct observation:** Same matched result has different printed P values; these are the reciprocal row values of OBS-02.
- **Reproducible reasoning:** The stated chi-square rule is compatible with reviewing the association, but exact test-variant details are not supplied. The candidate rests on the direct Table-2/eTable-6 mismatch, not a reconstructed P value.
- **Missing definition / human question:** Which P value belongs to this extracranial-bleeding comparison, and were the two bleeding-row P values transposed?

### OBS-04 — eTable 10 Normothermia evacuated-mass-lesion cell reverses count and percentage

- **Related S IDs:** S028.
- **Proposed category:** Numeric or arithmetic inconsistency / Measure, label, or scale inconsistency.
- **Exact source location:** DOC-003 PDF p. 18, eTable 10, Normothermia (n=196), “Evacuated mass lesion V” (`joi180132supp2_prod.pdf#page=18`).
- **Printed value:** Header is “No. (%)”; the cell prints **34.7 (68)**.
- **Direct observation:** A noninteger value occupies the printed count position and the integer occupies the parenthesized percentage position.
- **Reproducible reasoning:** **Diagnostic calculation:** 68/196×100 = 34.69%, rounding to 34.7%; therefore the two displayed tokens reconcile only if read as **68 (34.7)**, opposite the table header/order. The candidate is the direct header-versus-cell ordering conflict.
- **Missing definition / human question:** Confirm whether the intended printed cell is 68 (34.7) and whether a production reversal occurred.

### OBS-05 — eTable 10 Normothermia non-evacuated-mass-lesion cell reverses count and percentage

- **Related S IDs:** S028.
- **Proposed category:** Numeric or arithmetic inconsistency / Measure, label, or scale inconsistency.
- **Exact source location:** DOC-003 PDF p. 18, eTable 10, Normothermia (n=196), “Non-evacuated mass lesion VI” (`joi180132supp2_prod.pdf#page=18`).
- **Printed value:** Header is “No. (%)”; the cell prints **1 (2)**.
- **Direct observation:** Under a No. (%) header this states one participant and 2%, which do not reconcile with n=196 at the shown precision.
- **Reproducible reasoning:** **Diagnostic calculation:** 2/196×100 = 1.02%, rounding to 1.0%/1% as printed; the tokens reconcile as **2 (1)**, opposite their displayed order. This is distinct from OBS-04 because it is a different printed cell/value.
- **Missing definition / human question:** Confirm the intended cell order and count for non-evacuated mass lesion VI.

### OBS-06 — Adjusted odds-ratio interval is malformed in the supplied post-hoc-results text

- **Related S IDs:** S032.
- **Proposed category:** Statistical reporting inconsistency / Measure, label, or scale inconsistency.
- **Exact source location:** DOC-003 PDF p. 22, post-hoc adequate-cooling Results (`joi180132supp2_prod.pdf#page=22`); confirmed in the fresh rendered page and fresh layout/native text.
- **Printed value:** “adjusted odds ratio hypothermia vs normothermia; **0.95 (0.55-275 1.64) P = .84**.”
- **Direct observation:** The string labelled as one 95% CI contains `0.55-275 1.64`, which does not provide two unambiguous ordered endpoints for the stated adjusted OR.
- **Reproducible reasoning:** The unadjusted OR immediately above is 0.91 (0.59-1.41), P=.68; this does not define the adjusted CI. Reading the string as 0.55-1.64 is only a **diagnostic conjecture**, not an applied correction. No exact P/CI check is possible because the adjusted-model coefficient, SE, and intended endpoints are not supplied.
- **Missing definition / human question:** What exact lower and upper 95% CI endpoints were intended, and what is the meaning/source of the printed `275` token?

## Display-zero disposition

**DISPLAY_ZERO_NOT_CANDIDATE count: 0.** No assigned S relationship prints a coherent result as `P=0`, `p=0.000`, or equivalent. The eTable-4 value `<.0001` (S021/S023 scope) is an inequality, not a display zero; no candidate is based on it.

## Pass-1 totals and limitations

- **S-ID coverage:** 32/32 (`S001`--`S032`), each explicitly marked `PASS_1_COMPLETE`.
- **Candidate observations emitted:** 6 (`OBS-01`--`OBS-06`); no stable C IDs assigned.
- **Direct-versus-diagnostic separation:** retained in every observation.
- **Principal limitations:** no supplied embedded SAP text beyond protocol/SAP references; exact P/CI/test compatibility was not reconstructed where the package omits test variant, sidedness, degrees of freedom, covariance/variance estimator, model coefficients/SEs, multiplicity details, or model-to-estimand mapping. Graphical eFigure 1 lacks printed numerical endpoints. Historical protocol/DSMC material was not conflated with final-study estimands absent an exact match.
