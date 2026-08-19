# Statistical Consistency Pass 1

## Scope and completion

This independent pass processed every canonical relationship in `statistics/relationship_inventory.md`: **S001-S071 (71 of 71)**. It used only current-run source-linked maps and direct supplied-PDF confirmation. It did not consult legacy candidate, checker, rechecker, reviewer, or final-report outputs, and it assigns no C IDs, severity, validity, acceptance, rejection, or correction.

- **Relationship completion:** every S001-S071 is `PASS_1_COMPLETE` in the canonical inventory.
- **Point-estimate containment and endpoint order:** all reported point estimates lie within their own printed intervals and every printed lower/upper interval pair is ordered, including negative-scale intervals. No containment or ordering observation was emitted.
- **Sign/direction and measure/scale checks:** binary OR/RD, count RR/rate, WMD/mean-difference, and SMD labels match their displayed values except for the explicit cross-location standardized-QOL direction-label observation below.
- **Cross-location repetitions:** all repeated main/supplement values were checked after matching comparison, outcome, population/grouping, time, and measure. Four direct printed-value/label observations are recorded below.
- **P-value/test/statistic/SE compatibility:** the supplied article gives 95% CIs, two-tailed P<.05 convention, effect measures, and a model-selection statement, but not the exact effect-test calculation, SE, degrees of freedom, CI construction, study weights, covariance, continuity correction, or variance estimator. Accordingly, the pass completed only a threshold-direction screen where both a 95% CI and P were printed. All such screens are directionally coherent. The sole interval-to-P arithmetic calculation is explicitly a diagnostic (P1-OBS-002), not an exact rule application.
- **P display zeros:** 0. No `P = 0`/`p = 0.000` display occurred. The printed serious-adverse-event *incidence* of 0 per patient with CI 0.00-0.01 (S056) is coherent as a non-P printed value and produces no observation.

## Relationship-level check record

| S IDs | Applied supplied-source checks | Pass-1 result |
|---|---|---|
| S001, S003-S004, S006-S019 | Estimate-within-CI; endpoint order; null/sign direction; OR/RR/rate/SMD/mean-difference label; repeated-location agreement where present; P threshold-direction screen where P printed | PASS_1_COMPLETE — no observation |
| S002 | Estimate-within-CI; endpoint order; null/sign direction; OR label; repeated-location agreement; P threshold-direction screen plus clearly-labelled approximate CI-to-P diagnostic | PASS_1_COMPLETE — P1-OBS-002 |
| S005 | Estimate-within-each-CI; endpoint order; SMD/direction; abstract/narrative/Figure 4 matching | PASS_1_COMPLETE — P1-OBS-001 |
| S020 | Estimate-within-CI; endpoint order; RD/OR labels; main/supplement comparison and baseline-table total | PASS_1_COMPLETE — P1-OBS-004 |
| S021-S023 | Direction and measure/population labels; repeated main/supplement agreement; P screen where printed. No CI is printed for S021-S023. | PASS_1_COMPLETE — no observation |
| S024 | Estimate-within-each-CI; endpoint order; CAT higher-worse scale label; main/supplement matching | PASS_1_COMPLETE — P1-OBS-005 |
| S025-S035 | Estimate-within-CI; endpoint order; WMD/RD/OR labels; individual-instrument direction labels; repeated main/supplement agreement; P threshold-direction screen where P printed | PASS_1_COMPLETE — no observation |
| S036-S043 | Estimate-within-CI; endpoint order; subgroup population labels; OR/RR/SMD labels; P threshold-direction screen where P printed | PASS_1_COMPLETE — no observation |
| S044-S052 | Estimate-within-CI; endpoint order; subgroup/study-design labels; OR/RR/SMD labels. No P is printed for S044-S054. | PASS_1_COMPLETE — no observation |
| S053-S054 | Estimate-within-CI; endpoint order; Table 2 quality-of-life scale direction against DOC-001 p. 3 standardized-SMD direction and Figure 4 direction | PASS_1_COMPLETE — P1-OBS-003 |
| S055-S057 | Pooled-incidence containment/order; incidence-rate label and adverse-event population definition | PASS_1_COMPLETE — no observation |
| S058-S060 | Protocol/SOE definition identity and relationship-to-main-analysis label check; no source-defined numerical compatibility calculation applicable | PASS_1_COMPLETE — no observation |
| S061-S064 | Threshold/target/use parameter order, units, scale/definition labels; no inferential test/CI compatibility supplied | PASS_1_COMPLETE — no observation |
| S065-S067 | Direction label and P display; no estimate, CI, test statistic, or exact denominator-to-rate mapping supplied | PASS_1_COMPLETE — no observation |
| S068-S071 | Estimate-within-CI/order where a CI printed; outcome/scale label; matched-comparison check against DOC-001 where applicable | PASS_1_COMPLETE — no observation |

## Local checker observations

### P1-OBS-001 — BPAP quality-of-life pooled CI has different printed upper endpoints

