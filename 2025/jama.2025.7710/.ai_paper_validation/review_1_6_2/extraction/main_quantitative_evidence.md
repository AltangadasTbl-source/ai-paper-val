# Main quantitative evidence map

Document: DOC-001, REPORT, `jama_kumar_2025_oi_250034_1750956984.08518.pdf`, current SHA-256 `10ab2f532b03f65d1d84bc8e8a2a3a14e3b24a76f204123acd7049d67f7b73e3`. Scope: every PDF page 1-11, fresh-required. No legacy main extraction or scientific conclusion was used. Values below are transcriptions and relationship locators, without candidate diagnosis.

## Extraction provenance and page coverage

Native and sorted-reading-order layout were freshly extracted from the supplied PDF using the recorded package-local interpreter and `workflow_1_6_2/scripts/pdf_tools.py text`, `--first 1 --last 11`, with and without `--layout`. Engine: PyMuPDF 1.26.4, CPU. Derivatives: `preprocessing/main/main-native.txt`, `preprocessing/main/main-layout.txt`. Both contain all 11 page records. `preprocessing/main/page-8.png` is a fresh CPU PyMuPDF 1.26.4 rendering at 200 dpi, visually inspected for Figure 2 and Table 4 alignment. OCR was unnecessary. All direct-source locations below use physical PDF page numbers; printed pages are 149-159. Full freshly extracted native evidence is retained at the end of this artifact, including every narrative occurrence and footnote.

| PDF page | Content inspected | Mapping | Status |
|---|---|---|---|
| 1 | Title, abstract, design, population, intervention, outcomes, all abstract results | N001-N007, S001-S003 and matching table IDs | COMPLETE |
| 2 | Key Points, eligibility, registration, prior phase 2 contextual result | N008-N010, S004 | COMPLETE |
| 3 | Randomization, intervention, endpoint hierarchy, sample size, interim rule, statistical methods | N011-N013, S005-S014 | COMPLETE |
| 4 | Figure 1, follow-up, missing pH, subgroup/safety/statistical definitions, demographics narrative | N014-N023, S015-S018 | COMPLETE |
| 5 | Every Table 1 row and footnote, adherence and birth narrative | N024-N060 | COMPLETE |
| 6 | Every Table 2 row and footnote, primary/secondary and sensitivity narrative | N061-N092, S019-S020 | COMPLETE |
| 7 | Every Table 3 row and footnote, subgroup, site, tertiary, safety and discussion narrative | S021-S034, N093-N097 | COMPLETE |
| 8 | Every Figure 2 row, axes, caption and footnote; every Table 4 row and footnote | S035-S065 | COMPLETE |
| 9 | Site interaction continuation, contextual prior evidence, limitations, conclusions | N098-N100, S066-S068 | COMPLETE |
| 10 | Article information and references 1-21 | No additional applicable trial quantitative results; date/analysis-access metadata retained in full text | COMPLETE |
| 11 | References 22-41 | No applicable trial quantitative relationship; bibliography retained in full text | COMPLETE |

## Reading conventions

In the numeric tables, columns always compare sildenafil citrate with placebo, in that order. Unless specified otherwise, Table 1/2 cells are No. (%); counts are observed contributor counts, not person-time. Means are explicitly distinguished from medians. IQR, range, SD, units and row-specific denominators are preserved. In statistical tables, absolute differences are sildenafil minus placebo in percentage points, and the printed ratio contrast is sildenafil vs placebo. All intervals are printed 95% CIs. No standard errors or numerical test statistics are printed. No rates per person-time or person-time quantities are printed. Statistical labels are retained rather than converting model estimates to crude estimates.

## Numeric, population and reporting relationships

