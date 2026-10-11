# Support quantitative evidence — REPORT units

Assigned scope: DOC-004 physical PDF pages 1–7; DOC-005 physical PDF pages 1–19; DOC-006 sole worksheet eTable 3, A1:J115. These 27 units are disjoint from the main article, protocol and SAP mapper scopes. All three sources are REPORT by content. This is a fresh mapping from source-linked derivatives, not a candidate assessment. No prior scientific conclusions were used.

## Engines and evidence provenance

Retained doc004.layout.txt/doc004.native.txt and doc005.layout.txt/doc005.native.txt: legacy direct Poppler pdftotext native/layout; curator established current-source native identity byte-for-byte. Retained results page images pages 3, 8, 10 and 17 were visually inspected; legacy CPU rendering, exact engine version unconfirmed. Workbook JSON and Markdown: legacy permitted Office structure extractor; curator mechanically matched all 525 nonempty exact cells to current XML. Formulas are not recalculated. Direct unzip of current sheet1.xml confirms zero formula elements.

Fresh unit DOC-005 p12: direct Poppler pdftotext 26.01.0 native and layout, CPU, commands pdftotext -f 12 -l 12 SOURCE preprocessing/support_mapper/results-p012.native.txt and pdftotext -layout -f 12 -l 12 SOURCE preprocessing/support_mapper/results-p012.layout.txt. Existing fresh curator render preprocessing/curator/results-p012.png visually inspected, confirming footer only; no repeated rendering. Supplement model equations pp4–5 visually inspected using new pdftoppm 26.01.0 CPU renders: pdftoppm -f 4 -l 5 -scale-to 1800 -png SOURCE preprocessing/support_mapper/results; outputs results-04.png and results-05.png. No OCR was necessary. Assembly script only copies exact text and cells into this evidence artifact; scientific mapping is the agent-authored inventory below.

## Relationship inventory and matching keys

Local IDs are R001–R025. Each table family includes EVERY row and EVERY printed statistic in the exact page transcript following this inventory. Individual table rows are addressed by their printed row label, time and contrast, or workbook exact cells. No table row is selected or suppressed. Main-paper keys describe matching concepts, not an uninspected main-paper value.

| Key | Exact support scope | Complete relationship and matching main-paper key |
|---|---|---|
| R001 | DOC-004 pp2–4 | Three arms: Usual Care Plus resource guide; painTRAINER eight sequential self-completed online CBT sessions, 30–45 minutes; Health Coach eight one-on-one sessions, 45–60 minutes. 12-week completion period. Main key: intervention dose, duration and delivery. |
| R002 | DOC-004 pp2–3 | Health Coach resource materials: four recordings 5–20 minutes; two 5-minute videos. 12 coaches, two sites, weekly hour-long supervision; approximately 34 hours coursework, 90-minute overview; at least16 real sessions (two instances for each of eight sessions) to proficiency. Staff approximately9 training hours (1+3+1+2+2). Main key: intervention administration. |
| R003 | DOC-004 pp3–6 | Proficiency: 100% session-content fidelity, 80% core CBT fidelity across nine relevant domains. First12 months 5% sample; month13+ one session per coach per6 months. Actual299/4626 (6.5%), split193 training,89/1791 (5%) first12 months,17/2350 later. Content below100% in8/299 (2.7%); CBT below80% in11/299 (3.7%). Main key: fidelity denominators. |
| R004 | DOC-004 pp4–5 | PT onboarding approximately15 minutes; HC approximately10; HC four-week extension n14. PT outreach trigger >7 days uninitiated/incomplete, >10 days since completion, or ≥3 sessions in9 days.356/776 (45.9%) with≥1 call; mean1.8 calls range1–7, mean4 minutes. Full12-month PT access. Main key: adherence and intervention extension. |
| R005 | DOC-004 p5; DOC-005 pp13–14 | TIDieR change8/9/2021 after approximately140 enrolled; results narrative says after454; eTable8 restriction before/after8/9/2021 and after3/31/2022. All printed statements retained with their local populations. Main key: modification and subset-analysis definitions. |
| R006 | DOC-005 p2 | Every outcome scale definition: BPI severity mean11 items; intensity mean4; interference mean7; all0–10, higher worse. MCID≥30% reduction from baseline. PHQ8 sum0–24, thresholds10/15/20; GAD7 sum0–21, thresholds5/10/15. PROMIS sleep6 items, social4, physical6, each1–5, T-score50 SD10; sleep higher worse, social/physical higher better. Sleep≥60 moderate60–70/severe>70; social/physical≤40 moderate40–30/severe<30. Main key: outcome definitions and direction. |
| R007 | DOC-005 p3 | eFigure1 all two panels, horizontal sessions0–8 (ticks0,2,4,6,8), vertical arm proportions0–1 (ticks0,.2,.4,.6,.8,1). PT and Virtual Coach arm labels. Bars have no printed counts or numerical heights. Visual endpoints PT approximately.38 at zero and at full completion; VC approximately.18 at zero and.63 at full completion. These are visual approximations, not extracted counts. All eight completion bins are displayed in each panel. Main key: completion/adherence histogram. |
| R008 | DOC-005 pp4–5 | Reported prespecified MNAR trigger primary3-month missingness>15% or differential missingness; completeness77.1% overall,79.9 UC,69.8 PT,81.6 HC; all3 observed67.3%, none12.7. Three observed-pattern categories1/2/3, percentages8.1/12.1/67.3 of randomized population. Main key: primary missing-data decision. |
| R009 | DOC-005 pp4–5,7; DOC-006 H2:J114 | Covariate selection: separate logistic missingness and modified-Poisson3-month MCID models, add covariate when P<.10 in both with base adjustment. Base arm,baseline severity,age,sex,site,rural/underserved,multisite pain,mental health. Imputation/estimation extras education and unemployment; weight extras PEG,PHQ8,GAD7,any negative SDOH,education. Entire tested-variable catalogue retained p7; workbook selection P values have distinct outcome/nonresponse/3-month missingness columns. Main key: adjustment and predictor-selection specification. |
| R010 | DOC-005 pp4–5 | Imputation step1 conditional linear mean of change, identity link, treatment/time interactions, observed-pattern terms and treatment/pattern interactions. GEE independent working correlation, robust standard errors, health-coach and person clustering. Missing change replaced by predicted values; binary MCID calculated from change and baseline severity. Baseline missing covariates replaced by population means. Main key: primary imputation model. |
| R011 | DOC-005 p5 | Step2 log mean for binary MCID, arm+baseline covariates+6/12-month indicators+arm/time interactions; modified Poisson GEE robust sandwich provider/person clustering; coefficients from second-step solution and joint imputation/analysis covariance attributed to supplied reference2. Main key: primary estimation model and RR. |
| R012 | DOC-005 pp5–6 | Logistic nonresponse model for any observed follow-up among entire randomized cohort; arm,base covariates and selected additional variables; prediction pi, inverse weight1/pi scaled to sample size. None-follow-up fractions12.7% overall,9.5 UC,17.1 PT,11.3 HC; estimand ATE for all randomized. Main key: weighting model and analysis population. |
| R013 | DOC-005 p7 | eTable1 complete count/percent matrix all randomized, follow-ups3/6/12 months,at least1,none,exactly1/exactly2/exactly3 observed; every overall/UC/PT/HC cell retained. Main key: participant-flow and primary-outcome analysis counts. |
| R014 | DOC-005 p8 | eTable3 full28 coefficient rows with estimate,95% CI,P, including intercept,arm,time,pattern,all interactions,sex,age,sites,residence,pain conditions,mental health,severity,education,employment.6108 observations,2036 people,659 missing values. Duplicate printed education row labels preserved. Main key: imputation fit coefficients and test/interval pairs. |
| R015 | DOC-005 p9 | eTable4 full23 RR/CI/P rows, including all arm contrasts at3/6/12 months and adjustment terms; repeated HC/PT3M row preserved.6108 observations,2036 persons,sum weights6108. Main key: primary binary outcome RRs and adjustment-model fit. |
| R016 | DOC-005 p10 | eTable5 full16 logistic OR/95%CI/P rows plus c-statistic.679; reference PT for treatment rows. Site identity withheld; every printed row retained. Main key: nonresponse model. |
| R017 | DOC-005 p10 | eTable6 complete probability/weight summary, sum/mean/SD/min/P25/P50/P75/max; probability .88/.07/.50/.85/.90/.93/.98; weights sum2036,1.00/.09/.89/.94/.97/1.03/1.75. Main key: weight normalization and distribution. |
| R018 | DOC-005 p10 | eFigure2 complete two panels: estimated probability vs percent and weight vs percent; green at least1 follow-up,orange none,solid/dashed smooth curves. Printed probability ticks .6/.8/1.0;percent0/5/10/15/20; weight1/1.5/2,percent10/20/30/40. No individual bar labels or exact bin counts printed. Main key: estimated weight diagnostics. |
| R019 | DOC-005 p11 | eTable7 six rows: complete-case3/6/12 and worst/best3/6/12. Each row contains PT/HC/UC adjusted% with95%CI,three RR contrasts with95%CI,omnibusP,and three NNTs with95%CI. Complete-case3month N1798 UC621 PT542 HC635; worst/best N2331 UC777 PT776 HC778. Missing intervention outcomes0 and UC1 in worst/best. Main key: missing-data sensitivity binary primary outcome. |
| R020 | DOC-005 pp11,14 | Shared inferential definitions: modified Poisson GEE; adjusted population means at mean covariate distribution; sex,age,site,residency,multiple pain,mental-health,severity adjustment. Wald omnibus test any three-arm difference; pairwise only if omnibusP<.05 following least significant difference. NNT reciprocal adjusted improvement-probability difference. If RD CI spans0, positive lower NNT to infinity and negative upper NNH to negative infinity, printed endpoint pairs retained. Main key: RR/omnibus/NNT interpretation. |
| R021 | DOC-005 pp13–14 | eTable8 all nine rows across three subset blocks. Before8/9/2021 N454,any-follow-up366,printed3month PT149 HC153 UC152;after8/9/2021 N1877,any1670,3month UC512 PT448 HC527;after3/31/2022 N1038,any935,3month UC296 PT262 HC300. Each block3/6/12 months,all proportions/RRs/P/NNTs retained. Enhancement described prespecified; letter analysis post-hoc,reported follow-up82.7% at3month and90.1% any. Main key: intervention enhancement sensitivity. |
| R022 | DOC-005 p15 | eTable9 all nine outcome/time rows (severity,intensity,interference ×3/6/12); every PT/HC/UC numerator/denominator/percent and three RR/CI pairs. Narrative no adjustment,weighting,imputation; caption prints adjusted RR while footnote specifies modified-Poisson GEE without adjustment. Main key: main Table2 binary outcomes in unadjusted analysis. |
| R023 | DOC-005 p16 | eTable10 all15 rows (severity,intensity,interference,social,physical ×3/6/12); every printed group change median/IQR and three unadjusted between-group mean differences95%CI with omnibusP. Linear GEE specified. Main key: main Table3 continuous change outcomes. |
| R024 | DOC-005 pp17–18 | eTable11 all21 rows (above5 outcomes plus global-change pain/general ×3/6/12); each printed group raw-score median/IQR,three unadjusted mean differences95%CI,omnibusP. Column order PT,HC,UC visually confirmed; printed intervals and labels retained exactly without relabeling as means/CI. Main key: main Table3 continuous raw-score analysis. |
| R025 | DOC-006 eTable3 A1:J115 | Entire525 nonempty-cell table: overall2331,all-missing295,missing1/2468,all-observed1568; all demographic/clinical/pain/baseline outcome blocks,categorical counts/percentages,means/SD,missing denominators,prespecified marks,selectionP,and footnotes. Denominator excludes characteristic-specific missingness perA110. A114 defines bold selection P<.10 for both outcome and missingness after adjustment. Zero formulas; numeric entries are literal stored values; strings contain displayed values. Main key: baseline data by primary follow-up pattern and selection variables. |

## Visually transcribed model equations

Direct pp4–5 render avoids duplicated mathematical glyphs in native text. Let I denote an indicator; X group, m follow-up month, Z baseline covariates, Obs number of observed follow-ups. Printed prose enumerates X as UC,PT,UC; the equation itself contains PT and HC indicators with UC baseline. This records the printed notation without a candidate assessment.

Imputation equation p4: E(Y_im|X_i,Z_i)=alpha+beta_PT I(X_i=PT)+beta_HC I(X_i=HC)+beta_Z Z_i+beta_6 I(m=6)+beta_12 I(m=12)+gamma_PT,6 I(X_i=PT)I(m=6)+gamma_PT,12 I(X_i=PT)I(m=12)+gamma_HC,6 I(X_i=HC)I(m=6)+gamma_HC,12 I(X_i=HC)I(m=12)+eta_1 I(Obs_i=1)+eta_2 I(Obs_i=2)+eta_PT,1 I(X_i=PT)I(Obs_i=1)+eta_HC,1 I(X_i=HC)I(Obs_i=1)+eta_PT,2 I(X_i=PT)I(Obs_i=2)+eta_HC,2 I(X_i=HC)I(Obs_i=2).

Estimation equation p5: log(E(Yhat_im|X_i,Z_i))=alpha+beta_PT I(X_i=PT)+beta_HC I(X_i=HC)+beta_Z Z_i+beta_6 I(m=6)+beta_12 I(m=12)+gamma_PT,6 I(X_i=PT)I(m=6)+gamma_PT,12 I(X_i=PT)I(m=12)+gamma_HC,6 I(X_i=HC)I(m=6)+gamma_HC,12 I(X_i=HC)I(m=12).

Nonresponse equation p5: logit(E(R_i|X_i,Z_i))=beta_0+beta_PT I(X_i=PT)+beta_HC I(X_i=HC)+beta_Z Z_i. Raw weight w_i=1/p_i, then scaled. R_i indicates at least one observed follow-up.

## Complete unit coverage

