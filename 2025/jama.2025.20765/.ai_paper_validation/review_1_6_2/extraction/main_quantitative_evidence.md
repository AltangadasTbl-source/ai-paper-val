# Complete main-paper quantitative evidence map

Scope: DOC-001, jama_zahid_2025_oi_250093_1768590553.08463.pdf, PDF pp. 1-9, REPORT. Mapper runtime: 01a12c3e-01ad-7673-9de4-6a93ac228f9a; gpt-6.1-sol, medium. This is source mapping, without candidate diagnosis or adjudication. Local descriptive keys are matching aids; numeric/statistical relationship IDs belong to the checkers.

## Evidence and coverage

All nine canonical reusable normalized text pages were read, together with source-linked rendered pp. 6-7 for exact Table 2 alignment and Figure 2 visual inspection. Native sorted layout was freshly extracted from the supplied PDF using `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py text jama_zahid_2025_oi_250093_1768590553.08463.pdf --first 1 --last 9 .ai_paper_validation/review_1_6_2/preprocessing/main_source_layout.txt --layout`. Engine: PyMuPDF 1.26.4, sorted reading order, CPU. Native extraction and reusable normalized text corroborate the transcriptions below; rendered page layout controls ambiguous alignment. No OCR was necessary. No legacy scientific conclusions were read. Scientific coverage gaps: none. Figure 2 provides graphical, rather than numerically tabulated, probabilities and credible limits; approximate visual values below remain explicitly approximate.

Every source link below is relative to this artifact and terminates in its exact PDF page.

| Page | Content inspected | Mapping status |
|---|---|---|
| [1](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1) | Abstract: design, intervention, endpoints, flow, primary and secondary results | COMPLETE |
| [2](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=2) | Key Points; eligibility, randomization, visits and intervention design | COMPLETE |
| [3](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3) | Intervention schedule; endpoint definitions; sample-size assumptions; statistical methods | COMPLETE |
| [4](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4) | Figure 1 flow and exclusions; participants, missingness and primary outcome narrative | COMPLETE |
| [5](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5) | Table 1 and notes; secondary outcomes, adverse events, subgroup and sensitivity claims | COMPLETE |
| [6](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6) | Table 2, all 11 outcome rows and footnotes | COMPLETE |
| [7](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=7) | Figure 2, all 27 clusters, populations and fitted/observed contrasts; discussion continuation | COMPLETE |
| [8](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8) | Discussion, mortality and ICC claims; limitations, conclusion; article information | COMPLETE |
| [9](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=9) | References only; no applicable trial quantitative relationships | COMPLETE_NO_APPLICABLE |

## Design, definitions, methods and matching claims

Here and throughout, M denotes mHealth, U usual care. Order of paired values is M then U. Every row beginning `main:` is one mapped relationship bundle; a bundle retains all components needed to compare the same result. Repeated locations are attached to the same bundle rather than counted as another independent relationship.

