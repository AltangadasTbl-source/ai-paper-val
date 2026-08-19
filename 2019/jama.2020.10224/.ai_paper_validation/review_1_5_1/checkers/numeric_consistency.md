# Numeric Consistency Check

## Scope, method, and boundary

This checker reviewed all 53 numeric/reporting relationships in the canonical inventory: N001-N010, N100-N121, N300-N308, and N500-N511. It used the two canonical extraction maps and numeric/statistical relationship inventories as source locators. Direct-PDF layout text was checked against the supplied source for both proposed inconsistencies: DOC-001 PDF p. 6 and DOC-002 PDF p. 18. No legacy candidate, checker, disposition, or report was used.

Applied checks were arithmetic and partitions; numerator/denominator/percentage reconciliation; missingness and population identity; total/subgroup relations; rate versus count and person-time distinctions; unit, scale, and reference-label consistency; repeated-value and matched-location agreement where the relationship supplied a comparator; and stated rounding. A percentage is treated as reconciled when its printed count/denominator rounds to the displayed precision (normally 0.1 percentage point; explicitly approximate planning language is not tested as an exact equality). Rates per 1,000 person-years are not recomputed without person-time. Planned protocol inputs are not treated as achieved-trial results.

No stable candidate ID, severity, validity, disposition, or correction is assigned here. Each proposition below remains Pending Human Adjudication.

## Relationship-by-relationship outcomes

