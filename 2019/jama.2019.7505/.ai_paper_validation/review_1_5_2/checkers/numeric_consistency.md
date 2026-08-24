# Numeric Consistency Review

## Scope and method

This checker reviewed every canonical numeric/reporting relationship N001--N055 in `relationships/numeric_relationship_inventory.md`, using the current-run main and support evidence mappings and the fresh native/layout text in `preprocessing/`. It applied, where the displayed relationship permitted it, count/percentage/denominator reconciliation; mutually exclusive category and subgroup sums; flow arithmetic; displayed difference and rounding checks; missingness/population checks; measure, unit, label, scale, reference-group, and rate-versus-count checks; repeated-location comparison; and repeated-value checks. Printed values were treated as rounded where the display precision required it. No old audit derivative, web source, GPU, or unprovided data was used.

**Relationship coverage:** 55/55 complete.  
**Distinct provisional pre-ledger candidates:** 4.  
**Checked with no qualifying candidate:** 51 relationships.  
**Tolerance:** for a count percentage printed to one decimal, the accepted rounding interval is the exact count/denominator percentage rounded to nearest 0.1 percentage point (and analogous half-last-place tolerance for other rounded displays). Rounded group means were not required to reproduce a separately rounded difference exactly. A category total was required to reconcile only when the source identifies categories as mutually exclusive and jointly exhaustive with the same stated denominator.

## Candidate records for candidate registration

### PROV-N006-01 — Intraoperative adverse-event threshold definitions differ between the methods text and Table 3 footnotes

**Relationship:** N006.

**Category:** Measure, label, or scale inconsistency.

**Exact source locations and printed inputs:** In the main article methods, intraoperative hypoxemia is printed as `SpO2 ≤92% for more than 1 minute` and hypotension as `systolic blood pressure <90 mm Hg for more than 2 minutes` ([DOC-001 PDF p. 3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3)). In Table 3 footnotes, hypoxemia is printed as `SpO2 of 92% or less; or any decline in SpO2 greater than 5% if SpO2 was previously less than 92%`, and hypotension as `systolic blood pressure less than 90 mm Hg or any decrease ... greater than 10 mm Hg if systolic blood pressure was previously less than 90 mm Hg` ([DOC-001 PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10)).

**Direct observation:** The p. 10 definitions add baseline-dependent alternative criteria that are absent from the p. 3 definitions; the p. 3 definitions additionally specify durations that are absent from the p. 10 footnotes.

**Reproducible rule and calculation:** For the same named intraoperative adverse-event outcome, the operational threshold should identify the same qualifying event or explicitly state which definition supersedes the other. This is a logical identity check, not a statistical reconstruction: `{SpO2 ≤92% for >1 min}` is not textually identical to `{SpO2 ≤92% OR >5% decline when prior SpO2 <92%}`, and the analogous blood-pressure sets differ. No numeric tolerance applies to distinct decision thresholds.

**Alternative source-grounded interpretation:** The p. 3 prose may be abbreviated while the Table 3 footnotes are the intended complete adjudication criteria; alternatively, the footnotes may describe a rescue/measurement convention rather than the outcome definition. The supplied article does not state that either text supersedes the other.

**Quality-control relevance:** Different threshold rules can change the numerator for the printed intraoperative hypoxemia and hypotension outcomes and can change what a data extractor understands those reported proportions to represent.

**Exact human question:** Which threshold set governed the reported Table 3 intraoperative hypoxemia and hypotension counts, and should the other location be amended or explicitly described as an abbreviated definition?

### PROV-N015-01 — Printed white-blood-cell unit and displayed magnitude do not use a coherent scale

**Relationship:** N015.

**Category:** Measure, label, or scale inconsistency.

