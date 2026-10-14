# Support PLAN mapping, shard 003

Scope: DOC-002, `joi250093supp1_prod_1768590553.08963.pdf`, PDF pages 65–96 inclusive (32 unique PDF_PAGE units). Document role: PLAN throughout, comprising the concluding pages of a protocol version, its v4-to-v6 change statement, and the SAP introduction through initial table templates. Status: COMPLETE. Mapped units: 32/32. Scientific coverage gaps: none.

Runtime agent: `01a12c3e-6be1-7ae3-bfde-811b576aabdb`; role support quantitative mapper; run model gpt-6.1-sol; reasoning effort medium. Read `QUALITY_CONTROL_SCOPE.md`, `workflow_1_6_2/review_contract.md`, current source coverage, evidence-asset inventory, and tooling record. This artifact maps source statements without diagnosing findings or assigning global relationship/candidate IDs.

Evidence method: every assigned page was visually read from the source-linked reusable JPEG `.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/page_images/page-NNN.jpg`, 180 dpi, historical rendering engine version unrecorded. Native/layout character extraction is not relied upon. The new approved GPU OCR `preprocessing/gpu_ocr/DOC-002/page-080.txt` was read as a supplemental locator; it omits entire sentences visible in the page image, including the total SMS count. Therefore the visual transcription below retains all visible statements. No fresh rendering or OCR was produced by this agent, and no source or reusable artifact was modified. Recheck must use the exact supplied PDF page as final authority. All links below target that PDF, using PDF page numbers rather than printed protocol/SAP page numbers.

## Per-page coverage

| PDF page | Printed page / source section | Mapped content | Coverage |
|---:|---|---|---|
| 65 | Protocol p24, lines1957–1998 | Phase3/4 power, decision rule, margin preservation; economic analyses and bootstrap | COMPLETE |
| 66 | Protocol p25, lines1999–2027 | Economic CI/missing-data sensitivity; Poisson mixed model, MAR, RR | COMPLETE |
| 67 | Protocol p26, lines2028–2066 | Translation, adverse-event reporting statement, governance | COMPLETE |
| 68 | Protocol p27, lines2067–2118 | Committee unblinding and collaborator responsibilities; no additional result-relevant analysis specification | COMPLETE |
| 69 | Protocol p28, lines2119–2156 | Database and ethics/consent administration; no additional result-relevant quantitative relationship | COMPLETE |
| 70 | Protocol p29, lines2157–2193 | Consent, staff, documentation, training and confidentiality; no result-relevant quantitative relationship | COMPLETE |
| 71 | Protocol p30, lines2194–2229 | Amendment procedure, data protection, deviation logging; no additional statistical design amendment itself | COMPLETE |
| 72 | Protocol p31, lines2230–2265 | Study termination and end-of-study definition; no numerical statistical stopping boundary | COMPLETE |
| 73 | Protocol p32, lines2266–2298 | Insurance, stakeholders and publication confidentiality; no result-relevant quantitative relationship | COMPLETE |
| 74 | Protocol p33, lines2299–2342 | Authorship and publication processes; no result-relevant quantitative relationship | COMPLETE |
| 75 | Protocol p34, lines2343–2381 | Publication ethics and bibliography; no new study design or outcome relationship | COMPLETE |
| 76 | Protocol p35, lines2382–2402 | Bibliography only; no new study design or outcome relationship | COMPLETE |
| 77 | Change statement p1, lines2403–2442 | v4-to-v6 endpoint, sample-size and intervention/substudy changes | COMPLETE |
| 78 | SAP opening, lines2443–2475 | SAP scope/version, adaptive four-phase design and comparisons | COMPLETE |
| 79 | SAP p2, lines2476–2511 | Intervention content, pilot N16 and two-country split | COMPLETE |
| 80 | SAP p3, lines2512–2547 | Embedded pilot, refinement pause, intervention SMS dose/frequency/duration | COMPLETE |
| 81 | SAP p4, lines2548–2581 | Phase4 face-to-face dose/timing; primary and secondary objectives | COMPLETE |
| 82 | SAP p5, lines2582–2617 | Randomization unit and allocation ratio; blinding; population | COMPLETE |
| 83 | SAP p6, lines2618–2648 | Population context table and complete sample-size assumptions | COMPLETE |
| 84 | SAP p7, lines2649–2684 | Margin preservation, primary endpoint/biochemical thresholds and secondary outcomes | COMPLETE |
| 85 | SAP p8, lines2685–2720 | TB outcome definitions, symptom/dependence scales and adverse-event window | COMPLETE |
| 86 | SAP p9, lines2721–2756 | Baseline variables, EQ-5D-5L, complete data-collection schedule | COMPLETE |
| 87 | SAP p10, lines2757–2761 | Otherwise blank continuation page with text 'on Schedule'; no quantitative content | COMPLETE |
| 88 | SAP p11, lines2762–2796 | Dataset time points, country structure and wide/long-form data organization | COMPLETE |
| 89 | SAP p12, lines2797–2832 | Data queries/cleaning and storage; no additional inferential specification | COMPLETE |
| 90 | SAP p13, lines2833–2867 | Interim analysis/progression rule and descriptive analysis | COMPLETE |
| 91 | SAP p14, lines2868–2903 | Primary model/effect measure, ITT/missing-data rule, TB and AE analyses | COMPLETE |
| 92 | SAP p15, lines2904–2939 | AE test rule, EQ-5D mixed model, adjustment, complete-case and subgroup analysis | COMPLETE |
| 93 | SAP p16, lines2940–2966 | Remaining subgroups, site model and RR, exploratory status, software | COMPLETE |
| 94 | SAP p17, lines2967–2977 | Planned sociodemographic/background table; values unpopulated | COMPLETE |
| 95 | SAP p18, lines2978–2990 | Tobacco-form and tobacco-days templates; values unpopulated | COMPLETE |
| 96 | SAP p19, lines2991–2999 | Continuation tobacco-use template and cessation-behavior template; values unpopulated | COMPLETE |