| Source | Unit | Asset basis | Mapped content | Status |
|---|---|---|---|---|
| DOC-004 | PDF page 1 | REUSABLE layout | Cover; no applicable numeric result | COMPLETE |
| DOC-004 | PDF page 2 | REUSABLE layout | R001–R002 materials and intervention | COMPLETE |
| DOC-004 | PDF page 3 | REUSABLE layout | R001–R003 provider/training/dose | COMPLETE |
| DOC-004 | PDF page 4 | REUSABLE layout | R001–R004 schedule/outreach | COMPLETE |
| DOC-004 | PDF page 5 | REUSABLE layout | R003–R005 modification and fidelity | COMPLETE |
| DOC-004 | PDF page 6 | REUSABLE layout | R003 actual fidelity | COMPLETE |
| DOC-004 | PDF page 7 | REUSABLE layout | References; no applicable trial numeric result | COMPLETE |
| DOC-005 | PDF page 1 | REUSABLE layout | Cover and full contents; no applicable result | COMPLETE |
| DOC-005 | PDF page 2 | REUSABLE layout | R006 outcome measures | COMPLETE |
| DOC-005 | PDF page 3 | REUSABLE layout and visual image | R007 complete adherence figure | COMPLETE |
| DOC-005 | PDF page 4 | REUSABLE layout | R008–R010 missingness and imputation | COMPLETE |
| DOC-005 | PDF page 5 | REUSABLE layout | R009–R012 models and weights | COMPLETE |
| DOC-005 | PDF page 6 | REUSABLE layout | R012 weighting continuation | COMPLETE |
| DOC-005 | PDF page 7 | REUSABLE layout | R009,R013 complete eTables1–2 | COMPLETE |
| DOC-005 | PDF page 8 | REUSABLE layout and visual image | R014 complete eTable3 | COMPLETE |
| DOC-005 | PDF page 9 | REUSABLE layout | R015 complete eTable4 | COMPLETE |
| DOC-005 | PDF page 10 | REUSABLE layout and visual image | R016–R018 complete eTables5–6/eFigure2 | COMPLETE |
| DOC-005 | PDF page 11 | REUSABLE layout | R019–R020 complete eTable7 | COMPLETE |
| DOC-005 | PDF page 12 | FRESH pdftotext and curator image | Footer-only; visually confirmed no applicable content | COMPLETE |
| DOC-005 | PDF page 13 | REUSABLE layout | R005,R021 subset definitions | COMPLETE |
| DOC-005 | PDF page 14 | REUSABLE layout | R020–R021 complete eTable8 | COMPLETE |
| DOC-005 | PDF page 15 | REUSABLE layout | R022 complete eTable9 | COMPLETE |
| DOC-005 | PDF page 16 | REUSABLE layout | R023 complete eTable10 | COMPLETE |
| DOC-005 | PDF page 17 | REUSABLE layout and visual image | R024 complete eTable11 | COMPLETE |
| DOC-005 | PDF page 18 | REUSABLE layout | R024 eTable11 footnote continuation | COMPLETE |
| DOC-005 | PDF page 19 | REUSABLE layout | References; no applicable trial numeric result | COMPLETE |
| DOC-006 | eTable 3 A1:J115 | REUSABLE exact-cell JSON, current XML identity and formula check | R025 all525 nonempty cells; blank cells and row115 contain no result | COMPLETE |

## Complete page transcription

All source pages follow, including administrative and reference pages. Every table is retained in full layout with the original column header, row ordering and footnotes. Native equation glyph duplication is retained in the transcription as provenance; the visually transcribed equations above provide readable symbols.

### DOC-004 physical PDF page 1

