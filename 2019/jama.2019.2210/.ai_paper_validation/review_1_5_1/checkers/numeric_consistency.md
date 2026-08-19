# Numeric Consistency Check

## Scope and checking convention

This check covers every stable numeric/reporting relationship `N001` through `N089` in `relationships/numeric_relationship_inventory.md`. The direct PDFs are the authority; mapped extraction is used as a locator and transcription aid. No legacy candidate, checker, verifier, critic, quality, or report output was consulted.

For count/percentage pairs, the rule was `printed percentage = 100 × printed count / printed denominator`, allowing ordinary rounding to the displayed precision: ±0.5 percentage points for a whole-percent display, ±0.05 percentage points for one decimal place, and ±0.005 percentage points for two decimal places. A displayed sum was checked exactly unless the source labels categories nonexclusive. At-risk rows were checked as participant counts, not event counts, risks, percentages, rates, or person-time denominators; their only applicable arithmetic checks here are nonnegative whole-number values and nonincrease over follow-up. Medians, IQRs, Kaplan-Meier/Nelson-Aalen estimates, change ratios, and model-derived values were not forced to equal arithmetic functions of separately displayed summaries unless the PDF states that identity.

`No qualifying lead` means this numeric check found no document-grounded inconsistency under the printed definitions; it is not an adjudication. The leads below are pending human review only. No stable candidate ID, severity, validity, or disposition is assigned here.

## Complete relationship check register

