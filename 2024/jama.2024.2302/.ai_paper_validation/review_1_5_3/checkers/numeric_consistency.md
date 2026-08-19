# Numeric Consistency Review

## Scope

This review checked all 41 package-wide numeric relationships in `relationships/numeric_relationship_inventory.md` (`N001`-`N041`). It applied arithmetic, total, subgroup-sum, numerator/denominator/percentage, missingness, population, rounding, measure/label/scale, unit, reference direction, rate/risk/proportion/count, repeated-value, and applicable cross-source checks. Inferential compatibility beyond the printed numeric inputs remains assigned to the separate statistical passes. No legacy DOCX assertion was read or used.

## Rules and rounding tolerance

- Counts and mutually exclusive displayed components must sum exactly unless the source explicitly says that reasons overlap or events may occur more than once per infant.
- For a printed whole percentage, the accepted rounding interval is the conventional nearest whole-percent interval of ±0.5 percentage points; for a printed one-decimal percentage, ±0.05 percentage points. A percentage without a printed denominator is not reverse-engineered as a discrepancy.
- A modeled or adjusted risk difference/RR is not required to equal crude arithmetic from the displayed event counts when the source labels a model and adjustment. Medians are not totals or means.
- Values in distinct analysis populations, time windows, models, interval types, or precision formats are not treated as conflicting until those labels match.

## Complete relationship check record

| IDs | Checks and reproduced calculation/observation | Result |
|---|---|---|
| N001 | 172 + 166 = 338. | Reconciles. |
| N002 | The 320 operative-repair statement has no same-window operative-flow total explicitly labeled as its comparator. It must not be forced to equal a treatment-as-randomized branch total. | No candidate; population/time definition absent for a direct identity test. |
| N003, N019 | 44/159 = 27.673% → 28%; 27/149 = 18.121% → 18%; 159 + 149 = 308. Table/abstract/Key Points agree. Figure 3's −0.08 (−0.17 to 0.002) is compatible with Table 2's more rounded −7.9% (−16.9% to 0) after converting proportions to percent and allowing displayed precision. | Reconciles. |
| N004, N020 | Abstract and Table 2 both print early 19.0 (9.8-35.0), late 16.0 (7.0-38.0), days; secondary RR is labeled as a count-model measure, not a crude ratio of medians. | Reconciles. |
| N005-N006, N010 | 10-month window, infant-level outcome, 55-week threshold, GA <37, and timing labels are internally distinct and correctly retained. | Reconciles/no arithmetic identity applicable. |
| N007 | 442 + 734 = 1176; 1176 + 338 = 1514; 613 + 54 + 37 + 14 + 16 = 734. The seven listed not-eligible reasons total 474, but Figure 1 footnote permits more than one reason per infant, so they are not mutually exclusive components of 442. | Reconciles; no false subgroup-sum candidate. |
| N008 | 147 + 11 + 5 = 163; 163 + 9 = 172; 163 − 4 = 159. The seven/two subcategories of the nine protocol deviations total nine. | Reconciles. |
| N009 | 90 + 28 + 39 = 157; 157 + 9 = 166; 157 − 8 = 149. The 39 stated reasons total 13 + 11 + 8 + 5 + 2 = 39. | Reconciles. |
| N011, N026 | 338/1072 = 31.53% → 32%; 613/734 = 83.52% → 84%; (172−9−4) + (166−9−8) = 159 + 149 = 308. | Reconciles. |
| N012-N015 | Sex: 141+22=163, 133+24=157. Race: early 5+49+1+99+18=172; late 3+51+0+101+11=166. Ethnicity: early 28+135+9=172; late 26+135+5=166. Stated missingness gives apnea 137/162=84.57%→85% and 122/155=78.71%→79%; bradycardia 72/162=44.44%→44% and 70/156=44.87%→45%; IVH 11/162=6.79%→7%. GA categories: 103+60=163 and 104+53=157. | Reconciles; denominators explicitly differ by footnote and are not mixed. |
| N016 | 147 + 5 = 152; 152 + 11 = 163; 152/163=93.25%→93%; 62/147=42.18%→42%; 146/147=99.32%→99%. | Reconciles. |
| N017 | 17+4+2+5=28; 47/129=36.43%→36%; 127/129=98.45%→98%; the five pre-55-week reasons total 39. | Reconciles. |
| N018 | Procedure times are medians in minutes; `>58%` and orchiopexy percentages lack printed numerators/denominators. | No candidate; no denominator identity is stated. |
| N021 | Readmission 35/159=22.01%→22% and 42/149=28.19%→28%. These are infants/readmitted proportion labels, not person-time rates. | Reconciles. |
| N022-N024 | Table 3 percentage checks: 28/159=17.61%, 9/149=6.04%, 6/159=3.77%, 5/159=3.14%, 4/149=2.68%, 2/159=1.26%, 3/149=2.01%, 1/159=0.63%, and analogous listed event rows round as printed. The table expressly permits more than one SAE per infant; events therefore need not sum to 44/27. Narrative two early intestinal injuries matches Table 3 adjacent-structure injury 2. | Reconciles. |
| N025 | Incarceration 2+6=8 and reoperation 2/3 agree with Table 3. Clinical-resolution percentages cannot be checked against a stated same-population denominator; the text does not label one. | Reconciles where identity applies; no candidate for an unstated denominator. |
| N027-N028 | Pages contain no result-relevant numeric relationship. | No applicable check. |
| N029, N034 | Protocol repeatedly labels its primary endpoint as infants with `>1 SAE`; this is evaluated against later same-study `≥1/any/at least one` labels below. 30%−20%=10 percentage points; 1/0.10=10, so NNH 10 follows the printed design contrast. | One candidate below; otherwise reconciles. |
| N030, N033, N036 | Protocol p. 3 prints hospital-day medians 18/15. Protocol p. 12 prints median 8/5 (and means 18/13); SAP p. 3 explicitly calls p. 3's 18/15 medians incorrect and states the p. 12 values are correct. | One candidate below. |
| N031 | Pilot late group N=20, with 8 unrepaired, supplies the printed operative-event denominator 12. 4/19=21.05%, 5/19=26.32%, 9/19=47.37%, 2/12=16.67%, and 6/12=50%. | Reconciles. |
| N032, N038 | Protocol/SAP use `<28`/`>28` in some planned-stratum wording, while the final article uses `<28`/`≥28`. No reported final numeric result is paired with the former wording, and source records do not establish how exactly-28-week infants were classified in those planning versions. | No candidate; unresolved label history without a concrete reported-number contradiction. |
| N035 | Interim thresholds are `>95%` efficacy and `>90%` harm; the reported 97% is greater than 95%. Accrual quantities are planned schedules rather than components of an observed total. | Reconciles. |
| N037 | mITT/PP and total-hospital-day definitions distinguish population and measure; no numeric comparator carrying the same labels contradicts them. | Reconciles/no arithmetic identity applicable. |
| N039 | eTable 1: 280+196+71+66=613; 14+14+9=37; 4+4+3+2+1+1+1=16. The detailed associated-factor entries sum to 51, matching the Figure 1 displayed component; Figure 1's 442 has an explicit multiple-reasons qualifier. | Reconciles. |
| N040 | 44/159=28% and 27/149=18%. Frequentist RD −9.0% need not equal crude −9.55% because eTable 2 labels an adjusted model. Hospital-day outcome is a negative-binomial count model and its RR is not a ratio of medians. | Reconciles. |
| N041 | The 39 early centre counts sum to 172; the 39 late counts sum to 166; row early+late=overall throughout (for example Arkansas 16+17=33; Iowa 11+13=24). Percentages are consistent with denominators 172, 166, and 338 to shown precision. | Reconciles. |