| ID | Exact location | Quantity / population / time | Sildenafil citrate | Placebo / comparator | Matching occurrences or definition |
|---|---|---|---|---|---|
| N001 | PDF p.1 abstract | Randomized women / infants | 1626 / 1634 | 1631 / 1641 | Total 3257 women; p.4 results and Figure 1; Table 1 p.5, Table 2 p.6, Table 4 p.8 |
| N002 | PDF p.1 abstract | Maternal age mean (SD), years | 31.7 (5.1) | 31.5 (5.0) | p.4 narrative; N024 |
| N003 | PDF p.1 abstract | Gestation randomization mean (SD), weeks | 39.5 (1.2) | 39.5 (1.1) | p.4 narrative; N025 |
| N004 | PDF p.1 abstract | Australia/New Zealand ethnicity | 868 (53.4%) | 874 (53.6%) | p.4 narrative; N028 preserves Table 1 own printed percentage |
| N005 | PDF p.1 abstract | European ethnicity | 315 (19.4%) | 311 (19.1%) | p.4 narrative; N029 |
| N006 | PDF p.1 abstract | Nulliparity; missing | 944/1624 (58.1%); 2 missing | 966/1630 (59.3%); 1 missing | p.5 narrative; N036 |
| N007 | PDF p.1 abstract | Induction of labor | 1353/1621 (83.5%) | 1348/1627 (82.9%) | p.5 narrative; N071 |
| N008 | PDF p.2 Key Points | Primary infant mortality/neonatal morbidity frequency | 5.1% | 5.2% | Trial 3257 women; conclusion no difference; S001/S021 |
| N009 | PDF pp.1-3 design/eligibility | 13 Australian hospitals; September 6, 2021-June 28, 2024; follow-up July 26, 2024 | Age ≥18; singleton or dichorionic twins; term ≥37 weeks | Triplets/higher order and monochorionic twins excluded | Screen ≥34 weeks; registered preterm delivery excluded from randomization/analysis |
| N010 | PDF p.2 background | Earlier phase 2 operative birth for distress | 18% | 36.7% | Relative reduction 51%; S004; historical rather than current trial result |
| N011 | PDF pp.1,3 intervention | 1:1 woman-level assignment, site-stratified web allocation | 50 mg orally every 8 h, maximum 3 doses / 150 mg | Identical equivalent placebo | Term spontaneous labor or induction after membrane rupture; oxygen screening at 24-48 h |
| N012 | PDF p.3 outcomes | Primary composite: ≥1 of 10 events | Intrapartum stillbirth; 28-day neonatal death; Apgar <4 at 5 min (scale 0-10); cord artery pH <7.0; hypoxic ischemic encephalopathy; seizures; respiratory support >4 h; neonatal unit >48 h; persistent pulmonary hypertension; meconium aspiration | Individual components plus emergency cesarean/instrumental vaginal birth for fetal distress secondary | Abstract p.1 calls neonatal death without window; Table 3 p.7 specifies seizures within 28 d |
| N013 | PDF p.3 outcomes | Tertiary hierarchy | Emergency cesarean and instrumental vaginal birth for distress as primary indication; cesarean and instrumental vaginal birth for other indications; spontaneous vaginal birth; lengths stage 1/2; hemorrhage >1 L; hysterectomy; rupture; maternal ICU; maternal death | Additional hypothesis-generation outcomes said prespecified SAP; primary/secondary said prespecified protocol and registration | p.7 describes hemorrhage as 1 of 11 hypothesis-generating tertiary outcomes; Table 4 p.8 |
| N014 | PDF p.4 Figure 1 | Eligibility/registration/exclusion/randomization | 3748 eligible consented registered; 491 excluded; 3257 randomized | Exclusion reasons not routinely recorded at sites | Figure title Randomization, Delivery, and Assessment of Patients in a Clinical Trial of Sildenafil |
| N015 | PDF p.4 Figure 1 | Randomized; twin pregnancies | 1626; 8 twins | 1631; 10 twins | N001 and N040 |
| N016 | PDF p.4 Figure 1 | Received as randomized; did not receive | 1552; 74 | 1555; 76 | N054-N056 total doses |
| N017 | PDF p.4 Figure 1 | Nonreceipt reasons | Refusal 16; infant delivered 11; complete consent withdrawal 4; clinician discretion 2; received placebo 2; other 39 | Refusal 14; infant delivered 10; clinician discretion 6; complete withdrawal 2; other 44 | Printed figure includes wording indicating inadvertent receipt of placebo; exact original wording in source transcript |
| N018 | PDF p.4 Figure 1 | Follow-up attrition | Lost 4; consent withdrawn for future data/follow-up 1 | Lost 10; future data/follow-up withdrawal 2 | Distinct labels retained |
| N019 | PDF p.4 Figure 1 | Infants followed up / primary outcome | 1625 / 1625 | 1627 / 1625 | Placebo 2 incomplete primary component data |
| N020 | PDF p.4 results | Consent withdrawals and final ITT available outcomes | 9 women withdrew after randomization | 3248 women (3266 infants) outcome data; primary available 3250 infants | Source wording preserved separately from Figure 1 categories |
| N021 | PDF pp.4,6 | Cord artery pH testing, source says women | 1223/1629 (75.1%); 5 missing withdrawal/lost follow-up | 1159/1637 (70.8%); 4 missing | Primary no-event assumption when test not done; S015; sensitivity S019/S020 |
| N022 | PDF pp.4,7 | Largest site recruitment | Mater Mother’s 1763/3257 (54.1%) | Other participating sites | Post hoc outcome comparison; Table 1 N057 |
| N023 | PDF p.4 demographics narrative | Ethnicity at randomized denominators | 1626 total; Aboriginal 47 (2.9), African 14 (0.9), Australia/NZ 868 (53.4), European 315 (19.4), missing 2 (0.1), other 68 (4.2), Pacific 53 (3.3), SE/NE/South Asian 241 (14.8) | 1631 total; corresponding 42 (2.6),18 (1.1),874 (53.6),311 (19.1),2 (0.1),73 (4.5),53 (3.2),244 (15.0) | Self-reported open-ended ethnicity; Table 1 includes Middle Eastern separately |
| N024 | PDF p.5 Table 1 | Age mean (SD), y | 31.7 (5.1) | 31.5 (5.0) | Header n=1626/1631; N002 |
| N025 | PDF p.5 Table 1 | Gestation randomization mean (SD), wk | 39.5 (1.2) | 39.5 (1.1) | N003 |
| N026 | PDF p.5 Table 1 | Ethnicity denominator; Aboriginal/Torres Strait Islander | n=1624; 47 (2.9) | n=1629; 42 (2.6) | Shared ethnicity denominators N027-N033 |
| N027 | PDF p.5 Table 1 | African | 14 (0.9) | 18 (1.1) | N026 denominators |
| N028 | PDF p.5 Table 1 | Australia/New Zealand | 868 (53.4) | 874 (53.7) | N004/N023 own printed copies |
| N029 | PDF p.5 Table 1 | European | 315 (19.4) | 311 (19.1) | N005 |
| N030 | PDF p.5 Table 1 | Middle Eastern | 18 (1.1) | 14 (0.9) | N026 denominators |
| N031 | PDF p.5 Table 1 | Other | 68 (4.2) | 73 (4.5) | Footnote c no further breakdown |
| N032 | PDF p.5 Table 1 | Pacific Islander | 53 (3.3) | 53 (3.3) | N023 own printed copies |
| N033 | PDF p.5 Table 1 | Southeast/Northeast/South Asian | 241 (14.8) | 244 (15.0) | Footnote b self-reported open-ended ethnicity |
| N034 | PDF p.5 Table 1 | BMI first hospital visit, median (IQR) | 25.9 (22.4-31.2) | 25.7 (22.4-30.5) | BMI kg/m² footnote |
| N035 | PDF p.5 Table 1 | Smoking pregnancy | 77 (4.7), n=1624 | 72 (4.4), n=1630 | Row denominators |
| N036 | PDF p.5 Table 1 | Parity 0, births >20 wk | 944 (58.1), n=1624 | 966 (59.3), n=1630 | N006; shared denominator N037-N039 |
| N037 | PDF p.5 Table 1 | Parity 1 | 446 (27.5) | 450 (27.6) | N036 denominators |
| N038 | PDF p.5 Table 1 | Parity 2 | 152 (9.4) | 153 (9.4) | N036 denominators |
| N039 | PDF p.5 Table 1 | Parity ≥3 | 82 (5.0) | 61 (3.7) | N036 denominators |
| N040 | PDF p.5 Table 1 | Twin pregnancy | 8 (0.5), n=1621 | 10 (0.6), n=1627 | Figure 1 randomized twins N015 |
| N041 | PDF p.5 Table 1 | Previous pregnancy birth method denominator/spontaneous vaginal | n=680; 477 (70.1) | n=664; 432 (65.1) | Shared denominator N042-N044 |
| N042 | PDF p.5 Table 1 | Previous instrumental vaginal birth | 146 (21.5) | 159 (23.9) | N041 denominators |
| N043 | PDF p.5 Table 1 | Previous emergency cesarean | 49 (7.2) | 51 (7.7) | N041 denominators |
| N044 | PDF p.5 Table 1 | Previous elective cesarean | 8 (1.2) | 22 (3.3) | N041 denominators |
| N045 | PDF p.5 Table 1 | Natural conception | 1461 (90.0), n=1624 | 1468 (90.1), n=1630 | Assisted conception N046 |
| N046 | PDF p.5 Table 1 | Assisted conception | 163 (10.0) | 162 (9.9) | N045 denominators |
| N047 | PDF p.5 Table 1 | Gestational hypertension | 84 (5.2), n=1624 | 83 (5.1), n=1630 | Shared hypertension denominators N048/N049 |
| N048 | PDF p.5 Table 1 | Preeclampsia | 41 (2.5) | 39 (2.4) | N047 denominators |
| N049 | PDF p.5 Table 1 | Chronic/essential hypertension | 32 (2.0) | 24 (1.5) | N047 denominators |
| N050 | PDF p.5 Table 1 | Gestational diabetes | 318 (19.6), n=1624 | 324 (19.9), n=1630 | N051 same denominators |
| N051 | PDF p.5 Table 1 | Type I and II diabetes | 29 (1.8) | 25 (1.5) | N050 |
| N052 | PDF p.5 Table 1 | Antepartum hemorrhage | 11 (0.7), n=1624 | 7 (0.4), n=1630 | Row denominator |
| N053 | PDF p.5 Table 1 | Small for gestational age | 56 (3.4), n=1624 | 56 (3.4), n=1630 | Figure 2 birth-weight-defined subgroup separate printed definition |
| N054 | PDF p.5 Table 1 | Medication doses 1 | 902 (55.5) | 914 (56.0) | p.5 narrative; header denominators 1626/1631 |
| N055 | PDF p.5 Table 1 | Medication doses 2 | 558 (34.3) | 549 (33.7) | p.5 narrative |
| N056 | PDF p.5 Table 1 | Medication doses 3 | 94 (5.8) | 92 (5.6) | p.5 narrative |
| N057 | PDF p.5 Table 1 | Mater Mother’s recruitment | 880 (54.1) | 883 (54.1) | N022 |
| N058 | PDF p.5 Table 1 | Other hospitals recruitment | 476 (29.3) | 476 (29.2) | Header denominators |
| N059 | PDF p.5 Table 1 | Royal Prince Alfred recruitment | 164 (10.1) | 166 (10.2) | Header denominators |
| N060 | PDF p.5 Table 1 | Royal Brisbane and Women’s recruitment | 106 (6.5) | 106 (6.5) | Footnote a all data No.(%) unless specified |
| N061 | PDF p.6 Table 2 | Neonates | 1634 | 1641 | N001 |
| N062 | PDF p.6 Table 2 | Gestation birth mean (SD), wk | 39.6 (1.2) | 39.6 (1.2) | p.5 narrative |
| N063 | PDF p.6 Table 2 | Male; sex denominator | 833 (51.1), n=1629 | 840 (51.3), n=1637 | N064 same denominators |
| N064 | PDF p.6 Table 2 | Female | 796 (48.9) | 797 (48.7) | N063 |
| N065 | PDF p.6 Table 2 | Birth weight mean (SD), g | 3451.9 (474.9) | 3466.6 (452.7) | Infant population |
| N066 | PDF p.6 Table 2 | Spontaneous vaginal; birth mode denominator | 864 (53.0), n=1629 | 931 (56.9), n=1637 | N067-N070 same denominators; S055 |
| N067 | PDF p.6 Table 2 | Cesarean delivery | 466 (28.6) | 412 (25.2) | N066 denominators |
| N068 | PDF p.6 Table 2 | Instrumental vaginal vacuum | 209 (12.8) | 204 (12.5) | N066 |
| N069 | PDF p.6 Table 2 | Instrumental vaginal forceps | 86 (5.3) | 88 (5.4) | N066 |
| N070 | PDF p.6 Table 2 | Vaginal breech | 4 (0.2) | 2 (0.1) | N066 |
| N071 | PDF p.6 Table 2 | Women / induction | 1626 women; 1353 (83.5), n=1621 | 1631 women; 1348 (82.9), n=1627 | Onset denominators shared N072; N007 |
| N072 | PDF p.6 Table 2 | Spontaneous onset | 268 (16.5) | 279 (17.1) | N071 |
| N073 | PDF p.6 Table 2 | Induction oxytocin ± artificial membrane rupture | 1252 (92.5) | 1227 (91.0) | Method of induction section; induction counts N071 |
| N074 | PDF p.6 Table 2 | Balloon dilatation | 562 (41.5) | 592 (43.9) | Methods may overlap; source gives no exclusive-category statement |
| N075 | PDF p.6 Table 2 | Prostaglandin | 465 (34.4) | 474 (35.2) | Induction section |
| N076 | PDF p.6 Table 2 | Membrane rupture only | 60 (4.4) | 76 (5.6) | Induction section |
| N077 | PDF p.6 Table 2 | Meconium-stained liquor | 294 (18.1), n=1621 | 268 (16.5), n=1626 | p.7 no-difference narrative |
| N078 | PDF p.6 Table 2 | Epidural/spinal | 1239 (76.4), n=1621 | 1241 (76.4), n=1625 | Analgesia denominator shared N079-N081 |
| N079 | PDF p.6 Table 2 | Nitrous oxide | 217 (13.4) | 221 (13.6) | N078 |
| N080 | PDF p.6 Table 2 | No analgesia | 133 (8.2) | 127 (7.8) | N078 |
| N081 | PDF p.6 Table 2 | IM pethidine/morphine | 32 (2.0) | 36 (2.2) | IM intramuscular footnote |
| N082 | PDF p.6 Table 2 | Electronic fetal monitoring | 1579 (97.4), n=1621 | 1585 (97.4), n=1627 | p.5 narrative |
| N083 | PDF p.6 Table 2 | Stage 1 median (range), h | 3.58 (0.00-30.58) | 3.55 (0.00-40.08) | Distinct from Table 4 mean/SD S056 |
| N084 | PDF p.6 Table 2 | Stage 2 median (range), h | 0.40 (0.00-49.00) | 0.43 (0.00-33.00) | Distinct from Table 4 mean/SD S057 |
| N085 | PDF p.6 Table 2 | Suspected abruption | 5 (0.3), n=1621 | 9 (0.6), n=1627 | Shared printed denominators N086-N089,N091 |
| N086 | PDF p.6 Table 2 | Intrapartum bleeding | 17 (1.0), n=1621 | 17 (1.0), n=1627 | p.7 narrative |
| N087 | PDF p.6 Table 2 | Cord prolapse | 2 (0.1), n=1621 | 3 (0.2), n=1627 | p.7 narrative |
| N088 | PDF p.6 Table 2 | Uterine rupture | 4 (0.2), n=1621 | 2 (0.1), n=1627 | S060 |
| N089 | PDF p.6 Table 2 | Clinical chorioamnionitis | 28 (1.7), n=1621 | 20 (1.2), n=1627 | p.7 narrative |
| N090 | PDF p.6 Table 2 | Maternal eclampsia/seizures | 0 | 0 | No explicit row denominator printed |
| N091 | PDF p.6 Table 2 | Hemorrhage >1 L / hysterectomy / ICU | 164 (10.1), n=1621; 1 (0.1), n=1621; 2 (0.1), n=1617 | 128 (7.9), n=1627; 1 (0.1), n=1627; 1 (0.1), n=1614 | Each endpoint separately tracked S058/S059/S061 |
| N092 | PDF p.6 Table 2 | Hospital stay median (range), d | 3 (0-62) | 3 (0-41) | Footnote a No.(%) unless specified; p.7 narrative no differences |
| N093 | PDF p.7 site narrative | Primary outcome largest site, source says women | 16/883 (1.8%) | 24/887 (2.7%) | p.7 discussion/p.9 continuation; S066 |
| N094 | PDF p.7 site narrative | Primary outcome other sites, source says women | 67/742 (9.0%) | 60/738 (8.1%) | S066 |
| N095 | PDF p.7 site narrative | Hemorrhage >1 L at Mater Mother’s | 73/880 (8.3%) | 72/882 (8.2%) | Source says no difference; supplement eTable 2 pointer |
| N096 | PDF p.7 safety narrative | Maternal mortality, stillbirth, neonatal death | No cases | No cases | Pulmonary hypertension 1 vs 3 cases; eTable 3 pointer; S022,S023,S030,S062 |
| N097 | PDF p.7 discussion | Primary and secondary narrative interpretation | No difference in primary composite infant mortality/neonatal morbidity | No difference emergency operative birth or individual components | Site differences nonsignificant; N022,S066 |
| N098 | PDF p.9 contextual evidence | Prior phase 2 and meta-analysis | 51% reduction prior phase 2 | Meta-analysis 1090 women; 42% relative reduction operative birth for distress | Historical context only, no external lookup |
| N099 | PDF p.9 limitations | Overall primary incidence and component incidence | Observed 5.1% vs anticipated 7.0%; important components 0.1%-0.5% | Largest site 1.8% vs others 9.0%; induction >80% | No pharmacokinetic information; moderate 10% outcome reduction may require >75000 randomized |
| N100 | PDF p.9 conclusions | Treatment conclusion | No lower adverse perinatal incidence or emergency operative birth for intrapartum compromise | Does not preclude investigation in other care/populations | Matches abstract/Key Points |

## Inferential and statistical-design relationships

