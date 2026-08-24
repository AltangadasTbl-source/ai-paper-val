# Fresh Support Quantitative Evidence Mapping

Scope: DOC-002 `joi190122supp1_prod.pdf`, PDF pp. 1-33; DOC-003 `joi190122supp2_prod.pdf`, PDF pp. 1-19; DOC-004 `joi190122supp3_prod.pdf`, PDF p. 1. Evidence came only from the fresh native/layout text and, for DOC-003 pp. 17-19, the fresh rendered PNGs. No legacy audit derivative was used.

## Page coverage

| Source and pages | Fresh evidence / result-relevant content |
|---|---|
| DOC-002 pp. 1-3 | Protocol title, date, roster/contact material only; no study-result display. |
| DOC-002 pp. 4-10 | Background/planning only. Concrete definitions/comparators: parent trial 20,000, factorial vitamin D3 2,000 IU/d vs placebo and EPA+DHA 840 mg/d vs placebo; proposed diabetes subcohort 1,500; baseline/year 4 specimens. p. 5 defines abnormal ACR >=30 mg/g and eGFR <60 mL/min/1.73m2. No current trial result. |
| DOC-002 pp. 11-16 | Original protocol aims, eligibility, enrollment, randomization, collection, dose and units; mapped below. |
| DOC-002 pp. 17-20 | Original protocol outcome definitions, ANCOVA equations, planned power; mapped below. |
| DOC-002 pp. 21-30 | Protocol safety/monitoring and references; no current trial result. p. 21 repeats planned D3/EPA+DHA doses and safety comparisons. p. 23 supplies one concrete interim-monitoring definition: Haybittle-Peto z=3 / P=.0027. |
| DOC-002 pp. 31-33 | 2016 analytic-plan addendum, primary/secondary definitions, linear mixed-model equations, imputation, interaction, power; mapped below. |
| DOC-003 pp. 1, 5 | Cover/index and references only; no additional quantitative result. |
| DOC-003 pp. 2-4 | Assay QC/harmonization definitions and numeric calibration facts; mapped below. |
| DOC-003 pp. 6-16 | eTables 1-11, all result-relevant displayed values; mapped below. |
| DOC-003 pp. 17-19 | eFigures 1-3, fresh visual reading; mapped below. |
| DOC-004 p. 1 | Data-sharing statement: availability yes; deidentified participant data/data dictionary, from 2019-11-08; reproduction of trial results after proposal approval. No outcome result. |

## Protocol and analysis definitions (DOC-002)

- p. 11: original aims: D3 2,000 IU/d and EPA+DHA 840 mg/d, each versus placebo; albuminuria and GFR over 4 years. Parent 2x2 randomization; planned mean 5-year follow-up; diabetes cohort 1,500.
- pp. 12-14: men >=60 y, women >=65 y; parent trial N=20,000; ancillary target N=1,500. Run-in 3-6 months. Of 40,000 initially willing/eligible, projected 50% (n=20,000) randomized; projected 3,000 with diagnosed diabetes. Randomization stratified by 5-year age group in blocks of eight, two per each factorial combination.
- pp. 15-16: baseline and year-4 urine; year-4 blood (baseline blood parent trial); two 5-mL urine cryovials, six 2-mL aliquots; D3 2,000 IU=40 micrograms daily, nonstudy allowance <=800 IU/d; EPA+DHA 840 mg/d in 1,000-mg capsule, EPA:DHA 40:30.
- p. 17: original primary outcome percent ACR change = `(ACR4-ACR0)/ACR0`; secondary eGFR change=`eGFR4-eGFR0`. eGFR equation: `177.6 x SCr^-0.65 x CysC^-0.57 x age^-0.20 x (0.82 female) x (1.11 black)`; SCr mg/dL, CysC mg/L. Composite: ACR increase 100% plus ACR4 >=30 mg/g; eGFR loss >=12 mL/min over 4 y; ESRD or death.
- pp. 18-20: interaction on additive and multiplicative scales; ACR ANCOVA and eGFR ANCOVA. beta2/exp(beta2)-1 definitions; two-sided alpha .05, no multiplicity correction. Original power: N=1,500 / 1,200 follow-up (20% loss), 90% for 17% ACR and 2.6 mL/min/1.73m2 eGFR differences; table reports ACR 15/17/19/21/23/25% -> 81/90/96/98/>99/>99%, eGFR 2.0/2.2/2.4/2.6/2.8/3.0 ->71/79/85/90/94/97%. Composite assumptions: 17% albuminuria progression, 17% rapid loss, ESRD <1%, death about 4.6%, joint 20-30%; 80% power RR .69-.76, 90% RR .65-.73.
- p. 23: planned interim monitoring uses Haybittle-Peto rule, z=3 standard deviations / P=.0027, with multiple-look adjustment; it pertains to parent-trial interim endpoints and is not a reported VITAL-DKD result.
- pp. 32-33: addendum changes primary outcome to eGFR5-eGFR0; secondary ACR at years 2/5, >=40% eGFR loss, composite (rapid loss/ESRD/death). ITT is persons with >=1 follow-up biosample; 10 chained-equation imputations, Rubin rules. Linear mixed model time j=0,2,5; beta6 interaction P<.05. Treatment effect beta3, 95% CI and P, inference reserved year 5; ACR log transformed. Prespecified DKD: ACR >=30 mg/g or eGFR <60 mL/min/m2; adherent >=80%. Simulation 2,000 replications, N=1,058 (80%) and 80% power for 2.3 mL/min/1.73m2 year-5 difference.

