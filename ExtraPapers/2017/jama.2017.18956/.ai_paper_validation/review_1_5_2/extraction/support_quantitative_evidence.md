# Support-source quantitative evidence mapping

## Scope and evidence basis

Complete fresh mapping of `DOC-002` (`joi170144supp1_prod.pdf`, protocol, PDF pp. 1-16) and `DOC-003` (`joi170144supp2_prod.pdf`, online supplement, PDF pp. 1-4).  Locations below are truthful PDF locations in the supplied direct sources (`joi170144supp1_prod.pdf#page=N` and `joi170144supp2_prod.pdf#page=N`).  Native and layout text were freshly prepared for every assigned page; rendered pages were consulted where the fresh inventory identifies a dense result display (DOC-002 pp. 3, 4, 12-14; DOC-003 pp. 2-4).  No legacy audit derivative or external source was used.

This is an evidence map, not a candidate ledger or consistency disposition.  **Numeric/reporting** flags relationships for later numeric/cross-source allocation; **Inferential/statistical** flags relationships for later statistical allocation.  A comparison key specifies the population, treatment contrast, outcome definition, time point, measure, and precision needed to match main-paper evidence rather than assuming same-named outcomes are identical.

## DOC-002 — Protocol (pp. 1-16)

### Page-level coverage

| PDF page | Result-relevant content / coverage result |
|---:|---|
| 1 | Title page only; no result-relevant quantitative unit. |
| 2 | Abbreviations only; definitions `SPTB`, `OR`, `CI`, `GA`, and `SD` support later interpretation, but no displayed result. |
| 3 | Protocol summary: objective, eligibility threshold, and planned design. |
| 4 | Planned randomization gestational-age window, duration, estimated sample, and primary outcome. |
| 5 | Background only; literature burden values (15 million births, 1.1 million deaths) are not a study result or concrete supplied-package comparator. No applicable mapped result unit. |
| 6 | Repeats planned objective/outcome threshold. |
| 7 | Study design, arms, age and cervical-length eligibility definitions. |
| 8 | Exclusions, prior-SPTB definition, gestational-age ascertainment. |
| 9 | Outcome ascertainment, SPTB definition, cervical-length measurement/selection rule. |
| 10 | Intervention follow-up, progesterone threshold/dose/time limit. |
| 11 | Randomization allocation/strata and primary/initial secondary outcome list. |
| 12 | Remaining secondary outcomes and composite definition. |
| 13 | Sample-size assumptions and planned descriptive summaries. |
| 14 | Planned primary and secondary inferential analyses. |
| 15 | References only; no applicable mapped result unit. |
| 16 | References only; no applicable mapped result unit. |

### Protocol definitions, population, and outcome keys