| ID | Exact location | Analysis / outcome | Printed quantities / method / rule | Matching occurrence |
|---|---|---|---|---|
| S001 | PDF p.1 abstract | Primary | 83/1625 women (5.1%) vs 84/1625 (5.2%); RR 1.02, CI 0.75-1.37 | p.6 narrative; S021; Figure 2 S035 |
| S002 | PDF p.1 abstract | Emergency cesarean/instrumental vaginal birth for distress | RR 1.12, CI 0.98-1.29; no significant effect | p.6 narrative; S032 |
| S003 | PDF p.1 abstract | Components/subgroups | No significant effect individual components; no heterogeneity evidence | S024-S031; S063 |
| S004 | PDF p.2 background | Prior phase 2 | RR 0.49, CI 0.33-0.73, relative reduction 51%, 18% vs 36.7% | N010; contextual supplied-paper claim |
| S005 | PDF p.3 | Interim analysis | Independent committee 1 analysis at 50% recruitment; stop recommendation perinatal mortality difference Haybittle-Peto 3 SD from null, equivalent P<.003 | Mortality rather than primary composite stopping endpoint |
| S006 | PDF p.3 | Sample-size primary | Baseline 7%; 3200 women allowing 10% follow-up loss; detect 35% reduction from 7.0% to 4.6%, alpha .05, >80% power | p.9 observed primary incidence N099 |
| S007 | PDF p.3 | Sample-size secondary | Same sample gives >90% power to detect 25% reduction cesarean/instrumental birth for distress | Source does not state secondary baseline incidence in paragraph |
| S008 | PDF p.3 | Analysis population/timing | ITT, analyses said prespecified protocol/SAP before lock/unblinding | N020 available population |
| S009 | PDF p.3 | Primary model | GEE log-binomial, multifetal gestation clustering adjustment; RR and 95% CI relative reduction/increase sildenafil risk | Table 3 footnote, Figure 2 overall footnote |
| S010 | PDF p.3 | General comparisons | Chi-square, linear trend for ordered categorical; t test continuous; Wilcoxon rank sum if nonnormal | Table 1/2 descriptive quantities; no numerical test statistics |
| S011 | PDF p.3 | Secondary primary analysis | Robust modified Poisson with prognostic-factor adjustment | Sensitivity/adjusted eTable 1 pointer p.6; no covariates enumerated in main paragraph |
| S012 | PDF pp.3-4 | Multiplicity interpretation | Interrelated secondary outcomes; interpret pattern/consistency, not any single significant result; secondary/subgroup cannot infer definitive effect | p.4 no multiple-testing adjustment |
| S013 | PDF p.4 | Subgroup analysis | Prespecified interaction effects on primary for small for gestational age, multifetal, preeclampsia, noncephalic, prior cesarean, postnatal anomaly | Figure 2 S036-S047; all interaction P>.05 caption |
| S014 | PDF p.4 | Significance/software | Two-tailed P<.05; no multiplicity adjustment; SAS 9.4; analyzed October 24, 2024; CONSORT/TRIPOD | Applicable all inferential main displays |
| S015 | PDF p.4 | Missing pH primary | No event assumed if cord artery pH not tested; several imputation methods evaluated | N021; Table 3 footnote b |
| S016 | PDF p.4 | Post hoc site comparison | Mater Mother’s vs all other sites for primary, secondary, tertiary | N022,N093-N095,S066 |
| S017 | PDF p.4 | Safety population | ≥1 dose, count by treatment received | Figure 1 nonreceipt/inadvertent placebo; doses N054-N056 |
| S018 | PDF p.4 | Outcome collection | In-hospital records; primary except 28-day death before discharge; no formal assessments | N012 endpoint windows |
| S019 | PDF p.6 narrative | Missing-pH imputation sensitivity | RR 1.01 (0.75-1.36) | eTable 1 Supplement 3 pointer; no material change claim |
| S020 | PDF p.6 narrative | Adjusted primary sensitivity | RR 0.98 (0.73-1.31) | eTable 1 Supplement 3 pointer; printed description “adjusted for” |
| S021 | PDF p.7 Table 3 | Primary | 83/1625 (5.1) vs 84/1625 (5.2); RD -0.1 (-1.6 to 1.5); RR 1.02 (0.75 to 1.37); P=.91 | S001, p.6 clustering-adjusted narrative |
| S022 | PDF p.7 Table 3 | Intrapartum stillbirth | 0/1629 vs 0/1637; RD/RR/P NA | N096 |
| S023 | PDF p.7 Table 3 | 28-d neonatal death | 0/1625 vs 0/1627; RD/RR/P NA | N096 |
| S024 | PDF p.7 Table 3 | Apgar <4, 5 min | 5/1629 (0.3) vs 3/1637 (0.2); RD 0.1 (-0.3 to 0.5); RR 1.67 (0.40 to 7.00); P=.48 | RR/CI repeated p.6 |
| S025 | PDF p.7 Table 3 | Cord pH <7.0 | 12/1629 (0.7) vs 5/1637 (0.3); RD 0.4 (-0.1 to 1.0); RR 2.28 (0.81 to 6.47); P=.12 | Footnote not done assumes no event; p.6 RR/CI |
| S026 | PDF p.7 Table 3 | Neonatal encephalopathy | 1/1625 (0.1) vs 1/1625 (0.1); RD 0.0 (-0.2 to 0.2); RR 0.94 (0.06 to 14.94); P=.96 | RR/CI p.7 narrative |
| S027 | PDF p.7 Table 3 | Seizures within 28 d | 2/1625 (0.1) vs 1/1625 (0.1); RD 0.1 (-0.2 to 0.3); RR 1.87 (0.17 to 20.62); P=.61 | RR/CI p.7 narrative |
| S028 | PDF p.7 Table 3 | Neonatal unit >48 h | 50/1629 (3.1) vs 61/1637 (3.7); RD -0.7 (-2.0 to 0.6); RR 0.85 (0.59 to 1.23); P=.39 | RR/CI p.7 narrative |
| S029 | PDF p.7 Table 3 | Respiratory support >4 h | 37/1629 (2.3) vs 47/1637 (2.9); RD -0.6 (-1.7 to 0.5); RR 0.81 (0.53 to 1.25); P=.35 | RR/CI p.7 narrative |
| S030 | PDF p.7 Table 3 | Persistent pulmonary hypertension | 1/1629 (0.1) vs 3/1637 (0.2); RD -0.1 (-0.4 to 0.2); RR 0.33 (0.03 to 3.22); P=.34 | RR/CI and safety counts p.7 |
| S031 | PDF p.7 Table 3 | Meconium aspiration | 9/1629 (0.6) vs 5/1637 (0.3); RD 0.2 (-0.3 to 0.8); RR 1.81 (0.61 to 5.39); P=.29 | RR/CI p.7 narrative |
| S032 | PDF p.7 Table 3 | Emergency cesarean or instrumental vaginal birth for distress | 343/1629 (21.1) vs 307/1637 (18.8); RD 2.3 (-0.5 to 5.1); RR 1.12 (0.98 to 1.29); P=.10 | Abstract/p.6 narrative S002 |
| S033 | PDF p.7 Table 3 footnote a | Model / P attribution | GEE adjusting for multiple births applies superscripts to RR and P headings | RD column has no superscript a |
| S034 | PDF p.7 narrative | Other outcomes interpretation | No differences hospital stay, ICU, labor, analgesia, electronic monitoring, meconium liquor, abruption, bleeding, prolapse, rupture, chorioamnionitis, hysterectomy | Source points to Table 4; all descriptive Table 2 values retained |
| S035 | PDF p.8 Figure 2 | Overall | 83/1625 (5.1) vs 84/1625 (5.2); RR 1.02 (0.75-1.37) | Overall GEE log-binomial; S021 |
| S036 | PDF p.8 Figure 2 | Small for gestational age yes, birth weight <10th percentile gestation | 10/106 (9.4) vs 13/105 (12.4); RR 0.76 (0.35-1.66) | Model S064 |
| S037 | PDF p.8 Figure 2 | Small for gestational age no | 73/1519 (4.8) vs 71/1520 (4.7); RR 1.03 (0.75-1.42) | Model S064 |
| S038 | PDF p.8 Figure 2 | Multiple pregnancy yes | 2/16 (12.5) vs 7/20 (35.0); RR 0.36 (0.09-1.49) | Model S064 |
| S039 | PDF p.8 Figure 2 | Multiple pregnancy no | 81/1609 (5.0) vs 77/1605 (4.8); RR 1.05 (0.77-1.42) | Model S064 |
| S040 | PDF p.8 Figure 2 | Preeclampsia yes | 4/41 (9.8) vs 5/38 (13.2); RR 0.74 (0.21-2.56) | Model S064 |
| S041 | PDF p.8 Figure 2 | Preeclampsia no | 79/1584 (5.0) vs 79/1587 (5.0); RR 1.00 (0.74-1.36) | Model S064 |
| S042 | PDF p.8 Figure 2 | Prior cesarean yes | 4/57 (7.0) vs 1/71 (1.4); RR 4.98 (0.57-43.35) | Model S064 |
| S043 | PDF p.8 Figure 2 | Prior cesarean no | 79/1568 (5.0) vs 83/1554 (5.3); RR 0.94 (0.70-1.27) | Model S064 |
| S044 | PDF p.8 Figure 2 | Noncephalic yes | 1/4 (25.0) vs 1/2 (50.0); RR 0.50 (0.06-4.47) | Model S064 |
| S045 | PDF p.8 Figure 2 | Noncephalic no | 82/1621 (5.1) vs 83/1623 (5.1); RR 0.99 (0.73-1.33) | Model S064 |
| S046 | PDF p.8 Figure 2 | Postnatal anomaly yes | 7/19 (36.8) vs 4/22 (18.2); RR 2.03 (0.70-5.87) | Model S064 |
| S047 | PDF p.8 Figure 2 | Postnatal anomaly no | 76/1606 (4.7) vs 80/1603 (5.0); RR 0.95 (0.70-1.29) | Model S064 |
| S048 | PDF p.8 Table 4 | Cesarean fetal distress | 142/1629 (8.7) vs 129/1637 (7.9); RD 0.8 (-1.1 to 2.8); RR 1.11 (0.88 to 1.39) | Infant-level header 1634/1641; GEE multiple births |
| S049 | PDF p.8 Table 4 | IVB fetal distress | 201/1629 (12.3) vs 178/1637 (10.9); RD 1.5 (-0.8 to 3.7); RR 1.13 (0.94 to 1.37) | IVB instrumental vaginal birth; GEE |
| S050 | PDF p.8 Table 4 | Cesarean other indication | 291/1629 (17.9) vs 257/1637 (15.7); RD 2.2 (-0.5 to 4.8); RR 1.14 (0.97 to 1.32) | GEE |
| S051 | PDF p.8 Table 4 | IVB other indication | 94/1629 (5.8) vs 114/1637 (7.0); RD -1.2 (-2.9 to 0.5); RR 0.83 (0.64 to 1.08) | GEE |
| S052 | PDF p.8 Table 4 | Emergency operative birth distress a factor | 471/1629 (28.9) vs 431/1637 (26.3); RD 2.6 (-0.5 to 5.7); RR 1.10 (0.98 to 1.23) | GEE; broader indication than S032 |
| S053 | PDF p.8 Table 4 | Cesarean distress a factor | 233/1629 (14.3) vs 201/1637 (12.3); RD 2.0 (-0.4 to 4.4); RR 1.16 (0.98 to 1.39) | GEE |
| S054 | PDF p.8 Table 4 | IVB distress a factor | 238/1629 (14.6) vs 230/1637 (14.1); RD 0.6 (-1.9 to 3.0); RR 1.04 (0.88 to 1.23) | GEE |
| S055 | PDF p.8 Table 4 | Spontaneous vaginal | 864/1629 (53.0) vs 931/1637 (56.9); RD -3.8 (-7.3 to -0.4); RR 0.93 (0.88 to 0.99) | GEE; N066 |
| S056 | PDF p.8 Table 4 | Stage 1 mean (SD), h | 4.53 (4.19) vs 4.53 (4.14); absolute percentage difference NA; mean difference -0.00 (-0.29 to 0.28) | Maternal-level header 1626/1631; Table 2 uses median/range |
| S057 | PDF p.8 Table 4 | Stage 2 mean (SD), h | 0.85 (1.59) vs 0.88 (1.39); absolute percentage difference NA; mean difference -0.03 (-0.14 to 0.07) | Maternal level |
| S058 | PDF p.8 Table 4 | Hemorrhage >1 L | 164/1621 (10.1) vs 128/1627 (7.9); RD 2.2 (0.2 to 4.3); RR 1.29 (1.03 to 1.60) | RD/CI and counts p.7; possible increase/type I multiplicity discussion p.9 |
| S059 | PDF p.8 Table 4 | Hysterectomy | 1/1621 (0.1) vs 1/1627 (0.1); RD 0.0 (-0.2 to 0.2); RR 1.00 (0.06 to 16.03) | Maternal level; coordinator normalized the duplicated mapper locator S060 to S059 after pass-1 confirmation; supplied values unchanged |
| S060 | PDF p.8 Table 4 | Uterine rupture | 4/1621 (0.2) vs 2/1627 (0.1); RD 0.1 (-0.2 to 0.5); RR 2.01 (0.37 to 10.94) | Maternal level |
| S061 | PDF p.8 Table 4 | Maternal ICU | 2/1617 (0.1) vs 1/1614 (0.1); RD 0.1 (-0.2 to 0.3); RR 2.00 (0.18 to 21.99) | Maternal level |
| S062 | PDF p.8 Table 4 | Maternal mortality | 0/1617 vs 0/1618; RD/RR NA | Maternal level; no Table 4 P column |
| S063 | PDF p.8 Figure 2 caption | Interactions / graph scale | All treatment-by-subgroup interaction tests not significant, P>.05; inverse-variance square area; RR axis 0.01,0.1,1,10,50; lower side favors sildenafil, higher favors placebo | p.1,p.7 no heterogeneity claims |
| S064 | PDF p.8 Figure 2 footnote | Subgroup estimator | Within-subgroup generalized linear log-binomial model; described exploratory and small twin count reason; overall GEE log-binomial | Distinct from S009 clustering adjustment |
| S065 | PDF p.8 Table 4 footnote | Infant-level model | Relative risks GEE accounting multiple births; RR/difference in means heading with CI; NA not applicable | Footnote does not specify maternal RR model |
| S066 | PDF pp.7,9 discussion | Post hoc site interaction | Largest site primary frequency 33% lower sildenafil vs placebo, 16/883 (1.8) vs 24/887 (2.7); other sites 11% higher, 67/742 (9.0) vs 60/738 (8.1); interaction P=.16 | p.9 limitations repeats no differential effect site, P=.16 |
| S067 | PDF p.9 discussion | Hemorrhage interpretation | Hypothesis-generating possible increased risk could be type I due multiple comparisons | S058; source-grounded interpretation |
| S068 | PDF p.9 limitations | Precision / power interpretation | Observed overall 5.1% vs anticipated 7.0%; may underpower primary/components; moderate 10% reduction may need >75000 | N099; no full calculation inputs for 75000 printed |

## Exact direct-source links

All rows identify physical pages. These links establish the authoritative location for every page-level record:

- [PDF page 1](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=1)
- [PDF page 2](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=2)
- [PDF page 3](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=3)
- [PDF page 4](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4)
- [PDF page 5](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=5)
- [PDF page 6](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=6)
- [PDF page 7](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=7)
- [PDF page 8](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=8)
- [PDF page 9](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=9)
- [PDF page 10](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=10)
- [PDF page 11](../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=11)

## Completion and limits