## Protocol continuation: sample size, power, decision rules and methods

[PDF p65](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=65), lines1958–1969: Phase3 A versus C has stated 90% power at 5% significance, comparing 16 clusters randomized to A with eight to C. Assumed six-month abstinence is 8% under usual care and 18% under mTB-Tobacco. Phase4 proceeds if A is superior to C. Phase4 has stated 90% power at a one-sided 2.5% level for noninferiority of mobile versus face-to-face support, 20 clusters per arm A and B, assumed face-to-face six-month abstinence 18%, margin8%. Natural cessation2% gives established treatment effect16% (=18%−2%); margin8% preserves at least50% (=8/16). The source states sample-size assumptions will be checked midway through recruitment and sample size adjusted accordingly. No quantitative adjustment or stopping boundary is printed on this page beyond these phase/power rules. Matching main-paper keys: Phase3 superiority, planned cluster allocation, assumed abstinence, significance/power and adaptive progression. The stated Phase4 assumptions belong to a separate planned phase.

[PDF p65](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=65), lines1970–1998, and [PDF p66](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=66), lines1999–2010: health-economic analysis accompanies both phases. Total participant cost combines intervention costs, wider healthcare use and out-of-pocket expenditure; country-specific unit tariffs multiply recorded quantities. Phase3 incremental comparison is mTB-Tobacco versus usual care. EQ-5D-5L supplies QALYs. ICER units are cost per QALY and cost per additional quitter; printed description calls quitting a secondary outcome for this analysis. The CEA time horizon is12months. Phase4 compares arm costs against a pre-defined acceptable cost difference, but no numerical cost difference is printed in this scope. Phase4 also estimates cost/QALY differences and ICER per QALY/additional quitter. Uncertainty: nonparametric bootstrap5,000replications;95%CIs; CEACs estimate cost-effectiveness probability across QALY thresholds. Complete-case sensitivity includes participants with complete costs and QALYs at all time points, follows the primary method, and assesses impact of imputation. Pattern-mixture sensitivity examines multiple-imputation assumptions. Matching keys: economic-outcome status and supplementary economic analyses if reported; no observed numerical ICER is supplied here.