| Relationship ID | Checks and reproducible outcome | Candidate status / limitation |
|---|---|---|
| N001 | Randomization reconciles: 9,181 + 9,172 = 18,353 and 16,657 + 1,696 = 18,353. Allocation and 5.3-year follow-up agree at DOC-001 pp. 1, 3, 6, and 9. | PASS. |
| N002 | In each arm total events equal incident plus recurrent: 609 = 459 + 150 and 625 = 461 + 164. Counts, denominators, rates, and their labels agree in abstract, Results, and Figure 4 (DOC-001 pp. 1, 6, 8). Person-time is not printed; 12.9/13.3 cannot be reproduced from counts alone. | PASS; rate-reproduction limit. |
| N003 | Incident and recurrent risk sets partition the randomized cohort: 8,350 + 831 = 9,181 and 8,307 + 865 = 9,172. Their all-arm totals are 16,657 and 1,696. Event partitions reconcile as in N002; rates are correctly labelled per 1,000 person-years. | PASS; person-time not printed. |
| N004 | Parent allocation reconciles: 12,927 - 3,746 = 9,181 and 12,944 - 3,772 = 9,172. End-of-intervention counts reconcile: 8,859 + 322 = 9,181 and 8,872 + 300 = 9,172. Exclusion-category sums were not required to equal exclusions because the figure expressly says categories are nonexclusive. | PASS. |
| N005 | Table 1 category checks reconcile at their stated denominators, including age, race available-N, BMI available-N, Charlson, region, and factorial allocation. Percentages agree after 0.1-point rounding; the footnote permits non-100% sums. Units and conversion are stated. | PASS. |
| N006 | Table 2 and Figure 3 use identical group Ns at baseline and years 1-5 (9,181/9,172; 8,534/8,486; 8,381/8,344; 8,176/8,112; 7,763/7,603; 5,316/5,231). Missing repeated outcome values are expressly modelled as missing at random, not a denominator contradiction. | PASS. |
| N007 | Eligibility percentages round correctly: 8,350/9,181 = 90.95% -> 90.9%; 831/9,181 = 9.05% -> 9.1%; 8,307/9,172 = 90.57% -> 90.6%; 865/9,172 = 9.43% -> 9.4%. Completion percentages lack a printed numerator and are not mechanically reproduced. | PASS; completion numerator not printed. |
| N008 | Figure 4 subgroup count identities reconcile where categories partition a stated baseline denominator: sex, age (50-64 is merged), race (other is the specified combined categories), Charlson, vitamin-D use, activity, region, fish-oil allocation, and BMI. Subgroup rates are correctly labelled per 1,000 person-years and cannot be derived without person-time. | PASS; rate-reproduction limit. |
| N009 | Direct source check identifies the unit-label mismatch at DOC-001 p. 6; detailed proposition 1 below. The p. 6 31.1 and p. 9 30.8 ng/mL means need not agree because their populations/summaries are not stated as identical. | PROPOSITION 1; otherwise no cross-summary inconsistency. |
| N010 | Three suicide deaths is a standalone safety count; the repeated 5.3-year follow-up conclusion matches N001. No arithmetic comparator is printed. | PASS / no further applicable identity. |
| N100 | DOC-002 planned frame, dose, sex-age thresholds, and 5-year duration are internally repeated consistently. The 20,000 target is explicitly planned and is not compared as an achieved total. | PASS; planned-versus-observed comparison inapplicable. |
| N101 | 18,200 is explicitly an anticipated eligible population among up to 20,000, not a realized trial denominator. | PASS; planning quantity. |
| N102 | Exact planned partitions reconcile: 10,000 + 10,000 = 20,000; 1,400 + 18,600 = 20,000; 5,000 + 500 + 400 + 80 + 14,020 = 20,000. Race/ethnicity overlap is stated. | PASS. |
| N103 | Nested case-control total and matching ratio reconcile: 500 + 1,000 = 1,500 and 1:2. | PASS. |
| N104 | CTSC random subset n=1,000 at four centres and two stated assessments is a planned design quantity without a conflicting denominator. | PASS. |
| N105 | Composite endpoint components and year 0/1/3/5 schedule are definitions, not mutually exclusive counts. | PASS / no applicable arithmetic identity. |
| N106 | PHQ-8 0-24 scale and its >=10, >=15, and >=20 thresholds are separately defined; the source does not label them as interchangeable. | PASS. |
| N107 | Validation metrics are cited-context values, not additive components or a trial numerator/denominator. | PASS / no applicable identity. |
| N108 | Incident-case sources and earliest-date hierarchy define event timing and person-time; no count total is printed. | PASS / no applicable arithmetic identity. |
| N109 | Both assay CV statements use the explicit less-than-10% threshold; no conflicting unit or denominator is printed. | PASS. |
| N110 | ITT survival follow-up and adjustment labels distinguish an HR from a risk or count. | PASS. |
| N111 | The <2/3 adherence censoring rule is a planned sensitivity definition, not a reported percentage or event total. | PASS. |
| N112 | The planned mixed model distinguishes four assessment times from a treatment-by-time contrast; no displayed coefficient is supplied. | PASS / no applicable numeric identity. |
| N113 | The CTSC two-measure model is a planning definition and is kept distinct from the full cohort. | PASS. |
| N114 | Deficiency thresholds are equivalent as printed: 20 ng/mL x 2.5 = 50 nmol/L. Prevalence is explicitly approximate. | PASS. |
| N115 | Interim z=3 and p=.0027 are a monitoring rule, expressly distinct from final inference. | PASS. |
| N116 | Incident power-table partitions reconcile: 7,244 + 8,226 = 15,470 and 10,071 + 5,399 = 15,470. African-American n=3,868 is labelled a subgroup, so it is not added to the race partition. | PASS. |
| N117 | Recurrent power-table partitions reconcile: 1,856 + 874 = 2,730 and 1,777 + 953 = 2,730. African-American n=683 is a subgroup. | PASS. |
| N118 | 513/855 = 60.0%; 196/855 = 22.9%, consistent with "about 23%". | PASS; approximate planning language respected. |
| N119 | Expected cases, blood-sample subset, control prevalence, and power are explicitly approximate/assumed planning inputs, not observed event risks. | PASS. |
| N120 | Assumed RR, alpha, power, and continuous-outcome percentage differences are scenario inputs, with effect scales explicitly labelled. | PASS. |
| N121 | Direct source check identifies the adjacent table-reference mismatch at DOC-002 p. 18; detailed proposition 2 below. | PROPOSITION 2. |
| N300 | All reported baseline count partitions reconcile at their printed denominators: age, sex, race available-N, Charlson, smoking available-N, alcohol available-N, region, and fish-oil allocation. Count/denominator percentages round to the printed 0.1%; named missingness and available Ns prevent false whole-cohort comparisons. | PASS. |
| N301 | Sex and age subgroup Ns partition 18,353 exactly (9,023 + 9,330; 6,617 + 9,231 + 2,505). Other subgroup totals are availability/category subsets (for example race 17,989, BMI 17,919, vitamin-D status 11,417) and are not asserted to equal randomized N. | PASS; availability definitions limit other partitions. |
| N302 | Sensitivity baseline group Ns equal randomized Ns; later Ns decline under the stated post-antidepressant censoring and response availability. Annual contrasts are adjusted model estimates, so they are not required to equal subtraction of rounded within-group estimates. | PASS. |
| N303 | All pill-adherence percentages reproduce from printed numerators/denominators to 0.1 percentage point, including 8,237/8,688 = 94.8%, 7,793/8,448 = 92.2%, and 4,524/5,036 = 89.8%. Denominators are questionnaire respondents, not all randomized participants. | PASS. |
| N304 | Censoring sensitivity event totals reconcile by arm: 468 = 350 + 118 and 486 = 362 + 124. | PASS. |
| N305 | CVD-censoring sensitivity event totals reconcile: 598 = 453 + 145 and 606 = 446 + 160. | PASS. |
| N306 | Time-dependent-CVD-adjusted event totals reconcile: 609 = 459 + 150 and 625 = 461 + 164. | PASS. |
| N307 | Cancer-censoring sensitivity event totals reconcile: 590 = 445 + 145 and 602 = 441 + 161. | PASS. |
| N308 | Time-dependent-cancer-adjusted event totals reconcile: 609 = 459 + 150 and 625 = 461 + 164. | PASS. |
| N500 | Every listed HR lies within its printed CI. These are modelled sensitivity/narrative associations; exact SEs, person-time, and model details are not supplied for arithmetic reproduction. | PASS; inputs limited. |
| N501 | eTable 8 risk-set identity reconciles: 16,657 + 1,696 = 18,353. Footnotes distinguish composite total from its incident/recurrent components. | PASS. |
| N502 | Time-specific PHQ-8 Ns match main Table 2 at each year. The rate ratio is explicitly a percent difference in severity change, not an event rate, risk ratio, or count. | PASS. |
| N503 | Censored-after-letter sensitivity labels the censoring rule, group Ns, adjusted mean changes, and 5-df interaction separately. Rounded model contrasts are not required to equal rounded arm means. | PASS. |
| N504 | Omit-year-5 sensitivity explicitly changes the averaging window to years 1-4 and separately labels its interaction; it is not compared as the same estimand as the five-year result. | PASS. |
| N505 | Sex-specific risk sets and cases reconcile: men 8,642 + 688 = 9,330 and 426 + 122 = 548; women 8,015 + 1,008 = 9,023 and 494 + 192 = 686. Rates are cases per 1,000 person-years; no person-time is printed. | PASS; rate-reproduction limit. |
| N506 | Randomized-group risk sets and cases reconcile: vitamin D3 8,350 + 831 = 9,181 and 459 + 150 = 609; placebo 8,307 + 865 = 9,172 and 461 + 164 = 625. | PASS; person-time absent. |
| N507 | Vitamin-D-status sample identity reconciles: 10,089 + 1,328 = 11,417. Threshold and continuous scale are distinct and correctly labelled (<20 ng/mL versus per 10 ng/mL). | PASS. |
| N508 | eTable 15 is descriptive mean (SD) material with no printed denominators; it supplies no total, percentage, or rate identity to test. | PASS / denominator not printed. |
| N509 | The eFigure identifies likelihood ratios, CIs, P values, direction, and follow-up averaging; these are neither counts nor risks/rates. Numeric compatibility belongs to the S relationship check. | PASS / no additional N identity. |
| N510 | Historical protocol targets, age changes, approximate CMS linkage, CTSC Ns, ICC, CI, and agreement percentage have distinct contexts; no same-definition repeated result conflicts. | PASS. |
| N511 | Reference and data-sharing pages contain no applicable clinical numeric relationship. | NO APPLICABLE RELATIONSHIP. |

