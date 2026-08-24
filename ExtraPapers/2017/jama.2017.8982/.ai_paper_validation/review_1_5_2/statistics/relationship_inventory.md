# Canonical Statistical Relationship Inventory

## Scope and merge provenance

This canonical inventory merges, without removing source observations, the fresh registers at `statistics/parts/main_statistical_relationships.md` (S001--S017, DOC-001) and `statistics/parts/support_statistical_relationships.md` (S1001--S1012, DOC-002--DOC-003). It is a relationship map, not a candidate ledger or an adjudication record.

Pass 1 reviewer: fresh runtime agent `/root/statistical_pass_1`, `gpt-5.6-terra`, high effort. All records below have been independently revisited against the supplied PDFs and fresh source assets. `PASS_1_COMPLETE` documents coverage only; it is not a validity, severity, or disposition label.

## DOC-001 main article

### S001 — Sample-size planning

- **Printed evidence/location:** DOC-001 PDF p. 3: 80% power; 2-sided `P < .05` with Bonferroni adjustment; 10-percentage-point target difference; 1280 total/320 per treatment group; 20% anticipated loss leading to 1600/400.
- **Population/contrast/model/match key:** cluster RCT simulation; `sample-size-planning`.
- **Pass-1 checks:** `1280 = 4 × 320`; `1600 = 4 × 400`; and `1280 / (1 − 0.20) = 1600`. The reported planning arithmetic is coherent. The article does not state the comparison-wise Bonferroni alpha or simulation inputs in sufficient detail to recreate power.
- **PASS_1_COMPLETE:** no provisional candidate.

### S002 — Analysis-model definition

- **Printed evidence/location:** DOC-001 PDF p. 3: respondent/nonrespondent comparison used chi-square; unadjusted and adjusted GEE logistic regression accounted for within-hospital clustering and listed individual/baseline covariates.
- **Population/contrast/model/match key:** prespecified analyses; `analysis-model-definition`.
- **Pass-1 checks:** GEE/logistic, clustering, and covariate descriptions are compatible with the Table 3 model footnote on p. 7. The supplied article does not define working correlation, variance estimator, degrees of freedom, or every covariate-selection rule; no test-statistic/SE reconstruction is applicable.
- **PASS_1_COMPLETE:** no provisional candidate.

### S003 — OR-to-adjusted-risk-difference conversion

- **Printed evidence/location:** DOC-001 PDF p. 3: adjusted odds ratios and 95% CIs were converted to adjusted risk differences and 95% CIs using observed control prevalence.
- **Population/contrast/model/match key:** four outcomes; `effect-measure-conversion`.
- **Pass-1 checks:** p. 7 Table 3 footnote repeats the logistic-OR-to-aRD/CI conversion and labels estimates as adjusted risk differences, not odds ratios. Raw adjusted-risk subtraction agrees with displayed aRDs to shown precision where both are printed. The unprinted ORs, conversion method details, and covariance are unavailable, so interval reconstruction is not performed.
- **PASS_1_COMPLETE:** no provisional candidate.

### S004 — Multiplicity and imputation labels

- **Printed evidence/location:** DOC-001 PDF p. 5/p. 7: Hochberg-adjusted P values and a post hoc analysis using 20 imputed data sets.
- **Population/contrast/model/match key:** multiple outcomes/missing data; `multiplicity-imputation`.
- **Pass-1 checks:** main Table 3 and eTable 4 identify Hochberg-adjusted logistic-regression P values; protocol DOC-002 specifies planned Bonferroni adjustment. These are planned-versus-final analysis descriptions, not interchangeable inferential rules. The package supplies no final amendment/history or same-result two-method comparator; no contradiction is asserted.
- **PASS_1_COMPLETE:** no provisional candidate; missing definition is the final decision-rule/change documentation.

### S005 — Respondent/nonrespondent P-value summary

