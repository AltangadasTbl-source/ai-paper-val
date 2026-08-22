# Stable Candidate Ledger

All candidates are **Pending Human Adjudication**. These are source-grounded quality-control candidates, not severity assignments, validity determinations, exclusions, or corrections. Genuine duplicates were merged before stable IDs; similar issues involving different printed values remain separate.

## C001 — Protocol matching direction conflicts with the final matched cohort

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** NUM-P001; CROSS-P001
- **Relationship IDs:** N001
- **Exact source locations:** [main article PDF p. 1](../../jama_aminian_2019_oi_190103.pdf#page=1), [main article PDF p. 3](../../jama_aminian_2019_oi_190103.pdf#page=3), [main article PDF p. 4](../../jama_aminian_2019_oi_190103.pdf#page=4), [protocol PDF p. 3](../../joi190103supp2_prod.pdf#page=3).
- **Source evidence:** The article reports 2,287 surgical patients matched to 11,435 nonsurgical controls and states five nonsurgical patients per surgical patient. The protocol says each nonsurgical patient will be matched to five surgical patients.
- **Rule/calculation:** `2,287 × 5 = 11,435`; the protocol sentence grammatically reverses the group roles.
- **Alternative source-grounded interpretation:** The protocol sentence may be a planned-method wording error or may use an intended ratio convention different from its sentence-level direction.
- **Human question:** What matching direction was implemented, and does the protocol sentence invert the surgical and nonsurgical roles?

## C002 — Heart-failure ARD does not reconcile with displayed 8-year incidences

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Checker provenance:** NUM-P002; cross-source review recorded the values as matched but treated a separately bootstrapped point estimate as an alternative.
- **Relationship IDs:** N009; S010
- **Exact source locations:** [main article PDF p. 4](../../jama_aminian_2019_oi_190103.pdf#page=4), [main article PDF p. 7](../../jama_aminian_2019_oi_190103.pdf#page=7), [Supplement 1 PDF p. 7](../../joi190103supp1_prod.pdf#page=7).
- **Source evidence:** Heart-failure 8-year incidence is 6.8% for surgery and 18.9% for controls; ARD is 12.9% (95% CI 10.4%-15.1%), labeled control minus surgery.
- **Rule/calculation:** `18.9 - 6.8 = 12.1`, not 12.9; 0.8 percentage-point discrepancy exceeds the 0.10-point tolerance from two one-decimal inputs.
- **Alternative source-grounded interpretation:** The table footnote says the 95% CIs use 1,000 bootstrap samples; the point estimate may also come from a separate bootstrap estimator, but that rule is not stated for the point estimate.
- **Human question:** What exact estimator produced 12.9%, and is it intended to equal the displayed cumulative-incidence difference?

## C003 — Coronary-disease ARD does not reconcile with displayed 8-year incidences

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Checker provenance:** NUM-P003; cross-source review retained the separate-estimator alternative.
- **Relationship IDs:** N010; S010
- **Exact source locations:** [main article PDF p. 4](../../jama_aminian_2019_oi_190103.pdf#page=4), [main article PDF p. 7](../../jama_aminian_2019_oi_190103.pdf#page=7), [Supplement 1 PDF p. 7](../../joi190103supp1_prod.pdf#page=7).
- **Source evidence:** Coronary-disease 8-year incidence is 7.9% for surgery and 11.6% for controls; ARD is 4.2% (1.9%-6.8%).
- **Rule/calculation:** `11.6 - 7.9 = 3.7`, not 4.2; discrepancy 0.5 percentage point.
- **Alternative source-grounded interpretation:** A separately bootstrapped or otherwise distinct ARD point estimator may have been used, although only the CI bootstrap procedure is expressly stated.
- **Human question:** Was 4.2% produced by a distinct point estimator, and where is that estimator defined?

## C004 — Cerebrovascular-disease ARD does not reconcile with displayed 8-year incidences

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Checker provenance:** NUM-P004; cross-source review retained the separate-estimator alternative.
- **Relationship IDs:** N011; S010
- **Exact source locations:** [main article PDF p. 4](../../jama_aminian_2019_oi_190103.pdf#page=4), [main article PDF p. 7](../../jama_aminian_2019_oi_190103.pdf#page=7), [Supplement 1 PDF p. 7](../../joi190103supp1_prod.pdf#page=7).
- **Source evidence:** Cerebrovascular-disease 8-year incidence is 4.1% for surgery and 5.6% for controls; ARD is 1.8% (95% CI -0.03% to 3.4%).
- **Rule/calculation:** `5.6 - 4.1 = 1.5`, not 1.8; discrepancy 0.3 percentage point.
- **Alternative source-grounded interpretation:** The ARD may use a separate point estimator not expressly defined by the footnote.
- **Human question:** Does the ARD use a distinct estimator, or should it reconcile to 1.5% at displayed precision?

## C005 — Nephropathy ARD does not reconcile with displayed 8-year incidences

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Checker provenance:** NUM-P005; cross-source review retained the separate-estimator alternative.
- **Relationship IDs:** N012; S010
- **Exact source locations:** [main article PDF p. 4](../../jama_aminian_2019_oi_190103.pdf#page=4), [main article PDF p. 7](../../jama_aminian_2019_oi_190103.pdf#page=7), [Supplement 1 PDF p. 7](../../joi190103supp1_prod.pdf#page=7).
- **Source evidence:** Nephropathy 8-year incidence is 6.1% for surgery and 16.3% for controls; ARD is 11.1% (8.8%-13.6%).
- **Rule/calculation:** `16.3 - 6.1 = 10.2`, not 11.1; discrepancy 0.9 percentage point.
- **Alternative source-grounded interpretation:** The ARD may be a separately estimated quantity, but the table does not state a distinct point-estimate rule.
- **Human question:** What point-estimation procedure produced 11.1%, and how does it relate to the two displayed cumulative incidences?

## C006 — Atrial-fibrillation ARD does not reconcile with displayed 8-year incidences

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Checker provenance:** NUM-P006; cross-source review retained the separate-estimator alternative.
- **Relationship IDs:** N013; S010
- **Exact source locations:** [main article PDF p. 4](../../jama_aminian_2019_oi_190103.pdf#page=4), [main article PDF p. 7](../../jama_aminian_2019_oi_190103.pdf#page=7), [Supplement 1 PDF p. 7](../../joi190103supp1_prod.pdf#page=7).
- **Source evidence:** Atrial-fibrillation 8-year incidence is 7.9% for surgery and 13.6% for controls; ARD is 6.5% (4.4%-8.7%).
- **Rule/calculation:** `13.6 - 7.9 = 5.7`, not 6.5; discrepancy 0.8 percentage point.
- **Alternative source-grounded interpretation:** The ARD may be separately estimated; only bootstrap CI generation is explicitly described.
- **Human question:** Is 6.5% a separately estimated ARD, and where is that definition stated?

## C007 — Supplement tables use different nonsurgical medication denominators at baseline

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Checker provenance:** NUM-P007; cross-source review treated the tables as potentially different analysis sets.
- **Relationship IDs:** N029
- **Exact source locations:** [Supplement 1 PDF p. 5](../../joi190103supp1_prod.pdf#page=5), [Supplement 1 PDF p. 14](../../joi190103supp1_prod.pdf#page=14).
- **Source evidence:** eTable 3 labels matched nonsurgical baseline medication data `N=11435`; eTable 10 labels the nonsurgical medication-proportion sample at time 0 as `11433`. Both surgery values are 2,287.
- **Rule/calculation:** `11,435 - 11,433 = 2`; no printed missingness, timing, or inclusion rule reconciles the two baseline/index-date labels.
- **Alternative source-grounded interpretation:** eTable 10 may use a complete-case medication denominator that excludes two controls, while eTable 3 may classify all matched controls.
- **Human question:** What rule excludes two nonsurgical controls from the eTable 10 year-0 denominator?

## C008 — Medication comparison is labeled as two different named tests

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** CROSS-P002; statistical pass 1 recorded the possible interpretation that “two-sample proportions test” is a generic description encompassing Fisher exact testing.
- **Relationship IDs:** S013; S025
- **Exact source locations:** [main article PDF p. 4](../../jama_aminian_2019_oi_190103.pdf#page=4), [main article PDF p. 10](../../jama_aminian_2019_oi_190103.pdf#page=10), [Supplement 1 PDF p. 12](../../joi190103supp1_prod.pdf#page=12).
- **Source evidence:** Methods and eTable 8 say a two-sample proportions test was used for medication data; Figure 5 says its matched 8-year P values came from Fisher exact tests. The same six 8-year result-family P values appear, including insulin P=.008 and five P<.001 values.
- **Rule/calculation:** Matched outcome/time/population P values should carry the procedure that generated them; Fisher exact and the usual large-sample two-sample proportions test are distinct named procedures.
- **Alternative source-grounded interpretation:** “Two-sample proportions test” may have been intended as a generic family description, or Fisher exact may have been used only at year 8.
- **Human question:** Which procedure generated each 8-year medication P value, and which source label should govern?

## C009 — Time-varying-HR narrative cites eTable 4 while the displayed table is eTable 7

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** NUM-P008; CROSS-P003; STAT1-P001
- **Relationship IDs:** N038; S024
- **Exact source locations:** [Supplement 1 PDF p. 6](../../joi190103supp1_prod.pdf#page=6), [Supplement 1 PDF p. 10](../../joi190103supp1_prod.pdf#page=10), [Supplement 1 PDF p. 19](../../joi190103supp1_prod.pdf#page=19).
- **Source evidence:** Page 19 says eTable 4 displays adjusted HRs/CIs at 2, 5, and 8 years, but the adjacent and repeated table is headed eTable 7. Actual eTable 4 reports cause-specific event rates.
- **Rule/calculation:** A result cross-reference must identify the displayed table containing the described measure/time points; `eTable 4` and `eTable 7` are different labels and content.
- **Alternative source-grounded interpretation:** The prose may preserve numbering from an earlier supplement version.
- **Human question:** Should the page-19 reference name eTable 7, or was a different table intended?

## C010 — Biguanide count and percentage do not reconcile in eTable 3

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Checker provenance:** AUDIT-OMISSION-001 identified during final evidence-quality audit after numeric-check closure.
- **Relationship IDs:** N022
- **Exact source locations:** [Supplement 1 PDF p. 5](../../joi190103supp1_prod.pdf#page=5).
- **Source evidence:** eTable 3 labels the metabolic-surgery group N=2,287 and prints biguanides as 1,530 (67.9%).
- **Rule/calculation:** `1,530 / 2,287 × 100 = 66.8999%`, which rounds to 66.9% at one decimal, not 67.9%.
- **Alternative source-grounded interpretation:** The count or percentage may be a transcription error, or a different unprinted denominator may have been used; the row and column supply no alternate denominator.
- **Human question:** Which of the printed count, percentage, or denominator is intended for the surgery-group biguanide row?

## C011 — Standardized-difference footnote says absolute value while columns contain negative values

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** AUDIT-OMISSION-002 identified during final evidence-quality audit after numeric-check closure.
- **Relationship IDs:** N005
- **Exact source locations:** [main article PDF p. 5](../../jama_aminian_2019_oi_190103.pdf#page=5), [main article PDF p. 6](../../jama_aminian_2019_oi_190103.pdf#page=6).
- **Source evidence:** Table 1 footnote b defines standardized differences as the “absolute value” of the group difference divided by pooled SD. The before/after columns contain negative entries, including index date -42.6/-15.9, men -28.0/-2.9, age -75.3/-19.9, and numerous additional negative values.
- **Rule/calculation:** An absolute value is nonnegative; printed negative values cannot simultaneously be absolute values under the footnote definition.
- **Alternative source-grounded interpretation:** The table may intentionally report signed standardized differences in the stated surgery-minus-control direction, with “absolute value” inadvertently retained in the footnote.
- **Human question:** Are the columns intended to show signed standardized differences, or should the footnote/table signs be reconciled?

## Ledger Summary

- Stable candidate IDs: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011.
- Stable candidate count: **11**.
- Every candidate remains **Pending Human Adjudication**.