Source: [DOC-004 p1](../../../../joi250046supp3_prod_1755300121.15087.pdf#page=1). Mapped: Cover; no applicable numeric result.

```text
Supplementary Online Content

DeBar LL, Mayhew M, Wellman RD, et al. Telehealth and online cognitive behavioral therapy–
based treatments for high-impact chronic pain: a randomized clinical trial. JAMA. Published online
July 28, 2025. doi:10.1001/jama.2025.11178

RESOLVE Study Description of Interventions based on Template for Intervention Description
and Replication (TIDieR)


This supplementary material has been provided by the authors to give readers additional information
about their work




© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.
```

### DOC-004 physical PDF page 2

Source: [DOC-004 p2](../../../../joi250046supp3_prod_1755300121.15087.pdf#page=2). Mapped: R001–R002 materials and intervention.

```text
RESOLVE Study Description of Interventions Based on Template for Intervention Description and Replication (TIDieR)


                                Usual Care Plus                                     painTRAINER                                           Health Coach
WHY                Goal: To allow participants to pursue pain    Goal: To provide an online standardized               Goal: To provide standardized cognitive
Goal and           management-related care as they               cognitive behavioral therapy for chronic pain         behavioral therapy for chronic pain (CBT-CP)-
rationale of the   normally would within their healthcare        (CBT-CP)-based skills training program designed       based skills training with a focus on tailoring the
elements           system.                                       to accommodate low-literacy participant needs         speciﬁc elements of the skills training approach
essential to the                                                 and allow individuals a ﬂexible approach to skills    to participants’ circumstances in real time. Virtual
intervention       Rationale: Usual care comparison              training they can tailor (time/skill emphasis) to     delivery lowers barriers for receipt of services for
                   enables assessment of beneﬁt of the           their needs. The online format allowed a largely      those in rural/underserved regions of the country
                   study interventions over what treatments      self-directed approach provided at minimal            or otherwise unable to access clinical providers
                   participants are already able to access to    expense (i.e., not dependent on clinician             skilled in evidence-based behavioral pain
                   help manage their pain. This is important     involvement and support limited to technical          services. Interaction with a trained therapist to
                   to understand from a clinical and             help and engagement outreach).                        enhance connectedness and accountability.
                   healthcare-implementation (cost)                                                                    Rationale: CBT-CP-based program delivered by
                   perspective. The resource manual (“plus”)     Rationale: Self-directed CBT-CP-based skills          centrally located, master's-level clinicians should
                   provided to participants in this group was    training allows for a ﬂexible, low-cost approach      enable reinforcement of progress, tailored help
                   consistent with educational materials for     that lowers barriers for high quality CBT-CP-         for participants in identifying and problem-solving
                   healthcare self-management available to       based skills training for those with online access.   obstacles, while retaining beneﬁts of
                   patients in participating healthcare          Multi-media features provided in an easy-to-use       standardized training, treatment adherence, and
                   systems.                                      format utilizing computerized algorithms (based       scalability. Further, nonspeciﬁc elements of
                                                                 on expert clinician guidance) to tailor participant   therapist contact may enhance therapeutic
                                                                 experience and designed to enhance                    outcomes.
                                                                 development and sustained use of pain
                                                                 management coping skills.
WHAT
Participant        American Chronic Pain Association             Participant Workbook: Mailed to participant prior     Participant Workbook: Mailed to participant prior
Materials          Resource Guide to Chronic Pain                to ﬁrst contact from study staff. Includes            to ﬁrst contact from health coach. Includes
                   Management 7, 2020 edition                    instructions for registering, unique program login    overview of each session (content on the
                   This educational guide provides               information, and details on “How to Use the           concepts and skills taught), worksheets to help
                   comprehensive information describing the      Program,” with screenshots and text describing        aid learning of concepts and to log skills practices
                   spectrum of pain management modalities,       the website’s structure, features, how to use and     each week.
                   including passive, active and self-directed   outlines of session content.
                   interventions such as medications,            Program Website: (mypaintrainer.org)                  Participant Resources Website:
                   nutrition, exercise, complementary,           Online sessions that must be completed in a pre-      - 4 audio recordings of guided exercises lasting
                   alternative and integrative medicine, and     determined order, each teaching one or more               5-20 min. (Breath Awareness, 3-Part Breath,
                   biopsychosocial strategies. It is intended    evidence-based pain coping skill8; led by a               Progressive Muscle Relaxation, Guided
                   to educate individuals and does not           recorded “virtual coach” (audio to minimize               Imagery)
                   advise or instruct on treatments but can      reading and support needs for low-literacy



         © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 physical PDF page 3

Source: [DOC-004 p3](../../../../joi250046supp3_prod_1755300121.15087.pdf#page=3). Mapped: R001–R003 provider/training/dose.

```text
RESOLVE Study Description of Interventions Based on Template for Intervention Description and Replication (TIDieR)


                                  Usual Care Plus                                     painTRAINER                                         Health Coach
                     help inform patients on treatment            participants). Provides training in an easy-to-use   -   2 instructional videos lasting 5 min. each
                     decisions to be made in conjunction with     format that includes animated demonstrations,            (Science of Thinking, Feeling and Responding
                     and approved by their healthcare provider.   interactive exercises, tips for working through          to Pain; Activity / Rest Cycle)
                                                                  common barriers to behavior change/skills            -   Access to electronic (PDF) version of
                                                                  practice, and tailored feedback to reinforce             Workbook materials by session
                                                                  learning.
Staff &              None                                         Scripts for staff regarding onboarding and           Health coaches used Standardized Treatment
Interventionist                                                   engagement calls                                     Manual (“Health Coach Manual”)
Materials
Procedures           Printed / hard copy of the resource guide    Eight participant self-completed online              Participants had Eight one-on-one sessions with
                     mailed to participants                       sessions, 30-45 minutes each                         health coach, 45-60 minutes each

                                                                  Participant workbook guided planning and goal        Participant workbook with information on skills
                                                                  setting                                              practice and goal setting
WHO PROVIDED
Expertise/           Not applicable                               Technical support provided by research staff         Health coaches were master's-level behavioral
Background                                                        with prior administrative experience working         health practitioners with no prior training in
                                                                  directly with study participants intended to         chronic pain management (n=12). Centralized
                                                                  emulate what could be delivered by Medical           team based at 2 clinical study sites. Ongoing
                                                                  Assistant type outreach/support.                     supervision provided by clinical psychologist via
                                                                                                                       weekly hour-long team meetings.
Training             Not applicable                               Research staff who provided technical support        Health coaches had approx. 34 hours didactic
                                                                  were given approximately 9 hours of training:        and experiential coursework:
                                                                  - 1-hour videoconference with painTRAINER            - 90-minute overview of pain psychology
                                                                     program developer, Christine Rini; provided       -    For each session the coursework involved: 1)
                                                                     overview of program registration and                  detailed review and discussion of content in
                                                                     structure                                             treatment manual and participant workbook;
                                                                  - 3-hour online training on Motivational                 2) 1-hour, web-based, synchronous didactic
                                                                     Interviewing (MI) techniques provided to KP           training; 3) role playing a participant with
                                                                     employees                                             clinical supervisor or other health coach; 4)
                                                                  - 1-hour videoconference with study PI on                role play as health coach
                                                                     utilizing MI techniques during onboarding         - Clinical supervisors then reviewed for
                                                                     and engagement calls                                  proﬁciency at least 16 sessions completed
                                                                  - 2 hours of onboarding and engagement call              with real participants (2 instances for each of
                                                                     script role play                                      the 8 sessions); proﬁciency required 100%
                                                                  - 2-hour videoconference with study project              ﬁdelity in delivering session content and 80%
                                                                     manager on speciﬁc procedures for                     ﬁdelity on core CBT skills (i.e., ratings of


           © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 physical PDF page 4

Source: [DOC-004 p4](../../../../joi250046supp3_prod_1755300121.15087.pdf#page=4). Mapped: R001–R004 schedule/outreach.

```text
RESOLVE Study Description of Interventions Based on Template for Intervention Description and Replication (TIDieR)


                              Usual Care Plus                                   painTRAINER                                         Health Coach
                                                                conducting onboarding and engagement                  “adequate/good” or higher for each of the 9
                                                                calls, i.e., logging contacts in study tracking       domains on the modiﬁed Cognitive
                                                                system                                                Behavioral Therapy Skills Training for Chronic
                                                            Research staff also given the opportunity to              Pain Therapist Rating Scale relevant for a
                                                            complete each of the painTRAINER online                   particular session)
                                                            modules.
HOW               None                                      - Participants access painTRAINER via                 -   Participant completed sessions by phone or
                                                                website                                               videoconference
                                                            - Participant has unique account with                 -   Sessions were one-on-one with health coach
                                                                username and password
WHERE             Not applicable                            Participant chose location of preference (home,       Participant chose private location of preference
                                                            work, etc.) from which to complete online             (home, work, etc.) from which to complete
                                                            sessions                                              sessions

                                                            Internet access required; format optimized by         Phone access required; internet access for
                                                            computer (vs. smart phone) interface                  videoconferencing optional according to
                                                                                                                  participant preference
WHEN and HOW      Not applicable                            Participants received:                                Participants received:
MUCH                                                        - One onboarding and registration call                - One onboarding and initial scheduling call
                                                                (approx. 15 min)                                      (approx. 10 min)
                                                            - Access 8 weekly online modules (30-45 min)          - 8 weekly sessions with health coach (45-60
                                                                to be completed during 12-week treatment              min) to be completed during 12-week
                                                                period                                                treatment period; In limited instances to
                                                            - Tools to help do skills practice on own                 allow for extenuating circumstances a four-
                                                                between sessions (daily practice                      week extension was allowed (n=14)
                                                                encouraged)                                       - Encouragement to do skills practice on own
                                                            - (If applicable) Phone outreach/contact by               between sessions (daily practice encouraged)
                                                                study staff (MI-based “engagement calls”) if
                                                                not adhering to the recommended
                                                                completion schedule: > 7 days since
                                                                participant registered and session 1 not
                                                                initiated; initiated a session but incomplete
                                                                after > 7 days; >10 days since any session
                                                                completion date; and sessions completed
                                                                too quickly (3 or more sessions completed in
                                                                9 days). N=356 of the 776 in this study group
                                                                completed ≥1 outreach call with a staff


        © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 physical PDF page 5

Source: [DOC-004 p5](../../../../joi250046supp3_prod_1755300121.15087.pdf#page=5). Mapped: R003–R005 modification and fidelity.

```text
RESOLVE Study Description of Interventions Based on Template for Intervention Description and Replication (TIDieR)


                              Usual Care Plus                                     painTRAINER                                     Health Coach
                                                                   member (45.9%). Average number of
                                                                   outreach calls completed for these N=356
                                                                   was 1.8 (Range: 1-7) with an average length
                                                                   of 4 minutes.
                                                              - Full 12 month access to PainTRAINER online
                                                                   program
TAILORING/        Participants chose to pursue usual care     Participants chose when and which                  Participants chose to complete sessions by
PERSONAL-         according to their needs and preferences.   skills/strategies to practice.                     phone or videoconferencing.
IZATION
                                                              Participants chose to pursue usual care            Participants chose when and which
                                                              according to their needs and preferences.          skills/strategies to practice.

                                                                                                                 Participants chose to pursue usual care
                                                                                                                 according to their needs and preferences.

                                                                                                                 Health coaches tailored individual participant
                                                                                                                 home practice goals to participants resources,
                                                                                                                 interests, and values. Pain education was tailored
                                                                                                                 to participants’ speciﬁc musculoskeletal pain
                                                                                                                 condition(s) and related comorbidities.
MODIFICATIONS     None                                        Added motivational interviewing-based language     None
                                                              to the onboarding and registration call script
                                                              used by research staff to improve engagement.
                                                              Change was implemented on 8/9/2021 after
                                                              ~140 participants were enrolled in the study.
HOW WELL / FIDELITY
Planned          Not applicable                               Not applicable; treatment is standardized          Sessions were audio or video-recorded with
                                                              because the intervention is delivered via an       participant permission. Health coaches
                                                              online program thus no ﬁdelity monitoring of       completed self-assessment of their ﬁdelity to
                                                              intervention administration is warranted.          session content after each session.
                                                                                                                 - For first 12 months after reaching
                                                                                                                     proficiency, random sample of 5% of each
                                                                                                                     health coach’s completed sessions were
                                                                                                                     reviewed by clinical supervisors. Feedback
                                                                                                                     provided electronically with option for 1:1
                                                                                                                     discussion.



        © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 physical PDF page 6

Source: [DOC-004 p6](../../../../joi250046supp3_prod_1755300121.15087.pdf#page=6). Mapped: R003 actual fidelity.

```text
RESOLVE Study Description of Interventions Based on Template for Intervention Description and Replication (TIDieR)


                               Usual Care Plus                                painTRAINER                                       Health Coach
                                                                                                             -    For months 13+, one randomly selected
                                                                                                                  session per coach every 6 months was
                                                                                                                  reviewed for ﬁdelity. Feedback provided
                                                                                                                  electronically with option for 1:1 discussion.
                                                                                                             If reviewed session did not meet criteria of 100%
                                                                                                             ﬁdelity in session content and 80% ﬁdelity on CBT
                                                                                                             treatment principles, additional sessions
                                                                                                             reviewed, and feedback provided until met
                                                                                                             proﬁciency.
Actual             Not applicable                            Not applicable                                  A total of N=299 sessions out of 4,626 completed
                                                                                                             were reviewed for ﬁdelity (6.5%)
                                                                                                             - Training to proﬁciency period: 193 sessions
                                                                                                                  reviewed
                                                                                                             - First 12 months: 89 sessions out of 1,791
                                                                                                                  reviewed (5%)
                                                                                                             - Month 13+ (1 session reviewed every 6
                                                                                                                  months per coach): 17 sessions out of 2,350
                                                                                                             There were N=8 instances in which session
                                                                                                             content did not meet 100% ﬁdelity and needed to
                                                                                                             be redone (8/299=2.7%) and N=11 instances
                                                                                                             where the ﬁdelity to CBT treatment principles did
                                                                                                             not meet 80% (11/299=3.7%).




         © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-004 physical PDF page 7

Source: [DOC-004 p7](../../../../joi250046supp3_prod_1755300121.15087.pdf#page=7). Mapped: References; no applicable trial numeric result.

```text
RESOLVE Study Description of Interventions Based on Template for Intervention Description and Replication (TIDieR)


References
1.       Bandura A. Self-efficacy: The exercise of control. W.H. Freeman and Company.; 1997.
2.       Bandura A. Social foundations of thought and action: A social cognitive theory. Prentice-Hall; 1986:xiii, 617 p.
3.       Kennedy CM, Powell J, Payne TH, Ainsworth J, Boyd A, Buchan I. Active Assistance Technology for Health-Related Behavior Change: An
Interdisciplinary Review. Journal of Medical Internet Research. 2012;14(3):e80. doi:10.2196/jmir.1893
4.       Knowles MS, Holton EF, Swanson RA. The adult learner: The deﬁnitive classic in adult education and human resource development. 7th ed.
Elsevier; 2011.
5.       Mayer RE. Applying the science of learning: evidence-based principles for the design of multimedia instruction. American Psychologist. Nov
2008;63(8):760-9. doi:10.1037/0003-066X.63.8.760

6.        Michie S, Richardson M, Johnston M, et al. The behavior change technique taxonomy (v1) of 93 hierarchically clustered techniques: building an
international consensus for the reporting of behavior change interventions. Ann Behav Med. Aug 2013;46(1):81-95. doi:10.1007/s12160-013-9486-6
7.        Feinberg S, Feinberg R, Pohl M, Bokarius V, Darnall B. American Chronic Pain Association Resource Guide to Chronic Pain Management. An
Integrated Guide to Medical, Interventional, Behavioral, Pharmacologic and Rehabilitation Therapies: Rocklin, CA: American Chronic Pain Association,
Inc; 2018.
8.        Rini C, Porter LS, Somers TJ, et al. Automated Internet-based pain coping skills training to manage osteoarthritis pain: a randomized controlled
trial. Pain. May 2015;156(5):837-48. doi:10.1097/j.pain.0000000000000121




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 1

Source: [DOC-005 p1](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=1). Mapped: Cover and full contents; no applicable result.

```text
Supplementary Online Content


DeBar LL, Mayhew M, Wellman RD, et al. Telehealth and online cognitive behavioral
therapy–based treatments for high-impact chronic pain: a randomized clinical trial. JAMA.
Published online July 23, 2025. doi:10.1001/jama.2025.11178

OUTCOME MEASURES .............................................................................................................................. 2
INTERVENTION ADHERENCE .................................................................................................................... 3
MISSING DATA ............................................................................................................................................. 4
  Adjustment: ............................................................................................................................................... 4
  Imputation (MNAR): .................................................................................................................................. 4
  Non-Response Weighting: ........................................................................................................................ 5
SENSITIVITY ANALYSES .......................................................................................................................... 11
  Missing Data Analyses: ........................................................................................................................... 11
  Protocol Change Subset Analyses: ........................................................................................................ 13
ADDITIONAL UNADJUSTED DATA AND ANALYSES ............................................................................. 15
eREFERENCES .......................................................................................................................................... 19
eFigure 1. Histogram of Number of Sessions completed for those randomized to painTRAINER and those
     randomized to the Virtual Health Coach ...................................................................................... 3
eTable 1. Primary outcome follow-up rates and patterns overall and by arm. .........................................7
eTable 2. Baseline variables used in process of selecting covariates related to missingness and to MCID
     of pain severity at 3 months. ....................................................................................................... 7
eTable 3. Imputation step 1: Summary of ﬁtted imputation model for primary analysis. .........................8
eTable 4. Imputation step 2: Summary of primary estimation model ﬁt to imputed data with weighting. .9
eTable 5. Summary of logistic weighting model for any observed follow-up. ........................................ 10
eTable 6. Summary of estimated weights. .......................................................................................... 10
eFigure 2. Histogram of estimated probabilities and weights. ............................................................. 10
eTable 7. Pre-speciﬁed Sensitivity Analyses for different approaches to handling missing data. ........... 11
eTable 8. Results of a Subset of Participants after two different protocol changes: Enhancement to
     painTRAINER (randomized after 8/9/2021) and Adding follow-up letters to improve follow-up rates
     (randomized after 3/31/2022) .................................................................................................... 14
eTable 9. Unadjusted percentage of participants with clinically meaningful improvement by treatment
     group and adjusted relative risk between group comparisons for the binary primary outcome (pain
     severity) and secondary pain outcomes .................................................................................... 15
eTable 10. Unadjusted Median and Interquartile Ranges for change from baseline of continuous
     secondary outcomes by treatment group and unadjusted mean differences between group
     comparisons ............................................................................................................................ 16
eTable 11. Unadjusted Median and Interquartile Ranges of continuous secondary outcomes by
     treatment group and unadjusted mean differences in between group comparisons .................... 17

This supplementary material has been provided by the authors to give readers additional
information about their work.



© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 2

Source: [DOC-005 p2](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=2). Mapped: R006 outcome measures.

```text
OUTCOME MEASURES
Pain Severity Score: Based on modified 11-item version of the Brief Pain Inventory – Short Form (BPI-
SF). Score is calculated mean of all 11 items; range 0-10 with a higher score = worse pain severity

Pain Intensity Score: Based on 4-item subscale of the Brief Pain Inventory – Short Form (BPI-SF). Score
is calculated mean of all 4 items; range 0-10 with a higher score = worse pain intensity

Pain-related Interference Score: Based on 7-item subscale of the Brief Pain Inventory – Short Form (BPI-
SF). Score is calculated mean of 7 items; range 0-10 with a higher score = worse pain-related interference

Minimal clinically important difference (MCID) is defined as ≥30% decrease in pain score from baseline
(i.e., improvement; pain score range 0-10 with a higher score = worse pain severity, intensity or related
interference)

8-Item Patient Health Questionnaire Depression Scale (PHQ-8): Sum of 8 items related to depressive
symptoms (each item response 0-3) with total scale range=0-24; higher score = greater severity of
depressive symptoms. Cut points= 10 (moderate), 15 (moderately severe) and 20 (severe depression).

The Generalized Anxiety Disorder 7-item Scale (GAD-7): Sum of 7 items related to anxiety symptoms
(each item response 0-3) with total scale range=0-21; higher score = greater severity of anxiety
symptoms. Cut points= 5 (mild), 10 (moderate) and 15 (severe) levels of anxiety.

PROMIS (Patient-Reported Outcomes Measurement Information System) Sleep Disturbance – Short
Form 6a: Score by summing the 6 items (each item response 1-5) and then converting raw score to
standardized T-score, using the HealthMeasures Scoring Service, with mean of 50 and standard deviation
of 10. Higher T-score= worse sleep disturbance. Score ≥60 indicates moderate (60-70) to severe (>70)
sleep disturbance.

PROMIS Ability to Participate in Social Roles and Activities – Short Form 4a: Score by summing the 4
items (each item response 1-5) and then converting raw score to standardized T-score, using the
HealthMeasures Scoring Service, with mean of 50 and standard deviation of 10. Higher T-score= better
ability to participate in social roles and activities. Score ≤40 indicates moderate (40-30) to severe (< 30)
limitations in ability to participate.

PROMIS Physical Function – Short Form 6b: Score by summing the 6 items (each item response 1-5) and
then converting raw score to standardized T-score, using the HealthMeasures Scoring Service, with mean
of 50 and standard deviation of 10. Higher T-score= better physical functioning. Score ≤40 indicates
moderate (40-30) to severe (< 30) limitations in physical functioning.




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 3

Source: [DOC-005 p3](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=3). Mapped: R007 complete adherence figure.

```text
INTERVENTION ADHERENCE
eFigure 1. Histogram of Number of Sessions completed for those randomized to
painTRAINER and those randomized to the Virtual Health Coach




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 4

Source: [DOC-005 p4](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4). Mapped: R008–R010 missingness and imputation.

```text
MISSING DATA
The study met the pre-specified criteria enumerated in the statistical analysis plan (SAP; Supplement 2) for the
primary analysis to use an imputation approach which assumes the data are missing not at random (MNAR) in
combination with non-response weighting and regression adjustment. The specific criteria were missingness of the
primary outcome, MCID in pain severity (30% reduction from baseline), at 3-month (primary time-point) above
15% or differential missingness between arms. As shown in eTable 1, the 3-month primary outcome was complete
77.1% overall (79.9% UC, 69.8% PT, and 81.6% HC). Overall, 67.3% of individuals had all three time points
observed and 12.7% of individuals were missing follow-up at all three time points.
Details regarding the imputation procedure, the models for imputation and for the weights, measured covariates, and
variable selection are provided in the sections below. Supplement 5 displays the distributions of all measured
baseline characteristics, both overall and within groups defined by three patterns of observed follow-up data for the
primary outcome: 1) no recorded follow-up measures, 2) one or 2 follow-up measures recorded, or 3) all follow-up
measures recorded.
Adjustment: The statistical analysis plan for the primary outcome pre-specified adjustment for baseline levels of
pain severity, other stratification variables (sex, clinical site, and rural/medically underserved residency), and a priori
variables predictive of outcome (multisite pain and co-occurring mental health condition). Additional predictor
variables were assessed and included in the imputation and estimation models if they were related both to
missingness of the 3-month time-point and were predictive of MCID in pain severity at 3 months. Specific
additional predictors for the imputation and estimation models were selected after assessing all other available
covariates, one-by-one, in separate logistic regression models for missingness at 3-months, and in separate modified
Poisson models1 for MCID in pain severity at 3-months, while adjusting for study arm and the base set of pre-
specified adjustment variables: baseline pain severity, age, sex, clinical site, rural/medically underserved residency,
multisite pain, and co-occurring mental health conditions. In this context, if a covariate was significant at the 0.10
level in both the missingness and outcome models while adjusting for the base set of predictors, then it was added as
an adjustment factor in the imputation and estimation models for the main analysis. A similar process was used to
select additional covariates for the weight model, details of which are described below in the section on non-
response weighting. eTable 2 provides a list of variables that were assessed during the selection process and
provides a list of additional variables that were selected for the main models and the weight model. Supplement 5
also provides p-values for variables that were significant in one or more of the selection models used to identify
additional adjustment variables, i.e., variables that were significantly (P<0.10) related to the binary outcome MCID
in pain severity at 3 months and/or the presence of missing values in the 3-month pain severity, and/or the likelihood
of missing all follow-up points (non-response).
Imputation (MNAR): Implementation of the MNAR imputation approach for GEE2 requires the specification and
execution of a two-step modeling process. The first step is to impute missing outcome data using a pattern-mixture
approach with reasonable choices for included missing patterns given the amount of missing data. To classify
patterns of missing data in this study, among those with any observed follow-up measure we created a categorical
variable indicating whether each participant had one (8.1%), two (12.1 %) or three (67.3%) follow-up observations
recorded. The full imputation model was specified as follows:


         𝐸𝐸(𝑌𝑌𝑖𝑖𝑖𝑖 |𝑋𝑋𝑖𝑖 , 𝒁𝒁𝑖𝑖 ) = 𝛼𝛼 + 𝛽𝛽𝑃𝑃𝑃𝑃 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝑃𝑃𝑃𝑃) + 𝛽𝛽𝐻𝐻𝐻𝐻 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝐻𝐻𝐻𝐻) + 𝜷𝜷𝑧𝑧 𝒁𝒁𝑖𝑖 + 𝛽𝛽6 𝐼𝐼(𝑚𝑚 = 6) + 𝛽𝛽12 𝐼𝐼(𝑚𝑚 = 12)
                                 + 𝛾𝛾𝑃𝑃𝑃𝑃,6 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑚𝑚 = 6) + 𝛾𝛾𝑃𝑃𝑃𝑃,12 𝐼𝐼(𝑋𝑋i = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑚𝑚 = 12)

                                 +𝛾𝛾𝐻𝐻𝐻𝐻,6 𝐼𝐼(Xi = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑚𝑚 = 6) + 𝛾𝛾𝐻𝐻𝐻𝐻,12 𝐼𝐼(Xi = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑚𝑚 = 12)

                                                  +𝜂𝜂1 𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 1) + 𝜂𝜂2 𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 2)

                               +𝜂𝜂𝑃𝑃𝑃𝑃,1 𝐼𝐼(𝑋𝑋i = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 1) + 𝜂𝜂𝐻𝐻𝐻𝐻,1 𝐼𝐼(𝑋𝑋i = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 1)

                               +𝜂𝜂𝑃𝑃𝑃𝑃,2 𝐼𝐼(𝑋𝑋i = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 2) + 𝜂𝜂𝐻𝐻𝐻𝐻,2 𝐼𝐼(𝑋𝑋i = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 = 2)


© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 5

Source: [DOC-005 p5](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5). Mapped: R009–R012 models and weights.

```text
where 𝑌𝑌𝑖𝑖𝑖𝑖 is the change in pain severity for individual i at time point 𝑚𝑚, 𝑋𝑋𝑖𝑖 is the intervention group (UC, PT, and
UC), 𝑚𝑚 is the number of months post randomization, and 𝒁𝒁𝑖𝑖 is the vector of baseline covariates. Further, 𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 is a
variable that indicates the pattern of observed outcomes present. In this case, 𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 takes on the values 1, 2 or 3
depending on whether 1, 2 or 3 of the follow-up measures are observed for a randomized person. The 𝒁𝒁𝑖𝑖 include all
adjustment variables as specified previously. We fit this assuming a modified linear model using GEE with
independent working correlation and robust standard errors, accounting for clustering of participants within health
coaches and multiple observations per person. The fitted imputation model was then used to replace missing
outcomes data with predicted values from the model. The binary MCID outcome variable was then calculated using
the change outcome with imputed data and the baseline value of pain severity.

In the second step, the following estimation model was fit to the full imputed data with the binary MCID outcome
now represented as 𝑌𝑌�𝑖𝑖𝑖𝑖 and using the following pre-specified functional form from the statistical analysis plan:

      𝑙𝑙𝑙𝑙𝑙𝑙(𝐸𝐸�𝑌𝑌�𝑖𝑖𝑖𝑖 �𝑋𝑋𝑖𝑖 , 𝒁𝒁𝑖𝑖 )) = 𝛼𝛼 + 𝛽𝛽𝑃𝑃𝑃𝑃 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝑃𝑃𝑃𝑃) + 𝛽𝛽𝐻𝐻𝐻𝐻 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝐻𝐻𝐻𝐻) + 𝜷𝜷𝑧𝑧 𝒁𝒁𝑖𝑖 + 𝛽𝛽6 𝐼𝐼(𝑚𝑚 = 6) + 𝛽𝛽12 𝐼𝐼(𝑚𝑚 = 12)

                                   + 𝛾𝛾𝑃𝑃𝑃𝑃,6 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑚𝑚 = 6) + 𝛾𝛾𝑃𝑃𝑃𝑃,12 𝐼𝐼(𝑋𝑋i = 𝑃𝑃𝑃𝑃)𝐼𝐼(𝑚𝑚 = 12)

                                   +𝛾𝛾𝐻𝐻𝐻𝐻,6 𝐼𝐼(Xi = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑚𝑚 = 6) + 𝛾𝛾𝐻𝐻𝐻𝐻,12 𝐼𝐼(Xi = 𝐻𝐻𝐻𝐻)𝐼𝐼(𝑚𝑚 = 12).


The model was fit with GEE assuming Poisson errors and using robust sandwich standard errors to account for
clustering within provider and individual.1 Parameter estimates are taken directly from the solution to the second
step GEE model above and the variance-covariance matrix for the joint imputation and analysis model are calculated
as described in Wang and Fitzmaurice.2 Summaries of the fitted imputation and estimation models are provided in
eTable 3 and eTable 4.

As a final note on imputation, there were a small number of cases where baseline covariates contained a limited
number of missing values. To keep the entire randomized cohort intact for all analyses, these missing baseline values
were imputed with their corresponding population means estimated from all available baseline data.3

Non-Response Weighting: The imputation approach assuming data are MNAR was used to impute missing data for
those that had at least one observation, but we observed a higher-than-expected number of participants with all
outcome time points missing (12.7%) and a differential by study arm: 9.5% for Usual care plus, 17.1% for
painTRAINER, and 11.3% for health coach (eTable 1).To be able to estimate an average treatment effect (ATE)
amongst all randomized, and due to concern about differential missingness, we added non-response weighting which
we formally incorporated into the SAP.

For the primary weighted analysis, to estimate the non-response weights, we fit a logistic regression model to the
entire randomized population, with an indicator of at least one observed follow-up as the outcome. Predictor
variables included study arm, baseline pain severity, age, sex, clinical site, rural/medically underserved residency,
multisite pain, and co-occurring mental health conditions and additional variables that were associated both with the
3-month MCID in pain severity outcome and with having any follow-up at 3, 6 or 12 months (Supplement 5). As
detailed above for adjustment variables, additional variables for the weight model were evaluated one-at-a-time by
fitting a sequence of separate models for 3-month MCID in pain severity (modified Poisson regression) and for any
follow-up (logistic regression). Those baseline covariates that, when included in models with study arm and the base
set of adjustment variables, reached statistical significance at the 0.10 level in model for MCID and in the model for
any follow-up (Supplement 5) were added to the weight model.

The final model for the non-response weights took the following form:

                          𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙(𝐸𝐸(𝑅𝑅𝑖𝑖 |𝑋𝑋𝑖𝑖 , 𝒁𝒁𝑖𝑖 )) = 𝛽𝛽0 + 𝛽𝛽𝑃𝑃𝑃𝑃 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝑃𝑃𝑃𝑃) + 𝛽𝛽𝐻𝐻𝐻𝐻 𝐼𝐼(𝑋𝑋𝑖𝑖 = 𝐻𝐻𝐻𝐻) + 𝜷𝜷𝑧𝑧 𝒁𝒁𝑖𝑖 ,

where 𝑅𝑅𝑖𝑖 indicates having at least one observed follow-up measurement. Predictions, 𝑝𝑝𝑖𝑖 , from this model are used to
                         1
calculate weights 𝑤𝑤𝑖𝑖 = . The 𝑤𝑤𝑖𝑖 were then scaled to the study sample size and included as weights in the GEE
                            𝑝𝑝𝑖𝑖



© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 6

Source: [DOC-005 p6](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=6). Mapped: R012 weighting continuation.

```text
estimation model described in the imputation section (step 2). The fitted weight model is presented in eTable 5, and
eTable 6 and eFigure 1 provide summaries of the predicted probabilities and corresponding weights.




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 7

Source: [DOC-005 p7](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7). Mapped: R009,R013 complete eTables1–2.

```text
eTable 1. Primary outcome follow-up rates and patterns overall and by arm.
                                            Usual Care
                             OVERALL           plus    painTRAINER Health Coach
                             N    %          N      %    N     %     N      %
Randomized                  2331            777         776         778
Follow-up
 3 months                   1798    77.1     621    79.9   542     69.8    635     81.6
 6 months                   1790    76.8     622    80.1   547     70.5    621     79.8
 12 months                  1861    79.8     639    82.2   583     75.1    639     82.1
At least 1 follow-up        2036    87.3     703    90.5   643     82.9    690     88.7
No follow-up                 295    12.7      74     9.5   133     17.1     88     11.3
One observed follow-up       188     8.1      64     8.2    77      9.9     47      6.0
Two observed follow-ups      283    12.1      99    12.7   103     13.3     81     10.4
Three observed follow-ups   1568    67.3     540    69.5   464     59.8    564     72.5

eTable 2. Baseline variables used in process of selecting covariates related to
missingness and to MCID of pain severity at 3 months.
 Category                            Variables
                                     Study arm, sex (male vs. female), age (≥65 vs. <65 years),
                                     clinical site, rural/medically underserved residency (urban vs.
 Variables included in all models    rural), multisite pain (>1 site of pain), and co-occurring mental
                                     health conditions (presence of depression and/or anxiety
                                     diagnoses)
 VARIABLES PROVIDED FOR SELECTION
     Demographic characteristics     Race and ethnicity (Asian, Black, Hispanic, Multiple, Native
                                     Hawaiian or Pacific Islander, White non-Hispanic), education,
                                     unemployment, household income (<25K, 25-<50K, 50-<100K,
                                     100-<150K, 150K or more), married/partnered (yes vs. no),
                                     substance abuse disorder diagnosis (present vs. absent)
     Pain Related & expectations     Comorbidities (Charlson, EHR), number of musculoskeletal
                                     pain conditions in the past year (EHR), number of pain-related
                                     healthcare encounters (EHR), presence of specific types of
                                     pain (back, neck, arm/hand/wrist, legs/feet, head,
                                     abdomen/pelvis, tooth/jaw, general pain), pain duration
     Clinical Characteristics/Health Depression (PHQ-8), anxiety (GAD-7), PROMIS sleep
     Habits                          disturbance, presence of negative social determinants of health
                                     – individual, presence of any, and count (financial strain, food
                                     insecurity, housing instability, and/or transportation insecurity)
     Baseline secondary and          Pain intensity, pain-related interference, PROMIS social role
     Tertiary Outcomes               functioning, PROMIS physical functioning, PEG score
 FINAL VARIABLES SELECTED
     Additional variables selected   Education (any college vs. HS degree or less), unemployment
     for inclusion in imputation and (unemployed vs. employed [full or part-time])
     estimation models
     Additional variables selected   PEG score, Depression (PHQ-8 score), Anxiety (GAD-7 score),
     for inclusion in non-response   presence of any negative social determinant of health,
     weight model.                   education (any college vs. HS degree or less)




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 8

Source: [DOC-005 p8](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8). Mapped: R014 complete eTable3.

```text
eTable 3. Imputation step 1: Summary of fitted imputation model for primary
analysis.
 Step 1. Imputation Model (Linear)
 Outcome: Change in pain severity        Overall      N
 Number of observations used               6108    2036
 Number of missing values                   659

 Variable                                 Est.         95% CI      p-value
 Intercept                               -1.24     -1.42   -1.06    <.001
 painTRAINER (vs. Usual Care plus)       0.49       0.39    0.59    <.001
 Health Coach (vs. Usual Care plus)      0.45       0.36    0.54    <.001
 Time: 6M                                0.13       0.07    0.19    0.025
 Time: 12M                               0.31       0.24    0.38    <.001
 Pattern: 2 observed follow-ups          -0.28     -0.47   -0.08    0.150
 Pattern: 1 observed follow-up           -0.20     -0.36   -0.03    0.226
 painTRAINER | Time 6M                   0.02      -0.07    0.11    0.853
 painTRAINER | Time 12M                  0.01      -0.09    0.12    0.916
 Health Coach | Time 6M                  0.08      -0.01    0.17    0.351
 Health Coach | Time 12M                 -0.06     -0.16    0.04    0.535
 Pattern 2 | painTRAINER                 -0.30     -0.58   -0.02    0.280
 Pattern 1 | painTRAINER                 -0.21     -0.45    0.02    0.368
 Pattern 2 | Health Coach                -0.47     -0.74   -0.19    0.090
 Pattern 1 | Health Coach                0.18      -0.07    0.44    0.468
 Sex: Male                               -0.22     -0.29   -0.14    0.003
 Age >=65                                0.19       0.12    0.27    0.013
 Site 2                                  0.07      -0.03    0.17    0.479
 Site 3                                  0.19       0.08    0.29    0.069
 Site 4                                  0.15       0.05    0.24    0.124
 Residence:Urban                         0.07       0.00    0.15    0.306
 1+ musculoskeletal pain conditions      -0.22     -0.30   -0.14    0.004
 No Mental health diagnosis EHR          0.26       0.19    0.33    <.001
 Pain severity                           0.36       0.33    0.38    <.001
 Education:AA degree (ref = High         -0.02     -0.11    0.08    0.866
 school or less)
 Education:AA degree (ref = High         0.16      0.07    0.25     0.077
 school or less)
 Education:Graduate degree (ref = High   0.39      0.29    0.49    <.001
 school or less)
 Not employed                            -0.55     -0.62   -0.47   <.001




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 9

Source: [DOC-005 p9](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=9). Mapped: R015 complete eTable4.

```text
eTable 4. Imputation step 2: Summary of primary estimation model fit to imputed
data with weighting.
Step 2. Estimation Model (Poisson) –
Imputation with Weights.
                                              Overall Persons
Outcome: Binary 30% improvement in pain
severity.
Number of Observations Used                    6108    2036
Sum of Weights                                 6108
Variable                                        RR         95% CI      p-value
painTRAINER (vs. Usual Care plus)              1.28    1.06     1.55     0.010
Health Coach (vs. Usual care plus)             1.54     1.3     1.82     <.001
Health Coach vs. painTRAINER 3M                 1.2    1.03      1.4     0.019
painTRAINER vs. Usual Care plus 6M             1.44    1.21      1.7    <0.001
painTRAINER vs. Usual Care plus 12M            1.32    1.13     1.54    <0.001
Health Coach vs. Usual Care plus 6M            1.62    1.39      1.9    <0.001
Health Coach vs. Usual Care plus 12M           1.41    1.25     1.59    <0.001
Health Coach vs. painTRAINER 3M                 1.2    1.03      1.4     0.019
Health Coach vs. painTRAINER 6M                1.13    0.98      1.3     0.086
Health Coach vs. painTRAINER 12M               1.07    0.96     1.19     0.215
Sex: Male (vs. Female)                          0.8    0.71     0.91    <0.001
Age >=65 (vs. <65)                             1.15      1      1.33     0.046
Site                                           1.07    0.89     1.28     0.498
Site                                           1.15    0.97     1.37     0.102
Site                                           1.17    1.02     1.34     0.028
Residence: Urban (vs. Rural)                   1.07    0.96     1.19     0.226
1+ musculoskeletal pain conditions (vs. 1)     0.87    0.78     0.97     0.014
Mental health diagnosis EHR (vs. None)         1.15    1.04     1.27     0.008
Pain severity                                  0.99    0.96     1.02     0.451
Education: AA degree (vs. HS or less)          0.97    0.82     1.16     0.770
Education: AA degree (ref vs. HS or less)      1.16      1      1.33     0.046
Education: Graduate degree (vs. HS or less)    1.35    1.13     1.61    <0.001
Not employed (vs. Employed)                    0.72    0.64      0.8    <0.001




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 10

Source: [DOC-005 p10](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10). Mapped: R016–R018 complete eTables5–6/eFigure2.

```text
eTable 5. Summary of logistic weighting model for any observed follow-up.
Variable                                                    OR*              95% CI           P-value
Usual Care plus (vs. painTRAINER)                           2.05         1.50      2.79        <0.001
Health Coach (vs. painTRAINER)                              1.68         1.25      2.26        <0.001
Male Sex                                                    0.76         0.57      1.00         0.053
Age >=65                                                    0.97         0.70      1.35         0.859
Site                                                        2.93         1.97      4.36        <0.001
Site                                                        3.43         2.27      5.18        <0.001
Site                                                        2.48         1.70      3.61        <0.001
Residence Urban                                             0.67         0.49      0.90         0.009
>1 Musculoskeletal Pain Condition                           0.97         0.72      1.29         0.812
No Mental Health Diagnosis                                  1.21         0.92      1.59         0.165
Pain Severity                                               1.05         0.93      1.18         0.417
Not employed                                                1.49         1.11      2.00         0.008
No Negative Social Determinant of Health                    1.34         1.01      1.77         0.042
PEG score                                                   0.96         0.92      1.00         0.037
PHQ-8                                                       0.97         0.94      1.01         0.125
GAD-7                                                       0.99         0.96      1.02         0.524
c-statistic                                                0.679
* OR = Odds Ratio
Health care site information has been excluded.




 eTable 6. Summary of estimated weights.
                                                  Sum    Mean      SD   Min.   P25    P50    P75        Max.
  Estimated probability of having at
  least 1 follow-up.                               --    0.88   0.07    0.50   0.85   0.90   0.93       0.98
  Calculated weight used for
  analysis.                                       2036   1.00   0.09    0.89   0.94   0.97   1.03       1.75


 eFigure 2. Histogram of estimated probabilities and weights.




 © 2025 American Medical Association. All rights reserved, including those for text and data
 mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 11

