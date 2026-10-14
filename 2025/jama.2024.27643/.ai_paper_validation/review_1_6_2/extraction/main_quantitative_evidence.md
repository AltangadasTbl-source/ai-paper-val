# Main quantitative evidence map

Runtime agent: /root/main_mapper. Stage: fresh main_quantitative_mapper. Source: DOC-001, `jama_berry_2025_oi_240158_1742927563.7361.pdf`, REPORT. Scope: all PDF pages 1–12 (printed pages 1138–1149). This is source-linked reconstruction only; no candidate diagnosis or adjudication. Mapper-local identifiers M001–M100 identify relationship bundles; numeric and statistical reviewers assign final N/S identifiers. Each bundle includes all printed cells or statements named within it rather than one identifier per scalar.

## Assets and complete page coverage

Canonical inputs: `.ai_paper_validation/document_outputs/DOC-001/preprocessing/native_pages/page-01.txt` through `page-12.txt`; these are reusable native/layout locators. All twelve were read. Source-matched reusable `.ai_paper_validation/document_outputs/DOC-001/preprocessing/page_images/page-05.png` through `page-08.png` were visually inspected for Figure 1, Table 1, Figure 2, Table 2, and Figure 3. Engine provenance for these retained derivatives is recorded in evidence_asset_inventory.md (legacy extraction; CPU rendered images, historical version unavailable). No new extraction, rendering, or OCR produced. No fresh-required DOC-001 unit exists. Native text is usable; figure values and alignment were confirmed visually. Every direct source remains final authority.

| PDF page | Mapped content | Coverage |
|---|---|---|
| 1 | Abstract design, allocation, primary result, demographics, completion, safety | COMPLETE |
| 2 | Key Points; randomization; endpoint and analysis definitions; prior-study quantities | COMPLETE |
| 3 | Endpoint scales, exploratory outcomes, NfL analysis sets, sample size, population and statistical methods | COMPLETE |
| 4 | Significance/hierarchy; complete results narrative; primary and secondary results | COMPLETE |
| 5 | All Figure 1 counts, exclusions, follow-up, primary analysis sets, caption | COMPLETE |
| 6 | Every Table 1 cell and footnote; continuation of survival narrative | COMPLETE |
| 7 | Figure 2 all numeric vectors/captions; every Table 2 row and footnote; exploratory event analyses | COMPLETE |
| 8 | Figure 3 all labels/vectors/caption; biomarker, subgroup, safety results | COMPLETE |
| 9 | Discussion counterparts, 13-event statement, limitation assumptions; article metadata | COMPLETE |
| 10 | Author roles, affiliations and disclosures; no additional applicable quantitative result | COMPLETE; no-applicable result content |
| 11 | Disclosures, funding, governance, references; no additional applicable quantitative result | COMPLETE; no-applicable result content |
| 12 | Reference list/end matter only; no additional applicable quantitative result | COMPLETE; no-applicable result content |

Evidence links below are relative to this file (three levels below package root), ending in truthful PDF page anchors. Repeated labels p.N identify PDF pages. No inferred denominator silently replaces a printed denominator. Blank table cells are explicitly retained as blank, not converted into printed zeros.

## Design, analysis, and decision relationships