[PDF p66](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=66), lines2011–2016, section28.2.2: outcomes are primarily analyzed in a missing-at-random architecture by generalized linear mixed models with log link and Poisson distribution. Clusters are random effects; all analyses account for clustering through a random-intercept model. Crude and adjusted RRs and corresponding95%CIs will be estimated. This paragraph does not specify the adjustment variables. Matching main-paper keys: primary analysis family/link, cluster handling, RR, CI and missingness assumption. Preserve this statement separately from the SAP logistic-model language below; these are different source locations with different printed descriptions.

[PDF p66](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=66), lines2018–2025: urine samples are collected at follow-up from smokers who also use other tobacco, including smokeless tobacco. A nicotine dipstick result is recorded, sample discarded, no storage/shipment. Text says sample analysis is not critical to trial conduct and not related to tertiary/exploratory endpoint data/objectives. Matching keys: biochemical verification in concomitant tobacco users. No cotinine threshold is specified in this paragraph.

[PDF p67](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=67), lines2038–2043: intervention is behavioral; CO measurement and quantitative collection have minimal risk; the protocol states 'no adverse events will be reported to the sponsor for this study.' This is a sponsor-reporting statement; it does not itself specify whether events are collected as trial outcomes. The same page and [p68](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=68), lines2062–2071, describe an independent steering/monitoring committee including a statistician, at least a chair and two other independent members, which can see unblinded data and reviews serious treatment-related unexpected events. No numerical monitoring boundary is printed. These contextual statements are preserved for interpreting the SAP AE-outcome text.

[PDF p71](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=71), lines2206–2227: amendment policy requires Chief Investigator approval and sponsor/ethics authorization before enrollment under an amended protocol, excluding immediate-hazard measures. This is a general amendment policy, not an endpoint-specific amendment record. [PDF p72](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=72), lines2241–2262: end of study is last participant's last visit; investigators or sponsor may terminate for clinical/administrative reasons. Interventions do not continue beyond trial. No numerical statistical stopping boundary is supplied in this administrative section.

## Explicit v4-to-v6 change statement

[PDF p77](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=77), lines2403–2442, titled 'Changes between version v4 and v6':

| Element | Printed change | Matching key |
|---|---|---|
| Treatment-failure secondary endpoint | Text 'remained smear-positive at month5' replaced by 'remained smear positive at month6' in v6, cited printed protocol p6 | Secondary TB failure definition/window |
| Phase3 sample size | 888participants,16intervention+8usual-care clusters in v4 →1080participants,18intervention+9usual-care clusters in v6 | Superiority target N and cluster allocation |
| Phase4 sample size | 1480participants in40clusters →1620participants in36clusters in v6 | Noninferiority sample assumptions; separate phase |
| Combined phases and flow | Combined sample size, flow Diagram1 and entire sample-size section updated in v6 | Version context for numeric design comparisons |
| Technology Acceptance Model substudy | Phase3: random selection of20% of mTB-Tobacco participants in each country at trial end; Phase4: all mTB-Tobacco participants complete TAM | Outcome/substudy population and status |
| Education leaflets | Added to both intervention and usual care; Phase3 intervention receives leaflets in addition to mHealth package | Randomized intervention/control content |
| Weekly calls | Research assistants call participants weekly, ask whether SMS received and remind follow-up visits | Intervention exposure and follow-up support |
| Ethics references/travel allowance | Ethics numbers added; travel allowance revised and paid at two follow-ups | Administrative context, no inferential relation |

The statement expressly identifies Phase3 superiority as the trial reported here and Phase4 noninferiority as not reported here. It supplies disclosed amendment context; the mapper does not infer amendment chronology beyond this printed statement.

