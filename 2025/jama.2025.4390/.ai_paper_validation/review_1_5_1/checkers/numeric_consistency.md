# Numeric Consistency Check

## Scope and checking rules

This check covers every relationship in `relationships/numeric_relationship_inventory.md` (`N001`-`N067`) against the current supplied PDFs and their fresh direct-source maps: `extraction/main_quantitative_evidence.md`, `extraction/parts/support_protocol_sap.md`, `extraction/parts/support_results_001_024.md`, and `extraction/parts/support_results_025_049.md`. Direct PDF pages cited below use the package's current sources: DOC-001 `jama_garrison_2025_oi_250019_1749674951.29054.pdf`, DOC-002 `joi250019supp1_prod_1749674951.29554.pdf`, DOC-003 `joi250019supp2_prod_1749674951.30054.pdf`, and DOC-004 `joi250019supp3_prod_1749674951.30054.pdf`.

I checked addition/subtraction, stated denominators, displayed percentages (using ordinary one-decimal rounding, tolerance 0.05 percentage points unless a printed percentage has no decimal), mutually exclusive subgroup sums, count versus rate scales, population/time-point matching, repeated source values, and outcome/measurement labels. Counts tied to a versioned protocol plan, a nonexclusive medication class, a multiple-response reason set, a survival follow-up distribution, or a separately defined available-case population were not inappropriately forced to sum. A display of `P < .001` or another finite-precision small P value was not treated as a candidate on its own.

## Per-relationship outcomes