| Location | Type | Printed planned definition or quantity | Cross-match key / use |
|---|---|---|---|
| DOC-002 p. 3 | Numeric/reporting | Objective: reduce rate of `SPTB <34 weeks`; population is asymptomatic singleton pregnancies with no prior SPTB and short TVU CL. Study population threshold: `TVU CL ≤25 mm`. | `P0; arms=pessary versus no pessary; endpoint=SPTB<34 gestational weeks; eligibility=singleton/no-prior-SPTB/TVU-CL≤25 mm`. Match DOC-001 pp. 1, 3, 5 and Table 2. |
| DOC-002 p. 4 | Numeric/reporting | Randomization GA `18 0/7–23 6/7`; estimated sample `300` singleton pregnancies; stated primary outcome `SPTB <34 weeks`; study period `2 years` (`1` enrollment + `1` analysis), enrollment estimated Oct 2016-Oct 2017. | `P0` eligibility/timing and planned `N=300`; comparison with DOC-001 pp. 1-3/flow. Administrative period is context, not an observed outcome. |
| DOC-002 p. 6 | Numeric/reporting | Repeats planned endpoint: cervical pessary expected to reduce rate of `SPTB <34 weeks`. | Same `P0`; duplicate protocol location retained. |
| DOC-002 p. 7 | Numeric/reporting | Prospective single-center randomized trial; intervention `pessary`, control `no pessary`; inclusion age `18-50 years`, singleton gestation, no prior SPTB, `TVU CL ≤25 mm`. | `P0`; match main methods and baseline/flow population. |
| DOC-002 p. 8 | Numeric/reporting | Prior SPTB = spontaneous preterm delivery from `16 0/7` through `36 6/7` weeks in prior pregnancy. Excludes membranes ruptured, structural/chromosomal abnormality, fetal death, cerclage/pessary in situ, bleeding, placenta previa/accreta, ballooning membranes, `TVU CL=0 mm`, contractions; GA determined by menstrual history confirmed by first-trimester CRL or anatomy-scan head circumference. | `P0-definition-prior-SPTB` and `P0-eligibility`; affects correct population matching only. |
| DOC-002 p. 9 | Numeric/reporting | Pregnancy outcome source: hospital maternity records; PTB classified medically indicated versus spontaneous. `SPTB` includes spontaneous labor or PPROM. Cervical length is measured three times, during/after `30 seconds` fundal pressure; shortest CL is recorded; examination minimum `5 minutes`. | `P0-outcome-definition=SPTB (labor or PPROM) <34 wk`; `P0-exposure-measure=shortest TVU CL`. Match main pp. 3-4, especially outcome/table labels. |
| DOC-002 p. 10 | Numeric/reporting | Both groups followed monthly until delivery. At any follow-up, TVU CL/adverse events recorded. For `TVU CL ≤20 mm`, both groups recommended vaginal progesterone `200 mg` suppositories daily until `36 6/7` weeks. | `P0-cointervention=progesterone if CL≤20 mm; dose=200 mg/d; stop=36 6/7 wk`; match DOC-001 pp. 1, 3-4 and DOC-003 p. 4 progesterone subgroup denominators. |
| DOC-002 p. 11 | Numeric/reporting | 1:1 allocation to pessary/control; random blocks `2, 4, 6`; stratified by CL (`≤20 mm`, `>20–25 mm`). Pessary removed `37 0/7–37 6/7` weeks unless early clinical indication. | `P0-allocation=1:1; CL strata≤20 versus >20-25`; match DOC-001 pp. 1-4/flow and any subgroup label. |
| DOC-002 pp. 11-12 | Numeric/reporting | Planned primary `SPTB <34 weeks`. Planned secondary: SPTB `<37`, `<32`, `<28` weeks; mean GA at delivery (weeks); mean latency (randomization-to-delivery, days); PPROM `<34` weeks; mode of delivery; maternal side effects; chorioamnionitis (histopathological inflammation); birth weight; NICU; neonatal death (live-born death within first `28 days`); perinatal death (fetal or neonatal mortality); composite adverse perinatal outcome = ≥1 of NEC, IVH grade `≥3`, RDS, BPD, ROP requiring therapy, blood-culture proven sepsis, neonatal death. | Separate keys `P0-primary-SPTB<34` and `P0-secondary-{SPTB thresholds,GA,latency,PPROM,delivery,adverse,chorio,birthweight,NICU,death,composite}`. Compare definitions/labels with DOC-001 Table 2 (p. 5) and components/post-hoc table DOC-003 p. 3. |

### Protocol sample-size and descriptive-plan relationships