| ID | Exact location | Printed relationship and reconstruction keys |
|---|---|---|
| M001 | [p.1 abstract](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=1); p.2 Methods | Phase 2/3 multicenter randomized double-blind platform trial; regimen C; 54 US sites; July 2020–March 2022; final follow-up March 17, 2022. Regimen randomization open; treatment allocation blinded to participants/investigators. |
| M002 | pp.1–2 allocation | 161 randomized in regimen; active 120, regimen placebo 41; active 60 mg/day 61 and 30 mg/day 59; ratio 3:3:2; duration 24 weeks; additional concurrent other-regimen placebo 123. Stratification edaravone and/or riluzole use. Distinguish within-regimen n=161 from full analysis n=284. |
| M003 | p.1 primary measure; p.2 Outcomes; p.3 primary methods | Change in disease severity baseline through week 24 integrating ALSFRS-R and survival via Bayesian shared parameter model. DRR is functional slope ratio or survival HR within respective components; common increase/decrease in disease progression relative to control. DRR <1 benefit. |
| M004 | pp.2–3 endpoint definitions | ALSFRS-R total scale 0–48, higher better function. CAFS joint-rank function/survival, higher ranks beneficial; SVC is maximum slow exhalation after maximal inhalation, converted to PPN, higher better respiratory function. Three clinical secondary outcomes: CAFS, SVC decline, PAV-free survival. |
| M005 | p.3 exploratory outcome inventory | Prespecified biomarkers NfL, serum creatinine, urinary p75 extracellular domain. Clinical exploratory outcomes handheld dynamometry, quantitative motor speech, home vital capacity, ALSFRS-R domains, ALSAQ and domains, CNS-BFS. Time-to-event: 3 end-point cutoffs (example ALSFRS-R decline at least 6 points) and 8 clinical events (including assisted ventilation, feeding tube, first SAE hospitalization, first ALS-related SAE hospitalization). |
| M006 | p.3 NfL analysis-set statements | Serum NfL prespecified in full analysis set including other-regimen placebo; plasma prespecified regimen-only. Serum samples rerun with each individual's samples on one plate; shared placebo comparison not conducted; presented serum analysis post hoc regimen-only. Match to Figure 3 and p.8 narrative. |
| M007 | p.3 sample size | Simulations; 160 per regimen; active pooled:placebo 3:1 with shared concurrent controls; approximately 80% power; detect 30% slowing common to mortality/function; 1-sided type I rate <2.5%. No standalone sample-size formula or complete simulation inputs printed. |
| M008 | p.3 populations | Full analysis: all randomized active, all randomized regimen placebo, all shared concurrent placebo. Additional prespecified regimen-only efficacy analysis. Safety: regimen participants initiating treatment plus specified-regimen placebo initiators not known ineligible for focal regimen. |
| M009 | p.3 CAFS methods | Every active participant pairwise compared with each placebo participant using survival time and ALSFRS-R change; sum scores then rank; mean ranks compared; Wilcoxon rank-sum statistical test. |
| M010 | p.3 SVC methods | Repeated measures linear mixed model and random slopes model; centered months since symptom onset, delta-FRS, baseline riluzole, edaravone, and interactions with time. Missing data MAR conditional observed data/model structure. |
| M011 | p.3 survival methods | Cox model; vital status at last randomized clinical trial visit. PAV defined >22 hours/day for >7 consecutive days. Covariates prebaseline ALSFRS-R slope, months since symptom onset, baseline riluzole, baseline edaravone, baseline age. Exclude no follow-up or event at baseline from time-to-event models, retain in functional models. Table 2 covariates separately mapped M079. |
| M012 | pp.3–4 decisions | Primary Bayesian significance posterior Pr(DRR<1) ≥0.979, calibrated by simulations. If primary significant, secondary sequence CAFS → SVC → survival, comparison-wise 2-tailed P<.05; stop declarations after first failed endpoint; sequential closed testing controls overall type I rate 5%; nominal secondary P also reported without multiplicity adjustment. All missing data MAR given observed data/model structure. |
| M013 | p.3 analysis implementation | Primary combined dosages versus placebo; prespecified individual-dosage analyses. SAS 9.4 and R 4.1.2. |
| M014 | p.4 Trial participants | No early-futility cutoff met; trial completed as planned. All focal-regimen randomized participants received assigned drug and confirmed initiation. |
| M015 | p.2 introduction; p.9 limitation | Background SOD1 variations approximately 2% of ALS; prior phase 2 CNM-Au8 sporadic-ALS cohort 45. Current intervention elimination half-life 28 days, randomized duration 24 weeks; discussion says steady state only latter part. Historical cohort is background, not current analysis denominator. |