## Pre-ID numeric candidates requiring human adjudication

### Candidate N-CAND-01 — Conflicting planned median hospital-day values within the protocol/SAP record

- **Category:** Numeric or arithmetic inconsistency; Measure, label, or scale inconsistency.
- **Exact source locations:** [PDF-002 p. 3](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=3>), Specific Aims, lines 105-109 in fresh page text; [PDF-002 p. 12](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=12>), Statistical Analysis Plan, lines 454-462; [PDF-003 p. 3](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=3>), Secondary Hypotheses, lines 73-80.
- **Printed inputs:** PDF-002 p. 3: a “3 day reduction in the median total number of hospital days” is parenthetically defined as “18 hospital days for early IH repair versus 15 for late IH repair.” PDF-002 p. 12: the same 3-day median difference is assumed as “median=8, mean=18 for early group and median=5, mean=13 for the late group.” PDF-003 p. 3 says that the original protocol's expected *median* values of 18 and 15 “is incorrect” and that the correct values are 8 and 5.
- **Direct observation:** The supplied protocol prints two different pairs as the planned **median** total hospital days for the same early-versus-late 10-month outcome: 18/15 and 8/5. The SAP directly identifies the former as incorrect.
- **Reproducible rule and calculation:** Match outcome (total hospital days), contrast (early versus late), and stated summary (median). Under the rule that one planned median value per arm is used for this design assumption, compare (18,15) with (8,5): early difference = 18−8=10 days and late difference = 15−5=10 days. Both pairs preserve a 3-day contrast, so the conflict is the arm-specific values/scale, not the arithmetic difference.
- **Tolerance:** Exact for explicitly printed integer medians; no rounding tolerance can reconcile a 10-day difference.
- **Inference boundary:** The conflict and SAP correction are direct observations. The cause (a wording, copy, or analysis-plan version error) is not established and is inference only.
- **Alternative source-grounded interpretations:** The p. 3 pair may have intended *mean* values or may be an earlier design value retained after revision; p. 12 may distinguish median from mean correctly. Neither alternative removes the fact that p. 3 explicitly calls 18/15 the medians in the supplied final protocol.
- **Quality-control relevance:** A reader extracting planned hospital-stay assumptions, power inputs, or the meaning of the 3-day target could copy incompatible arm-level values.
- **Exact human question:** Which pair—18/15 or 8/5—was the intended planned **median** total hospital-day assumption in the final protocol, and should PDF-002 p. 3 be corrected or version-qualified?

