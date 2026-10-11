# Numeric consistency checker — Workflow 1.6

Runtime UUID: 01a12886-0eb9-7ba0-bdcd-bccaf6412cd7. Model/effort contract: gpt-6.1-sol/medium, fresh mandatory numeric reviewer.

Scope completed: DOC-001 REPORT physical pp.1–12; DOC-002 REPORT pp.1–20; DOC-003 PLAN pp.1–7. All 39 mapped pages and both complete extraction maps were read; all 61 Table 1 rows, all 80 risk-set counts, all supplementary scalar groups, code/threshold definitions, and graphical mappings were checked. No old candidate/report conclusions or web used. No sources or reused assets changed.

Inventory: [numeric_relationship_inventory.md](../relationships/numeric_relationship_inventory.md), 123 hierarchical N records: 38 complete source groups, 61 individual baseline rows, eight Table 2 rows, 16 risk-set rows. Inferential reconstruction is assigned separately, while this lane checks scalar containment, sign, units, reference groups and arithmetic. Fifteen distinct candidate aliases follow; no stable C IDs, severity, validity, evidence-state or disposition is assigned.

Direct-source confirmation: fresh pdftotext -layout, Poppler 26.01.0, local CPU:
- Main physical pp.5–7 → preprocessing/numeric-main-p05-p07.txt.
- Complete results supplement → preprocessing/numeric-support-layout.txt.
- Complete PLAN → preprocessing/numeric-plan-layout.txt.
Exact source inputs and commands: `pdftotext -layout -f 5 -l 7 jama_aminian_2019_oi_190103.pdf .ai_paper_validation/review_1_6/preprocessing/numeric-main-p05-p07.txt`; `pdftotext -layout joi190103supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/numeric-support-layout.txt`; `pdftotext -layout joi190103supp2_prod.pdf .ai_paper_validation/review_1_6/preprocessing/numeric-plan-layout.txt`. This is supplemental confirmation of already mapped reusable-backed pages; it does not change fresh-required coverage counts.

## Completed arithmetic and no-candidate observations

- All flow branches reconcile exactly. Overlapping exclusion reasons are explicitly permitted. Procedure and BMI category counts sum to 2287. Table 1 sex, race including missingness, smoking including missingness, location, BMI categories, and noninsulin medication-count classes sum to their cohort n in all three columns. Medication use plus zero-use counts also reconcile.
- All 142 explicitly printed Table 1 count/percentage pairs were recomputed against the cohort headers; two surgical BP missingness cells print zero without a percentage. Three separate percentage mismatches are recorded below. All other count/percentage pairs obey displayed precision. All continuous IQRs are ordered and contain their medians.
- The unmatched BMI upper quartile 60.6 is compatible with the category counts. Exactly 72.401762294% are below 40 and 27.598237706% are at least 40; a 75th percentile of 60.6 is mathematically possible if most of the upper category exceeds 60.6. No candidate alias is assigned to an unusual value without a supplied contradiction.
- Every Figure 2/3 risk row is nonnegative and nonincreasing. All Table 2 baseline populations match the figures. Nonrenal exclusions reproduce Table 1 baseline conditions exactly: surgery/control heart failure 2287−238=2049 /11435−1342=10093; coronary 2287−237=2050 /11435−1104=10331; cerebrovascular 2287−42=2245 /11435−358=11077; AF 2287−152=2135 /11435−701=10734. Renal populations additionally exclude baseline low eGFR/dialysis; therefore 2287−191 need not equal 1937, nor 11435−1219 equal 9190.
- Table 2 primary, secondary and mortality ARDs reconcile (47.7−30.8=16.9;27.6−17.0=10.6;17.8−10.0=7.8). The five other rows are distinct comparisons below.
- All early adverse-event count/percentage pairs round coherently at N=2287; events can overlap. Early raw percentages and later Kaplan–Meier incidence have different horizons and denominators.
- All eTable 3 count/percent pairs reconcile except biguanides. All eTable 4 differences equal nonsurgical minus surgical rates. All 48 eTable 5 cumulative-incidence tuples have ordered bounds and coherent increasing time series. All 24 eTable 7 tuples repeated on p19 agree exactly.
- All 120 eTable 9 observation/patient counts satisfy observations ≥ distinct patients and patients ≤ cohort; later samples are nonincreasing. These measurements occur AFTER timepoints and do not have to equal instantaneous survival risk sets. All ten eTable 10 counts obey cohort bounds and monotonicity.
- All eTable 8 pound/kg conversions reconcile under rounding; surgery−control negative change contrasts are consistent with the main's positive reduction magnitudes. Main 29.1−8.7=20.4 versus reported20.3kg remains compatible with three one-decimal rounding errors (combined0.15kg), so no candidate. Percent weight loss and kg change are distinct scales. All 24 eTable 11 cumulative intervention estimates increase over time with ordered intervals; overlapping procedures are not summed as exclusive categories.
- All 16 E-values obey E≥1 and upper-limit E-value≤point E-value. No unreported HR-to-RR formula is imposed. Explicitly varying reference groups in eTable 12 are retained rather than presumed errors. Eight PH P values reconcile the AF exception claim. Five assignments×three ratios=15 datasets and eight endpoints yield120 plotted HR/CI pairs. Graph-only numbers are not digitized.
- PLAN cutpoints, dates, component counts, risk exclusions, sensitivity counts and units were checked. HbA1c >6.4% and ≥6.5% are equivalent on a one-decimal measurement grid; an unreported finer grid does not itself contradict a reported count. BMI interval boundary shorthand and early-event <90 versus within90 wording do not supply an independently contradictory count.
- Historical numerical claims lack supplied independent matched comparator data; no external lookup is allowed. Background values, thresholds and code numbers remain covered. No display-zero P occurs in the supplied scalar maps.