Source: [DOC-005 p11](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11). Mapped: R019–R020 complete eTable7.

```text
SENSITIVITY ANALYSES
Missing Data Analyses: Sensitivity analysis results for different missing data assumptions for the MCID on pain severity primary outcome are presented in
eTable 7 below. eTable 7 provides results for different models assumptions for missing data that were pre-specified in the SAP including: a) complete-case
analysis (missing outcomes removed) adjusting for baseline pain severity, age, sex, clinical site, rural/medically underserved residency, multisite pain, and co-
occurring mental health conditions; b) worst case/best case analysis (missing outcomes for participants randomized to PT or HC are assumed 0 (worst case) and
missing outcomes for participants randomized to UC are 1 (best case)) adjusting for baseline pain severity, age, sex, clinical site, rural/medically underserved
residency, multisite pain, and co-occurring mental health conditions.

eTable 7. Pre-specified Sensitivity Analyses for different approaches to handling missing data.
              Adjusted % with a 30% improvement in pain                        Adjusted Relative Risk (95% CI)b                            Adjusted Number Needed to
                         score, % (95% CI)b                                                                                    P val c          Treat (95% CI)d,e
              painTRAINER Health Coach      Usual Care
                                                                         PT vs. UC          HC vs. UC          HC vs. PT                 PT vs. UC HC vs. UC HC vs. PT
                  (PT)           (HC)       Plus (UC)
Complete-Case analysis: Adjusted GEE without imputation or weighting (n=1,798 at 3-months; UC=621, PT=542, HC=635)
 3 monthsa 32.2 (28.5, 36.3) 35.5 (32.0, 39.3) 24.0 (20.9, 27.6) 1.34 (1.12, 1.61) 1.48 (1.24, 1.75) 1.10 (0.94, 1.29) <0.001 13 (8, 33)             9 (7, 15)      31 (13, -60)
 6 months 40.1 (36.3, 44.3) 41.1 (37.4, 45.1) 26.6 (23.4, 30.3) 1.51 (1.28, 1.77) 1.54 (1.32, 1.81) 1.02 (0.90, 1.17) <0.001 8 (6, 13) 7 (6, 11) 101 (16, -22)
 12 months 41.0 (37.3, 45.1) 41.5 (37.9, 45.4) 30.5 (27.2, 34.3) 1.34 (1.16, 1.56) 1.36 (1.17, 1.57) 1.01 (0.89, 1.15) <0.001 10 (7, 20) 10 (7, 15) 217 (22, -28)
Worst-Case/Best-Case: Adjusted GEE assuming missing outcome data is Worst Case/Best Case (n=2,331; UC=777, PT=776, HC=778)
 3 monthsa 22.7 (20.0, 25.8) 29.3 (26.3, 32.6) 39.4 (36.1, 43.0) 0.58 (0.49, 0.67) 0.74 (0.65, 0.85) 1.29 (1.09, 1.52) <0.001 -6 (-9, -5) -10 (-18, -7) 16 (10, 40)
  6 months 28.6 (25.6, 31.9) 33.1 (30.0, 36.5) 41.3 (38.0, 44.9) 0.69 (0.60, 0.79) 0.80 (0.70, 0.91) 1.16 (1.00, 1.34) <0.001 -8 (-13, -6) -13 (-26, -8) 23 (12, 227)
  12 months 31.3 (28.2, 34.6) 34.4 (31.2, 37.8) 43.0 (39.6, 46.7) 0.73 (0.64, 0.83) 0.80 (0.70, 0.91) 1.10 (0.96, 1.26) <0.001 -9 (-15, -7) -12 (-21, -8) 33 (15, -194)
a Primary timepoint
b Adjusted mean % and adjusted RR were calculated from a modified Poisson regression model fit using generalized estimating equations (GEE) for each

binary outcome. Adjusted mean % assumes the mean of the covariate distribution to calculate randomized population average effects. Adjustment variables:
Sex, age, site, rural vs. urban residence, more than 1 musculoskeletal pain condition, presence of mental health diagnoses, and pain severity at baseline.
c Omnibus P value is the Wald Test to assess if there is any difference between the three groups. To control for multiple compairsons between-group

comparisons should only be compared if the Omnibus P value<0.05 following the least significant difference approach.
d Adjusted Number needed to treat (NNT) to gain one additional 30% improvement, i.e., one over the difference in the adjusted percent with an 30%

improvement or greater.
e If CIs for the absolute risk difference contain zero the NNT confidence limits appear non-sensical due to division by zero. The NNT estimate is interpreted as

being consistent with a NNT from the lower limit (positive number) to infinity, and a number needed to harm (NNH) from the upper limit (negative number) to
negative infinity.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.
```

### DOC-005 physical PDF page 12

Source: [DOC-005 p12](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=12). Mapped: Footer-only; visually confirmed no applicable content.

```text
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.
```

### DOC-005 physical PDF page 13

Source: [DOC-005 p13](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=13). Mapped: R005,R021 subset definitions.

```text
Protocol Change Subset Analyses: Sensitivity analysis results for different protocol changes for the primary outcome MCID on pain severity are presented in
eTable 8. The results in eTable 8 shows the results of the primary analysis restricting to subsets of the randomized population after the following protocol
changes were made: a) enhancement to the painTRAINER engagement activities (restricts to those randomized after 8/9/2021) and b) reminder letter sent to all
participants prior to follow-up survey reach out (restrict to those randomized after 3/31/2022). Specifically, to improve engagement in the painTRAINER
intervention the study team added motivational interviewing-based language to the onboarding script for those randomized to the online program. This change
was implemented on 8/9/2021 after 454 patients were enrolled in the study. This sensitivity analysis was pre-specified in the SAP to evaluate whether the
“enhanced” painTRAINER engagement activities improved the effect of the painTRAINER intervention. The follow-up letter analysis was not pre-specified in
the SAP, but we have added this post-hoc analysis after observing large improvements in follow-up rates (82.7% overall at 3 months and 90.1% with at least one
follow-up measure) after the study added a reminder letter, mailed to all participants before the due date of their follow-up survey, to remind them to expect an
email or a call (depending on participant preference) from the study team, and encouraged participants to complete the survey when contacted.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.
```

### DOC-005 physical PDF page 14

Source: [DOC-005 p14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14). Mapped: R020–R021 complete eTable8.

```text
eTable 8. Results of a Subset of Participants after two different protocol changes: Enhancement to painTRAINER
      (randomized after 8/9/2021) and Adding follow-up letters to improve follow-up rates (randomized after 3/31/2022)
             Adjusted % with a 30% improvement in pain                  Adjusted Relative Riskc (95% CI)b                       Adjusted Number Needed to Treat
                        score, % (95% CI)b                                                                            P valc               (95% CI)d,e
             painTRAINER Health Coach      Usual Care                                                                                        HC vs.
                                                                    PT vs. UC        HC vs. UC         HC vs. PT                PT vs. UC              HC vs. PT
                 (PT)           (HC)       Plus (UC)                                                                                          UC
Randomized prior to 8/9/2021, N=454; 366 with at least 1 follow-up; PT=149, HC=153, UC=152 at 3-months
 3 monthsa 20.5 (14.2, 29.6) 28.5 (23.4, 34.8) 21.3 (15.2, 29.8) 0.96 (0.59, 1.57) 1.34 (0.92, 1.95) 1.39 (0.92, 2.10) 0.138 -120 (11, -10) 14 (7, -67) 13 (6, -84)
 6 months 32.9 (25.1, 43.0) 32.4 (27.8, 37.7) 25.2 (18.5, 34.2) 1.31 (0.88, 1.95) 1.29 (0.92, 1.80) 0.98 (0.73, 1.33) 0.313 13 (6, -27) 14 (7, -56) -185 (11, -10)
 12 months 32.6 (25.0, 42.5) 37.7 (32.2, 44.3) 20.5 (14.7, 28.6) 1.59 (1.05, 2.41) 1.84 (1.29, 2.63) 1.16 (0.85, 1.57) 0.003     9 (5, 75)   6 (4, 12)   20 (7, -20)
Enhancement to Pain Trainer (Randomized after 8/9/2021, N=1877; 1670 with at least 1 follow-up; UC=512, PT=448, HC=527 at 3-months)
 3 monthsa 28.0 (24.4, 32.0) 32.7 (29.5, 36.2) 20.4 (17.4, 23.9) 1.37 (1.11, 1.69) 1.60 (1.33, 1.93) 1.17 (0.99, 1.38) <0.001 14 (8, 39) 9 (6, 14) 22 (11, -327)
 6 months 33.8 (30.1, 38.1) 38.2 (34.5, 42.3) 22.2 (19.1, 25.7) 1.53 (1.27, 1.84) 1.72 (1.44, 2.06) 1.13 (0.97, 1.32) <0.001     9 (6, 16)   7 (5, 10)   24 (11, -88)
 12 months 36.9 (33.1, 41.2) 38.1 (36.0, 40.3) 28.6 (25.2, 32.5) 1.29 (1.09, 1.52) 1.33 (1.16, 1.52) 1.03 (0.92, 1.16) <0.001   13 (8, 34)   11 (8, 19) 86 (18, -31)
Reminder Letters Added (Randomized after 3/31/2022, N=1038; 935 with at least 1 follow-up; UC=296, PT=262, HC=300 at 3-months)
 3 monthsa 31.6 (26.7, 37.3) 34.1 (29.5, 39.5) 20.5 (16.6, 25.3) 1.54 (1.18, 2.01) 1.67 (1.30, 2.14) 1.08 (0.87, 1.34) <0.001 9 (6, 23) 8 (5, 14)   40 (11, -23)
  6 months 35.6 (30.6, 41.4) 40.6 (35.8, 46.1) 21.3 (17.5, 26.1) 1.67 (1.30, 2.14) 1.90 (1.50, 2.41) 1.14 (0.94, 1.39) <0.001 8 (5, 14)  6 (4, 8)    20 (9, -43)
  12 months 38.2 (33.1, 44.0) 38.9 (35.6, 42.5) 26.1 (21.9, 31.2) 1.46 (1.17, 1.83) 1.49 (1.23, 1.80) 1.02 (0.87, 1.20) <0.001 9 (6, 21) 8 (6, 14) 133 (15, -19)
a Primary timepoint
b Adjusted mean % and adjusted RR were calculated from a modified Poisson regression model fit using generalized estimating equations (GEE) for each

binary outcome. Adjusted mean % assumes the mean of the covariate distribution to calculate randomized population average effects. Adjustment variables:
Sex, age, site, rural vs. urban residence, more than 1 musculoskeletal pain condition, presence of mental health diagnoses, and pain severity at baseline.
c Omnibus P value is the Wald Test to assess if there is any difference between the three groups. To control for multiple comparisons between-group

comparisons should only be compared if the Omnibus P value<0.05 following the least significant difference approach.
d Number needed to treat (NNT) to gain one additional 30% improvement, i.e., one over the difference in the adjusted percent with an 30% improvement or

greater.
e When CIs for the absolute risk difference contain zero the NNT confidence limits appear non-sensical due to division by zero. The NNT estimate is interpreted

as being consistent with a NNT from the lower limit (positive number) to infinity, and a number needed to harm (NNH) from the upper limit (negative number) to
negative infinity.




      © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
      technologies.
```

### DOC-005 physical PDF page 15

Source: [DOC-005 p15](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15). Mapped: R022 complete eTable9.

```text
ADDITIONAL UNADJUSTED DATA AND ANALYSES
For completeness we replicated Tables 2 and 3 in the main manuscript but present unadjusted analyses with no adjustment, weighting or imputation for all
primary and secondary outcomes. eTable 9 presents unadjusted means of the binary primary and secondary outcomes. For Table 3 unadjusted results, we present
two tables in which eTable 10 provides unadjusted mean change from baseline secondary outcomes and eTable 11 provides unadjusted mean secondary
outcomes.

eTable 9. Unadjusted percentage of participants with clinically meaningful improvement by treatment group and
adjusted relative risk between group comparisons for the binary primary outcome (pain severity) and secondary
pain outcomes
                 Unadjusted Number with 30% improvement
                                                                                Relative Risk (95% CI)b
                           in pain score, n/N (%)
                 painTRAINER Health Coach          Usual Care
                                                                     PT vs UC          HC vs. UC          HC vs. PT
                     (PT)        (HC)               plus (UC)
Pain Severity
   3 monthsa     179/542 (33.0) 229/635 (36.1) 151/621 (24.3) 1.36 (1.13, 1.63) 1.48 (1.26, 1.75) 1.09 (0.94, 1.27)
   6 months      225/547 (41.1) 259/621 (41.7) 167/622 (26.8) 1.53 (1.30, 1.80) 1.55 (1.32, 1.83) 1.01 (0.88, 1.17)
   12 months 246/583 (42.2) 269/639 (42.1) 197/639 (30.8) 1.37 (1.18, 1.59) 1.37 (1.21, 1.54) 1.00 (0.90, 1.10)
Pain Intensity
   3 monthsa     164/543 (30.2) 192/635 (30.2) 129/621 (20.8) 1.46 (1.19, 1.78) 1.46 (1.18, 1.79) 1.00 (0.83, 1.21)
   6 months      183/548 (33.4) 222/622 (35.7) 153/623 (24.6) 1.36 (1.13, 1.63) 1.45 (1.20, 1.74) 1.06 (0.90, 1.26)
   12 months 218/583 (37.4) 238/641 (37.1) 191/639 (29.9) 1.25 (1.07, 1.47) 1.24 (1.08, 1.42) 0.99 (0.87, 1.12)
Pain-related Interference
   3 monthsa     206/543 (37.9) 249/635 (39.2) 169/620 (27.3) 1.39 (1.17, 1.64) 1.44 (1.25, 1.65) 1.03 (0.92, 1.17)
   6 months      249/546 (45.6) 277/620 (44.7) 176/621 (28.3) 1.61 (1.38, 1.88) 1.58 (1.35, 1.85) 0.98 (0.86, 1.12)
   12 months 267/583 (45.8) 293/638 (45.9) 221/638 (34.6) 1.32 (1.15, 1.52) 1.33 (1.18, 1.48) 1.00 (0.91, 1.10)
a Primary timepoint

b Relative Risk and 95% Confidence Intervals were calculated from a modified Poisson regression model fit using

generalized estimating equations (GEE) for each binary outcome without adjustment.




© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.
```