- **S ID:** S005.
- **Direct source evidence:** DOC-001 Figure 4 on [main article PDF p. 5](../../../jama_wilson_2020_oi_190154.pdf#page=5) prints overall SMD `0.16 (-0.06 to 0.38)`. The same page’s BPAP narrative and [main article PDF p. 1](../../../jama_wilson_2020_oi_190154.pdf#page=1) print `0.16 (-0.06 to 0.39)`, 9 studies/833 patients; p. 1 also prints P=.15.
- **Applicable rule:** same matched comparison, outcome, population, study count, patient count, point estimate, and measure should repeat the same rounded CI, unless a source-supplied distinct analysis/precision rule is stated.
- **Direct observation:** the upper endpoint is 0.38 in Figure 4 and 0.39 in abstract/narrative.
- **Diagnostic:** none required; this is a direct transcription comparison, not a derived calculation.
- **Alternative source-grounded interpretation:** the source does not state why the figures/narrative use different rounding. Independent display precision or one unreported analysis/export is possible.
- **Human question:** Which upper CI endpoint is the intended value for the BPAP/no-device quality-of-life pooled result, and are Figure 4 and narrative generated from the same final analysis?
- **Pass-1 handling:** local observation only; no stable C ID assigned.

### P1-OBS-002 — HMV mortality P value has a diagnostic mismatch with the rounded OR/CI, but the exact compatibility definition is absent

- **S ID:** S002.
- **Direct source evidence:** [main article PDF p. 6](../../../jama_wilson_2020_oi_190154.pdf#page=6) and p. 1 print HMV/no-device mortality `OR 0.56 (95% CI, 0.29-1.08); P=.49; 2 studies; 175 patients`. Figure 1 on p. 4 repeats the OR/CI; its `P=.01` is explicitly the HMV forest-plot heterogeneity P, not the pooled-effect P. DOC-001 p. 3 supplies a fixed-effect Mantel-Haenszel rule for comparisons with fewer than 3 studies and a two-tailed significance convention.
- **Applicable rule:** no exact interval-to-P rule is supplied. The available source rule permits only a diagnostic based on the rounded log OR and rounded 95% CI, not a definitive test-equivalence check.
- **Diagnostic approximation:** using `SE ≈ (ln(1.08)-ln(0.29))/(2×1.96)` and `z ≈ ln(0.56)/SE` gives an approximate two-sided P near .08. This is not a replacement for the reported model because the source omits the exact CI/test construction, weights, continuity correction, and other variance details.
- **Direct observation:** the printed CI crosses 1 and P=.49 is directionally non-significant; therefore the threshold-direction screen is coherent. The approximate numerical P differs from .49.
- **Alternative source-grounded interpretation:** the displayed P may arise from an unreported calculation/analysis quantity or from methods not recoverable from the rounded result.
- **Human question:** What exact effect-test, CI construction, weights, and zero-event/continuity handling produced the HMV mortality P=.49, and does that P refer to the same pooled OR/CI?
- **Pass-1 handling:** `DIAGNOSTIC_OBSERVATION`, **not a candidate emitted in pass 1** because the package does not supply a compatible exact inferential definition.

### P1-OBS-003 — Standardized quality-of-life direction labels conflict across the main article

- **S IDs:** S053 and S054; direction context also bears on S005 and Figure 4.
- **Direct source evidence:** [main article PDF p. 3](../../../jama_wilson_2020_oi_190154.pdf#page=3) says that for different quality-of-life measures the authors calculated SMD and standardized direction so higher scores represent better outcomes. Figure 4 on [p. 5](../../../jama_wilson_2020_oi_190154.pdf#page=5) labels negative SMDs `Favors NIPPV` and positive SMDs `Favors No NIPPV`. Table 2 on [p. 8](../../../jama_wilson_2020_oi_190154.pdf#page=8), directly under its RCT SMD 0.10 and observational SMD 0.97 results, says “Higher scores indicate worse quality of life.”
- **Applicable rule:** matched standardized outcome directions, SMD signs under the stated group subtraction, and favor labels must agree or explicitly identify distinct scale contexts.
- **Direct observation:** p. 3 says higher standardized scores are better; Table 2 says higher scores are worse; Figure 4 supplies the negative/positive favor labels but not the group-subtraction order.
- **Diagnostic:** none; direct label comparison only.
- **Alternative source-grounded interpretation:** Table 2 may describe original scales and Figure 4 may use control-minus-intervention subtraction, but neither distinction is stated and the pooled instruments have mixed native directions.
- **Human question:** What sign transformations and group-subtraction order were used, and which figure favor labels and table direction statement were intended for the standardized SMDs?
- **Pass-1 handling:** local observation only; no stable C ID assigned.

### P1-OBS-004 — Cheung BPAP-versus-CPAP effectiveness total differs from its displayed baseline-group total

- **S ID:** S020.
- **Direct source evidence:** [Supplement 2 PDF p. 19](../../../joi190154supp2_prod.pdf#page=19) lists Cheung 2010 CPAP `24 Patients` and BPAP-ST `23 Patients`, totaling 47 in the displayed two-group baseline row. [Supplement 2 PDF p. 43](../../../joi190154supp2_prod.pdf#page=43) reports the matched `BPAP vs. CPAP` exacerbation result as `1 RCT17; 49 patients`, 30.43% vs 53.85%, RD -0.23 (-0.50 to 0.03), OR 0.38 (0.12 to 1.22). DOC-001 p. 6 independently repeats `1 RCT of 49 patients` with the same result.
- **Applicable rule:** where study identity, intervention pair, and outcome table match, displayed participant totals should reconcile or state the analysis-population difference.
- **Direct observation:** the visible baseline groups sum to 47; the matched effectiveness result gives 49.
- **Diagnostic:** `24 + 23 = 47`; no denominator has been inferred from the percentages.
- **Alternative source-grounded interpretation:** the 49 may be an analysis/randomized total that includes two participants not represented in the eTable 6 baseline/intervention row. The supplied sources do not define such a difference.
- **Human question:** Does the effectiveness total include two randomized participants absent from the displayed two-group baseline row, or is either reported total incorrect?
- **Pass-1 handling:** local observation only; no stable C ID assigned.

### P1-OBS-005 — High-/low-intensity CAT CI has different printed endpoints in main text and Supplement 2

- **S ID:** S024.
- **Direct source evidence:** [main article PDF p. 7](../../../jama_wilson_2020_oi_190154.pdf#page=7) reports high- versus low-intensity HMV/BPAP mix CAT QOL `WMD, 2.30 (95% CI, -2.23 to 6.83); P=.32` in one RCT of 14 patients. [Supplement 2 PDF p. 43](../../../joi190154supp2_prod.pdf#page=43) reports the matching high-/low-intensity comparison, one RCT/14 patients, `WMD: 2.30, 95% CI: -2.35 to 6.95`; it identifies CAT as higher=worse.
- **Applicable rule:** same matched comparison, study count, patient count, point estimate, outcome, and measure should have the same rounded CI unless the source states different calculation or precision.
- **Direct observation:** the lower/upper endpoints are -2.23/6.83 in the main article and -2.35/6.95 in Supplement 2, while the point estimate remains 2.30.
- **Diagnostic:** none required; direct source-value comparison only.
- **Alternative source-grounded interpretation:** the files may reflect different analysis/export versions or an unreported calculation distinction. Neither supplied location identifies one.
- **Human question:** Which CI belongs to the 14-patient high-/low-intensity CAT result, and do the article and eTable 10 use the same analysis dataset and computation?
- **Pass-1 handling:** local observation only; no stable C ID assigned.

## Missing definitions and limitations

- No source supplies an exact reported SE, test statistic, degrees of freedom, covariance, variance estimator, continuity correction, study weights, or a formal mapping from each rounded CI to its P value. This prevents exact CI/P/statistic compatibility claims.
- Forest-plot P values printed after `I2` are heterogeneity P values. They were not compared as pooled-effect P values.
- S021-S023, S039, S044-S054, S065-S067, and S071 lack one or more interval, effect estimate, P value, test, or denominator inputs needed for broader arithmetic/inferential reconciliation; the named source fields were checked without inference from convention.
- The article’s p. 3 completed-analysis model rule and DOC-002 protocol p. 11 planned model rule differ by their stated threshold/variance wording. Pass 1 did not infer which protocol formulation applies to any individual final result beyond the final article’s explicit statement.
- All observations remain unadjudicated local checker records. A later coordinator may register only independently supported candidates; this pass assigns no stable candidate IDs.

## Explicit pass-1 completion register

This register expands the grouped scope table so every canonical relationship has a machine-readable individual completion record.

| S ID | Pass-1 status |
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
| S039 | PASS_1_COMPLETE |
| S040 | PASS_1_COMPLETE |
| S041 | PASS_1_COMPLETE |
| S042 | PASS_1_COMPLETE |
| S043 | PASS_1_COMPLETE |
| S044 | PASS_1_COMPLETE |
| S045 | PASS_1_COMPLETE |
| S046 | PASS_1_COMPLETE |
| S047 | PASS_1_COMPLETE |
| S048 | PASS_1_COMPLETE |
| S049 | PASS_1_COMPLETE |
| S050 | PASS_1_COMPLETE |
| S051 | PASS_1_COMPLETE |
| S052 | PASS_1_COMPLETE |
| S053 | PASS_1_COMPLETE |
| S054 | PASS_1_COMPLETE |
| S055 | PASS_1_COMPLETE |
| S056 | PASS_1_COMPLETE |
| S057 | PASS_1_COMPLETE |
| S058 | PASS_1_COMPLETE |
| S059 | PASS_1_COMPLETE |
| S060 | PASS_1_COMPLETE |
| S061 | PASS_1_COMPLETE |
| S062 | PASS_1_COMPLETE |
| S063 | PASS_1_COMPLETE |
| S064 | PASS_1_COMPLETE |
| S065 | PASS_1_COMPLETE |
| S066 | PASS_1_COMPLETE |
| S067 | PASS_1_COMPLETE |
| S068 | PASS_1_COMPLETE |
| S069 | PASS_1_COMPLETE |
| S070 | PASS_1_COMPLETE |
| S071 | PASS_1_COMPLETE |
