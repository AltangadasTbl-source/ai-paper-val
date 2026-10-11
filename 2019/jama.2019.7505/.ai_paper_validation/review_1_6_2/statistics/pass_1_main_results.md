# Statistical pass 1: main results shard

Runtime: 01a12959-b34f-7793-ae97-9dece6336e61; model gpt-6.1-sol; high effort; fresh spawn. Scope: S001–S101, 101 records. REPORT DOC-001, PDF pp. 1, 7–10 and matched narrative pp. 8–12. The source evidence and each exact tuple are preserved in extraction/main_part_2_intraoperative.md and extraction/main_part_3_outcomes_subgroups.md; these are new maps, not old review conclusions. Direct-source Poppler 26.01.0 layout extraction additionally confirmed pp. 1, 4, 7–10 in preprocessing/statistics_pass_1/main-N.txt. Existing rendered pp. 1, 7–10 were read visually. CPU; historical render engine unrecorded. No new rendering or OCR.

Checks covered point containment, endpoint order, direction, confidence/test compatibility, count/denominator implications and all matching text/figure occurrences. Table 2 variable-specific mean denominators and distribution-specific tests are absent; no equal-variance test, available-case denominator, or median-difference estimand is assumed. Table 3 states Wald approximation for risk-ratio intervals and chi-square for P values; different stated analyses are alternatives, not a reason to exclude a null/interval conflict. A subgroup interaction P is not treated as a within-subgroup main-effect P. No noninferiority or equivalence claim/margin is present.