## SAP scope, study design and randomized intervention

[PDF p78](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=78), lines2447–2472: SAP covers trial progress and effectiveness outcomes, explicitly excludes cost-effectiveness and process evaluation described elsewhere. It cites trial protocol version6.0 dated20.Mar.2025 and the supplied package's cited protocol paper. Design is adaptive, multicenter, cluster randomized, controlled, four phases:1PPI;2pilot feasibility of intervention/database;3superiority,12months total with6months recruitment+6months follow-up, mTB-Tobacco A versus usual care;4noninferiority, another12months with6months recruitment+6months follow-up, A versus face-to-face B. Matching main-paper key: trial phase/comparison/follow-up and protocol/SAP version disclosure.

[PDF p79](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=79), lines2476–2511: SMS has tobacco-quitting behavior content plus motivational/informative TB-treatment support. PPI6–8members in each country reviews materials. Pilot total16patients, eight Bangladesh and eight Pakistan. Users' reported experience and real-time engagement form two evaluation data sets. [PDF p80](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=80), lines2512–2536: pilot is embedded in Phase3; data receive main-trial governance. A refinement/study pause follows pilot before continuing superiority phase. Program comprises Bangla/Urdu SMS, transmission schedule, automated platform and monitoring team. Every intervention participant receives134SMS over6months. First month frequency3–4messages/day; next month1message/day; last four months1message/month. These are the printed schedule statements, without reconstructing an unprinted day count. Control receives no SMS (lines2545–2547). New GPU OCR p80 omits the line containing134; visual source-linked image plainly includes it. Matching keys: SMS dose, frequency, duration and pilot inclusion.

[PDF p81](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=81), lines2559–2572: Phase4 adapted face-to-face program has two sessions on day0 and day5(+2), lasting10 and5minutes respectively; quit date five days after day0; optional further support at week5. Education leaflets given to patients allocated to the respective arm. Primary objective is mTB-Tobacco effectiveness/cost-effectiveness for continuous abstinence of minimum6months in people with TB and daily smoking. Secondary objectives cover TB-treatment adherence (p81) and clinical TB progression, severity, treatment response (p82 lines2582–2584). Matching keys: intervention content/time and endpoint-objective hierarchy.

[PDF p82](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=82), lines2586–2610: interventions administered at health-facility group level. Facilities allocated2:2:1 to A(mTB-Tobacco),B(face-to-face),control. Independent Edinburgh statistician uses computer-generated random lists. Participants and investigators/research teams know allocation; statistician assigning clusters has no knowledge of participating facilities; steps planned to blind data analyst. Matching keys: randomization unit/ratio, clustering and blinded analysis. Do not substitute the three-arm overall allocation for the Phase3 two-arm comparison.

## SAP sample-size and power assumptions

[PDF p82](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=82), lines2611–2617, and [p83](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=83), lines2618–2620: target settings are Bangladesh/Pakistan public-sector TB facilities in Dhaka division/Punjab province. The contextual table lists Bangladesh221TB cases/100,000;357,000cases;47,000deaths;35%tobacco prevalence; Pakistan265/100,000;562,000cases;44,000deaths;20%prevalence. These are background populations, not randomized or analysis denominators.

[PDF p83](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=83), lines2623–2648, and [p84](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=84), lines2649–2651:

| Assumption or derived design quantity | SAP printed specification |
|---|---|
| Combined target | 2700smokers newly diagnosed pulmonary TB, approximately43recruits from63TB-center clusters |
| Missing primary outcome | 20%may not provide primary outcome data |
| Pilot inclusion | First16pilot participants included; may not use their data if intervention needed major refinement |
| Phase3 power/alpha | 90%power,5%significance |
| Phase3 expected six-month abstinence | 18%mTB-Tobacco,8%normal treatment |
| Phase3 clusters/ratio | 27TBcenters,2:1intervention:control |
| Phase3 pre-cluster size | 'After considering a20%attrition rate',704participants, around26individuals per cluster |
| Phase3 ICC/design effect | ICC0.02; design effect1.50 |
| Phase3 resulting target | Around1080people,40subjects/site |
| Phase4 power/alpha | 90%power,one-sided hypothesis,2.5%significance |
| Phase4 clusters |18clusters per treatment arm |
| Phase4 comparator/margin | Face-to-face18%abstinence at6months; noninferiority margin8% |
| Natural cessation and retained effect |2%natural;16%effect=18%−2%;8%margin preserves≥50%=8/16 |
| Phase4 ICC/design effect/target | ICC0.02;design effect1.50;around1620people,45subjects/site |

No cluster-size coefficient of variation is stated in these assigned SAP pages. No explicit sample-size equation or software calculation is printed here. Record quantities as separate inputs and printed derived values for quantitative review; do not treat 'effective sample size' in the text as a new independently observed trial denominator. Matching main-paper keys: planned superiority N/cluster totals, power, expected rates, attrition, ICC and inflation.

## SAP outcome hierarchy, definitions and collection schedule

[PDF p84](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=84), lines2653–2669: primary endpoint biochemically verified continuous abstinence6months postrandomization. Self-report no more than five cigarettes, bidis or water-pipe sessions since quit date; verification breathCO<10ppm at month6. Concomitant smokeless tobacco: urine cotinine strip scale0–6;level<3, described as equivalent to100–200ng/mLcotinine, counts as abstinence. Self-reported abstinence withCO>10ppm and cotinine indicating active use is superseded by biochemical evidence and classified tobacco use. Preserve both printed strict CO inequalities; boundary behavior at exactly10ppm is not supplied in these sentences. Matching main-paper keys: primary endpoint definition, six-month window, biochemical threshold, allowed lapses and concomitant-tobacco rule.

[PDF p84](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=84), lines2671–2684, and [p85](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=85), lines2685–2702: secondary section lists TB-treatment adherence from Treatment Support Card medication logs and TB-program outcomes fromTB03register at month6. Treatment-success composite includes cured+completed treatment. Cured: initially smear-positive, smear-negative at last treatment month(month6) and at least one prior occasion. Completed: completed at month6 without cure criteria. Treatment failure: initially smear-positive, remaining smear-positive at month5 or later during treatment (lines2685–2686). Default: treatment interrupted≥2consecutive months. Died: any cause during treatment. Relapse: previously cured/completed, now recurrent TB, true relapse or reinfection. Further listed TB outcomes: clinical TB score, sputum conversion, adherence, and success/failure/default/relapse/death. Clinical team supports symptom/sign assessment; routine cards/registers supply other outcomes. Matching keys: secondary/clinical outcome hierarchy, successful/unsuccessful composites and components, failure/default/death/relapse windows.

[PDF p85](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=85), lines2703–2720: nicotine-dependency section has MPSS, five domains(depression,irritability,restlessness,hunger,poor concentration), described5point scale and total5–35;higher=worse withdrawal. SUTS two questions, resulting score0(no urges)–5(extremely strong). AE section says collected up to week9, self-reported checklist: nausea,diarrhea,dry mouth,epigastric pain,headache,insomnia,abnormal dreams,irritability/moodiness,anxiety,tachycardia/palpitations,musculoskeletal pain. Matching keys: secondary/safety collection status, scale and event window; no observed event counts supplied.

[PDF p86](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=86), lines2722–2734: baseline variables age,gender,marital status,education,occupation,tobacco-use form,quit history,site/country. EQ-5D-5L five quality-of-life dimensions(mobility,self-care,usual activities,pain/discomfort,anxiety/depression); weighted population-referenced index, health-economic analysis. Complete Table1 schedule on this page:

| Assessment | Screening | Baseline | Week9 | Month6 |
|---|---|---|---|---|
| Eligibility;written consent | x | — | — | — |
| Sociodemographics;tobacco-use/quit history | — | x | — | — |
| Self-reported tobacco use/abstinence;CO/cotinine | — | — | — | x |
| MPSS;nicotine dependency(SUTS,HTUI) | — | x | — | x |
| Clinical TB score,symptoms,signs | — | x | x | x |
| Economic evaluation;EQ-5D-5L | — | x | — | x |
| TB adherence;sputum microscopy | — | — | x | x |
| Adverse-event review | — | — | x | x |
| m-TB usage(SMS) | — | — | x | — |

'—' means no printed check mark. Table shows AE review at month6 as well as week9; adjacent narrative collection window is retained separately. No assessment threshold is inferred from these marks. [PDF p87](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=87) contains only the continuation fragment 'on Schedule' and line numbers, with no further rows.

## SAP data organization, interim analysis and descriptive statistics

[PDF p88](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=88), lines2775–2791: baseline,follow-up1week9 andfollow-up2month6 eCRFs are separated by country; screening/change-in-status shared across countries. Cleaned data appended; wide-format master joins periods; long-format master for selected multivariate analyses has three times(baseline,week9,month6). Label/data-matrix navigation planned. These are data-structure statements, not supplied participant-level datasets or workbook cached values. Pages88–89 otherwise document consent, queries and storage without a primary analysis rule.

[PDF p90](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=90), lines2848–2854: at end of Phase3 superiority an independent statistician performs interim analysis of mTB-Tobacco effectiveness; result decides progression to Phase4 noninferiority or early termination. No statistical boundary, alpha-spending scheme, multiplicity correction or threshold beyond the protocol progression statement is printed in these assigned SAP pages.

[PDF p90](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=90), lines2855–2866: descriptive continuous summaries mean(SD) or median(IQR) according to distribution; categorical frequency/percent. EDA precedes formal analysis, investigates distributions, missingness and outliers; normality by histograms,Q–Qplots,skewness,kurtosis, guiding tests/models. [PDF p91](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=91), lines2868–2876: CONSORT flow; exclusion reason frequencies/percent by arm; baseline total and by arm for all randomized participants. Matching keys: analysis-population denominator/flow and Table1 descriptive statistics.

## SAP primary, sensitivity, secondary and subgroup analyses

[PDF p91](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=91), lines2878–2892, primary analysis:

- Primary biochemically verified continuous abstinence6months postrandomization; agreement of self-report/biochemical verification by arm; both abstinent count and proportion per arm for self-reported and verified outcome.
- Complete-case statistical analysis supplies risk difference and relative risk with95%CIs.
- Mixed-effects logistic regression treats site as random effect; treatment effect expressed asRR with95%CI andPvalue. No transformation from logistic coefficients toRR is specified on this page.
- Primary population intention-to-treat. Dropout or incomplete data regarded as continuing smokers under Russell Standard methodology.

Matching keys: primary RR/RD/CI/P, model family, site random intercept, ITT denominator and missing-outcome classification. Preserve complete-case and ITT statements as source text, without deciding their correspondence to a reported model.

[PDF p91](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=91), lines2894–2903, and [p92](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=92), lines2904–2906: TB score,sputum conversion,adherence,program outcomes use appropriate descriptive/inferential models for continuous/categorical data at all available time points. AE comparison uses chi-square; number with anyAE/seriousAE compared if at least10patients have≥1event; low-frequency events use exact test. Frequencies/percent also reported. This is a prespecified AE analysis, with no event count populated in the plan.

[PDF p92](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=92), lines2907–2915: EQ-5D-5L explicitly called a secondary outcome. Total-score basis is printed as a dotted placeholder. Baseline and6month total scores use mixed-effects model with site random effect; fixed effects treatment,time,treatment×time. Estimated marginal means/intergroup differences,95%CIs,Pvalues. Matching keys: outcome status, index/scale,time and repeated-measures model if reported.