| Key | Source locations | Quantitative/statistical content and matching context |
|---|---|---|
| main:design | pp. 1-2 abstract/design/procedures | Two-group multicenter cluster RCT, 27 TB clinics, Bangladesh and Pakistan; 2:1 M:U allocation; country-stratified randomization by independent masked statistician with computer-generated lists. Participants/researchers unmasked, statistician masked during analysis. September 18, 2023-January 2, 2025; follow-up 6 months. Phase 3 named in published protocol. |
| main:eligibility | p. 2 design/participants; p. 1 abstract | Clinics ≥50 new TB patients/month; patient age ≥15 years, drug-sensitive pulmonary TB diagnosed within past 4 weeks, daily smoking defined ≥1 puff on ≥25 days in last month, willing to quit and mobile access. Multidrug-resistant, miliary/extrapulmonary TB and treatment for tobacco dependence excluded. |
| main:visits | p. 2 procedures | Day 0, week 9, month 6 collection; missed appointments assessed within 5 days by phone/home. Weekly fidelity calls in both groups, checking message receipt/reading in M and contamination in U. |
| main:intervention | p. 1 abstract; p. 3 intervention | M n=720, U n=360; first 3 welcoming messages; 134 unique messages in 6 months: 100 in month 1 (3-4/day), 30 in month 2 (1/day), 4 in months 3-6 (1/month). Abstract daily 2 months, monthly 4 months. Opt-out possible; weekly system reports. Pilot phase 2 involved 16 patients. |
| main:cointervention | p. 3 intervention | Both groups written tobacco information/quit advice and TB medications; rifampicin/isoniazid/pyrazinamide/ethambutol first 2 months, rifampicin/isoniazid thereafter; no cessation medication offered. |
| main:primary-definition | pp. 1-3 abstract/Key Points/outcomes | Primary biochemically verified continuous abstinence 6 months after randomization. Self-report ≤5 cigarettes/bidis/water-pipe sessions since quit date, set 5 days after enrollment; CO <10 ppm at month 6. Baseline concomitant smokeless tobacco: urine cotinine rapid test, negative verifies abstinence. Abstract and Key Points describe continuous self-report supported by biochemical verification at month 6. |
| main:secondary-definition | pp. 1,3 outcomes | Exploratory analyses of secondary outcomes: point abstinence previous 7 days at week 9/month 6; TB adherence days medication taken; treatment success=cured+completed; failure; default=interruption ≥2 months; deaths at month 6. Abstract lists these as secondary outcomes. |
| main:sample-size | p. 3 sample size | Phase 3, power 90%, 2-sided significance 5%; 6-month abstinence probabilities M 18%, U 8%; ICC .02; cluster size 26; design effect 1.5; anticipated attrition 20%; resulting n=1080, 27 clusters capped at 40 participants each. Allocation 2:1 linked to pp. 1-2. |
| main:descriptive-method | p. 3 statistical analysis | Normality visual and Shapiro-Wilk; categorical frequencies/percentages, continuous means/SDs. Software R 4.4.3, JASP 0.19.3 (2024). |
| main:abstinence-model | p. 3 statistical analysis; p. 6 Table 2 headers/note a | Mixed-effects model fixed intervention and relevant post hoc covariates age, sex, education, occupation, smoking duration; random clusters. Text states logistic regression within mixed-effects framework for categorical outcomes; Table 2 effect label RR, crude and adjusted, footnote mixed-effects models for RR. |
| main:bayesian-model | p. 3 statistical analysis; pp. 4-5 narrative; p. 7 Figure 2 | Bayesian hierarchical logistic model in brms, cluster-level quit probabilities and 95% credible intervals, observed proportions overlaid. Figure posterior means include fixed+random effects. Narrative heterogeneity, generally higher fitted rates in M. |
| main:icc-method | p. 3 statistical analysis; p. 6 Table 2 note c; p. 8 limitations | Text: all analyses ICC from mixed-effects logistic regression variance components using lme4. Table note ICC reported for RR models only. Limitations observed ICC .19 vs assumed .02. Each Table 2 ICC retained below. |
| main:death-model | p. 3 statistical analysis; p. 6 Table 2 notes a,d | Cox proportional hazards frailty model, site-level clustering; adjusted shared frailty Cox model; HR label; six-month death comparison. Table note adjustment covariates as above. |
| main:multiplicity-test | p. 3 statistical analysis | Secondary outcomes exploratory, no multiple-comparison adjustment. All statistical tests 2-sided, P<.05 significant. |
| main:missingness-analysis | p. 3 statistical analysis; p. 6 table | Missing primary treated negative/not abstinent. ITT and complete-case analyses (missing discarded). Table calls complete-case rows PP and defines PP as per-protocol. Exact Table 2 denominators below. |
| main:sensitivity-co | p. 3 methods; p. 4 narrative; p. 6 table | Post hoc primary sensitivity CO <6 ppm; narrative RR 3.7 (95% CI 2.4-5.8), described consistent and robust. Four CO/population rows preserved below. |
| main:sensitivity-death | pp. 3,5 | Post hoc sensitivity excluding deaths; p. 5 results consistent with primary ITT, refers eTable 9. |
| main:subgroups | pp. 3,5 | Called prespecified: age <40/≥40; education none/primary/secondary or higher; employment active/dependent/retired; smoking duration <24/≥24 years. P. 5 says effect consistent across age, education, employment, ability to read SMS, smoking duration; eTable 8. |
| main:cluster-analysis | pp. 3,5 | Recruitment, abstinence, success, death rates at cluster level; multilevel exploration of cluster characteristics; p. 5 shorter smoking duration and higher education modified primary outcome (eTable 7), variations despite similar size (eTables 5-6). |
| main:primary-narrative | pp. 1-2,4 | Abstract 300/720 (41.7%) vs 55/360 (15.3%), RR 3.0 (2.0-4.9); Key Points n=1080, proportions 41.7% vs15.3%, significantly higher; body adds 95% proportion CIs 38.0-45.4 and11.7-19.4, adjusted RR3.2 (2.2-5.2); links Table 2 rows. |
| main:selfreport-narrative | p. 4 primary | Continuous self-report only 47.5% vs19.4%, matched to Table 2 342/720 vs70/360. |
| main:co-levels | p. 4 primary | Among biochemically verified continuous abstainers mean CO M3.54 (SD2.1) ppm, U4.38 (SD2.8) ppm, described similar; no P displayed. |
| main:adherence | pp. 1,5 secondary | Mean M174.3 (SD21.5) days, U178.0 (SD12.1) days, P=.23, described similar; links eTable3, no exact test named in main article. |
| main:mortality-interpretation | pp. 1,5,7-8 | Lower M mortality; p.5 TB disease61.5% (32/52) most common cause, eTable4. P.8 says exploratory analyses 4.8% trial participants died of TB within6 months; probability death significantly higher U; discussion potential mortality reduction within6 months. All exact claims preserved for matching, with no diagnosis. |
| main:retention-fidelity | pp. 1,4,8 | Abstract985 retained (91%); p.4 all M confirmed receipt; no cessation medication use, no contamination; p.8 all clusters and >90% participants retained, messages delivered as intended. |
| main:discussion-comparison | pp. 7-8 | Current trial continuous and point abstinence higher M; TB adherence/success did not differ, fewer deaths M. Conclusion feasible/effective tobacco cessation. No added current-trial estimate. |