| Relationship IDs checked | Exact direct-source location(s) | Checks applied and result |
|---|---|---|
| N001 | DOC-001 PDF pp. 1-2 | Population/time anchor checked as definitions only; no numerical identity or matched contrary value is printed. No qualifying lead. |
| N002 | DOC-001 pp. 1-2, 4 | `251 + 166 = 417`; 251/417=60.19% and 166/417=39.81%, consistent with printed 3:2 allocation and rounded 60%/40%. No qualifying lead. |
| N003 | DOC-001 pp. 1-2 | Outcome labels distinguish time-to-event outcomes from safety outcomes; no count/rate conflation in this relationship. No qualifying lead. |
| N004 | DOC-001 pp. 1, 3 | Efficacy ITT (`n=417`) and per-protocol safety populations are explicitly distinct. No concrete number is compared across those populations without its label. No qualifying lead. |
| N005 | DOC-001 p. 3 | Planning values are labelled as assumptions: 75% versus 62%, 400 total, 3:2, 5+2 years. `5 + 2 = 7`; no asserted observed-result identity. No qualifying lead. |
| N006 | DOC-001 p. 3 | Cut points `<20`, `20-40`, `>40 ng/mL` are nonoverlapping at the stated convention and high group is excluded from interaction testing. No qualifying lead. |
| N007 | DOC-001 p. 3 | Analysis settings (200-entry interim trigger, `.001`, 50 imputations) are not mutually conflicting numeric results. No qualifying lead. |
| N008 | DOC-001 pp. 1, 4 | `439 − 22 = 417`; `15 + 5 + 2 = 22`; abstract `15 + 7 = 22`. The abstract aggregates Figure 1's 5 and 2 exclusions. No qualifying lead. |
| N009 | DOC-001 p. 4 | `251 + 166 = 417`; randomized, received-treatment, and primary-analysis counts agree by arm. No qualifying lead. |
| N010 | DOC-001 p. 4 | Figure counts give `14+9=23` and `10+9=19`, with 1 lost participant shown separately. The narrative includes that loss among 15 vitamin-D nonmedical stops; `15+10+9+9=43` and `43/417=10.31%`, consistent with 10.3%. No qualifying lead. |
| N011 | DOC-001 pp. 1, 4 | `416/417=99.760%`, consistent with 99.8% to one decimal place. Aggregate and arm-specific median/IQR summaries are not required to pool arithmetically. No qualifying lead. |
| N012 | DOC-001 pp. 1, 4-5 | `173+103=276`; `78+63=141`; `276+141=417`; 276/417=66.19% and 141/417=33.81%, consistent with rounded narrative/abstract sex percentages. Mean age and median age are explicitly different measures. No qualifying lead. |
| N013 | DOC-001 pp. 4-5 | Site totals are `40+174+2+201=417`; shares are 9.59%, 41.73%, 0.48%, and 48.20%, consistent with printed rounded shares. Each arm also totals its header denominator. No qualifying lead. |
| N014 | DOC-001 pp. 4-5 | Stage totals are `182+111+124=417`; arm rows total 251 and 166; overall shares 43.65%, 26.62%, 29.74% support 44%, 26%, 30%. No qualifying lead. |
| N015 | DOC-001 p. 5 | Age rows total 251 and 166. BMI rows total 249 and 165, below the arm headers by 2 and 1 with no missingness note; this is registered as C007. Quartile ranges are categories, while narrative age/BMI figures are medians. |
| N016 | DOC-001 p. 5 | Each comorbidity percentage reconciles to its arm denominator within display rounding. Rows are not mutually exclusive, so a column sum is inapplicable. No qualifying lead. |
| N017 | DOC-001 p. 5 | Pathology rows total `226+22+3=251` and `147+16+3=166`; footnote components `4+1+1=6` equal the two arms' combined Other count. No qualifying lead. |
| N018 | DOC-001 pp. 4-6 | `173+232+5=410`; `417−410=7`; arm strata total 248 and 162, leaving 3 and 4 missing values, respectively, as stated on p. 6. No qualifying lead. |
| N019 | DOC-001 p. 5; DOC-003 pp. 7-27 | SNP counts and percentages were checked against the printed Table 1 group headers and against the supplement's time-zero risk rows. The omitted genotype counts are repeated by the supplement, but Table 1 supplies no genotype-specific denominator/missingness label. **NUM-LEAD-001 recorded below.** |
| N020 | DOC-001 pp. 1, 4 | 50/251=19.92%→20%; 43/166=25.90%→26%; 37/251=14.74%→15%; 25/166=15.06%→15%. Event counts are labelled as counts/proportions, not rates. No qualifying lead. |
| N021 | DOC-001 p. 4 | Death components reconcile: `27+10=37` and `16+9=25`. Relapse/death composite is not additive because relapse and death can occur in the same participant. No qualifying lead. |
| N022 | DOC-001 pp. 1-2, 4, 6 | 5-year RFS is consistently printed as 77% versus 69%. Figure 2A values are numbers at risk and nonincrease from years 0-6; they are not event numerators for the 5-year estimate. No qualifying lead. |
| N023 | DOC-001 pp. 1, 4, 6 | 5-year OS is consistently printed as 82% versus 81%. Figure 2B values are nonincreasing numbers at risk, not event numerators or person-time. No qualifying lead. |
| N024 | DOC-001 p. 4 | Baseline and one-year 25(OH)D summaries retain the printed `ng/mL` unit; no stated identity requires a median change ratio to equal a ratio of medians. No qualifying lead. |
| N025 | DOC-001 p. 6 | 25(OH)D is consistently `ng/mL` and calcium `mg/dL`; no unit mixing is printed. Change ratios are not defined as arithmetic functions of displayed medians, so 87% was not recalculated from 21 and 41. No qualifying lead. |
| N026 | DOC-001 pp. 6, 8 | Per-protocol-until-censoring pairs reconcile: 3/227=1.32%→1.3%, 5/147=3.40%→3.4%, 2/227=0.88%→0.9%, 19/227=8.37%→8.4%, 9/147=6.12%→6.1%, 15/227=6.61%→6.6%, 8/147=5.44%→5.4%. No qualifying lead. |
| N027 | DOC-001 p. 8 | One-year-adherent safety pairs reconcile to 243/160 under one-decimal rounding: 3,6; 4,2; 20,13; 16,9. No qualifying lead. |
| N028 | DOC-001 p. 8 | Randomization-group safety pairs reconcile to 251/166 under one-decimal rounding: 3,6; 4,4; 21,15; 16,9. These are labelled as a different population from N026/N027. No qualifying lead. |
| N029 | DOC-001 pp. 1, 8 | Abstract fracture 3 (1.3%) versus 5 (3.4%) and stone 2 (0.9%) versus 0 exactly match the per-protocol-until-censoring Table 3 column, with its denominators 227/147. No qualifying lead. |
| N030 | DOC-001 pp. 3-4 | Correlation 0.92 for 19 blinded duplicates and three interim analyses are separately labelled quantities. No conflicting total/denominator is printed. No qualifying lead. |
| N031 | DOC-001 p. 6 | Observation-time medians/IQRs are outcome/model-specific person-time summaries, not arm counts, rates, or common denominators. No qualifying lead. |
| N032 | DOC-001 p. 7 | The PDF visibly prints panel-C numbers at risk despite its caption statement that they are not given because of weighting. **NUM-LEAD-002 recorded below.** |
| N033 | DOC-001 p. 7 | Subgroup/outcome-specific observation-time medians and IQRs are consistently measured in years and are not count denominators. No qualifying lead. |
| N034 | DOC-002 pp. 18, 30-31 | `240+160=400` and 240:160=3:2. A literal within-protocol comparison finds two different printed accrual stopping formulations, `>400` versus 400. **NUM-LEAD-003 recorded below.** |
| N035 | DOC-002 pp. 3, 9, 18, 23, 25, 45 | The change summary explicitly identifies 1,200 IU/day as superseded before trial start and 2,000 IU/day as final; `2×1,000=2,000 IU/day`. No qualifying lead. |
| N036 | DOC-002 p. 30 | Design inputs are internally coherent: N1=160, N2=240, N=400, E=120, p1=.4000, and 0.62/0.75 survival inputs correspond to the displayed log-rank planning context. These are planned, not observed, quantities. No qualifying lead. |
| N037 | DOC-002 pp. 25, 29 | RFS definition and censoring origin are consistent within protocol pages; no printed event count/rate is attached. No qualifying lead. |
| N038 | DOC-002 pp. 25, 29 | OS definition and censoring origin are consistent within protocol pages; no printed event count/rate is attached. No qualifying lead. |
| N039 | DOC-002 pp. 25, 29, 40-41 | Surveillance interval is 1-6 months and forms define dates/sites; no incompatible quantitative result is printed. No qualifying lead. |
| N040 | DOC-002 pp. 19, 25-26, 29, 45 | The final synopsis calls de novo cancer an adverse event and “not as an outcome,” whereas final protocol pp. 25-26 calls it a tertiary outcome; p. 45 says it was separated and inserted as tertiary. **NUM-LEAD-004 recorded below.** |
| N041 | DOC-002 pp. 21, 23, 27, 31, 45 | Final p. 31 prints high as `>40 ng/mL`, while p. 23 prints high `(40 ng/mL)` without an inequality. **NUM-LEAD-005 recorded below.** |
| N042 | DOC-002 p. 31 | The 50 gastric, 50 colorectal, and 10 esophageal patients/year describe treated patients (110); the distinct sentence assumes 80 participants/year. They are not stated as mutually exclusive enrollment components. `5×80=400` and `5+2=7` are coherent. No qualifying lead. |
| N043 | DOC-002 pp. 28, 37 | Each displayed five-place allocation block contains three A and two P assignments; 3:2 allocation is consistent. No qualifying lead. |
| N044 | DOC-002 pp. 3, 6, 18, 21-22 | External-study background survival values and P=.005 are labelled background; no trial-result comparator applies. No qualifying lead. |
| N045 | DOC-002 p. 22 | External COPD background claim is not a trial result and has no supplied same-result comparator. No qualifying lead. |
| N046 | DOC-002 pp. 38-44 | Blank forms define fields only and contain no participant values or quantitative results. No qualifying lead. |
| N047 | DOC-002 p. 32 | Administrative safe range and compensation maxima are not trial quantitative outcomes and do not share a required arithmetic identity. No qualifying lead. |
| N048 | DOC-003 p. 2 | Five at-risk strata are nonnegative and nonincreasing. Time-zero total `114+123+94+39+43=413` matches eTable 1 treatment total 248+165. No qualifying lead. |
| N049 | DOC-003 p. 3 | Five at-risk strata are nonnegative and nonincreasing. Time-zero total is again 413, matching the same average-25(OH)D analysis population. No qualifying lead. |
| N050 | DOC-003 p. 4 | Active counts sum `40+56+71+39+42=248`; within-arm percentages reconcile to 248 under rounding and total share 248/413=60.05%→60%. No qualifying lead. |
| N051 | DOC-003 p. 4 | Placebo counts sum `74+67+23+0+1=165`; within-arm percentages reconcile to 165 under rounding and total share 165/413=39.95%→40%. No qualifying lead. |
| N052 | DOC-003 p. 4 | Both arm category sums and total 413 reconcile. No qualifying lead. |
| N053 | DOC-003 p. 5 | Box plots have no printed numerical medians/quartiles/sample sizes; graphical coordinates were not treated as exact values. Unit is `ng/mL`. No qualifying lead. |
| N054 | DOC-003 p. 6 | 3/251=1.20%→1% and 4/166=2.41%→2%; `3+4=7`, agreeing with main-paper baseline missingness. Multiple imputation is stated. No qualifying lead. |
| N055 | DOC-003 p. 7 | FokI-CC risk rows are nonincreasing; time-zero 57/92 matches Table 1. No qualifying lead beyond the shared unlabelled-SNP-denominator lead in N019. |
| N056 | DOC-003 p. 8 | FokI-CT risk rows are nonincreasing; time-zero 75/117 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N057 | DOC-003 p. 9 | FokI-TT risk rows are nonincreasing; time-zero 25/36 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N058 | DOC-003 p. 10 | BsmI-AA risk rows are nonincreasing; time-zero 8/14 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N059 | DOC-003 p. 11 | BsmI-AG risk rows are nonincreasing; time-zero 23/42 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N060 | DOC-003 p. 12 | BsmI-GG risk rows are nonincreasing; time-zero 119/175 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N061 | DOC-003 p. 13 | Cdx2-GG risk rows are nonincreasing; time-zero 49/89 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N062 | DOC-003 p. 14 | Cdx2-GA risk rows are nonincreasing; time-zero 77/103 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N063 | DOC-003 p. 15 | Cdx2-AA risk rows are nonincreasing; time-zero 24/38 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N064 | DOC-003 p. 16 | ApaI-GG risk rows are nonincreasing; time-zero 69/96 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N065 | DOC-003 p. 17 | ApaI-GT risk rows are nonincreasing; time-zero 61/104 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N066 | DOC-003 p. 18 | ApaI-TT risk rows are nonincreasing; time-zero 20/31 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N067 | DOC-003 p. 19 | TaqI-TT risk rows are nonincreasing; time-zero 115/172 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N068 | DOC-003 p. 20 | TaqI-TC risk rows are nonincreasing; time-zero 31/54 matches Table 1. No qualifying lead beyond the shared N019 lead. |
| N069 | DOC-003 p. 21 | TaqI-CC risk rows are nonincreasing; time-zero 4/5 matches Table 1. Dashes for HR/CI and P=1.00 were not treated as a numeric inconsistency. No qualifying lead beyond the shared N019 lead. |
| N070 | DOC-003 p. 22 | DBP1-TT risk rows 82/54/27/7 and 134/92/53/23 are nonincreasing counts at 0/2/4/6 years. No qualifying lead beyond shared N019 denominator context. |
| N071 | DOC-003 p. 23 | DBP1-TG risk rows 59/43/21/6 and 87/63/37/9 are nonincreasing counts. No qualifying lead beyond shared N019 denominator context. |
| N072 | DOC-003 p. 24 | DBP1-GG risk rows 9/7/3/1 and 10/7/2/2 are nonincreasing counts. No qualifying lead beyond shared N019 denominator context. |
| N073 | DOC-003 p. 25 | DBP2-CC risk rows 81/52/18/6 and 115/78/49/15 are nonincreasing counts. No qualifying lead beyond shared N019 denominator context. |
| N074 | DOC-003 p. 26 | DBP2-CA risk rows 58/46/29/7 and 91/64/33/14 are nonincreasing counts. No qualifying lead beyond shared N019 denominator context. |
| N075 | DOC-003 p. 27 | DBP2-AA risk rows 11/6/4/1 and 25/20/10/5 are nonincreasing counts. No qualifying lead beyond shared N019 denominator context. |
| N076 | DOC-003 p. 28 | Men risk rows are nonincreasing; time-zero `103+173=276`, matching main-paper male total. No qualifying lead. |
| N077 | DOC-003 p. 29 | Women risk rows are nonincreasing; time-zero `63+78=141`, matching main-paper female total. No qualifying lead. |
| N078 | DOC-003 p. 30 | Age ≤65 risk rows are nonincreasing; time-zero 91/106 equals Table 1's 35-59 plus 60-65 arm rows. No qualifying lead. |
| N079 | DOC-003 p. 31 | Age >65 risk rows are nonincreasing; time-zero 75/145 equals remaining randomized patients after N078. No qualifying lead. |
| N080 | DOC-003 p. 32 | BMI <25 risk rows are nonincreasing. Quartile cut points do not create an exact cross-table sum identity at BMI 25, so no invalid subtotal was imposed. No qualifying lead. |
| N081 | DOC-003 p. 33 | BMI ≥25 risk rows are nonincreasing; time-zero pairs with N080 to 165/249, consistent with the BMI analysis population rather than asserted randomized n. No qualifying lead. |
| N082 | DOC-003 p. 34 | Esophageal risk rows are nonincreasing; time-zero 18/22 matches Table 1. No qualifying lead. |
| N083 | DOC-003 p. 35 | Gastric risk rows are nonincreasing; time-zero 68/106 matches Table 1. No qualifying lead. |
| N084 | DOC-003 p. 36 | Colorectal risk rows are nonincreasing; time-zero 79/122 matches Table 1. The three site figures total each randomized arm when combined. No qualifying lead. |
| N085 | DOC-003 p. 37 | Stage-I risk rows are nonincreasing; time-zero 67/115 matches Table 1. No qualifying lead. |
| N086 | DOC-003 p. 38 | Stage-II risk rows are nonincreasing; time-zero 48/63 matches Table 1. No qualifying lead. |
| N087 | DOC-003 p. 39 | Stage-III risk rows are nonincreasing; time-zero 51/73 matches Table 1. N085-N087 total 166/251 by arms. No qualifying lead. |
| N088 | DOC-003 p. 40 | Adenocarcinoma risk rows are nonincreasing; time-zero 147/226 matches Table 1. No qualifying lead. |
| N089 | DOC-003 p. 41 | Nonadenocarcinoma risk rows are nonincreasing; time-zero 19/25 matches Table 1. N088+N089 totals 166/251 by arms. No qualifying lead. |