| S ID | Result checked and explicit outcome | Pass 1 |
|---|---|---|
| S001 | Tidal volume after intubation: ordered CI contains estimate and zero; .15 nonsignificant. Mean rounding can reconcile zero difference. | PASS_1_COMPLETE |
| S002 | Tidal volume first hour: CI 0–0.2 contains null with P .007; F-ST1-002. | PASS_1_COMPLETE |
| S003 | Tidal volume last hour: CI 0–0.2 contains null with P .008; F-ST1-002. Rounded means do not identify available-case contrast. | PASS_1_COMPLETE |
| S004 | Initial PEEP: positive ordered containing CI and P <.001 agree; intervention orientation agrees. | PASS_1_COMPLETE |
| S005 | First-hour PEEP: CI 7.9–8.0 contains 7.9, positive test agrees; means and narrative match with rounding. | PASS_1_COMPLETE |
| S006 | Last-hour PEEP: positive ordered containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S007 | Recruitment: percentage-point contrast, ordered CI and P <.001 agree; low rescue 11 patients matches text. | PASS_1_COMPLETE |
| S008 | Initial peak pressure: positive containing CI, P <.001 and narrative higher-high agree. | PASS_1_COMPLETE |
| S009 | First-hour peak pressure: positive containing CI, P <.001 and figure direction agree. | PASS_1_COMPLETE |
| S010 | Last-hour peak pressure: positive containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S011 | Initial driving pressure: negative containing CI and P <.001 agree with high-minus-low. | PASS_1_COMPLETE |
| S012 | First-hour driving pressure: negative containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S013 | Last-hour driving pressure: negative containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S014 | Initial respiratory rate: negative CI excludes zero and P <.001 agrees. | PASS_1_COMPLETE |
| S015 | First-hour respiratory rate: CI includes zero and P .09 agrees. | PASS_1_COMPLETE |
| S016 | Last-hour respiratory rate: CI −0.7 to 0 includes null with P .02; F-ST1-002. | PASS_1_COMPLETE |
| S017 | Initial FIO2: CI includes zero and P .27 agrees; fractional unit distinct from supplement percent. | PASS_1_COMPLETE |
| S018 | First-hour FIO2: negative containing CI and P <.001 agree; rounded group means insufficient for precise difference. | PASS_1_COMPLETE |
| S019 | Last-hour FIO2: negative containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S020 | Initial SpO2: positive containing CI and P <.001 agree; rounded means can yield 0.7. | PASS_1_COMPLETE |
| S021 | First-hour SpO2: positive containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S022 | Last-hour SpO2: positive containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S023 | Initial end-tidal CO2: CI includes zero and P .09 agrees. | PASS_1_COMPLETE |
| S024 | First-hour end-tidal CO2: positive CI and P .01 agree. | PASS_1_COMPLETE |
| S025 | Last-hour end-tidal CO2: positive CI and P .004 agree. | PASS_1_COMPLETE |
| S026 | Initial heart rate: containing CI crosses zero and P .38 agrees; printed Heat wording excluded. | PASS_1_COMPLETE |
| S027 | First-hour heart rate: containing CI crosses zero and P .36 agrees. | PASS_1_COMPLETE |
| S028 | Last-hour heart rate: negative containing CI and P .02 agree. | PASS_1_COMPLETE |
| S029 | Initial mean arterial pressure: positive containing CI and P .03 agree. | PASS_1_COMPLETE |
| S030 | First-hour mean arterial pressure: containing CI crosses zero and P .87 agrees. | PASS_1_COMPLETE |
| S031 | Last-hour mean arterial pressure: containing CI crosses zero and P .81 agrees. | PASS_1_COMPLETE |
| S032 | Head-elevation partition: both categories exhaust 989/987; global P .70 is not a category-specific P. | PASS_1_COMPLETE |
| S033 | Noninvasive ventilation: counts/percentages and RD agree within precision; containing CI crosses zero and P .64 agrees. | PASS_1_COMPLETE |
| S034 | Anesthesia partition: totals 989/987; global P .51 and no interval; no separate-category test inferred. | PASS_1_COMPLETE |
| S035 | Epidural: count-based RD and printed CI/P .92 agree. | PASS_1_COMPLETE |
| S036 | Epidural location: denominators 80/81 and category totals agree; global P .81, no separate estimates. | PASS_1_COMPLETE |
| S037 | Neuromuscular blockade: CI crosses zero and P .08 agrees; count-based RD reconciles. | PASS_1_COMPLETE |
| S038 | Monitoring: fractions reproduce RD −1.8, but percentages imply −2.8; F-ST1-003. CI/P .40 agree about nonsignificance. | PASS_1_COMPLETE |
| S039 | Reversal: fractions reproduce positive RD about 0.25, but percentages imply −0.9; F-ST1-003. CI/P .90 agree about nonsignificance. | PASS_1_COMPLETE |
| S040 | Total fluids: CI contains .02 and zero; P .79 agrees. Median difference is not substituted for unspecified contrast. | PASS_1_COMPLETE |
| S041 | Crystalloids: CI contains zero estimate and null; P .97 agrees. | PASS_1_COMPLETE |
| S042 | Colloid volume: CI contains .05 and zero; P .50 agrees; supplement volume includes nonrecipients, not substituted for conditional median. | PASS_1_COMPLETE |
| S043 | Colloid receipt: count-based RD 1.8 and CI/P .09 agree within precision. | PASS_1_COMPLETE |
| S044 | Urine output: CI contains −.02 and zero; P .16 agrees; contrast is not assumed a difference of medians. | PASS_1_COMPLETE |
| S045 | Packed cells: count-based RD and containing CI/P .14 agree. | PASS_1_COMPLETE |
| S046 | Plasma: count-based RD and containing CI/P .58 agree. | PASS_1_COMPLETE |
| S047 | Platelets: equal counts, zero RD, containing CI and P >.99 agree. | PASS_1_COMPLETE |
| S048 | Albumin: RD agrees with counts; containing CI crosses zero and P .14 agrees. | PASS_1_COMPLETE |
| S049 | Blood loss: containing CI crosses zero and P .77 agrees; 5.2 compatible with integer-rounded group means. | PASS_1_COMPLETE |
| S050 | End-surgery temperature: estimate and CI touch zero, P .12 nonsignificant; rounded group means can reconcile contrast. | PASS_1_COMPLETE |
| S051 | Surgery duration: CI contains zero; P .62 agrees; median/IQR not used to infer contrast method. | PASS_1_COMPLETE |
| S052 | Anesthesia duration: CI contains zero; P .94 agrees. | PASS_1_COMPLETE |
| S053 | Narrative directional and nonsignificance claims agree with matched intervention/management rows; pain/dyspnea checked against eTable 7. | PASS_1_COMPLETE |
| S054 | Primary composite: all copies match; CI/test nonsignificant at .044, direction coherent; effect-orientation diagnostic joins F-ST1-004. | PASS_1_COMPLETE |
| S055 | Mild respiratory failure: all copies match and null CI/P .22 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S056 | Moderate respiratory failure: ordered containing intervals and P .10 agree about null; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S057 | Severe respiratory failure: null intervals and P .45 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S058 | Atelectasis: null intervals and P .25 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S059 | Pleural effusion: both intervals positive and P .005 agree; narrative higher-high agrees; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S060 | Infiltrates: null intervals/P .47 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S061 | Cardiopulmonary edema: main RR CI .99–1.74 includes null with P .12; pattern F-ST1-004, distinguished from PP S355 conflict. | PASS_1_COMPLETE |
| S062 | Bronchospasm: null intervals and P .67 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S063 | Pulmonary infection: equal event counts, null CI/P >.99 agree; near-one effect within precision. | PASS_1_COMPLETE |
| S064 | Aspiration: null intervals/P >.99 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S065 | ARDS: null intervals and P .62 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S066 | Pneumothorax: null intervals and P .37 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S067 | Severe composite: interval/P .22 agree about null; component counts need not sum to union; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S068 | Extrapulmonary composite: null intervals/P .31 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S069 | SIRS: ordered null intervals/P .44 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S070 | Sepsis: ordered null intervals/P .60 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S071 | Severe sepsis: ordered null intervals/P .46 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S072 | Septic shock: ordered null intervals/P .79 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S073 | GI failure: ordered null intervals/P .40 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S074 | GI conditional severity: fractions/partition sums 49/46 agree; global P .64. Missing severity for some events is not itself a conflicting value. | PASS_1_COMPLETE |
| S075 | Kidney failure: null intervals/P .89 agree; near-one effect within precision. | PASS_1_COMPLETE |
| S076 | Kidney stage: fractions/partition totals 31/32 agree within precision; global P .97. | PASS_1_COMPLETE |
| S077 | Extrapulmonary infection: null intervals/P .40 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S078 | Hepatic failure: equal counts and null intervals/P >.99 agree. | PASS_1_COMPLETE |
| S079 | Coma: equal counts and null intervals/P >.99 agree. | PASS_1_COMPLETE |
| S080 | DIC: RR CI 1.91–2.09 excludes one with P >.99; F-ST1-005, separately from repeated effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S081 | MI: both zero, no effect/CI/P printed; no estimate is invented. | PASS_1_COMPLETE |
| S082 | Wound healing: null intervals/P .55 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S083 | ICU: null intervals/P .29 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S084 | Hospital-free days: mean-difference footnote resolves RR-column placement; negative .77 lies inside CI crossing zero, t P .27 agrees; rounded SD/sample-size diagnostic coherent. | PASS_1_COMPLETE |
| S085 | Hypoxemia: main Table 3 negative CI/P agree, abstract CI −11.1 to +6.1 includes null with P <.001; F-ST1-001. Effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S086 | Hypotension: positive intervals/P <.001 and narrative direction agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S087 | Bradycardia: positive intervals/P .001 and narrative direction agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S088 | In-hospital mortality: printed intervals/P .09 all nonsignificant; printed RR interval does not share reproducing log symmetry of other rows, F-ST1-006; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S089 | Rescue: negative RD, RR below one and P <.001 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S090 | Vasoactive need: positive intervals and P .02 agree; same counts/P as eTable 4; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S091 | Five-day mortality: HR explicitly Cox; containing CI crosses one and P .48 agrees, matched .484 in eFigure 11; broader supplement secondary designation does not contradict explicit main post hoc designation and is excluded as wording. | PASS_1_COMPLETE |
| S092 | Nonlaparoscopic: containing CI crosses one; graphical direction favors low; interaction .08 is separate contrast; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S093 | Laparoscopic: containing CI crosses one; graphical direction favors high; interaction .08 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S094 | BMI <40: containing CI crosses one; interaction .97 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S095 | BMI ≥40: containing CI crosses one; interaction .97 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S096 | SpO2 <96: containing CI crosses one; interaction .35 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S097 | SpO2 ≥96: containing CI crosses one; near-one allocation-risk diagnostic, no within-subgroup P supplied. | PASS_1_COMPLETE |
| S098 | Peripheral incision: containing CI crosses one; direction favors low; interaction .11 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S099 | Upper abdominal incision: containing CI crosses one; direction favors high; interaction .11 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S100 | Both waist/hip categories: ordered containing intervals cross one; interaction .65 separate; missing waist measurements do not conflict with full-population totals. Effect pattern F-ST1-004; cm wording excluded. | PASS_1_COMPLETE |
| S101 | All-patient diamond: same primary counts/RR/CI as S054; containing null interval agrees with main .23; effect pattern F-ST1-004. | PASS_1_COMPLETE |