## Participant flow and attrition

All relationships in this section are at [PDF p. 4, Figure 1 and Participants](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4), with abstract repeats at p.1. Exclusion reasons may overlap: Figure 1 note b explicitly permits more than one reason per participant. Clinic note a defines <50 new TB registrations/month or facilities unsuitable.

| Key | Printed quantity | Context or matching relationship |
|---|---|---|
| main:flow-total | 249 clusters;9232 patients assessed;222 clusters and8152 patients excluded;27 clusters randomized;1080 enrolled | Narrative six refusals,8146 not meeting inclusion; M720,U360. |
| main:flow-clinic-reasons |182 fewer than50 new registrations/month;40 not fit for trial | Reasons within222 excluded clusters. |
| main:flow-smoking |7069 not current smoker | Patient reasons within8152 exclusions; overlapping allowed. |
| main:flow-pulmonary |2783 not pulmonary TB | Same. |
| main:flow-time |1820 not diagnosed within last4 weeks | Same. |
| main:flow-phone |1290 no mobile access | Same. |
| main:flow-age |385 age<15 | Same. |
| main:flow-quit |273 unwilling to quit | Same. |
| main:flow-literacy |236 cannot read and no household reader | Same. |
| main:flow-refusal |6 refused | Same; narrative separates six from8146. |
| main:flow-m |18 clusters;720 randomized and received M,40 per cluster;0 clusters/53 participants lost:25 deaths,18 no contact,10 withdrew;720 primary analysis | Complete-case denominator667 in Table2. |
| main:flow-u |9 clusters;360 randomized and received U,40 per cluster;0 clusters/42 participants lost:27 deaths,9 no contact,6 withdrew;360 primary analysis | Complete-case denominator318 in Table2. |
| main:attrition-percent |8.8% no primary outcome:4.8% died,1.5% withdrew,2.5% lost contact | Body says no other missing outcomes; except death attrition comparable between arms. Linked counts52,16,27 and total95 from figure;985 retained from abstract. |

## Table 1 baseline characteristics, complete

[PDF p. 5, Table 1](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5). Participant denominators M720,U360 unless another population is identified by context. The low-addiction values are preserved as printed; cigarette-user counts679,326 also retained for population matching. Smoking types may coexist with each other and concurrent smokeless use; no exclusivity stated. BMI kg/m²; IQR displayed as a single width. Dependents include unemployed/homemakers/students/otherwise inactive. TB stages based on signs/symptoms:1 mild-moderate,2 severe,3 very severe. Narrative p.4 repeats cigarette/smokeless percentages, consumption and past quit attempts.