## Candidate leads for human review

### NUM-LEAD-001 — Table 1 SNP percentages use unlabelled, variable denominators rather than the printed group headers

- **Relationship IDs:** N019, with exact supplement repetitions N055-N075.
- **Category for later human consideration:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** [DOC-001 main article — PDF p. 5](<../../../jama_urashima_2019_oi_190023.pdf#page=5>) Table 1, headed “Vitamin D (n = 251)” and “Placebo (n = 166)”; [DOC-003 supplement — PDF pp. 7-27](<../../../joi190023supp2_prod.pdf#page=7>) eFigure 3A-U time-zero risk rows.
- **Printed inputs/comparators:** Table 1 FokI totals are Vitamin D `92+117+36=245` and placebo `57+75+25=157`; BsmI `14+42+175=231` and `8+23+119=150`; Cdx2 `89+103+38=230` and `49+77+24=150`; ApaI `96+104+31=231` and `69+61+20=150`; TaqI `172+54+5=231` and `115+31+4=150`; DBP1 `134+87+10=231` and `82+57+9=148`; DBP2 `115+91+25=231` and `81+58+11=150`. The only relevant Table 1 footnote says percentages may not total 100% because of rounding. Each corresponding eFigure time-zero row repeats its Table 1 count.
- **Rule and reproducible calculation:** A percentage printed under a column headed `n=251` or `n=166` should use that denominator unless a subgroup-specific available-case denominator/missingness is supplied. For example, Cdx2 Vitamin D `89/230=38.70%`, `103/230=44.78%`, and `38/230=16.52%`, matching printed 39%, 45%, and 17%; these cannot be obtained using 251. Cdx2 placebo `49/150=32.67%`, `77/150=51.33%`, `24/150=16.00%`, matching printed 33%, 51%, and 16%; these cannot be obtained using 166. The same count deficits occur in the other SNP sets listed above. Repeated eFigure time-zero counts confirm transcription but do not provide denominators.
- **Tolerance:** Whole-percentage rounding tolerance ±0.5 percentage points. Deficits from the Table 1 headers are integer count differences (for example, Cdx2 21/251 and 16/166), so cannot be explained by rounding.
- **Direct observation:** The table header names randomized arm sizes 251 and 166, while multiple SNP rows sum to smaller totals and their percentages match smaller, variable denominators; no SNP-specific missingness/available-case footnote appears in the table.
- **Inference:** The figures may be based on successfully genotyped subsets, but the available denominators and reasons for differences are not printed. This is not an assertion that any genotype count is incorrect.
- **Alternative source-grounded interpretations:** Different assays may have had unavailable specimens or uncalled genotypes; the risk-table repetition is compatible with this. The current table footnote, however, explains only rounding and not the count deficits.
- **Quality-control relevance:** An extractor could use the column headers as denominators, producing incorrect genotype proportions or subgroup sample sizes.
- **Exact human question:** What was the available denominator and missing/failed-genotype count for each SNP by randomized arm, and should Table 1 label those denominators or add a missingness footnote?

### NUM-LEAD-002 — Figure 3 caption denies panel-C risk numbers that are visibly printed

- **Relationship ID:** N032.
- **Category for later human consideration:** Numeric or arithmetic inconsistency.
- **Exact source location:** [DOC-001 main article — PDF p. 7](<../../../jama_urashima_2019_oi_190023.pdf#page=7>) Figure 3 and its caption.
- **Printed inputs/comparators:** Under panel C (“Death, baseline 25(OH)D level 20-40 ng/mL”), the visual risk table prints placebo `90, 88, 70, 51, 34, 22, 11` and Vitamin D `142, 139, 115, 88, 61, 41, 20` at years 0-6. The caption on that page states: “Numbers at risk for panel C are not given because of weighting.”
- **Rule and reproducible comparison:** A caption assertion that panel-C numbers are not given conflicts with a visible row of panel-C numbers. This is a direct text-versus-figure presence comparison; no calculation is required.
- **Tolerance:** Exact logical comparison; no numeric rounding tolerance applies.
- **Direct observation:** Both the caption statement and the two panel-C risk rows are printed on the same PDF page.
- **Inference:** One of the two figure elements may be a carryover/editing error, or “because of weighting” may refer to an unstated different kind of risk number.
- **Alternative source-grounded interpretations:** The rows may have been intended for a neighboring panel during layout, or the caption may have been retained after risk numbers were added. The PDF does not resolve which is intended.
- **Quality-control relevance:** A reader cannot determine whether to treat the displayed panel-C rows as valid analysis denominators.
- **Exact human question:** Were the displayed panel-C risk rows intended to be reported, and if so, should the caption’s statement that they are not given be removed or revised?

### NUM-LEAD-003 — Final protocol states two different planned accrual stopping thresholds

- **Relationship ID:** N034.
- **Category for later human consideration:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** [DOC-002 protocol/SAP — PDF p. 18](<../../../joi190023supp1_prod.pdf#page=18>) Protocol synopsis, Study period; [DOC-002 protocol/SAP — PDF p. 31](<../../../joi190023supp1_prod.pdf#page=31>) Statistical analysis, Study period.
- **Printed inputs/comparators:** Page 18 says, “Accrual, if the number of randomized patients reaches >400, then entry is stopped.” Page 31 says, “After enrolling 400 patients, enrollment will finish.” The sample-size section specifies total `N=400`, Vitamin D `n=240`, placebo `n=160`.
- **Rule and reproducible comparison:** A stopping rule at `>400` permits enrollment at 400 and stops only after exceeding it, whereas “after enrolling 400” states a 400-patient stopping threshold. This is an exact comparator of the two printed threshold conditions, not an arithmetic error in `240+160=400`.
- **Tolerance:** Exact integer threshold comparison; no rounding tolerance applies.
- **Direct observation:** Both threshold formulations appear in the final protocol/SAP.
- **Inference:** The authors may have intended `>400` to account for block randomization or may have used “after enrolling 400” as shorthand for the target sample size.
- **Alternative source-grounded interpretations:** The main article's observed 417 randomized participants is compatible with a target rather than an absolute cap, but it cannot determine which protocol wording was operative.
- **Quality-control relevance:** Planning/extraction users may misstate whether 400 was a target, a cap, or a trigger to close accrual.
- **Exact human question:** Which final accrual rule was operative—stop at 400 randomized participants or stop after the total exceeded 400—and should the other protocol statement be corrected?

### NUM-LEAD-004 — Final protocol gives incompatible labels for de novo cancer

- **Relationship ID:** N040.
- **Category for later human consideration:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-002 protocol/SAP — PDF p. 19](<../../../joi190023supp1_prod.pdf#page=19>) Protocol synopsis, Safety outcomes; [DOC-002 protocol/SAP — PDF pp. 25-26](<../../../joi190023supp1_prod.pdf#page=25>) Outcome Measures; [DOC-002 protocol/SAP — PDF p. 45](<../../../joi190023supp1_prod.pdf#page=45>) Summary of changes.
- **Printed inputs/comparators:** Page 19 says de novo cancer after starting supplementation “will be included as an adverse event, not as an outcome.” Pages 25-26 list “De novo cancer” under “Tertiary outcome.” Page 45 says it was separated from secondary and safety outcomes and inserted as tertiary outcome.
- **Rule and reproducible comparison:** The same defined event cannot simultaneously be labelled “not as an outcome” and a “tertiary outcome” in the same final protocol version without a qualification distinguishing these labels. This is an exact label/definition comparison; no numerical rounding applies.
- **Tolerance:** Exact categorical-label comparison; no numeric tolerance applies.
- **Direct observation:** The conflicting labels and change summary are printed in the supplied protocol.
- **Inference:** The synopsis may be outdated relative to the body/change summary, rather than describing a different analysis population or time period.
- **Alternative source-grounded interpretations:** The phrase “adverse event” may be intended to describe clinical ascertainment while “tertiary outcome” describes reporting hierarchy, but the protocol supplies no such distinction.
- **Quality-control relevance:** Extractors may classify de novo cancer differently when deriving safety-event denominators, endpoint sets, or protocol-versus-publication comparisons.
- **Exact human question:** In the final protocol, was de novo cancer a tertiary outcome, an adverse event only, or both under distinct definitions that should be explicitly stated?

### NUM-LEAD-005 — Final protocol omits the high-stratum inequality in one subgroup definition

- **Relationship ID:** N041.
- **Category for later human consideration:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-002 protocol/SAP — PDF p. 23](<../../../joi190023supp1_prod.pdf#page=23>) Study design, Specific Aim 1; [DOC-002 protocol/SAP — PDF p. 31](<../../../joi190023supp1_prod.pdf#page=31>) Subgroup analyses; corroborating final-protocol sources [DOC-002 PDF pp. 21, 27](<../../../joi190023supp1_prod.pdf#page=21>) and main article [DOC-001 PDF p. 5](<../../../jama_urashima_2019_oi_190023.pdf#page=5>).
- **Printed inputs/comparators:** Page 23 defines low `<20 ng/mL`, middle `≥20 to ≤40 ng/mL`, and high `(40 ng/mL)`. Page 31 defines high `>40 ng/mL`. The main article Table 1 also prints High `>40`.
- **Rule and reproducible comparison:** Given a middle stratum ending at `≤40 ng/mL`, the high stratum must state an inequality or otherwise identify whether 40 itself belongs to high. The page-23 text contains the threshold value but no operator, unlike the page-31 `>40 ng/mL` comparator.
- **Tolerance:** Exact symbol/label comparison; no rounding tolerance applies.
- **Direct observation:** The quoted p. 23 and p. 31 definitions are printed in the final protocol.
- **Inference:** The omitted greater-than sign on p. 23 may be a typographical omission, with p. 31 and the published table expressing the intended definition.
- **Alternative source-grounded interpretations:** Parenthetical `(40 ng/mL)` could be informal shorthand for `>40 ng/mL`; without the comparator it is not a complete boundary specification.
- **Quality-control relevance:** A reviewer could misclassify participants at or around 40 ng/mL or use overlapping/nonexhaustive subgroup boundaries.
- **Exact human question:** Should the p. 23 high-stratum label explicitly read `>40 ng/mL`, matching p. 31 and the main article, and is this the definition used in analysis?

## Limitations

- This numeric check does not determine whether a lead is valid or what correction, if any, is appropriate.
- The PDF does not provide individual-level data, SNP assay-call logs, available-case denominator labels, or the intended layout/edit history for Figure 3 and the protocol synopsis.
- Model-derived survival estimates, hazard ratios, confidence intervals, and P values are outside this numeric checker except where they establish a count, label, or denominator relationship. No candidate was created for any display-zero P value.