| ID | Outcome | Key completed check and evidence location |
|---|---|---|
| N001 | CONSISTENT | 1677 + 1680 = 3357; DOC-001 p.1. |
| N002 | CONSISTENT | Cohort summaries match the randomized baseline and stated median follow-up; DOC-001 pp.1, 4-6. |
| N003 | CONSISTENT | Abstract 2.3/2.4 per 100 patient-years is rounded consistently with Table 2's 2.30/2.44; DOC-001 pp.1, 8. |
| N004 | CONSISTENT | 429 family physicians + 7 nurse practitioners = 436; DOC-001 p.2. |
| N005 | UNRESOLVED_DEFINITION | “About three-fourths” is an approximate monotherapy/diuretic context statement, not a directly reconstructible denominator; DOC-001 p.2. |
| N006 | UNRESOLVED_DEFINITION | External-study numbers/effects are contextual and no supplied primary source permits independent reconstruction; DOC-001 p.2. |
| N007 | CONSISTENT | Block/stratum and contact-time labels are internally coherent; DOC-001 p.3. |
| N008 | CONSISTENT | 92.6% and 7.4% are complementary after rounding; source-coverage population is explicitly separate from randomized/available-case populations; DOC-001 p.3. |
| N009 | CONSISTENT | Thresholds, scales, and assessment times agree with Table 2/SAP definitions; DOC-001 p.3; DOC-003 pp.2-3. |
| N010 | CONSISTENT | 1249 + 375 + 87 + 5 = 1716; 5073 - 1716 = 3357; ineligible reasons sum to 375; DOC-001 p.4, Figure 1. |
| N011 | CONSISTENT | Arm-specific electronic/non-electronic subcounts sum to each withdrawal/loss count; six-month denominators are respondents (1518 and 1567), not randomized totals; DOC-001 p.4. |
| N012 | CONSISTENT | Narrative baseline percentages agree, at displayed rounding, with arm-specific Table 1 totals; medication classes are nonexclusive; DOC-001 pp.4-6. |
| N013 | CONSISTENT | 57 + 44 = 101 and 272 + 258 = 530; each percentage rounds from its stated randomized-arm denominator. The 101 is the unable-to-follow subset, matching Figure 1's non-electronically-followable subcounts; DOC-001 p.4. |
| N014 | CONSISTENT | Sex categories and age-at-least-75 percentages use arm denominators and round correctly; DOC-001 p.5. |
| N015 | CONSISTENT | Self-selected ethnicity counts/percentages are consistent at rounding; categories are explicitly not required to be mutually exclusive; DOC-001 p.5. |
| N016 | CONSISTENT | Province and chronotype category counts each sum to randomized arm totals; percentages round correctly; DOC-001 p.5. |
| N017 | CONSISTENT | Binary percentages reproduce from arm denominators; medians/IQRs are not additive quantities; DOC-001 p.5. |
| N018 | CONSISTENT | SBT categories, including declined, sum to 1677 and 1680; score labels match the footnote; DOC-001 pp.5-6. |
| N019 | CONSISTENT | Comorbidity percentages reproduce from randomized-arm denominators; conditions are nonexclusive; DOC-001 p.5. |
| N020 | CONSISTENT | Comorbidity/none values are properly nonadditive; displayed percentages are consistent with arm denominators; DOC-001 p.6. |
| N021 | CONSISTENT | 895+588+155+39=1677 and 908+577+170+25=1680; DOC-001 p.6. |
| N022 | CONSISTENT | Medication-class percentages reproduce from arm denominators; classes/combination products are nonexclusive; DOC-001 p.6. |
| N023 | CONSISTENT | Frailty, EQ-5D-5L, BMI, and SBT ranges/directions agree with supplied SAP definitions; DOC-001 p.6; DOC-003 p.6. |
| N024 | CONSISTENT | 406, revised 255, and observed 336 are sequential design/final quantities, not simultaneous totals; DOC-001 p.6. |
| N025 | CONSISTENT | Medication-level versus participant-level adherence and six- versus 72-month populations/timepoints are expressly distinct; DOC-001 p.6; DOC-004 pp.41-44. |
| N026 | CONSISTENT | Figure 2 risk sets decline plausibly and arm-specific median follow-up agrees with Table 2; risk sets are not event counts and are not expected to equal retention categories; DOC-001 p.7. |
| N027 | CONSISTENT | ABPM arms are 151+151=302; printed mean differences equal displayed means within one-decimal rounding and match eTable 9; DOC-001 p.7; DOC-004 p.49. |
| N028 | CONSISTENT | 78.9 - 79.5 = -0.6, compatible with modelled -0.75 after unrounded data; scale is 0-100; DOC-001 p.7. |
| N029 | UNRESOLVED_DEFINITION | These are external-study/review contextual totals with heterogeneous designs and no supplied underlying data; DOC-001 p.7. |
| N030 | CANDIDATE | Table 2 primary rates are arithmetically coherent, but the same all-patient event counts are paired with materially incompatible values under Figure 3's printed “Rate per 100 patient-years” header; full proposal A below; DOC-001 pp.8-9. |
| N031 | CONSISTENT | Component event counts are not mutually exclusive incident-person counts and need not sum to the composite; rate differences have the displayed sign/rounding; DOC-001 p.8. |
| N032 | CONSISTENT | 23.26 - 25.15 = -1.89; repeated-visit count/rate is not a participant proportion; DOC-001 p.8. |
| N033 | CONSISTENT | Survival-event rate differences have correct displayed direction within rounding; DOC-001 p.8. |
| N034 | CONSISTENT | Interview-level mean percentages/SDs are not cumulative participant event counts; measure label agrees with Table 2 footnote; DOC-001 p.8. |
| N035 | CONSISTENT | Glaucoma rate difference and vision percentages reproduce the displayed direction/rounding; DOC-001 p.8. |
| N036 | CONSISTENT | 376/1446=26.00% and 395/1493=26.46%; cognitive denominators are available 18-month assessments, while nursing-home rows are time-to-event; DOC-001 p.8. |
| N037 | CONSISTENT | Vision, cognitive, and nursing-home labels agree with SAP definitions; DOC-001 p.8; DOC-003 pp.2-3. |
| N038 | CONSISTENT | 302 is the 151-per-arm ABPM sample; 57% decline is a separate invitation-flow proportion; DOC-001 p.10; DOC-004 pp.18-19, 49. |
| N039 | CONSISTENT | 1.20/0.80=1.50, supporting the stated 50% higher rate; comparison is external contextual evidence; DOC-001 p.10. |
| N040 | CONSISTENT | 436 practices and 3% unable-to-follow summary match N001/N013 at rounded precision; DOC-001 p.10. |
| N041 | CONSISTENT | Protocol 406 is an original planned event target, consistent with later explicitly revised target; DOC-002 p.3; DOC-001 p.6. |
| N042 | CONSISTENT | 379 x 1.07=405.53, rounded to 406; enrollment/event rates are original planning assumptions; DOC-002 p.3. |
| N043 | CONSISTENT | Interim/follow-up values are version-specific plans/rules rather than final-result denominators; DOC-002 p.4. |
| N044 | CONSISTENT | Original 100+100 ABPM and 200-person diuretic-review triggers were superseded/separate protocol plans; DOC-002 p.4. |
| N045 | CONSISTENT | 365 x 250=91,250; 91,250 x .85 x .12=9307.5, whereas 8750 is explicitly a projected enrollment expectation and may reflect unprinted feasibility assumptions; no direct contradiction; DOC-002 p.5. |
| N046 | CONSISTENT | 8750 to 11,700 is an explicit dated amendment, not a final analysis population claim; DOC-002 p.9. |
| N047 | CONSISTENT | 151+151=302 and the amendment matches the reported ABPM sample; DOC-002 p.10; DOC-004 p.49. |
| N048 | UNRESOLVED_DEFINITION | “Over/about” recruitment-substudy counts and an unshown power-calculation variance/prevalence do not support exact arithmetic reconstruction; DOC-002 p.13. |
| N049 | CONSISTENT | About-70,000 comparator, 3357 trial dataset, and 302 unlinked ABPM dataset are different populations/files; DOC-002 pp.14-17. |
| N050 | CONSISTENT | Outcome thresholds/claims/process labels match their analysis-specific denominators and main-paper labels; DOC-003 pp.2-3. |
| N051 | CONSISTENT | Censoring/missingness rules distinguish claims-followable participants from those unavailable for each analysis; no numeric conflict identified; DOC-003 p.3. |
| N052 | CONSISTENT | Covariate limits, scale labels, and subgroup thresholds agree with main-paper figure/table definitions; DOC-003 pp.4-6. |
| N053 | CONSISTENT | Potential outcomes from overlapping administrative/self-report sources are explicitly nonadditive; accepted/rejected counts are internally tabulated by outcome/source; DOC-004 pp.10-12. |
| N054 | CONSISTENT | ABPM invitation, consent, inadequate-recording, repeat/replacement, and analyzed counts follow the diagram's distinct stages; final analyzed total is 151+151=302; DOC-004 pp.18-19. |
| N055 | CONSISTENT | Analysis/missingness framework supplies definitions rather than a competing result denominator; DOC-004 pp.20-21. |
| N056 | CONSISTENT | Named medicine counts are medicine-level/nonexclusive and correctly not summed to participant totals; DOC-004 pp.23-24. |
| N057 | CONSISTENT | Dashed all-withdrawal/loss endpoints visually approximate 329/1677=19.6% and 302/1680=18.0%; solid 3.4%/2.6% endpoints are unable-to-follow and match N013; DOC-004 p.25. |
| N058 | CANDIDATE | The bedtime diuretic triplet in eFigure 4 is 278/138/8, whereas eTable 6 reports 277/139/8 for the same 424 medicines; full proposal B below; DOC-004 pp.26, 42. |
| N059 | CONSISTENT | Recruitment rows sum to 1680 and 1677; 41,128 x 6.2%=2549.9, compatible with 2568 PCP-recruited participants after display rounding/defined numerator difference; DOC-004 p.27. |
| N060 | CONSISTENT | Online+phone equals total at every listed follow-up point; percentages sum to 100.0% at displayed precision; DOC-004 p.28. |
| N061 | CONSISTENT | Expanded baseline arm+arm=overall cells and categorical totals were checked; published percentage deviations are ordinary rounding or documented reduced administrative-data denominator; DOC-004 pp.29-32. |
| N062 | CONSISTENT | 2726 + 631=3357; completion/loss comparison uses a distinct retention classification and its baseline percentages use the stated group denominator; DOC-004 pp.33-36. |
| N063 | CANDIDATE | eTable 5's printed Other ethnicity row duplicates the White/Caucasian row (40 [90.9%] versus 53 [93.0%]) and makes an ostensibly categorical baseline table impossible; full proposal C below; DOC-004 p.37. |
| N064 | CANDIDATE | This is the table side of the N058 cross-display discrepancy; all other class triplets sum to their printed class totals, including eTable 6 bedtime diuretic 277+139+8=424; DOC-004 pp.41-42. |
| N065 | CONSISTENT | At-allocation counts reproduce displayed percentages at every month from 6-72 using that month/arm participant denominator; medication denominators and dose percentages are separately labelled; DOC-004 pp.43-44. |
| N066 | CONSISTENT | Success ratios reproduce printed percentages at ordinary one-decimal rounding; multiple failure reasons are expressly nonexclusive and were not summed; DOC-004 pp.45-48. |
| N067 | CONSISTENT | Each reported ABPM mean difference equals bedtime minus morning within rounding; dip categories sum to 151 in each arm (54+70+27 and 78+58+15); DOC-004 p.49. |