### DOC-005 physical PDF page 16

Source: [DOC-005 p16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16). Mapped: R023 complete eTable10.

```text
eTable 10. Unadjusted Median and Interquartile Ranges for change from baseline of continuous secondary
outcomes by treatment group and unadjusted mean differences between group comparisons
                                                                                 Unadjusted Between-Group Mean
             Change from Baseline Median (25%-tile, 75%tile)
                                                                                      Differences (95% CI)b                       Omnibus
             painTRAINER           Health Coach        Usual Care plus                                                             P value
                                                                             PT vs. UC         HC vs. UC         HC vs. PT
                 (PT)                  (HC)                 (UC)
Pain Severity
3 monthsa    -1.1 (-2.1, -0.1)     -1.1 (-2.3, -0.1)    -0.6 (-1.6, 0.2)   -0.4 (-0.6, -0.3) -0.4 (-0.6, -0.3) 0.0 (-0.2, 0.2)     <0.001
6 months     -1.3 (-2.5, -0.1)     -1.4 (-2.5, -0.2)    -0.8 (-1.8, 0.2)   -0.4 (-0.7, -0.2) -0.5 (-0.8, -0.3) -0.1 (-0.3, 0.1)    <0.001
12 months    -1.3 (-2.5, -0.3)     -1.4 (-2.5, -0.2)    -0.8 (-2.2, 0.1)   -0.4 (-0.7, -0.2) -0.4 (-0.6, -0.2) 0.0 (-0.1, 0.2)     <0.001
Pain Intensity
3 monthsa       -0.8 (-1.8, 0.0)   -0.8 (-2.0, 0.0)     -0.5 (-1.5, 0.2)   -0.3 (-0.5, -0.2) -0.3 (-0.5, -0.1) 0.0 (-0.1, 0.2)     <0.001
6 months        -1.0 (-2.0, 0.0)   -1.0 (-2.2, 0.0)     -0.8 (-1.5, 0.2)   -0.3 (-0.5, -0.1) -0.3 (-0.5, -0.2) -0.1 (-0.3, 0.1)    <0.001
12 months       -1.0 (-2.2, 0.0)   -1.0 (-2.2, 0.0)     -0.8 (-2.0, 0.2)   -0.3 (-0.5, -0.1) -0.2 (-0.4, -0.1) 0.0 (-0.1, 0.2)     <0.001
Pain-related Interference
3 monthsa    -1.3 (-2.4, -0.1)     -1.3 (-2.6, 0.0)     -0.7 (-1.9, 0.1)   -0.5 (-0.7, -0.3) -0.5 (-0.7, -0.3) 0.0 (-0.2, 0.2)     <0.001
6 months        -1.4 (-2.9, 0.0)   -1.6 (-2.9, -0.1)    -0.9 (-2.1, 0.1)   -0.6 (-0.8, -0.3) -0.6 (-0.9, -0.4) -0.1 (-0.4, 0.2)    <0.001
12 months    -1.6 (-3.0, -0.1)     -1.6 (-3.0, -0.1)    -1.0 (-2.6, 0.1)   -0.5 (-0.8, -0.3) -0.5 (-0.7, -0.3) 0.0 (-0.2, 0.3)     <0.001
Social Role Functioning
3 monthsa        1.8 (-2.0, 5.8)   1.9 (-1.9, 6.0)      0.0 (-2.2, 4.3)     0.9 (0.1, 1.7)    1.5 (0.7, 2.2)   0.5 (-0.2, 1.3)     <0.001
6 months         1.9 (-1.9, 6.5)   1.9 (-1.9, 7.4)      1.5 (-3.2, 5.5)     1.3 (0.4, 2.2)    1.7 (0.9, 2.6)   0.4 (-0.5, 1.4)     <0.001
12 months        1.9 (-1.9, 7.5)   2.0 (-1.7, 7.7)      0.0 (-3.2, 5.8)     1.4 (0.4, 2.3)    1.4 (0.8, 2.1)   0.1 (-0.7, 0.8)     <0.001
Physical Functioning
3 monthsa        1.6 (-0.8, 3.6)   1.2 (-0.8, 3.8)      0.9 (-1.4, 3.2)     0.6 (0.1, 1.1)    0.8 (0.3, 1.2)   0.1 (-0.3, 0.6)     0.002
6 months         1.7 (-0.8, 4.4)   1.2 (-0.9, 4.4)      1.0 (-1.0, 3.6)     0.8 (0.3, 1.4)    0.5 (0.1, 0.9)   -0.3 (-0.8, 0.2)    <0.001
12 months        1.9 (-0.9, 5.0)   1.3 (-1.2, 4.6)      0.9 (-1.7, 3.6)     1.1 (0.5, 1.7)    0.8 (0.2, 1.5)   -0.3 (-0.9, 0.4)    <0.001
a Primary timepoint
b Mean change from baseline and unadjusted between group mean difference confidence intervals were calculated using
linear regression model fit using generalized estimating equations (GEE) for each continuous outcome.


© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.
```

### DOC-005 physical PDF page 17

Source: [DOC-005 p17](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=17). Mapped: R024 complete eTable11.

```text
eTable 11. Unadjusted Median and Interquartile Ranges of continuous secondary outcomes by treatment group
     and unadjusted mean differences in between group comparisons
                         Raw Score Median (25%-tile, 75%tile)                Unadjusted Between-Group Mean Differences (95% CI)b
                                                                                                                                         Omnibus P
                                                      Usual Care plus                                                                      value
                 painTRAINER (PT) Health Coach (HC)                            PT vs. UC           HC vs. UC           HC vs. PT
                                                           (UC)
Pain Severity
3 monthsa            5.1 (4.9, 5.2)    4.6 (4.4, 4.7)     4.6 (4.5, 4.7)     -0.5 (-0.7, -0.3)   -0.5 (-0.7, -0.3)    0.0 (-0.2, 0.2)     <0.001
6 months             5.0 (4.8, 5.1)    4.4 (4.2, 4.6)     4.4 (4.2, 4.5)     -0.6 (-0.8, -0.3)   -0.6 (-0.8, -0.3)   -0.0 (-0.2, 0.2)     <0.001
12 months            4.8 (4.6, 4.9)    4.2 (4.1, 4.4)     4.3 (4.2, 4.5)     -0.5 (-0.8, -0.3)   -0.4 (-0.6, -0.2)    0.1 (-0.1, 0.3)     <0.001
Pain Intensity
3 monthsa            4.9 (4.7, 5.0)    4.5 (4.3, 4.6)     4.5 (4.4, 4.6)     -0.4 (-0.6, -0.2)   -0.3 (-0.5, -0.1)    0.0 (-0.2, 0.2)     <0.001
6 months             4.8 (4.6, 4.9)    4.4 (4.2, 4.5)     4.4 (4.3, 4.5)     -0.4 (-0.6, -0.2)   -0.4 (-0.6, -0.2)   -0.0 (-0.2, 0.2)     <0.001
12 months            4.6 (4.4, 4.7)    4.2 (4.1, 4.4)     4.3 (4.2, 4.4)     -0.3 (-0.6, -0.1)   -0.2 (-0.4, -0.1)    0.1 (-0.1, 0.3)     <0.001
Pain-related Interference
3 monthsa            5.2 (5.0, 5.3)    4.6 (4.4, 4.8)     4.6 (4.5, 4.7)     -0.6 (-0.8, -0.3)   -0.6 (-0.8, -0.4)    0.0 (-0.2, 0.2)     <0.001
6 months             5.1 (4.9, 5.2)    4.4 (4.2, 4.6)     4.4 (4.2, 4.6)     -0.7 (-0.9, -0.4)   -0.7 (-0.9, -0.4)   -0.0 (-0.3, 0.2)     <0.001
12 months            4.9 (4.7, 5.1)    4.2 (4.0, 4.4)     4.3 (4.2, 4.5)     -0.6 (-0.9, -0.4)   -0.5 (-0.8, -0.3)    0.1 (-0.1, 0.3)     <0.001
Social Role Functioning
3 monthsa          43.4 (42.8, 44.0) 44.6 (43.9, 45.3)   44.8 (44.4, 45.2)    1.2 (0.3, 2.1)      1.4 (0.7, 2.2)      0.2 (-0.5, 1.0)     0.001
6 months           43.6 (42.9, 44.2) 45.4 (44.7, 46.0)   45.1 (44.7, 45.4)    1.8 (0.9, 2.7)      1.5 (0.8, 2.2)     -0.3 (-1.0, 0.4)     <0.001
12 months          43.9 (43.3, 44.6) 45.8 (45.1, 46.5)   45.3 (44.8, 45.8)    1.8 (0.9, 2.8)      1.4 (0.5, 2.2)     -0.5 (-1.3, 0.3)     <0.001
Physical Functioning
3 monthsa          37.7 (37.1, 38.2) 38.2 (37.7, 38.8)   38.2 (37.7, 38.8)   0.6 (-0.2, 1.3)     0.6 (-0.2, 1.3)      0.0 (-0.8, 0.8)      0.212
6 months           37.9 (37.3, 38.4) 38.9 (38.4, 39.5)   38.3 (37.8, 38.8)   1.1 (0.3, 1.9)      0.4 (-0.3, 1.1)     -0.6 (-1.4, 0.1)      0.005
12 months          37.9 (37.3, 38.4) 39.1 (38.5, 39.7)   38.8 (38.1, 39.4)   1.2 (0.4, 2.0)      0.9 (0.0, 1.8)      -0.3 (-1.2, 0.6)      0.001
Patient Global Impression of Change – Pain
3 monthsa            2.9 (2.8, 2.9)    2.0 (1.0, 3.0)     1.9 (1.9, 2.0)     -0.8 (-0.9, -0.6)   -0.9 (-1.0, -0.8)   -0.2 (-0.3, -0.0)    <0.001
6 months             2.8 (2.7, 2.9)    2.1 (2.0, 2.2)     2.1 (2.0, 2.2)     -0.7 (-0.8, -0.5)   -0.7 (-0.8, -0.5)    -0.0 (-0.2, 0.1)    <0.001
12 months            2.8 (2.7, 2.9)    2.1 (2.0, 2.2)     2.2 (2.1, 2.3)     -0.7 (-0.8, -0.5)   -0.6 (-0.7, -0.4)     0.1 (-0.1, 0.2)    <0.001
Patient Global Impression of Change – General
3 monthsa            2.7 (2.6, 2.7)    2.0 (1.0, 2.0)     1.6 (1.5, 1.6)     -0.8 (-0.9, -0.6)   -1.1 (-1.2, -1.0)   -0.3 (-0.5, -0.2)    <0.001
6 months             2.5 (2.4, 2.6)    2.0 (1.9, 2.1)     1.8 (1.7, 1.9)     -0.6 (-0.7, -0.4)   -0.8 (-0.9, -0.6)   -0.2 (-0.3, -0.0)    <0.001
12 months            2.6 (2.4, 2.7)    1.9 (1.8, 2.1)     1.9 (1.7, 2.0)     -0.6 (-0.8, -0.4)   -0.7 (-0.8, -0.5)    -0.1 (-0.2, 0.1)    <0.001


     © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
     technologies.
```

### DOC-005 physical PDF page 18

Source: [DOC-005 p18](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=18). Mapped: R024 eTable11 footnote continuation.

```text
a Primary timepoint; b Unadjusted between group mean differences and 95% confidence intervals were calculated using linear regression model fit using generalized estimating equations (GEE) for

each continuous outcome.




       © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
       technologies.
```

### DOC-005 physical PDF page 19

Source: [DOC-005 p19](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=19). Mapped: References; no applicable trial numeric result.