| Location | Type | Printed relationship | Cross-match key / calculation inputs |
|---|---|---|---|
| DOC-002 pp. 12-13 | Inferential/statistical | Sample-size design seeks a `50%` reduction in overall spontaneous preterm delivery between randomization and `33 6/7` weeks, from anticipated `25%` in control (singletons with short cervix using vaginal progesterone). | `P0-power-endpoint=overall SPTB through 33 6/7 wk; assumed control risk=25%; target relative reduction=50%`. This is a planned power endpoint and needs population/outcome matching before comparison with observed SPTB `<34 weeks`. |
| DOC-002 p. 13 | Numeric/reporting | Assumes `60%` of eligible women agree/provide follow-up; about `500` approached for final `300`; planned `150 per group`; simulation used. Institutional context: about `3000` deliveries/y, `55000` regional deliveries/y, about `600` counselled/y, about `500` eligible singleton/no-prior-SPTB/y. | `P0-planned-N=300; group-N=150; approach-N≈500; expected participation=60%`. Observed randomization/retention comparison key: DOC-001 p. 3 flow and p. 4 results. Other hospital/regional counts are feasibility context, not observed trial data. |
| DOC-002 p. 13 | Numeric/reporting | Baseline plan: median/IQR; continuous data: mean, SD, minimum, maximum, quartiles; attribute data: frequency counts/proportions. | `P0-descriptive-convention`; compare only where a concrete reported display claims a matching statistic. |

### Protocol inferential-analysis definitions

| Location | Type | Printed plan | Cross-match key / required matching fields |
|---|---|---|---|
| DOC-002 p. 14 | Inferential/statistical | Primary analysis is intention-to-treat by assigned treatment at randomization; two-tailed `5%` level; `95% CI` for OR of intervention/control group. Incidence of `SPTB <34 weeks` to be quantified by `OR (95% CI)` using logistic regression with cervical length covariate. | `P0-primary-model=adjusted logistic OR intervention/control; covariate=CL; 95% CI; two-tailed α=.05; ITT`. Compare to DOC-001 p. 4 stated analysis change and p. 5 Table 2 (reported unadjusted RR/difference) only after measure/model matching. |
| DOC-002 p. 14 | Inferential/statistical | Secondary analysis: Kaplan-Meier risk of `SPTB <34`; gestational age time scale; spontaneous delivery event; elective deliveries censored; hazard ratios estimated. | `P0-survival=KM SPTB<34; time=GA; event=spontaneous delivery; censor=elective delivery; measure=HR`. Match DOC-001 pp. 4-6 narrative/Figure 2 only after confirming which event definition and time horizon each panel uses. |
| DOC-002 p. 14 | Numeric/reporting | Planned software `SPSS` (IBM, Armonk, NY). | Context key `P0-software`; no numerical reconciliation by itself. |

## DOC-003 — Online supplement (pp. 1-4)

### Page-level coverage

| PDF page | Result-relevant content / coverage result |
|---:|---|
| 1 | Supplement index names eTables 1-3; no additional quantitative result values. |
| 2 | eTable 1: vaginal-swab and antibiotic counts/percentages at randomization, plus non-mutually-exclusive abnormal-result/therapy counts. |
| 3 | eTable 2: 13 post hoc secondary outcomes, each with arm count/percentage, absolute between-group difference/95% CI, RR/95% CI, and P value; definitions/footnotes supplied. |
| 4 | eTable 3: four post hoc subgroup rows for SPTB <34 weeks, subgroup denominators/percentages, differences/RRs/CIs/P values, plus two interaction P values and test definitions. |

### eTable 1: vaginal swabs at randomization (DOC-003 p. 2)

**Table key:** `T1; population=randomized women at randomization; arms=pessary N=150 versus control N=150; measure=count (percentage) unless otherwise stated.`  The data-presented footnote says number (percentage).  Cross-match with DOC-001 p. 4/Table 1 and trial-flow arm totals on p. 3.