## Abstract, narrative and participant-flow relationships

| ID | Exact location | Printed values and matching keys |
|---|---|---|
| M016 | p.1 abstract demographics | Regimen randomized n=161, mean age 58.4 y; females 61 (37.9%); completed 145 (90%). Corresponding baseline/body demographic and flow locations pp.4–6. |
| M017 | p.1 abstract efficacy; p.2 Key Points | Combined dosages/shared placebo primary DRR .97; 95% CrI .783–1.175; posterior Pr(DRR<1) .65; primary and three secondaries suggest no benefit or harm. Key Points repeats .97, 161/120/41 plus123, 24 weeks, no significant benefit/harm. p.9 conclusion repeats no primary benefit. |
| M018 | p.1 abstract safety | Active n=120 vs safety placebo n=163: diarrhea 23 (19%) vs12 (7%); nausea17 (14.2%) vs14 (8.6%); fatigue12 (10.8%) vs30 (18.4%); muscular weakness24 (20%) vs45 (27.6%). Body safety counterpart p.8 and supplement eTable5 locator. |
| M019 | p.4 screened/randomized narrative | Focal screened163; pre-randomization died1 and window timeout1; randomized161: 59/61/41. Other-regimen placebo123; compare Figure1. |
| M020 | p.4 completion narrative | Analysis population placebo85%, CNM-Au8 92%; dose30 completion93%, dose60 completion90% on assigned drug. Drug discontinued before week24: placebo5, pooled active6 (3+3 by dosage). RCT deaths: regimen placebo1, dose30 1, dose60 3. These are drug/completion/death statements; do not silently replace with Figure1 follow-up labels. |
| M021 | p.4 demographic narrative | Focal randomized mean age57.7 y; females37.9%; 98% non–Hispanic or Latino White. Pooled active vs shared placebo: clinically definite48% vs40%; possible or probable laboratory-supported16% vs35%; King's1 11% vs21%. Regimen placebo BMI28.4 vs pooled active27.0. |
| M022 | p.4 baseline narrative | Plasma NfL regimen placebo75.7 (IQR48.5–105.8), dose30 92.2 (59.7–120.6), dose60 75.0 (51.0–110.9) pg/mL. Riluzole76%–80%, edaravone20%–26%, both19%–23%. Mean baseline ALSFRS-R described similar; eTable1 distribution locator. |
| M023 | [p.5 Figure1](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=5) root | Master assessed815; excluded128: inclusion/exclusion121, early termination4, withdrew consent2, timeout1. Remaining focal assigned163 and other assigned524. |
| M024 | p.5 Figure1 focal arm | Focal163 minus2 (died1, timeout1) → randomized161; allocated30 mg59,60 mg61, regimen placebo41. |
| M025 | p.5 Figure1 other arms | Other assigned524; excluded32 (timeout10, declined consent9, early termination7, eligibility5, died1); randomized other placebo123, other active369. Combined placebo164 =41+123. |
| M026 | p.5 Figure1 dose30 follow-up |59 randomized; discontinued follow-up4: terminated early3,died1; completed24-week follow-up55; primary analysis59. |
| M027 | p.5 Figure1 dose60 follow-up |61 randomized; discontinued follow-up6: terminated early2,died3,withdrew1; completed55; primary analysis61. |
| M028 | p.5 Figure1 regimen placebo follow-up |41 randomized; discontinued6: terminated early2,died1,withdrew1,lost1; completed35; primary analysis41. |
| M029 | p.5 Figure1 combined placebo follow-up |164 randomized; discontinued27: terminated early17,died3,withdrew2,lost3,sponsor terminated2; completed137; primary analysis164. Regimen placebo is nested, not an additional group to sum with combined placebo. |
| M030 | p.5 Figure1 footnotes |Multiple exclusion reasons permitted. Common exclusions SVC not ≥50% (46%), clinically significant unstable other condition (31%), investigational ALS treatment within5 half-lives or30 days whichever longer (17%). Common early termination before randomization travel/other study; after randomization progression/perceived lack efficacy. No exact numerator supplied for these percentages. |

