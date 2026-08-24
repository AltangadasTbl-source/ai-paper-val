# Numeric Consistency Review

## Scope and method

Assigned scope: all canonical numeric relationships `N001`-`N035` and `N501`-`N528` (63 relationships). I reviewed the current-run native/layout assets and the supplied PDFs at the cited pages. DOC-004 pp. 3-16 were checked only against the SHA-matched OCR asset authorized for this run; no OCR was created or rerun. This review applies displayed arithmetic, totals, numerator/denominator/percentage, missingness/population identity, rounding (ordinary one-decimal percentage rounding: tolerance 0.05 percentage points), unit/label, rate-versus-count, repeated-value, and matched cross-location checks when the printed definitions make them applicable. Model-derived adjusted values are not required to equal crude arithmetic unless the source says so.

`PASS_NO_CANDIDATE` means the stated source-grounded rule reconciled or that no same-result comparator was printed. `CANDIDATE_PROPOSAL` is an observation for the coordinator's duplicate merge and stable-ID process; it is **not** a C ID or an adjudication.

## Exhaustive relationship records

| ID | Checks applied and direct result | Status |
|---|---|---|
| N001 | Phase components sum: control `2915+2649+2251+1422+829+0=10,066`; intervention `0+662+1265+2432+3214+3735=11,308` ([main p. 1](../../../jama_huffman_2018_oi_170166.pdf#page=1)). | PASS_NO_CANDIDATE |
| N002 | `21,079+295=21,374`; `215+80=295`; completion/incompletion round to 99%/1% ([main pp. 1, 5](../../../jama_huffman_2018_oi_170166.pdf#page=1)). | PASS_NO_CANDIDATE |
| N003 | Abstract and Results both print control/intervention `10,066/11,308`; these are 47.1%/52.9% of 21,374, rounding to 47%/53%. | PASS_NO_CANDIDATE |
| N004 | `602/11,308=5.32%` and `645/10,066=6.41%`, matching 5.3%/6.4% in abstract, narrative, and Table 3. | PASS_NO_CANDIDATE |
| N005 | Design counts are definitions, not mutually exclusive observed totals; 63 hospitals, five 4-month steps, and four recruitment strata are consistently labelled ([main pp. 2-3](../../../jama_huffman_2018_oi_170166.pdf#page=2)). | PASS_NO_CANDIDATE |
| N006 | Planning values are consistently labelled assumptions/target parameters; no observed-result identity is asserted. | PASS_NO_CANDIDATE |
| N007 | At every step, enrolled = included + excluded (`3107=2915+192`, `2765=2649+116`, `2328=2251+77`, `1450=1422+28`, `844=829+15`, `1001=896+105`). Lost-to-follow-up is explicitly a subset included in analysis, not an additional term ([main p. 4](../../../jama_huffman_2018_oi_170166.pdf#page=4)). | PASS_NO_CANDIDATE |
| N008 | Exclusions `954+132+91+6=1,183`; `22,557-1,183=21,374`; step-level decompositions also sum to each printed exclusion count. | PASS_NO_CANDIDATE |
| N009 | Figure 1 explicitly resolves apparent overlap: lost participants are included in analysis; no population double-count is claimed. | PASS_NO_CANDIDATE |
| N010 | Table 1 count/percent checks: e.g. male `7654/10066=76.04%`, `8529/11308=75.42%`; tobacco `3772/10066=37.47%`, `2842/11308=25.13%`; diabetes `41.24%/47.16%`. All round as printed. | PASS_NO_CANDIDATE |
| N011 | Transfer `41.74%/37.13%`, no insurance `68.32%/76.62%`, and STEMI `68.76%/59.85%` round as printed. | PASS_NO_CANDIDATE |
| N012 | Continuous-variable units and incomplete-data denominators are explicitly printed; no arithmetic identity is implied for means/medians. Population denominators do not exceed group Ns. | PASS_NO_CANDIDATE |
| N013 | All displayed laboratory/physiologic incomplete-data denominators are positive and no greater than their group Ns; units/summary labels remain matched. | PASS_NO_CANDIDATE |
| N014 | Same denominator-bound and summary-label checks pass for LDL, triglycerides, creatinine, glucose, and hemoglobin. | PASS_NO_CANDIDATE |
| N015 | Hospital-type patient counts sum to group totals: control `4097+2785+3184=10,066`; intervention `3036+2964+5308=11,308`. Percents total 100.0% in each group within rounding. | PASS_NO_CANDIDATE |
| N016 | Hospital-size patient counts sum to group totals; control percents 18.4+35.4+38.2+8.0=100.0 and intervention 15.1+43.9+31.6+9.5=100.1 (normal independent one-decimal rounding; unrounded values reconcile). | PASS_NO_CANDIDATE |
| N017 | Catheterization-lab patient counts sum to group totals and each row's percentage reconciles; category hospital counts `3+17+43=63`. | PASS_NO_CANDIDATE |
| N018 | Narrative overall mean age and rounded proportions agree with the weighted/group values at stated precision; symptom-to-door values exactly repeat Table 1. | PASS_NO_CANDIDATE |
| N019 | Included/missing-follow-up troponin `1.3/4.6 ng/mL` matches eTable 1 complete/missing entries; distinct from intervention/control Table 1 comparison. | PASS_NO_CANDIDATE |
| N020 | All Table 2 printed numerator/denominator percentages (including `1696/10052=16.87%`, `9858/10042=98.17%`, `4638/10885=42.61%`) reconcile to one decimal. Eligible denominators are defined separately from group Ns. | PASS_NO_CANDIDATE |
| N021 | Procedures reconcile: echo `91.49%/92.998%`, angiography `61.40%/57.48%`, PCI `52.47%/46.61%`, and primary PCI `50.22%/47.78%`. | PASS_NO_CANDIDATE |
| N022 | Reperfusion/time rows reconcile: thrombolysis `23.06%/23.21%`, reperfusion `73.21%/71.00%`, rescue PCI `9.35%/15.24%`; time rows retain their median/IQR and eligible-N labels. | PASS_NO_CANDIDATE |
| N023 | Discharge fractions reconcile, including ACE/ARB `534/1029=51.90%` and `643/1495=43.01%`; discharge/eligibility denominators are explicitly narrower than randomized-group Ns. | PASS_NO_CANDIDATE |
| N024 | Matched narrative/table checks pass except the β-blocker adjusted-risk-difference CI endpoint described in proposal NCP-001. Other matched process numbers retain their appropriate raw-versus-model distinction. | CANDIDATE_PROPOSAL NCP-001 |
| N025 | Table 3 raw outcome counts divide by control/intervention Ns and round as printed, e.g. MACE 6.4%/5.3%, death 5.1%/3.9%, stroke 0.6%/0.8%. Components need not sum to MACE because patients may have more than one component. | PASS_NO_CANDIDATE |
| N026 | Process outcome percentage denominators are defined in footnotes; e.g. 3122/9848=31.70%, 3878/10833=35.80%, 3526/3673=96.00%, 2618/2765=94.68%. | PASS_NO_CANDIDATE |
| N027 | MACE, GUSTO, medication-composite, and baseline-smoker denominator definitions distinguish counts, proportions, and eligible populations. | PASS_NO_CANDIDATE |
| N028 | Figure 2 cohort/step denominators match the Figure 1 included populations by cohort and step; their total is 21,374. | PASS_NO_CANDIDATE |
| N029 | Figure 2 labels percent y-axes, control/intervention marker direction, and 95% CI error bars; no rate/count substitution is present. | PASS_NO_CANDIDATE |
| N030 | Expanded outcome is explicitly a distinct post-hoc composite; 7.0% intervention versus 9.1% control agrees with eTable 7 `795/11308` and `919/10066`. | PASS_NO_CANDIDATE |
| N031 | Age subgroup denominators and MACE events sum to overall totals in both groups; all six fractions round as printed. | PASS_NO_CANDIDATE |
| N032 | Sex and MI-status subgroup denominators/events separately sum to overall totals; every displayed rate reconciles under one-decimal rounding. | PASS_NO_CANDIDATE |
| N033 | Hospital-size subgroup events and denominators sum to overall totals; rates reconcile. | PASS_NO_CANDIDATE |
| N034 | Hospital-type subgroup events and denominators sum to overall totals; rates reconcile. | PASS_NO_CANDIDATE |
| N035 | The conclusion's “did not decrease” interpretation matches the temporal-adjusted primary MACE RD −0.09% (95% CI −1.32% to 1.14%) and OR 0.98 (0.80-1.21), which include null values. | PASS_NO_CANDIDATE |
| N501 | Protocol and SAP consistently describe a four-month baseline and later implementation at months 8/12/16/20; terminology is planned schedule, not an observed count. | PASS_NO_CANDIDATE |
| N502 | `60-70` hospitals, 15,750 subjects, two years, and 12-14 hospitals/cohort are explicitly protocol targets; no conflicting observed claim is printed. | PASS_NO_CANDIDATE |
| N503 | Planned identity is internally coherent: `15,000/(1-0.05)=15,789.5`, compatible with rounded target 15,750; all repeats are design parameters. | PASS_NO_CANDIDATE |
| N504 | The 2,200-patient SAQ/economic subset is consistently identified as a planned sub-study target. | PASS_NO_CANDIDATE |
| N505 | Follow-up/data-entry time limits are distinct operational timings and do not conflict: contact at 30 days; entry deadlines follow discharge/contact. | PASS_NO_CANDIDATE |
| N506 | The two 5% monitoring fractions have different bases (source audit and random discharged-patient confirmation) and are not additive trial outcomes. | PASS_NO_CANDIDATE |
| N507 | ICC 0.05 is consistently a power-calculation assumption, not an observed ICC. | PASS_NO_CANDIDATE |
| N508 | `>80%` is a predeclared concordance definition; it is not printed as a measured proportion. | PASS_NO_CANDIDATE |
| N509 | Missingness definition consistently specifies an unreturned 30-day form after OPD follow-up or three calls; no observed count is attached here. | PASS_NO_CANDIDATE |
| N510 | SAP's 12 clusters in five groups and two age strata are analysis definitions; no category-total identity is asserted. | PASS_NO_CANDIDATE |
| N511 | Interim/final z and P boundaries are distinct O'Brien-Fleming planned thresholds; no display-zero issue or incompatible same-test result is printed. | PASS_NO_CANDIDATE |
| N512 | OCR-only toolkit/sample-report numbers are explicitly templates, not trial results; no exact graph calculation was inferred. | PASS_NO_CANDIDATE |
| N513 | Performance measure is labelled as eligible opportunities met; measure counts (11 all, 11 STEMI, 8 NSTEMI, 6 discharge) are catalogue counts, not denominators to be summed. | PASS_NO_CANDIDATE |
| N514 | Timings/doses/EF threshold are care instructions, retain their stated units, and are not observed trial values. | PASS_NO_CANDIDATE |
| N515 | eTable 1 group Ns `21,079+295=21,374`, matching main-paper eligible total. | PASS_NO_CANDIDATE |
| N516 | eTable 1 percentages reconcile with complete/missing Ns, e.g. `15973/21079=75.78%` and `210/295=71.19%`; all categorical rows pass ordinary one-decimal rounding. | PASS_NO_CANDIDATE |
| N517 | Printed group headers are complete/missing follow-up while its sole difference-footnote comparator is intervention/control; see proposal NCP-002. | CANDIDATE_PROPOSAL NCP-002 |
| N518 | eTable 2 control/intervention Ns sum to 21,374 and match main paper/Figure 1 totals. | PASS_NO_CANDIDATE |
| N519 | eTable 2 is explicitly marginal/model-derived and labels differences intervention minus control; displayed differences match column direction at printed precision where crude arithmetic is relevant. | PASS_NO_CANDIDATE |
| N520 | eTable 3 ten cells group by step: `2915+(2649+662)+(2251+1265)+(1422+2432)+(829+3214)+3735=21,374`; matches main phase assignment. | PASS_NO_CANDIDATE |
| N521 | eTable 3's `NA` creatinine cells are explicitly data-not-collected and not numeric zeros; remaining cell summaries have their own labelled bases. | PASS_NO_CANDIDATE |
| N522 | eTable 4 step denominators `2915+3311+3516+3854+4043+3735=21,374`; its NA creatinine explanation agrees with eTable 3. | PASS_NO_CANDIDATE |
| N523 | eTable 4 labels all baseline grids by step, distinguishes mean/SD, n(%), and median/IQR, and consistently gives creatinine NA before collection. | PASS_NO_CANDIDATE |
| N524 | eTable 5 OR intervals have positive, ordered endpoints and contain their point estimates; sensitivity columns are distinct adjustment sets, not duplicate expected values. | PASS_NO_CANDIDATE |
| N525 | eTable 6 OR intervals have positive, ordered endpoints and contain their point estimates; time-exposure interaction is explicitly a separate model. | PASS_NO_CANDIDATE |
| N526 | eTable 7 fractions reconcile: MACE-plus `919/10066=9.13%`, `795/11308=7.03%`; HF `2.25%/1.69%`; shock `2.16%/1.50%`; arrest `2.05%/2.10%`. | PASS_NO_CANDIDATE |
| N527 | eTable 7 footnote explicitly defines OR intervention versus control and RD as intervention minus control; this matches signs/directions in the displayed models. | PASS_NO_CANDIDATE |
| N528 | eFigure 1B label is `Control − Intervention`, while eTable RDs are intervention minus control; these are separately labelled graphical/analytic scales and not conflicting values. No exact plotted numbers are printed. | PASS_NO_CANDIDATE |

## Exhaustive candidate-proposal section

### NCP-001 — β-blocker adjusted risk-difference CI has conflicting upper endpoint

- **Relationships:** N024.
- **Exact supplied-source locations:** [main-paper Table 2, p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6) and [main-paper Results narrative, pp. 6-7](../../../jama_huffman_2018_oi_170166.pdf#page=6).
- **Direct observation:** Table 2 prints for in-hospital β-blocker use an adjusted risk difference of `6.25 (4.10 to 8.40)`. The matched narrative prints `6.25% [95% CI, 4.10%-8.10%]` for the same intervention-versus-control result.
- **Reproducible rule/calculation:** A same-result value and its confidence-interval endpoints should agree across a table and its matched narrative after matching population (eligible individuals without contraindications), contrast (intervention vs control), effect measure (adjusted risk difference), and model description. The point estimate and lower endpoint match exactly; upper-endpoint discrepancy is `8.40 − 8.10 = 0.30` percentage points. This exceeds any decimal-rounding tolerance because both endpoints are printed to two decimal places (maximum half-unit rounding tolerance 0.005 percentage points).
- **Alternatives:** The narrative may contain a transcription/rounding error; Table 2 may contain a typesetting error; or the two locations may reflect analyses not fully identified in the prose. The source calls both adjusted and describes Table 2 as the association accounting for clustering and temporal trends, but it does not state that two different β-blocker models produced these otherwise matched values.
- **Quality-control relevance:** A conflicting interval endpoint can be carried into quantitative evidence extraction and later evidence products.
- **Human question:** Which upper confidence-limit value, `8.40%` or `8.10%`, is the intended value for the stated in-hospital β-blocker adjusted risk difference?
- **Status:** Pending Human Adjudication.

### NCP-002 — eTable 1 difference-footnote comparator conflicts with the displayed groups

- **Relationships:** N517.
- **Exact supplied-source location:** [online supplement 3, eTable 1, p. 17](../../../joi170166supp3_prod.pdf#page=17).
- **Direct observation:** The two data columns are headed `Complete Follow Up n=21079` and `Missing Follow Up n=295`, while footnote a says `Difference = intervention minus control`. The difference values follow the displayed complete/missing columns: age `60.6` versus `60.0` has printed difference `-0.6`; male `75.8%` versus `71.2%` has `-4.6`; tobacco `30.8%` versus `42.4%` has `11.6`.
- **Reproducible rule/calculation:** A table's difference label must name the populations in its two displayed comparator columns. For the printed values, `missing − complete` gives `60.0−60.6=−0.6`, `71.2−75.8=−4.6`, and `42.4−30.8=11.6`, exactly matching the reported differences. An `intervention − control` label identifies a different pair of populations that is absent from this table.
- **Alternatives:** Footnote a may have been inadvertently carried from eTable 2, where intervention/control columns actually appear; it could be a generic label but it is printed as the table-specific difference definition. No supplied-source text defines a different mapping for these eTable 1 columns.
- **Quality-control relevance:** The incorrect comparator label can make missing-follow-up comparisons look like randomized-group comparisons in data extraction or evidence synthesis.
- **Human question:** Should eTable 1 footnote a identify the difference as `missing follow-up minus complete follow-up` (the direction indicated by its numbers), or is another comparator intended?
- **Status:** Pending Human Adjudication.

## Limits

No raw dataset, unrounded values, model code, or analytic output is supplied. Accordingly, adjusted marginal differences and ORs were checked for explicitly printed labels, direction, endpoint order, and exact matched repetitions, not reverse-engineered from crude counts. Graphical points without printed values were not digitized. No web source, old audit derivative, or newly run OCR was used.

## Counts

- Relationships reviewed: 63/63.
- PASS_NO_CANDIDATE: 61.
- Candidate proposals: 2 (NCP-001 and NCP-002), each **Pending Human Adjudication**.