Mapped 11/11 fresh-required pages. Inventory: 100 numeric/reporting relationships N001-N100 and 68 inferential/design relationships S001-S068. No scientific coverage gaps. Native text was usable across every page; visual inspection of current p.8 confirmed numerical alignment and plotted orientation. Unreported inputs remain explicitly unreported; no estimates, intervals, P values, population labels or methods were inferred to fill them. The full source transcript below preserves narrative exactness; row-based paraphrases above do not replace the supplied PDF.

## Complete fresh native page transcript

### Direct-source PDF page 1

```text
Intrapartum Sildenafil to Improve Perinatal Outcomes
A Randomized Clinical Trial
Sailesh Kumar, DPhil(Oxon); William Tarnow-Mordi, MD; Ben W. Mol, PhD; Vicki Flenady, PhD; Helen G. Liley, MD;
Nadia Badawi, PhD; Susan Walker, MD; Jonathan Hyett, MD; Anna Lene Seidler, PhD; Emily Callander, PhD;
John Simes, MD; Rachel L. O’Connell, PhD; for the iSEARCH Investigators
IMPORTANCE Sildenafil citrate may increase uteroplacental blood flow. Its ability to reduce
perinatal complications related to fetal hypoxia during labor is uncertain.
OBJECTIVE To compare the effectiveness of intrapartum maternal oral sildenafil citrate
vs placebo in improving perinatal outcomes potentially related to intrapartum hypoxia
in term pregnancies.
DESIGN, SETTING, AND PARTICIPANTS This pragmatic, multicenter, investigator-initiated,
placebo-controlled randomized clinical trial including 3257 women was conducted in 13
Australian hospitals from September 6, 2021, to June 28, 2024. The last date of follow-up
(28-day neonatal mortality) was July 26, 2024. Women aged 18 years or older with singleton
or dichorionic twin pregnancies, planning vaginal birth at term by either spontaneous labor or
induction of labor, were recruited.
INTERVENTIONS Women were assigned to 50 mg oral sildenafil citrate every 8 hours
up to 150 mg or equivalent placebo.
MAIN OUTCOME AND MEASURES The primary composite outcome was intrapartum stillbirth,
neonatal death, Apgar score less than 4 at 5 minutes (a score of <4 at 5 minutes is indicative
of severe neonatal depression at birth, with scores ranging from 0 to 10), acidosis at birth
(umbilical cord artery pH <7.0), hypoxic ischemic encephalopathy, neonatal seizures,
neonatal respiratory support for greater than 4 hours, neonatal unit admission for greater
than 48 hours, persistent pulmonary hypertension of the newborn, or meconium aspiration
syndrome. Secondary outcomes were the individual components of the primary composite
and emergency cesarean delivery or instrumental birth for intrapartum fetal distress.
RESULTS A total of 3257 women were randomized to sildenafil citrate (n = 1626 women and
1634 infants) or placebo (n = 1631 women and 1641 infants). Mean (SD) maternal age and
gestation at randomization were similar in both groups (31.7 [5.1] vs 31.5 [5.0] years and 39.5
[1.2] vs 39.5 [1.1] weeks, respectively). A total of 868 participants (53.4%) vs 874 participants
(53.6%) were of Australia/New Zealand ethnicity and 315 participants (19.4%) vs 311
participants (19.1%) were of European ethnicity. Most participants were nulliparous (944 of
1624 [58.1%; 2 missing values] vs 966 of 1630 [59.3%; 1 missing value]). Induction of labor
occurred in 1353 of 1621 women (83.5%) in the sildenafil citrate group and 1348 of 1627
women (82.9%) in the placebo group. The primary outcome occurred in 83 of 1625 women
(5.1%) in the sildenafil citrate group and 84 of 1625 (5.2%) in the placebo group (relative risk,
1.02; 95% CI, 0.75-1.37). Sildenafil citrate had no significant effect on emergency cesarean
delivery or instrumental vaginal birth for fetal distress (relative risk, 1.12; 95% CI, 0.98-1.29) or
on any of the individual components of the primary outcome. Subgroup analyses showed no
evidence of heterogeneity of treatment effect.
CONCLUSIONS AND RELEVANCE Sildenafil citrate did not result in a lower incidence of adverse
perinatal outcomes potentially related to intrapartum hypoxia.
TRIAL REGISTRATION anzctr.org.au Identifier: ACTRN12621000231842
JAMA. 2025;334(2):149-159. doi:10.1001/jama.2025.7710
Published online June 9, 2025.
Visual Abstract
Supplemental content
CME Quiz at
jamacmelookup.com
Author Affiliations: Author
affiliations are listed at the end of this
article.
Group Information: The iSEARCH
investigators appear in
Supplement 4.
Corresponding Author: Sailesh
Kumar, DPhil(Oxon), Mater Research
Institute–University of Queensland,
Mater Campus, Whitty Building,
Level 1, South Brisbane, Queensland
4101, Australia (sailesh.kumar@
mater.uq.edu.au).
Research
JAMA | Original Investigation | WOMEN'S HEALTH
(Reprinted)
149
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/23/2026

```

### Direct-source PDF page 2

```text
D
uring labor, uterine contractions cause intermittent
but progressive reduction in placental perfusion,
which gradually limits fetal oxygenation. Intrapar-
tum fetal compromise (fetal distress) occurs when there is
inadequate placental reperfusion time between contractions
or when there is appropriate reperfusion time but underlying
placental dysfunction limits adequate oxygen transfer to the
fetus.1 Hypoxic-ischemic injury during labor2,3 is an impor-
tant cause of intrapartum stillbirth, neonatal death, and neo-
natal encephalopathy in late preterm and term infants, with
small for gestational age infants at particular risk.4 Although
the prevalence of hypoxia-related birth injury is high in
poorly resourced settings, the proportion of true intrapartum
hypoxic-ischemic events causing neonatal encephalopathy is
low in many high-income countries.5 When fetal distress is
suspected, emergency cesarean delivery or instrumental
vaginal birth is often required to prevent ongoing in utero
injury to the infant. Although these urgent interventions may
be necessary, they can be associated with significant mater-
nal and neonatal morbidity and have implications for future
pregnancies.6
Criteria used by various international bodies to deter-
mine whether an intrapartum hypoxic event is responsible
for neonatal encephalopathy include sentinel events occur-
ring during labor, specific pathologic fetal heart rate pat-
terns, neuroimaging abnormalities consistent with an acute
intrapartum event, subsequent spastic quadriplegia or dys-
kinetic cerebral palsy, and exclusion of other causative or
contributory factors.7,8 However, although electronic fetal
heart rate monitoring during labor is often used to detect
fetal compromise, its use has not resulted in improvements
in cerebral palsy rates, perinatal mortality, or other mea-
sures of neonatal well-being,9 emphasizing the imperative
for more effective or novel approaches to prevent adverse
perinatal outcomes related to intrapartum hypoxic injury.
One possible strategy is to improve fetoplacental perfusion
and fetal oxygenation during labor.
Cyclic nucleotide phosphodiesterases (PDEs) are a family
of 11 related phosphohydrolase isoforms that selectively cata-
lyze the hydrolysis of the 3′ cyclic phosphate bonds of aden-
osine or guanosine 3′,5′ cyclic monophosphate,10 increasing
bioavailability of nitric oxide causing vasodilatation. Phos-
phodiesterasetype5(PDE5)inhibitorsarelicensedforthetreat-
ment of erectile dysfunction in men11 and severe pulmonary
arterialhypertensioninadults,neonates,andchildren.12,13High
levels of PDE5 are found in vascular smooth muscle and pla-
centa. In human and animal models, both in vivo and in vitro
data suggest that PDE5 inhibitors increase uteroplacental
perfusion14-16 and reverse vasoconstriction in uterine and spi-
ral arteries.17,18 Only sildenafil citrate and tadalafil have been
used for a variety of indications related to placental dysfunc-
tion, to treat maternal hypertension, or both.19
In an earlier phase 2 randomized clinical trial (RCT),20 we
showedthatmaternaloralsildenafilcitratecomparedwithpla-
cebo reduced the relative risk (RR) of operative birth for fetal
distress by 51% (18% vs 36.7%; RR, 0.49; 95% CI, 0.33-0.73).
It also attenuated the normal intrapartum decline in placen-
tal growth factor levels, suggesting that it may preserve pla-
cental function in labor.21 This trial, however, lacked power to
show an effect on perinatal outcomes related to intrapartum
hypoxic injury.20
We report the results of the Australian iSEARCH (Can In-
trapartum Sildenafil Safely Avert the Risks of Contraction-
Induced Hypoxia in Labor) RCT, which tested the hypothesis
that, compared with placebo, intrapartum maternal oral silde-
nafil citrate improves perinatal outcomes in term pregnancies.
Methods
Study Design and Oversight
iSEARCH was a pragmatic, multicenter, investigator-
initiated, placebo-controlled, double-blind RCT involving
women with term pregnancies (≥37 weeks’ gestation) attempt-
ing vaginal birth at 13 Australian hospitals from September 6,
2021,toJune28,2024.Thetrialprotocolhasbeenpublished.22
The trial was approved by the Hunter New England Local
Health District Human Research Ethics Committee, New South
Wales Ministry of Health.
Participants
Women aged 18 years or older with singleton or dichorionic
twinpregnancies,planningvaginalbirthattermbyeitherspon-
taneous labor or induction of labor, were eligible for the trial.
Women with triplets or higher-order multifetal gestation, with
monochorionic twins, taking any type of nitrate-containing
medications or other PDE inhibitors, or affected by severe he-
patic or kidney impairment were excluded.
Screening, Recruitment, and Randomization
Women at at least 34 weeks’ gestation at all participating
hospitals were screened for eligibility by study midwives,
and those who met the inclusion criteria and consented to
participate were registered in an online trial registration
database (Medidata Solutions, Dassault Systèmes). Once
registered, each woman was assigned a unique study num-
ber and continued to receive routine prenatal care until
spontaneous labor or induction of labor occurred. Written
informed consent was obtained from all women at registra-
tion before randomization.
After spontaneous labor had been diagnosed or after
artificial rupture of membranes if induction of labor was
Key Points
Question Does maternal oral sildenafil citrate during labor improve
perinatal outcomes potentially related to intrapartum hypoxia?
Findings This placebo-controlled randomized trial of 3257 women
found no difference in the frequency of the primary composite
outcome of infant mortality or neonatal morbidity between
women assigned to receive oral sildenafil citrate in labor compared
with placebo (5.1% vs 5.2%).
Meaning Sildenafil citrate did not result in a lower incidence of
adverse perinatal outcomes after term labor and should not be
used for this indication.
Research Original Investigation
Intrapartum Sildenafil to Improve Perinatal Outcomes
150
JAMA
July 8, 2025
Volume 334, Number 2
(Reprinted)
jama.com
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/23/2026

```

### Direct-source PDF page 3