## Table 1: complete baseline matrix

Column order in every row below: CNM-Au8 30 mg n=59; CNM-Au8 60 mg n=61; shared placebo n=164; regimen placebo n=41. Shared placebo includes regimen-specific and other-regimen placebo (footnote a). All cells located [p.6 Table1](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=6). Counts default to column denominator unless an explicit fraction is printed. No baseline P values printed.

| ID | Characteristic | 30 mg | 60 mg | Shared placebo | Regimen placebo |
|---|---|---|---|---|---|
| M031 | Female, n (%) |26 (44.1)|23 (37.7)|49 (29.9)|12 (29.3)|
| M032 | Male, n (%) |33 (55.9)|38 (62.3)|115 (70.1)|29 (70.7)|
| M033 | Asian, n (%) |blank|blank|2/160 (1.2)|blank|
| M034 | Black or African American, n (%) |blank|blank|6/160 (3.8)|2 (4.9)|
| M035 | White, n (%) |59 (100.0)|61 (100.0)|151/160 (94.4)|38 (92.7)|
| M036 | Multiple races, n (%) |blank|blank|1/160 (0.6)|1 (2.4)|
| M037 | Not Hispanic or Latino, n (%) |56 (94.9)|60/60 (100.0)|157/163 (96.3)|38 (92.7)|
| M038 | Age, mean (SD), y |57.7 (10.2)|58.6 (9.9)|57.2 (11.3)|57.0 (11.7)|
| M039 | BMI, mean (SD), kg/m² |27.4 (5.3)|26.6 (4.8)|27.3 (5.0)|28.4 (5.5)|
| M040 | Bulbar onset, n (%) |10 (16.9)|8 (13.1)|29 (17.7)|6 (14.6)|
| M041 | Clinically definite ALS, n (%) |28 (47.5)|30 (49.2)|66 (40.2)|14 (34.1)|
| M042 | Clinically probable ALS, n (%) |22 (37.3)|21 (34.4)|40 (24.4)|10 (24.4)|
| M043 | Clinically probable–laboratory-supported, n (%) |8 (13.6)|8 (13.1)|42 (25.6)|16 (39.0)|
| M044 | Clinically possible, n (%) |1 (1.7)|2 (3.3)|16 (9.8)|1 (2.4)|
| M045 | King's stage1, n (%) |3 (5.1)|10 (16.4)|34 (20.7)|9 (22.0)|
| M046 | King's stage2, n (%) |18 (30.5)|18 (29.5)|39 (23.8)|11 (26.8)|
| M047 | King's stage3, n (%) |22 (37.3)|19 (31.1)|45 (27.4)|7 (17.1)|
| M048 | King's stage4a/4b nutritional failure, n (%) |1 (1.7)|blank|1 (0.6)|blank|
| M049 | King's stage4b respiratory failure, n (%) |15 (25.4)|14 (23.0)|45 (27.4)|14 (34.1)|
| M050 | Riluzole baseline, n (%) |45 (76.3)|49 (80.3)|126 (76.8)|32 (78.0)|
| M051 | Edaravone baseline, n (%) |12 (20.3)|16 (26.2)|41 (25.0)|10 (24.4)|
| M052 | Months since symptom onset, mean (SD) |21.2 (8.6)|24.2 (8.5)|21.9 (8.7)|21.9 (8.5)|
| M053 | Months since diagnosis, mean (SD) |9.8 (5.2)|11.1 (6.6)|10.3 (6.1)|10.0 (5.6)|
| M054 | SVC, PPN, mean (SD) |74.4 (16.0)|76.0 (16.3)|76.0 (16.5)|76.1 (16.8)|
| M055 | ALSFRS-R total, mean (SD) |34.5 (5.8)|34.0 (7.3)|35.1 (6.7)|36.1 (5.91)|
| M056 | ALSFRS-R bulbar, mean (SD) |9.8 (2.1)|10.0 (2.5)|10.0 (2.3)|10.6 (2.1)|
| M057 | ALSFRS-R fine motor, mean (SD) |7.3 (2.7)|6.9 (3.4)|7.6 (3.1)|7.8 (3.4)|
| M058 | ALSFRS-R gross motor, mean (SD) |7.2 (2.8)|6.7 (3.2)|7.3 (3.1)|7.3 (2.8)|
| M059 | ALSFRS-R combined motor, mean (SD) |14.4 (4.9)|13.6 (5.7)|14.9 (5.4)|15.1 (5.4)|
| M060 | ALSFRS-R respiratory, mean (SD) |10.3 (2.4)|10.5 (2.0)|10.2 (2.1)|10.3 (2.0)|
| M061 | Prebaseline ALSFRS-R slope, points/month, mean (SD) |0.8 (0.6)|0.7 (0.5)|0.7 (0.4)|0.6 (0.4)|
| M062 | Serum NfL, median (IQR), pg/mL |67.6 (44.3–91.6)|62.5 (44.4–95.1)|NA|51.6 (33.0–76.4)|
| M063 | Plasma NfL, median (IQR), pg/mL |92.2 (59.7–120.6)|75.0 (51.0–110.9)|NA|75.7 (48.5–105.8)|

