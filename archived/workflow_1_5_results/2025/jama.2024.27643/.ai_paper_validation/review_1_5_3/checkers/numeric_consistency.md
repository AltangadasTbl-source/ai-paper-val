# Numeric Consistency Review

## Scope, method, and output status

This review independently applied arithmetic, total, subgroup-sum, numerator/denominator, percentage, missingness, population, rounding, measure/label/scale, unit, reference-group, rate/risk/proportion/person-time/count, repeated-value, and concrete analysis-unit checks to all 56 relationships in `relationships/numeric_relationship_inventory.md`. Sources were the supplied PDFs, with direct PDF pages authoritative and current extraction maps used as locators. No web material and no legacy candidate, checker, verification, disposition, or report conclusion was used.

The review emitted **5 distinct raw candidates**. They are intentionally not assigned stable `C` identifiers, severity, validity, disposition, or any adjudication. Each remains a pending question for human adjudication. A distinct candidate is emitted only where the printed inputs, comparator, and reproducible rule establish a concrete mismatch. The following records use descriptive numeric-check labels only.

## Completed checks without a candidate

- Participant-flow equations reconcile where the flow branches state a common population: 163 - 1 - 1 = 161; dose arms 59 + 61 + 41 = 161; shared placebo 41 + 123 = 164; and completion counts reconcile with displayed discontinuations.
- Table 1 sex, El Escorial, and King's-stage category sums reconcile. Ethnicity 157/163 is 96.3%, and the one missing record matches its footnote.
- Table 2 event numerators/denominators produce all printed percentages within one-decimal rounding. The 162 shared-placebo time-to-event denominator is explicitly explained by two no-follow-up exclusions.
- eTable 3A/3B displayed active-minus-placebo differences reproduce from displayed estimates within rounding. eTable 5 pooled participant counts reproduce the two dose-arm counts and its event counts are not incorrectly treated as participant totals.
- Protocol/SAP values were distinguished from actual results. Planned 160-person/3:1 designs, product dose-volume arithmetic, SVC/ALSFRS-R scale definitions, and repeated safety-margin calculations reconcile.
- Reversed sensitivity-analysis contrasts between the article and eFigure reconcile after reversing the contrast and allowing displayed rounding. The apparent P=.05/P=.051 variation is compatible with that display precision.
- No candidate was created solely from a finite-precision displayed P value. **DISPLAY_ZERO_NOT_CANDIDATE:** no P=0 or equivalent display-zero-only inconsistency was found in this numeric lane.

## Raw candidate 1 — Shared-placebo race denominator is incompatible with the stated missing-race count

**Stable relationship:** N007.

**Exact source locations:** [DOC-001, PDF p. 6, Table 1 and footnote b](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=6>).

**Printed inputs:** The shared-placebo header is `n = 164`. Its race rows are Asian `2/160 (1.2)`, Black or African American `6/160 (3.8)`, White `151/160 (94.4)`, and multiple races `1/160 (0.6)`. Footnote b says, “Race was unknown or unreported for 3 participants.”

**Direct observation:** The displayed race numerator sum is 2 + 6 + 151 + 1 = 160, and each race percentage uses 160 as its denominator. The header for that same column is 164.

**Reproducible rule and calculation:** For a column with 164 participants, a complete set of 160 race-classified participants leaves 164 - 160 = **4** without a race classification. The stated footnote instead identifies **3** participants as race unknown/unreported. The discrepancy is 4 - 3 = **1 participant**.

**Tolerance:** Zero participants. This is integer missingness accounting, not a rounded percentage; no rounding tolerance applies.

**Inference separated from observation:** The direct mismatch is the one-person difference between the table's implied missing-race count and its footnote. It may reflect an unlisted race status, an incorrect denominator, or a footnote/row transcription issue; the source does not say which.

**Alternative source-grounded interpretations:** The footnote could be intended to cover a different subset than the displayed shared-placebo column, or one participant may have a status not meant to be counted as unknown/unreported. Neither qualification is printed in the table.

**Quality-control relevance:** A baseline category denominator and missing-data count can be copied into evidence extraction and population-characterization tables.

**Exact human question:** Does the shared-placebo race display have four unclassified participants (requiring correction/clarification of footnote b), or is one of the printed race denominators/numerators not intended to be 160?

## Raw candidate 2 — SVC change is labelled per month in the article but as a 24-week change estimate in eTable 3A