## DOC-003 laboratory calibration (pp. 2-4)

Five QC levels; 20 serum and 20 urine QC samples, each measured >=8 times. Cystatin-C post-shift ERM mean observed 5.96/5.961 mg/L vs expected 5.49 mg/L; post-shift values multiplied by 5.49/5.961. Pre-to-post harmonization equation: `0.006801 + 1.037603*(pre-shift concentration)`. Post-harmonization r=.999. Creatinine within 4.5% of NIST; no transform for creatinine, urine albumin, or urine creatinine.

## DOC-003 result tables and figures

- p. 6 eTable 1: adherence entries are N (% among questionnaire responders); point adherence >=2/3 medication. Vitamin-D overall 6m 1208(97), y1 1174(95), y2 1079(92), y3 1029(91), y4 984(91), y5 709(88); through y2 1194(91), through y5 1032(79). Omega-3: 1208(97),1177(95),1077(91),1031(92),987(91),721(89); through y2 1193(91), through y5 1032(79). Group values are fully preserved in `support_numeric_relationships.md`.
- pp. 7-8 eTables 2-3: medication percentages use nonmissing N=1312 baseline, 988 y2, 916 y5. All/active/placebo factorial counts and percentages for every displayed medication and time are preserved in `support_numeric_relationships.md`.
- p. 9 eTable 4 (complete baseline/year-5 population N=932): vitamin-D active/placebo baseline N495/437, eGFR 86.2/85.4; y5 74.2/72.5, changes -12.0/-12.8, difference .87 (-.83,2.58), P=.32. Omega-3 active/placebo N470/462; baseline 86.0/85.6; y5 73.7/73.2, changes -12.4/-12.4, difference .09 (-1.61,1.80), P=.92.
- p. 10 eTable 5 (adherent): vitamin D y5 active/placebo N461/404, means 74.4/72.6, changes -12.0/-12.8, difference .89 (-.74,2.52), P=.28; omega-3 N438/426 means 73.8/73.3, changes -12.1/-12.5, difference .42 (-1.22,2.06), P=.61.
- pp. 11-14 eTables 6-9: ACR geometric means, change ratios, active:placebo ratios and P values fully preserved in `support_numeric_relationships.md`; model adjusts age/sex and uses multiple imputation. Primary full eTable 6 y5: D3 ratio .99 (.84,1.17), P=.90; omega-3 .96 (.81,1.14), P=.64.
- p. 15 eTable 10: exploratory/post-hoc Cox results fully preserved in numeric/statistical records. HRs and 95% CIs: D3 1.03(.68,1.58), .82(.64,1.05), .82(.61,1.09), .79(.59,1.06), P=.88,.12,.17,.12; omega-3 1.07(.70,1.63), .96(.75,1.23), .89(.66,1.19), .86(.64,1.15), P=.77,.77,.44,.31.
- p. 16 eTable 11: safety event counts, all outcomes and arms, fully preserved in numeric record; counts are participants reporting >=1 occasion.
- p. 17 eFigure 1: changes 25(OH)D and omega-3 index baseline-y2 vs eGFR baseline-y5; all-data participants; correlations r=-.05 and r=-.02, respectively.
- pp. 18-19 eFigures 2-3: subgroup Ns, geometric-mean change ratios, ratio-of-change axes and interaction P values fully preserved in numeric record. Visual evidence shows participant-count columns that map to the opposite factorial arms; the overall change values remain aligned with their printed headings. Observations are recorded below without C IDs.

## Candidate observations, not candidate IDs

1. DOC-003 p. 18 eFigure 2 prints `Placebo` N=703 and `Active intervention` N=609, although randomized vitamin-D active/placebo totals are 703/609. Its overall changes 3.02 placebo and 2.97 active agree with eTable 6 under the printed headings. Only the overall and nested participant-count columns reproducibly map to the opposite arms; no C ID assigned here.
2. DOC-003 p. 19 eFigure 3 prints `Placebo` N=659 and `Active intervention` N=653, although randomized omega-3 active/placebo totals are 659/653. Its overall changes 3.05 placebo and 2.94 active agree with eTable 6 under the printed headings. Only the overall and nested participant-count columns reproducibly map to the opposite arms; no C ID assigned here.

Limitations: DOC-003 eFigures 2-3 print their subgroup estimates graphically; the fresh 180-dpi render permits reading displayed Ns, geometric means/SDs and interaction P values, but the individual forest-plot ratio/CI values are not printed as text. No OCR was needed or used.