M064: p.6 all Table1 footnotes. Footnote b says race unknown/unreported for3 participants, ethnicity1. El Escorial definitions: definite UMN+LMN in3 CNS regions; probable at least2 regions with UMN rostral; laboratory-supported UMN/LMN only1 region or UMN alone1 region with EMG LMN ≥2 limbs; possible UMN+LMN together1 region, UMN alone≥2 regions, or LMN rostral when laboratory-supported criteria cannot be established; exclusion of other diagnoses. King's staging5 stages:1 one region,2 second,3 third,4 nutritional/respiratory failure,5 death. ALSFRS-R0–48 higher better. BMI kg/m². These definitions key category partition and scale checks.

## Primary, secondary, survival and other time-to-event results

| ID | Exact source location | Printed analysis/result |
|---|---|---|
| M065 | [p.4 primary efficacy](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4) | Pooled active/shared placebo at24 weeks: DRR .97 (95% CrI .783–1.175), posterior Pr<1 .65. Regimen-only DRR .96 (95% CrI .709–1.357); source text's closing punctuation retained as typography, numeric limits clear. |
| M066 | p.4 primary functional component | Bayesian ALSFRS-R mean slope shared placebo −1.03 points/month (95% CrI −1.176 to−.892), pooled active −1.00 (−1.153 to−.858). |
| M067 | p.4 primary survival component | Shared-parameter model mortality .007 events/month shared placebo versus .006 pooled active. Figure2 and eTable2 locators; no component interval printed here. |
| M068 | p.4 CAFS | Mean rank shared placebo143.9 vs pooled active140.5; Wilcoxon P=.51. Baseline-NfL adjusted sensitivity P=.88, unchanged inference. |
| M069 | p.4 SVC main narrative | Text labels mean change over24 weeks: pooled active −9.32 PPN per month (dose30 −7.84; dose60 −10.79), shared placebo −8.53 PPN per month; difference −.78 PPN/month (95% CI −4.25 to2.68). eTables3A/3B locator. Labels and time window are recorded verbatim; not converted by mapper. |
| M070 | p.4 SVC sensitivity | Baseline-NfL sensitivity described mean change over24 weeks: pooled active −1.73 PPN/month (95% CI −2.18 to−1.29), shared placebo −1.55 PPN/month (−1.94 to−1.17). |
| M071 | p.4 PAV/death and exclusions | To week24: dose30 1/59,dose60 4/61,shared placebo9/162. Text: "Of those, 4 of the 41 participants in the regimen placebo group and 2 in the shared placebo group were excluded due to having no follow-up time (1 had PAV at baseline and 1 terminated early at baseline visit)." Record sentence exactly for comparison to Table2 footnote; mapper makes no change. |
| M072 | p.4 PAV/death sensitivity | Pooled vs shared adjusted cumulative HR .46 (95% CI .12–1.49); baseline-NfL sensitivity .45 (.11–1.50). Main counterpart Table2 and Figure2B. |
| M073 | [p.7 Table2](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7) row1; pp.4,6 | Pooled active5/120 (narrative4.2%) vs shared9/162 (5.6%); adjusted Cox HR .46 (.12–1.49); P=.22. |
| M074 | p.7 Table2 row2; pp.4,6 | Dose30 1/59 (1.7%) vs shared9/162 (5.6%); HR .06 (.002–.56); P=.04. |
| M075 | p.7 Table2 row3; p.6 | Dose60 4/61 (6.6%) vs shared9/162 (5.6%); HR .96 (.25–3.08); P=.95. |
| M076 | p.7 Table2 row4/narrative | Pooled5/120 (4.2%) vs regimen4/41 (9.8%); HR .25 (.05–1.09); P=.06. |
| M077 | p.7 Table2 row5; pp.6–7 | Dose30 1/59 (1.7%) vs regimen4/41 (9.8%); HR .03 (.0004–.36); P=.03. |
| M078 | p.7 Table2 row6/narrative | Dose60 4/61 (6.6%) vs regimen4/41 (9.8%); HR .47 (.10–2.16); P=.32. |
| M079 | p.7 Table2 footnotes | Table title Survival Analyses; comparison column PAV-free survival. Footnote a:2 shared-placebo excluded for no follow-up:1 baseline PAV,1 early termination at baseline. Footnote b:age, sex, time since symptom onset, prebaseline ALSFRS-R slope, baseline riluzole, baseline edaravone. Footnote c:CI from profile log-likelihood. None of these HRs stated crude. |
| M080 | p.7 exploratory event paragraph | Combined active vs within-regimen placebo, baseline-covariate adjusted: assisted ventilation16 (18%) vs9 (31%), HR .40 (.17–1.01); gastrostomy14 (12%) vs7 (17%), HR .37 (.14–1.04); first ALS-related SAE hospitalization5 (4%) vs3 (7%), HR .23 (.04–1.33); first SAE hospitalization14 (12%) vs7 (18%), HR .48 (.18–1.33). No printed denominators or P values in paragraph; baseline exclusions/risk sets must come from linked supporting analysis. |
| M081 | p.9 discussion survival | Prespecified exploratory30-mg but not60-mg nominal survival benefit after baseline covariate adjustment; small numbers described as total13 events in RCT shared-placebo plus combined active. Time-to-event exploratory point estimates favorable; not statistically significant; no multiplicity control for many exploratory outcomes. |