| Key | Characteristic/unit | M | U |
|---|---|---|---|
| main:baseline-clusters | Total clusters |18|9|
| main:baseline-size | Cluster size |40|40|
| main:baseline-rural | Rural clusters |11|7|
| main:baseline-tb-rate | Average TB cases/month |142|93|
| main:baseline-n | Participants |720|360|
| main:baseline-age | Age mean(SD),years |48.7(15.8)|48.7(15.9)|
| main:baseline-male | Male n(%) |698(96.9)|345(95.8)|
| main:baseline-female | Female n(%) |22(3.1)|15(4.2)|
| main:baseline-bmi | BMI median(IQR) |18.7(4)|18.6(4)|
| main:baseline-edu-none | No education n(%) |315(43.8)|155(43.1)|
| main:baseline-edu-primary | Primary n(%) |175(24.3)|114(31.7)|
| main:baseline-edu-middle | Middle n(%) |109(15.1)|43(11.9)|
| main:baseline-edu-secondary | Secondary n(%) |89(12.4)|36(10)|
| main:baseline-edu-higher | Higher n(%) |32(4.4)|12(3.3)|
| main:baseline-single | Single n(%) |83(11.5)|37(10.3)|
| main:baseline-married | Married n(%) |607(84.3)|304(84.4)|
| main:baseline-separated | Separated/divorced n(%) |30(4.2)|19(5.3)|
| main:baseline-employed | Employed n(%) |560(77.8)|275(76.4)|
| main:baseline-dependent | Dependents n(%) |128(17.8)|71(19.7)|
| main:baseline-retired | Retired n(%) |32(4.4)|14(3.9)|
| main:baseline-literacy | Able read messages n(%) |425(59.0)|225(62.5)|
| main:baseline-stage1 | TB stage1 n(%) |629(87.4)|326(90.6)|
| main:baseline-stage2 | TB stage2 n(%) |45(6.3)|20(5.6)|
| main:baseline-stage3 | TB stage3 n(%) |46(6.4)|14(3.9)|
| main:baseline-cigarette | Cigarette users n(%) |679(94.3)|326(90.6)|
| main:baseline-hookah | Hookah users n(%) |61(8.5)|35(9.7)|
| main:baseline-bidi | Bidi users n(%) |21(2.9)|21(5.8)|
| main:baseline-smokeless | Concurrent smokeless n(%) |50(6.9)|8(2.2)|
| main:baseline-bidi-dose | Bidi/day median(IQR) |8(10.0)|15(14.0)|
| main:baseline-cigarette-dose | Cigarette/day median(IQR) |5(6.0)|7(6.0)|
| main:baseline-hookah-dose | Hookah/day median(IQR) |3(4.0)|3(2.0)|
| main:baseline-home | Smoking allowed home n(%) |482(66.9)|189(52.5)|
| main:baseline-quit-history | Past quit attempt n(%) |178(24.7)|33(9.2)|
| main:baseline-duration | Smoking years mean(SD) |24.8(15.1)|24.6(15.2)|
| main:baseline-start-age | Starting age years median(IQR) |20(9.0)|20(8.0)|
| main:baseline-addiction | Heaviness Smoking Index low addiction n(%) |514(75.7)|212(65.0)|

## Table 2 full outcome relationship map

[PDF p. 6, Table 2](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6). All intervals 95% CI; group percentages and absolute differences are percentage points. Header prints `Absolute difference`, with no signed contrast specified. Effect contrast is M relative to U from narrative. Columns `Crude RR`, `Adjusted RR/HR`; ICC follows each. Adjustment is post hoc age,sex,education,occupation,smoking duration, with mixed-effects clustering for RR and shared-frailty Cox for HR. RR=relative risk; ITT=intention-to-treat; PP=per-protocol in table, complete case in methods. No P values, test statistics or standard errors appear in this table. Each row contains all printed columns; `NA` is literal not applicable. Source image confirms adjusted self-report upper limit printed `42`, without decimal.