- **Printed evidence/location:** DOC-001 PDF p. 6: age <30 years, Black race, never married, and no college differed, `P < .001` for all.
- **Population/contrast/model/match key:** respondent vs nonrespondent; `nonresponse-comparison`.
- **Pass-1 checks:** DOC-003 PDF pp. 3--4 eTable 2 supplies chi-square P values `<.0001` for the matched age, race/ethnicity, education, and marital-status variables; these satisfy the less-precise main-article bound. No display zero is present.
- **PASS_1_COMPLETE:** no provisional candidate.

### S006 — Supine: mHealth main effect

- **Printed evidence/location:** DOC-001 PDF pp. 1, 6--7: aRD 8.9% (95% CI 5.3% to 11.7%), `P < .001`; adjusted risks 89.1% vs 80.2%.
- **Population/contrast/model/match key:** adjusted mHealth main effect; `outcome-supine-mhealth-main`.
- **Pass-1 checks:** estimate is inside ordered CI; 89.1 − 80.2 = 8.9 percentage points; positive direction agrees with narrative and repeated abstract/table locations. The Hochberg-adjusted P value and transformed 95% CI are not a common, fully defined inversion rule, but their signs are compatible.
- **PASS_1_COMPLETE:** no provisional candidate.

### S007 — Supine: NQI-only interaction-model effect

- **Printed evidence/location:** DOC-001 PDF p. 7: aRD −1.7% (−10.1% to 4.7%), `P = .74`; adjusted risks 78.5% vs 80.2%.
- **Population/contrast/model/match key:** interaction model; `table3-nqi-main-supine`.
- **Pass-1 checks:** estimate is within ordered CI; 78.5 − 80.2 = −1.7 points; direction and P/CI null inclusion are compatible. P is Hochberg-adjusted; exact CI/P inversion is not defined.
- **PASS_1_COMPLETE:** no provisional candidate.

### S008 — Supine: NQI main-effect model and interaction test

- **Printed evidence/location:** DOC-001 PDF p. 7: aRD 2.6% (−3.1% to 7.2%), `P = .34`; adjusted risks 82.8% vs 80.2%; multiplicative interaction `P = .01`.
- **Population/contrast/model/match key:** Table 3 main-effect model plus separate interaction test; `table3-supine-interaction`.
- **Pass-1 checks:** Table 3 column header identifies the 2.6-point contrast as **NQI only** (the fresh part’s wording “mHealth-only interaction context” has been corrected in this canonical map). The estimate is contained in an ordered CI; 82.8 − 80.2 = 2.6 points. The distinct interaction P is correctly labeled as multiplicative logistic-regression interaction, not the NQI-effect P.
- **PASS_1_COMPLETE:** no provisional candidate.

### S009 — Supine: combined NQI+mHealth interaction contrast

- **Printed evidence/location:** DOC-001 PDF p. 7: aRD 9.4% (2.9% to 13.6%), `P = .03`; adjusted risks 89.6% vs 80.2%.
- **Population/contrast/model/match key:** interaction model; `table3-supine-interaction-estimate`.
- **Pass-1 checks:** estimate is inside ordered CI and 89.6 − 80.2 = 9.4 points. P is Hochberg-adjusted whereas the aRD CI is transformed from logistic OR/CI; the supplied evidence does not define a shared inversion rule, so only directional compatibility is assessed.
- **PASS_1_COMPLETE:** no provisional candidate.

### S010 — Room sharing: NQI main effect

- **Printed evidence/location:** DOC-001 PDF p. 7: aRD 3.7% (−0.4% to 7.2%), `P = .07`; adjusted risks 74.1% vs 70.4%.
- **Population/contrast/model/match key:** adjusted NQI main effect; `table3-nqi-roomshare`.
- **Pass-1 checks:** estimate containment, endpoint ordering, and 74.1 − 70.4 = 3.7 points are coherent; null is inside CI. Hochberg/transform rules preclude exact P/CI inversion.
- **PASS_1_COMPLETE:** no provisional candidate.

### S011 — Room sharing: mHealth main effect

