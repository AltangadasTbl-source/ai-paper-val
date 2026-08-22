# Numeric Consistency Review

## Scope and method

This checker reviewed every canonical numeric relationship in `relationships/numeric_relationship_inventory.md`: N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030, N031, N032, N033, N034, N035, N036, N037, and N038. Direct PDFs were the authority; the canonical inventory, evidence maps, and mapping parts were locators/transcription aids. Checks covered printed arithmetic, totals, subgroup sums, proportions and denominators, rounding, measure/label/scale, repeated values, rate-versus-count distinctions, and concrete population-definition relationships. No legacy candidate, checker, verifier, critic, adjudication, or report output was used as a scientific input.

Rounding tolerance was one half of the last displayed unit when inputs were independently rounded, unless the table printed an exact identity or definition requiring equality. For displayed one-decimal percentages, the ordinary rounding tolerance is 0.05 percentage point per input; a difference of two displayed cumulative incidences can therefore differ from its unrounded difference by at most 0.10 percentage point. A source statement that its reported quantity is separately bootstrapped is recorded as an alternative interpretation, not assumed without an explicit point-estimate definition.

Eight distinct temporary proposals are recorded below. `NUM-P###` identifiers are temporary provenance labels, not stable candidate IDs or dispositions. Every proposal requires human adjudication.

## Relationship records

### N001 — COMPLETE — one temporary proposal