## Relevant inferential-relationship numeric checks

The 35 S relationships were also screened only for the numeric/reporting checks assigned to this stage (denominators, event-count partitions, stated measure/scale, rate-versus-count distinction, CI endpoint order/containment, and exact matched repeated values). Formal test/P/SE compatibility remains assigned to the two statistical passes.

| S ID | Numeric-check outcome |
|---|---|
| S001 | HR 0.97 is within 0.87-1.09; matched counts/denominators are N002; HR is not treated as a risk ratio. PASS. |
| S002 | Both HRs lie within stated CIs; incident/recurrent denominators and event partitions are N003. PASS. |
| S003 | Mean-difference CI contains 0.01; PHQ-8 is explicitly 0-24 points, not a rate. PASS. |
| S004 | Every subgroup HR is within ordered CI; event/participant values are counts and rates are per 1,000 person-years, not proportions. PASS. |
| S100 | Protocol test labels distinguish continuous/categorical methods; no numerical result. PASS. |
| S101 | Planned HR/Cox/Kaplan-Meier labels distinguish time-to-event measures from RR. PASS. |
| S102 | Planned PH-assumption statement has no reported numeric diagnostic. PASS. |
| S103 | Two-sided alpha .05 is distinct from interim p=.0027. PASS. |
| S104 | The <2/3 censoring rule is not a reported adherence percentage. PASS. |
| S105 | Planned four-measure mixed-model statement gives no estimable numeric contrast. PASS. |
| S106 | CTSC two-measure model is distinct from full-cohort population. PASS. |
| S107 | Interaction scale/reference definitions are supplied; no printed result. PASS. |
| S108 | Interim z=3 and p=.0027 are monitoring thresholds, not event risks/results. PASS. |
| S109 | Incident-table percentages are power, not percentages of enrolled participants or risks. PASS. |
| S110 | Recurrent-table percentages are power, not observed risks. PASS. |
| S111 | CTSC/nested case-control power inputs are assumed quantities, not treatment results. PASS. |
| S112 | Interaction RR and added-reduction statements are explicitly assumed effect-scale scenarios. PASS. |
| S113 | Continuous-outcome power lacks absolute mean/SE inputs; no arithmetic comparison is valid. PASS with missing-input limit. |
| S300 | All PHQ-8 subgroup CIs contain their point estimates; subgroup Ns are availability-specific as N301. PASS. |
| S301 | Narrative HRs lie within their CIs and link to the same named risk-subgroup setting; no count partition conflict. PASS. |
| S302 | Censored PHQ-8 contrasts lie within CIs; censoring population is distinct and named. PASS. |
| S303 | Censoring sensitivity HRs lie within CIs; total/incident/recurrent event partition is N304. PASS. |
| S304 | CVD-censoring HRs lie within CIs; event partition is N305. PASS. |
| S305 | Time-dependent-CVD HRs lie within CIs; event partition is N306. PASS. |
| S306 | Cancer-censoring HRs lie within CIs; event partition is N307. PASS. |
| S307 | Time-dependent-cancer HRs lie within CIs; event partition is N308. PASS. |
| S500 | All stated HRs lie within ordered CIs; sensitivity settings keep measures distinct. PASS. |
| S501 | Fine-Gray HRs lie within ordered CIs; competing-risk HR is not compared as a raw risk. PASS. |
| S502 | Six RRs lie within ordered CIs; RRs are modelled repeated-measures effects, not event counts. PASS. |
| S503 | All sensitivity mean differences lie within ordered CIs; 5-df interaction is separate from annual estimates. PASS. |
| S504 | Omit-year-5 mean differences lie within ordered CIs and use a different time window. PASS. |
| S505 | Women-versus-men HR 1.34 lies within 1.19-1.50; comparator uses the sex-specific N505 population. PASS. |
| S506 | HRs and mean differences lie within their ordered CIs; categorical and per-10-ng/mL scales remain distinct. PASS. |
| S507 | Eight likelihood-ratio CIs contain their estimates; likelihood ratio is not a count/rate. PASS. |
| S508 | ICC .63 lies within .59-.67; 86% agreement lacks a printed denominator, so percentage is not recomputed. PASS with denominator limit. |