- **Printed evidence/location:** DOC-001 PDF pp. 1, 6--7: aRD 12.4% (9.3% to 15.1%), `P < .001`; adjusted risks 82.8% vs 70.4%; interaction `P = .08`.
- **Population/contrast/model/match key:** adjusted mHealth main effect; `outcome-roomshare-mhealth-main`.
- **Pass-1 checks:** estimate is in ordered CI; adjusted-risk difference is 12.4 points; sign and abstract/narrative/table repetitions agree. The interaction P is separately labeled and not conflated with effect P.
- **PASS_1_COMPLETE:** no provisional candidate.

### S012 — No soft bedding: NQI main effect

- **Printed evidence/location:** DOC-001 PDF p. 7: aRD 3.3% (−1.4% to 7.8%), `P = .22`; adjusted risks 70.9% vs 67.6%.
- **Population/contrast/model/match key:** adjusted NQI main effect; `table3-nqi-softbedding`.
- **Pass-1 checks:** estimate containment, ordered endpoints, 3.3-point adjusted-risk subtraction, and positive direction are coherent; null is inside CI.
- **PASS_1_COMPLETE:** no provisional candidate.

### S013 — No soft bedding: mHealth main effect

- **Printed evidence/location:** DOC-001 PDF pp. 1, 6--7: aRD 11.8% (8.1% to 15.2%), `P < .001`; adjusted risks 79.4% vs 67.6%; interaction `P = .29`.
- **Population/contrast/model/match key:** adjusted mHealth main effect; `outcome-softbedding-mhealth-main`.
- **Pass-1 checks:** estimate is in ordered CI; adjusted-risk difference is 11.8 points; sign and abstract/narrative/table repetitions agree. Interaction P remains separate.
- **PASS_1_COMPLETE:** no provisional candidate.

### S014 — Pacifier: NQI main effect

- **Printed evidence/location:** DOC-001 PDF p. 7: aRD 6.8% (1.4% to 11.9%), `P = .07`; adjusted risks 66.6% vs 59.8%.
- **Population/contrast/model/match key:** adjusted NQI main effect; `table3-nqi-pacifier`.
- **Pass-1 checks:** estimate is in ordered CI; adjusted-risk difference is 6.8 points and sign is coherent. CI excludes zero while the reported Hochberg-adjusted P is .07; this is not an independent contradiction because the package explicitly gives different CI-transform and multiplicity-adjustment layers but no rule tying the two.
- **PASS_1_COMPLETE:** no provisional candidate; missing definition is the exact CI/P joint inferential rule.

### S015 — Pacifier: mHealth main effect

- **Printed evidence/location:** DOC-001 PDF pp. 1, 6--7: aRD 8.7% (3.9% to 13.1%), `P < .001`; adjusted risks 68.5% vs 59.8%; interaction `P = .54`.
- **Population/contrast/model/match key:** adjusted mHealth main effect; `outcome-pacifier-mhealth-main`.
- **Pass-1 checks:** estimate is in ordered CI; adjusted-risk difference is 8.7 points; sign and repeated abstract/narrative/table locations agree. Interaction P is distinct.
- **PASS_1_COMPLETE:** no provisional candidate.

### S016 — Imputation sensitivity narrative

- **Printed evidence/location:** DOC-001 PDF p. 7: imputation analysis says the supine NQI-by-mHealth interaction was not significant and mHealth effects attenuated but consistent.
- **Population/contrast/model/match key:** post hoc imputation sensitivity analysis; `posthoc-imputation-supine`.
- **Pass-1 checks:** DOC-003 PDF p. 7 gives interaction `p = 0.05`, while p. 8 identifies Hochberg-adjusted logistic P values. “Not significant” is not mechanically contradictory: the final interaction decision threshold, unrounded adjusted P, and whether the multiplicity rule applies to interaction tests are not supplied. Main-versus-imputation mHealth estimates retain positive direction but are not uniformly smaller: supine is 9.0% versus 8.9%; the exact referenced interaction-model contrast is not printed in the supplement.
- **PASS_1_COMPLETE:** no provisional candidate; missing definitions recorded.

### S017 — Race-stratified post hoc narrative