```text
eREFERENCES
1. Zou G. A modified poisson regression approach to prospective studies with binary data. Am J Epidemiol. Apr 1
   2004;159(7):702-6.
2. Wang M, Fitzmaurice GM. A simple imputation method for longitudinal studies with non-ignorable non-
   responses. Biom J. Apr 2006;48(2):302-18.
3. White IR, Thompson SG. Adjusting for partially missing baseline measurements in randomized trials. Stat Med.
   Apr 15 2005;24(7):993-1007.




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

## DOC-006 complete exact worksheet-cell evidence

Source: [Results workbook](../../../../joi250046supp5_prod_1755300121.16087.xlsx), worksheet **eTable 3**, exact cells in the table below. All525 nonempty cells follow; dimensionA1:J115 includes blank cells which carry no value. ColumnsF and blank cells inG–J are not zeroP values. Stored numeric strings retain their full precision and scientific notation. Numeric cells are literal values, not computed formula caches; text strings embed displayed counts/percentages or means/SD. Zero formula cells; zero formula-derived caches; no recalculation.

| Exact cell | Stored/displayed value | Formula |
|---|---|---|
| eTable 3!A1 | Baseline Characteristics Overall and by Category of Primary Outcome Completion: Missing all 3 Follow-up Points, Missing 1 or 2 Follow-ups or Having All Follow-ups Observed  | None |
| eTable 3!B2 | OVERALL | None |
| eTable 3!C2 | Missing All | None |
| eTable 3!D2 | Missing 1 or 2 | None |
| eTable 3!E2 | All Observed | None |
| eTable 3!G2 | Pre-specified Adjustment Variables | None |
| eTable 3!H2 | P-Value if Related to Primary MCID Outcome | None |
| eTable 3!I2 | P-Value if Related to Overall Non-Response | None |
| eTable 3!J2 | P-Value if related to missingnes in 3 month primary time point  | None |
| eTable 3!A3 | BASELINE CHARACTERISTICS | None |
| eTable 3!B3 | (N=2331) | None |
| eTable 3!C3 | (N=295 ) | None |
| eTable 3!D3 | (N=468) | None |
| eTable 3!E3 | (N=1568) | None |
| eTable 3!A4 | Clinical Site, N (%) | None |
| eTable 3!G4 | X | None |
| eTable 3!A5 | A | None |
| eTable 3!B5 | 566 (24.3) | None |
| eTable 3!C5 | 51 (17.3) | None |
| eTable 3!D5 | 109 (23.3) | None |
| eTable 3!E5 | 406 (25.9) | None |
| eTable 3!A6 | B | None |
| eTable 3!B6 | 609 (26.1) | None |
| eTable 3!C6 | 68 (23.1) | None |
| eTable 3!D6 | 162 (34.6) | None |
| eTable 3!E6 | 379 (24.2) | None |
| eTable 3!A7 | C | None |
| eTable 3!B7 | 606 (26.0) | None |
| eTable 3!C7 | 119 (40.3) | None |
| eTable 3!D7 | 117 (25.0) | None |
| eTable 3!E7 | 370 (23.6) | None |
| eTable 3!A8 | D | None |
| eTable 3!B8 | 550 (23.6) | None |
| eTable 3!C8 | 57 (19.3) | None |
| eTable 3!D8 | 80 (17.1) | None |
| eTable 3!E8 | 413 (26.3) | None |
| eTable 3!A9 | DEMOGRAPHICS | None |
| eTable 3!A10 | Age in yearsc | None |
| eTable 3!B10 | 58.8 (14.3) | None |
| eTable 3!C10 | 56.3 (15.2) | None |
| eTable 3!D10 | 57.7 (13.8) | None |
| eTable 3!E10 | 59.6 (14.1) | None |
| eTable 3!G10 | X | None |
| eTable 3!A11 | Female*,b,c N (%) | None |
| eTable 3!B11 | 1713 (73.5) | None |
| eTable 3!C11 | 206 (69.8) | None |
| eTable 3!D11 | 343 (73.3) | None |
| eTable 3!E11 | 1164 (74.2) | None |
| eTable 3!G11 | X | None |
| eTable 3!A12 | Educationb | None |
| eTable 3!H12 | 1.5599999999999999E-2 | None |
| eTable 3!J12 | 0.05 | None |
| eTable 3!A13 | High school degree or less | None |
| eTable 3!B13 | 627 (27.2) | None |
| eTable 3!C13 | 86 (29.5) | None |
| eTable 3!D13 | 146 (31.8) | None |
| eTable 3!E13 | 395 (25.4) | None |
| eTable 3!A14 | Associate's or Technical degree | None |
| eTable 3!B14 | 657 (28.5) | None |
| eTable 3!C14 | 100 (34.2) | None |
| eTable 3!D14 | 139 (30.3) | None |
| eTable 3!E14 | 418 (26.9) | None |
| eTable 3!A15 | College degree | None |
| eTable 3!B15 | 597 (25.9) | None |
| eTable 3!C15 | 64 (21.9) | None |
| eTable 3!D15 | 109 (23.7) | None |
| eTable 3!E15 | 424 (27.2) | None |
| eTable 3!A16 | Doctoral or Postgraduate degree | None |
| eTable 3!B16 | 426 (18.5) | None |
| eTable 3!C16 | 42 (14.4) | None |
| eTable 3!D16 | 65 (14.2) | None |
| eTable 3!E16 | 319 (20.5) | None |
| eTable 3!A17 | Missinga | None |
| eTable 3!B17 | 24 | None |
| eTable 3!C17 | 3 | None |
| eTable 3!D17 | 9 | None |
| eTable 3!E17 | 12 | None |
| eTable 3!A18 | Not employed,b N (%) | None |
| eTable 3!B18 | 1234 (53.4) | None |
| eTable 3!C18 | 135 (45.9) | None |
| eTable 3!D18 | 213 (46.3) | None |
| eTable 3!E18 | 886 (57) | None |
| eTable 3!H18 | <0.001 | None |
| eTable 3!I18 | 2.2800000000000001E-2 | None |
| eTable 3!J18 | 5.91E-2 | None |
| eTable 3!A19 | Missinga | None |
| eTable 3!B19 | 22 | None |
| eTable 3!C19 | 1 | None |
| eTable 3!D19 | 8 | None |
| eTable 3!E19 | 13 | None |
| eTable 3!A20 | Household income,b N (%) | None |
| eTable 3!H20 | 1.8599999999999998E-2 | None |
| eTable 3!A21 | less than $24,999 | None |
| eTable 3!B21 | 273 (13.7) | None |
| eTable 3!C21 | 40 (16.4) | None |
| eTable 3!D21 | 53 (13.7) | None |
| eTable 3!E21 | 180 (13.2) | None |
| eTable 3!A22 | $25,000--- $49,999 | None |
| eTable 3!B22 | 461 (23.1) | None |
| eTable 3!C22 | 65 (26.6) | None |
| eTable 3!D22 | 93 (24) | None |
| eTable 3!E22 | 303 (22.2) | None |
| eTable 3!A23 | $50,000--- $99,999 | None |
| eTable 3!B23 | 736 (36.9) | None |
| eTable 3!C23 | 86 (35.2) | None |
| eTable 3!D23 | 131 (33.9) | None |
| eTable 3!E23 | 519 (38) | None |
| eTable 3!A24 | $100,000--- $149,999 | None |
| eTable 3!B24 | 316 (15.8) | None |
| eTable 3!C24 | 29 (11.9) | None |
| eTable 3!D24 | 65 (16.8) | None |
| eTable 3!E24 | 222 (16.3) | None |
| eTable 3!A25 | 150000 or greater | None |
| eTable 3!B25 | 209 (10.5) | None |
| eTable 3!C25 | 24 (9.8) | None |
| eTable 3!D25 | 45 (11.6) | None |
| eTable 3!E25 | 140 (10.3) | None |
| eTable 3!A26 | Missinga | None |
| eTable 3!B26 | 336 (14.4) | None |
| eTable 3!C26 | 51 (17.3) | None |
| eTable 3!D26 | 81 (17.3) | None |
| eTable 3!E26 | 204 (13) | None |
| eTable 3!A27 | Married or domestic partnered,b N (%) | None |
| eTable 3!B27 | 1507 (65.5) | None |
| eTable 3!C27 | 181 (61.6) | None |
| eTable 3!D27 | 290 (63) | None |
| eTable 3!E27 | 1036 (67) | None |
| eTable 3!A28 | Missinga | None |
| eTable 3!B28 | 31 | None |
| eTable 3!C28 | 1 | None |
| eTable 3!D28 | 8 | None |
| eTable 3!E28 | 22 | None |
| eTable 3!A29 | Race and Ethnicity,b N(%) | None |
| eTable 3!A30 | White Non-Hispanic | None |
| eTable 3!B30 | 1699 (75) | None |
| eTable 3!C30 | 212 (74.1) | None |
| eTable 3!D30 | 313 (70.3) | None |
| eTable 3!E30 | 1174 (76.5) | None |
| eTable 3!A31 | Black or African American and Non-Hispanic | None |
| eTable 3!B31 | 350 (15.4) | None |
| eTable 3!C31 | 40 (14) | None |
| eTable 3!D31 | 96 (21.6) | None |
| eTable 3!E31 | 214 (13.9) | None |
| eTable 3!A32 | Hispanic | None |
| eTable 3!B32 | 77 (3.4) | None |
| eTable 3!C32 | 15 (5.2) | None |
| eTable 3!D32 | 13 (2.9) | None |
| eTable 3!E32 | 49 (3.2) | None |
| eTable 3!A33 | Asian | None |
| eTable 3!B33 | 27 (1.2) | None |
| eTable 3!C33 | 2 (0.7) | None |
| eTable 3!D33 | 4 (0.9) | None |
| eTable 3!E33 | 21 (1.4) | None |
| eTable 3!A34 | American Indian/ Alaska Native | None |
| eTable 3!B34 | 28 (1.2) | None |
| eTable 3!C34 | 7 (2.4) | None |
| eTable 3!D34 | 3 (0.7) | None |
| eTable 3!E34 | 18 (1.2) | None |
| eTable 3!A35 | Native Hawaiian or Other Pacific Islander | None |
| eTable 3!B35 | 2 (0.1) | None |
| eTable 3!C35 | 0 (0) | None |
| eTable 3!D35 | 2 (0.4) | None |
| eTable 3!E35 | 0 (0) | None |
| eTable 3!A36 | More than one Race | None |
| eTable 3!B36 | 83 (3.7) | None |
| eTable 3!C36 | 10 (3.5) | None |
| eTable 3!D36 | 14 (3.1) | None |
| eTable 3!E36 | 59 (3.8) | None |
| eTable 3!A37 | Missinga | None |
| eTable 3!B37 | 65 | None |
| eTable 3!C37 | 9 | None |
| eTable 3!D37 | 23 | None |
| eTable 3!E37 | 33 | None |
| eTable 3!A38 | Rural/medically underserved residency,c N (%) | None |
| eTable 3!B38 | 1030 (44.2) | None |
| eTable 3!C38 | 136 (46.1) | None |
| eTable 3!D38 | 204 (43.6) | None |
| eTable 3!E38 | 690 (44) | None |
| eTable 3!G38 | X | None |
| eTable 3!A39 | Any Negative Social Determinate of Health, N (%) | None |
| eTable 3!B39 | 758 (33) | None |
| eTable 3!C39 | 125 (42.7) | None |
| eTable 3!D39 | 174 (38.2) | None |
| eTable 3!E39 | 459 (29.6) | None |
| eTable 3!H39 | 6.3600000000000004E-2 | None |
| eTable 3!I39 | 1.9599999999999999E-2 | None |
| eTable 3!A40 | Missinga | None |
| eTable 3!B40 | 33 | None |
| eTable 3!C40 | 2 | None |
| eTable 3!D40 | 12 | None |
| eTable 3!E40 | 19 | None |
| eTable 3!A41 | Financial resource strain, N (%) | None |
| eTable 3!B41 | 567 (24.5) | None |
| eTable 3!C41 | 93 (31.6) | None |
| eTable 3!D41 | 130 (28.2) | None |
| eTable 3!E41 | 344 (22.1) | None |
| eTable 3!H41 | 5.2499999999999998E-2 | None |
| eTable 3!A42 | Missinga | None |
| eTable 3!B42 | 19 | None |
| eTable 3!C42 | 1 | None |
| eTable 3!D42 | 7 | None |
| eTable 3!E42 | 11 | None |
| eTable 3!A43 | Food insecurity, N (%) | None |
| eTable 3!B43 | 333 (14.4) | None |
| eTable 3!C43 | 59 (20.1) | None |
| eTable 3!D43 | 78 (17.0) | None |
| eTable 3!E43 | 196 (12.6) | None |
| eTable 3!H43 | 5.7599999999999998E-2 | None |
| eTable 3!A44 | Missinga | None |
| eTable 3!B44 | 21 | None |
| eTable 3!C44 | 2 | None |
| eTable 3!D44 | 8 | None |
| eTable 3!E44 | 11 | None |
| eTable 3!A45 | Transportation insecurity - activities of daily living, N (%) | None |
| eTable 3!B45 | 170 (7.3) | None |
| eTable 3!C45 | 29 (9.8) | None |
| eTable 3!D45 | 37 (7.9) | None |
| eTable 3!E45 | 104 (6.7) | None |
| eTable 3!H45 | 3.0800000000000001E-2 | None |
| eTable 3!A46 | Missinga | None |
| eTable 3!B46 | 12 | None |
| eTable 3!C46 | 0 | None |
| eTable 3!D46 | 2 | None |
| eTable 3!E46 | 10 | None |
| eTable 3!A47 | Housing insecurity, N (%) | None |
| eTable 3!B47 | 364 (15.9) | None |
| eTable 3!C47 | 75 (25.7) | None |
| eTable 3!D47 | 88 (19.3) | None |
| eTable 3!E47 | 201 (13.0) | None |
| eTable 3!I47 | 2.0000000000000001E-4 | None |
| eTable 3!A48 | Missinga | None |
| eTable 3!B48 | 35 | None |
| eTable 3!C48 | 3 | None |
| eTable 3!D48 | 12 | None |
| eTable 3!E48 | 20 | None |
| eTable 3!A49 | CLINICAL CHARACTERISTICS | None |
| eTable 3!A50 | Pain-related symptoms, conditions and treatment | None |
| eTable 3!A51 | Num. of pain-related encounters in past year,c mean (sd) | None |
| eTable 3!B51 | 9.3 (9.4) | None |
| eTable 3!C51 | 7.3 (7) | None |
| eTable 3!D51 | 9.8 (10.8) | None |
| eTable 3!E51 | 9.5 (9.3) | None |
| eTable 3!I51 | 1E-3 | None |
| eTable 3!A52 | Musculoskeletal pain conditions in past yearc | None |
| eTable 3!H52 | 7.4099999999999999E-2 | None |
| eTable 3!A53 | mean (sd) | None |
| eTable 3!B53 | 2.5 (1.3) | None |
| eTable 3!C53 | 2.5 (1.3) | None |
| eTable 3!D53 | 2.5 (1.3) | None |
| eTable 3!E53 | 2.5 (1.3) | None |
| eTable 3!A54 | >1, N (%) | None |
| eTable 3!B54 | 1710 (73.4) | None |
| eTable 3!C54 | 213 (72.2) | None |
| eTable 3!D54 | 353 (75.4) | None |
| eTable 3!E54 | 1144 (73) | None |
| eTable 3!G54 | X | None |
| eTable 3!H54 | 5.1000000000000004E-3 | None |
| eTable 3!A55 | Long-Term Opioid Use,c N (%) | None |
| eTable 3!B55 | 163 (9.6) | None |
| eTable 3!C55 | 14 (8.2) | None |
| eTable 3!D55 | 31 (9.1) | None |
| eTable 3!E55 | 118 (10) | None |
| eTable 3!A56 | Missinga (Data only available for 3 of 4 sites) | None |
| eTable 3!B56 | 634 | None |
| eTable 3!C56 | 124 | None |
| eTable 3!D56 | 126 | None |
| eTable 3!E56 | 384 | None |
| eTable 3!A57 | Specific pain condition bothered a lot in the last 3 months | None |
| eTable 3!A58 | Back pain, N (%) | None |
| eTable 3!B58 | 1225 (52.6) | None |
| eTable 3!C58 | 162 (54.9) | None |
| eTable 3!D58 | 258 (55.1) | None |
| eTable 3!E58 | 805 (51.4) | None |
| eTable 3!H58 | 6.1499999999999999E-2 | None |
| eTable 3!A59 | Missinga | None |
| eTable 3!B59 | 2 | None |
| eTable 3!C59 | 0 | None |
| eTable 3!D59 | 0 | None |
| eTable 3!E59 | 2 | None |
| eTable 3!A60 | Neck pain, N (%) | None |
| eTable 3!B60 | 622 (26.7) | None |
| eTable 3!C60 | 83 (28.1) | None |
| eTable 3!D60 | 126 (26.9) | None |
| eTable 3!E60 | 413 (26.3) | None |
| eTable 3!H60 | 1.6999999999999999E-3 | None |
| eTable 3!A61 | Missinga | None |
| eTable 3!A62 | Hand, arm, or shoulder pain, N (%) | None |
| eTable 3!B62 | 883 (37.9) | None |
| eTable 3!C62 | 120 (40.7) | None |
| eTable 3!D62 | 176 (37.7) | None |
| eTable 3!E62 | 587 (37.5) | None |
| eTable 3!A63 | Missinga | None |
| eTable 3!B63 | 2 | None |
| eTable 3!C63 | 0 | None |
| eTable 3!D63 | 1 | None |
| eTable 3!E63 | 1 | None |
| eTable 3!A64 | Hip, knee, or foot pain, N (%) | None |
| eTable 3!B64 | 1476 (63.3) | None |
| eTable 3!C64 | 176 (59.7) | None |
| eTable 3!D64 | 303 (64.7) | None |
| eTable 3!E64 | 997 (63.6) | None |
| eTable 3!A65 | Missinga | None |
| eTable 3!B65 | 0 | None |
| eTable 3!C65 | 0 | None |
| eTable 3!A66 | Headache or migraine, N (%) | None |
| eTable 3!B66 | 343 (14.7) | None |
| eTable 3!C66 | 56 (19) | None |
| eTable 3!D66 | 72 (15.4) | None |
| eTable 3!E66 | 215 (13.7) | None |
| eTable 3!H66 | 3.2300000000000002E-2 | None |
| eTable 3!A67 | Missinga | None |
| eTable 3!B67 | 1 | None |
| eTable 3!C67 | 0 | None |
| eTable 3!D67 | 0 | None |
| eTable 3!E67 | 1 | None |
| eTable 3!A68 | Abdominal, pelvic, or genital pain, N (%) | None |
| eTable 3!B68 | 197 (8.5) | None |
| eTable 3!C68 | 19 (6.4) | None |
| eTable 3!D68 | 39 (8.4) | None |
| eTable 3!E68 | 139 (8.9) | None |
| eTable 3!H68 | 0.01 | None |
| eTable 3!A69 | Missinga | None |
| eTable 3!B69 | 4 | None |
| eTable 3!C69 | 0 | None |
| eTable 3!D69 | 1 | None |
| eTable 3!E69 | 3 | None |
| eTable 3!A70 | Toothache or jaw pain, N (%) | None |
| eTable 3!B70 | 143 (6.1) | None |
| eTable 3!C70 | 18 (6.1) | None |
| eTable 3!D70 | 28 (6) | None |
| eTable 3!E70 | 97 (6.2) | None |
| eTable 3!A71 | Missinga | None |
| eTable 3!B71 | 1 | None |
| eTable 3!C71 | 1 | None |
| eTable 3!D71 | 0 | None |
| eTable 3!E71 | 0 | None |
| eTable 3!A72 | Whole body pain, N (%) | None |
| eTable 3!B72 | 460 (19.8) | None |
| eTable 3!C72 | 60 (20.4) | None |
| eTable 3!D72 | 104 (22.3) | None |
| eTable 3!E72 | 296 (18.9) | None |
| eTable 3!H72 | <0.001 | None |
| eTable 3!A73 | Missinga | None |
| eTable 3!B73 | 4 | None |
| eTable 3!C73 | 1 | None |
| eTable 3!D73 | 1 | None |
| eTable 3!E73 | 2 | None |
| eTable 3!A74 | Pain Duration in yearsb, N(%) | None |
| eTable 3!H74 | <0.001 | None |
| eTable 3!A75 | ≤1 yr | None |
| eTable 3!B75 | 107 (4.6) | None |
| eTable 3!C75 | 16 (5.4) | None |
| eTable 3!D75 | 21 (4.5) | None |
| eTable 3!E75 | 70 (4.5) | None |
| eTable 3!A76 | >1-5 yrs | None |
| eTable 3!B76 | 614 (26.4) | None |
| eTable 3!C76 | 84 (28.5) | None |
| eTable 3!D76 | 123 (26.3) | None |
| eTable 3!E76 | 407 (26) | None |
| eTable 3!A77 | >5 yrs | None |
| eTable 3!B77 | 1609 (69.1) | None |
| eTable 3!C77 | 195 (66.1) | None |
| eTable 3!D77 | 324 (69.2) | None |
| eTable 3!E77 | 1090 (69.6) | None |
| eTable 3!A78 | Missinga | None |
| eTable 3!B78 | 1 | None |
| eTable 3!C78 | 0 | None |
| eTable 3!D78 | 0 | None |
| eTable 3!E78 | 1 | None |
| eTable 3!A79 | Related health conditions | None |
| eTable 3!A80 | Anxiety or depression diagnosis,c N (%) | None |
| eTable 3!B80 | 965 (41.4) | None |
| eTable 3!C80 | 141 (47.8) | None |
| eTable 3!D80 | 209 (44.7) | None |
| eTable 3!E80 | 615 (39.2) | None |
| eTable 3!G80 | X | None |
| eTable 3!A81 | Depression PHQ-8 (0-24),b mean (sd) | None |
| eTable 3!B81 | 9.8 (5.6) | None |
| eTable 3!C81 | 11 (5.5) | None |
| eTable 3!D81 | 10.3 (5.8) | None |
| eTable 3!E81 | 9.5 (5.5) | None |
| eTable 3!H81 | <0.001 | None |
| eTable 3!I81 | 9.4999999999999998E-3 | None |
| eTable 3!A82 | Current depression (PHQ-8 ≥10),c No. (%) | None |
| eTable 3!B82 | 1116 (47.9) | None |
| eTable 3!C82 | 162 (54.9) | None |
| eTable 3!D82 | 243 (51.9) | None |
| eTable 3!E82 | 711 (73.2) | None |
| eTable 3!A83 | Missinga | None |
| eTable 3!B83 | 2 | None |
| eTable 3!C83 | 0 | None |
| eTable 3!D83 | 0 | None |
| eTable 3!E83 | 2 | None |
| eTable 3!A84 | Anxiety GAD-7 (0-21),b mean (sd) | None |
| eTable 3!B84 | 6.9 (5.4) | None |
| eTable 3!C84 | 7.9 (5.3) | None |
| eTable 3!D84 | 7 (5.2) | None |
| eTable 3!E84 | 6.7 (5.4) | None |
| eTable 3!H84 | 3.27E-2 | None |
| eTable 3!I84 | 3.3099999999999997E-2 | None |
| eTable 3!A85 | Moderate to severe anxiety (GAD-7 ≥10),c No. (%) | None |
| eTable 3!B85 | 648 (27.8) | None |
| eTable 3!C85 | 102 (34.6) | None |
| eTable 3!D85 | 126 (27.0) | None |
| eTable 3!E85 | 420 (26.8) | None |
| eTable 3!A86 | Missinga | None |
| eTable 3!B86 | 2 | None |
| eTable 3!C86 | 0 | None |
| eTable 3!D86 | 2 | None |
| eTable 3!E86 | 0 | None |
| eTable 3!A87 | Substance use disorder diagnosis,c N (%) | None |
| eTable 3!B87 | 86 (3.7) | None |
| eTable 3!C87 | 16 (5.4) | None |
| eTable 3!D87 | 22 (4.7) | None |
| eTable 3!E87 | 48 (3.1) | None |
| eTable 3!H87 | 1.0800000000000001E-2 | None |
| eTable 3!A88 | Charlson Comorbidity Index,c mean (sd) | None |
| eTable 3!B88 | 1.2 (1.7) | None |
| eTable 3!C88 | 1 (1.6) | None |
| eTable 3!D88 | 1.3 (1.9) | None |
| eTable 3!E88 | 1.1 (1.6) | None |
| eTable 3!A89 | 0 conditions, N (%) | None |
| eTable 3!B89 | 1162 (49.8) | None |
| eTable 3!C89 | 156 (52.9) | None |
| eTable 3!D89 | 225 (48.1) | None |
| eTable 3!E89 | 781 (49.8) | None |
| eTable 3!A90 | 1-2 conditions, N (%) | None |
| eTable 3!B90 | 812 (34.8) | None |
| eTable 3!C90 | 95 (32.2) | None |
| eTable 3!D90 | 160 (34.2) | None |
| eTable 3!E90 | 557 (35.5) | None |
| eTable 3!A91 | ≥ 3, N (%) | None |
| eTable 3!B91 | 357 (15.3) | None |
| eTable 3!C91 | 44 (14.9) | None |
| eTable 3!D91 | 83 (17.7) | None |
| eTable 3!E91 | 230 (14.7) | None |
| eTable 3!A92 | PROMIS Sleep Disturbance,b mean (sd) | None |
| eTable 3!B92 | 58.8 (8.3) | None |
| eTable 3!C92 | 59.2 (9) | None |
| eTable 3!D92 | 59.4 (8) | None |
| eTable 3!E92 | 58.5 (8.2) | None |
| eTable 3!A93 | Moderate to severe sleep disturbance (PROMIS® Sleep Disturbance T-score >60),c N. (%) | None |
| eTable 3!B93 | 1005 (43.3) | None |
| eTable 3!C93 | 136 (46.4) | None |
| eTable 3!D93 | 221 (47.6) | None |
| eTable 3!E93 | 648 (41.5) | None |
| eTable 3!A94 | Missinga | None |
| eTable 3!B94 | 12 | None |
| eTable 3!C94 | 2 | None |
| eTable 3!D94 | 4 | None |
| eTable 3!E94 | 6 | None |
| eTable 3!A95 | BASELINE PRIMARY OUTCOME | None |
| eTable 3!A96 | Pain Severity (0-10)b | None |
| eTable 3!A97 | mean (sd) | None |
| eTable 3!B97 | 5.9 (1.7) | None |
| eTable 3!C97 | 6 (1.7) | None |
| eTable 3!D97 | 6.1 (1.7) | None |
| eTable 3!E97 | 5.8 (1.6) | None |
| eTable 3!A98 | ≥7 score, N (%) | None |
| eTable 3!B98 | 594 (25.5) | None |
| eTable 3!C98 | 89 (30.2) | None |
| eTable 3!D98 | 147 (31.4) | None |
| eTable 3!E98 | 358 (22.8) | None |
| eTable 3!A99 | BASELINE SECONDARY OUTCOMES | None |
| eTable 3!A100 | Pain Intensity (0-10),b mean (sd) | None |
| eTable 3!B100 | 5.5 (1.6) | None |
| eTable 3!C100 | 5.7 (1.7) | None |
| eTable 3!D100 | 5.7 (1.6) | None |
| eTable 3!E100 | 5.4 (1.6) | None |
| eTable 3!H100 | 4.9200000000000001E-2 | None |
| eTable 3!A101 | Pain-related interference (0-10),b mean (sd) | None |
| eTable 3!B101 | 6.1 (1.9) | None |
| eTable 3!C101 | 6.2 (1.9) | None |
| eTable 3!D101 | 6.3 (2) | None |
| eTable 3!E101 | 6 (1.9) | None |
| eTable 3!H101 | 4.9200000000000001E-2 | None |
| eTable 3!A102 | PROMIS Social role functioning, mean (sd) | None |
| eTable 3!B102 | 42.5 (7.4) | None |
| eTable 3!C102 | 41.8 (7.6) | None |
| eTable 3!D102 | 42.1 (7.7) | None |
| eTable 3!E102 | 42.7 (7.3) | None |
| eTable 3!H102 | <.0001 | None |
| eTable 3!A103 | PROMIS Social role functioning ≤40,b mean (sd) | None |
| eTable 3!B103 | 818 (35.7) | None |
| eTable 3!C103 | 113 (38.8) | None |
| eTable 3!D103 | 180 (38.7) | None |
| eTable 3!E103 | 525 (34.2) | None |
| eTable 3!A104 | Missinga | None |
| eTable 3!B104 | 38 | None |
| eTable 3!C104 | 4 | None |
| eTable 3!D104 | 3 | None |
| eTable 3!E104 | 31 | None |
| eTable 3!A105 | PROMIS Physical functioning,b mean (sd) | None |
| eTable 3!B105 | 36.6 (5.9) | None |
| eTable 3!C105 | 36.8 (6.2) | None |
| eTable 3!D105 | 35.9 (6.1) | None |
| eTable 3!E105 | 36.7 (5.8) | None |
| eTable 3!H105 | <.0001 | None |
| eTable 3!A106 | PROMIS Physical functioning ≤40,b mean (sd) | None |
| eTable 3!B106 | 1709 (74.1) | None |
| eTable 3!C106 | 209 (72.6) | None |
| eTable 3!D106 | 357 (76.8) | None |
| eTable 3!E106 | 1143 (73.6) | None |
| eTable 3!A107 | Missinga | None |
| eTable 3!B107 | 24 | None |
| eTable 3!C107 | 7 | None |
| eTable 3!D107 | 3 | None |
| eTable 3!E107 | 14 | None |
| eTable 3!A108 | PEG (0-30),b mean (sd) | None |
| eTable 3!B108 | 20.5 (4.4) | None |
| eTable 3!C108 | 21 (4.5) | None |
| eTable 3!D108 | 21.2 (4.5) | None |
| eTable 3!E108 | 20.2 (4.4) | None |
| eTable 3!H108 | 2.4500000000000001E-2 | None |
| eTable 3!I108 | 4.0500000000000001E-2 | None |
| eTable 3!A109 | Missinga | None |
| eTable 3!B109 | 1 | None |
| eTable 3!C109 | 0 | None |
| eTable 3!D109 | 0 | None |
| eTable 3!E109 | 1 | None |
| eTable 3!A110 | a Missing is reported as n but excluded from the denominator in the % reported | None |
| eTable 3!A111 | b HEAL common data element | None |
| eTable 3!A112 | c Derived from the electronic health record (EHR) | None |
| eTable 3!A113 | * Note for sex used self-reported sex unless sex was missing and used then used EHR sex.  | None |
| eTable 3!A114 | Bold indicates that a variable is related (e.g., P<0.10) to both the primary outcome MCID on pain severity at 3 months (after adjusting for pre-specified covariates) and missingness of the outcome at either 3 months or all time points (after adjusting for pre-specified covariates) | None |

## Limits and closure

All27 assigned units mapped. No scientific coverage gap. Histograms contain unnumbered graphical bars, so no exact counts or bin-height values are invented; axis labels, all panels, group legends, complete rendered shapes and printed numerical summaries have been inspected and mapped. Legacy rendering versions are unconfirmed. Full exact cell transcription preserves stored values rather than inferring number formatting. Formatting-bold selection is defined byA114 but not represented in retained JSON; numerical P values and selection definitions are completely retained. Candidate diagnoses and screening decisions are outside this mapper stage. PLAN evidence will be appended by the coordinator from disjoint completed parts.