| Key | Outcome/population/time | M n/N;%(CI) | U n/N;%(CI) | Absolute difference(CI) | Crude RR(CI);ICC | Adjusted RR/HR(CI);ICC |
|---|---|---|---|---|---|---|
| main:outcome-primary-itt10 | Biochemically verified abstinence month6,<10ppm,ITT |300/720;41.7(38.0,45.4)|55/360;15.3(11.7,19.4)|26.4(21.0,31.6)|3.0(2.0,4.9);.18|3.2(2.2,5.2);.18|
| main:outcome-primary-pp10 | Same month6,<10ppm,PP |300/667;45(41.2,48.8)|55/318;17.3(13.3,21.9)|27.7(22.1,33.3)|2.9(2.0,4.7);.19|3.1(2.1,5.2);.19|
| main:outcome-primary-itt6 | Biochemically verified abstinence,<6ppm,ITT;month6 by context |264/720;36.7(33.1,40.3)|38/360;10.6(7.6,14.2)|26.1(21.2,30.7)|3.7(2.4,5.8);.16|3.9(2.4,6.9);.18|
| main:outcome-primary-pp6 | Same month6,<6ppm,PP |264/667;39.6(35.9,43.4)|39/318;11.9(8.6,16.1)|27.7(22.5,32.8)|3.6(2.14,6.87);.17|3.8(2.3,7.7);.18|
| main:outcome-continuous-self | Continuous abstinence self-report only,ITT |342/720;47.5(43.8,51.2)|70/360;19.4(15.5,23.9)|28.1(22.6,33.5)|2.7(1.8,4.1);.19|2.8(1.9,42);.19|
| main:outcome-point9 | Point abstinence previous7days,week9,ITT |353/720;49.0(45.3,52.7)|75/360;20.8(16.7,25.4)|28.2(22.6,33.8)|2.6(1.8,3.9);.19|2.7(1.8,4.3);.18|
| main:outcome-point6 | Point abstinence previous7days,month6,ITT |400/720;55.6(51.8,59.2)|82/360;22.8(18.5,27.5)|32.8(27.1,38.4)|2.7(2.0,3.8);.19|2.7(1.9,4.0);.19|
| main:outcome-success | TB treatment success,cured+completed |643/720;89.3(86.8,91.5)|308/360;85.6(81.5,89.0)|3.8(-.5,8.2)|1.2(.9,1.6);.16|1.2(.9,1.5);.15|
| main:outcome-death | Death,6months |25/720;3.5(2.2,5.0)|27/360;7.5(5.0,10.7)|4(1.0,7.1)|NA;NA|HR.4(.2,.9);NA|
| main:outcome-default | TB treatment interruption≥2months |22/720;3.1(1.9,4.6)|7/360;1.9(.8,4.0)|1.1(-.8,3.0)|NA;NA|NA;NA|
| main:outcome-failure | TB treatment failure |1/720;.1(.01,.8)|2/360;.5(.1,2.0)|.4(-.4,1.2)|NA;NA|NA;NA|

Footnote f: mixed-effects models could not be estimated for default/failure because very low event numbers across clusters. Footnote b: number outcomes/total in group. Footnote e: CO breath-test cutoffs. Narrative matches primary,success,death,default,failure above; abstract repeats same inferential values where stated. Secondary point abstinence narrative says higher M at both times.

## Figure 2: every cluster

[PDF p. 7, Figure 2](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=7). Two panels: A M18 clusters,B U9 clusters. Each cluster has posterior mean (filled) with95% credible whisker and observed proportion (open) with graphical whisker; caption specifies whiskers95% credible intervals, posterior fixed+random. Horizontal axes `Cluster-level quit probability,%`, ticks0,20,40,60,80,100; no individual numeric posterior estimates/limits printed. Vertical IDs18→1/9→1; `Cluster size at6-mo follow-up,No.` printed beside each. Dashed vertical reference near36%; no numerical label or inferential threshold stated. Below is visual mapping, with approximate percentages read to nearest few points solely to preserve graphical direction, containment and ordering. They must not be treated as exact printed estimates or used for precision-based findings.

| Key | Group/cluster | Follow-up N printed | Posterior mean; observed proportion, approximate % | Posterior95% interval graphical span, approximate % |
|---|---|---:|---|---|
| main:figure-m18 |M18|38|84;92|78-97|
| main:figure-m17 |M17|39|69;74|58-82|
| main:figure-m16 |M16|37|65;68|51-80|
| main:figure-m15 |M15|39|59;59|45-74|
| main:figure-m14 |M14|38|58;58|44-72|
| main:figure-m13 |M13|39|54;67|35-80|
| main:figure-m12 |M12|34|50;59|31-73|
| main:figure-m11 |M11|36|46;44|29-64|
| main:figure-m10 |M10|34|41;44|24-59|
| main:figure-m9 |M9|40|40;43|23-58|
| main:figure-m8 |M8|38|35;42|18-58|
| main:figure-m7 |M7|36|33;31|18-48|
| main:figure-m6 |M6|36|29;33|15-49|
| main:figure-m5 |M5|39|24;26|12-45|
| main:figure-m4 |M4|35|20;20|10-35|
| main:figure-m3 |M3|33|20;18|9-35|
| main:figure-m2 |M2|40|16;13|6-30|
| main:figure-m1 |M1|36|15;14|6-28|
| main:figure-u9 |U9|35|24;34|20-51|
| main:figure-u8 |U8|37|24;22|7-40|
| main:figure-u7 |U7|36|19;19|8-31|
| main:figure-u6 |U6|30|17;17|6-30|
| main:figure-u5 |U5|38|15;18|7-30|
| main:figure-u4 |U4|36|14;14|5-28|
| main:figure-u3 |U3|33|14;18|6-31|
| main:figure-u2 |U2|38|10;11|3-24|
| main:figure-u1 |U1|35|3;3|1-10|