## Candidate proposals

### Proposal A — Figure 3 rate-column value/label conflict

- **Relationship:** N030 cross-checked with the Figure 3 all-patients/subgroup display.
- **Exact source locations:** DOC-001 p.8, Table 2 primary outcome; DOC-001 p.9, Figure 3 (and fresh direct text `preprocessing/main/doc001_p09_layout.txt`, lines 9-12).
- **Direct observation:** Table 2 prints 163 bedtime events, rate 2.30 per 100 patient-years, and 173 morning events, rate 2.44 per 100 patient-years. Figure 3 prints the same all-patient event counts, 163 and 173, but under the header “Rate per 100 patient-years” prints 71.0 and 71.0. Its mutually exclusive subgroup rows partition those displayed values (for example, sex: 30.5+40.5=71.0 and 30.4+40.6=71.0; age: 14.9+56.1=71.0 and 14.5+56.5=71.0).
- **Rule/calculation and tolerance:** A rate per 100 patient-years must equal `100 x events / total person-years`. Table 2 supplies the directly reported all-patient rates, 2.30 and 2.44. The Figure 3 values differ by 68.70 and 68.56 rate units, far beyond display rounding tolerance (0.005 for a two-decimal printed rate or 0.05 for a one-decimal rate). The subgroup values summing to 71.0 establish that they cannot each be independently derived event rates under the printed header.
- **Inference boundary and alternative:** The header and values are directly observed; the conclusion that one is mislabelled/misreported is an inference. A possible alternative is that “71.0” and its partitions encode another unlabelled quantity (for example a total follow-up quantity) rather than a rate. That alternative still leaves the printed rate label inconsistent.
- **Quality-control relevance:** This is a scale/label inconsistency in the primary-outcome subgroup display. It can cause incorrect extraction of subgroup event rates or rate-based effect calculations.
- **Human question:** What quantity do the Figure 3 71.0 and subgroup-partitioned values represent, and should the column header or displayed values be corrected to the actual per-100-patient-year rates?