## Candidate propositions requiring human adjudication

### Proposition 1 — Concentration unit label at the 20-unit threshold

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-001 `jama_okereke_2020_oi_200066.pdf` PDF p. 6, Results—Baseline Characteristics, states: “The mean 25-hydroxyvitamin D level was 31.1 ng/mL and 11.6% of participants had levels lower than 20 mg/mL.” Comparators: DOC-001 PDF p. 4, Table 1, labels 25-hydroxyvitamin D as ng/mL and supplies ng/mL-to-nmol/L conversion; PDF p. 6 immediately preceding sentence says 31.1 ng/mL; PDF p. 8 Figure 4 labels <20 / >=20 ng/mL; PDF p. 9 labels mean baseline 25-hydroxyvitamin D as 30.8 ng/mL.
- **Printed inputs:** `31.1 ng/mL`; `11.6%`; threshold `20 mg/mL`; comparison thresholds `<20 ng/mL` and `>=20 ng/mL`; conversion `ng/mL x 2.5 = nmol/L`.
- **Rule and calculation:** A single 25-hydroxyvitamin-D concentration threshold must retain the stated unit across matched current-study descriptions. If `20 mg/mL` is read literally, it is 20,000,000 ng/mL because 1 mg = 1,000,000 ng; it cannot be the same threshold as 20 ng/mL. This conversion is a diagnostic of label incompatibility, not a proposed corrected value.
- **Tolerance:** None for a dimensional-unit label. Decimal/percentage rounding cannot reconcile mg/mL with ng/mL.
- **Direct observation versus inference:** Direct observation: the p. 6 sentence prints `mg/mL`, while the listed matched locations print `ng/mL`. Inference: the isolated `mg/mL` is likely a unit-label error; the source does not explicitly state its intended replacement.
- **Alternative source-grounded interpretations:** The `mg/mL` text might refer to a different, unstated analytic unit; however the same sentence's 31.1 ng/mL mean and the matched <20 ng/mL categories make that interpretation unsupported by the supplied source. It could be a typographic error, but mechanism is not established.
- **Quality-control relevance:** A data extractor could copy an incompatible vitamin-D threshold unit, changing a biomarker eligibility/subgroup definition by orders of magnitude.
- **Exact human question:** Does the printed `20 mg/mL` on DOC-001 PDF p. 6 require correction or clarification, and if so what unit was intended for that threshold?