- **Printed evidence/location:** DOC-001 PDF pp. 7--8: beneficial-outcome rates for group 4 were similarly high regardless of race; disparities were no longer significant.
- **Population/contrast/model/match key:** exploratory race analysis; `posthoc-race`.
- **Pass-1 checks:** DOC-003 PDF pp. 9--11 provides unadjusted stratum frequencies but no effect estimate, test, P value, variance, or multiplicity definition. The qualitative statement cannot be mechanically tested for statistical significance. The age-threshold label discrepancy is separately recorded under S1012.
- **PASS_1_COMPLETE:** no provisional candidate; missing inferential definitions recorded.

## DOC-002 protocol and DOC-003 results supplement

### S1001 — Cluster/factorial primary-model definition

- **Printed evidence/location:** DOC-002 PDF p. 13: 2×2 factorial hospital randomization; GEE multiple logistic regression; NQI/mHealth/interaction indicators; baseline prevalence and infant age covariates, with possible individual/hospital confounders.
- **Population/contrast/model/match key:** mothers with 2--5-month outcome surveys; `GEE_logistic_primary_safe_sleep_outcomes`.
- **Pass-1 checks:** DOC-001 p. 3/p. 7 reports a compatible GEE logistic cluster-aware final analysis with expanded stated covariates. Protocol language permits confounders, so no direct model-label conflict is established. Final working correlation and variance details are missing.
- **PASS_1_COMPLETE:** no provisional candidate.

### S1002 — Outcomes and interaction branching rule

- **Printed evidence/location:** DOC-002 PDF p. 13: four binary outcomes; significant interaction invokes interaction model, otherwise main-effects model; combined-versus-individual contrasts derive from intervention/interaction parameters.
- **Population/contrast/model/match key:** four primary outcomes, 2--5-month follow-up; `protocol_primary_outcomes_interaction_rule`.
- **Pass-1 checks:** DOC-001 Table 3 labels interaction P values as multiplicative logistic-regression tests and presents a combined contrast for supine, the outcome with interaction `P = .01`; labels/direction are compatible. The protocol does not supply an exact interaction significance criterion for the final reported analysis.
- **PASS_1_COMPLETE:** no provisional candidate.

### S1003 — Protocol multiplicity/significance definition

- **Printed evidence/location:** DOC-002 PDF pp. 13--14: Bonferroni for four intervention tests, 2-tailed alpha .05, comparison-wise alpha .0125.
- **Population/contrast/model/match key:** planned inference; `protocol_bonferroni_4_outcomes_alpha_0.0125`.
- **Pass-1 checks:** DOC-001/DOC-003 state final Hochberg-adjusted P values. A planned Bonferroni procedure and a final Hochberg procedure are not the same inferential rule, so no equality or P/CI compatibility calculation is applicable; the package has no amendment record.
- **PASS_1_COMPLETE:** no provisional candidate; final rule-change documentation is unavailable.

### S1004 — Planned mediation/breastfeeding models

- **Printed evidence/location:** DOC-002 PDF p. 13: Baron-Kenny mediation, GEE linear/logistic models, and breastfeeding GEE logistic models.
- **Population/contrast/model/match key:** secondary planned analyses; `protocol_secondary_mediation_breastfeeding_GEE`.
- **Pass-1 checks:** no matched final estimate, CI, P value, or statistic is supplied in this package. Absence is not a reporting-consistency candidate.
- **PASS_1_COMPLETE:** no provisional candidate.

### S1005 — Simulated power relationship

- **Printed evidence/location:** DOC-002 PDF p. 14: baseline .50--.60, each intervention +10 points, both +20, ICC .002, Bonferroni alpha .0125, 96% power for either main effect and 80% for combined-versus-one.
- **Population/contrast/model/match key:** protocol projection; `protocol_power_1600_1280_ICC_0.002`.
- **Pass-1 checks:** its 1600 enrollment, 1280 analysis total, and 320/group arithmetic match DOC-001 planning. The 96% and 80% values concern different stated contrasts in the protocol; DOC-001’s 80% wording does not identify an identical contrast/simulation setting. No power-value contradiction is mechanically established.
- **PASS_1_COMPLETE:** no provisional candidate; exact cross-document power estimand mapping is missing.