```text
undertaken, randomization was performed by the respon-
sible midwife or obstetrician after confirming that the
woman met the eligibility criteria. Only women who were in
spontaneous labor or undergoing induction at term (≥37
weeks) were randomized. Women who were registered but
who delivered before 37 weeks were not randomized and
were not part of the analysis of study outcomes. Randomiza-
tion was performed using a web-based (Medidata Solutions),
computer-generated, concealed allocation sequence, strati-
fied by study site. After randomization, women were
assigned a treatment group. The first participant was regis-
tered on September 6, 2021; and the final participant, on
June 28, 2024.
Trial Interventions and Management of Labor
and Puerperium
Women were assigned in a 1:1 ratio to receive 50 mg sildenafil
citrate or identical placebo orally every 8 hours to a maxi-
mumof3doses.TrialmedicationwasmanufacturedbyOptima
Ovest. The Therapeutic Goods Administration is Australia’s
government authority responsible for evaluating, assessing,
and monitoring products that are defined as therapeutic goods
for use in clinical practice or research studies. Trial medica-
tion was stored at room temperature at each center’s phar-
macy and transferred to the labor ward when required.
All women, regardless of treatment group, were treated
according to local intrapartum and postnatal protocols and
guidelines (including the use of electronic fetal heart rate
monitoring).23,24 Spontaneous labor was defined as regular
uterine contractions with progressive cervical dilatation.23
Methods for induction of labor included vaginal prostaglan-
dins, balloon cervical dilatation, artificial rupture of mem-
branes, and oxytocin infusion.23
Classification of fetal heart rate abnormalities followed
Royal Australian and New Zealand College of Obstetricians and
Gynecologists guidelines.25 Where possible, umbilical artery
cord pH was measured after birth. To detect persistent pul-
monary hypertension of the newborn, all neonates received
oxygen saturation screening 24 to 48 hours after birth.
Trial Outcomes
The primary outcome was a composite of 10 intrapartum or
neonatal events potentially reflecting intrapartum hypoxia, in-
cluding 1 or more of intrapartum stillbirth, 28-day neonatal
death, Apgar score less than 4 at 5 minutes (a score of <4 at 5
minutes is indicative of severe neonatal depression at birth,
with scores ranging from 0 to 10), acidosis at birth (umbilical
cord artery pH <7.0), hypoxic ischemic encephalopathy, neo-
natal seizures, neonatal respiratory support for greater than
4hours,neonatalunitadmissionforgreaterthan48hours,per-
sistent pulmonary hypertension of the newborn, or meco-
nium aspiration syndrome. Similar (but not identical) com-
posite outcomes have been used in other large perinatal
trials26,27 to reflect severe neonatal outcome (death or severe
morbidity). Secondary outcomes included each of the 10 in-
dividual components of the primary composite outcome and
emergency cesarean delivery or instrumental vaginal birth for
fetal distress. Tertiary outcomes were emergency cesarean
delivery for fetal distress (primary indication), instrumental
vaginal birth for fetal distress (primary indication), cesarean
delivery for indications other than fetal distress, instrumen-
tal vaginal birth for indications other than fetal distress, spon-
taneous vaginal birth, length of first and second stage of la-
bor, postpartum hemorrhage greater than 1 L, postpartum
hysterectomy,uterinerupture,maternalintensivecareunitad-
mission, and maternal death. Primary and secondary out-
comes were prespecified in the trial protocol (Supplement 1)
and prospective trial registration records; additional hypoth-
esis-generation tertiary outcomes were prespecified in the sta-
tistical analysis plan (Supplement 2).
Cases that met the primary and secondary outcomes were
reviewed by the local lead investigator. In-hospital maternal
and neonatal outcome events were collected from medical rec-
ords into electronic case report forms. Apart from 28-day neo-
natal mortality, all primary outcome data were routinely avail-
able before discharge and collected electronically. There were
no formal study assessments visits.
An independent data and safety monitoring committee
conducted 1 interim analysis after 50% of participants were re-
cruited. A recommendation to stop the trial early required a
difference in perinatal mortality indicated by a Haybittle-Peto
boundary of 3 SDs from the null (equivalent to P < .003).28,29
Sample Size Calculation
The incidence of the primary composite adverse outcome was
estimatedas7%basedondatafromparticipatinghospitalsand
the ARRIVE trial.26 A sample size of 3200 women (allowing for
10% lost to follow-up) permitted detection of a 35% reduc-
tion in the primary outcome (from 7.0% to 4.6%) for an α of
.05 and greater than 80% power in the treatment group com-
pared with the placebo group. This sample size also yielded
greater than 90% power to detect a 25% reduction for the sec-
ondary outcome of cesarean delivery or instrumental vaginal
birth for fetal distress.
Statistical Analysis
Analyses were performed according to the intention-to-treat
principle and were prespecified in the trial protocol (Supple-
ment 1) and statistical analysis plan (Supplement 2) before
the trial database was locked and unblinding performed. The
primary composite outcome was analyzed using a general-
ized estimating equation log-binomial model adjusting for
clustering due to multifetal gestation, with RR and 95% CI to
indicate the relative reduction (or increase) in risk associated
with sildenafil citrate therapy. χ2 Tests (with linear trend test
for ordered variables) were used to compare categorical vari-
ables and t tests were used for continuous variables, or if the
distribution of the data was nonnormal, the Wilcoxon rank
sum test was used. Secondary analysis of the primary out-
come was undertaken, which included adjustment for prog-
nostic factors using robust (modified) Poisson regression.
Because the secondary outcomes are interrelated and poten-
tially causally attributable to hypoxic birth injury, we inter-
preted the pattern and consistency of findings across related
outcomes rather than focusing on any single, statistically sig-
nificant result.30 Thus, results from secondary outcomes and
Intrapartum Sildenafil to Improve Perinatal Outcomes
Original Investigation Research
jama.com
(Reprinted)
JAMA
July 8, 2025
Volume 334, Number 2
151
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/23/2026

```

### Direct-source PDF page 4

```text
subgroup analyses should not be used to infer definitive
treatment effect.
Prespecified subgroup analyses were performed by as-
sessing interaction effects on the primary composite out-
come. We prespecified subgroup analyses for women with
small for gestational age infants, multifetal gestation, pre-
eclampsia, noncephalic presentation, cesarean delivery in
precedingpregnancy,andpostnataldiagnosisoffetalanomaly.
Because cord artery pH testing was performed for only 1223
of 1629 women (75.1%) in the sildenafil citrate group and 1159
of 1637 women (70.8%) in the placebo cohort (5 and 4 miss-
ing values, respectively, because of withdrawals and loss to
follow-up), the primary outcome was evaluated with this com-
ponentimputedseveralways.Intheprimaryanalysis,noevent
was assumed when cord artery pH testing was not done. Be-
cause 1 center (Mater Mother’s Hospital) recruited 54.1% of the
trial cohort (1763 of 3257), we undertook additional post hoc
analyses for the primary, secondary, and tertiary outcomes be-
tweentheMaterMother’sHospitalandotherparticipatingsites.
Safety analysis of adverse events was undertaken among pa-
tients who received at least 1 dose of study treatment, with
subjects counted in the group according to the treatment they
received. Two-tailed P < .05 was considered statistically
significant. There was no adjustment for multiple testing.
Statistical analyses were performed with SAS version 9.4 (SAS
Institute); data were analyzed on October 24, 2024. Report-
ing followed CONSORT31 and TRIPOD32 guidelines.
Results
Participants and Adherence
Between September 6, 2021, and June 28, 2024, 3257 women
were randomized after written informed consent (1626 receiv-
ing sildenafil citrate [1634 infants] and 1631 allocated to pla-
cebo [1641 infants]). After randomization 9 women withdrew
consent,leaving3248women(3266infants)withoutcomedata
for the final intention-to-treat analysis. The primary end point
was available for 3250 infants (Figure 1). The last date of
follow-up (28-day neonatal mortality) was July 26, 2024.
Baseline characteristics for the 2 groups were compa-
rable. Mean maternal age and gestation at randomization
were 31.7 years (SD, 5.1 years) and 39.5 weeks (SD, 1.2 weeks),
respectively, in the sildenafil citrate group and 31.5 years (SD,
5.0 years) and 39.5 weeks (SD, 1.1 weeks) in the placebo
cohort. Ethnicity of the 1626 participants in the sildenafil
citrate group and 1631 participants in the placebo cohort
included Aboriginal and Torres Strait Islander (47 [2.9%] vs
42 [2.6%]), African (14 [0.9%] vs 18 [1.1%]), Australia/New
Zealand (868 [53.4%] vs 874 [53.6%]), European (315 [19.4%]
vs 311 [19.1%]), missing (2 [0.1%] vs 2 [0.1%]), other (68
[4.2%] vs 73 [4.5%]; no further breakdown was available for
this category), Pacific Islander (53 [3.3%] vs 53 [3.2%]), and
Southeast Asian/Northeast Asian/South Asian (241 [14.8%] vs
244 [15.0%]). Ethnicity was a self-reported variable in
Figure 1. Randomization, Delivery, and Assessment of Patients in a Clinical Trial of Sildenafil
3748 Eligible women consented and registered
491 Women excludeda
10 Lost to follow-up
2 Consent withdrawn for future
data collection or follow-up
4 Lost to follow-up
1 Consent withdrawn for future
data collection or follow-up
2 Incomplete data for primary
end point components
3257 Randomized
1631 Randomized to placebo (10 twin pregnancies)
1555 Received placebo as randomized
76 Did not receive placebo
14 Participant refusal
10 Infant delivered
6 Clinician discretion
2 Complete withdrawal of consent
44 Other reason
1626 Randomized to sildenafil citrate (8 twin pregnancies)
1552 Received sildenafil citrate as randomized
74 Did not receive sildenafil citrate
16 Participant refusal
11 Infant delivered
2 Clinician discretion
4 Complete withdrawal of consent
2 Received placebo by mistake
39 Other reason
1627 Infants followed up
1625 Infants followed up
1625 Infants with primary outcome
1625 Infants with primary outcome
aReasons women were excluded are not shown because this information was not routinely recorded by participating sites.
Research Original Investigation
Intrapartum Sildenafil to Improve Perinatal Outcomes
152
JAMA
July 8, 2025
Volume 334, Number 2
(Reprinted)
jama.com
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/23/2026

```

### Direct-source PDF page 5

```text
response to an open-ended question. In the sildenafil citrate
cohort, 902 (55.5%), 558 (34.3%), and 94 (5.8%) women
received 1, 2, and 3 doses, respectively; in the placebo group,
914 (56.0%), 549 (33.7%), and 92 (5.6%) women received 1, 2,
and 3 doses, respectively (Table 1). Most participants were
nulliparous (944 of 1624 [58.1%; 2 missing values] vs 966 of
1630 [59.3%; 1 missing value]).
Mean gestation at birth was similar in both groups (silde-
nafilcitrate,39.6weeks[SD,1.2];placebo,39.6weeks[SD,1.2]).
Induction of labor occurred for 83.5% of women (1353 of 1621)
in the sildenafil citrate group and 82.9% of women (1348 of
1627) receiving placebo. The proportion of women who had
electronic fetal heart rate monitoring in labor was similar in
both cohorts (1579 [97.4%] vs 1585 [97.4%]) (Table 2).
Table 1. Characteristics of Study Participantsa
Sildenafil citrate
(n = 1626)
Placebo
(n = 1631)
Age, mean (SD), y
31.7 (5.1)
31.5 (5.0)
Gestation at randomization, mean (SD), wk
39.5 (1.2)
39.5 (1.1)
Ethnicityb
n = 1624
n = 1629
Aboriginal and Torres Strait Islander
47 (2.9)
42 (2.6)
African
14 (0.9)
18 (1.1)
Australia/New Zealand
868 (53.4)
874 (53.7)
European
315 (19.4)
311 (19.1)
Middle Eastern
18 (1.1)
14 (0.9)
Otherc
68 (4.2)
73 (4.5)
Pacific Islander
53 (3.3)
53 (3.3)
Southeast Asian/Northeast Asian/South Asian
241 (14.8)
244 (15.0)
BMI at first hospital visit, median (IQR)
25.9 (22.4-31.2)
25.7 (22.4-30.5)
Smoking during pregnancy
77 (4.7) [n = 1624]
72 (4.4) [n = 1630]
Parity (births >20 wk gestation)
n = 1624
n = 1630
0
944 (58.1)
966 (59.3)
1
446 (27.5)
450 (27.6)
2
152 (9.4)
153 (9.4)
≥3
82 (5.0)
61 (3.7)
Twin pregnancy
8 (0.5) [n = 1621]
10 (0.6) [n = 1627]
Method of birth in preceding pregnancy
n = 680
n = 664
Spontaneous vaginal birth
477 (70.1)
432 (65.1)
Instrumental vaginal birth
146 (21.5)
159 (23.9)
Emergency cesarean delivery
49 (7.2)
51 (7.7)
Elective cesarean delivery
8 (1.2)
22 (3.3)
Mode of conception
n = 1624
n = 1630
Natural
1461 (90.0)
1468 (90.1)
Assisted
163 (10.0)
162 (9.9)
Hypertension
n = 1624
n = 1630
Gestational
84 (5.2)
83 (5.1)
Preeclampsia
41 (2.5)
39 (2.4)
Chronic/essential
32 (2.0)
24 (1.5)
Diabetes mellitus
n = 1624
n = 1630
Gestational
318 (19.6)
324 (19.9)
Type I and II
29 (1.8)
25 (1.5)
Antepartum hemorrhage
11 (0.7) [n = 1624]
7 (0.4) [n = 1630]
Small for gestational age
56 (3.4) [n = 1624]
56 (3.4) [n = 1630]
No. of trial medication doses received
1
902 (55.5)
914 (56.0)
2
558 (34.3)
549 (33.7)
3
94 (5.8)
92 (5.6)
Recruitment at participating hospitals
Mater Mother’s Hospital
880 (54.1)
883 (54.1)
Other
476 (29.3)
476 (29.2)
Royal Prince Alfred Hospital
164 (10.1)
166 (10.2)
Royal Brisbane and Women’s Hospital
106 (6.5)
106 (6.5)
Abbreviation: BMI, body mass index
(calculated as weight in kilograms
divided by height in meters squared).
a Data are presented as No. (%)
unless otherwise indicated.
bEthnicity was a self-reported
variable in response to an
open-ended question.
c No further breakdown was available
for this category.
Intrapartum Sildenafil to Improve Perinatal Outcomes
Original Investigation Research
jama.com
(Reprinted)
JAMA
July 8, 2025
Volume 334, Number 2
153
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/23/2026

```

### Direct-source PDF page 6