Each plotted mean sits between its own graphical whisker ends. Posterior versus observed values are separate quantities. No arm-level exact Figure2 effect estimate, P value, test statistic, standard error, person-time or survival quantity is printed. Follow-up totals are linked to Figure1 complete-case denominators667/318 by these cluster sizes; all27 mapped rather than selected.

## Adverse-event narrative, complete

[PDF p. 5, Adverse Events](../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5); percentages M vsU, refers eTable10. Main article gives no denominator/time per row here. All eleven pairs retained. Sentence following them says dry mouth,irritability,and anxiety more common M; this exact statement is a matching claim, without adjudication.

| Key | Event | M% | U% |
|---|---|---:|---:|
| main:ae-nausea |Nausea|23.0|22.3|
| main:ae-diarrhea |Diarrhea|7.5|7.5|
| main:ae-mouth |Dry mouth|62.7|55.7|
| main:ae-epigastric |Epigastric pain|27.7|40.4|
| main:ae-headache |Headache|45.1|49.1|
| main:ae-insomnia |Insomnia|35.3|33.5|
| main:ae-dreams |Abnormal dreams|10|13.2|
| main:ae-irritability |Irritability|40.5|43.4|
| main:ae-anxiety |Anxiety|33.3|36.8|
| main:ae-palpitations |Palpitations|31|28.4|
| main:ae-pain |Musculoskeletal pain|61.4|60.8|

## Context-only numerical material

Page2 introduction: >8.7million global deaths,230million DALYs,>$1.4trillion annually,>1.3billion tobacco users,>80% in low/middle income countries,approximately90% men,17%-32% TB patients currently smoke. These describe cited background and not trial results. Page8 cited background:14study review15%-82% abstinence; telecounseling study67.5% vs42%,RR1.60(95%CI1.19-2.16); general-population review13studies; psychosocial meta-analysis16RCTs. Limitations participant male>96%, country male smoking proportions97.8%/91.4%, CO validates24-48hours with half-life5-6hours, earlier trial3of4 abstinent at1year. These were inspected and preserved here as context rather than current-trial statistical relationships. Article dates/funding/author information and p.9 reference citation numbers are administrative/bibliographic material, with no additional current-trial quantitative relationship. No supplied main-paper person-time, rate denominator, test statistic or standard error is omitted: none is printed.

## Completeness statement

Nine of nine assigned direct-source pages mapped. Every displayed Table1 cell, all11 Table2 rows with every interval/ICC/effect column, all27 Figure2 cluster population/graphical relationships, every Figure1 count and reason, and all11 adverse-event pairs are retained. All matching main-paper abstract/Key Points/narrative claims, analysis populations, models, time points, endpoints, covariates, missingness and multiplicity descriptions were mapped. Zero scientific-coverage gaps. Checkers must resolve scientific inclusion independently and use the supplied PDF as final authority.

Additional Figure2 open-marker whisker mapping (approximate visual percentages, same source and limitations as above): M18 71-94;M17 58-83;M16 52-80;M15 43-74;M14 42-72;M13 52-77;M12 43-74;M11 27-62;M10 24-59;M9 27-58;M8 26-58;M7 16-49;M6 16-49;M5 11-45;M4 8-38;M3 7-36;M2 6-26;M1 6-29. U9 28-40;U8 9-38;U7 7-33;U6 6-33;U5 8-33;U4 5-26;U3 7-34;U2 3-26;U1 1-9. These are attached to the existing27 figure relationships, not additional relationships; numerical graphical approximations do not substitute for source recheck. Each open marker is within its graphical whisker ends.

Current-run source correction: independent C008 recheck and coordinator direct viewing of st1-main-006.png confirm the Table2 CO<6 PP usual-care numerator is39/318, while the printed percentage remains11.9%. The row transcription is corrected above. Initial mapper/checker parts remain preserved. Pass2 will independently apply the display-precision rule to this pair; no candidate selection follows from a transcription update alone.