### S1006 — eTable 2 respondent/nonrespondent chi-square tests

- **Printed evidence/location:** DOC-003 PDF pp. 3--4: chi-square P values .5206, .2039, and `<.0001` for demographic category blocks, with 1263 respondents and 337 nonrespondents.
- **Population/contrast/model/match key:** categorical respondent/nonrespondent comparison; `respondent_nonrespondent_chisquare_etab2`.
- **Pass-1 checks:** category counts total to their displayed respondent/nonrespondent/total denominators, and the matched main-article summary’s `<.001` bounds are compatible with `<.0001`. No statistic, degrees of freedom, correction, or exact test implementation is printed, so P values are not independently reconstructed. `<.0001` is an inequality, not display zero.
- **PASS_1_COMPLETE:** no provisional candidate.

### S1007 — Imputation model/adjustment definition

- **Printed evidence/location:** DOC-003 PDF p. 8: aR is adjusted risk; aRD derives from logistic-OR/CIs; P values are Hochberg-adjusted logistic values; interaction P is multiplicative; covariates and soft-bedding SAFE-rate exception listed.
- **Population/contrast/model/match key:** imputed age ≥60-day analysis; `imputation_aR_aRD_definitions`.
- **Pass-1 checks:** labels distinguish aR/aRD/OR, adjusted P values, and interaction tests. P/CI inversion is not available because P is multiplicity-adjusted and CI is a transformed logistic interval; model covariance and exact conversion rules are not supplied.
- **PASS_1_COMPLETE:** no provisional candidate.

### S1008 — Imputed supine effects

- **Printed evidence/location:** DOC-003 PDF p. 7: NQI aRD 2.8% (−3.7% to 7.9%), p=.38; mHealth 9.0% (4.2% to 12.6%), p=.003; interaction p=.05; aRC 78.8, aRNQI 81.6, aRmH 87.8.
- **Population/contrast/model/match key:** imputed age ≥60-day adjusted logistic model; `imputation_supine_adjusted_effects`.
- **Pass-1 checks:** both estimates lie in ordered CIs and equal aR intervention minus control (2.8; 9.0) to printed precision; signs and outcome direction agree. P/CI exact compatibility is not assessed beyond direction for the stated Hochberg/transform limitation.
- **PASS_1_COMPLETE:** no provisional candidate.

### S1009 — Imputed room-sharing effects

- **Printed evidence/location:** DOC-003 PDF p. 7: NQI aRD 3.9% (−1.1% to 8.4%), p=.38; mHealth 12.0% (8.1% to 15.3%), p<.001; interaction p=.55; aRC 69.7, aRNQI 73.6, aRmH 81.7.
- **Population/contrast/model/match key:** imputed age ≥60-day adjusted logistic model; `imputation_roomsharing_adjusted_effects`.
- **Pass-1 checks:** estimates are contained in ordered CIs and adjusted-risk differences reproduce 3.9 and 12.0 points; direction/labels are coherent. `<.001` is not display zero.
- **PASS_1_COMPLETE:** no provisional candidate.

### S1010 — Imputed soft-bedding effects

- **Printed evidence/location:** DOC-003 PDF p. 7: NQI aRD 3.4% (−2.6% to 8.9%), p=.38; mHealth 11.7% (6.9% to 15.8%), p<.001; interaction p=.50; aRC 67.4, aRNQI 70.8, aRmH 79.1.
- **Population/contrast/model/match key:** imputed age ≥60-day adjusted logistic model without SAFE soft-bedding rate; `imputation_softbedding_adjusted_effects`.
- **Pass-1 checks:** estimates are contained in ordered CIs; adjusted-risk subtractions reproduce 3.4 and 11.7 points; signs and covariate-exception label are coherent.
- **PASS_1_COMPLETE:** no provisional candidate.

### S1011 — Imputed pacifier effects