```text
Primary and Secondary Outcomes
The primary composite outcome occurred in 83 of 1625
women (5.1%) in the sildenafil citrate group and 84 of 1625
women (5.2%) in the placebo group (RR, 1.02; 95% CI, 0.75-
1.37 after adjustment for clustering due to multifetal gesta-
tion) (Table 3). There were no cases of infant death. Umbili-
cal cord artery pH testing was performed for only 1223 of
1629 women (75.1%) in the sildenafil citrate group and 1159
of 1637 women (70.8%) in the placebo cohort (5 and 4 miss-
ing values, respectively, owing to withdrawals or loss to
follow-up). However, the finding for the primary outcome
did not change materially whether missing cord artery pH
was either imputed (RR, 1.01; 95% CI, 0.75-1.36) or adjusted
for (RR, 0.98; 95% CI, 0.73-1.31) (eTable 1 in Supplement 3).
Sildenafil citrate had no effect on emergency operative birth
(cesarean delivery or instrumental vaginal birth) for fetal
distress (RR, 1.12; 95% CI, 0.98-1.29) nor on any of the indi-
vidual components of the primary outcome: Apgar score
less than 4 at 5 minutes (RR, 1.67; 95% CI, 0.40-7.00), cord
artery pH less than 7 (RR, 2.28; 95% CI, 0.81-6.47), neonatal
Table 2. Intrapartum and Birth Outcomesa
Sildenafil citrate
Placebo
Neonates, No.
1634
1641
Gestation at birth, mean (SD), wk
39.6 (1.2)
39.6 (1.2)
Infant sex
n = 1629
n = 1637
Male
833 (51.1)
840 (51.3)
Female
796 (48.9)
797 (48.7)
Birth weight, mean (SD), g
3451.9 (474.9)
3466.6 (452.7)
Mode of birth
n = 1629
n = 1637
Spontaneous vaginal birth
864 (53.0)
931 (56.9)
Cesarean delivery
466 (28.6)
412 (25.2)
Instrumental vaginal birth (vacuum)
209 (12.8)
204 (12.5)
Instrumental vaginal birth (forceps)
86 (5.3)
88 (5.4)
Vaginal breech birth
4 (0.2)
2 (0.1)
Women, No.
1626
1631
Onset of labor
n = 1621
n = 1627
Induction
1353 (83.5)
1348 (82.9)
Spontaneous
268 (16.5)
279 (17.1)
Method of induction of labor
Oxytocin with or without artificial rupture
of membranes
1252 (92.5)
1227 (91.0)
Balloon cervical dilatation
562 (41.5)
592 (43.9)
Prostaglandin
465 (34.4)
474 (35.2)
Artificial rupture of membranes only
60 (4.4)
76 (5.6)
Details of labor
Meconium-stained liquor
294 (18.1) [n = 1621]
268 (16.5) [n = 1626]
Analgesia in labor
n = 1621
n = 1625
Epidural/spinal
1239 (76.4)
1241 (76.4)
Nitrous oxide (gas and air)
217 (13.4)
221 (13.6)
None
133 (8.2)
127 (7.8)
IM pethidine or morphine
32 (2.0)
36 (2.2)
Electronic fetal monitoring in labor
1579 (97.4) [n = 1621]
1585 (97.4) [n = 1627]
Length of stage 1, median (range), h
3.58 (0.00-30.58)
3.55 (0.00-40.08)
Length of stage 2, median (range), h
0.40 (0.00-49.00)
0.43 (0.00-33.00)
Complications during labor
Suspected abruption
5 (0.3) [n = 1621]
9 (0.6) [n = 1627]
Intrapartum bleeding
17 (1.0) [n = 1621]
17 (1.0) [n = 1627]
Cord prolapse
2 (0.1) [n = 1621]
3 (0.2) [n = 1627]
Uterine rupture
4 (0.2) [n = 1621]
2 (0.1) [n = 1627]
Clinical chorioamnionitis
28 (1.7) [n = 1621]
20 (1.2) [n = 1627]
Maternal eclampsia/seizures
0
0
Postpartum hemorrhage (>1 L)
164 (10.1) [n = 1621]
128 (7.9) [n = 1627]
Postpartum hysterectomy
1 (0.1) [n = 1621]
1 (0.1) [n = 1627]
Maternal intensive care unit admission
2 (0.1) [n = 1617]
1 (0.1) [n = 1614]
Length of hospital stay, median (range), d
3 (0-62)
3 (0-41)
Abbreviation: IM, intramuscular.
a Data are presented as No. (%)
unless otherwise indicated.
Research Original Investigation
Intrapartum Sildenafil to Improve Perinatal Outcomes
154
JAMA
July 8, 2025
Volume 334, Number 2
(Reprinted)
jama.com
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/23/2026

```

### Direct-source PDF page 7

```text
encephalopathy (RR, 0.94; 95% CI, 0.06-14.94), neonatal
seizures (RR, 1.87; 95% CI, 0.17-20.62), neonatal unit admis-
sion (RR, 0.85; 95% CI, 0.59-1.23), neonatal respiratory sup-
port greater than 4 hours (RR, 0.81; 95% CI, 0.53-1.25), per-
sistent pulmonary hypertension of the newborn (RR, 0.33;
95% CI, 0.03-3.22), or meconium aspiration syndrome (RR,
1.81; 95% CI, 0.61-5.39) (Table 3).
Subgroup analyses related to small for gestational age in-
fants, multifetal gestation, preeclampsia, noncephalic presen-
tation, preceding pregnancy cesarean delivery, and postnatal
diagnosis of fetal anomaly showed no appreciable differ-
ences in treatment effect across the subgroup categories, con-
sistent with the overall result of no effect (Figure 2).
Other Maternal and Neonatal Outcomes
There were no differences in length of hospital stay, maternal
intensive care unit admission, length of labor, method of an-
algesia, or use of electronic fetal heart rate monitoring. Rates
of meconium-stained liquor, abruption, intrapartum bleed-
ing, cord prolapse, uterine rupture, chorioamnionitis, or hys-
terectomy were also no different between the sildenafil ci-
trate and placebo groups (Table 4).
Therewerenosignificantdifferencesbetweenthe2groups
regarding prespecified adverse effects potentially related to
sildenafil or any other serious maternal or neonatal out-
comes. Specifically, there were no cases of maternal mortal-
ity, intrapartum stillbirth, or neonatal death in either group.
Onecaseofpersistentpulmonaryhypertensionoccurredinthe
sildenafil citrate group compared with 3 cases in the placebo
group (eTable 3 in Supplement 3).
Site-Specific Differences
There were potentially important site-specific differences in
outcomes: the primary outcome at the Mater Mother’s Hospi-
tal occurred in 16 of 883 women (1.8%) in the sildenafil citrate
group and 24 of 887 women (2.7%) in the placebo group com-
pared with 67 of 742 women (9.0%) and 60 of 738 women
(8.1%), respectively, at the other sites. Rates of emergency
operative birth (cesarean delivery or instrumental vaginal
birth) for fetal distress were also lower at the Mater Mother’s
Hospital compared with that at the other sites (eTable 2 in
Supplement 3). Although rates of postpartum hemorrhage,
which was 1 of 11 hypothesis-generating tertiary outcomes,
were higher in the sildenafil citrate group (164 of 1621 [10.1%]
vs 128 of 1627 [7.9%]; absolute risk difference, 2.2%; 95% CI,
0.2%-4.3%), there was no difference in this outcome at the
Mater Mother’s Hospital between the 2 groups (73 of 880
[8.3%] vs 72 of 882 [8.2%]) (eTable 2 in Supplement 3).
Discussion
In this randomized trial of women attempting vaginal birth
at term, we did not find any difference in the frequency of
the primary composite outcome of infant mortality or neo-
natal morbidity between those assigned to receive oral
sildenafil citrate in labor compared with placebo. There
were also no differences in the secondary outcomes of
emergency operative birth for fetal distress nor for any of
the components of the primary composite outcome. There
were important nonsignificant differences in frequency of
outcomes between the center with the largest number of
participating women (Mater Mother’s Hospital, 1763 of 3257
[54.1%]) and other hospitals. Post hoc analyses comparing
outcomes between the Mater Mother’s Hospital and other
centers showed that the frequency of the primary compos-
ite outcome in the sildenafil citrate group was 33% lower
compared with placebo (16 of 883 [1.8%] vs 24 of 887
Table 3. Primary and Secondary Outcomes
No./total No. (%)
Sildenafil citrate vs placebo (95% CI)
P valuea
Sildenafil citrate
Placebo
Absolute difference, %
Relative riska
Primary outcome
83/1625 (5.1)
84/1625 (5.2)
−0.1 (−1.6 to 1.5)
1.02 (0.75 to 1.37)
.91
Secondary outcomes
Intrapartum stillbirth
0/1629
0/1637
NA
NA
NA
28-d Neonatal death
0/1625
0/1627
NA
NA
NA
Apgar score <4 at 5 min
5/1629 (0.3)
3/1637 (0.2)
0.1 (−0.3 to 0.5)
1.67 (0.40 to 7.00)
.48
Umbilical cord artery pH <7.0b
12/1629 (0.7)
5/1637 (0.3)
0.4 (−0.1 to 1.0)
2.28 (0.81 to 6.47)
.12
Neonatal encephalopathy
1/1625 (0.1)
1/1625 (0.1)
0.0 (−0.2 to 0.2)
0.94 (0.06 to 14.94)
.96
Neonatal seizures within 28 d
2/1625 (0.1)
1/1625 (0.1)
0.1 (−0.2 to 0.3)
1.87 (0.17 to 20.62)
.61
Neonatal unit admission >48 h
50/1629 (3.1)
61/1637 (3.7)
−0.7 (−2.0 to 0.6)
0.85 (0.59 to 1.23)
.39
Neonatal respiratory support >4 h
37/1629 (2.3)
47/1637 (2.9)
−0.6 (−1.7 to 0.5)
0.81 (0.53 to 1.25)
.35
Persistent pulmonary hypertension
of the newborn
1/1629 (0.1)
3/1637 (0.2)
−0.1 (−0.4 to 0.2)
0.33 (0.03 to 3.22)
.34
Meconium aspiration
9/1629 (0.6)
5/1637 (0.3)
0.2 (−0.3 to 0.8)
1.81 (0.61 to 5.39)
.29
Emergency cesarean delivery
or instrumental vaginal birth
for fetal distress
343/1629 (21.1)
307/1637 (18.8)
2.3 (−0.5 to 5.1)
1.12 (0.98 to 1.29)
.10
Abbreviation: NA, not applicable.
a Generalized estimating equations adjusting for multiple births.
bNot done for cord artery pH less than 7 assumed to be no event.
Intrapartum Sildenafil to Improve Perinatal Outcomes
Original Investigation Research
jama.com
(Reprinted)
JAMA
July 8, 2025
Volume 334, Number 2
155
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/23/2026

```

### Direct-source PDF page 8