**Stable relationship:** N012.

**Exact source locations:** [DOC-001, PDF p. 4, Secondary Efficacy Outcomes](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [DOC-004, PDF p. 16, eTable 3A](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=16>).

**Printed inputs:** The article calls the “mean change in SVC over 24 weeks” `−9.32 PPN per month` for pooled CNM-Au8 and `−8.53 PPN per month` for shared placebo, with difference `−0.78 PPN/month`. eTable 3A has the heading `24-week Change Estimate` and lists SVC (% predicted) as `−9.32 (1.36)`, `−8.53 (1.15)`, and difference `−0.78 (1.77)`.

**Direct observation:** The same numerical values and shared-placebo/pool contrast occur in both locations, but their unit/scale labels differ: per month in the article versus 24-week change estimate in the eTable.

**Reproducible rule and calculation:** If `−9.32` were a monthly change sustained across 24 weeks (approximately 24/4.345 = 5.52 months), its implied 24-week change would be about −9.32 × 5.52 = **−51.4 PPN**, not the eTable's printed `−9.32` 24-week change estimate. Conversely, a `−9.32` 24-week change corresponds to approximately −9.32 / 5.52 = **−1.69 PPN/month**, not `−9.32 PPN/month`.

**Tolerance:** Unit identity must match exactly. The gap is a factor of approximately 5.5, far beyond rounding.

**Inference separated from observation:** The conflicting labels are directly printed. The calculation is a diagnostic showing why a time-unit difference cannot be ordinary rounding. It does not establish which label is intended.

**Alternative source-grounded interpretations:** The article may use “per month” as an editorial label while intending the eTable's 24-week model-based change, or eTable 3A's heading may omit a monthly-rate convention. The article explicitly says “over 24 weeks,” while the table expressly labels its displayed column “24-week Change Estimate”; the supplied sources do not resolve the intended unit.

**Quality-control relevance:** A monthly rate and a 24-week cumulative change are different effect scales and could be extracted as incompatible outcomes.

**Exact human question:** For the displayed SVC estimates `−9.32`, `−8.53`, and `−0.78`, should the published unit be PPN per month or 24-week change in percent-predicted SVC, and which location needs correction or clarification?

## Raw candidate 3 — Article mortality event rates disagree with eTable 2 for the same Bayesian model

**Stable relationship:** N016.

**Exact source locations:** [DOC-001, PDF p. 4, Primary Efficacy Outcome](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [DOC-004, PDF p. 15, eTable 2](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=15>).

**Printed inputs:** Article: “The bayesian shared parameter model estimated that the mortality event rate was `0.007 events per month` for the shared placebo group and `0.006 events per month` for the combined CNM-Au8 dosage groups,” citing eTable 2. eTable 2, headed “Primary Efficacy Analysis of Function and Mortality with Bayesian Shared Parameter Model,” prints median and mean `0.010` events/month for shared placebo and `0.009` events/month for pooled CNM-Au8.

**Direct observation:** Both locations identify the Bayesian shared-parameter model, same groups, same outcome label, and events-per-month unit, but print different values.

**Reproducible rule and calculation:** Shared placebo: 0.010 - 0.007 = **0.003 events/month**. Pooled CNM-Au8: 0.009 - 0.006 = **0.003 events/month**.

**Tolerance:** Both locations print to three decimals, so a standard display rounding interval is ±0.0005. The 0.003 differences are six times the combined endpoint half-unit distance (0.001) and cannot be one common three-decimal rounding of one value.

**Inference separated from observation:** Directly observed are the matched model/group/unit labels and the two incompatible value pairs. It is an inference that one is a reporting/transcription/version mismatch; the sources do not identify the production history.

**Alternative source-grounded interpretations:** One location could represent an unstated alternate posterior summary, analysis run, time scale, or version. eTable 2 explicitly gives both median and mean, each displayed as 0.010/0.009, and the article provides no alternate qualifier.

**Quality-control relevance:** Model-estimated event rates are quantitative outcome summaries that may be extracted as absolute mortality parameters.

**Exact human question:** Are the article's 0.007/0.006 events-per-month values based on a distinct stated analysis, or should they agree with eTable 2's 0.010/0.009 values for the cited Bayesian shared-parameter model?

## Raw candidate 4 — Plasma NfL confidence-interval upper endpoint differs within the article

**Stable relationship:** N018.

**Exact source location:** [DOC-001, PDF p. 8, Figure 3 and Biomarker Analyses text](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>).

**Printed inputs:** Figure 3 prints plasma NfL Week-24 least-squares mean difference `−9.5% (95% CI, −17.8% to −0.5%); P=.04`. The narrative immediately below prints the same treatment difference `−9.5%` and P=.04, but `95% CI, −17.8 to −0.4%`.

**Direct observation:** The result identity, contrast, point estimate, lower endpoint, and P value match, while the CI upper endpoint differs by 0.1 percentage point.

**Reproducible rule and calculation:** (−0.4) - (−0.5) = **0.1 percentage point**. Both endpoints are printed to one decimal.

**Tolerance:** ±0.05 percentage point for one-decimal rounding. A single underlying value cannot round to both −0.4 and −0.5 under ordinary nearest-one-decimal rounding because their rounding intervals do not overlap.

**Inference separated from observation:** The endpoint mismatch is directly observed. A transcription, post-layout update, or different unprinted computation would be an inference, not established by the source.

**Alternative source-grounded interpretations:** One location could use a differently rounded internal endpoint or a nonstandard rounding convention, but no such convention or alternate analysis label is supplied.

**Quality-control relevance:** A confidence-interval endpoint affects extraction of precision and statistical compatibility.

**Exact human question:** Which upper CI endpoint, −0.5% or −0.4%, is the intended value for the stated plasma NfL Week-24 treatment difference, and is there a documented alternate calculation behind either display?

## Raw candidate 5 — Serum NfL repeated results disagree between the article and regimen-only eTable

**Stable relationship:** N019.

**Exact source locations:** [DOC-001, PDF p. 8, Figure 3 and Biomarker Analyses text](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>); [DOC-004, PDF p. 17, eTable 3B](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=17>).

**Printed inputs:** The article identifies regimen placebo versus combined CNM-Au8 and prints serum NfL placebo `+30.8%`, active `+0.4%`, treatment difference `−23.2%` (95% CI `−39.5%` to `−2.5%`; P=.03). eTable 3B, identified as the ERO dataset using only Regimen C placebo participants, prints serum NfL active `+0.4%`, regimen placebo `+26.8%`, difference `−26.4%` (95% CI `−50.3%` to `−2.6%`; P=.03).

**Direct observation:** The active change, regimen-only placebo identity, endpoint, time frame, and P value match; placebo change, treatment difference, and both CI endpoints do not.

**Reproducible rule and calculation:** Article arithmetic is +0.4 - +30.8 = **−30.4%**, which does not equal its printed −23.2% (difference **7.2 percentage points**). eTable arithmetic is +0.4 - +26.8 = **−26.4%**, exactly its printed difference. Across locations, placebo change differs by 30.8 - 26.8 = **4.0 points** and treatment difference differs by (−23.2) - (−26.4) = **3.2 points**.

**Tolerance:** ±0.05 percentage point for one-decimal displays. The observed 3.2-7.2 point discrepancies exceed rounding tolerance.

**Inference separated from observation:** The mismatched printed values and the article's displayed arithmetic nonreconciliation are direct. It is not established whether the article intended a different geometric-mean contrast, analysis set, covariate adjustment, or a typographic value; the source does not supply an alternate label that would explain the mismatch.

**Alternative source-grounded interpretations:** eTable 3B explicitly labels ERO/regimen-only placebo. The article also says “regimen placebo group,” but it may summarize another unstated model output. Because the article's own active and placebo changes do not reproduce its reported difference, an unstated population alone does not explain every mismatch.

**Quality-control relevance:** Biomarker percentage changes and their contrast/interval are likely to be copied into evidence syntheses; mismatched values can alter the extracted effect estimate and precision.

**Exact human question:** For the regimen-placebo versus pooled-active serum NfL analysis, which placebo change, treatment difference, and CI are authoritative, and how should the article's +30.8%, −23.2% display be reconciled with eTable 3B's +26.8%, −26.4% result?

## Limitations

- This lane does not adjudicate the five candidates, determine their cause, or assign severity, validity, or a correction.
- Graph-only preclinical data lacked exact source tables; no value was read from a plot as though it were an exact printed number.
- Protocol and SAP design parameters were not equated to observed trial results without matching population, version, time, contrast, and model qualifiers.
- Statistical interval/test/P-value compatibility requiring unprinted model inputs remains for the dedicated statistical reviewers.