## Figure 2 complete numeric and visual map

M082: p.7 Figure2A. X week ticks0,4,8,12,16,20,24. Y ALSFRS-R score change ticks10,5,0,−5,−10,−15,−20,−25. Groups regimen C placebo, pooled CNM-Au8, shared placebo. Every box: lower/upper quartiles25th/75th, median horizontal line; whiskers extreme points within1.5 IQR, outliers solid circles; points raw means; solid curves covariate-adjusted modeled change. Regimen-placebo estimated curve borrows other-regimen placebo information. Graphically all three modeled trajectories decline similarly from0 to roughly−5.5 at24 weeks; there are no printed numeric curve/box ordinates, so exact endpoint means, medians, quartiles and outlier values are not recoverable from typography and are not invented. Supplied plotted marks are visually inspected, not omitted.

M083: Figure2A printed "No. of participants at risk" vectors, weeks0/4/8/12/16/20/24: shared154/151/148/147/145/140/140; pooled active115/115/111/112/109/110/111; regimen placebo37/36/36/37/35/35/34. Caption defines counts as known ALSFRS-R outcomes at each visit and excludes all ALSFRS-R data from participants with death or death-equivalent PAV. Thus these are contributor counts, not silently assumed survival risk sets.

M084: Figure2B title Kaplan-Meier mortality; y mortality probability ticks0,.04,.08,.12,.16,.20; x week0,4,8,12,16,20,24,28. Solid lines KM death/PAV; dashed model-estimated exponential mortality curves active versus pooled placebo. Both plotted probabilities increase, shared KM ends visually around.073, active around.042; exact unprinted ordinates not digitized. Caption jointly names death and PAV despite short panel title.