```text
Table 4. Tertiary Outcomes
No./total No. (%)
Absolute difference
(95% CI), %
Relative risk/difference
in means
(95% CI)a
Sildenafil citrate
Placebo
Infant-level analyses, No.
1634
1641
NA
NA
Cesarean delivery for fetal distress
142/1629 (8.7)
129/1637 (7.9)
0.8 (−1.1 to 2.8)
1.11 (0.88 to 1.39)
IVB for fetal distress
201/1629 (12.3)
178/1637 (10.9)
1.5 (−0.8 to 3.7)
1.13 (0.94 to 1.37)
Cesarean delivery for other indications
291/1629 (17.9)
257/1637 (15.7)
2.2 (−0.5 to 4.8)
1.14 (0.97 to 1.32)
IVB for other indications
94/1629 (5.8)
114/1637 (7.0)
−1.2 (−2.9 to 0.5)
0.83 (0.64 to 1.08)
Emergency operative birth
(fetal distress was a factor)
471/1629 (28.9)
431/1637 (26.3)
2.6 (−0.5 to 5.7)
1.10 (0.98 to 1.23)
Cesarean delivery
(fetal distress was a factor)
233/1629 (14.3)
201/1637 (12.3)
2.0 (−0.4 to 4.4)
1.16 (0.98 to 1.39)
IVB (fetal distress was a factor)
238/1629 (14.6)
230/1637 (14.1)
0.6 (−1.9 to 3.0)
1.04 (0.88 to 1.23)
Spontaneous vaginal birth
864/1629 (53.0)
931/1637 (56.9)
−3.8 (−7.3 to −0.4)
0.93 (0.88 to 0.99)
Maternal-level analyses, No.
1626
1631
NA
NA
Length of stage 1 labor,
mean (SD), h
4.53 (4.19)
4.53 (4.14)
NA
−0.00 (−0.29 to 0.28)
Length of stage 2 labor,
mean (SD), h
0.85 (1.59)
0.88 (1.39)
NA
−0.03 (−0.14 to 0.07)
Postpartum hemorrhage >1 L
164/1621 (10.1)
128/1627 (7.9)
2.2 (0.2 to 4.3)
1.29 (1.03 to 1.60)
Postpartum hysterectomy
1/1621 (0.1)
1/1627 (0.1)
0.0 (−0.2 to 0.2)
1.00 (0.06 to 16.03)
Uterine rupture
4/1621 (0.2)
2/1627 (0.1)
0.1 (−0.2 to 0.5)
2.01 (0.37 to 10.94)
Maternal intensive care unit
admission
2/1617 (0.1)
1/1614 (0.1)
0.1 (−0.2 to 0.3)
2.00 (0.18 to 21.99)
Maternal mortality
0/1617
0/1618
NA
NA
Abbreviations: IVB, instrumental vaginal birth; NA, not applicable.
a For infant-level analyses, relative risk estimates were calculated with generalized estimating equations accounting for multiple births.
Figure 2. Prespecified Subgroup Analyses According to Maternal and Neonatal Characteristics
Favors
sildenafil citrate
Favors
placebo
0.1
0.01
50
10
1
Relative risk (95% CI)
No. of events/total No. of patients (%)
Sildenafil
citrate
Placebo
Subgroup
Relative risk
(95% CI)
83/1625 (5.1)
84/1625 (5.2)
Overalla
1.02 (0.75-1.37)
Small for gestational age (birth weight <10th
percentile for gestation)
10/106 (9.4)
13/105 (12.4)
Yes
0.76 (0.35-1.66)
73/1519 (4.8)
71/1520 (4.7)
No
1.03 (0.75-1.42)
Multiple pregnancy
2/16 (12.5)
7/20 (35.0)
Yes
0.36 (0.09-1.49)
81/1609 (5.0)
77/1605 (4.8)
No
1.05 (0.77-1.42)
Preeclampsia
4/41 (9.8)
5/38 (13.2)
Yes
0.74 (0.21-2.56)
79/1584 (5.0)
79/1587 (5.0)
No
1.00 (0.74-1.36)
Cesarean delivery in preceding pregnancy
4/57 (7.0)
1/71 (1.4)
Yes
4.98 (0.57-43.35)
79/1568 (5.0)
83/1554 (5.3)
No
0.94 (0.70-1.27)
Noncephalic presentation
1/4 (25.0)
1/2 (50.0)
Yes
0.50 (0.06-4.47)
82/1621 (5.1)
83/1623 (5.1)
No
0.99 (0.73-1.33)
Postnatal diagnosis of fetal anomaly
7/19 (36.8)
4/22 (18.2)
Yes
2.03 (0.70-5.87)
76/1606 (4.7)
80/1603 (5.0)
No
0.95 (0.70-1.29)
The forest plot shows relative risks and 95% CIs in a comparison of sildenafil
citrate with placebo on the composite primary end point. The size of the
squares is proportional to the amount of statistical information in that category
(ie, the inverse of the variance). Interaction tests between treatment and
subgroup were not significant (P > .05).
aThe overall treatment effect is based on a generalized estimating equation
log-binomial model. Effects within subgroups were estimated using a
generalized linear log-binomial model because the analysis was exploratory and
because of the small number of twins within subgroups.
Research Original Investigation
Intrapartum Sildenafil to Improve Perinatal Outcomes
156
JAMA
July 8, 2025
Volume 334, Number 2
(Reprinted)
jama.com
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/23/2026

```

### Direct-source PDF page 9

```text
[2.7%]) vs 11% higher (67 of 742 [9.0%] vs 60 of 738 [8.1%])
at the other sites, but this difference across sites was still
nonsignificant (interaction P = .16).
The findings of this RCT are thus inconsistent with the
promising results of an earlier single-center phase 2 trial20
that showed a 51% reduction in emergency operative birth
rates for intrapartum fetal distress and the findings of a sub-
sequent systematic review and meta-analysis19 of 1090
women that found that PDE5 inhibitor use was associated
with a 42% relative reduction of the same outcome. One
explanation may be that in the previous phase 2 study, the
investigators independently reviewed fetal heart rate
recordings and indications for emergency operative birth for
all trial participants and recategorized these ratings, if
appropriate. However, these steps were not taken in the cur-
rent RCT (given its pragmatic nature), and indications for
operative birth as judged by the treating obstetric team were
accepted without further review. It is therefore possible that
in some cases in which an element of significant fetal com-
promise was present, it was not recorded as the primary rea-
son for emergency operative birth because of another com-
peting indication. Alternatively, the results in the previous
trial may have been a chance finding, demonstrating the
importance of large phase 3 trials to confirm findings of
early promising studies.
Phosphodiesterase type 5 inhibitors may prevent intra-
partumfetaldistressbyincreasingfetoplacentalbloodflow,14-16
reversingvasoconstrictioninuterineandspiralarteries,17,18and
preserving intrapartum placental function and fetoplacental
perfusion,21 thereby increasing fetal oxygenation and toler-
ance to progressive intrapartum hypoxia. However, many of
the data for PDE5 inhibitor use in pregnancy relate to treat-
ment of severe preterm fetal growth restriction.19,33 Because
sildenafil citrate for this indication is not efficacious and may
increase the risk of persistent pulmonary hypertension of the
newborn, it is not recommended for the treatment of fetal
growth restriction and should not be used outside of a re-
search setting.34-36 Our hypothesis-generating finding of a pos-
sible increase in the risk of postpartum hemorrhage may be a
type I error related to multiple comparisons but emphasizes
the need for caution: through its relaxant action on myome-
trial smooth muscle,37 uterine atony may be aggravated, in-
creasing the risk of bleeding.
Strengths of the study include its size, high level of adher-
ence to the protocol, and low levels of missing data. The pri-
mary perinatal outcome included mortality and other out-
comes identified by parents, former patients, health care
professionals, and researchers as important.38 This RCT also
demonstrates the feasibility of intrapartum randomization of
women and that it is possible to recruit for and conduct a large
pharmacologic study even in low-risk pregnancies, notwith-
standing the obvious challenges of therapeutic trials in
pregnancy.39,40
Limitations
This RCT has several limitations. First, the overall incidence
of the primary composite outcome was lower than antici-
pated (5.1% vs 7.0%), suggesting that the study may have
been underpowered for this outcome, as well as several of its
important components (intrapartum stillbirth, neonatal mor-
tality, Apgar score <4 at 5 minutes, neonatal encephalopathy,
and neonatal seizures), which had incidences varying
between 0.1% and 0.5%. Reasons for admission to the neona-
tal nursery may not necessarily reflect complications related
to intrapartum hypoxia. Second, the lower incidence of the
primary outcome in the sildenafil citrate group at the largest
recruiting center (1.8%) compared with that at other sites
(9.0%) that recruited substantially fewer women suggests
that unmeasured heterogeneity in recruitment, conduct, or
outcome measurement for the trial might be responsible for
the absence of a treatment effect like the one observed in the
earlier phase 2 trial.20 Because this was a pragmatic trial,
some variation in specific intrapartum management algo-
rithms between study sites and between individual clinicians
was expected and allowed within the protocol, which may
have accounted for site differences particularly regarding
decisions of when to intervene for suspected fetal compro-
mise or management of postpartum hemorrhage. At the
Mater Mother’s Hospital, there is 24-hour on-site specialist
obstetrician cover for the labor ward in contrast to other sites,
where specialist obstetricians were normally off-site at night.
Nevertheless, although there was a lower rate of the primary
outcome at the Mater Mother’s Hospital compared with other
sites, there was no evidence of a differential treatment effect
by site (test for interaction P = .16). There was no reduction
observed in operative birth for fetal compromise even at the
Mater Mother’s hospital, and for the trial as a whole, there
was no difference in fetal distress rates between both groups.
Third, we do not have pharmacokinetic information, making
it difficult to be certain whether the lack of effect on out-
comes was due to inadequate maternal levels of sildenafil
citrate or for other drug-related reasons. Fourth, because
more than 80% of women in this trial underwent induction
of labor, it is not possible to generalize these findings to all
women attempting vaginal birth. Fifth, given the low inci-
dence of adverse neonatal outcomes secondary to intrapar-
tum hypoxic injury in high-income settings, reliably detect-
ing a moderate but clinically important 10% reduction in
poor neonatal outcome by any intervention, pharmacologic
or otherwise, may require randomization of more than
75 000 participants.20,41
Conclusions
Maternal oral sildenafil citrate during term labor did not re-
sult in a lower incidence of adverse perinatal outcomes po-
tentially related to intrapartum hypoxia or in a reduction in
emergency operative birth for intrapartum fetal compro-
mise. These results, however, do not preclude its investiga-
tion in other areas of pregnancy care and different popula-
tions. Future research should focus on better identification of
at-risk infants, alternative intrapartum therapies to mitigate
complications related to hypoxia during labor, and consider-
ation of mode and timing of birth to improve perinatal out-
comes for late-gestation infants.
Intrapartum Sildenafil to Improve Perinatal Outcomes
Original Investigation Research
jama.com
(Reprinted)
JAMA
July 8, 2025
Volume 334, Number 2
157
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/23/2026

```

### Direct-source PDF page 10