[PDF p92](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=92), lines2917–2935: sensitivity heading includes adjusted mixed-effects logistic model with site random effect. Fully adjusted controls sociodemographic variables,tobacco form,other baseline characteristics(e.g.education,smoking duration). Effects RR+95%CIs. Categorical variables factors;continuous effects per unit. Missing-data sensitivity repeats primary logistic model in available-outcome patients, excludes missing outcomes;self-reported/COverified abstinent count/proportion per arm;coefficient with95%CI/Pvalue. Matching keys: reported adjusted covariates,complete-case sensitivity,model/effect identity. No exact finite adjustment list is printed beyond examples and broad categories here.

[PDF p92](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=92), lines2936–2939, and [p93](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=93), lines2940–2952: subgroup sensitivity evaluates stability of primary effect by age<40vs≥40years;education none/primary/more-than-primary;occupation active employment/business vsdependents/retired;gender male/female;smoking duration<24vs≥24years. Each subgroup has separate mixed-effects model with site random intercept,RR and95%CI. Consistency assessed qualitatively across RRs/CIs;missing CIs disclosed;limited power and exploratory nature noted. No treatment-interaction test is specified in this subsection. Matching keys: prespecified subgroup list,cuts,categories,statistical comparison.

[PDF p93](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=93), lines2953–2963: additional exploratory subgroup/sensitivity/posthoc analyses may arise from research team/protocol changes or emerging questions, justified and separately documented/reported from original primary/secondary analyses. Software open-sourceR andJASP0.19.3(JASPTeam2024). NoSAP signature/date appears on this assigned software page.

## Initial planned table templates

[PDF p94](../../../../joi250093supp1_prod_1768590553.08963.pdf#page=94), lines2967–2972: selected tables/figures are templates; final displays may differ in some details. All numerical outcome cells in assigned templates pp94–96 are blank, with no cached/formula values or observed effects to extract.

| PDF page | Template | Complete displayed keys/statistical columns |
|---:|---|---|
| 94 | Sociodemographic & Background | Variable,Level,m-Health,Control,χ²,Pvalue. Gender male/female;education noformal/primary/middle/secondary/higher;marital single/married/separated-divorced-widowed;occupation activejob-business/dependents/retired;TBstage1/2/3;readingSMSyes/no;ageMean(SD);BMIMedian(IQR). |
| 95 | Tobacco Use and Quit History | Smoking form cigarette,bidi,hookah,electronic cigarette,smokeless products,other. Response,m-Healthn(%),Controln(%),χ²,Pvalue. Response cells unfilled. |
| 95 | Tobacco Use | Variable,Types,Group,n,Median(IQR),Mean(SD),Zvalue superscripta,Pvalue. Tobacco-use days,cigarettes,m-Health/control starts here. Superscripta explanation is not printed on this page. |
| 96 | Tobacco Use continuation | Days:bidi,hookah,smokeless tobacco;daily tobacco-use average number:cigarette,bidi,hookah,smokeless tobacco;each m-Health/control. All summary/test cells blank. |
| 96 | Smoking Behavior and Cessation Attempts | Variable,Response,m-Healthn(%),Controln(%),χ²/t/z,Pvalue;first row smokinginsidehome superscripta. Three blank response rows;footnote definition absent on this assigned page. |

Matching keys: main/supplement baseline,tobacco form and smoking-behavior displays. Templates supply planned labels/tests without numerical results. Continuations outside pp65–96 belong to the next disjoint shard and are not inferred here.

## Handoff completeness and limitations

All32assigned pages inspected;32mapped;no unit skipped;no scientific gap. Source text is transcribed from readable rendered locators, not recovered from garbled native text. Approved new GPU OCRp80 is a partial transcription aid and does not replace the visual134SMS statement. NoOffice/workbook/CSV source is within this shard, so formulas,cached workbook values and record-group extraction are not applicable. No observed inferential results are supplied in these PLAN pages; all numerical values above are design assumptions,definition thresholds,assessment schedules,scale descriptions or contextual background. Global numeric/statistical relationship IDs and checker inclusion decisions remain coordinator/checker responsibilities.