M085: Figure2B shared-placebo "participants exposed (events)" at0/4/8/12/16/20/24/28 weeks:164(1),162(0),162(0),160(1),158(2),155(3),115(2),0(1). Count and event vectors both fully transcribed. Sum printed event cells10; no interpretation of time-bin boundaries imposed.

M086: Figure2B pooled active exposed(events), same weeks:120(0),120(0),120(0),120(0),118(2),115(3),91(0),1(0). Sum event cells5. Figure x axis extends28 although title disease severity over24 weeks. Match with M067 modeled rates, M073 observed proportions and M081 RCT-event statement using documented endpoint/window definitions.

## Biomarker, Figure 3 and safety relationships

| ID | Exact location | Printed values, labels, population/window/model keys |
|---|---|---|
| M087 | [p.8 serum narrative](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8) | Regimen-only rerun serum NfL: placebo geometric mean43.1 baseline→56.5 pg/mL week24, +30.8%; pooled active60.6→60.8, +.4%. Treatment difference −23.2% geometric mean ratio (95% CI −39.5% to−2.5%), P=.03. Figure3B repeats. |
| M088 | p.8 serum post hoc outlier sensitivity | Very low excluded <4 pg/mL or <2% maximum for given participant; removed1 placebo baseline observation from1 participant. Active geometric change+.8%, placebo+11.6%, treatment difference−9.7% (95% CI−18.5% to.1%), P=.05; eFigure locator. Magnitude but not direction sensitive to outlier. |
| M089 | p.8 plasma narrative | Placebo72.8→78.5 pg/mL, geometric increase7.9%; active80.3→78.5, decrease2.3%; treatment difference−9.5% geometric mean ratio (95% CI−17.8 to−.4%), P=.04. eTables3A/3B and Figure3A locators. |
| M090 | p.8 Figure3A numeric annotation | Week24 least-squares mean difference−9.5% (95% CI−17.8% to−.5%); P=.04. Label y least-squares geometric mean ratio; ticks.9,1.0,1.1,1.2; x week(postbaseline)0,4,8,12,24; actual plotted measurements0,4,8,24. Baseline normalized1; placebo curves rise, active curves fall. No other exact plotted means/intervals printed. |
| M091 | p.8 Figure3A evaluable vectors | At0/4/8/24: active118/111/110/105; placebo41/38/35/34. There is no printed evaluable vector entry under12. |
| M092 | p.8 Figure3B numeric annotation | Week24 least-squares mean difference−23.2% (95% CI−39.5% to−2.5%); P=.03. Y least-squares geometric mean ratio; ticks.8,1.0,1.2,1.4,1.6,1.8; x0,8,12,16,24; measurements0,8,16,24. Baseline normalized1; placebo rises, active essentially unchanged. No exact unprinted intermediate curve values or error-bar bounds assigned. |
| M093 | p.8 Figure3B evaluable vectors | At0/8/16/24: active112/107/97/95; placebo39/32/33/33. No evaluable entry under12. |
| M094 | p.8 Figure3 caption methods | Samples baseline,4(plasma only),8,16,24; natural-log transform before analysis; least-squares mean difference at each point; back-transform comparison placebo versus combined doses. Plasma placebo+7.9%, serum+30.8%, active plasma−2.3%, serum+.4%; nominal P=.04/.03. Distinguish displayed tick12 from caption measurement schedule and plasma vector; no unprinted16-week plasma count invented. |
| M095 | p.8 subgroup and other outcomes | No predefined subgroup significant ALSFRS-R progression differences combined active vs shared placebo; eTable4 locator. No other exploratory combined/dose-specific results suggesting benefit vs placebo; eTables3A/3B locator. No subgroup estimate or interval printed in main. |
| M096 | p.8 safety population/exposure | Active120, shared safety placebo163. ≥1 treatment-emergent AE: active93%, placebo90%; few dosing interruptions; eTable5 locator. |
| M097 | p.8 safety event percentages | ≥5 percentage points more common: diarrhea19% vs7%, nausea14.2% vs8.6%; ≥5 points less common: fatigue10.8% vs18.4%, muscular weakness20% vs27.6%. Counts printed in abstract M018. |
| M098 | p.8 serious TEAE | Shared placebo9%, dose30 10%, dose60 16%, regimen placebo17%; P=.31. No SAE/no death considered drug-related. eTable5 locator. Compare safety denominators M096 and dose denominators M002; no SAE counts invented. |
| M099 | pp.8–9 interpretation matching | Primary/secondary no benefit over24 weeks, dose-combined or separate. NfL nominal24-week difference; serum/plasma placebo rise, pooled active no rise. Missing-at-random mixed-model assumption includes death; discussion calls few deaths. No multiplicity correction exploratory; survival nominal/hypothesis generating. |
| M100 | pp.9–12 end matter | p.9 conclusion/limitations already mapped M081/M099/M015; article information, roster, affiliations, contributions, disclosures, funding and bibliography supply no further current-study result-relevant numbers. Reference bibliographic volumes/pages/DOIs, addresses and funding-role text were inspected and excluded from quantitative result mapping as no-applicable content. |