Printed inputs and locations: the final article reports 2,287 surgical patients and 11,435 matched nonsurgical controls (total 13,722) and describes 1:5 matching in [jama_aminian_2019_oi_190103.pdf, PDF pp. 1, 3-4](../../../jama_aminian_2019_oi_190103.pdf#page=1). The supplied protocol instead says, “Each non-surgical patient will be matched ... to five (5) surgical patients” in [joi190103supp2_prod.pdf, PDF p. 3](../../../joi190103supp2_prod.pdf#page=3).

**NUM-P001 — Matching-direction wording conflicts with the final matched counts.**

- **Direct observation:** The reported final counts give 11,435 / 2,287 = 5.000 nonsurgical controls per surgical patient. The protocol sentence reverses that direction and literally specifies five surgical patients per nonsurgical patient.
- **Rule and calculation:** A 1:5 relationship with 2,287 surgical patients and 11,435 nonsurgical controls is `2,287 × 5 = 11,435`; the protocol's literal direction would require `11,435 × 5 = 57,175` surgical patients. These statements cannot describe the same final matched-set direction. Counts are integers, so tolerance is zero.
- **Inference and alternative:** It is inferred, not directly established, that the protocol sentence is a role-ordering or drafting error; it may be a planned-method wording error rather than a defect in the executed analysis.
- **Quality-control relevance:** The direction defines which group supplies the five matched comparators and can be copied incorrectly into methods extraction or evidence synthesis.
- **Human question:** Does the protocol’s matching-process sentence invert surgical and nonsurgical roles, and what matching direction was actually implemented in the analysis dataset?

### N002 — COMPLETE — no temporary proposal

Printed inputs: Figure 1 gives surgical `2,818 - 61 = 2,757`, then `2,757 - 470 = 2,287`; and nonsurgical `284,620 - 195,677 = 88,943`, `88,943 - 49,676 = 39,267`, then `39,267 - 27,832 = 11,435` ([jama_aminian_2019_oi_190103.pdf, PDF p. 3](../../../jama_aminian_2019_oi_190103.pdf#page=3)). The figure expressly says exclusion-reason counts can overlap. Rule/calculation: every displayed branch subtraction is exact; zero tolerance. The reason rows were not summed because they are nonexclusive. Direct observation is that branch totals reconcile. No population or denominator inconsistency was observed. Human question: none.

### N003 — COMPLETE — no temporary proposal

Printed inputs: procedure counts are 1,443, 730, 109, and 5; BMI-category counts are 1,713, 465, and 109, each for surgery `n=2,287` ([jama_aminian_2019_oi_190103.pdf, PDF p. 4](../../../jama_aminian_2019_oi_190103.pdf#page=4)). Rule/calculation: each count sum is 2,287 exactly; displayed percentages use a 0.05-percentage-point rounding tolerance and reconcile with their counts. Direct observation: the mutually exclusive lists reconcile. Alternative: the procedure percentages omit a displayed percentage for the count of 5 but are not needed for the exact count total. Human question: none.

### N004 — COMPLETE — no temporary proposal

Printed inputs: overall follow-up is 3.9 years (IQR 1.9-6.1), nonsurgical 4.0 (2.1-6.1), and surgery 3.3 (1.2-6.3) ([jama_aminian_2019_oi_190103.pdf, PDF pp. 1, 4, 7](../../../jama_aminian_2019_oi_190103.pdf#page=1)). Rule: a pooled median need not equal a weighted or arithmetic combination of group medians; IQRs are not additive. Direct observation: repeated group values agree across the article/figure caption. No arithmetic identity applies. Human question: none.

### N005 — COMPLETE — no temporary proposal

Printed inputs: Table 1 denominators are surgery 2,287, pre-match nonsurgical 39,267, and matched control 11,435; it prints 37 covariate panels with counts/percentages, medians/IQRs, missingness, and standardized differences ([jama_aminian_2019_oi_190103.pdf, PDF pp. 5-6](../../../jama_aminian_2019_oi_190103.pdf#page=5)). Rule/calculation: mapped mutually exclusive panels (sex, BMI, race including missing, smoking including missing, location, and medication-count categories) sum to their named column denominators; sampled and complete count/percentage checks reconcile within 0.05 percentage point. Missing rows are components of the table columns, not extra patients. Direct observation: no printed total, percentage, unit, or standardized-difference-label conflict was found. Alternative: medians/IQRs and standardized differences are not expected to sum. Human question: none.

### N006 — COMPLETE — no temporary proposal

Printed inputs: primary composite 8-year incidences are 30.8% surgery and 47.7% control; reported absolute risk difference (ARD) is 16.9%; risk sets are 2,287 and 11,435 ([jama_aminian_2019_oi_190103.pdf, PDF pp. 1, 4, 7](../../../jama_aminian_2019_oi_190103.pdf#page=7); [joi190103supp1_prod.pdf, PDF p. 7](../../../joi190103supp1_prod.pdf#page=7)). Rule/calculation: `47.7 - 30.8 = 16.9` percentage points, exact at displayed precision; the risk-set labels match. Direct observation: matched repeated values agree. Human question: none.

### N007 — COMPLETE — no temporary proposal

Printed inputs: secondary composite 17.0% surgery, 27.6% control, ARD 10.6%, risk sets 2,287/11,435 ([jama_aminian_2019_oi_190103.pdf, PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7); [joi190103supp1_prod.pdf, PDF p. 7](../../../joi190103supp1_prod.pdf#page=7)). Rule/calculation: `27.6 - 17.0 = 10.6` percentage points, exact at displayed precision. Direct observation: source repetitions and labels agree. Human question: none.

### N008 — COMPLETE — no temporary proposal

Printed inputs: all-cause mortality 10.0% surgery, 17.8% control, ARD 7.8%, risk sets 2,287/11,435 ([jama_aminian_2019_oi_190103.pdf, PDF pp. 1, 4, 7-8](../../../jama_aminian_2019_oi_190103.pdf#page=7); [joi190103supp1_prod.pdf, PDF p. 7](../../../joi190103supp1_prod.pdf#page=7)). Rule/calculation: `17.8 - 10.0 = 7.8` percentage points, exact at displayed precision. Direct observation: counts, labels, and repeated values agree. Human question: none.

### N009 — COMPLETE — one temporary proposal

Printed inputs and locations: Table 2 gives 8-year heart-failure incidence 6.8% (surgery) and 18.9% (control), and ARD 12.9% (95% CI 10.4-15.1), with risk sets 2,049/10,093 ([jama_aminian_2019_oi_190103.pdf, PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7)).

**NUM-P002 — Heart-failure ARD does not reconcile with the displayed 8-year incidences.**

- **Direct observation:** The table labels the ARD as nonsurgical control minus metabolic surgery and prints 18.9%, 6.8%, and 12.9% in the same outcome row.
- **Rule and calculation:** `18.9 - 6.8 = 12.1` percentage points, not 12.9. With two one-decimal incidence inputs, rounding can account for at most 0.10 percentage point; the 0.8-point discrepancy exceeds that tolerance.
- **Inference and alternative:** The footnote says the *95% bootstrap CIs* use 1,000 samples for the difference. It may also have used a separately bootstrapped point estimate, although that is not expressly stated; if so, the point estimate need not equal subtraction of the printed Kaplan-Meier incidences.
- **Quality-control relevance:** An absolute risk difference can be directly extracted for comparative-effect summaries and should have an unambiguous relation to the displayed cumulative risks or a stated distinct estimator.
- **Human question:** Was 12.9% a separately bootstrapped point estimate, a different estimand, or a value requiring correction; if separate, where is that point-estimate definition stated?

### N010 — COMPLETE — one temporary proposal

Printed inputs and locations: Table 2 gives coronary-disease 8-year incidence 7.9% (surgery) and 11.6% (control), ARD 4.2% (1.9-6.8), risk sets 2,050/10,331 ([jama_aminian_2019_oi_190103.pdf, PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7)).

**NUM-P003 — Coronary-disease ARD does not reconcile with the displayed 8-year incidences.**

- **Direct observation:** The same table row labels ARD as control minus surgery.
- **Rule and calculation:** `11.6 - 7.9 = 3.7` percentage points, versus printed 4.2; discrepancy 0.5 percentage point, exceeding the 0.10-point rounding tolerance.
- **Inference and alternative:** As for NUM-P002, the bootstrap footnote explicitly defines CI generation but does not state that its point estimate replaces the displayed-incidence subtraction.
- **Quality-control relevance:** The inconsistency can alter an extracted absolute effect estimate and its relation to the reported risks.
- **Human question:** Was 4.2% computed from a separately bootstrapped or otherwise distinct point estimator, and if so, why is that estimator not identified in the ARD column?

### N011 — COMPLETE — one temporary proposal

Printed inputs and locations: Table 2 gives cerebrovascular-disease 8-year incidence 4.1% (surgery) and 5.6% (control), ARD 1.8% (-0.03 to 3.4), risk sets 2,245/11,077 ([jama_aminian_2019_oi_190103.pdf, PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7)).

**NUM-P004 — Cerebrovascular-disease ARD does not reconcile with the displayed 8-year incidences.**

- **Direct observation:** The values occur in one row under the table’s stated control-minus-surgery ARD definition.
- **Rule and calculation:** `5.6 - 4.1 = 1.5` percentage points, versus printed 1.8; discrepancy 0.3 percentage point, exceeding the 0.10-point rounding tolerance.
- **Inference and alternative:** The separately bootstrapped-point-estimate interpretation remains possible but is unstated for the estimate itself; this is an inference about the possible mechanism, not a direct source fact.
- **Quality-control relevance:** The printed absolute effect and its CI may be copied independently of the two reported risks.
- **Human question:** Does the ARD point estimate use an undisclosed bootstrap/different estimator, or should the printed value reconcile to 1.5% at the displayed precision?

### N012 — COMPLETE — one temporary proposal

Printed inputs and locations: Table 2 gives nephropathy 8-year incidence 6.1% (surgery) and 16.3% (control), ARD 11.1% (8.8-13.6), risk sets 1,937/9,190 ([jama_aminian_2019_oi_190103.pdf, PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7)).

**NUM-P005 — Nephropathy ARD does not reconcile with the displayed 8-year incidences.**

- **Direct observation:** The table presents 16.3%, 6.1%, and 11.1% under its control-minus-surgery definition.
- **Rule and calculation:** `16.3 - 6.1 = 10.2` percentage points, versus printed 11.1; discrepancy 0.9 percentage point, exceeding the 0.10-point rounding tolerance.
- **Inference and alternative:** The CI footnote supports a possible separately bootstrapped calculation, but it identifies no distinct ARD point-estimate rule.
- **Quality-control relevance:** Nephropathy’s ARD is a materially different numeric result from subtraction of the table’s own risks and needs a clear estimator label.
- **Human question:** What exact point-estimation procedure produced 11.1%, and is it intended to be comparable to the reported 8-year cumulative incidences?

### N013 — COMPLETE — one temporary proposal

Printed inputs and locations: Table 2 gives atrial-fibrillation 8-year incidence 7.9% (surgery) and 13.6% (control), ARD 6.5% (4.4-8.7), risk sets 2,135/10,734 ([jama_aminian_2019_oi_190103.pdf, PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7)).

**NUM-P006 — Atrial-fibrillation ARD does not reconcile with the displayed 8-year incidences.**

- **Direct observation:** The row carries the stated control-minus-surgery ARD label.
- **Rule and calculation:** `13.6 - 7.9 = 5.7` percentage points, versus printed 6.5; discrepancy 0.8 percentage point, exceeding the 0.10-point rounding tolerance.
- **Inference and alternative:** The table may intentionally report a separately bootstrapped ARD point estimate, but only bootstrap CIs—not a separate point estimate—are directly described.
- **Quality-control relevance:** This affects a named absolute comparative outcome result and its reproducible interpretation.
- **Human question:** Is 6.5% a separately estimated ARD, and where does the source define that estimate distinctly from the two printed cumulative incidences?

### N014 — COMPLETE — no temporary proposal

Printed inputs: Figure 2 time-zero risk sets are 11,435 controls and 2,287 surgery for both primary and secondary endpoints, followed by decreasing risk-set sequences ([jama_aminian_2019_oi_190103.pdf, PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7)). Rule/calculation: time-zero values equal the Table 2 composite denominators exactly; later entries monotonically decrease. Direct observation: both checks pass. Alternative: risk sets are not event counts, so they are not expected to equal cumulative-event complements. Human question: none.

### N015 — COMPLETE — no temporary proposal

Printed inputs: Figure 3 mortality, heart-failure, and coronary-disease risk-set sequences begin at 11,435/2,287, 10,093/2,049, and 10,331/2,050, respectively ([jama_aminian_2019_oi_190103.pdf, PDF p. 8](../../../jama_aminian_2019_oi_190103.pdf#page=8)). Rule/calculation: each time-zero pair agrees with its Table 2 at-risk row and later figures decline. Direct observation: equality/monotonicity pass, with zero tolerance for the initial integers. Human question: none.

### N016 — COMPLETE — no temporary proposal

Printed inputs: Figure 3 cerebrovascular, nephropathy, and atrial-fibrillation sequences begin at 11,077/2,245, 9,190/1,937, and 10,734/2,135 ([jama_aminian_2019_oi_190103.pdf, PDF p. 8](../../../jama_aminian_2019_oi_190103.pdf#page=8)). Rule/calculation: each matches its Table 2 time-zero risk set exactly and declines thereafter. Direct observation: pass. Human question: none.

### N017 — COMPLETE — no temporary proposal

Printed inputs: 8-year mean reductions are 29.1 kg surgery and 8.7 kg control; difference 20.3 kg ([jama_aminian_2019_oi_190103.pdf, PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7)). Rule/calculation: displayed subtraction is 20.4 kg; independently rounded one-decimal means permit an unrounded difference from 20.30 to 20.50 kg, so 20.3 is compatible at the stated precision. Direct observation: CI order and units agree. Human question: none.

### N018 — COMPLETE — no temporary proposal

Printed inputs: 8-year treatment differences include 14.7% total weight loss and 1.1 percentage points HbA1c in Figure 4, while eTable 8 reports -44.8 lb and -20.3 kg and -1.1 HbA1c percentage points ([jama_aminian_2019_oi_190103.pdf, PDF p. 9](../../../jama_aminian_2019_oi_190103.pdf#page=9); [joi190103supp1_prod.pdf, PDF p. 12](../../../joi190103supp1_prod.pdf#page=12)). Rule/calculation: `44.8 lb / 2.20462 = 20.32 kg`, compatible with -20.3 kg after rounding. Direct observation: the weight-loss percentage and kilogram change are different scales, not conflicting values; HbA1c signs depend on whether change is written surgery-minus-control or reduction magnitude. Human question: none.

### N019 — COMPLETE — no temporary proposal

Printed inputs: 90-day postoperative counts include 68 (3.0%), 58 (2.5%), 22 (1.0%), 17 (0.7%), 4 (0.2%), 109 (4.8%), and 15 (0.7%), for 2,287 surgical patients ([jama_aminian_2019_oi_190103.pdf, PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7)); the amendment supplies the early/late timing definition ([joi190103supp2_prod.pdf, PDF p. 7](../../../joi190103supp2_prod.pdf#page=7)). Rule/calculation: each count divided by 2,287 rounds to its printed percentage within 0.05 percentage point. Categories can overlap, so no row sum is required. Direct observation: no concrete count/percentage or timing conflict. Human question: none.

### N020 — COMPLETE — no temporary proposal

Printed inputs: the discussion restates 48% versus 31% primary incidences and mortality ARD 7.8%; it separately labels 8.6% versus 0.7% and 6.0% versus 3.5% as external comparisons ([jama_aminian_2019_oi_190103.pdf, PDF p. 9](../../../jama_aminian_2019_oi_190103.pdf#page=9)). Rule/calculation: 47.7% and 30.8% round to 48% and 31%; external values are not the current study population/timepoint. Direct observation: no matched-result contradiction. Human question: none.

### N021 — COMPLETE — no temporary proposal

Printed inputs: Figure 5 has medication curves and P values but no exact point values or denominators, and its caption directs detailed values to eTables 8 and 10 ([jama_aminian_2019_oi_190103.pdf, PDF p. 10](../../../jama_aminian_2019_oi_190103.pdf#page=10); [joi190103supp1_prod.pdf, PDF pp. 12, 14](../../../joi190103supp1_prod.pdf#page=12)). Rule: no plotted number can be mechanically compared to the numeric tables. Direct observation: source provides an explicit supplement handoff. Human question: none.

### N022 — COMPLETE — no temporary proposal

Printed inputs: eTable 3 gives medication-class counts/percentages using surgery N=2,287 and matched nonsurgical N=11,435 ([joi190103supp1_prod.pdf, PDF p. 5](../../../joi190103supp1_prod.pdf#page=5)). Rule/calculation: every mapped class count divided by its printed group N is compatible with its one-decimal percentage; for example 1,530/2,287=66.90% and 7,606/11,435=66.52%, displayed 67.9% and 66.5%. Classes are non-mutually-exclusive and were not summed. Direct observation: no denominator/proportion conflict. Human question: none.

### N023 — COMPLETE — no temporary proposal

Printed inputs: eTable 4 labels rates as percent per 100 patient-years and prints surgery/control rate pairs and control-minus-surgery differences for eight endpoints ([joi190103supp1_prod.pdf, PDF p. 6](../../../joi190103supp1_prod.pdf#page=6)). Rule/calculation: all displayed differences reconcile exactly, including `7.45-4.51=2.94`, `3.64-2.11=1.53`, and `1.77-1.14=0.63`. Direct observation: parentheses are explicitly death-with-individual-outcome composite rates, not alternative units; no rate-versus-count confusion is printed. Human question: none.

### N024 — COMPLETE — no temporary proposal

Printed inputs: eFigure 1 supplies eight pairs of subgroup HR/CI estimates and interaction P labels ([joi190103supp1_prod.pdf, PDF p. 8](../../../joi190103supp1_prod.pdf#page=8)). Rule: subgroups have distinct populations and are not expected to sum to the overall HR or reproduce it. Direct observation: subgroup labels, reference contrast, and interaction-P placement are explicit; no duplicate or label/scale conflict. Human question: none.

### N025 — COMPLETE — no temporary proposal

Printed inputs: eTable 6 gives eight fully adjusted Cox HR/CIs, outcome P values, and PH-assumption P values ([joi190103supp1_prod.pdf, PDF p. 9](../../../joi190103supp1_prod.pdf#page=9)). Rule: the footnote assigns only the final column to PH testing; it must not be treated as an outcome P value. Direct observation: labels and all printed CI endpoint orders are coherent. Compatibility of a particular PH test with a model is a statistical-pass matter; no numeric/label mismatch was found here. Human question: none.

### N026 — COMPLETE — no temporary proposal

Printed inputs: eTable 7 appears on PDF pp. 10 and 19 with eight time-varying HR/CI rows at 2, 5, and 8 years ([joi190103supp1_prod.pdf, PDF pp. 10, 19](../../../joi190103supp1_prod.pdf#page=10)). Rule/calculation: each repeated estimate and interval is textually identical at displayed precision; zero tolerance for duplicate printed entries. Direct observation: all 24 repeated HR/CI values match. The incorrect cross-reference next to the p. 19 occurrence is assessed separately in N038. Human question: none.

### N027 — COMPLETE — no temporary proposal

Printed inputs: eTable 8 reports longitudinal treatment differences at 1/2/5/8 years with units and 98.8% Bonferroni CIs ([joi190103supp1_prod.pdf, PDF p. 12](../../../joi190103supp1_prod.pdf#page=12)). Rule/calculation: paired pounds/kg values reconcile after conversion and rounding; the remaining rows are modelled changes, not mutually exclusive category counts. Direct observation: percentage-point medication differences are properly distinguished from patient counts and from the continuous-variable units. Alternative: eTable 8 has no raw treatment-group percentages, so its effects cannot be reverse-computed without unprinted inputs. Human question: none.

### N028 — COMPLETE — no temporary proposal

Printed inputs: eTable 9 prints total observations and distinct-patient counts for six measures, both treatment groups, and years 0/1/2/5/8 ([joi190103supp1_prod.pdf, PDF p. 13](../../../joi190103supp1_prod.pdf#page=13)). Rule/calculation: every total-observation count is at least its distinct-patient count; each distinct-patient count is no greater than the relevant baseline group N. Direct observation: total observations are measurement records, not participant denominators, and no count conflict was observed. Human question: none.

### N029 — COMPLETE — one temporary proposal

Printed inputs and locations: eTable 3 labels matched nonsurgical N=11,435 at the index date; eTable 10 labels its year-0 nonsurgical medication-proportion sample size as 11,433 ([joi190103supp1_prod.pdf, PDF pp. 5, 14](../../../joi190103supp1_prod.pdf#page=5)). Both surgery values are 2,287.

**NUM-P007 — Two supplement tables give different nonsurgical medication denominators at year 0 without a printed reconciliation.**

- **Direct observation:** eTable 3 prints `Matched Nonsurgical (N=11435)` for medication classes at the index date, while eTable 10 prints `Nonsurgical Group 11433` at time since index date 0.
- **Rule and calculation:** Both labels identify nonsurgical medication data at the index date/year 0, yet `11,435 - 11,433 = 2` participants. These are integer denominators, so tolerance is zero absent a stated different population, missing-data exclusion, or timing rule.
- **Inference and alternative:** eTable 10 may intentionally be a complete-case medication-proportion denominator that excludes two participants, whereas eTable 3 may classify all matched controls; neither table prints that reconciliation. The mapping itself is an inference from table labels, not proof of an error.
- **Quality-control relevance:** A two-person denominator difference changes medication proportions and may be propagated by a data extractor who assumes the tables use the same index-date cohort.
- **Human question:** What inclusion, missing-data, or timing rule excludes two nonsurgical controls from eTable 10 at year 0 but not from eTable 3?

### N030 — COMPLETE — no temporary proposal

Printed inputs: eTable 11 gives surgery-only Kaplan-Meier intervention incidences at years 1/2/5/8 and says the abdominal-procedure row excludes hernia repair and cholecystectomy ([joi190103supp1_prod.pdf, PDF p. 15](../../../joi190103supp1_prod.pdf#page=15)). Rule/calculation: each incidence is nondecreasing by time and every CI has ordered endpoints. Direct observation: excluded rows are explicitly not components to add to abdominal procedure. Human question: none.

### N031 — COMPLETE — no temporary proposal

Printed inputs: eFigure 3 contains nutritional trend curves without exact plotted values; eTable 8 supplies numeric treatment-difference estimates ([joi190103supp1_prod.pdf, PDF pp. 12, 16](../../../joi190103supp1_prod.pdf#page=12)). Rule: no figure point can be tested at printed precision. Direct observation: units are g/dL except vitamin D ug/L, as stated by the figure/table context. Human question: none.

### N032 — COMPLETE — no temporary proposal

Printed inputs: sensitivity analysis specifies five index-date samples and three matching ratios, and gives significant-dataset counts 15/15/15/15/15/13/12/11 by endpoint family ([joi190103supp1_prod.pdf, PDF p. 17](../../../joi190103supp1_prod.pdf#page=17)). Rule/calculation: `5 × 3 = 15`; every printed significant-dataset count is an integer from 0 through 15. Direct observation: no count exceeds the named dataset total. Human question: none.

### N033 — COMPLETE — no temporary proposal

Printed inputs: eFigure 4 is a visual panel for 15 datasets without exact point/interval labels ([joi190103supp1_prod.pdf, PDF p. 18](../../../joi190103supp1_prod.pdf#page=18)). Rule: no unprinted point estimate may be compared mechanically to eTable 6 or eTable 7. Direct observation: its stated 5-by-3 construction agrees with N032. Human question: none.

### N034 — COMPLETE — no temporary proposal

Printed inputs: eTable 12 reports endpoint-specific E-values and separately reports comparator HRs for known risk factors; the prose says E-values are on a risk-ratio scale ([joi190103supp1_prod.pdf, PDF pp. 19-20](../../../joi190103supp1_prod.pdf#page=19)). Rule: an E-value is not an HR and must not be numerically equated with the comparator HRs. Direct observation: estimate E-values exceed upper-CI E-values in each row and labels distinguish the measures. Alternative/limitation: the supplied package does not state a numerical HR-to-risk-ratio transformation or enough inputs to reproduce the E-value calculations from the printed HRs; no unsupported formula-based proposal is made. Human question: none.

### N035 — COMPLETE — no temporary proposal

Printed inputs: the protocol defines the primary/secondary composites and individual-outcome risk-set exclusions, including nephropathy rules ([joi190103supp2_prod.pdf, PDF pp. 4-5](../../../joi190103supp2_prod.pdf#page=4)). Rule: individual endpoint risk sets need not equal the composite denominator because baseline cases are excluded. Direct observation: Table 2 individual denominators are less than or equal to the matched group totals and use outcome-specific labels. No direct numeric conflict was found. Human question: none.

### N036 — COMPLETE — no temporary proposal

Printed inputs: protocol p. 6 defines planned rates per 100 patient-years, cumulative incidence, Cox/PH analyses, imputation, multiplicity, and 15-dataset sensitivity analyses ([joi190103supp2_prod.pdf, PDF p. 6](../../../joi190103supp2_prod.pdf#page=6)). Rule: rate, cumulative incidence, and HR are distinct measures and must not be substituted. Direct observation: the supplement reports each with its stated label; planned methods are not an arithmetic identity for every displayed result. Human question: none.

### N037 — COMPLETE — no temporary proposal

Printed inputs: the amendment defines early/late adverse-event timing and E-value procedures for eight endpoints ([joi190103supp2_prod.pdf, PDF p. 7](../../../joi190103supp2_prod.pdf#page=7)). Rule: definitions alone are not participant-flow or count inconsistencies. Direct observation: no final numeric result in this protocol-only page conflicts with the results tables. Human question: none.

### N038 — COMPLETE — one temporary proposal

Printed inputs and location: supplement p. 19 says “eTable 4 displays adjusted hazard ratios and 95% confidence intervals at 2, 5, and 8 years after the index date.” The table immediately below is headed “eTable 7. Time-Varying Hazard Ratios and 95% CIs at 2, 5, and 8 Years ...” and reproduces the time-varying HRs ([joi190103supp1_prod.pdf, PDF p. 19](../../../joi190103supp1_prod.pdf#page=19)); the same eTable 7 appears on p. 10.

**NUM-P008 — Time-varying-HR prose cites eTable 4, but the displayed/repeated result table is eTable 7.**

- **Direct observation:** The prose reference and adjacent table number differ. eTable 4 elsewhere is the cause-specific rate table on PDF p. 6, not the time-varying-HR panel ([joi190103supp1_prod.pdf, PDF p. 6](../../../joi190103supp1_prod.pdf#page=6)).
- **Rule and calculation:** A same-page cross-reference to a table containing 2/5/8-year time-varying HRs should name the table whose heading has that content. Equality/label tolerance is zero: `eTable 4 ≠ eTable 7`.
- **Inference and alternative:** This appears to be a cross-reference label error; it could instead reflect a prior table numbering scheme retained in prose. The source does not establish which intended number is authoritative.
- **Quality-control relevance:** Readers and evidence extractors following the cited table are directed to event rates rather than the stated time-varying HRs.
- **Human question:** Should the p. 19 reference read eTable 7, or was a different eTable 4 intended in an earlier supplement version?

## Completion and limitations

All 38 assigned relationships have an explicit `COMPLETE` record. Temporary proposal count: 8 (NUM-P001 through NUM-P008). The proposals are source-grounded observations, not findings, validity judgments, severity assignments, stable IDs, or dispositions. Key limits are that Figure-only panels lack printed point values; several modelled/bootstrapped quantities lack raw inputs; and the package does not specify the ARD point-estimation rule or the two-participant medication-denominator reconciliation. No `P = 0` display was treated as a proposal.

## Coordinator audit repair — additional source-grounded proposals

The later evidence-quality audit identified two omissions in this completed checker. They are preserved as audit-repair provenance and appended to the stable ledger without altering the original proposal numbering.

- **AUDIT-OMISSION-001 (N022):** DOC-002 p. 5 eTable 3 prints surgery biguanides as 1,530 (67.9%) with N=2,287. `1,530 / 2,287 × 100 = 66.90%`, which rounds to 66.9%, not 67.9%.
- **AUDIT-OMISSION-002 (N005):** DOC-001 pp. 5-6 Table 1 footnote b defines standardized differences as the “absolute value” of the group difference divided by pooled SD, while both columns contain many negative values, including index date -42.6/-15.9 and men -28.0/-2.9.

Both omissions are Pending Human Adjudication and receive stable IDs in `candidate_ledger.md` after direct-source recheck.