### Proposition 2 — Protocol cross-reference names a nonadjacent table

- **Category:** Measure, label, or scale inconsistency (table-reference label).
- **Exact source locations:** DOC-002 `joi200066supp1_prod.pdf` PDF p. 18, prose: “ICD-9 codes will be used to identify depression (Table 3)”; on the same direct PDF page, the immediately following displayed table caption is “Table 1. ICD-9 Codes Identifying Relevant Depressive Disorders.” The inventory's complete protocol transcription locates the actual `Table 3` as the recurrent-depression power table at DOC-002 PDF p. 23.
- **Printed inputs:** prose reference `Table 3`; adjacent caption `Table 1. ICD-9 Codes Identifying Relevant Depressive Disorders`; later Table 3 title, recurrent-depression power table.
- **Rule and calculation:** A textual cross-reference for the ICD-9 code list should identify the table that contains that list. Direct location comparison gives `Table 3 != Table 1`; no numeric rounding tolerance applies.
- **Tolerance:** None for a table-number reference.
- **Direct observation versus inference:** Direct observation: the code-list prose says `Table 3` and its adjacent code-list table says `Table 1`. Inference: the prose cross-reference may be a numbering/citation error; it is not possible to determine from the supplied package whether a prior protocol version used a differently numbered table.
- **Alternative source-grounded interpretations:** The reference may be stale after table renumbering, or “Table 3” may point to an unavailable version. It cannot point to the p. 23 displayed Table 3 for ICD-9 codes because that table is a power table.
- **Quality-control relevance:** A protocol reader or data extractor following the stated reference is directed away from the code-list definition used for depression ascertainment.
- **Exact human question:** Should the DOC-002 p. 18 prose reference to `Table 3` instead identify the adjacent ICD-9 code-list `Table 1`, or is another versioned table intended?

## Non-candidate explanations and limitations

- No relationship was registered merely because a P value was small or displayed at finite precision; there is no display-zero-P proposition in this N scope.
- Protocol N100-N120 quantities are expected, assumed, or planned values and are not numeric comparators for later achieved trial totals without a like-for-like stated comparison.
- Participant-flow exclusions in N004 are explicitly nonexclusive, so their category counts are not tested as a sum.
- Repeated-measures adjusted contrasts (N006, N302-N304, N503-N504) are model outputs; subtracting rounded arm means is an invalid identity unless the source defines that estimand as the raw difference.
- Case rates in N002, N003, N008, N505, and N506 cannot be recomputed because the sources provide event counts and a per-1,000-person-years label but not the relevant person-time totals.
- Available-data and subgroup denominators in N005, N300, N301, and N507 are explicitly population-specific; they do not create missingness inconsistencies merely because they differ from randomized N.