| Row / exact label | Pessary group (N=150) | Control group (N=150) | Type and comparison key |
|---|---:|---:|---|
| Positive vaginal swab at randomization, n (%) | 36 (24.0%) | 41 (27.3%) | Numeric/reporting; `T1-positive-swab`; match DOC-001 Table 1, p. 4. |
| Antibiotics for positive vaginal swab, n (%) | 33 (22.0%) | 38 (25.3%) | Numeric/reporting; `T1-antibiotics-positive-swab`; match DOC-001 Table 1 p. 4 and its narrative. |
| Bacterial vaginosis: abnormal results n / antibiotic therapy n | 30 / 30 | 34 / 34 | Numeric/reporting; `T1-organism=bacterial-vaginosis; display=count only`. Component categories may overlap; do not sum them without an exclusivity statement. |
| Candida: abnormal results n / antibiotic therapy n | 3 / 0 | 3 / 0 | Numeric/reporting; `T1-organism=Candida; display=count only`; comparator includes no therapy. |
| Escherichia coli: abnormal results n / antibiotic therapy n | 1 / 1 | 2 / 2 | Numeric/reporting; `T1-organism=E-coli; display=count only`. |
| Ureoplasma: abnormal results n / antibiotic therapy n | 1 / 1 | 1 / 1 | Numeric/reporting; `T1-organism=Ureoplasma; display=count only`. |
| Group B streptococcus: abnormal results n / antibiotic therapy n | 1 / 1 | 1 / 1 | Numeric/reporting; `T1-organism=GBS; display=count only`. |

### eTable 2: post hoc secondary outcomes (DOC-003 p. 3)

**Table key:** `T2; population=all randomized participants; arms=pessary N=150/control N=150; post hoc exploratory outcomes; displayed measures=count (percentage), between-group difference in percentage points (95% CI), RR (95% CI), and continuity-corrected chi-square P value.`  `Overall preterm birth` is explicitly either spontaneous or indicated preterm birth.  There was no multiple-comparison adjustment; boldface marks statistically significant values.  The table’s `RR` is relative risk and `CI` confidence interval.  Asterisks identify reasons for iatrogenic preterm birth; they are not missing values.