## Candidate evidence cards

## NUM-01: Heart failure: displayed absolute risk difference

- **Relationship inventory:** N103.
- **Compared locations and document roles:** [Main Table 2 Heart failure row](../../../jama_aminian_2019_oi_190103.pdf#page=7) REPORT, surgical 8-year risk cell; same page/row REPORT, nonsurgical 8-year risk cell; same page/row REPORT, absolute 8-year risk difference cell; same page Table 2 footnote a REPORT.
- **Printed inputs:** 6.8% surgical; 18.9% nonsurgical; printed ARD 12.9%; footnote defines difference as nonsurgical control group − metabolic surgery.
- **Reproducible rule:** Subtract the two same-outcome 8-year absolute risks in the stated order.
- **Calculation:** 18.9 − 6.8 = 12.1 percentage points; printed 12.9 differs by 0.8 percentage points.
- **Tolerance:** Each one-decimal input represents ±0.05 percentage points; difference discrepancy has maximum combined rounding tolerance 0.15 percentage points.
- **Direct observation versus inference:** All three cells and subtraction definition are directly printed. The diagnostic inference is that the printed point estimates cannot be one subtraction of the displayed same-outcome group risks under the stated rule.
- **Source-grounded alternatives / missing definition:** A separately adjusted, bootstrap-averaged, differently censored or differently time-indexed contrast could differ, but Table 2 does not label its ARD point estimate that way; bootstrapping is explicitly named for the CI. Missing definition: exact estimand and point-estimate construction.
- **Quality-control relevance:** Extracted ARDs may be reused independently of the displayed group risks; the point estimates need a consistent relationship or explicit alternate label.
- **Exact human question:** Does the heart failure ARD use a different estimand, population, time, or averaging rule from the two displayed 8-year cumulative risks, or does one printed point estimate require correction?

## NUM-02: Coronary artery disease: displayed absolute risk difference

- **Relationship inventory:** N104.
- **Compared locations and document roles:** [Main Table 2 Coronary artery disease row](../../../jama_aminian_2019_oi_190103.pdf#page=7) REPORT, surgical 8-year risk cell; same page/row REPORT, nonsurgical 8-year risk cell; same page/row REPORT, absolute 8-year risk difference cell; same page Table 2 footnote a REPORT.
- **Printed inputs:** 7.9% surgical; 11.6% nonsurgical; printed ARD 4.2%; footnote defines difference as nonsurgical control group − metabolic surgery.
- **Reproducible rule:** Subtract the two same-outcome 8-year absolute risks in the stated order.
- **Calculation:** 11.6 − 7.9 = 3.7 percentage points; printed 4.2 differs by 0.5 percentage points.
- **Tolerance:** Each one-decimal input represents ±0.05 percentage points; difference discrepancy has maximum combined rounding tolerance 0.15 percentage points.
- **Direct observation versus inference:** All three cells and subtraction definition are directly printed. The diagnostic inference is that the printed point estimates cannot be one subtraction of the displayed same-outcome group risks under the stated rule.
- **Source-grounded alternatives / missing definition:** A separately adjusted, bootstrap-averaged, differently censored or differently time-indexed contrast could differ, but Table 2 does not label its ARD point estimate that way; bootstrapping is explicitly named for the CI. Missing definition: exact estimand and point-estimate construction.
- **Quality-control relevance:** Extracted ARDs may be reused independently of the displayed group risks; the point estimates need a consistent relationship or explicit alternate label.
- **Exact human question:** Does the coronary artery disease ARD use a different estimand, population, time, or averaging rule from the two displayed 8-year cumulative risks, or does one printed point estimate require correction?

## NUM-03: Cerebrovascular disease: displayed absolute risk difference

- **Relationship inventory:** N105.
- **Compared locations and document roles:** [Main Table 2 Cerebrovascular disease row](../../../jama_aminian_2019_oi_190103.pdf#page=7) REPORT, surgical 8-year risk cell; same page/row REPORT, nonsurgical 8-year risk cell; same page/row REPORT, absolute 8-year risk difference cell; same page Table 2 footnote a REPORT.
- **Printed inputs:** 4.1% surgical; 5.6% nonsurgical; printed ARD 1.8%; footnote defines difference as nonsurgical control group − metabolic surgery.
- **Reproducible rule:** Subtract the two same-outcome 8-year absolute risks in the stated order.
- **Calculation:** 5.6 − 4.1 = 1.5 percentage points; printed 1.8 differs by 0.3 percentage points.
- **Tolerance:** Each one-decimal input represents ±0.05 percentage points; difference discrepancy has maximum combined rounding tolerance 0.15 percentage points.
- **Direct observation versus inference:** All three cells and subtraction definition are directly printed. The diagnostic inference is that the printed point estimates cannot be one subtraction of the displayed same-outcome group risks under the stated rule.
- **Source-grounded alternatives / missing definition:** A separately adjusted, bootstrap-averaged, differently censored or differently time-indexed contrast could differ, but Table 2 does not label its ARD point estimate that way; bootstrapping is explicitly named for the CI. Missing definition: exact estimand and point-estimate construction.
- **Quality-control relevance:** Extracted ARDs may be reused independently of the displayed group risks; the point estimates need a consistent relationship or explicit alternate label.
- **Exact human question:** Does the cerebrovascular disease ARD use a different estimand, population, time, or averaging rule from the two displayed 8-year cumulative risks, or does one printed point estimate require correction?

## NUM-04: Nephropathy: displayed absolute risk difference

- **Relationship inventory:** N106.
- **Compared locations and document roles:** [Main Table 2 Nephropathy row](../../../jama_aminian_2019_oi_190103.pdf#page=7) REPORT, surgical 8-year risk cell; same page/row REPORT, nonsurgical 8-year risk cell; same page/row REPORT, absolute 8-year risk difference cell; same page Table 2 footnote a REPORT.
- **Printed inputs:** 6.1% surgical; 16.3% nonsurgical; printed ARD 11.1%; footnote defines difference as nonsurgical control group − metabolic surgery.
- **Reproducible rule:** Subtract the two same-outcome 8-year absolute risks in the stated order.
- **Calculation:** 16.3 − 6.1 = 10.2 percentage points; printed 11.1 differs by 0.9 percentage points.
- **Tolerance:** Each one-decimal input represents ±0.05 percentage points; difference discrepancy has maximum combined rounding tolerance 0.15 percentage points.
- **Direct observation versus inference:** All three cells and subtraction definition are directly printed. The diagnostic inference is that the printed point estimates cannot be one subtraction of the displayed same-outcome group risks under the stated rule.
- **Source-grounded alternatives / missing definition:** A separately adjusted, bootstrap-averaged, differently censored or differently time-indexed contrast could differ, but Table 2 does not label its ARD point estimate that way; bootstrapping is explicitly named for the CI. Missing definition: exact estimand and point-estimate construction.
- **Quality-control relevance:** Extracted ARDs may be reused independently of the displayed group risks; the point estimates need a consistent relationship or explicit alternate label.
- **Exact human question:** Does the nephropathy ARD use a different estimand, population, time, or averaging rule from the two displayed 8-year cumulative risks, or does one printed point estimate require correction?

## NUM-05: Atrial fibrillation: displayed absolute risk difference

- **Relationship inventory:** N107.
- **Compared locations and document roles:** [Main Table 2 Atrial fibrillation row](../../../jama_aminian_2019_oi_190103.pdf#page=7) REPORT, surgical 8-year risk cell; same page/row REPORT, nonsurgical 8-year risk cell; same page/row REPORT, absolute 8-year risk difference cell; same page Table 2 footnote a REPORT.
- **Printed inputs:** 7.9% surgical; 13.6% nonsurgical; printed ARD 6.5%; footnote defines difference as nonsurgical control group − metabolic surgery.
- **Reproducible rule:** Subtract the two same-outcome 8-year absolute risks in the stated order.
- **Calculation:** 13.6 − 7.9 = 5.7 percentage points; printed 6.5 differs by 0.8 percentage points.
- **Tolerance:** Each one-decimal input represents ±0.05 percentage points; difference discrepancy has maximum combined rounding tolerance 0.15 percentage points.
- **Direct observation versus inference:** All three cells and subtraction definition are directly printed. The diagnostic inference is that the printed point estimates cannot be one subtraction of the displayed same-outcome group risks under the stated rule.
- **Source-grounded alternatives / missing definition:** A separately adjusted, bootstrap-averaged, differently censored or differently time-indexed contrast could differ, but Table 2 does not label its ARD point estimate that way; bootstrapping is explicitly named for the CI. Missing definition: exact estimand and point-estimate construction.
- **Quality-control relevance:** Extracted ARDs may be reused independently of the displayed group risks; the point estimates need a consistent relationship or explicit alternate label.
- **Exact human question:** Does the atrial fibrillation ARD use a different estimand, population, time, or averaging rule from the two displayed 8-year cumulative risks, or does one printed point estimate require correction?

## NUM-06: Table 1 Men, n (%): percentage versus count

- **Relationship inventory:** N041.
- **Compared locations and document roles:** [Main Table 1 Men, n (%)](../../../jama_aminian_2019_oi_190103.pdf#page=5) REPORT, count/percent cell for unmatched nonsurgical patients; same page Table 1 cohort header REPORT.
- **Printed inputs:** 18895 (48.2%); cohort n=39267.
- **Reproducible rule:** Percentage = 100 × displayed count / stated same-column cohort denominator.
- **Calculation:** 18895/39267 ×100 = 48.119285914%, which rounds to 48.1%; printed 48.2%.
- **Displayed rounding interval:** [48.15,48.25)%; the exact recomputed percentage is outside this interval. This uses the printed column n and assumes unweighted percentages of that cohort.
- **Tolerance:** ±0.05 percentage points for the displayed one-decimal percentage; exact integer counts/denominator have tolerance zero.
- **Direct observation versus inference:** The count, percentage and denominator are direct observations; recomputed percentage and rounding are arithmetic, without imputation/model inference.
- **Source-grounded alternatives / missing definition:** An alternate denominator or weighted percentage could explain a mismatch, but Table 1 labels number (%) under these cohort n values. Race categories plus missingness sum exactly to 11435, and unmatched sex categories sum exactly to39267. Missing definition if applicable: whether percentages use a different population or weights.
- **Quality-control relevance:** Small percentage discrepancies can propagate when downstream users extract the displayed percentage rather than recompute it.
- **Exact human question:** Is the printed percentage based on the stated count and cohort n, or is another denominator/weighting rule intended? If the cohort denominator is intended, which printed input needs correction?

## NUM-07: Table 1 Other race, n (%): percentage versus count

- **Relationship inventory:** N050.
- **Compared locations and document roles:** [Main Table 1 Other race, n (%)](../../../jama_aminian_2019_oi_190103.pdf#page=5) REPORT, count/percent cell for matched nonsurgical patients; same page Table 1 cohort header REPORT.
- **Printed inputs:** 234 (2.1%); cohort n=11435.
- **Reproducible rule:** Percentage = 100 × displayed count / stated same-column cohort denominator.
- **Calculation:** 234/11435 ×100 = 2.046348929%, which rounds to 2.0%; printed 2.1%.
- **Displayed rounding interval:** [2.05,2.15)%; the exact recomputed percentage is outside this interval. This uses the printed column n and assumes unweighted percentages of that cohort.
- **Tolerance:** ±0.05 percentage points for the displayed one-decimal percentage; exact integer counts/denominator have tolerance zero.
- **Direct observation versus inference:** The count, percentage and denominator are direct observations; recomputed percentage and rounding are arithmetic, without imputation/model inference.
- **Source-grounded alternatives / missing definition:** An alternate denominator or weighted percentage could explain a mismatch, but Table 1 labels number (%) under these cohort n values. Race categories plus missingness sum exactly to 11435, and unmatched sex categories sum exactly to39267. Missing definition if applicable: whether percentages use a different population or weights.
- **Quality-control relevance:** Small percentage discrepancies can propagate when downstream users extract the displayed percentage rather than recompute it.
- **Exact human question:** Is the printed percentage based on the stated count and cohort n, or is another denominator/weighting rule intended? If the cohort denominator is intended, which printed input needs correction?

## NUM-08: Table 1 UACR missing, n (%): percentage versus count

- **Relationship inventory:** N088.
- **Compared locations and document roles:** [Main Table 1 UACR missing, n (%)](../../../jama_aminian_2019_oi_190103.pdf#page=6) REPORT, count/percent cell for unmatched nonsurgical patients; same page Table 1 cohort header REPORT.
- **Printed inputs:** 14665 (37.4%); cohort n=39267.
- **Reproducible rule:** Percentage = 100 × displayed count / stated same-column cohort denominator.
- **Calculation:** 14665/39267 ×100 = 37.346881605%, which rounds to 37.3%; printed 37.4%.
- **Displayed rounding interval:** [37.35,37.45)%; the exact recomputed percentage is outside this interval. This uses the printed column n and assumes unweighted percentages of that cohort.
- **Tolerance:** ±0.05 percentage points for the displayed one-decimal percentage; exact integer counts/denominator have tolerance zero.
- **Direct observation versus inference:** The count, percentage and denominator are direct observations; recomputed percentage and rounding are arithmetic, without imputation/model inference.
- **Source-grounded alternatives / missing definition:** An alternate denominator or weighted percentage could explain a mismatch, but Table 1 labels number (%) under these cohort n values. Race categories plus missingness sum exactly to 11435, and unmatched sex categories sum exactly to39267. Missing definition if applicable: whether percentages use a different population or weights.
- **Quality-control relevance:** Small percentage discrepancies can propagate when downstream users extract the displayed percentage rather than recompute it.
- **Exact human question:** Is the printed percentage based on the stated count and cohort n, or is another denominator/weighting rule intended? If the cohort denominator is intended, which printed input needs correction?

## NUM-09: Absolute standardized-difference definition versus signed columns

- **Relationship inventory:** N007; N039–N099.
- **Compared locations and document roles:** [Table 1 footnote b](../../../jama_aminian_2019_oi_190103.pdf#page=6) REPORT; [Table 1 signed columns](../../../jama_aminian_2019_oi_190103.pdf#page=5) REPORT; [Table 1 continued signed columns](../../../jama_aminian_2019_oi_190103.pdf#page=6) REPORT.
- **Printed inputs:** Footnote b defines absolute value of the difference in means or proportions (surgery − nonsurgical) divided by pooled SD. Printed examples: index date −42.6/−15.9; men −28.0/−2.9; age −75.3/−19.9; HbA1c −2.3/−11.4; diastolic BP −35.3/−44.2.
- **Reproducible rule and calculation:** An absolute difference divided by positive SD cannot be negative. 69 of 122 standardized-difference cells are negative; any absolute-difference formula is incompatible with, for example, −28.0.
- **Tolerance:** Zero sign tolerance; rounding cannot yield a negative absolute value.
- **Direct observation versus inference:** Negative cells and absolute-value wording are directly printed. No SD formula, mean from median, or percentage scaling is inferred.
- **Alternatives / missing definition:** The intended measure may be signed differences or absolute differences. Pooled-SD formula and scaling are unspecified, but neither affects the sign check.
- **Quality-control relevance:** The single shared column definition determines interpretation of all signed cells.
- **Exact human question:** Are these columns intended to contain signed or absolute standardized differences, and should the definition or signed entries describe that convention?

## NUM-10: Surgical biguanide percentage versus count

- **Relationship inventory:** N024.
- **Compared locations and document roles:** [eTable 3 biguanides row](../../../joi190103supp1_prod.pdf#page=5) REPORT, surgical count/percent cell; same page REPORT, surgical N header.
- **Printed inputs:** 1530 (67.9%); N=2287.
- **Reproducible rule and calculation:** Percentage = 100 × count / stated cohort denominator. 1530/2287 × 100 = 66.899868824%, which rounds to 66.9%.
- **Tolerance:** Printed 67.9% implies [67.85,67.95)% under nearest one-decimal rounding; exact counts have zero tolerance.
- **Direct observation versus inference:** Inputs are directly printed; percentage is arithmetic.
- **Alternatives / missing definition:** A different denominator or weighted percentage could differ, but neither is stated under N=2287.
- **Quality-control relevance:** Baseline medication prevalence may be extracted directly.
- **Exact human question:** Does 67.9% use count 1530 and N=2287, or is another denominator intended? Which input or label represents the baseline cohort?

## NUM-11: Baseline medication sample size versus matched control cohort

- **Relationship inventory:** N032; N013; N006.
- **Compared locations and document roles:** [eTable 10 year 0](../../../joi190103supp1_prod.pdf#page=14) REPORT, nonsurgical sample; [eTable 3 N header](../../../joi190103supp1_prod.pdf#page=5) REPORT; [Table 1 N header and medications](../../../jama_aminian_2019_oi_190103.pdf#page=6) REPORT.
- **Printed inputs:** eTable 10 year 0 nonsurgical sample 11433; eTable 3 and Table 1 matched nonsurgical N=11435.
- **Reproducible rule and calculation:** The same baseline medication population should reconcile or identify an exclusion/missingness rule. 11435 − 11433 = 2 participants, or 0.017490% of the matched cohort.
- **Tolerance:** Zero integer tolerance; population identity remains conditional.
- **Direct observation versus inference:** Both counts and baseline labels are printed. The inference assumes the same baseline eligible medication population.
- **Alternatives / missing definition:** Two patients could lack medication observations or eligible follow-up; eTable 10 supplies no exclusion reason.
- **Quality-control relevance:** Medication proportions depend on their eligible denominator.
- **Exact human question:** Which two matched nonsurgical patients are excluded at year 0 in eTable 10, and what data or follow-up rule explains 11433 rather than 11435?

## NUM-12: Percentage notation in a person-time rate title

- **Relationship inventory:** N025.
- **Compared locations and document roles:** [eTable 4 title](../../../joi190103supp1_prod.pdf#page=6) REPORT; same page REPORT, headers/footnotes; [Contents eTable 4 title](../../../joi190103supp1_prod.pdf#page=1) REPORT.
- **Printed inputs:** Title contains Cause-Specific Event Rates (%) per 100 Patient-Years; header states rate per 100 patient-years; primary values 4.51/7.45 and difference 2.94.
- **Reproducible rule and calculation:** An incidence density is events/person-time; a percentage is dimensionless. 4.51 events/100 patient-years = 0.0451 events/patient-year; this alone does not identify a 4.51% risk. Scaling by 100 does not remove the time denominator.
- **Tolerance:** Unit distinction has no rounding tolerance; printed rate differences themselves reconcile.
- **Direct observation versus inference:** Both (%) and the person-time unit are printed; dimensional comparison is derived reasoning.
- **Alternatives / missing definition:** (%) may be informal notation for per-100 scaling; the column unit and footnotes correctly identify rates. No count/person-time totals are supplied.
- **Quality-control relevance:** A title-level unit ambiguity can cause extraction of a rate as a risk.
- **Exact human question:** Does (%) denote per-100 scaling only, or a risk/proportion? Which unit should readers attach to these values?

## NUM-13: Five-component MACE label attached to the primary result

- **Relationship inventory:** N036; N002.
- **Compared locations and document roles:** [E-value primary interpretation](../../../joi190103supp1_prod.pdf#page=19) REPORT, HR/E-value paragraph and subsequent five-component sentence; [Primary endpoint definition](../../../jama_aminian_2019_oi_190103.pdf#page=2) REPORT; [Figure 2 caption](../../../jama_aminian_2019_oi_190103.pdf#page=7) REPORT.
- **Printed inputs:** Supplement primary HR 0.61 (0.55,0.69), E-value 2.15; subsequent sentence says both 5-component MACE and metabolic surgery. Main defines primary MACE as 6 outcomes: death, coronary events, cerebrovascular events, heart failure, nephropathy, atrial fibrillation.
- **Reproducible rule and calculation:** Count components of the matched primary endpoint. Six listed components versus five in the interpretation; 6 − 5 = 1 component.
- **Tolerance:** Zero integer tolerance; identical HR and CI identify the primary result.
- **Direct observation versus inference:** Six-component definition, five-component label, and matching HR are printed. A drafting omission is only an inferred explanation.
- **Alternatives / missing definition:** A separate five-component analysis would require its definition and confirmation that the same HR/E-value refers to it; none is identified.
- **Quality-control relevance:** Endpoint definitions determine quantitative result matching.
- **Exact human question:** Which component set underlies HR 0.61 and E-value 2.15, and does five-component MACE refer to a separate analysis or the six-component primary endpoint?

## NUM-14: Time-varying HR paragraph references an event-rate table

- **Relationship inventory:** N036; N028.
- **Compared locations and document roles:** [Time-varying HR paragraph](../../../joi190103supp1_prod.pdf#page=19) REPORT; [eTable 4](../../../joi190103supp1_prod.pdf#page=6) REPORT; [eTable 7](../../../joi190103supp1_prod.pdf#page=10) REPORT; [Repeated eTable 7](../../../joi190103supp1_prod.pdf#page=19) REPORT.
- **Printed inputs:** Paragraph says eTable 4 displays adjusted HRs/95% CIs at 2,5,8 years. Actual eTable 4 displays rates per 100 patient-years at 8 years. eTable 7 displays the claimed HRs/time grid.
- **Reproducible rule and calculation:** A numeric table reference should identify its stated measure and times. Table 4 primary rates 4.51/7.45 at 8 years versus table 7 primary HRs 0.57/0.78/0.79 at 2/5/8 years.
- **Tolerance:** Exact table-number, measure and time identity; rounding irrelevant.
- **Direct observation versus inference:** Reference 4 and both table contents are direct observations; intended reference 7 is an inference.
- **Alternatives / missing definition:** Table numbers may have changed during assembly; final supplied numbers still disagree with the text.
- **Quality-control relevance:** Following the reference yields a different measure and time definition.
- **Exact human question:** Which supplied table is intended by this paragraph, and should the numeric reference identify eTable 7?

## NUM-15: Plan matching direction versus achieved cohort ratio

- **Relationship inventory:** N001; N037; N038.
- **Compared locations and document roles:** [Protocol matching process](../../../joi190103supp2_prod.pdf#page=3) PLAN; [Figure 1 cohort and matching caption](../../../jama_aminian_2019_oi_190103.pdf#page=3) REPORT; [Cohort results](../../../jama_aminian_2019_oi_190103.pdf#page=4) REPORT; [Protocol sensitivity ratios](../../../joi190103supp2_prod.pdf#page=6) PLAN, contextual corroboration.
- **Printed inputs:** PLAN: Each non-surgical patient will be matched ... to five (5) surgical patients. REPORT: 2287 surgical and 11435 nonsurgical; caption matches surgery patients to 5 controls. PLAN p6 lists 1:5 without explicit group order.
- **Reproducible rule and calculation:** Named group order determines direction of the matching ratio. REPORT surgery:nonsurgery = 2287:11435 = 1:5; literal PLAN surgery:nonsurgery = 5:1. Ratios are 0.2 and 5, respectively.
- **Tolerance:** Exact integer ratio; no rounding tolerance.
- **Direct observation versus inference:** Named groups and five-match wording are printed; ratio arithmetic is derived. No claim about execution or protocol compliance is made.
- **Alternatives / missing definition:** The PLAN sentence may reverse group names while intending one surgery patient to five controls; p6 alone does not define the order. A disclosed change is another possible explanation.
- **Quality-control relevance:** Direction defines the reported comparison population.
- **Exact human question:** Was the plan one surgery patient to five controls or one control to five surgery patients, and does the p3 wording need clarification or describe a planned change?

## Scope limits

No scientific coverage gap. Exact graphical coordinates, raw person-time, some event counts, pooled-SD conventions, and E-value transformations are not supplied. These limit reconstruction, not mapped coverage. Candidate NUM-11 explicitly preserves the unresolved baseline-population distinction. Individual statistical diagnostic relationships are handled by separate mandatory agents, without suppressing this lane's numeric candidates.

