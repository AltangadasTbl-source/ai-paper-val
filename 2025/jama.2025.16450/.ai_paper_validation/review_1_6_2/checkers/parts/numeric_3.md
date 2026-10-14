# Numeric consistency review: disjoint shard 3

Scope: all 47 assigned relationships in `relationships/parts/assigned_n_3.md`: N726, N727, N728, N729, N730, N731, N732, N733, N734, N735, N736, N737, N738, N739, N740, N741, N742, N743, N744, N745, N746, N747, N748, N749, N750, N751, N752, N753, N754, N755, N756, N757, N758, N801, N802, N803, N804, N805, N806, N807, N808, N809, N810, N811, N812, N813, N814. All are DOC-003 PLAN content. Completed: 47/47 relationships; findings: 1; excluded observations: 3. No participant results, randomized totals, effect estimates, intervals, or P values are printed in this shard. Category codes are not event counts or denominators.

The complete scope and review contract, numeric role preset, source inventory and tooling record were read. Current source-linked mapping and GPU OCR were used as locators; no previous checker, candidate, screening or report conclusion was used. Source images were consulted for the arithmetic displays and the apparent wording observations. The finding was confirmed against a fresh render of the exact supplied PDF page, with the recorded fallback helper and PyMuPDF 1.26.4 on CPU at 200 dpi:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render joi250072supp2_prod_1761000786.6938.pdf --page 152 .ai_paper_validation/review_1_6_2/preprocessing/numeric_3_source_p152.png
```

Derivative: `preprocessing/numeric_3_source_p152.png`. Its printed factor, all comparator cells and the lookup instructions match the source-linked mapping. Arithmetic was checked with JavaScript interval calculations, without Python scientific orchestration.

## Relationship completion inventory

Each row records the source-grounded applicability of the numeric checks. COMPLETE means the assigned relationship was checked; an absence of realized counts is an applicability statement, not an excluded observation.

| Relationship | DOC-003 PDF page | Numeric check and outcome | Status |
|---|---|---|---|
| N726 | 86 | Five family digits plus one birth-order digit yield six-digit identifiers. Both examples have six digits and an allowed initial digit. Identifiers do not represent participant totals. | COMPLETE |
| N727 | 87 | 68875 plus birth-order suffix 1 gives 688751. Masked courses are left blank, with later known clinical courses recorded separately; no course total is printed to reconcile. | COMPLETE |
| N728 | 88 | Parity counts pregnancies rather than fetuses. First twin pregnancy parity 1 and following pregnancy parity 2 reconcile. Completed maternal years and unmasked course rules contain no observed counts. | COMPLETE |
| N729 | 88 | Marital codes 1, 2 and 6 are nominal labels, not an exhaustive numeric sequence or total. No count/percentage pair is printed. | COMPLETE |
| N730 | 89 | Education, insurance and ethnicity codes define categories; multiple insurance responses are allowed, so category identifiers are not additive totals. | COMPLETE |
| N731 | 90 | Race codes 1–7 and anthropometric unit alternatives are specified. No observed race counts or unit-conversion pair is printed. | COMPLETE |
| N732 | 90 | Fetuses include live and stillborn; early reductions before 14 weeks are excluded. No reported multiple-birth total is printed. | COMPLETE |
| N733 | 91 | Limited versus adequate prenatal care use complementary visit/start-time rules; no visits belongs to its explicit separate category. Unknown gestational days are not assigned zero. | COMPLETE |
| N734 | 91 | Diabetes and treatment codes are nominal hierarchy labels; gaps in code sequence do not imply omitted participant counts. | COMPLETE |
| N735 | 92 | Gestational-diabetes treatment hierarchy matches N734. Hypertension and obstetric timing thresholds define ascertainment, with no printed count to recompute. | COMPLETE |
| N736 | 93 | Date/time and >18-hour ROM rules distinguish known and estimated duration. No paired dates or realized duration is supplied. | COMPLETE |
| N737 | 93 | Two betamethasone or four dexamethasone doses, predelivery-only counting and at least 24 hours define completion; no participant dose/course total is printed. | COMPLETE |
| N738 | 94 | Predelivery 72-hour antibiotic and 12-hour monitoring windows and delivery codes are prospective definitions, with no realized numerators or denominators. | COMPLETE |
| N739 | 94 | Birth calendar day counts as day 1 and next calendar day as day 2; matches the support-day convention in N808. | COMPLETE |
| N740 | 95 | Early mortality threshold is ≤12 hours, matching N744 and N806. Sex/diagnosis/gestational-age codes are not participant totals. | COMPLETE |
| N741 | 96 | Apgar times 1, 5 and 10 minutes and FiO2 >.21 support definition contain no computed scores or participant counts. | COMPLETE |
| N742 | 96 | Cord-delay bins distinguish <30 seconds, 30–60 seconds, >1–3 minutes and >3 minutes; unit boundaries reconcile. Birthweight unit is grams. | COMPLETE |
| N743 | 97 | Anthropometry within 72 hours and alternative temperature units define collection. No numeric Celsius/Fahrenheit pair or conversion result is printed. | COMPLETE |
| N744 | 98 | NG03 through status/day 120, NG03E for ≤12-hour deaths and NG05 for >120-day hospitalization partition the specified form use. Seven-day return rule is an observation boundary, not a realized follow-up count. | COMPLETE |
| N745 | 99 | Transfer counts are continued from an explicitly supplied end date; time points not yet reached remain blank. No realized transfer/day/course total is supplied. | COMPLETE |
| N746 | 100 | Status codes and seven-day growth measurement window do not print count/denominator pairs. Transfer rule agrees with N744. | COMPLETE |
| N747 | 101 | Final transfer outcomes and discharge medication fields are categorical; no one-year survival count is supplied. | COMPLETE |
| N748 | 102 | Milk codes match N807. Death ascertainment selects one underlying cause; numeric cause codes are category identifiers, not event counts. | COMPLETE |
| N749 | 102 | Status and 36-week ±7-day anthropometry are defined; there are no measurements or totals to recompute. The separate respiratory-weight window in N809 is a different field. | COMPLETE |
| N750 | 103 | Grams and centimeters are explicit. No growth-score formula or calculated growth result is printed. | COMPLETE |
| N751 | 103 | Surfactant type/route codes match N806. Masked exposure routes to N727; no randomized dose or treated count is printed. | COMPLETE |
| N752 | 104 | Pulmonary complication fields define Y/N ascertainment; no event count, total or percentage is printed. | COMPLETE |
| N753 | 104 | >one steroid course and >14-day exposure thresholds are explicit; no realized course/day totals are printed. Masked clinical treatment rules are separately specified. | COMPLETE |
| N754 | 105 | PDA and treatment fields are Y/N classifications; failed catheter closures are expressly included. No numerical PDA denominator or event total is printed. | COMPLETE |
| N755 | 106 | Two PDA-treatment 24-hour vasoactive windows use the same rule for catheter and surgical closure. First-24-hour hypotension and first-week echo fields have no observed counts. | COMPLETE |
| N756 | 107 | Late pulmonary hypertension, first-24-hour indomethacin and EEG seizures are ascertainment fields, not numerical results. | COMPLETE |
| N757 | 107 | First-28-day imaging and most-severe/earliest-tie rules define aggregation. Multiple independent findings may coexist; their sum is not required to equal an infant total. | COMPLETE |
| N758 | 108 | Grades I–IV map to specified independent findings; grade III maps to two fields without representing two infants. No grade-specific event counts are printed. | COMPLETE |
| N801 | 111–112 | Parenteral calendar days, zero for no exposure, 120 ml/kg/day using current weight and first-feed majority are explicit. No dose/weight pair or total days is supplied. Milk wording observation is recorded below. | COMPLETE |
| N802 | 116 | Hemoglobin or hematocrit is entered, not both; units and first-14-day bilirubin window are explicit. No transfusion count or laboratory pair is supplied. | COMPLETE |
| N803 | 117–118 | Days 1–4 and 5–7 partition week 1, followed by weeks 2–6. Maximum/minimum values and dates are blank collection specifications. | COMPLETE |
| N804 | 120 | Infection codes 4–12 label diagnoses; they are not observed diagnosis counts. | COMPLETE |
| N805 | 121 | Six paper entries versus ten accepted electronic entries explicitly describe different storage capacities, not conflicting observed procedure totals. | COMPLETE |
| N806 | 122 | Early-death surfactant/route codes agree with N751, and ≤12-hour death field routing agrees with N740/N744. Albumin concentrations are treatment descriptors, not randomized doses. | COMPLETE |
| N807 | 124, 127 | Late-status grams/centimeters and within-seven-day collection are explicit. Discharge milk types 1–4 agree with N748. | COMPLETE |
| N808 | 129 | Day-7 example 4 + 2 + 1 = 7 reconciles with exclusive highest-mode counting. FiO2 1.00 exceeds .27 and its paired 0.03 LPM is correctly retained. | COMPLETE |
| N809 | 130 | Days 2–4, 6–8, 12–16 and 26–30 contain target days 3, 7, 14 and 28. Respiratory weight windows 36–37 and 40–41 weeks serve separate measurement fields; no realized time-point totals are printed. | COMPLETE |
| N810 | 141–142 | Procedure identifiers label GI, pulmonary, CNS and ROP events. ROP exclusions and category codes do not impose numeric row/column totals. | COMPLETE |
| N811 | 151 | Certification scenarios have unselected answers and hypothetical values. They are not participant results; no numerator/denominator or answered classification conflicts. | COMPLETE |
| N812 | 152 | All 144 factor cells checked against the reproducible min(100,100×flow/weight) pattern with half-unit intervals. One cell qualifies; the other 143 reconcile under that rule. | COMPLETE |
| N813 | 154 | All 336 effective-oxygen cells checked against the reproducible 21 + factor×(concentration−21)/100 pattern. Five remaining interval gaps are below 0.05 relative discrepancy; no qualifying cell. | COMPLETE |
| N814 | 154–155 | Printed lookup example 2.0 kg/0.15 LPM gives factor 8; factor 8/100% gives 27%, which is less than 30%. Missing saturation detail is recorded below. | COMPLETE |

## Findings

### F-NUM-2001

**Title:** A nasal-cannula factor lookup cell does not reproduce the relationship supported by the other cells.

**Relationships:** N812; N813 supplies the downstream lookup meaning. Proposed relationship type: `P_P`; all relationships: `P_P`.

**Exact source locations and document roles:** PLAN [DOC-003 PDF page 152, Appendix J, Table 1, flow 0.125 LPM (alternate label 1/8 LPM), weight 2.5 kg](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=152); PLAN the other cells of the same Table 1; PLAN [DOC-003 PDF page 154, Table 2, factors 4 and 5 at 100% concentration](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=154) supplies the consequence of selecting the factor. The Table 1 discrepancy itself is entirely within PLAN content.

**Printed inputs:** Table 1 prints factor **4** at flow **0.125 LPM / 1/8 LPM** and weight **2.5 kg**. In the same 2.5-kg column, factors at flows 0.15, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5 and 2.0 LPM are respectively 6, 10, 20, 30, 40, 50, 60 and 80. Higher flow cells cap at 100. Table 1 instructs use of the nearest tabulated flow and weight, rounding exact midpoint inputs upward. Table 2 prints effective oxygen 24% for factor 4/100% and 25% for factor 5/100%.

**Rule and calculation:** The method `factor = min(100, 100 × flow LPM / weight kg)` reproduces all other 143 Table 1 cells under the workflow display-precision rule, including every other cell of the same weight column. This is a method evidenced by this display, not an asserted external physiologic formula. At the disputed nominal inputs it gives `100 × 0.125 / 2.5 = 5`. Allow flow its half-unit interval [0.1245, 0.1255] and weight [2.45, 2.55]. The recomputed factor interval is [100×0.1245/2.55, 100×0.1255/2.45] = **[4.88235294, 5.12244898]**. The printed factor 4 has interval **[3.5, 4.5]**. The gap is **0.38235294**, and the relative discrepancy is **0.38235294/4 = 0.09558824**, above 0.05. Treating the alternate 1/8 flow as exact would not remove the discrepancy.

**Focus area:** C, numerical method logic for the planned oxygen lookup; D, a calculation used in the planned physiologic BPD assessment.

**Proposed review domain:** `plan_material`.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** The factor selected for a 2.5-kg infant receiving 0.125 LPM nasal-cannula oxygen, and the effective FiO2 derived from that factor. At 100% source oxygen the displayed lookup selects 24%, whereas factor 5 selects 25%. This card does not assert that an actual infant's outcome or eligibility changed; no participant-level use of this cell is supplied.

**Why context does not resolve it:** Route A category 4 applies because the printed result does not reproduce under a method that reproduces the other rows and cells of the same display beyond the required relative-discrepancy threshold. An unstated distinct calculation for this cell is an alternative to ask about, rather than grounds to suppress the finding as conditional or peripheral. The nearest-input instructions do not resolve an exact tabulated input cell.

**Source-grounded alternatives and missing definition:** The table may intentionally use a cell-specific factor-generation method, but it supplies no algebraic derivation or explanation of an exception at these inputs. The printed lookup itself may be the intended operational rule regardless of the surrounding proportional pattern. The other 0.125-LPM cells and the adjacent same-weight cells support the reproduced relationship but do not authorize substituting a final value.

**Exact human question:** What factor-generation method produces the printed factor 4 at 0.125 LPM (1/8 LPM) and 2.5 kg while producing the other Table 1 values, and which factor should be used for this exact tabulated input when calculating effective FiO2?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN [DOC-003 p152 Table 1](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=152), 0.125 LPM/4 kg; PLAN [DOC-003 p154 Table 2](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=154), factor/concentration pairs 15/40%, 25/40%, 27/40%, 31/50%, 31/100% | Apparent departures from the same-display arithmetic patterns are screened together by the precision rule. Table 1's nominal 3.125 versus printed 4 overlaps after half-unit input intervals [2.7667,3.5857] versus [3.5,4.5]. Table 2, using 21 + factor×(concentration−21)/100, yields intervals [23.6825,24.0225], [25.5325,25.9725], [25.9025,26.3625], [29.6925,30.2925], [44.9425,46.0425], compared with printed 23,25,25,31,47. Remaining gap/printed-value ratios are 0.007935,0.001300,0.016100,0.006694,0.009734; all are at most 0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN [DOC-003 p111 J2d](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=111) | Human-milk instructions say to code all types but describe maternal/donor options with “only,” and the none option includes feeding-trial wording. This is wording in a generic collection field, with no printed count/percentage, changed prespecified outcome status, or conflicting primary analysis statement. No numerical result is reproduced from it. | TERMINOLOGY_OR_WORDING |
| PLAN [DOC-003 pp154–155 example and answer](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=155) | The example calls the infant eligible based on the 27% lookup but supplies no saturation readings. The lookup arithmetic reconciles. A challenge-eligibility conflict would require assuming the infant's unreported saturation values; none is printed. | CONDITIONAL_OR_UNREPORTED |

## Limitations

No scientific coverage gap remains within the 47 assigned relationships. Font-mangled native text means OCR and mapped transcriptions served as locators; source images remain authority. The lookup equations are supported by the printed numerical patterns but are not explicitly supplied as algebraic formulas. That missing factor-generation definition is retained in the finding's human question. No raw participant data are supplied to determine whether the factor cell was used or whether any outcome classification changed. Statistical and cross-source relationships outside this disjoint N assignment belong to their separately assigned review stages.