| Outcome | Pessary | Control | Difference in % (95% CI) | RR (95% CI) | P value | Type / cross-match key |
|---|---:|---:|---:|---:|---:|---|
| Overall preterm birth `<37 weeks` | 35 (23.3%) | 53 (35.3%) | -12.0 (-22.5 to -1.2) | 0.66 (0.46 to 0.95) | 0.03 | Inferential/statistical + numeric/reporting; `T2-overall-PTB<37; type=spontaneous+iatrogenic; post-hoc`. Do not equate with DOC-001 Table 2 `SPTB<37`. |
| Overall preterm birth `<34 weeks` | 14 (9.3%) | 26 (17.3%) | -8.0 (-16.1 to -0.1) | 0.54 (0.29 to 0.99) | 0.04 | Inferential/statistical + numeric/reporting; `T2-overall-PTB<34; type=spontaneous+iatrogenic; post-hoc`. Distinct from primary SPTB `<34`. |
| Overall preterm birth `<32 weeks` | 11 (7.3%) | 15 (10.0%) | -2.7 (-4.2 to +9.7) | 0.73 (0.35 to 1.54) | 0.54 | Inferential/statistical + numeric/reporting; `T2-overall-PTB<32; type=spontaneous+iatrogenic`. |
| Overall preterm birth `<28 weeks` | 7 (4.7%) | 9 (6.0%) | -1.3 (-4.4 to +7.1) | 0.78 (0.30 to 2.03) | 0.80 | Inferential/statistical + numeric/reporting; `T2-overall-PTB<28; type=spontaneous+iatrogenic`. |
| Iatrogenic preterm birth `<34 weeks` | 3 (2.0%)* | 3 (2.0%)** | 0 (-4.1 to +4.1) | 1.00 (0.21 to 4.88) | 1.00 | Inferential/statistical + numeric/reporting; `T2-iatrogenic-PTB<34`. `*`: one nonreassuring fetal heart rate nonstress test, two preeclampsia; `**`: one IUGR, two preeclampsia. |
| Birth weight `<2500 grams` | 28 (18.7%) | 45 (30.0%) | -11.3 (-1.1 to +21.2) | 0.62 (0.41 to 0.94) | 0.03 | Inferential/statistical + numeric/reporting; `T2-birthweight<2500g; unit=grams`. |
| Birth weight `<1500 grams` | 10 (6.7%) | 15 (10.0%) | -3.3 (-3.5 to +10.2) | 0.67 (0.31 to 1.44) | 0.40 | Inferential/statistical + numeric/reporting; `T2-birthweight<1500g; unit=grams`. |
| Necrotizing enterocolitis | 3 (2.0%) | 4 (2.7%) | -0.7 (-3.5 to +5.0) | 0.75 (0.17 to 3.29) | 0.99 | Inferential/statistical + numeric/reporting; `T2-NEC; component=planned composite`. |
| Intraventricular hemorrhage grade 3 or 4 | 4 (2.7%) | 6 (4.0%) | -1.3 (-3.5 to +6.2) | 0.67 (0.19 to 2.31) | 0.75 | Inferential/statistical + numeric/reporting; `T2-IVH-grade3or4; component=planned composite`. |
| Respiratory distress syndrome | 14 (9.3%) | 31 (20.7%) | -11.4 (-19.9 to -2.9) | 0.45 (0.25 to 0.81) | 0.01 | Inferential/statistical + numeric/reporting; `T2-RDS; component=planned composite`. |
| Bronchopulmonary dysplasia | 8 (5.3%) | 12 (8.0%) | -2.7 (-3.5 to +9.0) | 0.67 (0.28 to 1.58) | 0.49 | Inferential/statistical + numeric/reporting; `T2-BPD; component=planned composite`. |
| Retinopathy of prematurity requiring therapy | 1 (0.7%) | 9 (6.0%) | -5.3 (-10.4 to -0.9) | 0.11 (0.01 to 0.87) | 0.02 | Inferential/statistical + numeric/reporting; `T2-ROP-treatment; component=planned composite`. |
| Blood-culture proven sepsis | 9 (6.0%) | 13 (8.7%) | -2.7 (-3.8 to +9.3) | 0.69 (0.31 to 1.57) | 0.50 | Inferential/statistical + numeric/reporting; `T2-sepsis; component=planned composite`. |

### eTable 3: subgroup analyses for SPTB <34 weeks (DOC-003 p. 4)

**Table key:** `T3; outcome=SPTB<34 gestational weeks; post hoc subgroups; within-subgroup comparison=pessary versus control; displayed data=number/total number (percentage), difference percentage points (95% CI), RR (95% CI), continuity-corrected chi-square P value.`  The interaction P values use a Wald test.  Boldface identifies statistically significant displayed results. `SPTB` means spontaneous preterm birth; `TVU CL` means transvaginal-ultrasound cervical length.

| Subgroup variable / level | Pessary | Control | Difference % (95% CI) | RR (95% CI) | Within-level P | Interaction P | Type / cross-match key |
|---|---:|---:|---:|---:|---:|---:|---|
| Progesterone therapy | 10/133 (7.5%) | 21/125 (16.8%) | -9.3 (-17.7 to -1.0) | 0.45 (0.22 to 0.91) | 0.04 | 0.56 | Inferential/statistical + numeric/reporting; `T3-progesterone=yes; outcome=SPTB<34; denom=133/125`. Denominators match DOC-001 p. 3 flow and p. 4 Table 1 eligibility/cointervention counts. |
| No progesterone therapy | 1/17 (5.9%) | 2/25 (8.0%) | -2.1 (-21.8 to +21.0) | 0.74 (0.07 to 7.48) | 0.99 | 0.56 (same subgroup-variable interaction) | Inferential/statistical + numeric/reporting; `T3-progesterone=no; outcome=SPTB<34; denom=17/25`. Complements to 150 in each arm with prior row. |
| TVU CL `≤10 mm` | 3/56 (5.4%) | 10/42 (23.8%) | -18.4 (-34.6 to -3.3) | 0.23 (0.07 to 0.77) | 0.02 | 0.46 | Inferential/statistical + numeric/reporting; `T3-CL≤10mm; outcome=SPTB<34; denom=56/42`. Match DOC-001 Table 1 p. 4 CL category counts. |
| TVU CL `>10 mm` | 8/94 (8.5%) | 13/108 (12.0%) | -3.5 (-5.8 to +12.5) | 0.71 (0.31 to 1.63) | 0.56 | 0.46 (same subgroup-variable interaction) | Inferential/statistical + numeric/reporting; `T3-CL>10mm; outcome=SPTB<34; denom=94/108`. Complements to 150 in each arm with prior row. |