## Cross-location match index and completeness

Allocation/analysis n: M002/M008/M016/M019/M023–M029/M096. Primary DRR: M003/M012/M017/M065–M067/M082–M086. Baseline demographics: M016/M021/M022/M031–M064. Completion/attrition/death: M016/M020/M026–M029/M071/M073–M086. Secondary function/respiratory results: M004/M009/M010/M068–M070. Survival specification: M011/M012/M071–M081/M084–M086. Biomarker specification/results: M005/M006/M062/M063/M087–M094/M099. Safety: M008/M018/M096–M098. These keys preserve different analysis populations, windows, models and effect measures for downstream alignment; no findings selected by mapper.

All12 direct-source units mapped;12 reusable-backed,0 fresh-required,0 scientific coverage gaps. Relationship bundle count100. No direct-source numeric diagram/image is uninspected. Main publication does not print exact Figure2 box coordinates or intermediate Figure3 LS geometric means/bounds; visual marks are covered as graphically encoded evidence, and exact values require supplied supplement/model tables rather than invented precision. No OCR limitation affects coverage. There are no main-paper person-time totals, standalone test statistics or standard errors printed beyond monthly modeled event rates, interval and P-value relationships explicitly mapped above.

## Direct-source transcription correction during checking

Numeric reviewer freshly rendered source PDF p5 with PyMuPDF1.28.0, CPU200dpi, as preprocessing/numeric/main-p05.png. Coordinator visually confirmed Figure1 regimen-placebo follow-up prints 1 Died, not the initially transcribed3 in M028. M028 now reads1. This current-run derivative transcription correction creates no source finding; all legacy assets and the supplied PDF remain unchanged. Primary Figure1 printed subtotal6 and four listed reason counts2,1,1,1 are retained literally for precision-aware checking.