```text
ARTICLE INFORMATION
Accepted for Publication: April 28, 2025.
Published Online: June 9, 2025.
doi:10.1001/jama.2025.7710
Author Affiliations: Mater Mothers’ Hospital and
Mater Research Institute–University of Queensland,
Brisbane, Queensland, Australia (Kumar, Flenady,
Liley); National Health and Medical Research
Council Stillbirth Centre for Research Excellence,
Brisbane, Queensland, Australia (Kumar, Flenady);
Faculty of Medicine, University of Queensland,
Brisbane, Queensland, Australia (Kumar); NHMRC
Clinical Trials Centre, University of Sydney, Sydney,
New South Wales, Australia (Tarnow-Mordi, Seidler,
Simes, O’Connell); Department of Obstetrics and
Gynecology, Monash University, Melbourne,
Victoria, Australia (Mol); Cerebral Palsy Alliance,
Sydney, New South Wales, Australia (Badawi);
Department of Neonatology, University of Sydney,
Sydney, New South Wales, Australia (Badawi);
Obstetrics and Gynecology, Mercy Hospital,
University of Melbourne, Melbourne, Victoria,
Australia (Walker); Department of Obstetrics and
Gynecology, Liverpool Hospital, Sydney, New South
Wales, Australia (Hyett); Department of Obstetrics
and Gynecology, Western Sydney University,
New South Wales, Australia (Hyett); Department of
Child and Adolescent Psychiatry, University Medical
Center Rostock, Rostock, Germany (Seidler);
German Center for Child and Adolescent Health
(DZKJ), Greifswald/Rostock, Rostock, Germany
(Seidler); School of Public Health, University of
Technology Sydney, Sydney, New South Wales,
Australia (Callander).
Author Contributions: Drs Kumar and O’Connell
had full access to all of the data in the study and
take responsibility for the integrity of the data and
the accuracy of the data analysis. Drs Kumar and
Tarnow-Mordi contributed equally to the
manuscript. Drs Simes and O’Connell served as
co–last authors.
Study concept and design: Kumar, Tarnow-Mordi,
Mol, Flenady, Liley, Badawi, Hyett, Seidler,
Callander, Simes, O'Connell.
Acquisition, analysis, or interpretation of data:
Kumar, Tarnow-Mordi, Liley, Badawi, Walker,
Seidler, Callander, Simes, O'Connell.
Drafting of the manuscript: Kumar, Tarnow-Mordi,
Flenady, Badawi, O'Connell.
Critical review of the manuscript for important
intellectual content: Kumar, Tarnow-Mordi, Mol,
Flenady, Liley, Walker, Hyett, Seidler, Callander,
Simes, O'Connell.
Statistical analysis: Tarnow-Mordi, Mol, O'Connell.
Obtained funding: Kumar, Tarnow-Mordi, Flenady,
Hyett, Callander.
Administrative, technical, or material support:
Kumar, Tarnow-Mordi, Badawi, Hyett, Callander.
Supervision: Kumar, Tarnow-Mordi, Flenady, Walker.
Review and interpretation of statistical analysis:
Simes.
Conflict of Interest Disclosures: Dr Kumar
reported grants from the National Health and
Medical Research Council (NHMRC) during the
conduct of the study. Dr Tarnow-Mordi reported
grants from NHMRC during the conduct of the
study. Dr Mol reported consultancy fees, travel
support, and grants from Merck KGaA; and
consultancy fees from Ferring, Organon, and
Norgine outside the submitted work. Dr Flenady
reported serving as chief investigator for the
Stillbirth Centre of Research Excellence, funded by
NHMRC. Dr Simes reported grants from Roche,
Merck Sharp & Dohme, Bayer, Bristol Myers Squibb,
and Amgen to his institution outside the submitted
work. No other disclosures were reported.
Funding/Support: This study was funded by the
Australian NHMRC Medical Research Future Fund
(grant APP1199329). The legal sponsor of the trial
was the University of Sydney.
Role of the Funder/Sponsor: The funder had no
role in the design and conduct of the study;
collection, management, analysis, and
interpretation of the data; preparation, review, or
approval of the manuscript; and decision to submit
the manuscript for publication.
Group Information: The iSEARCH investigators are
listed in Supplement 4.
Data Sharing Statement: See Supplement 5.
Additional Contributions: The trial was
coordinated by the NHMRC Clinical Trials Centre,
University of Sydney.
Additional Information: A trial management
committee and an independent data and safety
monitoring committee monitored the trial. The trial
statistician had full access to all the data.
REFERENCES
1. Turner JM, Mitchell MD, Kumar SS. The
physiology of intrapartum fetal compromise at
term. Am J Obstet Gynecol. 2020;222(1):17-26.
doi:10.1016/j.ajog.2019.07.032
2. Graham EM, Ruis KA, Hartman AL, Northington
FJ, Fox HE. A systematic review of the role of
intrapartum hypoxia-ischemia in the causation of
neonatal encephalopathy. Am J Obstet Gynecol.
2008;199(6):587-595. doi:10.1016/j.ajog.2008.06.
094
3. Stoke R, Schreiber V, Hocking K, Jardine L,
Kumar S. Perinatal antecedents of moderate and
severe neonatal hypoxic ischaemic
encephalopathy: an Australian birth cohort study.
Aust N Z J Obstet Gynaecol. 2023;63(3):409-417.
doi:10.1111/ajo.13665
4. Triggs T, Crawford K, Hong J, Clifton V, Kumar S.
The influence of birthweight on mortality and
severe neonatal morbidity in late preterm and term
infants: an Australian cohort study. Lancet Reg
Health West Pac. 2024;45:101054. doi:10.1016/j.
lanwpc.2024.101054
5. McIntyre S, Nelson KB, Mulkey SB, Lechpammer
M, Molloy E, Badawi N; Newborn Brain Society
Guidelines and Publications Committee. Neonatal
encephalopathy: focus on epidemiology and
underexplored aspects of etiology. Semin Fetal
Neonatal Med. 2021;26(4):101265. doi:10.1016/j.
siny.2021.101265
6. Sandall J, Tribe RM, Avery L, et al. Short-term
and long-term effects of caesarean section on the
health of women and children. Lancet. 2018;392
(10155):1349-1357. doi:10.1016/S0140-6736(18)
31930-5
7. MacLennan A. A template for defining a causal
relation between acute intrapartum events and
cerebral palsy: international consensus statement.
BMJ. 1999;319(7216):1054-1059. doi:10.1136/bmj.319.
7216.1054
8. Executive summary: neonatal encephalopathy
and neurologic outcome, second edition: report of
the American College of Obstetricians and
Gynecologists’ Task Force on Neonatal
Encephalopathy. Obstet Gynecol. 2014;123(4):896-
901. doi:10.1097/01.AOG.0000445580.65983.d2
9. Alfirevic Z, Devane D, Gyte GM, Cuthbert A.
Continuous cardiotocography (CTG) as a form of
electronic fetal monitoring (EFM) for fetal
assessment during labour. Cochrane Database Syst
Rev. 2017;2(2):CD006066. doi:10.1002/14651858.
CD006066.pub3
10. Baillie GS, Tejeda GS, Kelly MP. Therapeutic
targeting of 3′,5′-cyclic nucleotide
phosphodiesterases: inhibition and beyond. Nat
Rev Drug Discov. 2019;18(10):770-796. doi:10.
1038/s41573-019-0033-4
11. Salonia A, Rigatti P, Montorsi F. Sildenafil in
erectile dysfunction: a critical review. Curr Med Res
Opin. 2003;19(4):241-262. doi:10.1185/
030079903125001839
12. Kelly LE, Ohlsson A, Shah PS. Sildenafil for
pulmonary hypertension in neonates. Cochrane
Database Syst Rev. 2017;8(8):CD005494. doi:10.
1002/14651858.CD005494.pub4
13. Barnes H, Brown Z, Burns A, Williams T.
Phosphodiesterase 5 inhibitors for pulmonary
hypertension. Cochrane Database Syst Rev. 2019;1
(1):CD012621. doi:10.1002/14651858.CD012621.pub2
14. Groom KM, David AL. The role of aspirin,
heparin, and other interventions in the prevention
and treatment of fetal growth restriction. Am J
Obstet Gynecol. 2018;218(2S):S829-S840. doi:10.
1016/j.ajog.2017.11.565
15. Dastjerdi MV, Hosseini S, Bayani L. Sildenafil
citrate and uteroplacental perfusion in fetal growth
restriction. J Res Med Sci. 2012;17(7):632-636.
16. Hale SA, Jones CW, Osol G, Schonberg A,
Badger GJ, Bernstein IM. Sildenafil increases uterine
blood flow in nonpregnant nulliparous women.
Reprod Sci. 2010;17(4):358-365. doi:10.1177/
1933719109354648
17. Wareing M, Myers JE, O’Hara M, Baker PN.
Sildenafil citrate (Viagra) enhances vasodilatation in
fetal growth restriction. J Clin Endocrinol Metab.
2005;90(5):2550-2555. doi:10.1210/jc.2004-1831
18. Samangaya RA, Wareing M, Skillern L, Baker PN.
Phosphodiesterase inhibitor effect on small artery
function in preeclampsia. Hypertens Pregnancy. 2011;
30(2):144-152. doi:10.3109/10641955.2010.484083
19. Turner JM, Russo F, Deprest J, Mol BW, Kumar S.
Phosphodiesterase-5 inhibitors in pregnancy:
systematic review and meta-analysis of maternal and
perinatal safety and clinical outcomes. BJOG. 2022;
129(11):1817-1831. doi:10.1111/1471-0528.17163
20. Turner J, Dunn L, Tarnow-Mordi W, Flatley C,
Flenady V, Kumar S. Safety and efficacy of sildenafil
citrate to reduce operative birth for intrapartum
fetal compromise at term: a phase 2 randomized
controlled trial. Am J Obstet Gynecol. 2020;222(5):
401-414. doi:10.1016/j.ajog.2020.01.025
21. Turner J, Dunn L, Kumar S. Oral sildenafil citrate
during labor mitigates the intrapartum decline in
placental growth factor in term pregnancies. Am J
Obstet Gynecol. 2020;223(4):588-590. doi:10.
1016/j.ajog.2020.05.030
Research Original Investigation
Intrapartum Sildenafil to Improve Perinatal Outcomes
158
JAMA
July 8, 2025
Volume 334, Number 2
(Reprinted)
jama.com
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/23/2026

```

### Direct-source PDF page 11

```text
22. Kumar S, Tarnow-Mordi W, Mol BW, et al. The
iSEARCH randomised controlled trial protocol:
a pragmatic Australian phase III clinical trial of
intrapartum sildenafil citrate to improve outcomes
potentially related to intrapartum hypoxia. BMJ Open.
2024;14(9):e082943. doi:10.1136/bmjopen-2023-
082943
23. Blackburn R, Mehmeti A, Russell S, Rivers F,
Blott M; Guideline Committee. Intrapartum
care—updated summary of NICE guidance. BMJ.
2024;384:2885. doi:10.1136/bmj.p2885
24. National Institute for Health and Care
Excellence. Inducing labour. Published November 4,
2021. Accessed January 31, 2025. https://www.
nice.org.uk/guidance/ng207
25. Royal Australian and New Zealand College of
Obstetricians and Gynaecologists. Intrapartum fetal
surveillance: clinical guideline—fourth edition 2019.
Accessed January 31, 2025. https://ranzcog.edu.au/
wp-content/uploads/Intrapartum-Fetal-
Surveillance.pdf
26. Grobman WA. Labor induction vs expectant
management of low-risk pregnancy. N Engl J Med.
2018;379(23):2278-2279. doi:10.1056/NEJMc1812323
27. Rial-Crestelo M, Lubusky M, Parra-Cordero M,
et al; RATIO37 Study Group. Term planned delivery
based on fetal growth assessment with or without
the cerebroplacental ratio in low-risk pregnancies
(RATIO37): an international, multicentre,
open-label, randomised controlled trial. Lancet.
2024;403(10426):545-553. doi:10.1016/S0140-6736
(23)02228-6
28. Peto R, Pike MC, Armitage P, et al. Design and
analysis of randomized clinical trials requiring
prolonged observation of each patient, 1:
introduction and design. Br J Cancer. 1976;34(6):
585-612.
29. Haybittle JL. Repeated assessment of results in
clinical trials of cancer treatment. Br J Radiol. 1971;
44(526):793-797. doi:10.1259/0007-1285-44-526-
793
30. Schulz KF, Grimes DA. Multiplicity in
randomised trials 1: endpoints and treatments.
Lancet. 2005;365(9470):1591-1595. doi:10.1016/
S0140-6736(05)66461-6
31. Schulz KF, Altman DG, Moher D; CONSORT
Group. CONSORT 2010 statement: updated
guidelines for reporting parallel group randomised
trials. BMJ. 2010;340:c332. doi:10.1136/bmj.c332
32. Collins GS, Reitsma JB, Altman DG, Moons KG.
Transparent reporting of a multivariable prediction
model for individual prognosis or diagnosis
(TRIPOD): the TRIPOD statement. BMJ. 2015;350:
g7594. doi:10.1136/bmj.g7594
33. Pels A, Ganzevoort W, Kenny LC, et al.
Interventions affecting the nitric oxide pathway
versus placebo or no therapy for fetal growth
restriction in pregnancy. Cochrane Database Syst Rev.
2023;7(7):CD014498. doi:10.1002/14651858.
CD014498
34. Ganzevoort W, Gluud C, Lim K, Mol B, Groom K.
The STRIDER trials: ongoing research. Lancet Child
Adolesc Health. 2018;2(3):e3. doi:10.1016/S2352-
4642(18)30036-1
35. Groom KM, Ganzevoort W, Alfirevic Z, Lim K,
Papageorghiou AT; STRIDER Consortium. Clinicians
should stop prescribing sildenafil for fetal growth
restriction (FGR): comment from the STRIDER
Consortium. Ultrasound Obstet Gynecol. 2018;52
(3):295-296.
36. Pels A, Derks J, Elvan-Taspinar A, et al; Dutch
STRIDER Trial Group. Maternal sildenafil vs placebo
in pregnant women with severe early-onset fetal
growth restriction: a randomized clinical trial. JAMA
Netw Open. 2020;3(6):e205323. doi:10.1001/
jamanetworkopen.2020.5323
37. Khan RN, Hamoud H, Warren A, Wong LF,
Arulkumaran S. Relaxant action of sildenafil citrate
(Viagra) on human myometrium of pregnancy. Am J
Obstet Gynecol. 2004;191(1):315-321. doi:10.1016/j.
ajog.2003.11.005
38. Webbe JWH, Duffy JMN, Afonso E, et al. Core
outcomes in neonatology: development of a core
outcome set for neonatal research. Arch Dis Child
Fetal Neonatal Ed. 2020;105(4):425-431.
39. Eke AC, Dooley KE, Sheffield JS. Pharmacologic
research in pregnant women—time to get it right.
N Engl J Med. 2019;380(14):1293-1295. doi:10.
1056/NEJMp1815325
40. Eke AC, Olagunju A, Momper J, et al;
Participants of the WHO-IMPAACT Workshop on
“Approaches to Optimize and Accelerate
Pharmacokinetic Studies in Pregnant and Lactating
Women”. Optimizing pharmacology studies in
pregnant and lactating women using lessons from
HIV: a consensus statement. Clin Pharmacol Ther.
2021;110(1):36-48. doi:10.1002/cpt.2048
41. Demoule A, Carreira S, Lavault S, et al. Impact
of earplugs and eye mask on sleep in critically ill
patients: a prospective randomized study. Crit Care.
2017;21(1):284. doi:10.1186/s13054-017-1865-0
Intrapartum Sildenafil to Improve Perinatal Outcomes
Original Investigation Research
jama.com
(Reprinted)
JAMA
July 8, 2025
Volume 334, Number 2
159
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
Downloaded from jamanetwork.com by University of Arizona Health Sciences Library user on 07/23/2026

```