### Candidate N-CAND-02 — Primary-outcome event threshold is printed as `>1 SAE` in protocol/SAP locations but as `≥1`/`any` in the analyzed result

- **Category:** Denominator, proportion, or total inconsistency; Measure, label, or scale inconsistency.
- **Exact source locations:** [PDF-002 p. 2](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=2>), lines 55-58 and 80-81; [PDF-002 p. 3](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=3>), lines 97-102; [PDF-002 p. 11](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=11>), line 392; [PDF-003 p. 2](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=2>), lines 49-50 and 67-69; [PDF-003 p. 4](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=4>), lines 132-135; [PDF-003 p. 7](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=7>), lines 238-240; [PDF-001 p. 6](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6>), Table 2 and Primary Outcome; [PDF-004 p. 5](<../../../joi240020supp3_prod_1710443209.75411.pdf#page=5>), eTable 2.
- **Printed inputs:** Protocol and some SAP objective/hypothesis text say “proportion of infants with `>1 SAE`.” The SAP analysis framework says “proportion of children with `≥ 1 SAE`,” SAP p. 7 says “whether an infant experienced any SAEs,” the main Table 2 says “Had ≥1 serious adverse event,” and eTable 2 says “Infant had > 1 SAE” while reporting the same 44/159 and 27/149 analyzed primary-result counts.
- **Direct observation:** The supplied documents use mathematically different threshold symbols/phrases—`>1` (more than one event) and `≥1`/“any” (one or more events)—for the matched primary endpoint. The main/eTable result counts are matched by population and contrast but their label differs.
- **Reproducible rule and calculation:** For nonnegative integer SAE count (x), `x > 1` means (x≥2), whereas `x≥1` means one or more. The set difference consists of infants with exactly one SAE. Therefore these labels are not algebraically interchangeable without an explicit editorial convention or evidence that no infant had exactly one SAE. The package supplies neither.
- **Tolerance:** None: the issue is an integer threshold/operator and outcome definition, not a rounded numerical display.
- **Inference boundary:** Conflicting printed threshold labels are directly observed. Whether `>1` was used informally to mean “at least one,” and whether the analyzed 44/27 counts actually use the `≥1` definition, require inference/human confirmation.
- **Alternative source-grounded interpretations:** Repeated “any,” “at least one,” and `≥1` language in the SAP and main article supports a likely typographical/operator error in the `>1` instances. Conversely, the repeated `>1` wording in the protocol and eTable 2 means a reader cannot resolve the endpoint definition from one location alone.
- **Quality-control relevance:** The threshold determines the numerator of an infant-level primary proportion and could alter data extraction, replication, or comparison of the primary endpoint across the protocol, SAP, main article, and supplement.
- **Exact human question:** Did every reported primary analysis count infants with at least one SAE, and should all `>1 SAE` endpoint labels in the protocol/SAP/eTable be corrected to `≥1 SAE` (or otherwise version-qualified)?

## Result and limitations

- **Relationships checked:** 41 of 41 numeric/reporting relationships.
- **Distinct pre-ID candidates:** 2.
- **Not candidates:** Differences in model-adjusted versus crude measures, separately labeled Bayesian versus frequentist results, explicit rounding/precision differences, events allowed to recur per infant, and values lacking a common stated denominator/time window were retained as checked non-candidates.
- **Limitations:** This reviewer did not assign stable C IDs, severity, validity, or disposition. Exact identities of infants with one versus multiple SAEs and the editorial/version history of the protocol/SAP are not supplied. Statistical interval/test compatibility is reserved for the two statistical-review stages.