- **Printed evidence/location:** DOC-003 PDF pp. 7--8: NQI aRD 5.7% (−1.0% to 11.9%), p=.38; mHealth 6.8% (0.0% to 12.8%), p=.05; interaction p=.84; aRC 60.2, aRNQI 65.9, aRmH 67.0.
- **Population/contrast/model/match key:** imputed age ≥60-day adjusted logistic model; `imputation_pacifier_adjusted_effects`.
- **Pass-1 checks:** estimates are within ordered CIs and aR differences reproduce 5.7 and 6.8 points. The printed 0.0 lower endpoint is a rounded boundary, not a P-value display; no exact P/CI inversion is available under Hochberg/OR-to-aRD transformation.
- **PASS_1_COMPLETE:** no provisional candidate.

### S1012 — Race/ethnicity frequency display and figure/table labels

- **Printed evidence/location:** DOC-003 PDF pp. 9--10 eTable 5 lists control and combined-intervention frequency counts/percentages by stratum; p. 11 eFigure plots percentages and excludes Other. eTable title says infant age `≥60 days`; eFigure title says `>60 days`.
- **Population/contrast/model/match key:** post hoc unadjusted frequency display; `posthoc_race_ethnicity_control_vs_combined_safe_sleep`.
- **Pass-1 checks:** every eTable 5 result was checked as an unadjusted count/denominator/percentage relationship. One independently observable percentage discrepancy is emitted as `STAT1-CAND-001`; no test, effect estimate, or significance inference is supplied. The strict/inclusive age-label mismatch is emitted separately as `STAT1-CAND-002` because the table and its graphical display present the same stated analysis population with nonidentical boundary labels.
- **PASS_1_COMPLETE:** two provisional candidates emitted in `checkers/statistical_pass_1.md`.

## Pass-1 coverage summary

- **Assigned and completed S records:** 29 (S001--S017; S1001--S1012).
- **Provisional candidates:** 2 (`STAT1-CAND-001`, `STAT1-CAND-002`); neither is a stable candidate ID or disposition.
- **Display-zero records:** 0. No `P = 0`, `p = 0.000`, or equivalent was printed in the assigned S evidence. Inequality displays such as `P < .001` and `<.0001` are not display zeros.
- **Diagnostic calculations:** only count/denominator percentage arithmetic is used; no diagnostic P-value reconstruction was performed.

## Pass-2 completion index

Independent pass 2 was performed by fresh runtime `/root/statistical_pass_2` (`gpt-5.6-terra`, high effort). The complete relationship-level rechecks are in `checkers/statistical_pass_2.md`. This index makes the second-pass status explicit for every canonical relationship; it is a coverage label, not an adjudication.

| S ID | Pass-2 status | S ID | Pass-2 status | S ID | Pass-2 status |
|---|---|---|---|---|---|
| S001 | PASS_2_COMPLETE | S002 | PASS_2_COMPLETE | S003 | PASS_2_COMPLETE |
| S004 | PASS_2_COMPLETE | S005 | PASS_2_COMPLETE | S006 | PASS_2_COMPLETE |
| S007 | PASS_2_COMPLETE | S008 | PASS_2_COMPLETE | S009 | PASS_2_COMPLETE |
| S010 | PASS_2_COMPLETE | S011 | PASS_2_COMPLETE | S012 | PASS_2_COMPLETE |
| S013 | PASS_2_COMPLETE | S014 | PASS_2_COMPLETE | S015 | PASS_2_COMPLETE |
| S016 | PASS_2_COMPLETE | S017 | PASS_2_COMPLETE | S1001 | PASS_2_COMPLETE |
| S1002 | PASS_2_COMPLETE | S1003 | PASS_2_COMPLETE | S1004 | PASS_2_COMPLETE |
| S1005 | PASS_2_COMPLETE | S1006 | PASS_2_COMPLETE | S1007 | PASS_2_COMPLETE |
| S1008 | PASS_2_COMPLETE | S1009 | PASS_2_COMPLETE | S1010 | PASS_2_COMPLETE |
| S1011 | PASS_2_COMPLETE | S1012 | PASS_2_COMPLETE |  |  |

Pass 2 registered zero genuinely new candidates and zero display-zero P-value records. Stable candidates remain C001; C002; C003; C004; C005.