### Proposal B — One-medicine conflict between six-month diuretic timing displays

- **Relationship:** N058/N064.
- **Exact source locations:** DOC-004 p.26, eFigure 4; DOC-004 p.42, eTable 6 (fresh direct text `preprocessing/support_results_025_049/page_42_layout.txt`).
- **Direct observation:** For bedtime-allocation diuretics, eFigure 4 prints the stacked triplet as allocated/off allocation/twice-or-more daily: 278/138/8. eTable 6 prints total 424 and the corresponding triplet 277/424 (65.3%), 139/424 (32.8%), and 8/424 (1.9%). Both displays identify the same six-month allocation/class/timing relationship.
- **Rule/calculation and tolerance:** Both triplets sum to 424: 278+138+8=424 and 277+139+8=424. But category-by-category equality requires a zero-count tolerance: eFigure 4 differs by +1 as allocated and -1 off allocation. This is not a percentage-rounding issue because the printed counts differ.
- **Inference boundary and alternative:** The discordant printed counts are direct observations. The inference is that one display contains a one-medicine transcription/reporting error. An alternative is that the figure used a subtly different data cut or classification rule; neither display states such a distinction, and both otherwise match the same eTable 6 class triplets.
- **Quality-control relevance:** A figure-table conflict can propagate an incorrect class-specific adherence numerator and percentage into evidence extraction.
- **Human question:** Which bedtime-diuretic counts (278/138/8 or 277/139/8) are authoritative, and was a distinct classification/data-lock rule used for eFigure 4?

### Proposal C — Duplicated ethnicity category values in eTable 5

- **Relationship:** N063.
- **Exact source location:** DOC-004 p.37, eTable 5, Ethnicity rows (fresh direct text `preprocessing/support_results_025_049/page_37_layout.txt`).
- **Direct observation:** eTable 5 states morning n=44 and bedtime n=57. It prints White/Caucasian as 40 (90.9%) and 53 (93.0%), then later prints Other as exactly 40 (90.9%) and 53 (93.0%). The intervening Asian, Indigenous, South East Asian/Indian, Black/African American, Latino, and declined rows already contain their own category counts.
- **Rule/calculation and tolerance:** A category count cannot simultaneously be both White/Caucasian and Other in this table's mutually exclusive ethnicity presentation. Summing the printed morning ethnicity rows gives 45, exceeding n=44; bedtime sums to 58, exceeding n=57. Count tolerance is zero; the excess is one in each arm. The printed Other values duplicate White rather than represent an independent category.
- **Inference boundary and alternative:** The duplicate values and impossible sums are direct observations. The likely copy/paste error is an inference. An alternative is overlapping ethnicity selection, but the table labels/readout present a categorical comparison and would then need an explicit nonexclusive-category note; none appears on the page.
- **Quality-control relevance:** The table reports a baseline subgroup distribution and an ethnicity-comparison P value. The duplicate row makes the category distribution not reproducible and can mislead secondary users.
- **Human question:** What are the correct Other-ethnicity counts/percentages for morning and bedtime allocation in eTable 5, and are the ethnicity categories intended to be mutually exclusive?

## Counts and limitations

- **Relationships reviewed:** 67/67 (`N001`-`N067`).
- **Outcomes:** 59 `CONSISTENT`, 4 `CANDIDATE` ID outcomes (N058 and N064 are the two sides of one discrepancy, therefore representing 3 distinct candidate proposals), and 4 `UNRESOLVED_DEFINITION` outcomes.
- **Limitations:** External contextual-study quantities and approximate recruitment statements could not be independently recalculated from supplied primary data. Survival rates cannot be reconstructed exactly from medians/IQR follow-up. Figure 3's rate conflict was confirmed from the current rendered PDF and direct layout text; the reports do not state an alternative denominator/quantity for its values. No web or legacy candidate/report conclusion was used.