**Exact source locations and printed inputs:** Table 1 prints `White blood cells, × 10^9/L` with mean (SD) `8224 (2346)` in the high-PEEP group and `8347 (2758)` in the low-PEEP group ([DOC-001 PDF p. 6](../../../jama_bluth_2019_oi_190055_16092.pdf#page=6)). The supplied supplement defines leukocytosis/leukopenia using `white blood cell count <4000 cells/mm3 or >12000 cells/mm3` ([DOC-005 PDF p. 20](../../../joi190055supp4_prod_16092.pdf#page=20)).

**Direct observation:** The Table 1 label pairs values in the thousands with `×10^9/L`.

**Reproducible rule and calculation:** A value of `8224 ×10^9/L` equals `8,224,000 cells/mm3`, because 1 L equals 1,000,000 mm3; the corresponding low-group value is `8,347,000 cells/mm3`. Those values are about 685.3 and 695.6 times the supplied 12,000 cells/mm3 leukocytosis threshold, respectively. Conversely, `8224 cells/mm3 = 8.224 ×10^9/L` and `8347 cells/mm3 = 8.347 ×10^9/L`. This is a unit/scale identity check; rounding tolerance cannot bridge a factor of 1,000.

**Alternative source-grounded interpretation:** The table may have intended `cells/mm3` (or an equivalent per-microlitre unit) for the displayed values, or it may have intended values approximately `8.224` and `8.347` under the printed `×10^9/L` unit. The sources do not identify which printed element is in error.

**Quality-control relevance:** A factor-of-1,000 unit/scale mismatch can cause a baseline laboratory value to be copied or interpreted on the wrong scale.

**Exact human question:** Should the Table 1 unit be changed to cells/mm3 (or equivalent), or should the displayed numeric values be rescaled to match `×10^9/L`?

### PROV-N048-01 — Per-protocol eTable 8 effect-estimate column is unlabeled and its values do not reproduce as crude ratios from the displayed counts

**Relationship:** N048.

**Category:** Measure, label, or scale inconsistency.

**Exact source locations and printed inputs:** eTable 8 labels its third numeric column only `Effect Estimate 95% CI`, while printing, for example, primary PPC `186/917 (20.3)` versus `209/912 (22.9)`, `0.92 (0.82–1.04)`; pleural effusion `38/917 (4.1)` versus `18/912 (2.0)`, `1.37 (1.14–1.65)`; and cardiopulmonary edema `15/917 (1.6)` versus `7/912 (0.8)`, `1.36 (1.02–1.82)` ([DOC-005 PDF p. 29](../../../joi190055supp4_prod_16092.pdf#page=29)). The main article labels its analogous column `Risk Ratio` and says its risk ratios and CIs use the Wald likelihood-ratio approximation ([DOC-001 PDF pp. 9-10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), [p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10)).

**Direct observation:** eTable 8 does not name the estimand, model, adjustment, or reference direction for its printed effect estimates.

**Reproducible rule and calculation:** If the eTable 8 values were unadjusted high-PEEP/low-PEEP risk ratios from their own displayed counts, the diagnostic calculations are: primary PPC `(186/917)/(209/912) = 0.885100` (not `0.92`); pleural effusion `(38/917)/(18/912) = 2.099600` (not `1.37`); and cardiopulmonary edema `(15/917)/(7/912) = 2.131173` (not `1.36`). If they were crude odds ratios, the corresponding values are `0.855864`, `2.147137`, and `2.149984`, also not the printed estimates. The exact numerator and denominator pairs remove rounding ambiguity. This does not establish an arithmetic error in an adjusted model; it establishes that the printed generic label lacks the definition required to reconcile the displayed inputs.

**Alternative source-grounded interpretation:** The estimates may be adjusted/model-based per-protocol effects, may use a different estimand or transformation, or may have been carried from an analysis with further covariates. The supplied eTable neither says this nor supplies the model inputs.

**Quality-control relevance:** An unlabeled non-crude effect column can be misextracted as a risk ratio, odds ratio, or simple proportion ratio and can be assigned the wrong meaning in evidence synthesis.

**Exact human question:** What exact effect measure, reference direction, model, and adjustment set generated every eTable 8 estimate, and should that information be printed in the table or its footnotes?

### PROV-N054-01 — eFigure 11 death figure caption calls the reported rate postoperative extra-pulmonary complications

**Relationship:** N054.

**Category:** Measure, label, or scale inconsistency.

**Exact source locations and printed inputs:** The supplement contents and eFigure 11 title say `Probability of death in the first 5 postoperative days` ([DOC-005 PDF pp. 1, 41](../../../joi190055supp4_prod_16092.pdf#page=1), [p. 41](../../../joi190055supp4_prod_16092.pdf#page=41)). Its caption instead says `the rate of postoperative extra-pulmonary complications ... was 0.5% ... and 0.3%`, followed by `hazard ratio for 5-day mortality, 1.67; 95% confidence interval 0.40 to 6.97; P=0.484` ([DOC-005 PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41)). The main article reports mortality at 5 days `5 (0.5%)` versus `3 (0.3%)`, `HR, 1.67 (0.40 to 6.97)`, `P=.48` ([DOC-001 PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10)).

**Direct observation:** Within eFigure 11, the outcome in the figure title and HR label is death/5-day mortality, while the rate sentence names postoperative extra-pulmonary complications. The numerical rate and HR match the main article's 5-day mortality result.

**Reproducible rule and calculation:** A caption's named outcome should agree with its figure title and the outcome named for its effect estimate. Direct text comparison yields `death / 5-day mortality` versus `postoperative extra-pulmonary complications`; this is a label-identity conflict, so no numerical tolerance applies.

**Alternative source-grounded interpretation:** `postoperative extra-pulmonary complications` may be a residual phrase copied from eFigure 10; the numerical mortality values may be correct. The source does not explicitly correct the caption.

**Quality-control relevance:** The conflicting label can cause the mortality time-to-event result to be extracted as an extra-pulmonary-complication result or vice versa.

**Exact human question:** Should eFigure 11's rate sentence name 5-day mortality rather than postoperative extra-pulmonary complications, and are the plotted curve and all caption values intended to be the mortality analysis?

## Explicit checked-no-candidate coverage

| Relationship | Applied source-grounded checks | Result |
|---|---|---|
| N001 | population totals, cross-location demographics, unit/date/site labels | CHECKED_NO_CANDIDATE |
| N002 | assigned-intervention values, units, repeated methods locations | CHECKED_NO_CANDIDATE |
| N003 | randomization-to-analysis flow arithmetic and per-protocol exclusions | CHECKED_NO_CANDIDATE |
| N004 | narrative flow totals: 2013−29=1984; 1984−8=1976; 989+987=1976 | CHECKED_NO_CANDIDATE |
| N005 | outcome count, time-window, and label inventory | CHECKED_NO_CANDIDATE |
| N007 | baseline count/percentage rounding and mutually exclusive sex/BMI totals | CHECKED_NO_CANDIDATE |
| N008 | waist/hip and ARISCAT subgroup sums, denominators, rounding | CHECKED_NO_CANDIDATE |
| N009 | oxygenation-category sums and count/percentage rounding | CHECKED_NO_CANDIDATE |
| N010 | incision, duration, ASA category totals and rounding | CHECKED_NO_CANDIDATE |
| N011 | baseline denominators, diabetes-treatment subgroups, rounding | CHECKED_NO_CANDIDATE |
| N012 | tobacco-category sums, COPD treatment denominators, rounding | CHECKED_NO_CANDIDATE |
| N013 | cardiac-history and NYHA displayed subgroup denominators/rounding | CHECKED_NO_CANDIDATE |
| N014 | medication/vital-sign units, percentages, denominators | CHECKED_NO_CANDIDATE |
| N016 | surgery-type sums, abdominal/nonabdominal labels and available denominators | CHECKED_NO_CANDIDATE |
| N017 | mean PEEP/recruitment repeated-location values and percentage rounding | CHECKED_NO_CANDIDATE |
| N018 | timepoint means, displayed differences, units, and rounding tolerance | CHECKED_NO_CANDIDATE |
| N019 | recruitment/peak-pressure counts, labels, differences, extraction alignment limitation | CHECKED_NO_CANDIDATE |
| N020 | driving-pressure identity, respiratory-rate differences and signs | CHECKED_NO_CANDIDATE |
| N021 | FiO2/SpO2 units, timepoint differences and signs | CHECKED_NO_CANDIDATE |
| N022 | CO2/heart-rate/MAP units, differences and rounding tolerance | CHECKED_NO_CANDIDATE |
| N023 | head-elevation and NIV category totals/percentages | CHECKED_NO_CANDIDATE |
| N024 | anesthesia/epidural totals, subgroup denominators, differences | CHECKED_NO_CANDIDATE |
| N025 | blockade/monitoring/reversal denominators and differences | CHECKED_NO_CANDIDATE |
| N026 | fluid amount/use labels, units, medians, differences | CHECKED_NO_CANDIDATE |
| N027 | blood-product counts/percentages, amount units, duration displays | CHECKED_NO_CANDIDATE |
| N028 | primary-PPC count/percentage/difference, RR label, repeated locations | CHECKED_NO_CANDIDATE |
| N029 | component count/percentage rounding and composite-versus-component interpretation | CHECKED_NO_CANDIDATE |
| N030 | absolute-difference signs, intervals, narrative/table matching, rounding | CHECKED_NO_CANDIDATE |
| N031 | secondary-outcome counts/percentages and nonexclusive-component interpretation | CHECKED_NO_CANDIDATE |
| N032 | GI/AKI severity subgroup sums and stated denominators | CHECKED_NO_CANDIDATE |
| N033 | hospital-free-day units and adverse-event count/percentage rounding | CHECKED_NO_CANDIDATE |
| N034 | rescue/vasoactive/mortality count, risk-versus-HR labels and repeated values | CHECKED_NO_CANDIDATE |
| N035 | subgroup counts/denominators, risk-ratio direction, nonexhaustive/missing subgroup values | CHECKED_NO_CANDIDATE |
| N036 | remaining subgroup denominators, overall repeated primary result, RR direction | CHECKED_NO_CANDIDATE |
| N037 | narrative direction versus displayed outcome counts and analysis labels | CHECKED_NO_CANDIDATE |
| N038 | planned-enrollment chronology, dropout arithmetic, historical-versus-observed labels | CHECKED_NO_CANDIDATE |
| N039 | eligibility/ARISCAT thresholds and protocol-to-published definition matching | CHECKED_NO_CANDIDATE |
| N040 | ventilation/rescue units, steps, intervention labels, protocol/published matching | CHECKED_NO_CANDIDATE |
| N041 | endpoint-component counts, threshold labels, planned-versus-observed distinction | CHECKED_NO_CANDIDATE |
| N042 | mITT/complete-case population definitions and reported flow compatibility | CHECKED_NO_CANDIDATE |
| N043 | fluid count/percentage rounding, amounts/units, nonexclusive subtype sums | CHECKED_NO_CANDIDATE |
| N044 | vasoactive count/percentage rounding, dose unit labels, nonexclusive drug use | CHECKED_NO_CANDIDATE |
| N045 | agent count/percentage rounding and nonexclusive medication-category interpretation | CHECKED_NO_CANDIDATE |
| N046 | priority/position/wound subgroup totals, missingness-compatible denominators, pressure unit | CHECKED_NO_CANDIDATE |
| N047 | daily observed denominators, VAS unit, attrition/missingness pattern, repeated values | CHECKED_NO_CANDIDATE |
| N049 | sensitivity-result model labels, estimate/CI/P-value pairing and population label | CHECKED_NO_CANDIDATE |
| N050 | figure-series definitions, unit/scale labels, unavailable plotted-value limitation | CHECKED_NO_CANDIDATE |
| N051 | time-to-PPC rate/HR/CI/P-value labels and main-result matching | CHECKED_NO_CANDIDATE |
| N052 | time-to-severe-PPC rate/HR/CI/P-value labels and main-result matching | CHECKED_NO_CANDIDATE |
| N053 | time-to-PEPC rate/HR/CI/P-value labels and main-result matching | CHECKED_NO_CANDIDATE |
| N055 | availability-statement quantities and absence of supplied structured outcome data | CHECKED_NO_CANDIDATE |

## Limitations

The fresh text extraction on DOC-001 p. 7 (Table 2) and p. 9 (Table 3) serializes some columns out of visual row alignment; calculations were limited to values whose row identity was recoverable in fresh text or corroborated by a same-source narrative/footnote. Direct page rendering/OCR tools were unavailable in this environment (`pdftoppm` and `pdfinfo` were not installed), so no unverified visual reassignment was made. DOC-005 eFigures 1-7 and 12 contain plot values unavailable as printed native/layout text; their captions and labels were checked, but unreadable coordinates were not reconstructed. These limitations do not affect the four candidate records above.