## Explicit matched-result index for later cross-source review

| Support evidence key | Exact support location | Intended main-paper match / necessary distinctions |
|---|---|---|
| `P0-primary-SPTB<34` | DOC-002 pp. 3-4, 6, 11, 14 | DOC-001 p. 1 abstract, p. 3 outcome definition, p. 5 Table 2. Match *spontaneous* PTB, <34 weeks, arm comparison, ITT population; distinguish planned adjusted OR from reported RR. |
| `P0-planned-N=300` / `P0-allocation` | DOC-002 pp. 4, 11, 13 | DOC-001 pp. 1, 3-4: 300 randomised, 150 per arm, no loss; check only matched concepts, not feasibility estimates. |
| `P0-progesterone-CL≤20` | DOC-002 p. 10 | DOC-001 pp. 1, 3-4 and DOC-003 p. 4; distinguish prescription rule from receipt/subgroup membership. |
| `P0-secondary-definitions` | DOC-002 pp. 11-12 | DOC-001 pp. 3, 5 and DOC-003 p. 3. Distinguish pre-specified SPTB outcomes and composite components from post hoc **overall** (spontaneous + indicated) PTB/component results. |
| `P0-primary-model` | DOC-002 p. 14 | DOC-001 p. 4 says original prespecified logistic-OR analysis changed to unadjusted RR, and p. 5 displays RR. Match measure, adjustment, and model before any comparison. |
| `P0-survival` | DOC-002 p. 14 | DOC-001 pp. 4-6: Kaplan-Meier/Cox descriptions and figure panels. Confirm whether all-delivery versus spontaneous-delivery event/censoring definitions and reported HR correspond before reconciliation. |
| `T1-positive-swab`, `T1-antibiotics` | DOC-003 p. 2 | DOC-001 p. 4 Table 1 and narrative. Arm N=150; compare counts/proportions at randomization. Do not derive a total across microbial rows because overlap/exclusivity is unstated. |
| `T2-*` | DOC-003 p. 3 | DOC-001 p. 5 narrative/Table 2 where applicable. eTable results are post hoc; `Overall PTB` includes spontaneous + indicated, so it is not the Table 2 SPTB endpoint. Components map to the composite definition but are not necessarily additive. |
| `T3-*` | DOC-003 p. 4 | DOC-001 p. 4 baseline CL/progesterone denominators, p. 5 primary SPTB totals, p. 6 subgroup-interaction narrative. Match subgroup denominator, SPTB<34 outcome, and test type. |

## Mapping limitations

- DOC-002 is a prospective protocol: its numerical statements are planned assumptions, definitions, feasibility context, or analysis specifications, not observed results.
- DOC-003 reports table displays with limited detail about CI construction beyond its stated chi-square continuity correction for P values. No unreported model or CI method was inferred.
- Microbial abnormal-result rows in eTable 1 have no statement of mutual exclusivity; they must not be summed to evaluate the positive-swab total without a source-grounded overlap rule.
- The protocol’s sample-size endpoint is phrased as spontaneous preterm delivery through `33 6/7` weeks, whereas observed documents commonly label an endpoint `<34 weeks`; locations retain both wordings for later adjudication rather than treating them as identical automatically.
