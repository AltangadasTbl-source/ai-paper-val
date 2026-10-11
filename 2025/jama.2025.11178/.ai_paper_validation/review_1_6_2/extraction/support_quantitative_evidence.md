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

Source: [DOC-004 p1](../../../joi250046supp3_prod_1755300121.15087.pdf#page=1). Mapped: Cover; no applicable numeric result.

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

Source: [DOC-004 p2](../../../joi250046supp3_prod_1755300121.15087.pdf#page=2). Mapped: R001–R002 materials and intervention.

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

Source: [DOC-004 p3](../../../joi250046supp3_prod_1755300121.15087.pdf#page=3). Mapped: R001–R003 provider/training/dose.

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

Source: [DOC-004 p4](../../../joi250046supp3_prod_1755300121.15087.pdf#page=4). Mapped: R001–R004 schedule/outreach.

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

Source: [DOC-004 p5](../../../joi250046supp3_prod_1755300121.15087.pdf#page=5). Mapped: R003–R005 modification and fidelity.

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

Source: [DOC-004 p6](../../../joi250046supp3_prod_1755300121.15087.pdf#page=6). Mapped: R003 actual fidelity.

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

Source: [DOC-004 p7](../../../joi250046supp3_prod_1755300121.15087.pdf#page=7). Mapped: References; no applicable trial numeric result.

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

Source: [DOC-005 p1](../../../joi250046supp4_prod_1755300121.15587.pdf#page=1). Mapped: Cover and full contents; no applicable result.

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

Source: [DOC-005 p2](../../../joi250046supp4_prod_1755300121.15587.pdf#page=2). Mapped: R006 outcome measures.

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

Source: [DOC-005 p3](../../../joi250046supp4_prod_1755300121.15587.pdf#page=3). Mapped: R007 complete adherence figure.

```text
INTERVENTION ADHERENCE
eFigure 1. Histogram of Number of Sessions completed for those randomized to
painTRAINER and those randomized to the Virtual Health Coach




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 4

Source: [DOC-005 p4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4). Mapped: R008–R010 missingness and imputation.

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

Source: [DOC-005 p5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5). Mapped: R009–R012 models and weights.

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

Source: [DOC-005 p6](../../../joi250046supp4_prod_1755300121.15587.pdf#page=6). Mapped: R012 weighting continuation.

```text
estimation model described in the imputation section (step 2). The fitted weight model is presented in eTable 5, and
eTable 6 and eFigure 1 provide summaries of the predicted probabilities and corresponding weights.




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

### DOC-005 physical PDF page 7

Source: [DOC-005 p7](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7). Mapped: R009,R013 complete eTables1–2.

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

Source: [DOC-005 p8](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8). Mapped: R014 complete eTable3.

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

Source: [DOC-005 p9](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9). Mapped: R015 complete eTable4.

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

Source: [DOC-005 p10](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10). Mapped: R016–R018 complete eTables5–6/eFigure2.

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

Source: [DOC-005 p11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11). Mapped: R019–R020 complete eTable7.

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

Source: [DOC-005 p12](../../../joi250046supp4_prod_1755300121.15587.pdf#page=12). Mapped: Footer-only; visually confirmed no applicable content.

```text
© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.
```

### DOC-005 physical PDF page 13

Source: [DOC-005 p13](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13). Mapped: R005,R021 subset definitions.

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

Source: [DOC-005 p14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14). Mapped: R020–R021 complete eTable8.

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

Source: [DOC-005 p15](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15). Mapped: R022 complete eTable9.

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

Source: [DOC-005 p16](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16). Mapped: R023 complete eTable10.

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

Source: [DOC-005 p17](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17). Mapped: R024 complete eTable11.

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

Source: [DOC-005 p18](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18). Mapped: R024 eTable11 footnote continuation.

```text
a Primary timepoint; b Unadjusted between group mean differences and 95% confidence intervals were calculated using linear regression model fit using generalized estimating equations (GEE) for

each continuous outcome.




       © 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
       technologies.
```

### DOC-005 physical PDF page 19

Source: [DOC-005 p19](../../../joi250046supp4_prod_1755300121.15587.pdf#page=19). Mapped: References; no applicable trial numeric result.

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

Source: [Results workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx), worksheet **eTable 3**, exact cells in the table below. All525 nonempty cells follow; dimensionA1:J115 includes blank cells which carry no value. ColumnsF and blank cells inG–J are not zeroP values. Stored numeric strings retain their full precision and scientific notation. Numeric cells are literal values, not computed formula caches; text strings embed displayed counts/percentages or means/SD. Zero formula cells; zero formula-derived caches; no recalculation.

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
# DOC-002 protocol evidence, physical PDF pages 1–32

Document role: PLAN. Exact source: joi250046supp1_prod_1755300121.14087.pdf. This disjoint mapping contains local P-A keys, not findings or adjudications. Every assigned physical page is opened through readable OCR and targeted visual inspection; the schedule table was transcribed directly from its rendered page because rotated header OCR was unusable. Source quotations below preserve numbers and planned status; OCR is a locator/transcription aid.

## Engines and derivative provenance

Compute device: CPU. Pages 1–20 use curator-inventoried, hashed reusable rendered images `.ai_paper_validation/review_1_5_1/preprocessing/doc002_render/pNNN.png`; fresh readable OCR is retained in `.ai_paper_validation/review_1_6_2/preprocessing/protocol_a/pNNN.txt`. Pages 21–32 receive direct Poppler pdftotext native and layout extraction (`pNNN.native.txt`, `pNNN.layout.txt`) and CPU Poppler pdftoppm PNG rendering at 160 dpi (`pNNN.png`), followed by Tesseract 5.5.0 English OCR with `OMP_THREAD_LIMIT=1 --psm 3` (`pNNN.txt`). Poppler version 26.01.0. Native/layout for this source is font-encoding-corrupted and is retained as an extraction record, not used for scientific prose. The source and reused images remain unchanged. No workbook, formula, cached value, or CSV exists in this assigned scope.

## Planned relationships and source transcriptions

### P-A01 — Plan identity and chronology

[Physical page 1](../../../joi250046supp1_prod_1755300121.14087.pdf#page=1): “Version Number: 5.0”; “10 November 2022”; “ClinicalTrials.gov Protocol Identifier: NCT04523714.” The bundle identifies itself as UH3 STUDY PROTOCOL. Every substantive current page repeats version 5.0, 10 Nov 2022. This is a plan version and not a results report.

### P-A02 — Amendments affecting quantitative design

[Page 3](../../../joi250046supp1_prod_1755300121.14087.pdf#page=3), dated 07/15/20: phase III designation and additional age/race-ethnicity subgroup analyses, located in sections 3.4 and 15.7. Dated 08/06/20: modified BPI-SF changed from 10 to 11 items and pain intensity subscale from 3 to 4 items; randomization sex stratum moved from baseline self-report to EHR. Dated 09/25/20: 3-month collection window 80–140 days (formerly 75–110), 6-month 170–230 (formerly 165–200), 12-month 350–410 (formerly 345–480); maximum active intervention duration 12 weeks. Same date: added MCID assessment for pain-intensity and pain-interference subscales to secondary outcomes/analyses; added rural/medically underserved residence to randomization strata and primary-model adjustment.

[Page 5](../../../joi250046supp1_prod_1755300121.14087.pdf#page=5), dated 03/31/21: KP inclusion criterion now ≥2 pain-related encounters ≥30 days apart; Essentia remains ≥1 encounter. Added exclusion for surgery in preceding 60 days and planned surgery in next year. Dated 02/24/22: online painTRAINER described as CBT-based; printed old and revised Aim #1 both retain clinically meaningful improvement in composite pain severity at 3 months.

[Page 6](../../../joi250046supp1_prod_1755300121.14087.pdf#page=6), dated 02/24/22: active interventions described independently rather than coach intervention derived from painTRAINER; onboarding/outreach descriptions added. Every 2,380-enrollment target gained qualification that consent/enrollment may need to exceed 2,380 to achieve 2,331 randomized.

[Page 7](../../../joi250046supp1_prod_1755300121.14087.pdf#page=7), dated 11/10/22: enrollment target changed from 2,380 to approximately 2,500; site totals may vary (range 595–625) to achieve overall randomized target. Randomized target clarified as “at least 2,331 or 777 per arm.” Enrollment expansion at Essentia and KPGA approved via NIA/JHU email 10/31/22. Qualitative stakeholder interviews up to 2, years 4–5 rather than years 2–3; administrative/qualitative context, not a clinical inferential result.

### P-A03 — Trial arms, populations, intervention and time axis

[Pages 13–15](../../../joi250046supp1_prod_1755300121.14087.pdf#page=13), synopsis: 3-arm parallel comparative effectiveness design; online self-directed painTRAINER and live coach-led telephone/video intervention each compared with usual care. “8 CBT-based sessions” approximately weekly. Usual care receives a chronic pain education/resource manual. All participants enrolled for 12 months; self-reported assessments baseline, notification of randomization, 3, 6, 12 months. Goal approximately 2,331 randomized, at least 777/arm; approximately 2,500 enrolled, potentially more to achieve randomized target. Four health systems. Both active modalities have analogous pain coping skills content and eight expected weekly sessions. “All enrollees can receive any pharmacologic and nonpharmacologic treatments available to them without restriction.” Qualitative subset 120 randomized participants; interviews approximately 3–5 and 12–14 months, 20 healthcare stakeholders, approximately 12 intervention staff. Study duration 48 months; enrollment 25 months; majority subject duration 12 months, qualitative subjects 12–14.

Matching main-paper keys for subsequent comparison: three-arm randomized allocation; online/coach/usual-care contrasts; intervention 8 sessions over up to 12 weeks; randomized/analysis population; high-impact chronic pain; BPI composite response at 3 months; follow-up 6 and 12 months.

### P-A04 — Schedule table and windows (visual transcription)

[Page 16](../../../joi250046supp1_prod_1755300121.14087.pdf#page=16), Table 1: screening/consent day −14 to −1 or day 0; baseline/randomization day 0; notification approximately days 1–7. Sessions #1–#8 approximately days 8–14, 15–21, 22–28, 29–35, 36–42, 43–49, 50–56, 57–63. Follow-ups: 3 months days 80–140; 6 months days 170–230; 12 months/final days 350–410. Baseline assessment and randomization at day 0; notification assessment days 1–7; study assessments baseline, notification, 3, 6, 12 months. Adverse-event review runs from notification to final follow-up. Qualitative interviews shown at 3- and 12-month columns. Footnote 1 allows screening, consent, baseline in same phone/online encounter and otherwise aims completion within 14 days of screening. Footnote 2: “The maximum duration for active intervention sessions is 12 weeks”; sessions intended weekly over 8 weeks, with variation due to participant circumstances.

### P-A05 — Population and aim definitions

[Pages 17–18](../../../joi250046supp1_prod_1755300121.14087.pdf#page=17): chronic pain ≥3 months; high-impact chronic pain ≥3 months plus at least one major activity restriction (work outside home, school, household chores). Background prevalence about one in ten adults, not a trial outcome. Conventional CBT background duration 50 minutes or more weekly over 2–3 months is historical context, not assigned intervention dosing. Rationale compares both scalable treatment modalities with usual care.

### P-A06 — Primary endpoint status, threshold and direction

[Page 19](../../../joi250046supp1_prod_1755300121.14087.pdf#page=19), Aim #1: “clinically meaningful improvements (≥ 30%)” in pain severity (pain intensity + pain-related interference), active interventions relative to usual care at 3 months. [Page 22](../../../joi250046supp1_prod_1755300121.14087.pdf#page=22), section 3.1: higher proportion achieving MCID; MCID “30% decrease in score on modified 11-item version” of BPI-SF from baseline, binary yes/no, self-reported baseline and 3 months. Reduced score means improvement; two active versus usual-care contrasts. No formula for item aggregation or missing items appears in assigned pages.

### P-A07 — Full secondary outcome table, including printed time labels

[Pages 22–23](../../../joi250046supp1_prod_1755300121.14087.pdf#page=22), section 3.2 explicitly headed Secondary Objectives. Preserve its endpoint status separately from the time-frame labels “Primary” (baseline–3 months) and “Secondary” (baseline–6 and 12 months).

| Planned secondary endpoint | Measure/type | Printed measurement occasions | Printed time-frame cell |
|---|---|---|---|
| Composite pain-severity MCID at 6 and 12 months | Same 11-item BPI-SF threshold as primary; binary | Baseline, 6, 12 months | Baseline–6 and 12 months |
| Pain-intensity MCID | 30% decrease from baseline; 4-item BPI-SF intensity; binary | Baseline, 6, 12 months | Primary: baseline–3; Secondary: baseline–6,12 |
| Pain-interference MCID | 30% decrease; 7-item BPI-SF interference; binary | Baseline, 6, 12 months | Primary: baseline–3; Secondary: baseline–6,12 |
| Pain severity continuous | BPI-SF 11 items | Baseline, 3, 6, 12 | Primary baseline–3; Secondary baseline–6,12 |
| Pain intensity continuous | BPI-SF 4 items | Baseline, 3, 6, 12 | Primary baseline–3; Secondary baseline–6,12 |
| Pain interference continuous | BPI-SF 7 items | Baseline, 3, 6, 12 | Primary baseline–3; Secondary baseline–6,12 |
| Social-role functioning | PROMIS Ability to Participate in Social Roles 4A, 4 items, continuous | Baseline, 3, 6, 12 | Primary baseline–3; Secondary baseline–6,12 |
| Physical functioning | PROMIS Physical Functioning Short Form 6b, 6 items, continuous | Baseline, 3, 6, 12 | Primary baseline–3; Secondary baseline–6,12 |
| Patient global impression of change | Guy/Farrar PGIC, 1 item each for pain status and overall status | 3, 6, 12 | Primary baseline–3; Secondary baseline–6,12 |

Literal transcription of the pain-interference row's description includes “MCID in pain intensity” while naming the 7-item “pain-related interference subscale.” This transcription records both printed phrases without diagnosing them. Image confirmed the MCID-subscale rows' measurement-occasion cells omit 3 months while time-frame cells include it. Matching report keys: primary composite responder; intensity/interference responder; continuous BPI composite and subscales; social/physical function; pain/overall PGIC; outcome hierarchy and time point.

### P-A08 — Economic outcomes

[Page 24](../../../joi250046supp1_prod_1755300121.14087.pdf#page=24), section 3.3: active interventions versus each other and usual care; healthcare utilization and intervention costs; incremental cost per additional patient with 30% MCID pain-severity reduction at 12 months; QALY gained from EQ-5D-5L utilities. Utilization from EHR with standard costing algorithms and Medicare fee schedules; intervention delivery resource/process data; EQ-5D-5L baseline, 3, 6, 12 months; economic horizon baseline–12 months. Matching keys: economic versus clinical outcome status, 12-month pain responder and EQ-5D-5L.

### P-A09 — Exploratory (tertiary) endpoints and EHR windows

[Page 25](../../../joi250046supp1_prod_1755300121.14087.pdf#page=25), section 3.4 explicitly “Exploratory (Tertiary) Objectives.” All compare impact of active interventions; stated horizons baseline–3,6,12 months.

| Planned exploratory endpoint | Definition/type | Source/time |
|---|---|---|
| Long-term opioid use | Prescription orders/fills indicating continuous ≥60-day supply in prior 90 days; prescriptions before look-back carried forward into assessment period; binary | EHR quarterly: baseline days −89 to −0; 3 months 1–90; 6 months 91–180; 9 months 181–270; 12 months 271–360, relative to baseline survey day0 |
| Depression | PHQ-8, 8 items, continuous | Self-report baseline,3,6,12 |
| Anxiety | GAD-7, 7 items, continuous | Self-report baseline,3,6,12 |
| Sleep disturbance | PROMIS Sleep Disturbance Short Form6a, 6 items, continuous | Self-report baseline,3,6,12 |
| High-impact chronic pain and graded chronic pain | High Impact Chronic Pain; Graded Chronic Pain Scale–Revised; reported pain intensity/duration/disability | Self-report baseline,3,6,12 |

This hierarchy is retained for comparison with reported secondary/exploratory/safety designations; no report designation inferred here.

### P-A10 — Prespecified moderators and 6-month target

[Pages 25–26](../../../joi250046supp1_prod_1755300121.14087.pdf#page=25): “The following moderators will be assessed related to MCID in pain severity at 6 months.”

| Moderator | Exact groups/definition | Data source |
|---|---|---|
| Sex | Male vs Female/Other; sex at birth HEAL CDE | Baseline self-report |
| Age | <65 vs ≥65 years | EHR |
| Race/ethnicity | White/non-Hispanic; Black or African American/non-Hispanic; Hispanic; Other | Baseline self-report |
| Rural/medically underserved | Urban vs rural/medically underserved; rural resident Census Tract RUCA codes4,5,6,7,8,9,10; medically underserved HRSA primary-care or mental-health geographic/high-needs HPSA | Baseline geocoded EHR |
| Multiple nonmalignant musculoskeletal pain conditions | 1 pain cluster vs >1 cluster; >1 ICD-10 diagnosis corresponding to >1 cluster | Prior360-day EHR |
| Mental-health mood disorder | Depression and/or anxiety ICD-10 diagnosis | Prior360-day EHR |
| Negative social determinants | Existing need vs no need; ≥1 of financial strain(1item), food insecurity(2), transportation/access(2), housing instability(3) | Baseline self-report |

Eight pain clusters are back, neck, limb/extremity/joint/arthritic, fibromyalgia, headache, orofacial/ear/temporomandibular, musculoskeletal chest, and general-pain subcategory of Other painful conditions. Exact patient sex source here is self-report; randomization stratum source below is EHR, retained separately. No interaction model, test alpha or multiplicity rule appears in these assigned pages.

### P-A11 — Mediators and timing

[Page 27](../../../joi250046supp1_prod_1755300121.14087.pdf#page=27): mediators assessed for “MCID in pain severity at 6 months.” Pain catastrophizing: PCS Short Form6, 6 items continuous, baseline/3-month self-report. Pain self-efficacy: Chronic Pain Self-Efficacy Scale pain-management subscale, 5 items continuous, baseline/3-month self-report. Perceived support: 2 UG3-developed items, notification-of-randomization/3-month self-report. These are mediation targets/timings, distinct from primary endpoint at3 months.

### P-A12 — Qualitative sample context and intervention discontinuation

[Pages 27–28](../../../joi250046supp1_prod_1755300121.14087.pdf#page=27): purposeful active-arm sample stratified by site, online/coach arm, response, rural/underserved residency; patient interviews3–5 and12–14 months. Health-system stakeholders years4–5; participant early interviews years1–3 and later years2–3; staff interviews years1 and3. Patients not completing active interventions are explicitly “still enrolled in the study.” These definitions can distinguish intervention completion from enrollment/analysis exclusions; no quantitative clinical analysis rule is specified here.

### P-A13 — Allocation unit, ratio, strata, blocks

[Page 29](../../../joi250046supp1_prod_1755300121.14087.pdf#page=29), section4.3: individual randomization after baseline collection; “equal ratio” across3 arms (1:1:1). Strata: EHR sex Male vs Female/Other; baseline BPI-SF score <7 vs ≥7; clinical site KPWA/KPNW/KPGA/Essentia; rural/medically underserved residency via EHR Census-Tract geocode. Within each stratum, random permuted variable block sizes3,6,9 for approximately equal accrual. [Page30](../../../joi250046supp1_prod_1755300121.14087.pdf#page=30): randomization in KPCHR-hosted electronic system after baseline completion. Matching report keys: unit/ratio, four strata, allocation concealment/block structure, primary-model adjustment factors. No outcome model specified in assigned pages.

### P-A14 — Historical intervention data, distinct from trial results

[Page30](../../../joi250046supp1_prod_1755300121.14087.pdf#page=30): prior painTRAINER feasibility self-efficacy effect size d=0.43 and pain effect in women d=0.33; mean age68 range38–90;35% African American;29% high-school or less;93% easy-to-use agreement;91% completed8 sessions. [Page31](../../../joi250046supp1_prod_1755300121.14087.pdf#page=31): prior442-patient telephonic CBT/exercise trial OR5.0,95%CI2.0–12.5 at6 months; OR5.4,95%CI2.3–12.8 at9 months. These are background from external studies as quoted in supplied plan, not RESOLVE data or power inputs. They are retained as numerical context, with no external sources opened. Historical telephone-first plan adapted to video where available/acceptable after Covid-era care changes. End of study follows last12-month assessment and scheduled interviews up to14 months.

### P-A15 — Eligibility population, numeric thresholds

[Page32](../../../joi250046supp1_prod_1755300121.14087.pdf#page=32), section5.1: EHR eligibility active health-system membership now/prior360 days; age≥18; English or no interpreter need; Essentia≥1 pain-related outpatient encounter, KP≥2 “>60 days apart,” in prior360 days; no common musculoskeletal surgery in prior60 days; no≥2 separate malignant-cancer encounters except nonmelanoma skin cancer in prior60 days; no hospice/palliative-care code/encounter prior360 days; no severe cognitive impairment. KPWA additionally excludes OUD codes. Subsequent screening requires high-impact chronic pain: pain most/every day and limiting life/work most/every day over prior3 months; persistent pain self-report “PEG score of ≥12”; internet and phone access. Literal >60-day encounter separation is image-confirmed and retained alongside the dated amendment wording in P-A02. This shard ends during section5.1; continuation belongs to the next disjoint shard.

## Complete physical-page coverage

All32 assigned pages mapped. Reusable-backed20; fresh-required12. Each page has explicit content/relevance, including administrative and nonapplicable units. OCR retained for every page; p16 table headers were read visually. Models, power calculations, missing-data procedures, formal analysis populations, stopping and multiplicity rules do not appear in pp1–32; their absence here is a shard-boundary fact, and later protocol/SAP shards cover statistical sections. No scientific gap in assigned scope.

| Physical page | Content opened and relevance | Local map key/status |
|---|---|---|
|1|Protocol title/version/date/registry; plan identity|P-A01 COMPLETE|
|2|Regulatory compliance; no result-relevant numeric/statistical content|NO_APPLICABLE COMPLETE|
|3|Amendments: phase, subgroups, BPI items, sex source, windows, MCID, strata|P-A02 COMPLETE|
|4|Amendments: OUD eligibility, consent/referral, qualitative enrollment, recordings/staff; approximately12 coaches|P-A02/P-A03 context COMPLETE|
|5|Amendments: pain encounters, surgery exclusions, intervention naming and Aim1|P-A02 COMPLETE|
|6|Amendments: independent interventions/onboarding, variable enrolled target vs2331 randomized|P-A02 COMPLETE|
|7|Amendments:2500 enrolled,≥2331 randomized,777/arm,site targets/qualitative schedule|P-A02 COMPLETE|
|8|Contents sections1–9; locator only, no independent statistical relationship|NO_APPLICABLE COMPLETE|
|9|Contents sections9–15; locator only, no independent statistical relationship|NO_APPLICABLE COMPLETE|
|10|Contents statistical/safety/interim and administration; locator only|NO_APPLICABLE COMPLETE|
|11|Abbreviations BPI,CI,MCID and administrative terms; no independent relationship|DEFINITIONS COMPLETE|
|12|Abbreviations OR,QALY,PEG,PROMIS,SAP,UC; no independent relationship|DEFINITIONS COMPLETE|
|13|Synopsis design,8 sessions,12-month assessments,aims/subgroups/mediators|P-A03 COMPLETE|
|14|Synopsis population2500/2331/777,4sites,120 interviews, intervention arms|P-A03 COMPLETE|
|15|Subject12–14 months/enrollment25-month duration|P-A03 COMPLETE|
|16|Table1 schedule,windows,footnotes,8-week intended/12-week maximum intervention|P-A04 COMPLETE|
|17|Background chronic/high-impact pain definition,prevalence; not trial data|P-A05 COMPLETE|
|18|Background conventional dose and rationale; not assigned intervention dose|P-A05 COMPLETE|
|19|Aims ≥30% primary3-month composite, secondary/exploratory status,mediators|P-A06/P-A09 COMPLETE|
|20|Risk management and concomitant treatment freedom; no numeric outcome rule|P-A03 context COMPLETE|
|21|Confidentiality/crisis/benefits; no result-relevant numeric/statistical content|NO_APPLICABLE COMPLETE|
|22|Primary binary MCID and secondary MCID table;3/6/12-month labels|P-A06/P-A07 COMPLETE|
|23|Secondary continuous BPI/social/physical/PGIC measures and timing|P-A07 COMPLETE|
|24|Economic cost/QALY objectives and12-month horizon|P-A08 COMPLETE|
|25|Exploratory opioid/depression/anxiety/sleep/chronic pain;sex/age/race moderators|P-A09/P-A10 COMPLETE|
|26|Rurality,pain clusters,mood,SDH moderator definitions|P-A10 COMPLETE|
|27|Mediator measures/timepoints;qualitative stratification/schedule|P-A11/P-A12 COMPLETE|
|28|Qualitative noncompletion/staff interviews; enrolled despite intervention noncompletion|P-A12 COMPLETE|
|29|Design/arms,equal individual randomization,strata,block3/6/9|P-A13 COMPLETE|
|30|Allocation implementation,enhanced usual care,historical feasibility numbers|P-A13/P-A14 COMPLETE|
|31|Historical trialOR/CI,video adaptation,end of study12/14-month|P-A14 COMPLETE|
|32|EHR/screening inclusion criteria,≥18,360/60-day windows,PEG≥12|P-A15 COMPLETE|

## Limitations and handoff

Native/layout text is corrupted for this source, resolved in assigned units through page-linked rendering/OCR and targeted visual transcription. OCR may preserve spacing/letter slips in nonquantitative prose; exact source images remain available. Numerical symbols ≥30%,≥60-day supply,≥65 years, BPI≥7, PEG≥12 and >60-day encounter separation were visually confirmed; p16 rotated table headers were visually transcribed. No unresolved assigned scientific-coverage gap; no candidate diagnosis performed. Full fresh OCR page transcriptions follow to preserve all prose, table footnotes and numeric context for downstream source localization.

## Complete OCR transcription appendix (locator aid)

### Physical PDF page 1 — OCR locator

```text
Tailored Non-Pharmacotherapy Services for Chronic Pain:
Testing Scalable and Pragmatic Approaches (RESOLVE Study)

UH3 STUDY PROTOCOL
Principal Investigator: Lynn L. DeBar, PhD, MPH

Grantee Institution:
Kaiser Permanente Washington Health Research Institute (KPWHRI)

Version Number: 5.0

10 November 2022

ClinicalTrials.gov Protocol Identifier: NCT04523714

```

### Physical PDF page 2 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

STATEMENT OF COMPLIANCE
The study will be conducted in accordance with the following:

e The International Council for Harmonisation Good Clinical Practice (ICH GCP) E6

e United States (US) Code of Federal Regulations (CFR) applicable to clinical studies (45
CFR Part 46)

e Completion of Human Subjects Protection and ICH GCP training by the Principal
Investigator and clinical trial site staff wno are responsible for the conduct, management,
or oversight of National Institute of Health (NIH)-funded clinical trials


```

### Physical PDF page 3 — OCR locator

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

SUMMARY OF CHANGES

Date Description of Change Rationale for Change
(Include specific sections affected)
07/15/20 Corrected the description of clinical trial phase to Inaccuracy in text
phase III; it was incorrectly stated as phase IV.
1.1 Synopsis
4.1 Overall Design
07/15/20 Added description of subgroup analyses based on Required by NIH and requested
age and race/ethnicity, as required for NIH phase III by NIA
clinical trial.
3.4 Exploratory (Tertiary) Objectives
15.7 Additional Effectiveness Analyses for Primary
Outcome (Moderators and Mediators)
08/06/20 Corrected description of modified BPI-SF to be 11 Inaccuracy in text
items (vs. 10 items) and pain intensity subscale to be
4 items (vs. 3 items)
3.1 Primary Objective
3.2 Secondary Objectives
08/06/20 Added final info on perceived support measure to Finalized based on pilot study
mediator table completion
3.4 Exploratory (Tertiary) Objectives
08/06/20 Changed randomization stratification based on sex to | Changed due to ability to ensure
be based on EHR data and not self-reported sex in availability of EHR variable (i.e.,
baseline survey not missing)
4.3 Study Arm Assignment/Randomization
08/06/20 Added information on KP CHR (KPNW) as site of Update to team structure/
virtual health coaches intervention staffing
10.1 Description of Interventions
09/25/20 Changed KPGA site PI from Dr. Bradlyn to Dr. Current KPGA site PI is retiring
McCracken since Dr. Bradlyn is retiring and revised in Dec. 2020
page to just include contact info and not signatures
Page iii. Investigator Contact Information
09/25/20 Edited the follow-up data collection windows to reflect | Changed to reflect final
final data collection decisions: 3-month changed to decisions related to follow-up
80-140 days (from 75-110); 6-month changed to 170- | data collection
230 days (from 165-200); and 12-month changed to
350-410 days (from 345-480). In addition, revised
description of duration of active intervention to clearly
specify max. duration is 12 weeks by moving to
footnote in Table 1.
1.2 Schedule of Activities and Table 1
09/25/20 Added assessment of MCID for two subscales of pain | In response to DSMB
severity composite measure (MCID in pain intensity recommendation
and MCID in pain-related interference)
3.2 Secondary Outcomes
15.6 Secondary Effectiveness Analyses
09/25/20 Added rural/medically underserved residency as In response to DSMB

stratum for randomization and adjustment variable
4.3 Study Arm Assignment/Randomization
15.5 Primary Effectiveness Analyses

recommendation


```

### Physical PDF page 4 — OCR locator

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

Date Description of Change Rationale for Change
(Include specific sections affected)

09/25/20 Specified one additional EHR-based inclusion To ensure coordination with
criterion to be applied at KPWA site only: no opioid another HEAL study at KPWA
use disorder (OUD) ICD-10 codes site specifically treating those
5.1 Participant Inclusion Criteria with pain and OUD

09/28/20 Added step to recruitment process where patients Another method was identified
who are referred by their clinician can contact the by health care system
study staff directly. For these individuals, consent to stakeholders and
access their medical record to assess eligibility will be | accommodated by study for how
obtained. patients might be referred
6.1 Recruitment of Patients
8.1 Informed Consent of Patients

09/28/20 Added ClinicalTrials.gov registration info to the title Study registration with
page ClinicalTrials.gov was posted

08/24/20

11/10/20 Removed statement related to obtaining waiver of Removed at request of VUMC
written consent and alteration of HIPAA from IRB as it | IRB
was not accurate.

8.1 Informed Consent of Patients

11/10/20 Revised the section on informed consent to clearly Revised in response to VUMC
delineate consent processes related to screening and | IRB questions
study enrollment.

11/23/20 Clarified that no consent is required for the population | Revised at request of VUMC
EHR-based eligibility screening IRB
8.1 Informed Consent of Patients

11/23/20 Clarified that sample of patients who do not complete | Add text to clarify in response to
the active interventions and will participate in VUMC IRB questions
qualitative interviews are still enrolled in the study.

This is already specified in section 9.1, which has not
been edited, but text was added to other places in
protocol where these interviews are described.

3.5 Qualitative Evaluation Objectives

6.1 Recruitment of Patients

11.3 Qualitative Interviews

11/24/20 Added text to indicate virtual intervention sessions Finalization of procedures
completed by secure video encounter that are related to recording virtual
recorded will generate a video recording sessions
2.4.1 Potential Risks
17 Source Documents

11/24/20 Added Ms. Firemark as staff person involved in Finalization of staff/study team
intervention supervision and fidelity monitoring roles
10.4 Study Intervention Fidelity Monitoring
Procedures

03/22/21 Updated info on number of health coach interviews Finalization of hiring/staffing of

from “up to 10” to reflect that all coaches (currently
projected at 12 so described as “approx.12”) will be
offered to complete an interview

1.1 Synopsis

6.2 Recruitment of Stakeholders for Qualitative
Evaluation

11.3 Qualitative Interviews

health coaches


```

### Physical PDF page 5 — OCR locator

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

entire document to clarify painTRAINER as “CBT-
based.” This affected wording in many places
throughout protocol. Most significantly, it changed
Aim #1 wording from this:

Aim #1: Determine the effectiveness of a web-based
CBT-CP program and virtual coach-led
(telephonic/video) CBT-CP on achieving clinically
meaningful improvements in patients’ pain severity
(pain intensity + pain-related interference) relative to
those receiving usual care at 3 months.

To revised:

Aim #1: Determine the effectiveness of an online,
CBT-based pain management program and virtual
coach-led (telephonic/video) CBT-CP on achieving
clinically meaningful improvements in patients’ pain
severity (pain intensity + pain-related interference)
relative to those receiving usual care at 3 months.

Date Description of Change Rationale for Change
(Include specific sections affected)
03/31/21 Modified EHR-based inclusion criteria related to the High rate of refusal prior to
minimum number of pain-related encounters (criterion | screening due to no chronic pain
#4 in section 5.1) for the 3 KP sites; changed to 2 2 and ineligibility among those
encounters that are at least 30 days apart. Essentia screened at KP sites. By
remains at least 1 encounter. increasing threshold for required
5.1 Participant Inclusion Criteria pain visits, more likely to
efficiently identify people likely
to have chronic pain.
03/31/21 Added an EHR-based exclusion criterion related to High rate of refusal and
surgery in the past 60 days for all sites reporting recent surgery and
5.2 Participant Exclusion Criteria therefore no current chronic
pain. By adding criterion, more
likely to efficiently identify
people likely to have chronic
pain.
03/31/21 Added exclusion criterion related to Multiple virtual health coach
planned/scheduled surgery in next year. intervention participants have
5.2 Participant Exclusion Criteria indicated upcoming surgery;
7 Eligibility Screening common exclusion criterion for
pain studies
03/31/21 Updated description of virtual intervention fidelity Provide more details on final
monitoring to include more details and specific info on | plan/procedure
final plan.
10.4 Study Intervention Fidelity Monitoring
Procedures
03/31/21 Added information on third framework to be used in Expanded constructs for
qualitative evaluation, Theoretical Framework of qualitative interviews to include
Acceptability more related to acceptability
16 Qualitative Evaluation Analyses
02/24/22 Revised description of active interventions throughout | NIH Project Scientist, Dr.

Wandner, requested edit; using
the consistent description of
painTRAINER as CBT-based
and not CBT was agreed upon
for all HEAL studies that include
painTRAINER.


```

### Physical PDF page 6 — OCR locator

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

Date Description of Change Rationale for Change
(Include specific sections affected)

02/24/22 Removed references to painTRAINER as an “Application” was inaccurate
“application” and replaced with “online program” as it | description.
is not an application (“App”) that can be downloaded
to a mobile device but can only be used online via a
web browser. Also removed “web-based” as
descriptor and replaced with “online” as it is clearer to
describe as “online CBT-based.” (vs. web-based,

CBT-based)

02/24/22 Revised description of active interventions throughout | Both active interventions
entire document to be independent/standalone. needed equal description and
Previously, painTRAINER had substantial detail but previous text inaccurately
the virtual coach-led CBT-CP was only described as__| presented the coach-led
“having content analogous to painTRAINER.” The intervention as derived from
structure of Section 10 was changed to provide an painTRAINER.
overview of the core elements of both interventions
and then give specifics on each one.

Precis
Section 10 Study Interventions

02/24/22 Added descriptions of the onboarding and ongoing Requested by DSMB
support/outreach for both active interventions. In
addition, described the motivational interviewing
language included in the painTRAINER onboarding
script.

Section 10 Study Interventions

02/24/22 Added this information in each location where 2,380 Clarify that the target number
enrollment target is stated: consented/enrolled is variable
Note: The number enrolled might need to be greater | and may change in order to
than 2,380 to ensure reaching the randomized meet the 2,331 target for
participant target of 2,331 (as not all who number randomized, which is
consent/enroll go on to be randomized). invariable.

02/24/22 Clarified that intervention staff who support Oversight in original description
participant engagement with painTRAINER will also as just stated “health coaches”
be invited to complete qualitative interviews.

1.1 Synopsis

6.2 Recruitment of Stakeholders for Qualitative
Evaluation

11.3 Qualitative Interviews

02/24/22 Added information to Section 8.1 indicating that, as Added as a contact and strategy
needed, sites may follow-up by phone with individuals | to support retention.
who enrolled by web in order to briefly welcome them
to the study and clarify next steps.

Section 8.1 Informed Consent
11/10/22 Updated Dr. DeBar’s KP site affiliation to KP CHR (as | Dr. DeBar is transferring to KP

of 1/1/23). Removed Dr. Elder as KP CHR site PI.
Added Dr. Cook as KPWHRI site PI.
Section: Investigator Contact Information

CHR (as of Jan. 1, 2023) and it
will become the prime site.


```

### Physical PDF page 7 — OCR locator

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

with each healthcare system stakeholder and that
interviews will be conducted in years 4-5 of the study
(vs. years 2-3).

1.2 Schedule of Activities

3.5 Qualitative Evaluation Objectives

Date Description of Change Rationale for Change
(Include specific sections affected)

11/10/22 Updated the number to be enrolled to approximately As the study nears the end of
2,500 from 2,380. Clarified that the total number recruitment, we are aiming to
enrolled and randomized by each of the 4 sites may enroll more at Essentia and
vary (range of 595-625) in order to reach the overall KPGA where enrollment rates
study target for number randomized within the study have remained steady in order
timeline with some sites enrolling more than others to ensure we have the overall
(i.e., Essentia and KPGA vs. KPWA). target N. KPWA rates have
1.1 Synopsis been lower than the other sites
6.1 Recruitment of Patients and seem to be decreasing

slightly in recent months. This
approach was approved by NIA
and JHU via email on 10/31/22.

11/10/22 Clarified the target N to be randomized is at least Clarify that the N randomized
2,331 or 777 per arm. will not be exactly 2,331 but
1.1 Synopsis might be slightly over.

6.1 Recruitment of Patients
15.1 Sample Size Determination
11/10/22 Indicated that up to 2 interviews will be conducted Study team would like to be able

to interview healthcare system
stakeholders more than one
time.

Vi

```

### Physical PDF page 8 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

TABLE OF CONTENTS

STATEMENT OF COMPLIANCE
SUMMARY OF CHANGES
INVESTIGATOR CONTACT INFORMATION...
TABLE OF CONTENTS
LIST OF ABBREVIATIONS
1 PROTOCOL SUMMARY
1.1 Synopsis......
1.2 Schedule of Activities (SoA)
2 INTRODUCTION
2.1 Background Information..
2.2 Rationale
2.3 Specific Aims
2.4 Potential Risks and Benefits
2.4.1 Potential Risks ..
2.4.2 Potential Benefits
3 OBJECTIVES AND OUTCOME MEASURES.
3.1 Primary Objective
3.2 Secondary Objectives.. .
3.3 Economic Evaluation Objectives .
3.4 Exploratory (Tertiary) Objectives..
3.5 Qualitative Evaluation Objectives...
4 STUDY DESIGN
41 Overall Design
42 Study Arms.....
4.3 Study Arm Assignment/Randomization..
44 Scientific Rationale for Study Design ..
4.5 Justification for Interventions
4.6 End-of-Study Definition...
5 STUDY POPULATION
5.1 Participant Inclusion Criteria
5.2 Participant Exclusion Criteria
6 RECRUITMENT PROCEDURES AND RETENTION STRATEGIES
6.1 Recruitment of Patients... eee eeeeseesseeeneeeneeneeeneees
6.2 Recruitment of Stakeholders for Qualitative Evaluation
6.3 Retention Strategies ....
7 ELIGIBILITY SCREENING .
8 INFORMED CONSENT PROCESSES.
8.1 Informed Consent of Patients te “
8.2 Informed Consent of Stakeholders and Staff vette eeaeeeaeeneeeeeeeeneseneeeeesieeteeeneaseneeenes
9 STUDY INTERVENTION DISCONTINUATION AND PARTICIPANT
DISCONTINUATION/WITHDRAWAL ........ 2... eecceesceecececeeeeceeeeeeeeeaeeeneeeereeeneeneeeueeeteeenreeeees 29

VIII

```

### Physical PDF page 9 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

10

11

12

13

14

15

.29
.29
-.29

.30
.30
31

9.1 Discontinuation of Study Intervention.
9.2 Participant Discontinuation/Withdrawal from Stud
9.3 Loss to Follow-Up
STUDY INTERVENTIONS
10.1 Description of Interventions.

10.1.1 painTRAINER.

10.1.2 Virtual Coach-led CBT-CP 32
10.2 Intervention Administration and Dosing.... 83
10.3 Masking and Measures to Minimize Bias . 33

133
34
35

10.4 Study Intervention Fidelity Monitoring Procedures
10.5 Concomitant Therapy..........ceeeeeeeees
STUDY ASSESSMENTS AND PROCEDURES
11.1 Baseline Assessment...... 35
11.2 Follow-Up Assessments . 35
11.3 Qualitative InterviewS .........o. eee cece eee cece cee eeeeeeee cece cesanteneeseceestaneenetecee 35
ADVERSE EVENTS AND UNANTICIPATED PROBLEMS INVOLVING RISKS TO
SUBJECTS OR OTHERS
12.1 Definition, Classification and Reporting of Adverse Events
12.1.1 Definition of Adverse Events (AEs)
12.1.2 Definition of Serious Adverse Events (SAEs)
12.1.3 Definition of Adverse Events of Special Interest (AESI)
12.1.4 Severity of Adverse Events .............
12.1.5 Relationship to Research Participation ..
12.1.6 Expectedness of Adverse Events/Serious Adverse Events ...
12.1.7 Reporting Procedures for Adverse Events/Serious Adverse Events
12.2 Definition and Reporting of Unanticipated Problems
12.2.1 Definition of Unanticipated Problems
12.2.2 Reporting of Unanticipated Problems .
STUDY OVERSIGHT
13.1 Halting Rules
STUDY MONITORING..
14.1 Clinical Site Monitoring
STATISTICAL CONSIDERATIONS
15.1 Sample Size Determination.
15.2 Populations for Analyses ...
15.3 General Approach to Statistical Analyses
15.4 Baseline Descriptive Statistics ....
15.5 Primary Effectiveness Analyses..

37
37
37
dT
238

38
38
-39
-39
-39
39
39
41

A1
42
42
43
43
44
44
44
44

15.6 Secondary Effectiveness Analyses ............c.:ccccccceceeeceeeeeseeceeteeaeeeteesenseeneeatennenteees 45

15.7 Additional Effectiveness Analyses for Primary Outcome (Moderators and
Mediators).

15.8 Economic Evaluation Analyses...

15.9 Exploratory Effectiveness Analyses .............00ccccceceeeee tcc csc teneeeneeeteeteeeeneneenecaeee 47

IX

```

### Physical PDF page 10 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

16
17
18
19

20

21
22
23

15.10 Safety Analyses...
15.11 Planned Interim Analyses ..
QUALITATIVE EVALUATION ANALYSES...
SOURCE DOCUMENTS AND ACCESS TO SOURCE DATA/DOCUMENTS...
QUALITY CONTROL AND QUALITY ASSURANCE
ETHICS/PROTECTION OF HUMAN SUBJECTS..
19.1 Ethical Standard .......0.0.0....
19.2 Institutional Review Board .
19.3. Exclusion of Women, Minorities, and Children (Special Populations)
19.4 Subject Confidentiality ..............

19.4.1 Certificate of Confidentiality..
DATA HANDLING AND RECORD KEEPING.
20.1 Data Management Responsibilities
20.2 Schedule and Content of Reports
20.3 Study Records Retention
20.4 Protocol Deviations
PUBLICATION ....
DATA SHARING . on
REFERENCES. ....00......cccceeceeceeseecesceeeeceeeeeceeeeeeeeseenaeeecceceseneeeaesaccesneseeeneseaeeeenrenseneteatees


```

### Physical PDF page 11 — OCR locator

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

AE

BPI - SF
CBT-CP
CCC
CFR

cl

CMP
CRF
csi
DCC
DSMB
eCRF
EDA
EDC

EH

EHR
EQ-5D-5L
FFR
FWA
GCP
HCS
HIPAA
ICF

ICH
ICMJE
IRB
JHU

KP

KP CHR
KPGA
KPNW
KPWA
KPWHRI
MCcID

LIST OF ABBREVIATIONS
Adverse Event
Brief Pain Inventory — Short Form
Cognitive Behavioral Therapy for Chronic Pain
Clinical Coordinating Center
Code of Federal Regulations
Confidence Interval
Clinical Monitoring Plan
Case Report Form
Clinical Site Investigator
Data Coordinating Center
Data and Safety Monitoring Board
Electronic Case Report Form
Exploratory Data Analysis
Electronic Data Capture
Essentia Health
Electronic Health Records
EuroQoL 5 Dimensions — 5 Levels
Federal Financial Report
Federalwide Assurance
Good Clinical Practice
Health care system
Health Insurance Portability and Accountability Act
Informed Consent Form
International Council for Harmonisation
International Committee of Medical Journal Editors
Institutional Review Board
Johns Hopkins University
Kaiser Permanente
Kaiser Permanente Center for Health Research
Kaiser Permanente Georgia
Kaiser Permanente Northwest
Kaiser Permanente Washington
Kaiser Permanente Washington Health Research Institute
Minimal Clinically Important Difference

Xl

```

### Physical PDF page 12 — OCR locator

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

mHealth
MOP
N

NIA
NIH
OHRP
OR
PEG
PCP
PHI

Pl

PO
PROMIS
QA
QALY
Qc
QoL
RIC
SAE
SAP.
SIRB
SOP
TIC
UC
UP

Mobile Health

Manual of Procedures

Number (typically refers to participants)
National Institute on Aging

National Institutes of Health

Office for Human Research Protections
Odds Ratio

Pain, Engagement of Life & General Activity
Primary Care Providers

Protected Health Information

Principal Investigator

Program Official, NIH

Patient-Reported Outcomes Measurement Information System
Quality Assurance

Quality-Adjusted Life Year

Quality Control

Quality of Life

Recruitment Innovation Center

Serious Adverse Event

Statistical Analysis Plan

Single Institutional Review Board
Standard Operating Procedure

Trial Innovation Center

Usual Care Study Arm / Group
Unanticipated Problem

XII

```

### Physical PDF page 13 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022
1 PROTOCOL SUMMARY
1.1 Synopsis
Title: Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable
and Pragmatic Approaches (RESOLVE Study)
Précis: The RESOLVE study is a multicenter comparative effectiveness trial

evaluating two cognitive-behavioral therapy (CBT)-based chronic pain
treatments delivered via different telehealth modalities: 1) online program
and 2) live, coach-led, virtual sessions (telephone and/or video conference).
The study uses a 3-arm, parallel intervention design; both intervention arms
will be compared to usual care services.

Participants randomized to the two intervention arms will complete 8 CBT-
based sessions for chronic pain (approximately 1 per week) via the online
program (self-directed) or one-on-one with the live coach. Those
randomized to usual care will receive an education resource manual for
chronic pain management. All study participants will be enrolled for 12
months and complete self-reported assessments at baseline, notification of
randomization, and 3-, 6- and 12-months. A subset of participants will
participate in the qualitative evaluation and complete an hour-long interview
at approximately 3-5 months follow-up and 12-14 months follow-up.

In addition, qualitative interviews will be completed with approximately 20
health care system stakeholders across the 4 study sites and the staff who
support the painTRAINER intervention administration and those who deliver
the virtual CBT-CP sessions (approximately 12).
Specific Aims: Aim #1: Determine the effectiveness of an online, CBT-based pain
management program and virtual coach-led (telephonic/video) CBT-CP on
achieving clinically meaningful improvements in patients’ pain severity (pain
intensity + pain-related interference) relative to those receiving usual care
at 3 months.
1a. Examine the impact of the active interventions on secondary
pain outcomes and related quality of life outcomes (social role
functioning, physical functioning, and patient global impression of
change); as well as exploratory outcomes, which include long-term
opioid use; comorbid symptomology (depression, anxiety, and
sleep disturbance); and high impact chronic pain and graded
chronic pain.
1b. Conduct subgroup analyses to determine the impact of the
active interventions on specific populations and explore for
potential heterogeneity of treatment effects by sex; rural/medically
underserved residency; multiple pain conditions; mental health
mood disorders; and negative social determinants of health.
1c. Examine the role of theory-based mediators, pain
catastrophizing, pain-related self-efficacy, and perceived support,
on pain-severity.
Aim #2: Assess the cost and incremental cost-effectiveness of the online
and virtual coach-led CBT-CP interventions compared to each other and
usual care.
Aim #3: Conduct a qualitative evaluation to understand: 1) patient
experiences of the interventions, including how they relate to treatment


```

### Physical PDF page 14 — OCR locator

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

response, variability by site, and rural/medically underserved residency
status; and 2) health system issues, including adaptations and contextual
factors at the site and external levels, barriers and facilitators to intervention
success and potential for adoption, sustainability, and dissemination.

Population:

Approximately 2,500 participants with high-impact chronic pain, as
demonstrated by initial electronic health records (EHR)-based eligibility
criteria and subsequent screening, will be enrolled in this study with the
goal of randomizing approximately 2,331 participants (at least 777 per
study arm). [Note: The number enrolled might need to be greater than
2,500 to ensure reaching the randomized participant target of at least 2,331
(as not all who consent/enroll go on to be randomized).]

Participants will be recruited from four integrated health care
systems/clinical sites: 1) Kaiser Permanente Georgia (KPGA), 2) Kaiser
Permanente Northwest (KPNW), 3) Kaiser Permanente Washington
(KPWA), and 4) Essentia Health.

Of the randomized participants, 120 will participate in the interviews for the
qualitative evaluation. The health care system stakeholders to be
interviewed will be administrators in the areas of quality improvement,
primary care, and/or pain management at each of the 4 study sites and
referring clinicians. The intervention / health coaching staff to be
interviewed will be the centralized staff who support painTRAINER
engagement as well as those who deliver the virtual CBT-CP sessions.

Phase:

Phase III Clinical Trial

Anticipated Number of
Sites:

Four clinical sites:
1. Kaiser Permanente Georgia (KPGA)
2. Kaiser Permanente Northwest (KPNW)
3. Kaiser Permanente Washington (KPWA)
4. Essentia Health

Description of
Interventions:

Two interventions will be tested in this comparative effectiveness trial.
1) An online, CBT-based pain coping skills training program
(painTRAINER)

2) A virtual, live coach-led CBT-CP intervention (telephone or
video-administered

Both interventions are comprised of 8 sessions which participants are

expected to complete weekly. The content of the 2 interventions is

analogous and focuses on interactive training in evidence-based pain-
coping skills.

Those randomized to the usual care arm of the study will be sent a bound
copy of the 2020 edition of the American Chronic Pain Association
Resource Guide to Chronic Pain Management.

All enrollees can receive any pharmacologic and nonpharmacologic
treatments available to them without restriction.

Study Duration:

48 months from start of enrollment to completion of data analyses


```

### Physical PDF page 15 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

Subject Participation 12-14 months
Duration: (The majority of subjects will participate for 12 months. The subset of

qualitative evaluation subjects will complete the last follow-up interviews at
12-14 months.)

Estimated Time to 25 months
Complete Enrollment:


```

### Physical PDF page 16 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

1.2 Schedule of Activities (SoA)

The schedule of activities in Table 1 below pertains to the patients who will participate in the
RESOLVE UH3 trial.

For the health care system stakeholders who participate, study activities will include
approximately two hour-long interviews conducted by phone. For the health coach / intervention
staff who participate, study activities will include two approximately hour-long interviews
conducted by phone early and later in the study implementation.

Table 1. UH3 Schedule of Activities for Patients

=e
¥ e
= ~ o
9 < c a
25/8 § |e laeleolz 2a Pol ko | deo 3
=| 8 SB. /ES/EN/ EN) ES) ED LES EBL RS] ao fo | B
i = 2 5 se2|6e2|6 s2/5e/6 Se/2 3
of rs €2}/Se/s2|/ 52) 52g] 52/582) 52) §2|/ 20/28] ge
Se S SH | BS) Be] Ba] Bo] GO] Bam] Bol on) ET) EN) ES
So | Bo /2e/ 8S) Br] 9) BX] BO |] Bt! BB) go) 8 | So) to
Ps BO [eB lOO OF|HO>| HFl/He HOD! HF] SL| Sz) ~=S
g2| S& 22/89/89) 8°] 84) 89/54) 54] 54/28/28) $8
o+ aod ax /fy/ 25) 8.) 28 2 2! g co. s ic >
Oy e RS |/2S/ 2x) 2X) Bx] BX lEBX) Bx) ex) ESE
5x] & es/SS/SS/ 55/55) 5/55/55) §S\a8|Sa| FF
Ox| g 6alegles8) e8)ec) eS8)/es)e5/$al/e 20) 3a
>e| & ot) Se) s2)/ 82/82) SF | SZ 82) sF\o |s | L
a} ¢ § |£ |E*S/E*) ETE E*/Et/=z ©
o a = 2
a iS)
=
a
Procedures
Eligibility screening X (or) X
Informed consent X (or) X
Baseline assessment x
Randomization x
Notification of study arm x
assignment

Administer study
intervention (if

applicable, based on x | x x x x x x x
study arm assignment)

Adverse event review
and evaluation

Study assessments
completion x x x x x

Interviews with subset of x x
participants

1. The eligibility screening, consent and baseline survey can all be completed in the same phone encounter or online
survey session, if feasible for the participant. If these activities are not completed in the same encounter or
session, efforts will be made to complete the consent and baseline survey with those eligible individuals who want
to participate in the study within 14 days of them completing the eligibility screening.

2. The active intervention sessions are intended to occur approximately weekly over the course of 8 weeks;
however, completion may vary due to personal circumstances of the participants. The maximum duration for
active intervention sessions is 12 weeks. (See Section 10.2 for further information).


```

### Physical PDF page 17 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

2 INTRODUCTION
2.1 Background Information

Chronic pain, defined as pain lasting for 3 months or longer, is one of the most common,
disabling, and costly public health problems in the United States." It is one of the primary
reasons patients seek medical care. It often involves high levels of disability and emotional
suffering.’? High impact chronic pain, defined as pain that has lasted 3 months or longer and
is accompanied by at least one major activity restriction, such as being unable to work outside
the home, go to school, or do household chores affects about one in ten adults.1>4

Rural residency is associated with higher prevalence of high impact chronic pain with
complicating features such as depression and medical comorbidities.5° Rural residents with
chronic pain report higher pain frequency and intensity and more pain-related disability and
depression than urban residents with pain.”® Health care disparities between rural and urban
areas are widely recognized with rural residents often affected by difficulties in availability,
accessibility, and affordability of health services.° These disparities put rural patients with
chronic pain at higher risk for adverse outcomes and suboptimal pain management.

Most patients with chronic pain are treated by primary care clinicians and medications are
mainstays of pain management. While opioids were, until recently, viewed favorably for long-
term chronic pain management, supporting evidence was weak.'? Recent evidence shows
opioid-related harms and widespread opioid use has left an aftermath of adverse effects for
patients and communities.'"'? These consequences have been especially pronounced in rural
communities where the abuse rates of prescription opioids and drug-related overdoses are
disproportionally higher than in urban areas.'*4 Consequently, primary care clinicians and
their patients, especially in medically underserved areas, urgently need increased access to
viable nonopioid options and treatments for long-term chronic pain management.

Cognitive-behavioral therapy for chronic pain (CBT-CP) is the most widely accepted and
effective treatment'®® and is shown to benefit low-literacy adults in rural areas.'’ CBT-CP is
based on the theory that patients’ beliefs, attitudes, behavior, and coping styles play central
roles in determining (mediating) the impact of persistent pain.'’® CBT-CP effects can be
maintained long after treatment ends, without the negative side effects of opioids and other pain
medications. CBT-CP is an attractive adjunct or alternative to pharmacological treatments. It
focuses on helping patients develop and master skills to manage pain and its associated
disability and emotional distress to improve functioning and quality of life. The National Pain
Strategy calls for wider implementation of CBT-CP self-management programs," noting that
despite supporting evidence, 2° CBT-CP implementation lags due to significant barriers.

Outside Veterans Affairs health care systems,”° few clinicians are trained to deliver CBT-CP.
CBT-CP services in community practice often vary in quality despite the growing emphasis on
standardized training methods.?' In community settings, fidelity to best treatment practices is
rarely assessed.” Frontline behavioral health providers offering CBT-CP generally have high
caseloads and pressure to prioritize treatment for mental disorders, limiting CBT-CP availability.
These problems are especially critical in rural areas and medically underserved
communities”®? where there are generally few behavioral health and psychotherapy providers
and extreme scarcity in those trained to deliver CBT-CP. In addition, conventional CBT-CP
programs can be difficult to use for patients with limited time, transportation or mobility barriers,


```

### Physical PDF page 18 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

or competing demands. Most CBT-CP programs require weekly in-person sessions of 50
minutes or more over 2-3 months, often in group formats with inflexible scheduling. Patients
referred for CBT-CP may attend too few sessions to receive an adequate treatment dose.
Further, the stigma associated with what are perceived to be “psychological” interventions can
limit patient uptake.2°” Providing CBT-CP by telephone or in an online program may help
destigmatize its use and encourage patients to view it as complementing conventional medical
management of chronic pain, while helping them achieve functional and quality-of-life goals.

Lastly, there are gaps in primary care providers’ (PCP) referral to CBT treatment. PCPs who
lack familiarity with CBT-CP are often concerned about not having enough time to discuss CBT-
CP, lack ways to provide a compelling rationale for CBT-CP, or have difficulty explaining why a
psychologically informed treatment may help manage a physical condition. Moreover, guidelines
do not exist for determining which patients might benefit from CBT-CP.?

Technologies to deliver and assist treatment such as online- and telephone-based treatment
programs’®*° offer ways to increase access to evidence-based pain care, including CBT-CP
and related self-management approaches.°? Because mobile health (mHealth) and
telehealth services have lower marginal costs than in-person care, they can reach large
numbers of patients and support health behavior change and self-management efforts while
overcoming system, patient, and clinician barriers.** mHealth interventions can improve self-
management? and chronic illness care outcomes.* Finally, following the Covid-19 outbreak,
mHealth and telehealth services are rapidly becoming the norm with a particular push towards
video visits both to best approximate in-person visits and increase likely payment.°® Further, as
Eccleston and colleagues (2020) note, “preventing [and managing] chronic pain is complex at
the best of times but in a global health pandemic, risk factors for pain morbidity and mortality
will be magnified. (p.8904)"°

2.2 Rationale

High impact chronic pain is persistent and limits life and work activities. It affects about one in
ten adults."° Treatment is inadequate, with overuse of long-term opioid therapy and underuse
of evidence-based nonpharmacologic treatments.'® Cognitive-behavioral therapy for chronic
pain (CBT-CP) is the most widely accepted and effective of these treatments.''®'® Enhanced
availability of CBT-CP services for high impact chronic pain is of critical public health
importance®’, particularly for medically underserved and rural populations devastated by the
opioid epidemic.'** However, professionals trained to deliver CBT-CP are typically in urban
areas. Making CBT-CP widely available and low cost would reduce barriers to use of CBT-CP
for the majority of the US population, particularly those in rural and medically underserved
areas.

This comparative effectiveness research trial will evaluate two potentially low-cost and
scalable CBT-based treatments for chronic pain: 1) an established online, CBT-based
pain coping skills training (PCST) program (painTRAINER), and 2) a virtual, coach-led
(telephone/video-administered) CBT-CP intervention. Both modalities will be compared
to usual care services.


```

### Physical PDF page 19 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

2.3 Specific Aims

Aim #1: Determine the effectiveness of an online, CBT-based pain management program and
virtual coach-led (telephonic/video) CBT-CP on achieving clinically meaningful improvements (2
30%) in patients’ pain severity (pain intensity + pain-related interference) relative to those
receiving usual care at 3 months.

1a. Examine the impact of the active interventions on secondary pain outcomes and
related quality of life outcomes (social role functioning, physical functioning, and patient
global impression of change); as well as exploratory outcomes, which include long-term
opioid use, comorbid symptomology (depression, anxiety, and sleep disturbance), and
high impact and graded chronic pain.

1b. Conduct subgroup analyses to determine the impact of the active interventions on
specific populations and explore for potential heterogeneity of treatment effects by sex;
rural/medically underserved residency; multiple pain conditions; mental health mood
disorders; and negative social determinants of health.

1c. Examine the role of theory-based mediators, pain catastrophizing, pain-related self-
efficacy, and perceived support, on pain-severity.

Aim #2: Assess the cost and incremental cost-effectiveness of the online and virtual coach-led
CBT-CP interventions compared to each other and usual care.

Aim #3: Conduct a qualitative evaluation to understand: 1) patient experiences of the
interventions, including how they relate to treatment response, variability by site, and
rural/medically underserved residency status; and 2) health system issues, including
adaptations and contextual factors at the site and external levels, barriers and facilitators to
intervention success and potential for adoption, sustainability, and dissemination.

2.4 Potential Risks and Benefits

2.4.1 Potential Risks

The RESOLVE study poses minimal risks. Those risks that might exist fall into four categories:
(a) risks of the intervention; (b) risks associated with research assessments; (c) risks associated
with potential loss of confidentiality; and (d) risks of worsening physical or emotional state.
These minimal risks and the procedures to help mitigate the risks are described further below.

Risks associated with the intervention. The intervention programs consist of either an
online program or virtual coach-led (telephone and/or video) CBT-CP sessions. CBT-CP
focuses on helping people change how they think and act in response to pain-related
stressors® and on increasing patients’ coping skills to help them better manage their
pain and improve their emotional and physical functioning. Therefore, individuals who
participate in the interventions might experience emotional or physical discomfort related
to challenges in modifying their thoughts and behaviors related to pain. For example,
someone might feel discouraged or frustrated during the intervention process or they
might be physically challenged by behaviors they try to address in increasing physical
activity. However, these risks are minimal, in that the probability and magnitude of


```

### Physical PDF page 20 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

discomfort is no greater than what someone might encounter in daily life. CBT-CP.
interventions have been used by the current study team and other investigators without
adverse effects in studies as well as in clinical practice with patients with chronic pain
and other health conditions.

Procedures to help mitigate these risks. All behavioral health staff who will be conducting
the intervention sessions with participants will receive comprehensive training and
supervision from one or more of the following individuals: Drs. DeBar (PI), Balderson
(Co-Investigator at KPNW), and Keefe (Co-Investigator at Duke University), all with
considerable experience supervising and training the delivery of such clinical research
interventions. Finally, participants who experience emotional or physical discomfort
during the intervention have the option of seeking services in the participating health
care system in which they are insured/served as well as outside of the health care
system, if they prefer; enrollees can receive any pharmacologic or non-pharmacologic
treatments available to them without restriction.

Risks associated with research assessments. Research assessments consist of
accessing data from participants’ electronic health records (EHR) data, conducting
surveys and interviews, and collecting data related to the delivery of the intervention
programs, including audio- and video-recordings of virtual CBT-CP sessions and the
collection of painTRAINER usage data. Any risks related to the collection of research
data and the potential for accidental disclosure of protected health information (PHI), are
described specifically below. Survey and interview questions focus on pain and
associated impairment and functioning, comorbid conditions (including depression and
anxiety), and use of treatments outside of traditional health care. Some of the questions
might make participants feel uncomfortable. However, the study surveys and interviews
involve no specific risk or discomfort beyond those associated with a standard clinical
interview. Proposed assessment tools, or ones assessing similar domains, have been
used by the research team in previous research, with no known problems or distress on
the part of participants. Virtual intervention sessions will be audio- or video-recorded, for
the purpose of review by senior research staff, who will make quality assurance ratings
of staff performance. (Note: The audio recording of the session is the only data needed
for quality assurance review, however if the participant completes a session via video,
the recording will generate a video recording from which the audio recording will be
extracted.) If participants are uncomfortable with having their session recorded, they can
refuse having their session recorded and still participate in the study.

Protection for risks associated with research assessments. Participants will be told that
they are free not to respond to specific survey or interview questions or to terminate
involvement in completing a survey or interview at any time, with no adverse
consequences. If a participant appears to be distressed during assessments, research
staff will halt the survey or interview and offer to call back to complete the assessment.
The assessment will only re-commence when and if the participant reports feeling
capable of doing so. Survey assessments will be conducted by research staff who are
trained to address anticipated participant concerns; interviews will be conducted by
experienced research staff who have previously conducted interviews with the target
population and are sensitive to these issues.

Risks associated with potential loss of confidentiality. The confidentiality of participants
could be compromised by an accidental release of protected health information (PHI)
that are accessed or collected as part of this study’s research assessments. The
recruitment design used in this study carries the potential risk of loss of privacy and or


```

### Physical PDF page 21 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

unwanted contacts because EHR data are queried, and pertinent information extracted
for potentially eligible individuals. As in any research study, there is the slight risk that
records might be accessed or obtained by persons who are not authorized to do so.
Procedures to help mitigate these risks. All participant information is considered
confidential and will be used only for research purposes. This confidentiality will be
ensured through several mechanisms. Each participant will be assigned a study ID and
direct identifiers will only be linked to subjects’ study ID in circumstances where staff
need to access information in order to contact participants to conduct study activities.
Analytic datasets will be de-identified. All study forms, paper and electronic records, and
all participant data (both hard copies and electronic) will be stored in secure areas, with
access restricted to select study staff, or on secure servers, as relevant at the
participating institutions. Third, access to participant data and information will be
restricted to authorized personnel as necessitated by their professional role and tasks on
the project. Data transfer between participating institutions will be done using Secure
Socket Layer (SSL) encryption. In accordance with HIPPA regulations and local IRB
requirements, all appropriate compliance requirements for data transfer and data use will
be met after consultation with compliance officers.

Risks of worsening mental or emotional state. Many of the study participants are
expected to have comorbid depression, anxiety and/or other mental health conditions. It
is expected that mental and emotional symptoms experienced by these individuals will
fluctuate throughout the study period and some participants may have worsening pain
and/or other mental health symptoms during the study period. However, these are risks
inherent in the population and would occur regardless of study enrollment.

Procedures to help mitigate these risks. All patient participants enrolled in the study will
have access to treatment through their health care system and will be encouraged to
seek care in the event that their symptoms significantly worsen during the intervention.
This is consistent with the standard of care provided within the participating health care
systems (KPGA, KPNW, KPWA, and Essentia). Participants in the study are free to
withdraw from the study at any time with no consequence to their health care. If a patient
reports imminent risk of a psychiatric crisis, study staff will take appropriate immediate
action by connecting the patient with emergency services in his/her region.

2.4.2 Potential Benefits

Potential benefits for those participating in the intervention arms of the study include access to
evidence-based intervention programs that may help participants develop the skills to better
manage their pain, improve their functioning, and potentially lower their reliance on opioid
medication. While those in the usual care arm will not receive such care, the American Chronic
Pain Association Resource Guide to Chronic Pain Management’ is detailed and
comprehensive and may help them better navigate the treatment options available to them
through their health care system and surrounding communities.

Although patients, clinical staff, and administrators participating in the interview portions of the
study may not directly benefit from participation in interviews, many individuals enjoy the
opportunity to provide their opinions and tell their stories. Further, these individuals may derive
personal satisfaction from being part of a study that may have public health implications and
that will further scientific knowledge concerning various treatment and self-care options for pain
management.


```

### Physical PDF page 22 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022
3 OBJECTIVES AND OUTCOME MEASURES
3.1 Primary Objective
Primary Objective Brief Description of Measure | Outcome Measured By Time Frame
Determine whether the Minimal clinically important Patient self-reported pain Baseline to 3
active interventions result | difference (MCID) in pain at baseline and 3 months months
in a higher proportion of severity (pain intensity + pain
patients achieving a interference) is defined as a
reduction in pain severity | 30% decrease in score on
that is a minimal clinically | modified 11-item version of the
important difference Brief Pain Inventory — Short
(MCID) relative to those Form (BPI-SF)*°4? from
receiving usual care at 3 baseline (consistent with
months. IMMPACT consensus
guidelines)*? (Binary; Yes/No)
3.2 Secondary Objectives
Secondary Objectives Brief Description of Measure Outcome Measured By Time Frame
Determine whether the See above (Binary; Yes/No) Patient self-reported pain Baseline to 6

active interventions
result in a higher
proportion of patients
achieving a MCID in pain
severity relative to those
receiving usual care at 6
and 12 months.

at baseline, 6 and 12
months

and 12 months

Determine whether the
active interventions
result in a higher
proportion of patients
achieving a MCID in pain
intensity

Minimal clinically important
difference (MCID) in pain
intensity is defined as a 30%
decrease in score on 4-item pain
intensity subscale of the Brief
Pain Inventory — Short Form
(BPI-SF)*°“2 from baseline
(Binary; Yes/No)

Patient self-reported pain
at baseline, 6 and 12
months

Primary:
Baseline to 3
months

Secondary:
Baseline to 6

and 12 months

Determine whether the
active interventions
result in a higher
proportion of patients
achieving a MCID in
pain-related interference

Minimal clinically important
difference (MCID) in pain
intensity is defined as a 30%
decrease in score on 7-item
pain-related interference
subscale of the Brief Pain
Inventory — Short Form (BPI-
SF)°42 from baseline (Binary;
Yes/No)

Patient self-reported pain
at baseline, 6 and 12
months

Primary:
Baseline to 3
months

Secondary:
Baseline to 6

and 12 months

10


```

### Physical PDF page 23 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

Secondary Objectives Brief Description of Measure Outcome Measured By Time Frame

Examine the impact of Brief Pain Inventory — Short Patient self-reported pain | Primary

the active interventions Form (BPI-SF)*°“? (11 items; at baseline, 3, 6 and 12 Baseline to 3

on pain severity continuous) months months
Secondary
Baseline to 6

and 12 months

Examine the impact of
the active interventions
on pain intensity

Pain intensity subscale of the
BPI-SF (4 items; continuous)

Patient self-reported pain
at baseline, 3, 6 and 12
months

Primary
Baseline to 3
months

Secondary
Baseline to 6

and 12 months

Examine the impact of Pain-related interference Patient self-reported pain | Primary
the active interventions subscale of the BPI-SF (7 items; | at baseline, 3, 6 and 12 Baseline to 3
on pain-related continuous) months months
interference
Secondary
Baseline to 6
and 12 months
Examine the impact of PROMIS Ability to Participate in Patient self-reported Primary
the active interventions Social Roles 4A“4 (4 items; social role functioning at Baseline to 3
on social role functioning | continuous) baseline, 3, 6 and 12 months
months
Secondary
Baseline to 6

and 12 months

Examine the impact of
the active interventions
on physical functioning

PROMIS Physical Functioning
Short Form 6b (6 items;
continuous)

Patient self-reported
physical functioning at
baseline, 3, 6 and 12
months

Primary
Baseline to 3
months

Secondary
Baseline to 6

and 12 months

Examine the impact of
the active interventions
on patient global
impression of change
(PGIC)

Guy/Farrar Patient Global
Impression of Change (1 item
each for pain status and overall
status)

Patient self-reported
impression of change at 3,
6 and 12 months

Primary
Baseline to 3
months

Secondary
Baseline to 6
and 12 months

11


```

### Physical PDF page 24 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

3.3 Economic Evaluation Objectives
Economic Evaluation Brief Description of Measure Outcome Measured By Time Frame

Objectives

Assess the costs and
incremental cost-
effectiveness of the
active interventions
compared to each other
and usual care

Costs based on health care
utilization and intervention costs
will be assessed.

Using the framework of cost-
effectiveness, the incremental
cost per additional patient with a
MCID in pain severity (30%
reduction from baseline) will be
estimated at 12 months, and the
quality-adjusted life year (QALY)
gained—utilities will be
estimated using the EQ-5D-5L.*°

Health care utilization
costs: EHR data costed
using standard costing
algorithms*®4” and
Medicare fee schedules

Intervention costs:
Process data related to all
relevant resources used in
the intervention delivery

EQ-5D-5L: Patient self-
report at baseline, 3-, 6-
and 12-months

Baseline to 12
months

12


```

### Physical PDF page 25 — OCR locator

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

3.4

Exploratory (Tertiary) Objectives

Exploratory Objectives

Brief Description of Measure

Outcome Measured By

Time Frame

Examine the impact of
the active interventions
on long-term opioid use

Opioid prescription orders or fills
indicating a continuous 2 60-day
supply during the prior 90-day
period; account for prescriptions
prior to 90-day look-back which
carry into the assessment period
(Binary)

Electronic health record
(EHR) opioid prescription
data assessed quarterly

90-day periods for

quarterly variables
(Baseline survey date = Day 0)
Baseline = Day -89 to day -0

3 months = Day 1 to day 90

6 months = Day 91 to day 180

9 months = Day 181 to day 270
12 months = Day 271 to day 360

Baseline to 3, 6
and 12 months

Examine the impact of
the active interventions
on depression
symptomology

Patient Health Questionnaire-8
(PHQ-8)'8 (8 items; continuous)

Patient self-reported
depression
symptomatology at
baseline, 3, 6 and 12
months

Baseline to 3, 6,
and 12 months

Examine the impact of
the active interventions
on anxiety
symptomology

Generalized Anxiety Disorder-7
(GAD-7)? (7 items; continuous)

Patient self-reported
anxiety symptomatology
at baseline, 3, 6 and 12
months

Baseline to 3, 6,
and 12 months

Examine the impact of
the active interventions
on sleep disturbance

PROMIS Sleep Disturbance —
Short Form 6a® (6 items;
continuous)

Patient self-reported sleep
disturbance at baseline, 3,
6 and 12 months

Baseline to 3, 6,
and 12 months

Examine the impact of
the active interventions
on high impact chronic
pain and graded chronic
pain

High Impact Chronic Pain*>"

Graded Chronic Pain Scale-
Revised*"

Patient self-reported pain
intensity, duration, and
pain-related disability

Baseline to 3, 6,
and 12 months

The following moderators will be assessed related to MCID in pain severity at 6 months.

Black or African American/Non-Hispanic,

Hispanic
Other

Moderator Definition Data Source

Sex Male vs. Female/Other Patient self-report at baseline
Sex at birth as reported by subject; assessed
using HEAL CDE Demographic question

Age <65 vs. 2 65 years old EHR data

Race/Ethnicity White/Non-Hispanic Patient self-report at baseline

13


```

### Physical PDF page 26 — OCR locator

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

Moderator

Definition

Data Source

Rural/medically
underserved residency

Urban vs. Rural/medically underserved

Rural is defined as subject’s resident Census
Tract corresponds to US Census 2010 Rural-
Urban Commuting Area (RUCA) Codes 4, 5,
6, 7, 8, 9 or 10
(https.//www.ers.usda.gov/data-products/rural-
urban-commuting-area-codes/documentation/)

Medically underserved is defined as subject's
resident Census Tract corresponds to HRSA-
designated primary care or mental health
geographic or geographic high needs health
professional shortage area

(https://data. hrsa.gov/tools/shortage-
area/hpsa-find)

EHR patients’ geocoded data
extracted at baseline

Multiple non-malignant
musculoskeletal pain
conditions

1 pain cluster vs. >1 pain cluster

> 1 pain-related ICD-10 diagnosis

corresponding to more than one (>1) of the

non-malignant musculoskeletal chronic pain

condition clusters developed for the National

Pain Strategy chronic pain condition clusters®?

1. Back pain

2. Neck pain

3. Limb/extremity pain, joint pain, and
arthritic disorders

4. Fibromyalgia

5. Headache

6. Orofacial, ear, and temporomandibular
disorder pain

7. Musculoskeletal chest pain

8. General pain subcategory of the Other
painful conditions cluster

EHR data; diagnoses in patient's
EHR extracted at baseline for prior
360 days

Mental health mood
disorders

ICD-10 diagnosis for depression and/or
anxiety diagnosis

EHR data; diagnoses in patient's
EHR extracted at baseline for prior
360 days

Negative social
determinants of health
(SDH)

Negative SDH/existing need vs. No SDH need
Patient endorses need in one or more of the
following domains:
1. Financial Resource Strain (1 item)
2. Food Insecurity (2 items)
3. Transportation/Access
Needs (2 items)
4. Housing Instability (3 items)

Patient self-report at baseline

14


```

### Physical PDF page 27 — OCR locator

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

The following mediators will be assessed related to MCID in pain severity at 6 months.

Mediator

Brief Description of Measure

Measured By

Pain catastrophizing

Pain Catastrophizing Scale (PCS)- Short
Form 6% (6-item; continuous)

3 months

Patient self-report at baseline and

Pain self-efficacy

Self-Efficacy for Pain Management subscale
of the Chronic Pain Self-Efficacy Scale (5-
item; continuous)

3 months

Patient self-report at baseline and

Perceived support

2 items developed in UG3 phase

Patient self-report at notification of
randomization and 3 months

3.5

Qualitative Evaluation Objectives

Qualitative Evaluation Objectives

Measured By

Time Frame
during the 4-year
UH3 study period

Understand health system issues,
including adaptations and contextual
factors at the site and external levels,
barriers and facilitators to intervention
success and potential for adoption,
sustainability, and dissemination
from perspective of health care
systems

Interviews with health care system
stakeholders (including referring
clinicians) using semi-structured interview
guides designed to assess relevant domains.

Conducted in
years 4-5 of study

Understand patient experiences of the
interventions, including how they relate
to treatment response, variability by
site, and rurality/medically underserved
residency status

Interviews with a purposeful sample of
patients who participate in the active
interventions, stratified by site, active
intervention (online program vs. virtual coach-
led), response to treatment, and
rurality/medically underserved residency
status. Interviews will use semi-structured
interview guides designed to assess relevant
domains.

e Interviews at 3-5 months will focus on
participants’ experience with the
intervention and intentions to change
or maintain changes learned from the
intervention

« — Interviews at 12-14 months will focus
on participants’ maintenance of
behavioral skills practice since
intervention, and changes in domains
likely affected by treatment.

Conducted in
years 1-3 for 3- to
5-month
interviews

Conducted in
years 2-3 for 12-
to 14-month
interviews

15


```

### Physical PDF page 28 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022
Qualitative Evaluation Objectives Measured By Time Frame

during the 4-year
UH3 study period

Understand patient experiences
related to discontinuation of the
intervention

Interviews with a sample of patients who did
not complete the active interventions to
which they were randomized (but are still
enrolled in the study) using a semi-structured
interview guide designed to assess relevant
domains

Conducted in year
1

Process evaluation of trial
implementation and delivery, including
barriers and facilitators to
accomplishing aims, lessons learned
and changes to planned activities.

Interviews with intervention staff/health
coaches to chronicle the process of trial
implementation and delivery

Conducted years
1 and 3 of study

16


```

### Physical PDF page 29 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

4 STUDY DESIGN
41 Overall Design

This phase III, randomized, comparative effectiveness research trial will evaluate two CBT-
based chronic pain treatments delivered via different remote modalities: 1) an established
online, CBT-based program (painTRAINER), and 2) a centralized, virtual coach-led CBT-CP
intervention. Both modalities will be compared to usual care services.

The study uses a three-arm, parallel intervention design. Participants will be recruited from the
populations of four integrated health care systems which serve as the clinical sites: 1) Kaiser
Permanente Georgia (KPGA), 2) Kaiser Permanente Northwest (KPNW), 3) Kaiser Permanente
Washington (KPWA) and 4) Essentia Health in Minnesota, North Dakota, and Wisconsin.

4.2 Study Arms

The three study arms to which participants will be randomized for the UH3 randomized clinical
comparative effectiveness trial will be: 1) The painTRAINER online, CBT-based, pain coping
skills training (PCST) program, 2) Virtual CBT-CP delivered by health coaches, and 3) Usual
care. See section 10 for details on study arms 1 and 2 (the active interventions).

Those randomized to the usual care arm of the study will be mailed a bound copy of the 2020
edition of the American Chronic Pain Association Resource Guide to Chronic Pain
Management.*®

Patients randomized to either of the active intervention arms or the usual care arm of the study
can receive any pharmacologic and nonpharmacologic treatments available to them without
restriction during the study period.

4.3 Study Arm Assignment/Randomization

After completion of the baseline data collection, study participants will be individually
randomized in equal ratio to one of the three study arms.

Randomization will be stratified on:

Variable Source

Sex Sex from electronic health record (Male vs.
Female or Other)

Pain severity score Score on BPI-SF from baseline survey (< 7
vs. 27)

Clinical site KPWA, KPNW, KPGA, Essentia

Rural/medically underserved residency Residency geocode for Census Tract from
electronic health record

Within each stratum, to contain concealment and balance randomization over time, a random
permutated block design will be used with random variable block sizes of 3, 6, or 9 to ensure
approximately equal accrual into the three study arms.

17

```

### Physical PDF page 30 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

The TIN JHU/Tufts Lead biostatistician, in collaboration with the study Biostatistician, will
develop the randomization scheme and the TIN Utah DCC will implement the scheme by
developing the randomization tables, which will be provided to KP CHR for integration into the
electronic data capture system.

Randomization will occur within the KP CHR-hosted electronic data capture system after
baseline assessment completion.

4.4 Scientific Rationale for Study Design

An enhanced usual care study arm has been included to address the critical question: What is
the incremental benefit of the study interventions over what treatments patients are already able
to access to help manage their pain? This is important to understand from a research, cost-
analysis, health care-implementation and dissemination perspective. The study team recognizes
that those motivated to join the study have effectively expressed an interest in obtaining
additional resources for helping them manage their pain so those randomized to the usual care
study arm will be sent a bound copy of the 2020 edition of the American Chronic Pain
Association Resource Guide to Chronic Pain Management. This is a detailed informational
guide to medical, interventional, behavioral, pharmacological and rehabilitation therapies, that
can serve as a helpful, up-to-date resource to recipients for considering a broad range of
treatment and self-management options that might help with their needs.

4.5 Justification for Interventions

Online, CBT-based pain coping skills training (PCST) program. Multiple meta-analyses support
the efficacy of web-based CBT-CP interventions for improving pain and pain-related
impairment.22©.°° Although overall effect sizes are modest, these reviews suggest the potential
impact of these treatment approaches with respect to lower costs and greater safety than
pharmacologic pain treatments. painTRAINER has been shown to be effective in a number of
studies with high completion rates compared to other studies.5’° painTRAINER uses a novel
approach by incorporating the expertise of experienced CBT-CP clinicians into the program's
decision rules (tailoring algorithms) and knowledge database to retain critical therapeutic
features of in-person CBT-CP.™ In a randomized control feasibility trial of painTRAINER,
participants demonstrated increases in self-efficacy from baseline to post intervention compared
with the control group (effect size d=0.43), and women who completed the program had
reduced pain compared to those in the assessment-only control condition (effect size d=0.33).
The study sample included those who might be considered to have significant barriers to using
online programs, including older adults (mean age of 68, range 38-90 years), minorities (35%
African American), and people largely from rural, low-income areas. Some had little computer
experience, and many had lower education levels (29% with high school education or less).
Importantly, 93% of participants agreed the program was easy to use, and 91% completed all 8
sessions, a much higher rate than for most online interventions, and many in-person CBT-CP
interventions. Overall, pain levels were mild to moderate in the feasibility trial sample, limiting
benefits and indicating a need for more rigorous screening to target persons with high impact
chronic pain. Screening procedures for the RESOLVE study are designed to ensure that
patients in the trial have greater potential for clinical benefit (i.e., they report their pain as more
disabling).

18

```

### Physical PDF page 31 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

Virtual coach-led CBT-CP (telephone/video). Large trials have demonstrated clinically meaningful
benefits of telephone-based CBT-CP for pain-related outcomes in the context of multicomponent
interventions.*°* |n a trial with 442 patients, evaluating telephonic CBT-CP and graded exercise
for treating chronic widespread pain (an often treatment-resistant pain variant), telephonic CBT-CP
was associated with substantial, statistically significant improvements in patient global assessment
at 6- (odds ratio [OR], 5.0; 95% confidence interval [Cl] 2.0 to 12.5) and 9-month (OR, 5.4; 95% Cl
2.3-12.8) follow-ups.°° The PPACT trial used substantial telephone-based CBT-CP delivery for
patients experiencing barriers to in-person treatment. This care was highly acceptable to patients
and feasible for master's-level, trained clinicians to reliably deliver. Finally, KPWHRI has a long
history of developing successful and highly deployable telephone interventions with national uptake
to provide behavioral treatment for depression and smoking.”°?9°67 Two small trials of telephonic
CBT-CP had negative results: one was markedly underpowered and the other tested an intervention
that did not emphasize behavioral activation,®° deficiencies which will be addressed in the
RESOLVE virtual intervention. Although this arm of the trial was initially planned as a primarily
telephone-based intervention, following the Covid-19 outbreak, the health care systems in which this
study is being conducted, like many across the country, are pivoting towards remote delivery of
health care.*° In this rapidly evolving treatment landscape in the participating, video-visits are
preferred to telephone-visits because they are widely seen to be more satisfactory for patients given
the better approximation of in-person visits as well as the additional utility of being able to share
materials and see face and body language (Permanente Medicine staff communication, 4/16/20).
Given that these video visits are quickly becoming the standard of care, together with findings from
our pilot intervention that highlighted limitations of discussing key CBT-CP tools without being able
to visually share, video visits when available and acceptable for patients will be provided.

4.6 End-of-Study Definition

A clinical trial is considered completed when participants are no longer being examined or the last
participant's last study visit has occurred. Therefore, the study will be complete when the last
participant has completed their 12-month follow-up assessment and any scheduled qualitative
interviews which will occur up to 14 months follow-up from study randomization.

19

```

### Physical PDF page 32 — OCR locator

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

5 STUDY POPULATION
5.1 Participant Inclusion Criteria

This study will primarily employ a population-based recruitment approach in which the
individuals who are invited/recruited to potentially participate in the study will be identified based
on the following electronic health records (EHR)-based criteria. In addition, health care
providers can refer patients to the study; however, any patient referred must meet the same
criteria described below.

Individuals must first meet these EHR-based criteria in order to be invited to be screened for
participation.

1. Active/enrolled in one of the 4 participating integrated health care systems at the
time of query and for the prior 360 days

2. Age 18 years or older (based on date of birth documented in EHR)

3. English speaking or do not need interpreter services

4. Have at least one [at Essentia] or at least two which are >60 days apart [at KP
sites] outpatient pain-related health care encounter with nonmalignant
musculoskeletal pain diagnoses [as determined by ICD10 codes for any of the
following: back- neck-, limb/extremity-, joint-pain, arthritic disorders, fibromyalgia,
headache, orofacial/ temporomandibular pain, or musculoskeletal pain]®? within
the past 360 days

5. Do not have an encounter for surgery related to common musculoskeletal pain
conditions (e.g., joint replacement, spinal fusion, carpal tunnel release surgery)
[as determined by CPT and/or ICD-10 codes] within the past 60 days

6. Do not have two or more separate encounters with a malignant cancer diagnosis
other than non-melanoma skin cancer [as determined by ICD-10 codes] within
past 60 days

7. Do not have ICD-10 code(s), CPT code(s) or department/provider encounters
indicating receipt of hospice or other palliative care within the past 360 days

8. Do not have ICD-10 codes indicating severe cognitive impairment precluding
participation in a behavioral lifestyle change program

[Note: At the KPWA site only, one additional EHR-based exclusion criterion will be applied,
which is: Do not have ICD-10 codes indicating opioid use disorder (OUD). This criterion is being
applied because there is another HEAL study being conducted at KPWA that focuses on
treating individuals with pain and OUD specifically.]

Individuals who meet the above EHR criteria will be invited to respond to screening questions
and must meet the following inclusion criteria:

1. Have high-impact chronic pain (as indicated by self-report of having pain on most
or every day in past 3 months and pain limiting life or work activities on most or
every day in past 3 months)*

2. Have persistent pain (as indicated by self-report PEG score of 2 12)

3. Be able to participate in either of the active interventions (i.e., have internet and
phone access required for accessing treatments)

20

```
# DOC-002 protocol evidence, physical PDF pages 33–64

## Scope and derivation

Fresh disjoint support mapping; PLAN by prospective protocol content. Exact source: `joi250046supp1_prod_1755300121.14087.pdf`; RESOLVE UH3 Protocol Version 5.0, 10 Nov 2022. Physical PDF pages 33–64 correspond to printed protocol pages 21–52. No source or reused asset was modified. No other source units or earlier scientific conclusions were read.

Engines: direct Poppler 26.01.0 `pdftotext` native and layout extraction for pages 33–64 produced `preprocessing/protocol_b/native.txt` and `layout.txt`; font encoding is unreadable. Direct Poppler 26.01.0 `pdftoppm -f 33 -l 64 -r 160 -png` produced `preprocessing/protocol_b/page-33.png` through `page-64.png`. Direct Tesseract 5.5.0, `OMP_THREAD_LIMIT=1`, English, `--psm 3`, CPU, produced corresponding `ocr-33.txt` through `ocr-64.txt`; `ocr_engine.log` records engine messages. OCR is a locator/transcription aid; source pages remain final authority. Each page has been opened through fresh extraction; numeric tables/symbols needing clarification receive visual source checks below. Keys P-B are local mapping keys, not candidate IDs.

All evidence links below are relative to this part artifact. If this artifact is merged, the coordinator must rebase source links to the merged artifact's depth.

## Planned quantitative relationship map

| Local key | Physical pages | Main-paper matching key | Planned quantitative relationship and exact operative content |
|---|---|---|---|
| P-B001 | 33,37 | Eligibility/analysis population | Exclude CBT for pain or comparable training during past6 months, current/planned next month, current/planned intensive substance-use treatment next month, and scheduled pain-related surgery next12 months. Screening high-impact chronic pain: pain most/every day past3 months AND limits life/work most/every day past3 months. PEG3-item score ≥12. Visual page37 confirms ≥; OCR `212` is a transcription limitation. |
| P-B002 | 34 | Planned recruitment/randomized population | Exact note: “The study aims to randomize 2,331 individuals (at least 777 per arm)” and number enrolling may exceed2,500 because not all enrollees randomize. Each of4 sites initially approximately595–625 patients, allowed to vary. |
| P-B003 | 34 | Rural/MUA moderator | Recruitment stratified urban versus rural/MUA; urban Census2010 RUCA1,2,3; rural4–10; MUA HRSA primary-care/mental-health geographic or geographic-high-needs shortage area. Approximately500–700 invitations/month/site. Rural/MUA overall30–50%; every site at least20% in either subgroup to support subgroup analyses. |
| P-B004 | 35,36,47,48 | Qualitative secondary/process outcomes | Approximate100–120 patient interviews:20 early intervention noncompleters/low engagement (2–5 sessions), approximately100 selected by clinical site, active arm,3-month BPI-SF response, and rural/MUA; latter interviews3–5 and12–14 months. Up to20 stakeholders, approximately8 leadership/up to12 referrers; approximately12 intervention staff interviewed twice. Administrative/process scope; not randomized efficacy denominator. |
| P-B005 | 36,47 | Assessment schedule/retention | Baseline and3-,6-,12-month assessments. Incentive table: phone25/30/35/40 dollars; paper N/A/30/35/40; web25/35/40/45. Patient interview30 dollars. Baseline consent+assessment45–60min; randomization-notification perceived support paper survey≤5min; follow-up survey approximately30min. These timing/incentive values are not endpoint effect measures. |
| P-B006 | 41 | Discontinuation, retention and exposure | Withdrawal retains collected data. Active-intervention loss to follow-up: missed2 or more weekly sessions OR unable to reach after up to7 calls/emails and2 letters over4–6 weeks. Intervention loss to follow-up does not discontinue assessment outreach unless no working contact details. |
| P-B007 | 42–45 | Randomized intervention content, dose, duration | Both active arms share8 session topics. Session1 rationale/foundation self-care/relaxation;2 progressive muscle relaxation and mini-practice;3 activity/rest cycling;4 pleasant activity scheduling/negative automatic thoughts;5 negative automatic thoughts/coping thoughts;6 pleasant imagery/distraction;7 problem solving;8 monitoring for maintenance. Both columns checked for every row, visually confirmed p42. Footnote: goal setting session1; review/refinement sessions2–8. painTRAINER45–60min/session; coach-led60min one-to-one phone/video. Intended1 weekly session over8 weeks; maximum intended active period12 weeks. Full dose at least75%=6/8 sessions. |
| P-B008 | 43 | Intervention modification/onboarding | Page43 explicit dated note: “On 08/09/21 VUMC IRB approved revised onboarding guidelines which added motivational interviewing-based language. This language was to be used, as feasible.” Automated reminders plus staff outreach if first session uninitiated>7 days after registration, session remains incomplete>7 days, new session not initiated>10 days after last completion, or≥3 sessions in9 days. |
| P-B009 | 44,45 | Delivery duration/adherence | Coach onboarding approximately1 week after materials mailed; coach reminders1–2 days before session. After12 weeks, no further staff prompting or telephonic/video scheduling, except engaged coach participants requesting near-target completion with supervisor approval; postperiod contacts flagged analytically. painTRAINER remains accessible after12 weeks and automatically logs later use. |
| P-B010 | 45,46 | Masking/concomitant treatment | Participants/intervention staff unmasked, outcome assessors and paper-survey entry staff masked. No restrictions on pharmacologic/nonpharmacologic care after enrollment. Other CBT assessed at3-,6-,12-month follow-up. Coach initial training approximately16h;2 role-plays per8 sessions=16 mock sessions; first4 months review≥2 encounters/session from first5 patients, subsequent monthly ratings. |
| P-B011 | 49–51 | Safety outcome ascertainment | AEs not uniformly solicited; self-reported events recorded. SAEs defined deaths/inpatient hospitalizations during active participation; pre-enrollment planned hospitalization excluded. EHR systematically assessed every6 months aligned DSMB meetings; independent physician reviews each death/hospitalization. No solicited AESIs; page50 states differential contact opportunities preclude meaningful between-group AE comparisons. Historical PPACT850 participants/12 deaths/287 hospitalizations(116 intervention,171usual care) is background only, not RESOLVE outcomes. |
| P-B012 | 53 | Interim/stopping | DSMB before enrollment then every6 months; may recommend continuing/modifying/terminating. Halting rule: DCC notifies chair when unexpected SAEs related to procedures/intervention occur; chair recommends temporary suspension/enrollment/intervention and ad-hoc meeting if warranted. No numeric efficacy boundary on this page. |
| P-B013 | 55 | Primary outcome/sample size/power/multiplicity | Primary MCID=30% reduction overall BPI-SF pain severity baseline→3 months; two-sided independent proportions,90% power; Fisher least significant difference with omnibus Wald test for any three-group difference then pairwise tests conditional on global significance at alpha0.05. UC15%, intervention22.5%, detectable7.5 percentage-point difference; printed relative change150%. Required1,863=621/arm;80% retention; at least2,331=777/arm randomized. |
| P-B014 | 55,56 | Moderator power | Table title “Power for Subgroup Analyses Ranging the Size of the Subgroup”;80% power. N372(20% of1,863), UC15.0%, intervention31.0%, difference16.0%, relative change206.7%; N558(30%),15.0%,27.7%,12.7%,184.7%; N744(40%),15.0%,25.8%,10.8%,172.0%. Relative-change column explicitly `% Int / %UC`, visual confirmed. Prior sex/mental-health subgroups≥40%; rural/MUA target≥20%; negative social determinants exploratory due unknown prevalence. |
| P-B015 | 56 | Analysis population/significance | “All analyses will be conducted following an intent-to-treat approach, including all individuals randomized regardless of their engagement with or exposure to the intervention.” All intervals and P values two-sided; significance0.05. Baseline categorical percentages; continuous mean/SD. No missing-data method is specified in this assigned shard; section15 points to supplied SAP for detailed analyses. |
| P-B016 | 56 | Primary model/timepoint/covariates | Modified Poisson regression fit using GEE for binary MCID30% pain-severity reduction at3(primary),6/12(secondary) months. Arm×time indicators estimate time-specific effects; intervention versus UC3-month primary. Covariates baseline pain severity; stratification variables sex,clinical site,rural/MUA; a priori predictive variables multisite pain and co-occurring mental-health condition. |
| P-B017 | 57 | Secondary outcome status/model | Aim1a: continuous overall pain severity; pain intensity(MCID and overall); pain interference(MCID and overall); social role functioning,physical functioning,patient global impression of change. Primary timepoint3 months, secondary6/12. Linear regression continuous outcomes; Poisson binary/count outcomes; arm×time interactions; baseline pain severity and all stratification variables as covariates. Exact claim “Analyses of secondary outcomes (Aim 1a) will follow the same proposed approach as Aim 1.” |
| P-B018 | 57,58 | Prespecified subgroup moderators | Sex,age,race/ethnicity,rural/MUA,multiple pain conditions,mental-health mood disorders,negative social determinants. Each assessed separately; moderator main effect and moderator×intervention×follow-up-time interaction; primary Aim1b comparisons interaction terms at3 months. Hypothesis more complex conditions(mood/anxiety,multisite pain) or challenging social/environmental factors(rural/MUA/unmet needs) favor telephonic coach over online. |
| P-B019 | 58 | Mediators | Changes baseline→3 months in pain catastrophizing,pain-related self-efficacy,perceived support hypothesized mediate6-month outcomes in both active arms. Primary mediation6-month binary MCID pain-severity outcome; explanatory secondary mediation6-month secondary outcomes. |
| P-B020 | 58,59 | Economic endpoint/analysis | Aim2 economic analysis only Kaiser sites with complete utilization capture. Incremental cost/additional MCID patient at12 months and QALY gained(EQ-5D-5L). Health-plan perspective; total/pain-specific care plus implementation/delivery costs. Net-benefit regression: visually printed `nb_i = λ·effect_i − cost_i`; λ willingness-to-pay varied for CEAC, example30,000–100,000 dollars/QALY. Sensitivity costs to other settings,replication,economies of scale; health-care costs GEE appropriate links. Cost table has blank pain-related/total columns, not results; categories prescription,primary care,PT/OT/physiatry,pain clinic,mental/behavioral/addiction,ER/urgent care,other specialty,inpatient. Footnotes medication classes/pain diagnostic codes; pain hospitalizations primary/principal pain-related ICD-10-CM. |
| P-B021 | 59,60 | Exploratory outcome status/interim | Exploratory long-term opioid use,depression,anxiety,sleep disturbance,high-impact chronic pain,graded chronic pain; same approach as secondary outcomes. Safety monitoring twice/year. “There are no planned interim analyses of primary or secondary outcome data before the study is completed.” DSMB-requested estimates permitted for evaluating safety; “No formal futility or effectiveness interim analyses will be conducted.” |
| P-B022 | 61,62 | Process/reach denominators | Qualitative Aim3 EPIS/RE-AIM/TFA; reach percentages excluded and reasons; participation denominator all approached in each health system, plus all potentially eligible health-plan patients irrespective approach. Implementation adherence automated painTRAINER logging or coach-collected data. Qualitative text coding/thematic comparisons; no additional efficacy model/estimate. |

### Exact statistical source quotes

- Page55: “specifically conduct Omnibus Wald Test for any difference between three groups and then conduct pairwise comparisons given an overall difference is statistically significant at the 0.05 alpha level”.
- Page56: “Modified Poisson regression ... fit using generalized estimating equations (GEE) will be used to model the binary primary outcome, MCID in pain severity (30% reduction from baseline), 3 months (primary time point) and 6 and 12 months (secondary time points).” Citation superscripts omitted in this locator quote; no numeric value omitted.
- Page56: “Adjustment will be made for baseline levels of pain severity, other stratification variables (sex, clinical site, and rural/medically underserved residency), and a priori variables predictive of outcome (multisite pain and co-occurring mental health condition).”
- Page57: “baseline levels of pain severity and all stratification variables will be included as covariates.”
- Page60: “No formal futility or effectiveness interim analyses will be conducted.”

## Complete page coverage

| Physical PDF page | Printed page | Coverage disposition | Result-relevant content mapped |
|---|---:|---|---|
| 33 | 21 | COMPLETE | Exclusion windows; P-B001 |
| 34 | 22 | COMPLETE | Recruitment/randomized target, geographic definitions/subgroup sampling; P-B002,P-B003 |
| 35 | 23 | COMPLETE | Recruitment pathways, qualitative strata/timing/sample; P-B004 |
| 36 | 24 | COMPLETE | Stakeholder/staff sample, retention incentive table; P-B004,P-B005 |
| 37 | 25 | COMPLETE | Population thresholds/eligibility; P-B001 |
| 38 | 26 | COMPLETE | Consent/administrative EHR screening; no additional applicable quantitative analysis |
| 39 | 27 | COMPLETE | Consent/enrollment administrative; no additional applicable quantitative analysis |
| 40 | 28 | COMPLETE | Interview consent administrative; no additional applicable quantitative analysis |
| 41 | 29 | COMPLETE | Withdrawal/data retention, exposure versus assessment loss to follow-up; P-B006 |
| 42 | 30 | COMPLETE | Eight-session common content table/footnote; P-B007 |
| 43 | 31 | COMPLETE | painTRAINER delivery/dose,dated onboarding modification,outreach rules; P-B007,P-B008 |
| 44 | 32 | COMPLETE | Coach-led delivery/dose/outreach; P-B007,P-B009 |
| 45 | 33 | COMPLETE | Active duration/full-dose definition,postperiod access,masking; P-B007,P-B009,P-B010 |
| 46 | 34 | COMPLETE | Fidelity/concomitant care follow-up; P-B010 |
| 47 | 35 | COMPLETE | Assessment timepoints,randomization-notification mediator,qualitative timepoints; P-B004,P-B005 |
| 48 | 36 | COMPLETE | Qualitative stakeholder/staff timing; P-B004 |
| 49 | 37 | COMPLETE | AE/SAE definitions,ascertainment,historical PPACT background; P-B011 |
| 50 | 38 | COMPLETE | Systematic SAE6-month assessment,no solicited AESIs; P-B011 |
| 51 | 39 | COMPLETE | AE/SAE expectedness/reporting,UP definitions; P-B011 |
| 52 | 40 | COMPLETE | UP reporting administrative; no additional applicable quantitative analysis |
| 53 | 41 | COMPLETE | DSMB timing/suspension rules; P-B012 |
| 54 | 42 | COMPLETE | Clinical-site monitoring administrative; no numeric statistical boundary or additional applicable quantitative analysis |
| 55 | 43 | COMPLETE | Primary sample/power assumptions,multiplicity,subgroup power table; P-B013,P-B014 |
| 56 | 44 | COMPLETE | ITT,two-sided significance,primary hypothesis/model/covariates; P-B014,P-B015,P-B016 |
| 57 | 45 | COMPLETE | Secondary outcomes,status,model and moderator structure; P-B017,P-B018 |
| 58 | 46 | COMPLETE | Moderator3-month tests,mediators,economic methods/formula; P-B018,P-B019,P-B020 |
| 59 | 47 | COMPLETE | Economic cost table/footnotes,exploratory outcomes,safety analyses; P-B020,P-B021 |
| 60 | 48 | COMPLETE | No planned interim efficacy/futility analyses; P-B021 |
| 61 | 49 | COMPLETE | Qualitative frameworks/reach denominators/adherence; P-B022 |
| 62 | 50 | COMPLETE | Qualitative text-analysis continuation; P-B022 |
| 63 | 51 | COMPLETE | Source/data origins,EHR/self-report/recordings; no new numeric efficacy specification |
| 64 | 52 | COMPLETE | Website use-data security; no additional applicable quantitative analysis |

## Complete fresh page-keyed transcription

The following preserves all fresh OCR output, including references and administrative content, so later reviewers can locate every quantitative statement without relying on mapper selection. OCR glyph/spacing issues are unnormalized here; visual corrections above are authoritative transcriptions for PEG ≥12, all intervention table checks, subgroup power table/formulas, economic lambda/subscript formula, and incentive-table alignment. No efficacy results are reported in this PLAN shard. Source pages contain no workbook formulas/cached values or CSV/DOC unit locations.

### DOC-002 physical page 33

[Direct source page 33](../../../joi250046supp1_prod_1755300121.14087.pdf#page=33)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

5.2 Participant Exclusion Criteria

Individuals screened who meet the inclusion screening criteria (and the initial EHR criteria
described above) cannot endorse any of the following exclusion criteria:

1. Have received CBT for pain or pain-related psychoeducation or behavioral skills
training within in the past 6 months (in-person, by phone or videoconference, or
online)

2. Currently receiving or will be starting CBT for pain or pain-related
psychoeducation or behavioral skills training in the next month (in-person, by
phone or videoconference, or online)

3. Currently receiving or will be starting inpatient or intensive outpatient services for
substance use disorder in the next month

4. Have a planned/scheduled surgery in next 12 months related to pain condition

21

```

### DOC-002 physical page 34

[Direct source page 34](../../../joi250046supp1_prod_1755300121.14087.pdf#page=34)

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

6 RECRUITMENT PROCEDURES AND RETENTION STRATEGIES

6.1 Recruitment of Patients

Each of the 4 sites will be responsible for recruiting and enrolling approximately 595-625

patients per site but the final number will vary slightly across sites. In order to reach the overall
study target for number randomized within the study timeline, some sites may enroll more than
others (i.e., Essentia and KPGA vs. KPWA). [Note: The study aims to randomize 2,331
individuals (at least 777 per arm) and, as such, the number needed to enroll may be larger than
the 2,500 target as not all who consent/enroll go on to be randomized.] Study activities from
recruitment through completion of baseline survey will be completed by each site for their
population of patients.

For recruitment, each site will query their EHR data warehouses to identify a sample of patients
who meet the EHR-based inclusion criteria on a set frequency. The sample of patients will be
stratified by urban vs. rural or medically underserved residence, based on the individuals’
resident Census Tract/geocoded data in the EHR. The table below provides definitions to be
used for these categories.

Urban Rural or Medically Underserved (MUA)

Urban is defined as subject's resident Census
Tract corresponds to US Census 2010 Rural-
Urban Commuting Area (RUCA) Codes 1, 2 or 3
(https:/www.ers.usda.gov/data-products/rural-
urban-commuting-area-codes/documentation/)

Rural is defined as subject's resident Census
Tract corresponds to US Census 2010 Rural-
Urban Commuting Area (RUCA) Codes 4, 5, 6, 7,
8, 9 or 10 (https:/Avww.ers. usda.gov/data-
products/rural-urban-commuting-area-

codes/documentation/)

Medically underserved (MUA)is defined as
subject's resident Census Tract corresponds to
HRSA-designated primary care or mental health
geographic or geographic high needs health
professional shortage area
(https:/data.hrsa.gov/tools/shortage-area/hpsa-
find)

Then, a random sample of approximately 500-700 patients per month per site will be generated,
with adjusted sampling for rural residency to ensure at least 20% in either the urban or
rural/MUA subgroup at each site. Specifically, individuals who reside in rural or medically
underserved areas will comprise 30-50% of the overall RESOLVE study population. Each site
will have at least 20% enrollment in either subgroup (urban vs. rural/MUA) to enable sufficient
sample size for subgroup analyses.

Patients in the random sample will be mailed a recruitment letter and brochure which includes: a
description of the study, instructions for how to call a research staff person to complete the
screening survey by phone or complete it online, and select elements of informed consent,
including a clear statement of the ability to opt out of further contact by calling the site-specific
study telephone number. Finally, the letter states that patients might be contacted by phone in
the following weeks to participate in the study if they have not called to opt-out of further contact
or gone online to complete the screening survey. Each site, as feasible/allowable, will also send

22

```

### DOC-002 physical page 35

[Direct source page 35](../../../joi250046supp1_prod_1755300121.14087.pdf#page=35)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

a recruitment email in follow-up to the mailing to patients in the sample who have an active
email address. See section 7 for a complete description of the screening process.

The population-based recruitment process described above will be the primary method for
identifying potentially eligible patients for this trial. A secondary method will be by health care
provider or self-referral. Health care providers, including primary care providers, physical
therapists, health and wellness education staff, and others within the participating health care
system, will be given information about the study via multiple methods such as staff messaging,
staff intranet resources, and outreach/education at existing clinic and provider meetings. For
patients who agree, health care providers will be able to electronically route a referral to a study
staff member either within the EPIC EHR (that is linked to the patient’s record), by staff
message, or by leaving pertinent information (patient name and health record number for
retrieval of contact information) on a study-specific voicemail, accessible only by select study
staff. Then, study staff would ensure that the patient meets the EHR-based inclusion criteria (by
analyst executing a pre-developed program). Health care providers will also be able to provide
patients with information about the study (brochure) and the number of the study-specific
confidential voicemail so that patients can self-refer to the study or patients may obtain
information about the study on their own. Study staff would contact patients who self-refer,
obtain their permission to assess their EHR-based eligibility, and then the analyst would execute
the pre-developed program. If the person does not meet the EHR-based inclusion criteria, the
study staff person will follow-up with the patient by phone or mailed letter to explain this and call
or send a staff message back to the referring provider informing them. If the person does meet
the EHR-based inclusion criteria, the study staff member will notify the referring clinician of this
(if applicable), and the participant will then be mailed a recruitment letter and follow the same
process as described above for those identified through the EHR query.

In addition, a subset of approximately 100-120 patient participants will be invited to complete
interviews as part of the qualitative evaluation. Approximately 20 of these interviews will be
conducted once early in the launch of the UH3 trial with select participants randomized to the
active intervention arms who drop-out of intervention participation early (i.e., only complete 2-5
sessions) or are less consistent in their engagement with intervention activities; these
individuals have not withdrawn from the study. The remaining approximately 100 interviews will
be conducted with a subset of individuals randomized to the active intervention arms; sampling
for these interviews will be based on 1) clinical site, 2) active intervention arm, 3) treatment
response at 3 months (based on 3-month BPI-SF assessment), and 4) rural/medically
underserved vs. urban residency. This larger subset of interviewees will be recruited to
complete interviews at approximately 3-5 months and again at 12-14 months following
randomization. Individuals who are recruited for interviews will have endorsed their willingness
to potentially participate in the interviews on their baseline survey. The Utah Data Coordinating
Center (DCC) will work with the study team to provide a report of individuals to enable
stratification for interview sampling based on the criteria listed above. These individuals will first
be mailed a letter describing the goals of the interview, the process, and who to contact on the
study team if they are interested. Finally, the letter states that patients might be contacted by
phone in the following weeks about participating in an interview if they have not called to opt-in
or out of participating. Study staff will follow-up by phone and/or email to schedule interviews.

6.2 Recruitment of Stakeholders for Qualitative Evaluation

23

```

### DOC-002 physical page 36

[Direct source page 36](../../../joi250046supp1_prod_1755300121.14087.pdf#page=36)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

Recruitment of health care system stakeholders and referring clinicians. Up to 20 health care
system stakeholders will be interviewed, including select clinicians, from KPGA, KPNW, KPWA,
and Essentia in the areas of quality improvement, primary care, and/or pain management.
Stakeholders and clinicians will be identified by the research investigators at each site in
collaboration with health care system study partners based on their expertise and roles within
the health care system as it pertains to pain management / service delivery. Approximately 8
interviews will be with health care system leadership and up to 12 interviews with referring
clinicians across the health care systems if this option is used routinely. Targeted stakeholders
and clinicians will be sent a one-page fact sheet, which will include the consent elements that
are pertinent to the interview process, and invitation email from the site Pl or co-l, inviting them
to do an interview. If the individual agrees, they will be connected to the KP CHR qualitative
research team members who will schedule the interview.

Recruitment of intervention / health coaching staff for qualitative evaluation.

All (approximately 12) of the health coaching staff [centralized at KPWHRI (KPWA) and KP
CHR (KPNW)] who deliver the virtual intervention and the intervention staff who support
participant engagement with painTRAINER will be invited to complete study interviews with
members of the qualitative research team at KP CHR describing their experiences delivering the
study protocol and working with participants in the active intervention arms of the study.
Intervention staff / health coaches will be free to decline these interviews and will be told that
their names will not be attached to any data derived from this interview data.

See section 8 for a description of the consent processes for these individuals.

6.3 Retention Strategies

Retention of patients. The following strategies will be used to maximize follow-up rates: 1) allow
participants to complete assessments using the mode they prefer (online, by telephone, or a mailed
survey); 2) confirm and update contact details at each survey contact; 3) use standard tracking or
EHR/administrative records to locate persons who move; and, 4) provide incentives that adequately
compensate subjects for the time spent completing assessments (see table below) and increase as
subjects continue in the study. Specifically, participants will receive $25 at baseline and $30, $35,
and $40 at each follow-up time point respectively, if they complete by paper or phone, and $5
more at each follow-up time point for completing by web (with the rationale that the additional
funds compensate for the cost of broadband necessary to complete the assessments online).

Time Point
Completion Mode Baseline 3-month | 6-month 12-month
Phone $25 $30 $35 $40
Paper N/A $30 $35 $40
Web $25 $35 $40 $45

Patients who participate in the qualitative evaluation will receive $30 for each interview
completed.

24

```

### DOC-002 physical page 37

[Direct source page 37](../../../joi250046supp1_prod_1755300121.14087.pdf#page=37)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

7 ELIGIBILITY SCREENING

Patient screening process. Upon receiving the recruitment letter and brochure or recruitment
email (if applicable at the site), patients can choose to complete the eligibility screening survey
by web or call study staff at their specific clinical site to complete the questions by phone. In
addition, as described in section 6.1 on recruitment, study staff will also conduct outreach calls
to conduct eligibility screening with individuals who do not complete the screening by web or call
in on their own. The specific procedures for each screening mode are described below.

The eligibility screening survey will take approximately 10-15 minutes and assess the following
eligibility criteria:
e English speaking
Do not have a cognitive impairment severe enough to preclude participation in study
Be able to participate in either of the active interventions (i.e., have email, internet
and phone access required for accessing CBT-CP treatments).
« Meet the following definition of high impact chronic pain.
o Experience pain on most or every day of the past 3 months
AND
Pain limits life or work activities most or every day of the past 3 months
* Score 212 on the 3-item PEG assessment
e Not currently receiving, about to start, or have received in the past 6 months CBT for
pain or similar pain-related psychoeducation or behavioral skills training
e Not currently receiving or about to start substance abuse treatment services
(inpatient or intensive outpatient)
e Not planning/scheduled for surgery related to pain condition in next 12 months

Screening by web. Patients who choose to complete the eligibility screening by web will
either go to the study website and access the screening survey by entering the unique
survey code from their recruitment letter or click on the unique survey link provided in the
recruitment email (if applicable for their site). As described above, the web-based
screening survey should take approx. 10-15 minutes to complete. Upon completion of
the screening survey, patients will be informed whether they are eligible to participate in
the study or not.

If ineligible, they will be presented with a closing webpage thanking them for their

time and interest, briefly explaining the reasons for ineligibility, and giving them

the site study contact phone number if they have further questions.

If eligible, they will be able to complete the informed consent and baseline survey

via web, as described in section 8.

Screening by phone. Patients who opt for phone screening will complete the 10-15
minute screening survey with the health care system research staff supporting telephone
screening. If ineligible, they will be informed during the call and able to ask questions. If
eligible, they will be given the options of 1) completing the informed consent immediately
by phone as well as the baseline survey, or 2) being contacted at a later time to
complete the informed consent and baseline survey by phone.

25

```

### DOC-002 physical page 38

[Direct source page 38](../../../joi250046supp1_prod_1755300121.14087.pdf#page=38)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

8 INFORMED CONSENT PROCESSES

8.1 Informed Consent of Patients

Electronic Health Records (EHR)-Based Population Screening and Recruitment

e« Noconsent is required to conduct the population-based screening and recruitment
process described in section 6.1, which involves each site querying existing
administrative EHR records to extract PHI limited to the information necessary for
determining potential eligibility and conducting further screening.

* This also applies (no consent required) to the patients who are referred by their health
care provider to be screened for study eligibility. The provider will discuss the study
directly with the patient; if s/he agrees, a referral will be electronically routed to a study
staff member who will assess whether the patient meets the EHR-based inclusion
criteria, as also described in section 6.1.

* Avwaiver of the documentation of informed consent will be obtained for patients who self-
refer to the study after receiving the brochure from their provider or obtaining the
information on their own. Because these individuals will contact study staff directly, it is
feasible to obtain verbal consent to verify their potential eligibility based on the EHR-
based inclusion criteria. The provider recruitment brochure and EHR eligibility consent
phone script address the elements of consent that are applicable to this screening
process. In addition, patients will agree to the use of their PHI to assess their eligibility.

Eligibility Screening Survey

A waiver of the documentation of informed consent will be obtained in order to conduct the
eligibility screening survey. All potentially eligible patients (based on the EHR data) will have
been mailed a recruitment letter and brochure, as described in section 6. Upon receiving the
recruitment letter and brochure, patients can choose to go to the website to complete the
eligibility screening survey or call their clinical site to complete the eligibility screening survey by
phone. If a potentially eligible patient does not complete the screening survey by web or
proactively call the study on their own, study staff will attempt to reach them by phone, as
described in section 6.1 on recruitment.

Screening Survey by Web: If a patient goes to the website to complete the screening,
before they are presented with the opportunity to answer the eligibility questions, they will
be presented with a written statement that contains the elements of informed consent that
are applicable to the screening process. In addition, the statement will provide a phone
number to call research staff if they have questions. After being presented with this
statement to read, patients will be asked to electronically endorse their consent to complete
the eligibility screening before they can answer the eligibility questions.

Screening Survey by Phone: If a patient calls into the study phone line or is called by study
staff after receiving the recruitment letter and brochure, a staff member will review the same
information that is presented to patients who go to the website using a script that contains
the elements of informed consent that are applicable to the screening process. In addition,
the research staff will ask patients if they have any questions. After reviewing this
information, patients will be asked to verbally confirm their consent to proceed with the

26

```

### DOC-002 physical page 39

[Direct source page 39](../../../joi250046supp1_prod_1755300121.14087.pdf#page=39)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

eligibility screening and their response will be documented by study staff in the electronic
data capture system. Only after providing verbal consent will, they be asked the eligibility
screening questions by the research staff.

Study Enrollment
A waiver of the documentation of informed consent will be obtained in order to conduct the

informed consent process for the study by phone (consent obtained verbally) or by web
(electronic endorsement of consent). All participants are provided with information
containing all elements of informed consent, as they apply to all parts of the study, however
participants will not document consent with a signature.

If a patient is determined to be eligible based on the screening survey, s/he can proceed
with the informed consent process by web or phone during the same encounter as the
screening survey. Or, if a patient would prefer to conduct the informed consent process at a
later time s/he can return to the website later to complete it electronically or schedule a time
to complete it by phone with a study staff member.

Website: If a patient is determined to be eligible based on the screening survey
completed by web, s/he will be able to continue with the informed consent process.
Patients will be directed to download and read (via PDF link) the combined master
information sheet and site-specific information sheet, which includes all elements of
consent and HIPAA authorization information and encouraged to keep it for their
records. They will also be directed to call their site’s study-specific phone line if they
have any questions before they decide to participate. Patients will be asked to
electronically endorse their consent and HIPAA authorization. After completion of the
consent process by web, participants will be mailed a copy of the information sheet for
their records. In addition, sites may follow-up by phone with individuals who enrolled by
web in order to briefly welcome them to the study and clarify next steps.

Phone: If a patient is determined to be eligible based on the screening survey completed
by phone, s/he will be able to continue with the informed consent process. The study
staff person will review the elements of consent and HIPAA authorization information
which are contained in the study information sheet, using the consent phone script.
While on the phone, the staff person will direct the patient to the study website where the
combined master information sheet and site-specific information sheet can be
downloaded and reviewed by the patient as the staff person explains/reviews its content.
Verbal consent will be obtained as well as verbal HIPAA authorization. After completion
of the verbal consent process, participants will be mailed a copy of the information sheet
for their records.

For the subset of individuals who are recruited to complete interviews, they will have consented
to the interview as part of the study’s informed consent process. When the KP CHR study team
member calls these individuals at the pre-scheduled time, s/he will confirm that the individual

27

```

### DOC-002 physical page 40

[Direct source page 40](../../../joi250046supp1_prod_1755300121.14087.pdf#page=40)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

received the information sheet and confirm that the interviewee agrees to have the interview
recorded before any recording begins.

8.2 Informed Consent of Stakeholders and Staff

As noted in section 6.2, which describes recruitment strategies, stakeholders will have received
an email invitation with a one-page fact sheet attached, which includes the consent elements
that are pertinent to the interview process prior to agreeing to schedule an interview. When the
KP CHR study team member calls these individuals at the pre-scheduled time, s/he will ask if
the stakeholder interviewee has received the fact sheet and if s/he has any questions before the
interview commences. In addition, the KP CHR study team member will confirm that the
stakeholder interviewee agrees to have the interview recorded before any recording begins.
Consent will not be obtained from the individuals who choose to complete a stakeholder
interview. They are given a fact sheet, containing elements of consent, as described above. The
interview itself focuses on organizational processes, and although the stakeholder does share
opinions and perspectives on organizational topics, they do not share personal or protected
health information. This is an appropriate consent procedure given the minimal risk to the
stakeholder posed by the interview and the fact that the interview involves discussing
organizational topics commonly discussed in work-related meetings. In addition, due to the
professional focus of the interviews (and often the organizational prohibitions restricting such
individuals from accepting an incentive), stakeholders will not be paid an incentive for their
participation.

Informed consent process for intervention / health coaching staff. The intervention / health
coaching staff will be given a one-page fact sheet, which includes the consent elements that are
pertinent to the interview process prior to agreeing to schedule an interview. They will be
informed that they can refuse participation with no impact on their work. When the KP CHR
study team member calls these individuals at the pre-scheduled time, s/he will ask if the
interviewee has received the fact sheet and if s/he has any questions before the interview
commences. In addition, the KP CHR study team member will confirm that the interviewee
agrees to have the interview recorded before any recording begins. Consent will not be obtained
from the staff who choose to complete an interview based on the rationale outlined above for
the stakeholders.

28

```

### DOC-002 physical page 41

[Direct source page 41](../../../joi250046supp1_prod_1755300121.14087.pdf#page=41)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

9 STUDY INTERVENTION DISCONTINUATION AND PARTICIPANT
DISCONTINUATION/WITHDRAWAL

9.1 Discontinuation of Study Intervention

There are no criteria for the PI to discontinue the administration of the study intervention that are
related to specific adverse events or serious adverse events.

There may be rare instances in which an individual decompensated (or was threatening to study
staff) and was consequentially unable to continue to actively participate in a behavioral
intervention of the type administered in this trial. In this event, the reason for discontinuation will
be documented and an attempt to connect the participant to relevant behavioral health
resources/support in their region will be made.

If a participant informs the study staff that they will discontinue participation in the intervention,
staff will assess their reasons for discontinuation and determine whether the participant wants to
continue with the other study activities or withdraw from the study entirely.

9.2 Participant Discontinuation/Withdrawal from Study

There are only rare circumstances under which the PI would discontinue/withdraw a participant
from the study. As noted above, in the rare instance in which an individual decompensated (or
was threatening to study staff) and was consequentially unable to continue to complete study
assessments, the reason for discontinuation would be documented and an attempt to connect
the participant to relevant behavioral health resources/support in their region. If a participant
informs the study staff that they will discontinue participation in the study, staff will assess and
document their reasons for discontinuation. As specified in the consent, any data collected up to
the point of withdrawal will be retained.

9.3 Loss to Follow-Up

Participants randomized to the online program or virtual CBT-CP will be considered lost to
follow-up after 1) they have missed 2 or more of the weekly sessions or 2) a study staff member
has been unable to reach them after making multiple contact attempts (up to 7 calls or emails
and 2 mailed letters) over a 4 to 6-week period.

If a participant is considered lost to follow-up for the active intervention, the individual will still be
contacted per the follow-up assessment outreach process for each time point unless there is no
active/working phone, email, or mailing address available for them.

29

```

### DOC-002 physical page 42

[Direct source page 42](../../../joi250046supp1_prod_1755300121.14087.pdf#page=42)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

10 STUDY INTERVENTIONS

10.1. Description of Interventions

Both active intervention arms are based on the same core CBT-CP program (pain-coping skills
training) developed and refined by Dr. Keefe and colleagues at Duke University over the past
three decades. In addition, the virtual coach-led CBT-CP coach manual and participant workbook
are based on the PPACT intervention, which was tested in a large pragmatic trial led by Dr.
DeBar.”

CBT is the most widely accepted, evidence-based, nonpharmacologic treatment for chronic pain
and has been shown to benefit low-literacy adults in rural areas."'*'” CBT-CP is based on the
theory that patients' beliefs, attitudes, behavior, and coping styles play central roles in
determining (mediating) the impact of persistent pain.®

CBT-CP effects can be maintained long after treatment ends, without the negative side effects of
opioids and other pain medications and is an attractive adjunct or alternative to pharmacological
treatments. CBT-CP It focuses on helps patients develop and master skills to manage pain and
the disability and emotional distress associated with pain in order to improve their functioning
and quality of life. CBT-CP enhances the use and perceived self-efficacy of pain coping skills
that address cognitive processes (e.g., reducing catastrophizing) and behaviors (e.g., engaging
in meaningful activities and goals).

The table below provides an overview of the core content for both of the RESOLVE study
interventions. Both interventions include elements to enhance learning and mastery of skills that
are guided by social cognitive theory (e.g., social modeling, vicarious learning),’*”* adult
learning theory (e.g., tying skills to personal goals and experiences),’*> principles of multimedia
instruction (interactive exercises, graphics to reinforce explanations),’° and behavior change
theory” (e.g., behavior tracking).

Description of RESOLVE Intervention Session Content

Session Unique Topics/Skills* painTRAINER Virtual Coach-Led
CBT-CP

+ <

Rationale & Foundation of Self-Care/Relaxation Skills

Review relaxation skills (Progressive Muscle Relaxation and Mini-practice) Vv

Activity / rest cycling Vv

Pleasant activity scheduling / Negative automatic thoughts Vv

Negative automatic thoughts / Coping thoughts v
v
v
v

Pleasant imagery / distraction
Problem-solving
Monitoring for maintenance

“Each session includes goal setting (Session 1); goal review and refinement (sessions 2-8)

eo Noaaalwr a
0000006

30

```

### DOC-002 physical page 43

[Direct source page 43](../../../joi250046supp1_prod_1755300121.14087.pdf#page=43)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

10.1.1 painTRAINER

Overview. painTRAINER is an online, 8-session, pain coping skills training program (PCST)
based on cognitive behavioral therapy (CBT). Each session takes 45-60 minutes to complete
and provides interactive training in one or more evidence-based pain-coping skills.5°
Participants complete sessions on their own, in a set order, and are encouraged to complete
one session per week. Session completion is flexible — participants can close a session before
completing it and later resume where they left off. They can also go back to review completed
sessions or sections of completed sessions (e.g., an audio recording of a skill practice, or
instructions on how to use a skill). The sessions are led by a recorded “virtual coach” who
speaks directly to users. Thus, content is provided in audio to minimize reading and facilitate
program completion for low-literacy patients. painTRAINER was designed to include features of
therapist delivered PCST, while providing training in an easy-to-use format that includes
animated demonstrations, interactive exercises, working through common barriers to behavior
change/skills practice, and tailored feedback to reinforce learning.

Onboarding and Registration. Following randomization, participants who are assigned to
painTRAINER are mailed materials that include instructions for registering for the program,
unique login information, a participant workbook, and study team contact information (in case of
questions or technical difficulties). Approximately a week after the materials are mailed, study
staff call participants to “onboard” them to the program. This entails providing a verbal overview
of the program and making sure participants register and are able to access/log into
painTRAINER. Study staff follow specified guidelines to complete the onboarding call which
include suggested language/scripting. [Note: On 08/09/21 VUMC IRB approved revised
onboarding guidelines which added motivational interviewing-based language. This language
was to be used, as feasible.] The primary goal of the onboarding call is to ensure that
participants register and have no technical difficulties. The inclusion of Ml-based language
allows the staff person doing the onboarding to ask participants to consider potential barriers to
participation and how they might plan in advance to overcome such challenges as well as to
reaffirm their rationale and commitment to utilize painTRAINER to learn skills to manage their
pain.

Ongoing Support and Engagement. After participants begin the painTRAINER program,
automated email reminders are sent to practice skills and complete modules. Support is also
provided by study staff if a participant is not adhering to the recommended completion schedule.
Specifically, a study staff person will follow-up with a participant by phone in the following
circumstances:

e It has been more than 7 days since the participant registered and session 1 has not
been initiated.

« Asession has been initiated but is still incomplete after more than 7 days.

« thas been more than 10 days since the most recent session completion date and
another session has not been initiated.

e Sessions are being completed too quickly (3 or more sessions completed in 9 days).

Study staff utilize specified guidelines to complete follow-up calls which include suggested
language/scripting. The goal of the follow-up call is to identify and resolve the reason for non-
adherence.

31

```

### DOC-002 physical page 44

[Direct source page 44](../../../joi250046supp1_prod_1755300121.14087.pdf#page=44)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

10.1.2 Virtual Coach-led CBT-CP

Overview. The coach-led program includes 8 sessions of CBT-CP provided one-on-one via
telephone or video encounters. Each session takes 60 minutes and provides interactive training
in one or more evidence-based pain-coping skills. Sessions are scheduled at the participant's
convenience with approximately one session per week and participants have the option of
meeting with the coach by telephone only, using video conferencing or a combination of the two.
The live virtual-enabled coaching provided can enhance patient motivation and engagement.
This approach is likely to be especially useful for depressed or anxious patients (common
chronic pain comorbidities) for whom de-activation and/or avoidance may create barriers to
implementing effective pain-coping skills. Coaches providing these virtual visits are required to
have at least master's-level behavioral health training and conduct coaching sessions from the
study sites at KPWHRI in Seattle and KP CHR in Portland. This telehealth model of centralized
behavioral health services is being widely adopted across health care systems nationally, and
thus represents a critically important approach for this active arm of the study.

Onboarding. Following randomization, participants assigned to Virtual Coach-led CBT-CP are
mailed materials that include a brief biographical description of their health coach and a
participant workbook with handouts for the 8 sessions and materials for logging skills practice.
The assigned coach calls the participant approximately one week after the materials are mailed.
The primary goal of this outreach by the coach is to introduce themselves and to “onboard” the
participant to the program. The onboarding call includes verifying receipt of the packet of
materials and orienting the participant to the Virtual Coach-led program structure and format.
Participants are informed that coaching calls are confidential, asked their preference for
telephone or video coaching calls and for permission to record all coaching calls. The coach will
use the onboarding call as an opportunity to respond to questions from the participant and to
schedule the first coaching call. Coaches follow specified guidelines to complete the onboarding
call which include suggested language/scripting.

Ongoing Support and Engagement. Coaches work with participants to schedule sessions at the
most convenient time for them, with an emphasis on completing one coaching call per week for
8 weeks. Frequently, a standing weekly meeting time is identified for the 8 weeks, however
there is flexibility in this schedule and coaches can accommodate scheduling challenges, as
necessary. Coaches remind participants 1-2 days before a scheduled session via phone or
email (based on participant preference). If a participant does not attend a scheduled call, the
coach will first reach out by telephone to reconnect and reschedule the missed appointment.
When reached, the coach may explore possible barriers to completing the program and work
with the participant to problem-solve for any challenges, as appropriate. If the participant is not
reached right away, as described in Section 9.3. multiple outreach attempts will be made over
the course of several weeks, using different contact modes, including phone, email and mailed
letters. (Note: In the rare circumstance that a participant cannot be reached by phone, email or
letter, the coach will send a text as a last resort for outreach.)

32

```

### DOC-002 physical page 45

[Direct source page 45](../../../joi250046supp1_prod_1755300121.14087.pdf#page=45)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

10.2 ‘Intervention Administration and Dosing

Both the painTRAINER program and the virtual coach-led CBT-CP sessions are intended to
follow a weekly administration schedule (1 session per week over the course of 8 weeks).
However, completion may vary due to the personal circumstances of the participants. The
maximum intended duration for the active intervention period is 12 weeks, meaning study staff
will proactively follow-up to ensure session completion during that time period. If someone has
not completed all 8 sessions within 12 weeks, study staff will not do any further follow-up to
encourage completion of online sessions or schedule telephonic/video sessions.

« The exception to this is when a participant is actively engaged with coaching staff and
requests and is able to complete any remaining intervention sessions beyond yet close
to the 12-week target. These instances will be reviewed by clinical supervisors and
decisions will be made on a case-by-case basis before virtual intervention activities
continue. All intervention-related contacts are documented and any that occur after the
active intervention period can be identified/flagged for analytic purposes.

e Note: painTRAINER remains open to participants and access cannot be restricted after
12 weeks. However, the program automatically collects data on any logins that occur
after the 12-week period and information related to completion of sessions after the
intervention period may be used analytically.

Participants are considered to have received a full dose of the interventions if at least 75%, or 6
of the 8, sessions have been completed.

10.3. Masking and Measures to Minimize Bias

It is not feasible for participants to be masked to treatment arm assignment due to the
behavioral nature of the intervention. The PI and select Co-Investigators and study staff who are
involved in the oversight and delivery of the interventions will also be aware of treatment
assignment. Outcome assessors will be masked to treatment assignment. Assessments
completed on paper will be entered by research staff who are blinded to the randomization
status of the study participants.

10.4 Study Intervention Fidelity Monitoring Procedures

Training and monitoring intervention fidelity for virtual coach-led CBT-CP. Maximum
generalizability and relevance to community providers will be addressed by applying the
Treatment Fidelity Workgroup of the NIH Behavioral Change Consortium® framework to ensure
interventions are delivered as intended. Treatment fidelity is maximized by use of fidelity
induction and monitored by fidelity assessment. In this study, fidelity induction will be achieved
by the use of proactive strategies including: a formal structured orientation and training
process for health coaches, use of standardized treatment manuals and training materials,
repetition and practice of training skills, and adequate achievement of proficiency in core skills
before health coaches start to work with study participants.

All coaches will receive training prior to conducting treatment sessions with study participants.
The initial training will consist of approximately 16 hours of didactic and experiential coursework
conducted by Drs. Balderson, DeBar, Murphy and/or Keefe. Interventionists will be provided
with the treatment manual and the treatment strategies will be taught through didactic
instruction, recorded illustrations of techniques from model cases, and role-play of common

33

```

### DOC-002 physical page 46

[Direct source page 46](../../../joi250046supp1_prod_1755300121.14087.pdf#page=46)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

scenarios. Health coaches will complete two role plays of the eight intervention sessions, one as
a coach and one as a participant (i.e., 16 mock sessions total). Upon completion these initial
training activities, a health coach will be assigned active study patients.

During the first 4 months post-completion of training, recordings from at least two completed
encounters for each session number from the coaches’ first 5 patients will be reviewed and
scored for proficiency by at least one of the following individuals: Drs. Balderson, DeBar, Keefe,
Murphy and/or Ms. Firemark. For each encounter that is reviewed, two assessments will be
completed: 1) Fidelity to Session Content 2) Fidelity to Cognitive-Behavioral Therapy Treatment
(using a modified version of the VA Cognitive Behavioral Therapy for Chronic Pain Therapist
Rating Scale).2° During this acute phase of session review, written and/or verbal feedback is
provided to coaches on a weekly basis.

After health coaches reach proficiency in the delivery of each session (based on scored
recordings), ongoing ratings of recorded sessions will be conducted by one or more of the
following individuals: Drs. Keefe, Balderson, DeBar, Murphy and /or Ms. Firemark monthly as
coaches gain experience with the intervention. Ongoing telephonic treatment protocol
adherence will be monitored via multiple methods that include: 1) therapists’ completion of a
self-assessment of protocol fidelity adherence after every session using the session-specific
Fidelity to Session Content checklists, 2) review and scoring of recorded sessions with patients
using the Content checklists and the Cognitive Therapist Rating Scale, and 3) coach request for
recording review for any challenging session or sessions viewed as potentially problematic in
treatment fidelity. Identified deviations from the treatment protocol will be addressed
immediately by providing any coach identified as having poor adherence to the intervention
manual with more intensive supervision and monitoring until adherence criteria is re-
established. This is consistent with how this would occur in everyday clinical care. This
approach was used successfully in previous CBT-CP studies.2°.718183

10.5 Concomitant Therapy

As noted in the exclusion criteria, study participants cannot at the time of study enrollment or in
the 6 months prior receive Cognitive Behavioral Therapy (CBT) for pain or a similar
psychoeducational skill-based training for pain (nor indicate that they have scheduled to begin
such treatment). However once enrolled, participants can receive any pharmacologic or
nonpharmacologic treatments available to them without restriction. At each study assessment
(3-, 6- and 12-month follow-ups), participants’ use of CBT for pain or a similar
psychoeducational skill-based training for pain (in-person, by phone or via online or App-based
programs) will be assessed.

34

```

### DOC-002 physical page 47

[Direct source page 47](../../../joi250046supp1_prod_1755300121.14087.pdf#page=47)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

11 STUDY ASSESSMENTS AND PROCEDURES

Section 8 describes the informed consent process in detail. The consent process will occur prior
to initiation of the baseline survey but ideally during the same phone encounter or web survey
session as the screening.

11.1 Baseline Assessment

Patient baseline assessment. Patients who consent to participate in the study will be asked to
complete the baseline assessment either by phone or online immediately following the informed
consent process. The baseline assessment will include the measures described in section 3.1.
In addition, the baseline assessment will confirm contact information, collect preferences for the
administration mode of follow-up assessments, and assess subjects’ willingness to potentially
participate in the interviews as part of the qualitative evaluation. It is expected that the informed
consent and baseline assessment will take approximately 45-60 minutes.

11.2 Follow-Up Assessments

Patient assessment at the time of notification of randomization. At the time that participants are
mailed the materials notifying them of their study arm assignment, they will also be mailed a
brief paper survey and a pre-posted return envelope. The paper survey will assess the
participants’ perceived support of the intervention to which they have been assigned and will
serve as the baseline assessment of this potential mediator variable. The paper survey will take
no more than 5 minutes to complete. (Note: This assessment is offered only by paper due to the
fact that it is mailed with the other materials related to randomization notification and logistically
it is most feasible to administer this way at this particular time point.)

Patient follow-up assessments at 3-, 6- and 12-months. Based on the preference for survey
administration mode (online, phone or paper) indicated at the time of the baseline assessment,
participants will initially be sent the follow-up survey via their preferred mode. (Note: At any point
during the study, a participant can change their preferred survey mode.) The protocol for follow-
up with non-responders within the assessment window will employ the other modes of contact in
order to maximize the opportunity to reach participants. For example, subjects who prefer email
contact for the assessments will also be contacted by phone if they do not complete the
assessment using the web link in the emails within a set period of time. Each follow-up
assessment will take approximately 30 minutes to complete. The specific protocol for contacts
related to follow-up assessments is described in the study’s operating procedures.

11.3 Qualitative Interviews

Patient interviews. A subset of approximately 100 patients will be invited to complete two
approximately one-hour long interviews by phone at approximately 3-5 months and 12-14
months post-randomization. A different subset of 20 individuals who do not complete the
interventions but are still enrolled in the study (see details related to selection criteria for these
interviews in section 6.1) will complete one interview approximately one-hour in length by
phone. Interviewers will use semi-structured interview guides for all patient interviews. These
interviews will be audio-recorded.

35

```

### DOC-002 physical page 48

[Direct source page 48](../../../joi250046supp1_prod_1755300121.14087.pdf#page=48)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

Stakeholder and referring clinician interviews. The stakeholder interviews will be approximately
an hour in length and conducted primarily by phone using a semi-structured interview guide; in
the instance that a stakeholder is unable to complete the interview in one encounter due to
scheduling issues that may arise which allow less an hour for the phone call, follow-up to
complete questions may be conducted by phone or email. These interviews will be audio-
recorded.

Intervention staff / health coach interviews: Qualitative research team members will attempt to
conduct interviews with all (approximately 12) of the intervention/health coaching staff. These
interviews will be approximately one-hour in length and conducted twice (early in study
implementation and later); they will be audio-recorded.

36

```

### DOC-002 physical page 49

[Direct source page 49](../../../joi250046supp1_prod_1755300121.14087.pdf#page=49)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

12 ADVERSE EVENTS AND UNANTICIPATED PROBLEMS INVOLVING RISKS TO
SUBJECTS OR OTHERS

12.1 Definition, Classification and Reporting of Adverse Events

12.1.1 Definition of Adverse Events (AEs)

An adverse event (AE) is any untoward or unfavorable medical occurrence in a human subject,
including abnormal signs, symptoms, or diseases, temporally associated with the subject's
participation in the research, whether or not considered related to the subject’s participation in
the research.

Because the RESOLVE study involves minimal risk and the study population includes patients
with high impact chronic pain, who have fluctuating physical and emotional symptoms as part of
the natural course of their condition, such symptoms will not be systematically solicited as part
of the trial.

AEs will be identified if:
e Participants proactively contacts study staff at any time to self-report an AE;
« Participants happen to self-report an AE during a regular study contact with intervention
or study staff; or
. Participants attribute study withdrawal or dropout to unfavorable medical / health-related
issues.

AEs will not be solicited uniformly from all study participants, as capture of these events will be
biased by study arm (i.e., telephone CBT-CP participants will have greater interaction with study
staff by phone and more opportunity to self-report these symptoms and events).

AEs will be entered by study staff into the Utah/DCC REDCap AE database at the time of
reporting by the participant.

12.1.2 Definition of Serious Adverse Events (SAEs)

For this comparative effectiveness trial, a serious adverse event (SAE) is defined as an event
that:
e Results in death during a patient's active participation in the trial.
« Results in inpatient hospitalization during a patient’s active participation in the trial.
(Planned hospitalization scheduled before the enrollment of a study participant is not an
SAE.)

Because the patients who participate in the RESOLVE study will be older and have co-morbid
health conditions, it is expected that subjects will experience inpatient hospitalizations, which
are unrelated to study participation, during the course of the study. In addition, it is expected
that deaths, which are also unrelated to study participation, might occur among study enrollees
based on prior studies. Specifically, in the study Pl’s recently completed pragmatic trial, PPACT,
which provided an intensive in-person behavioral intervention and enrolled 850 patients with
chronic pain, there were 12 deaths during the study, all unrelated to study participation, and 287
hospitalizations (116 for intervention participants and 171 for usual care).

37

```

### DOC-002 physical page 50

[Direct source page 50](../../../joi250046supp1_prod_1755300121.14087.pdf#page=50)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

SAEs will be systematically assessed every 6 months for active study participants based on
electronic health records (EHR) data.

e Each clinical site will query active participants’ electronic health records data every 6
months (in alignment with the DSMB meeting schedule) to identify any deaths or
hospitalizations throughout the interval of active participant enrollment in the trial.

e An independent physician within each health care system/clinical site will conduct a
chart review for each death and hospitalization to assess its potential relatedness to
study procedures and interventions.

e The summary of SAEs and findings of these reviews will be submitted to the DCC.

In addition to the semi-annual EHR queries, SAEs may be identified by participant self-report. If
this occurs, the event will be documented and reviewed by the independent physician as part of
the semi-annual review described above.

12.1.3 Definition of Adverse Events of Special Interest (AES!)

This protocol will not collect solicited adverse events of special interest (AESI). There is no
clinical or empirical basis for hypothesizing that either of the active interventions would increase
risk of AESIls. In addition, the unequal contact with study staff among participants in the three
study arms inherently results in differential opportunities for ascertainment of “events.”
Therefore, between-group comparison of adverse events reported to or discovered by study
staff would be biased and hence not meaningfully interpretable or actionable.

12.1.4 Severity of Adverse Events

For an AE, the following guidelines will be used to describe severity:

* Mild — event does not generally interfere with usual daily activities and/or does not require
medical care.

* Moderate — event interferes with usual daily activities and/or requires self-medical care or
outpatient medical care.

* Severe — event interrupts usual daily activities and/or requires inpatient medical care or
medical care with overnight stay in hospital observation services.

12.1.5 Relationship to Research Participation

For an SAE, the following guidelines will be used to describe relatedness to study procedures and

study interventions:

« Related — There is clear evidence to suggest a causal relationship between the study
procedures or study interventions and the SAE, and other possible contributing factors can
be ruled out.

¢ Possibly Related -There is a reasonable possibility that the study procedures or study
interventions caused the SAE. Reasonable possibility means that there is evidence to suggest
a causal relationship between the study procedures or study interventions and the SAE.

« Not Related — There is not a reasonable possibility that the study procedures or study
interventions caused the SAE, there is no temporal relationship between the study procedures
or study interventions and event onset, or an alternate etiology has been established.

38

```

### DOC-002 physical page 51

[Direct source page 51](../../../joi250046supp1_prod_1755300121.14087.pdf#page=51)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

12.1.6 Expectedness of Adverse Events/Serious Adverse Events

An AE/SAE will be considered unexpected if it occurs in one or more subjects, the nature,

severity, or frequency of which is not consistent with either:

« The known or foreseeable risk of adverse events associated with the procedures involved in
the research that are described in Section 2; or

« The expected natural progression of any underlying disease, disorder, or condition of the
subject(s) experiencing the adverse event and the subject’s predisposing risk factor profile
for the adverse event.

12.1.7 Reporting Procedures for Adverse Events/Serious Adverse Events

Any AEs self-reported by participants to study staff will be entered into the Utah/DCC REDCap
AE database.

As described above, every 6 months in alignment with the DSMB meeting schedule, the study
sites will provide a summary of SAEs to the DCC.

12.2 Definition and Reporting of Unanticipated Problems

12.2.1 Definition of Unanticipated Problems

This study protocol uses the following definition of Unanticipated Problems (UPs) to include, in
general, any incident, experience, or outcome that meets all of the following criteria:

« Unexpected;

e Related or possibly related to participation in the research; and

« Suggests that the research places participants or others at a greater risk of harm
(including physical, psychological, economic, or social harm) than was previously known
or recognized.

“Unexpected” means the nature, severity, or frequency is not consistent with either (a) the study
procedures or study interventions that are described in section 2; and (b) the characteristics of
the participant population being studied.

“Related” means there is clear evidence that the unanticipated problems were caused by the
study procedures or study interventions involved in the research and “possibly related” means a
reasonable possibility that the unanticipated problem(s) may have been caused by the study
procedures or study interventions involved in the research.

12.2.2 Reporting of Unanticipated Problems

The study site investigator will report UPs to the lead principal investigator (PI). The lead PI will
report UPs to the IRB of record. The UP report will include the following information:

¢ Protocol identifying information: protocol title and number, Pl’s name, and the IRB project
number
¢ Adetailed description of the event, incident, experience, and/or outcome

39

```

### DOC-002 physical page 52

[Direct source page 52](../../../joi250046supp1_prod_1755300121.14087.pdf#page=52)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

« An explanation of the basis for determining that the event, incident, experience, or outcome
represents an UP

¢ Adescription of any changes to the protocol or other corrective actions that have been taken
or are proposed in response to the UP

To satisfy the requirement for prompt reporting, UPs will be reported using the timeline specified
in the written reliance agreement between the IRB of record and the relying IRB at each study
site.

40

```

### DOC-002 physical page 53

[Direct source page 53](../../../joi250046supp1_prod_1755300121.14087.pdf#page=53)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

13 STUDY OVERSIGHT

Study oversight will be under the direction of a Data and Safety Monitoring Board (DSMB)
comprised of members with expertise in appropriate clinical, statistical, scientific, ethical
disciplines.

The DSMB will meet before study enrollment begins and every six months thereafter, until the
end of the study; to approve the study protocol prior to implementation; assess safety and
effectiveness data; to monitor accrual of study participants; to study progress, and data integrity
for the study. If safety concerns arise, ad-hoc meetings and more frequent standing meetings
may be held.

The DSMB will operate under the rules of a charter that will be approved at the initial DSMB
organizational meeting. At that time, data elements that the DSMB needs to assess will be
clearly defined. The DSMB will provide recommendations to the funding agency, the National
Institute on Aging, regarding proceeding with the study as planned, proceeding with
modifications, or terminating the study, as noted in the DSMB Charter.

This study may be suspended or prematurely terminated if, in the opinion of the investigators or
the NIA, there is reasonable cause. Written notification, documenting the reason for study
suspension or termination, will be provided by the suspending, or terminating party. The
investigators will promptly inform the IRB, providing the reason(s) for suspension or termination.

Circumstances that may warrant termination include, but are not limited to:
« Determination of unexpected, significant, or unacceptable risk to participants.
e Insufficient adherence to protocol requirements.
« Data that are not sufficiently complete and/or evaluable.

13.1 Halting Rules

The DCC will monitor the safety data submitted by the study site investigator. The DCC will
notify the DSMB chair when any SAEs deemed to be unexpected and related to study
procedures or study interventions occur during the study.

In such an instance, the DSMB chair will provide recommendations regarding the temporary
suspension of enrollment and/or administration of study procedures or study interventions. If
warranted, an ad-hoc DSMB meeting will be convened.

41

```

### DOC-002 physical page 54

[Direct source page 54](../../../joi250046supp1_prod_1755300121.14087.pdf#page=54)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

14 STUDY MONITORING

Clinical site monitoring is conducted to ensure that the rights of human subjects are protected,
that the study is implemented in accordance with the protocol and/or other operating
procedures, and that the quality and integrity of study data and data collection methods are
maintained. Clinical site monitoring and remote monitoring for this study will be performed by
the Duke/Vanderbilt (Clinical Coordinating Center or CCC) and Utah (Data Coordinating Center
or DCC) Trial Innovation Centers, respectively.

14.1. Clinical Site Monitoring

The CCC utilizes risk-based methodology to identify and correct problems that may arise at
sites. Details of clinical site monitoring will be documented in a supplemental study-specific risk-
based Clinical Monitoring Plan (CMP), separate from this protocol. The CMP will specify the
frequency of monitoring, monitoring procedures, the level of clinical site monitoring activities
(e.g., the percentage of participant data to be reviewed), and the distribution of monitoring
reports.

Site monitoring will be performed by a trained site monitor during the study period to ensure
regulatory compliance, patient safety, and to monitor the quality of data collected. Essential
document binders, regulatory documents and data collection forms may be reviewed. Interim
monitoring will take place depending on grant budget, site enrollment, and compliance issues
identified. The site monitor will provide each site with a written report, and sites will be required
to follow up on any deficiencies. It is anticipated that the study monitoring for this protocol will
consist of site initiation (prior to patient enrollment), interim monitoring, and close out. The site
initiation may take place as group training made up of site investigators and research assistants.

Study monitors will evaluate study processes and documentation based on the International
Council for Harmonisation (ICH), E6: Good Clinical Practice guidelines (GCP). Documentation
of monitoring activities and findings will be provided to the site study team, the study Pls, NIH,
and NIH Program staff. The NIH reserves the right to conduct independent clinical site
monitoring as necessary.

The CCC may conduct clinical site monitoring remotely. Remote monitoring involves detailed
review of the data entered by the clinical sites (KPGA, KPNW, KPGA and Essentia) and
consultations with the clinical site investigators and/or research coordinator/manager to review
safety and data quality. This may require uploading patient study files, regulatory
documentation, or other source documents for the monitor to review. Alternatively, other
methods, such as remotely viewing source documentation, may be utilized. This helps assure
protocol compliance and accurate data collection. The CCC may conduct more remote
monitoring activities early in the trial to assure protocol compliance and identify any training
issues that may exist. Remote monitoring documents will be retained in accordance with federal
requirements. Safety of subjects will be monitored and ensured in accordance with the Data and
Safety Monitoring Plan (DSMP).

42

```

### DOC-002 physical page 55

[Direct source page 55](../../../joi250046supp1_prod_1755300121.14087.pdf#page=55)

```text
RESOLVE UH3 Protocol

Version 5.0
10 Nov 2022

15 STATISTICAL CONSIDERATIONS

This section provides an overview of the planned statistical analyses for the RESOLVE study.
See the RESOLVE Statistical Analysis Plan (SAP) for specific details related to the study

hypotheses and analytic approaches.

15.1

Sample Size Determination

For the primary study outcome, clinically meaningful improvement (MCID; 30% reduction in
overall BPI-SF score) in pain severity at 3 months, sample size requirements were calculated
for a two-sided comparison of independent proportions with 90% power using Fisher’s Least
Significant difference method to account for three-way comparisons (specifically conduct
Omnibus Wald Test for any difference between three groups and then conduct pairwise
comparisons given an overall difference is statistically significant at the 0.05 alpha level).
Sample size calculations assumed a usual care outcome rate of 15% who achieve the MCID of
30% reduction in pain severity from baseline to 3 months. The 15% usual care rate was chosen
because this rate was observed among participants in the usual care arm of the study Pl’s
recently completed PPACT trial’ and it is similar to rates observed by others in the usual care
arm of similar trials.°° The necessary sample size of 1,863 (621 per arm) was calculated to
detect a difference of 7.5% between a given intervention group relative to usual care in the
proportion of individuals who attain a clinically meaningful change (30% reduction from
baseline) in pain severity. A retention rate of 80% is estimated. Thus, to achieve this final
sample size, at least 2,331 individuals will be randomized, 777 per intervention arm. A 7.5%
detectable difference corresponds to 22.5% (relative change of 150%) of individuals in an
intervention arm attaining a clinically meaningful change in pain severity.

Power for secondary analyses related to aim 1b (subgroup analyses) was also estimated.
Sample size requirements for these secondary analyses were calculated using the same
assumptions described above (i.e., a two-sided comparison of independent proportions using
Fisher’s Least Significant difference approach to account for three-way comparisons, with
sample size calculations assuming an improvement rate of 15% in the usual care arm). The
subgroup sample size was projected to range between 20% and 40% of the original 1,863
sample size since this should cover the range of the subgroup sample sizes of interest.

Power for Subgroup Analyses Ranging the Size of the Subgroup

Assumptions

80% Power to Detect:

Subgroup Usual Care Intervention Detectable
Sample Size (UC) (Int) Difference Relative Change
N (% of 1,863) % UC % Int %lnt - Y%UC % Int | %UC
372 (20%) 15.0% 31.0% 16.0% 206.7%
558 (30%) 15.0% 27.7% 12.7% 184.7%
744 (40%) 15.0% 25.8% 10.8% 172.0%

There is 80% power to detect a 10.8% difference (relative change of 172%) between each
intervention group and UC if subgroup sample size is 40% of the overall study population and
16.0% difference (relative change of 206.7%) if the subgroup sample size is 20% of the overall

study population.

43


```

### DOC-002 physical page 56

[Direct source page 56](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

Note that in previous studies of this study team, sex, and comorbid mental health conditions
(depression, anxiety) were not less than 40% of the population suggesting there is high power
for the primary subgroups of interest. Further, the study is aiming to have at least 20% of
rural/medically underserved residency and therefore there is good power for this subgroup.
Individuals with negative social determinants of health comprise an exploratory subgroup since
it is not clear how many people in this population a priori will have this indication.

15.2 Populations for Analyses

All analyses will be conducted following an intent-to-treat approach, including all individuals
randomized regardless of their engagement with or exposure to the intervention.

15.3. General Approach to Statistical Analyses

All confidence intervals and p-values will be two-sided and statistical significance at the 0.05 level.

15.4 Baseline Descriptive Statistics

Descriptive statistics of the baseline study population by intervention arm will be provided,
presenting percentages for categorical variables and means and standard deviations for
continuous variables. The RESOLVE Statistical Analysis Plan (SAP) provides specifics on the
planned analyses related to demographics and baseline characteristics.

15.5 Primary Effectiveness Analyses

Primary Outcome (Aim 1) Statistical Hypothesis: Both active interventions are
expected to result in a higher proportion of patients achieving MCID (30% reduction in
overall BPI-SF score) in pain severity relative to those receiving usual care at 3-month
follow-up (primary time point).

Secondary Time Point Statistical Hypotheses: Both active interventions are expected
to result in a higher proportion of patients achieving MCID (30% reduction in overall BPI-
SF score) in pain severity relative to those receiving usual care at the 6 and 12-month
follow-ups (secondary time points).

Modified Poisson regression®®*’ fit using generalized estimating equations (GEE) will be used to
model the binary primary outcome, MCID in pain severity (30% reduction from baseline), 3
months (primary time point) and 6 and 12 months (secondary time points).

Interactions between each intervention and indicators of time (3, 6, 12 months) will be included
to estimate time-specific intervention effects; the primary comparisons will be between the
interventions and usual care at 3 months (i.e., primary effectiveness will test the size of the
intervention coefficient at the 3-months timepoint). Adjustment will be made for baseline levels
of pain severity, other stratification variables (sex, clinical site, and rural/medically underserved
residency), and a priori variables predictive of outcome (multisite pain and co-occurring mental
health condition).

44

```

### DOC-002 physical page 57

[Direct source page 57](../../../joi250046supp1_prod_1755300121.14087.pdf#page=57)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

The RESOLVE Statistical Analysis Plan (SAP) provides further information on the rationale for
this approach as well as the specific details on the planned analyses.

15.6 Secondary Effectiveness Analyses

Secondary Outcomes (Aim1a) Primary Statistical Hypotheses: Those in both
active intervention conditions will show greater improvements in overall pain severity,
pain intensity (MCID and overall), pain-related interference (MCID and overall) and
related quality of life outcomes (social role functioning, physical functioning, and patient
global impression of change) relative to those receiving usual care at the 3-month
follow-up.

Secondary Outcomes (Aim1a) Secondary Statistical Hypotheses: Those in both
active intervention conditions will show greater improvements in overall pain severity,
pain intensity (MCID and overall), pain-related interference (MCID and overall) and
related quality of life outcomes (social role functioning, physical functioning, and patient
global impression of change) relative to those receiving usual care at the 6- and 12-
months follow-ups (secondary time points).

Analyses of secondary outcomes (Aim 1a) will follow the same proposed approach as Aim 1.
Linear regression will be used to assess continuous outcomes and Poisson regression for
binary and count outcomes. An interaction between intervention arms and time indicators will be
included, and the primary time point for all secondary analyses will be 3 months following
randomization; baseline levels of pain severity and all stratification variables will be included as
covariates.

The RESOLVE Statistical Analysis Plan (SAP) provides details on these planned secondary
outcome analyses.

15.7 Additional Effectiveness Analyses for Primary Outcome (Moderators and
Mediators)

Moderator (Aim 1b) Statistical Hypotheses: For patients with more complex conditions
(concomitant mood or anxiety disorders; multisite pain) or challenging social / environmental
factors (rural/medically underserved or unmet social needs) the contact with a telephonic
coach will result in better pain-severity outcomes when compared to those receiving online
CBT-CP.

Moderator Analyses: Subgroup analyses will be conducted to determine the impact of the active
interventions on specific populations and explore for potential heterogeneity of treatment effects
by sex, age, race/ethnicity, rural/medically underserved residency, multiple pain conditions,
mental health mood disorders, and negative social determinants of health. Analyses for Aim 1b
will follow the same general approach as for Aim 1 but will be focused on assessing
heterogeneity of treatment effects (sub-groups). Heterogeneous treatment effects by each
potential moderator will be assessed separately. For each moderator, included in the regression
models described in the analytic plan for Aim 1 will be a main effect for the moderator and an
interaction between the moderator, intervention, and follow-up time, to estimate time-specific
intervention effects within each subgroup defined by the potential moderator. The primary

45

```

### DOC-002 physical page 58

[Direct source page 58](../../../joi250046supp1_prod_1755300121.14087.pdf#page=58)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

comparison for Aim 1b will be of the interaction terms associated with each intervention arm at
the 3-months follow-up time.

Mediator (Aim1c) Statistical Hypotheses: Changes in pain catastrophizing, pain-
related self-efficacy, and perceived support from baseline to 3 months will be mediators
of treatment outcomes at 6 months for those in both active interventions.

Mediator Analyses: Mediation analyses will be used to assess and quantify the effect of theory-
based mediators (pain-catastrophizing, pain self-efficacy, perceived support). Primary mediation
analyses will assess the effect of the potential mediators on the primary outcome at 6 months,
MCID in pain severity, while explanatory secondary analyses will investigate mediator impacts
on secondary outcomes at 6 months.

The RESOLVE SAP provides further detail on the planned moderator and mediator analyses.

15.8 Economic Evaluation Analyses

For aim #2, a full economic evaluation of the CBT-CP interventions, compared to usual care, will
be conducted, using the framework of cost-effectiveness, including the costs of implementation
and maintenance, following best practice in economic evaluation. This analysis will be
conducted for the Kaiser Permanente clinical sites where the capture of all health care utilization
is available through administrative data. Information on resources used to implement the
intervention will come from the trial data collection instruments and from medical office staff,
provider interviews, and study staff. All relevant resources used in the intervention delivery (e.g.,
training, counseling, fidelity assurance) will be included. EHR data will be used to identify and
classify health care encounters and prescription medications. Using the framework of cost-
effectiveness, the incremental cost per additional patient with a MCID in pain severity (30%
reduction from baseline) will be estimated at 12 months, and the Quality-Adjusted Life Year
(QALY) gained—utilities will be estimated using the EQ-5D-5L.”

Costs to be collected. Medical care utilization and intervention costs will be considered. Medical
care utilization includes pharmacy, outpatient visits (including specialty care), inpatient stays,
and referrals, and will be costed using standard costing algorithms***” and Medicare fee
schedules. In addition to total medical care costs, we will also undertake an analysis of pain-
related care focused on utilization linked to pain conditions, identified by diagnostic and
procedure codes, and pain-related medications. Intervention costs include program
implementation (e.g., training, meetings, and supervision; patient identification, invitation, and
screening) and delivery (e.g., online hosting, clinician calls). The analysis will take the
perspective of the health plan (a principal decision maker for future implementation), so it will
include all health system costs of intervention implementation and delivery in clinical settings.

Cost-effectiveness calculations. As done in prior economic evaluations of trials,°° the cost-
effectiveness of the intervention will be estimated using net benefit regression methods." This
technique uses a "net benefits" framework, comparing the incremental cost-effectiveness ratio
to a range of potential values for a decision maker’s willingness-to-pay (WTP) for a unit of
health gain. A cost-effectiveness acceptability curve (CEAC) is constructed that illustrates the
intervention’s probability of being cost-effective at various levels of WTP for a unit of outcome
(e.g., cost per QALY of $30,000 to $100,000). The regression framework allows ready
evaluation of cost-effectiveness in subgroups (following the intervention’s findings). Net benefit
regression uses as the dependent variable, net benefit: nb; =A-effect; - cost; (from person-level

46

```

### DOC-002 physical page 59

[Direct source page 59](../../../joi250046supp1_prod_1755300121.14087.pdf#page=59)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

effect and cost data; A = WTP level and is varied to construct the CEAC). Sensitivity analyses
will be performed to assess the applicability of costs to other settings, the estimation of
replication costs, and economies of scale.°°

Health care cost comparisons: A comparison of the health care costs between the randomized
groups will be conducted. These comparisons will include overall, and pain-specific costs. The
table below describes the proposed categories of health care costs. Health care costs will be
analyzed using generalized estimating equations with appropriate link functions.

Categories of Health Care Costs to be Assessed

Pain-related' Total

Prescription medications

Ambulatory encounters

Primary Care

Physical Therapy, Occupational
Therapy and / or Physiatry?

Pain Medicine/Pain Clinic

Mental/Behavioral Health or
Addiction Medicine

ER or Urgent Care

Other specialty medical care®

In-patient hospital*

1. Pain-related medications are identified by medication class (i.e., opioids, etc.). Pain-related
in-person health care encounters are identified based on ICD-10-CM diagnostic codes.

2. Physical Therapy includes Physical Therapy, Occupational Therapy and Physiatry visits.

3. Specialty medical care includes in-person encounters with any non-primary care department
that is not already included in the table.

4. Pain-related hospitalizations have a primary (or principal) pain-related ICD-10-CM
diagnostic code.

15.9 Exploratory Effectiveness Analyses

The impact of the active interventions on exploratory outcomes will be assessed. These
exploratory outcomes are described in detail in section 3.4 and include long-term opioid use,
depression symptomology, anxiety symptomology, sleep disturbance, high impact chronic pain,
and graded chronic pain. The same approach that is proposed for secondary outcomes and
outlined above will be used.

15.10 Safety Analyses

Safety monitoring analyses will be prepared for the external Data Safety and Monitoring Board
(DSMB) twice per year to align with the DSMB meeting schedule. See the Data and Safety
Monitoring Plan for specific details on the data and safety monitoring procedures and reporting
guidelines.

47

```

### DOC-002 physical page 60

[Direct source page 60](../../../joi250046supp1_prod_1755300121.14087.pdf#page=60)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

15.11. Planned Interim Analyses

There are no planned interim analyses of primary or secondary outcome data before the study
is completed. However, if in context of evaluating the safety outcomes the DSMB requests
interim effectiveness estimates they will be provided. No formal futility or effectiveness interim
analyses will be conducted.

48

```

### DOC-002 physical page 61

[Direct source page 61](../../../joi250046supp1_prod_1755300121.14087.pdf#page=61)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

16 QUALITATIVE EVALUATION ANALYSES

The qualitative evaluation (Aim #3) will be guided by three frameworks. First is the EPIS
implementation framework.°* The EPIS framework emphasizes both the inner (organizational)
and outer context (environmental context), which are both important to monitor. The outer
context may pose unique issues in each implementation site and impact the intervention even
when the inner context is stable and being implemented with a high level of fidelity and
consistency.

The RE-AIM model®®.% will be used to document and help triangulate and explain the research
outcomes. This model has four components: Reach, Effectiveness, Adoption, Implementation,
and Maintenance. Reach reflecting the percentage and characteristics of persons who receive
or are affected by a program. The project will use EHR data to examine: 1) the percentage of
patients excluded from the trial and the rationale for exclusion, and 2) the percentage of patients
who participate in the program based on the denominator of all patients who were approached
for participation in each health care system, as well as all potentially eligible patients in the
health plan regardless of whether or not they were approached for participation. Effectiveness
measures the impact of the intervention on primary and secondary outcomes. Further, the
qualitative evaluation is critical for understanding the reach, recruitment, and effectiveness
findings. Adoption is less relevant to the current study as the telehealth programs can and will
be made available to patients completely outside the ambulatory care setting, thereby reducing
or eliminating routine barriers for adoption of health care treatments. Implementation will be
assessed by examining participant adherence to the two CBT-CP-based programs (data
collected in an automated fashion from the painTRAINER platform and by the virtual CBT-CP
coaches in that arm of the study). Finally, Maintenance, or the opportunity thereof, will be
assessed through stakeholder interviews with clinical and operational leaders in each of the
participating health care systems.

In addition to EPIS and RE-AIM, we will utilize the Theoretical Framework of Acceptability
(TFA)’” to explore in-depth issues of satisfaction. The TFA is a multifaceted construct that
reflects the extent to which people delivering or receiving a health care intervention consider it
to be appropriate. The TFA is complimentary to constructs in the other two frameworks, while
further examining issues of acceptability, particularly for patients, less explored in either RE-AIM
or EPIS. The TFA consists of eight primary domains that have temporal aspects (e.g., before,
during, and after an intervention) and consider both anticipated reactions to an intervention as
well as cognitive and emotional responses experienced with an intervention. The domains
include affective attitude, burden, ethicality, intervention coherence, opportunity costs, perceived
effectiveness, and self-efficacy. As with EPIS and RE-AIM, we will use the TFA to guide
interview question development for all our stakeholders and will code for TFA related constructs
(e.g., sense of burden to participate) in our analysis process.

All audio-recorded interviews will be professionally transcribed, and coding will be completed by
trained coders using qualitative analysis software that aids management and interpretation of
text-based and other non-quantitative data. Reliability will be addressed by creating coding
definitions and modifying them as needed, clarifying coding instructions, and using an iterative
process of coding the same text and comparing codes and discussing discrepancies. Analytic
techniques best suited to answer the study aims, maximize validity, and develop an evolving
understanding of study findings will be utilized. These techniques can include using queries to

49

```

### DOC-002 physical page 62

[Direct source page 62](../../../joi250046supp1_prod_1755300121.14087.pdf#page=62)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

produce reports of text associated with primary codes and synthesizing themes from this text.
Retrieving coded information in multiple ways, including by participant features (e.g., gender,
pain diagnoses) by a code alone, or by combinations of co-occurring codes. Searches for text
strings that occur in the qualitative dataset will also be conducted. Analysis will involve
comparing themes and responses across participants and within categories of participants to
examine common patterns and differences in beliefs, attitudes, behaviors, and experiences.
Additionally, to ensure validity, searches for areas of contradiction across participants°*' and
across groups will be conducted. This approach to coding and data reduction will enable the
examination of issues from a number of perspectives and ensures a thorough review of the data
increase the breadth and depth of insights generate from the qualitative data gathered.

50

```

### DOC-002 physical page 63

[Direct source page 63](../../../joi250046supp1_prod_1755300121.14087.pdf#page=63)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

17 SOURCE DOCUMENTS AND ACCESS TO SOURCE DATA/DOCUMENTS

Study staff will maintain appropriate medical and research records for this study, in compliance
with ICH E6, regulatory and institutional requirements for the protection of confidentiality of
participants. Study staff will permit authorized representatives of the Data and Clinical
Coordinating Centers (DCC & CCC), upon request, for source verification of study
documentation, quality assurance reviews, audits, and evaluation of the study safety, progress,
and data validity. In addition, health information and data generated by this study must be
available for inspection upon request by representatives of the NIH and the Institutional Review
Board (IRB) for each study site.

Sources of Materials

Data will be obtained from multiple sources: electronic health records and administrative health
plan records; participant self-report (via online, mailed survey, or telephone administered
surveys); audio recordings of participant interviews; audio/video-recordings of virtual
intervention sessions; and utilization data from the painTRAINER website. Only approved
research staff with a need to review or analyze data will have access to study assessment data,
intervention program use data, aggregate EHR data or study transcripts. Only study staff
involved with administering study-related assessments (survey or interviews for the qualitative
evaluation activities), or study interventions will have access to individually identifiable private
information about participants.

Electronic Health Record (EHR) and Administrative Data. Patient health care utilization and
administrative data will be used for the identification of patients who are potentially eligible for
the study and to examine pertinent health care utilization patterns among study participants
(including health care encounters and pharmacy-related outcomes). All data will be extracted
from EHR and administrative databases in each of the health care systems participating in the
study. Prior to consent in order to identify potentially eligible patients, select variables will be
extracted and uploaded into the study’s electronic data capture system (EDC), which will be
password-protected and accessible only to authorized study staff. Only the minimum variables
needed to identify and recruit patients will be uploaded into the EDC. As part of the consenting
process, participants will be informed that their EHR data will be linked to their assessment data
and shared with the investigative team at KPWHRI to be included in analyses. No individual
identifying data will be published or released, and data will be summarized and presented only
in summary or statistical form.

Participant self-report data. Self-report data will be collected via online, mailed survey, or
telephone-administered survey and entered into either the KP CHR REDCap or the University of
Utah REDCap system, which will be password-protected and accessible only to authorized
study staff.

Audio- and video-recordings. Audio-recordings related to subject interviews will be kept in
password-protected electronic files on the servers maintained by KP. Audio- or video-
recordings related to the delivery of the virtual CBT-CP intervention will be kept in password-
protected electronic files maintained by KPWHRI and KP CHR on its servers. When relevant
(for interviews), transcription will occur with participant identifiers removed. No individual-
identifying data will be published or released, and data will be summarized and presented only
in summary or statistical form.

51

```

### DOC-002 physical page 64

[Direct source page 64](../../../joi250046supp1_prod_1755300121.14087.pdf#page=64)

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

Utilization data from the painTRAINER website. All data collected during participant interaction
with the painTRAINER intervention will be done through a secure, password-protected, mobile-
optimized website.

52

```

## Completion and limitations

Completed32/32 assigned physical pages,32 fresh renders,32 nonempty fresh OCR page transcriptions,22 local quantitative/analysis relationship keys, and32 explicit coverage rows. Five numeric/definition tables were visually inspected at physical pages34,36,42,55,59; eligibility comparator at37 and economic formula at58 were visually confirmed. No scientific-coverage gap remains in this shard. Native/layout font corruption is a reusable-derivative limitation covered by fresh CPU rendering and OCR. Raw OCR retains occasional glyph/citation/table-layout artifacts; visually confirmed planned numeric values above take precedence. No additional missing-data specification appears in these assigned units; this is a shard-bound statement, not a package-level conclusion. No source beyond physical pages33–64 was scientifically inspected, and no candidate diagnosis was performed.

Fresh processing window: 2026-10-11T08:25:04Z through 2026-10-11T08:28:05Z, approximately3 minutes before final completion checks. No fallback environment or GPU was used.
# Fresh protocol support mapping: DOC-002 physical pages 65–77

- Runtime scope: protocol_mapper_c; fresh support quantitative mapping shard.
- Exact source: joi250046supp1_prod_1755300121.14087.pdf; document role PLAN, determined by prospective protocol content.
- Version: RESOLVE UH3 Protocol, version 5.0, 10 Nov 2022, repeated in page headers. Physical pages 65–77 correspond to printed pages 53–65.
- Assigned units: 13; reusable-backed 0; fresh-required 13; freshly mapped 13. All 13 source-derived page images were opened visually and all 13 OCR transcriptions were read. No other scientific source unit was inspected by this shard.
- Extraction engines: direct Poppler pdftotext 26.01.0 (native and layout per page); direct Poppler pdftoppm 26.01.0 (150 dpi PNG CPU render); Tesseract 5.5.0, eng, psm 3, OMP_THREAD_LIMIT=1, CPU. No fallback environment, Python extraction, external sources or prior scientific conclusions used.
- Derivative names: preprocessing/protocol_c/native-N.txt, layout-N.txt, page-N.png, ocr-N.txt for each physical page N from 65 through 77. Every native/layout file is retained as a font-corrupted derivative, not usable scientific prose. Fresh image and OCR derivatives close coverage.
- Exact command patterns: `pdftotext -f N -l N SOURCE native-N.txt`; `pdftotext -layout -f N -l N SOURCE layout-N.txt`; `pdftoppm -f 65 -l 77 -r 150 -png SOURCE page`; `OMP_THREAD_LIMIT=1 tesseract page-N.png ocr-N -l eng --psm 3`.
- Scientific coverage gaps: None. OCR limitations: minor punctuation, bullet, superscript and reference-number segmentation artifacts; cited substantive passages below were confirmed on images. Raw OCR is preserved verbatim after the mapping and is a transcription aid. No statistical formulas, workbook values, tables, figures, result estimates or inferential tests occur in this shard.

## Page-by-page complete coverage

Source links are relative to this part's actual location; physical PDF page anchors are used throughout.

| Physical page | Printed page | Content inspected | Mapping / no-applicable record | Status |
|---|---:|---|---|---|
| [65](../../../joi250046supp1_prod_1755300121.14087.pdf#page=65) | 53 | Section 18 Quality control and quality assurance | P-C001 missing-data/data-anomaly clarification; no statistical missing-data method, endpoint, sample or result | COMPLETE |
| [66](../../../joi250046supp1_prod_1755300121.14087.pdf#page=66) | 54 | Sections 19.1–19.4 ethics, IRB, exclusions, confidentiality | P-C002 age and language exclusions; P-C003 amendment approval provision; remaining content administrative, no quantitative result | COMPLETE |
| [67](../../../joi250046supp1_prod_1755300121.14087.pdf#page=67) | 55 | Section 19.4.1 certificate of confidentiality | Administrative legal/privacy provisions only; no applicable result-relevant quantitative relationship | COMPLETE |
| [68](../../../joi250046supp1_prod_1755300121.14087.pdf#page=68) | 56 | Sections 20–20.4 data handling, reports, records, deviations | P-C004 safety/DSMB reports and EDA; P-C005 primary/secondary/derivative analysis completion; record retention at least three years is administrative | COMPLETE |
| [69](../../../joi250046supp1_prod_1755300121.14087.pdf#page=69) | 57 | Section 20.4 continuation, deviation reporting | Administrative reporting within 7 calendar days, repeated for rights/safety/welfare risk; no analysis rule or stopping threshold | COMPLETE |
| [70](../../../joi250046supp1_prod_1755300121.14087.pdf#page=70) | 58 | Section 21 publication | Publication, registration and results submission policy; no applicable outcome hierarchy or statistical rule | COMPLETE |
| [71](../../../joi250046supp1_prod_1755300121.14087.pdf#page=71) | 59 | Section 22 data sharing | P-C006 public database dictionary and unreliable elements; release at primary manuscript publication or within 12 months of last patient procedure, whichever first, is administrative | COMPLETE |
| [72](../../../joi250046supp1_prod_1755300121.14087.pdf#page=72) | 60 | Section 23 references 1–19 | Bibliographic only; no trial quantitative relationship; reference years/volumes/pages are not trial quantities | COMPLETE |
| [73](../../../joi250046supp1_prod_1755300121.14087.pdf#page=73) | 61 | References 20–37 | Bibliographic only; no trial quantitative relationship | COMPLETE |
| [74](../../../joi250046supp1_prod_1755300121.14087.pdf#page=74) | 62 | References 38–55 (55 continues) | Bibliographic only; instrument names BPI, PROMIS, EQ-5D-5L, PHQ-8, GAD-7, pain scales locate cited methods; no trial outcome status/definition follows from citation alone | COMPLETE |
| [75](../../../joi250046supp1_prod_1755300121.14087.pdf#page=75) | 63 | Reference 55 continuation, references 56–71 | Bibliographic only; no trial quantitative relationship | COMPLETE |
| [76](../../../joi250046supp1_prod_1755300121.14087.pdf#page=76) | 64 | References 72–90 | P-C007 method citation locators 86–89; no new statistical specification; remaining bibliographic only | COMPLETE |
| [77](../../../joi250046supp1_prod_1755300121.14087.pdf#page=77) | 65 | References 91–102 | Bibliographic only; economic net-benefit regression/acceptability-curve reference locators 91–93, childhood-intervention references 101–102; no new statistical specification | COMPLETE |

## Local relationship and context keys

These are source mapping records, not checker observations or candidates. Seven P-C keys retain all applicable contextual statements. Only P-C002 defines a numeric trial-population boundary; the others preserve administrative/analysis context without inventing a statistical design rule. No sample-size/power, endpoint definition/status/timepoint, model/covariates, analysis population label, imputation, sensitivity/subgroup result, multiplicity/interim/stopping rule, intervention dose/duration, or amendment/version difference is present in this exact shard. Its consistent version/date header identifies this content as version 5.0; comparison with other versions belongs to their assigned source scopes.

### P-C001 — Missing data clarification, section 18, physical page 65

Image-confirmed quotation: “Quality control (QC) procedures will be implemented beginning with the data collection and data QC checks that will be run on the database. Any missing data or data anomalies will be communicated to the site(s) for clarification/resolution.”

The Clinical Monitoring Plan is maintained by the CCC and Data Management Plan by the DCC. This is data collection/QC handling, with no imputation, missing-at-random assumption, excluded-participant rule or model specification. Matching main-paper key: data quality / missing data handling; do not equate database clarification with an inferential missing-data method.

### P-C002 — Eligibility boundary, section 19.3, physical page 66

Image-confirmed quotations: “Children under the age of 18 will be excluded.” “Adults who do not speak English will be excluded from study participation.”

The adult-tested telehealth CBT-CP interventions and assessment validation in adult samples are the stated rationale; pediatric mHealth versions contain a family component. Numeric population boundary: age less than 18 excluded; language boundary: non-English-speaking adults excluded. This section supplies no upper age limit or analyzed denominator. Matching main-paper keys: adult eligibility, age minimum and English language requirement.

### P-C003 — Amendment approval, section 19.2, physical page 66

Image-confirmed quotation: “Any amendment to the protocol will require review and approval by the IRB before the changes are implemented in the study.”

VUMC is the single IRB; KPGA, KPNW, KPWA and Essentia cede oversight. Approval of protocol and consent forms is required before enrollment. This states an administrative amendment process; no actual amendment or changed endpoint/model is supplied on this page. Matching main-paper key: disclosed protocol changes only if another source supplies the change itself.

### P-C004 — Safety and monitoring reports, section 20.2, physical page 68

Image-confirmed quotation: “For safety analyses and DSMB report production, the JHU-Tufts Statistical Core, physically located at the Johns Hopkins University will examine or oversee data quality, create secondary variables, and perform exploratory data analyses (EDA).”

DCC creates recruitment/data-collection, ongoing QA/DSMB and intervention monitoring reports or makes data available to the appropriate TIC/RIC. “Secondary variables” here denotes generated variables and does not designate secondary clinical outcomes. No stopping rule, safety threshold or safety-analysis population is defined. Matching main-paper key: monitoring/safety reporting, EDA scope.

### P-C005 — Completion of analyses, section 20.3, physical page 68

Image-confirmed quotation: “Completion of the research for this protocol should be anticipated to include planned primary and secondary analyses, as well as subsequent derivative analyses.”

Record retention is at least three years from submission of the last grant federal financial report. The completion statement does not name an outcome, hierarchy, analysis model or reporting time. Matching main-paper key: planned analysis completion; use named outcome/analysis definitions from other assigned pages for actual comparisons.

### P-C006 — Public database, section 22, physical page 71

Image-confirmed quotation: “The DCC will also prepare a data dictionary that provides a concise definition of every data element included in the database. If specific data elements have idiosyncrasies that might affect interpretation or analysis, this will be discussed in the dictionary document. Data elements that are considered unreliable will be deleted, and this will be noted in the documentation.”

Immediate context is the public/releasable de-identified database, which lacks institutional identifiers. It does not say the trial primary analysis deletes unreliable outcome data or define a missing-data strategy. Release timing is primary manuscript publication or within 12 months of last patient procedure, whichever first. Matching main-paper key: data availability/dictionary; no inferential analysis specification inferred.

### P-C007 — Bibliographic statistical-method locators, physical pages 76–77

Source-confirmed reference entries relevant as locators only:

- 86, physical page 76: “Zou G. A modified poisson regression approach to prospective studies with binary data. Am J Epidemiol. 2004;159(7):702-706.”
- 87, physical page 76: “SL LJZ. Longitudinal data analysis using generalized linear models. Biometrika. 1986;73(1):13-22.” Author string is preserved as supplied; no expansion inferred.
- 88, physical page 76: “COST-EFFECTIVENESS in HEALTH and MEDICINE. New York, NY: Oxford University Press, Inc.; 1996.”
- 89, physical page 76: “Sanders GD, Neumann PJ, Basu A, et al. Recommendations for Conduct, Methodological Practices, and Reporting of Cost-effectiveness Analyses: Second Panel on Cost-Effectiveness in Health and Medicine. Jama. 2016;316(10):1093-1103.”
- 91, physical page 77: “Hoch JS, Briggs AH, Willan AR. Something old, something new, something borrowed, something blue: a framework for the marriage of health econometrics and cost-effectiveness analysis. Health economics. 2002;11(5):415-430.”
- 92, physical page 77: “Hoch JS, Rockx MA, Krahn AD. Using the net benefit regression framework to construct cost-effectiveness acceptability curves: an example using data from a trial of external loop recorders versus Holter monitoring for ambulatory monitoring of ‘community acquired’ syncope. BMC Health Serv Res. 2006;6:68.”

No external reference was accessed. Matching main-paper keys: modified Poisson binary analysis, longitudinal GLM/GEE, economic analysis, only when identified by supplied plan/report prose elsewhere. These citations alone establish neither a covariance estimator nor a particular inferential method for the trial.

## Full per-page fresh OCR transcription

The following unedited OCR blocks preserve all page contents for locator use, including administrative text and bibliography. Source images govern punctuation, superscripts, reference numbering and any ambiguous token. Substantive passages quoted above were visually checked. Complete images remain in preprocessing/protocol_c.

### DOC-002 physical page 65 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

18 QUALITY CONTROL AND QUALITY ASSURANCE

The Clinical Monitoring Plan, maintained by the CCC, and Data Management Plan, maintained
by the DCC, describe the processes related to quality management for the study.

Quality control (QC) procedures will be implemented beginning with the data collection and data
QC checks that will be run on the database. Any missing data or data anomalies will be
communicated to the site(s) for clarification/resolution.

Following written Standard Operating Procedures (SOPs), the study monitors will verify that the
clinical trial is conducted, and data are generated, documented (recorded), and reported in
compliance with the protocol, International Conference on Harmonisation Good Clinical Practice
(ICH GCP), and applicable regulatory requirements.

The study sites will provide access to all trial-related locations, source data/documents, and
reports for the purpose of monitoring and auditing by the sponsor, and inspection by local and
regulatory authorities.

53

```

### DOC-002 physical page 66 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

19 ETHICS/PROTECTION OF HUMAN SUBJECTS
19.1 Ethical Standard

The investigator will ensure that this study is conducted in full conformity with the principles set
forth in The Belmont Report: Ethical Principles and Guidelines for the Protection of Human
Subjects of Research, as drafted by the US National Commission for the Protection of Human
Subjects of Biomedical and Behavioral Research (April 18, 1979) and codified in 45 CFR Part
46 and/or the ICH E6.

19.2 Institutional Review Board

The Vanderbilt University Medical Center (VUMC) IRB will serve as the single IRB (SIRB) for
this study. The local IRBs for KPGA, KPNW, KPWA and Essentia will cede oversight to the
VUMC IRB.

The protocol, informed consent form(s), recruitment materials, and all participant materials will
be submitted to the IRB for review and approval. Approval of both the protocol and the consent
form(s) must be obtained before any participant is enrolled. Any amendment to the protocol will
require review and approval by the IRB before the changes are implemented in the study.

19.3. Exclusion of Women, Minorities, and Children (Special Populations)

Children under the age of 18 will be excluded. mHealth versions of CBT-CP have been
developed for children and adolescents," but they all include a family component that differs
substantially from the telehealth CBT-CP programs under evaluation in this study, both of which
were developed and tested among adult samples. Further, our standardized assessment
measures were validated in adult samples and as such, are not always applicable to children
and adolescents.

Adults who do not speak English will be excluded from study participation. The interventions to
be studied in this comparative effectiveness trial have not been developed for or tested for
effectiveness in non-English speaking populations and are therefore not available for inclusion
in this trial.

19.4 Subject Confidentiality

Subject confidentiality is strictly held in trust by the investigators, study staff, and the study
sponsor(s) and their agents. This confidentiality is extended to any study information relating to
participants.

The study protocol, documentation, data, and all other information generated will be held in
strict confidence. No information concerning the study, or the data will be released to any
unauthorized third party without prior written approval of the study sponsor.

The study monitor(s) or other authorized representatives of the Data and Clinical Coordinating
Centers (DCC & CCC), NIH and the Institutional Review Board (IRB), may inspect all study
documents and records required to be maintained by the site investigators.

54

```

### DOC-002 physical page 67 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

19.4.1 Certificate of Confidentiality

To further protect the privacy of study participants, the Secretary, Health and Human Services
(HHS), has issued a Certificate of Confidentiality (CoC) to all researchers engaged in
biomedical, behavioral, clinical, or other human subjects research funded wholly or in part by
the federal government. Recipients of NIH funding for human subjects research are required to
protect identifiable research information from forced disclosure per the terms of the NIH Policy
(https:/humansubjects.nih.gov/coc/index). As set forth in 45 CFR Part 75.303(a) and NIHGPS
Chapter 8.3, recipients conducting NIH-supported research covered by this Policy are required
to establish and maintain effective internal controls (e.g., policies and procedures) that provide
reasonable assurance that the award is managed in compliance with Federal statutes,
regulations, and the terms and conditions of the award. It is the NIH policy that investigators and
others who have access to research records will not disclose identifying information except
when the participant consents or in certain instances when federal, state, or local law or
regulation requires disclosure. NIH expects investigators to inform research participants of the
protections and the limits to protections provided by a Certificate issued by this Policy.

55

```

### DOC-002 physical page 68 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

20 DATA HANDLING AND RECORD KEEPING

The investigators are responsible for ensuring the accuracy, completeness, legibility, and
timeliness of the data reported. All source documents should be completed in a neat, legible
manner to ensure accurate interpretation of data and kept in a secure file container throughout
the duration of the study. The investigators will maintain adequate case histories of study
participants, including accurate case report forms (CRFs), and source documentation.

20.1 Data Management Responsibilities

Data collection and accurate documentation are the responsibility of the study staff under the
supervision of the investigator. All source documents must be reviewed by the study team and
data entry staff, who will ensure that they are accurate and complete. Study staff are
responsible for training interviewers and providing participants’ clear and adequate instructions
for survey completion so that valid data capture is accomplished.

Unanticipated problems and AEs identified must be reviewed by the investigator or designee.

Data will be stored at the University of Utah and KP CHR, which are responsible for security of
their information systems.

20.2 Schedule and Content of Reports

The Data Coordinating Center will be responsible for creating the following reports or making
the data available to the appropriate TIC/RIC: recruitment and data collection reports, ongoing
QA monitoring and DSMB reports, and intervention monitoring reports. For safety analyses and
DSMB report production, the JHU-Tufts Statistical Core, physically located at the Johns Hopkins
University will examine or oversee data quality, create secondary variables, and perform
exploratory data analyses (EDA).

20.3 Study Records Retention

Study records will be maintained for at least three years from the date that the last grant federal
financial report (FFR) is submitted to the NIH.

Completion of the research for this protocol should be anticipated to include planned primary
and secondary analyses, as well as subsequent derivative analyses.

Completion of the research also entails completion of all publications relating to the research. All
records shall be accessible for inspection and copying by authorized representatives of the
regulatory authorities at reasonable times and in a reasonable manner [45 CFR §46.115(b)].

20.4 Protocol Deviations

A protocol deviation is any noncompliance with the clinical study protocol or Good Clinical
Practice requirements. The noncompliance may be on the part of the participant, the
investigator, or study staff. As a result of deviations, corrective actions are to be developed by
the study staff and implemented promptly as determined by the IRB.

These practices are consistent with ICH E6:

56

```

### DOC-002 physical page 69 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

e¢ Compliance with Protocol, section 4.5
¢ Quality Assurance and Quality Control, section 5.1
e Noncompliance, section 5.20

It is the responsibility of the Principal Investigator(s) to use continuous vigilance to identify and
report any deviations within 7 calendar days of identification of the protocol deviation to the
HEAL ERN within the DCC REDCap system. Protocol deviations that result in increased risk or
affect the participant’s rights, safety, or welfare will also be reported to the IRB and the NIA
Program Official within 7 calendar days of identification of the problem.

57

```

### DOC-002 physical page 70 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

21 PUBLICATION

The study PI in collaboration with select study team members will develop a publication policy
which will specify publication procedures and authorship requirements. The study will comply
with NIH’s Public Access Policy and Policy on the Dissemination of NIH-Funded Clinical Trial
Information, as described below.

NIH Public Access Policy
The NIH Public Access Policy requires scientists to submit final peer-reviewed journal

manuscripts that arise from NIH funds to PubMed Central immediately upon acceptance for
publication. This ensures that the public has access to the published results of NIH funded
research.

NIH Policy on the Dissemination of NIH-Funded Clinical Trial Information

The study is a clinical trial and will comply with the NIH policy that establishes the expectation
that all investigators conducting clinical trials funded in whole or in part by the NIH will ensure
that these trials are registered at ClinicalTrials.gov, and that results of these trials are submitted
to ClinicalTrials.gov.

58

```

### DOC-002 physical page 71 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

22 DATA SHARING

This study will comply with all applicable NIH Data Sharing Policies. (See
https://grants.nih.gov/policy/sharing.htm for policies and resources)

The DCC will produce a public/releasable database from the RESOLVE study. The releasable
database will be completely de-identified in accordance with the definitions provided in the
Health Insurance Portability and Accountability Act (HIPAA). Namely, all identifiers specified in
HIPAA will be recoded in a manner that will make it impossible to deduce or impute the specific
identity of any patient. The database will not contain any institutional identifiers.

The DCC will also prepare a data dictionary that provides a concise definition of every data
element included in the database. If specific data elements have idiosyncrasies that might affect
interpretation or analysis, this will be discussed in the dictionary document. Data elements that
are considered unreliable will be deleted, and this will be noted in the documentation.

The policies for release of this database will be determined by the NIH. These policies are
expected to focus primarily on the timing of data release. The preliminary plan is to release the
database (defined below) at the time of publication of the primary manuscript, or within 12
months of last patient procedure, whichever comes first. Implementation of the plan will follow
the HEAL Public Access and Data Sharing Policy as outlined at
https://heal.nih.gov/about/public-access-data.

In accordance with policies of the NIH, the DCC will send the releasable database and its
relevant documentation to the entity determined by the NIH or specific institute to be the
repository for data created under the HEAL initiative.

Access to the releasable database housed in the NIH-assigned repository will be in accordance
with procedures and regulations of the NIH or specific institute.

59

```

### DOC-002 physical page 72 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

23 REFERENCES

1.

2.

10.

11.

12.

13.

14.

15.

16.

17.

18.

19.

Institute of Medicine. Relieving Pain in America: A Blueprint for Transforming Prevention,
Care, Education and Research. Washington DC2011.

Pain Management Task Force. Providing a Standardized DoD and VHA Vision and
Approach to Pain Management to Optimize the Care for Warriors and their Families.
5/2010 2010.

Von Korff M, Scher Al, Helmick C, et al. United States National Pain Strategy for
Population Research: Concepts, Definitions, and Pilot Data. J Pain. 2016;17(10):1068-
1080.

Dahlhamer J, Lucas J, Zelaya C, et al. Prevalence of Chronic Pain and High-Impact
Chronic Pain Among Adults - United States, 2016. MMWR Morbidity and mortality
weekly report. 2018;67(36):1001-1006.

Rost K, Fortney J, Fischer E, Smith J. Use, quality, and outcomes of care for mental
health: the rural perspective. Med Care Res Rev. 2002;59(3):231-265; discussion 266-
271.

Tollefson J, Usher K. Chronic pain in the rural arena. The Australian journal of rural
health. 2006;14(3):134-135.

Goode AP, Freburger JK, Carey TS. The influence of rural versus urban residence on
utilization and receipt of care for chronic low back pain. J Rural Health. 2013;29(2):205-
214.

Hoffman PK, Meier BP, Council JR. A comparison of chronic pain between an urban and
rural population. Journal of community health nursing. 2002;19(4):213-224.

Nelson JA GB. Rural health: access to care and services. Home Health Care
Management and Practice. 2010;22(5):339-343.

Chou R, Turner JA, Devine EB, et al. The effectiveness and risks of long-term opioid
therapy for chronic pain: a systematic review for a National Institutes of Health Pathways
to Prevention Workshop. Ann Intern Med. 2015;162(4):276-286.

Von Korff MR, Franklin G. Responding to America's latrogenic Epidemic of Prescription
Opioid Addiction and Overdose. Med Care. 2016;54(5):426-429.

Von Korff M, Kolodny A, Deyo RA, Chou R. Long-term opioid therapy reconsidered. Ann
Intern Med. 2011;155(5):325-328.

Cicero TJ, Surratt H, Inciardi JA, Munoz A. Relationship between therapeutic use and
abuse of opioid analgesics in rural, suburban, and urban locations in the United States.
Pharmacoepidemiol Drug Saf. 2007;16(8):827-840.

Okie S. A flood of opioids, a rising tide of deaths. N Engl J Med. 2010;363(21):1981-
1985.

Von Korff MR. Health care for chronic pain: overuse, underuse, and treatment needs:
commentary on: chronic pain and health services utilization-is there overuse of
diagnostic tests and inequalities in nonpharmacologic methods utilization? Med Care.
2013;51(10):857-858.

Skelly AC, Chou R, Dettori JR, et al. AHRQ Comparative Effectiveness Reviews. In:
Noninvasive Nonpharmacological Treatment for Chronic Pain: A Systematic Review.
Rockville (MD): Agency for Healthcare Research and Quality (US); 2018.

Thorn BE, Day MA, Burns J, et al. Randomized trial of group cognitive behavioral
therapy compared with a pain education control for low-literacy rural people with chronic
pain. Pain. 2011;152(12):2710-2720.

Turk DC, Meichenbaum D, Genest M. Pain and behavioral medicine: A cognitive
behavioral perspective. New York: Guilford Press; 1983.

Interagency Pain Research Coordinating Committee. National Pain Strategy: A
Comprehensive Population Health-Level Strategy by Pain. 2015 2015.

60

```

### DOC-002 physical page 73 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

20,

21.

22.

23,

24.

25.

26.

27.

28.

29.

30.

31.

32.

33.

34.

35.

36.

37.

Stewart MO, Karlin BE, Murphy JL, et al. National dissemination of cognitive-behavioral
therapy for chronic pain in veterans: therapist and patient-level outcomes. Clin J Pain.
2015;31(8):722-729.

Keefe FJ, Main CJ, George SZ. Advancing Psychologically Informed Practice for
Patients With Persistent Musculoskeletal Pain: Promise, Pitfalls, and Solutions. Phys
Ther. 2018;98(5):398-407.

Waller G, Turner H. Therapist drift redux: Why well-meaning clinicians fail to deliver
evidence-based therapy, and how to get back on track. Behav Res Ther. 2016;77:129-
137.

Kapoor S, Thorn BE. Healthcare use and prescription of opioids in rural residents with
pain. Rural Remote Health. 2014;14(3):2879.

Cully JA, Jameson JP, Phillips LL, Kunik ME, Fortney JC. Use of psychotherapy by rural
and urban veterans. J Rural Health. 2010;26(3):225-233.

Cherkin DC, Sherman KJ, Balderson BH, et al. Effect of Mindfulness-Based Stress
Reduction vs Cognitive Behavioral Therapy or Usual Care on Back Pain and Functional
Limitations in Adults With Chronic Low Back Pain: A Randomized Clinical Trial. Jama.
2016;315(12):1240-1249.

Jensen MP, Nielson WR, Kerns RD. Toward the development of a motivational model of
pain self-management. J Pain. 2003;4(9):477-492.

Bair MJ, Matthias MS, Nyland KA, et al. Barriers and facilitators to chronic pain self-
management: a qualitative study of primary care patients with comorbid musculoskeletal
pain and depression. Pain medicine (Malden, Mass). 2009; 10(7):1280-1290.

Ludman EJ, Simon GE, Tutty S, Von Korff M. A randomized trial of telephone
psychotherapy and pharmacotherapy for depression: continuation and durability of
effects. J Consult Clin Psychol. 2007;75(2):257-266.

Simon GE, Ludman EJ, Tutty S, Operskalski B, Von Korff M. Telephone psychotherapy
and telephone care management for primary care patients starting antidepressant
treatment: a randomized controlled trial. Jama. 2004;292(8):935-942.

McBeth J, Prescott G, Scotland G, et al. Cognitive behavior therapy, exercise, or both for
treating chronic widespread pain. Arch Intern Med. 2012;172(1):48-57.

Eccleston C, Fisher E, Craig L, Duggan GB, Rosser BA, Keogh E. Psychological
therapies (Internet-delivered) for the management of chronic pain in adults. Cochrane
Database Syst Rev. 2014(2):Cd010152.

Macea DD, Gajos K, Daglia Calil YA, Fregni F. The efficacy of Web-based cognitive
behavioral interventions for chronic pain: a systematic review and meta-analysis. J Pain.
2010;11(10):917-929.

Waegemann CP. mHealth: the next generation of telemedicine? Telemedicine journal
and e-health : the official journal of the American Telemedicine Association.
2010;16(1):23-25.

Hamine S, Gerth-Guyette E, Faulx D, Green BB, Ginsburg AS. Impact of mHealth
chronic disease management on treatment adherence and patient outcomes: a
systematic review. J Med Internet Res. 2015;17(2):e52.

Mehrotra A RK, Brockmeyer DM, Barnett ML, Bender JA. Rapidly Converting to “Virtual
Practices : Outpatient Care in the Era of Covid-19. NEJM Catalyst. 2020.

Eccleston C, Blyth FM, Dear BF, et al. Managing patients with chronic pain during the
COVID-19 outbreak: considerations for the rapid introduction of remotely supported
(eHealth) pain management services. Pain. 2020;161(5):889-893.

Pitcher MH, Von Korff M, Bushnell MC, Porter L. Prevalence and Profile of High-Impact
Chronic Pain in the United States. J Pain. 2019;20(2):146-160.

61

```

### DOC-002 physical page 74 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

38.

39.

40.

41,

42.

43.

44.

45.

46.

47.

48.

49.

50.

51.

52.

53.

54.

55.

Ehde DM, Dillworth TM, Turner JA. Cognitive-behavioral therapy for individuals with
chronic pain: efficacy, innovations, and directions for research. Am Psychol.
2014;69(2):153-166.

Feinberg S, Feinberg R, Pohl M, Bokarius V, Darnall B. American Chronic Pain
Association Resource Guide to Chronic Pain Management. In. An Integrated Guide to
Medical, Interventional, Behavioral, Pharmacologic and Rehabilitation Therapies:
Rocklin, CA: American Chronic Pain Association, Inc; 2018.

Cleeland C, Ryan K. Pain assessment: global use of the Brief Pain Inventory. Annals of
the Academy of Medicine, Singapore. 1994;23(2):129-138.

Keller S, Bann CM, Dodd SL, Schein J, Mendoza TR, Cleeland CS. Validity of the brief
pain inventory for use in documenting the outcomes of patients with noncancer pain. The
Clinical journal of pain. 2004;20(5):309-318.

Tan G, Jensen MP, Thornby JI, Shanti BF. Validation of the Brief Pain Inventory for
chronic nonmalignant pain. The Journal of Pain. 2004;5(2):133-137.

Dworkin RH, Turk DC, McDermott MP, et al. Interpreting the clinical importance of group
differences in chronic pain clinical trials: IMMPACT recommendations. Pain.

2009; 146(3):238-244.

Carle AC, Riley W, Hays RD, Cella D. Confirmatory Factor Analysis of the Patient
Reported Outcomes Measurement Information System (PROMIS) Adult Domain
Framework Using Item Response Theory Scores. Med Care. 2015;53(10):894-900.
Herdman M, Gudex C, Lloyd A, et al. Development and preliminary testing of the new
five-level version of EQ-5D (EQ-5D-5L). Qual Life Res. 2011;20(10):1727-1736.
Hornbrook M, Goodman, M.J., ed Adjusting health benefit contributions to reflect risks.
Greenwich: JAI Press; 1991. Hornbrook M, ed. Risk Based Contributions to Private
Health Insurance; No. 41.

O'Keeffe-Rosetti MC, Hornbrook MC, Fishman PA, et al. A standardized relative
resource cost model for medical care: application to cancer control programs. Journal of
the National Cancer Institute Monographs. 2013;2013(46):106-116.

Kroenke K, Strine TW, Spitzer RL, Williams JB, Berry JT, Mokdad AH. The PHQ-8 as a
measure of current depression in the general population. J Affect Disord. 2009;114(1-
3):163-173.

Spitzer RL, Kroenke K, Williams JB, Lowe B. A brief measure for assessing generalized
anxiety disorder: the GAD-7. Arch Intern Med. 2006;166(10):1092-1097.

Full KM, Malhotra A, Crist K, Moran K, Kerr J. Assessing psychometric properties of the
PROMIS Sleep Disturbance Scale in older adults in independent-living and continuing
care retirement communities. Sleep Health. 2019;5(1):18-22.

Von Korff M, DeBar LL, Krebs EE, Kerns RD, Deyo RA, Keefe FJ. Graded chronic pain
scale revised: mild, bothersome, and high-impact chronic pain. Pain. 2020;161(3):651-
661.

Mayhew M, DeBar LL, Deyo RA, et al. Development and Assessment of a Crosswalk
Between ICD-9-CM and ICD-10-CM to Identify Patients with Common Pain Conditions. J
Pain. 2019.

McWilliams LA, Kowal J, Wilson KG. Development and evaluation of short forms of the
Pain Catastrophizing Scale and the Pain Self-efficacy Questionnaire. Eur J Pain.
2015;19(9):1342-1349.

Anderson KO, Dowds BN, Pelletz RE, Edwards WT, Peeters-Asdourian C. Development
and initial validation of a scale to measure self-efficacy beliefs in patients with chronic
pain. Pain. 1995;63(1):77-84.

Vugts MAP, Joosen MCW, van der Geer JE, Zedlitz A, Vrijhoef HJM. The effectiveness
of various computer-based interventions for patients with chronic pain or functional

62

```

### DOC-002 physical page 75 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0
10 Nov 2022

somatic syndromes: A systematic review and meta-analysis. PloS one.
2018;13(5):e0196467.

56. Martorella G, Boitor M, Berube M, Fredericks S, Le May S, Gelinas C. Tailored Web-
Based Interventions for Pain: Systematic Review and Meta-Analysis. J Med Internet
Res. 2017;19(11):e385.

57. Bennell KL, Nelligan RK, Rini C, et al. Effects of internet-based pain coping skills training
before home exercise for individuals with hip osteoarthritis (HOPE trial): a randomised
controlled trial. Pain. 2018;159(9):1833-1842.

58. Bennell KL, Nelligan R, Dobson F, et al. Effectiveness of an Internet-Delivered Exercise
and Pain-Coping Skills Training Intervention for Persons With Chronic Knee Pain: A
Randomized Trial. Ann Intern Med. 2017;166(7):453-462.

59. Rini C, Porter LS, Somers TJ, et al. Automated Internet-based pain coping skills training
to manage osteoarthritis pain: a randomized controlled trial. Pain. 2015;156(5):837-848.

60. Rini C, Porter LS, Somers TJ, McKee DC, Keefe FJ. Retaining critical therapeutic
elements of behavioral interventions translated for delivery via the Internet:
recommendations and an example using pain coping skills training. J Med Internet Res.
2014;16(12):e245.

61. Bair MJ, Ang D, Wu J, et al. Evaluation of Stepped Care for Chronic Pain (ESCAPE) in
Veterans of the Iraq and Afghanistan Conflicts: A Randomized Clinical Trial. JAMA
Intern Med. 2015;175(5):682-689.

62. Kroenke K, Bair MJ, Damush TM, et al. Optimized antidepressant therapy and pain self-
management in primary care patients with depression and musculoskeletal pain: a
randomized controlled trial. JAMA. 2009;301(20):2099-2110.

63. Kealey KA, Ludman EJ, Marek PM, Mann SL, Bricker JB, Peterson AV. Design and
implementation of an effective telephone counseling intervention for adolescent smoking
cessation. Journal of the National Cancer Institute. 2009;101(20):1393-1405.

64. McClure JB, Ludman EJ, Grothaus L, Pabiniak C, Richards J. Impact of a brief
motivational smoking cessation intervention the Get PHIT randomized controlled trial.
Am J Prev Med. 2009;37(2):116-123.

65. Simon GE, Ludman EJ, Rutter CM. Incremental benefit and cost of telephone care
management and telephone psychotherapy for depression in primary care. Arch Gen
Psychiatry. 2009;66(10):1081-1089.

66. Simon GE, VonKorff M, Rutter C, Wagner E. Randomised trial of monitoring, feedback,
and management of care by telephone to improve treatment of depression in primary
care. Bmj. 2000;320(7234):550-554.

67. Wang PS, Simon GE, Avorn J, et al. Telephone screening, outreach, and care
management for depressed workers and impact on clinical and work productivity
outcomes: a randomized controlled trial. JAMA. 2007;298(12):1401-1411.

68. Carmody TP, Duncan CL, Huggins J, et al. Telephone-delivered cognitive-behavioral
therapy for pain management among older military veterans: a randomized trial. Psychol
Serv. 2013;10(3):265-275.

69. Rutledge T, Atkinson JH, Chircop-Rollick T, et al. Randomized Controlled Trial of
Telephone-delivered Cognitive Behavioral Therapy Versus Supportive Care for Chronic
Back Pain. Clin J Pain. 2018;34(4):322-327.

70. DeBar L, Mayhew M, Benes L, et al. A Primary Care-Based Cognitive Behavioral
Therapy Intervention for Long-Term Opioid Users With Chronic Pain: A Randomized
Pragmatic Trial. Annals of internal medicine. 2022;175(1):46-55.

71. DeBar L, Benes L, Bonifay A, et al. Interdisciplinary team-based care for patients with
chronic pain on long-term opioid treatment in primary care (PPACT) - Protocol for a
pragmatic cluster randomized trial. Contemp Clin Trials. 2018;67:91-99.

63

```

### DOC-002 physical page 76 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

72,

73.

74.

75.

76.

77.

78.

79.

80.

81.

82.

83.

84.

85.

86.

87.

88.

89.

90.

Bandura A. Self-efficacy: The exercise of control. New York: W.H. Freeman and
Company.; 1997.

Bandura A. Social foundations of thought and action: A social cognitive theory.
Englewood Cliffs, N.J.: Prentice-Hall; 1986.

Kennedy CM, Powell J, Payne TH, Ainsworth J, Boyd A, Buchan I. Active Assistance
Technology for Health-Related Behavior Change: An Interdisciplinary Review. Journal of
Medical Internet Research. 2012;14(3):e80.

Knowles MS, Holton EF, Swanson RA. The adult learner: The definitive classic in adult
education and human resource development. 7th ed. Boston: Elsevier; 2011.

Mayer RE. Applying the science of learning: evidence-based principles for the design of
multimedia instruction. American Psychologist. 2008;63(8):760-769.

Michie S, Richardson M, Johnston M, et al. The behavior change technique taxonomy
(v1) of 93 hierarchically clustered techniques: building an international consensus for the
reporting of behavior change interventions. Ann Behav Med. 2013;46(1):81-95.

Rini C, Williams DA, Broderick JE, Keefe FJ. Meeting them where they are: Using the
Internet to deliver behavioral medicine interventions for pain. Trans! Behav Med.
2012;2(1):82-92.

The Plain Language Action and Information Network. plainlanguage.gov.
https://plainlanquage.gov/. Accessed February 5, 2019.

Bellg AJ, Borrelli B, Resnick B, et al. Enhancing treatment fidelity in health behavior
changer studies: Best practices and recommendations from the NIH Behavior Change
Consortium. Health Psychology. 2004;23(5):443-451.

Von Korff M, Balderson BH, Saunders K, et al. A trial of an activating intervention for
chronic back pain in primary care and physical therapy settings. Pain. 2005;113(3):323-
330.

Vitiello MV, McCurry SM, Shortreed SM, et al. Cognitive-behavioral treatment for
comorbid insomnia and osteoarthritis pain in primary care: the lifestyles randomized
controlled trial. J Am Geriatr Soc. 2013;61(6):947-956.

Bennell KL, Ahamed Y, Jull G, et al. Physical Therapist-Delivered Pain Coping Skills
Training and Exercise for Knee Osteoarthritis: Randomized Controlled Trial. Arthritis
Care Res (Hoboken). 2016;68(5):590-602.

Palermo TM, Slack K, Loren D, Eccleston C, Jamison RN. Measuring and reporting
adverse events in clinical trials of psychological treatments for chronic pain. Pain.
2020;161(4):713-717.

Peterson K, Anderson J, Bourne D, Mackey K, Helfand M. Effectiveness of Models Used
to Deliver Multimodal Care for Chronic Musculoskeletal Pain: a Rapid Evidence Review.
J Gen Intern Med. 2018;33(Suppl 1):71-81.

Zou G. A modified poisson regression approach to prospective studies with binary data.
Am J Epidemiol. 2004;159(7):702-706.

SL LJZ. Longitudinal data analysis using generalized linear models. Biometrika.
1986;73(1):13-22.

COST-EFFECTIVENESS in HEALTH and MEDICINE. New York, NY: Oxford University
Press, Inc.; 1996.

Sanders GD, Neumann PJ, Basu A, et al. Recommendations for Conduct,
Methodological Practices, and Reporting of Cost-effectiveness Analyses: Second Panel
on Cost-Effectiveness in Health and Medicine. Jama. 2016;316(10):1093-1103.

Smith DH, O'Keeffe-Rosetti M, Owen-Smith AA, et al. Improving Adherence to
Cardiovascular Therapies: An Economic Evaluation of a Randomized Pragmatic Trial.
Value in Health. 2016;19(2):176-184.

64

```

### DOC-002 physical page 77 — raw Tesseract CPU OCR

```text
RESOLVE UH3 Protocol Version 5.0

10 Nov 2022

91,

92.

93.

94,

95.

96.

97.

98.
99.
100.
101.

102.

Hoch JS, Briggs AH, Willan AR. Something old, something new, something borrowed,
something blue: a framework for the marriage of health econometrics and cost-
effectiveness analysis. Health economics. 2002;11(5):415-430.

Hoch JS, Rockx MA, Krahn AD. Using the net benefit regression framework to construct
cost-effectiveness acceptability curves: an example using data from a trial of external
loop recorders versus Holter monitoring for ambulatory monitoring of "community
acquired" syncope. BMC Health Serv Res. 2006;6:68.

Meenan RT, Stevens VJ, Hornbrook MC, et al. Cost-effectiveness of a hospital-based
smoking cessation intervention. Medical care. 1998;36(5):670-678.

Aarons GA, Hurlburt M, Horwitz SM. Advancing a conceptual model of evidence-based
practice implementation in public service sectors. Adm Policy Ment Health. 2011;38(1):4-
23.

Glasgow RE. RE-AlMing research for application: ways to improve evidence for family
medicine. J Am Board Fam Med. 2006;19(1):11-19.

Glasgow RE, Vogt TM, Boles SM. Evaluating the public health impact of health
promotion interventions: the RE-AIM framework. Am J Public Health. 1999;89(9):1322-
1327.

Sekhon M, Cartwright M, Francis JJ. Acceptability of healthcare interventions: an
overview of reviews and development of a theoretical framework. BMC Health Services
Research. 2017;17(1):88.

Bernard HR. Research methods in anthropology: Qualitative and quantitative
approaches. 2nd Edition ed. Thousand Oaks, CA: Sage Publications; 1994.

Miller WL, Crabtree BF. Clinical research. In: Denzin NK, Lincoln YS, eds. Strategies of
Qualitative Inquiry. Thousand Oaks, California: Sage Publications; 1998:292-314.
Spradley JP. Participant Observation. New York: Holt, Rinehart & Winston; 1980.
Palermo TM, Law EF, Fales J, Bromberg MH, Jessen-Fiddick T, Tai G. Internet-
delivered cognitive-behavioral treatment for adolescents with chronic pain and their
parents: a randomized controlled multicenter trial. Pain. 2016;157(1):174-185.
Eccleston C, Palermo TM, Williams AC, et al. Psychological therapies for the
management of chronic and recurrent pain in children and adolescents. Cochrane
Database Syst Rev. 2014(5):Cd003968.

65

```
# DOC-003 SAP quantitative evidence, physical pages 1–29

Document role: PLAN. Scope: every physical PDF page 1–29 of `joi250046supp2_prod_1755300121.15087.pdf`; no other source was read for scientific mapping. Local keys SAP-N001 onward track numeric definitions; SAP-S001 onward track inferential relationships. Matching main-paper keys below are semantic join keys, not claims that a main-paper occurrence was inspected. No candidates are selected or diagnosed here.

## Engines and source authority

All 29 pages were freshly rendered with direct Poppler pdftoppm 26.01.0, `-r 160 -png`, CPU, and freshly recognized using Tesseract 5.5.0, `OMP_THREAD_LIMIT=1`, `-l eng --psm 3`. Derivatives are `preprocessing/sap_mapper/page-01.png` through `page-29.png` and corresponding `.txt` files, relative to the run directory. Fresh full native and layout extraction used Poppler pdftotext 26.01.0 (`native.txt`, `layout.txt` in that directory); font-corrupted native/layout outputs cannot support substantive transcription. OCR is a locator/transcription aid; the exact PDF remains final authority. Visual confirmation resolved thresholds, table cell alignment, title version, and formulas on pages 1, 11, 14, 17, 18, 21, and 23. No external links printed in the SAP were opened.

Source links below are relative to this part: [SAP](../../../joi250046supp2_prod_1755300121.15087.pdf#page=1). Unit coverage is explicit at the end. No workbook formulas or cached values are applicable to this PDF.

## Identity and amendments

- SAP-N001, p1: exact title `STATISTICAL ANALYSIS PLAN`; `ClinicalTrials.gov Protocol Identifier: NCT04523714`; study title `Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches (RESOLVE Study)`. Exact version text: `Version Number: 6.0`; `Version Date: 18 July 2024`; `Based on Study Protocol Version 5.0; 10 November 2022`. Visually confirmed. Title lists Lynn L. DeBar, PhD, MPH at KP CHR and Andrea J. Cook, PhD at KPWHRI; institution/version metadata are administrative.
- SAP-N002, pp2–4: change history is part of this bound PLAN, not separate results. 08/06/20: first approved version March30,2020 relabeled to1.0 and revised SAP2.0; phaseIII description; randomization notification wording; aims distinguish secondary/exploratory; interventions online vs virtual coach; modified BPI-SF11 items and4 intensity items; age and race/ethnicity subgroup analyses added; perceived support measure finalized; mediators assessed baseline or notification and3months; eligibility updated; sex stratification uses EHR rather than self-report; SAE relatedness recoded related/possibly related/not related. 09/18/20: rural/medically underserved stratum and adjusted variable added; MCID for intensity/interference subscales added; coach clustering handling added. 09/25/20: KPWA OUD ICD-10 exclusion added.
- SAP-N003, p3: 10/19/20 Essentia geography description changed to Wisconsin; routine physician chart review of hospitalizations removed; ad-hoc SAE identification/review aligned with DSMP. 07/01/21: KP sites require at least2 pain-related encounters at least60days apart (Essentia at least1); surgery past60days exclusion added; planned/scheduled next-year surgery exclusion added. 03/29/22: painTRAINER described consistently as CBT-based online program; onboarding sensitivity analysis added. These historical records preserve their dates; no standalone inference is drawn.
- SAP-S001, p4, July17,2024: PGIC description changed from1item to `1 item each for pain status and overall status`; exploratory high-impact and graded chronic pain added to SAP description to reflect protocol/aims. The history explicitly says actual assessed outcomes did not change.
- SAP-S002, p4, July17,2024: `Added inverse probability of missing weights (IPW) to address missing data for those missing all time points.` Earlier pattern-mixture approach imputed only among those with at least1 follow-up. IPW aims for interpretation among all randomized. Rationale reports `12.1%` missing all outcomes at all time points; proposal by masked statistician without access to outcomes or summaries by arm. Masking clarification added for assignment and outcome data.
- SAP-S003, p10: SAP finalization/approval before unblinding; SAP modifications take precedence over protocol analytical plans, while modifications to primary endpoint or its analysis also reflected in protocol amendment; updates documented at beginning.

## Trial, outcomes and measurement definitions

- SAP-N004 / SAP-S004, pp8–9: phaseIII randomized comparative effectiveness,3 parallel arms,2 active interventions vs usual care. Individual patients from4 integrated systems KPGA, KPNW, KPWA, Essentia. Planned randomized2,331,777/arm. Baseline before randomization; notification approximately1–2weeks after randomization; follow-up3,6,12months; enrollment12months. Both active interventions8 sessions expected weekly. Online CBT-based painTRAINER vs live coach-led CBT-CP by phone/video; UC receives bound2020 ACPA resource guide; concomitant pharmacologic/nonpharmacologic care unrestricted. Semantic join: intervention/arm; randomizedN; timepoint.
- SAP-S005, pp8–9: Aim1 clinically meaningful ≥30% improvement in pain severity (intensity+interference), each active vs UC at3months. Aim1a secondary pain/QOL (social role, physical function, PGIC); exploratory opioid use, depression, anxiety, sleep, high-impact/graded pain. Aim1b subgroup effects; Aim1c mediators; Aim2 incremental cost-effectiveness active arms each other and UC. Aim3 qualitative evaluation explicitly outside SAP statistical analysis scope.

| Local relationship | Exact source location | Planned status and measure | Timepoint/semantic join key |
|---|---|---|---|
| SAP-N005; SAP-S006 | p11 section3.1 | Sole primary: binary MCID in pain severity; `30% decrease in score on modified 11-item version` BPI-SF from baseline, intensity4+interference7 items | baseline to3months; primary pain-severity responder |
| SAP-N006; SAP-S007 | p11 section3.2 | Secondary binary MCID in severity, same definition | baseline to6,12months; later primary-outcome timepoints |
| SAP-N007; SAP-S008 | p11 section3.2 | Secondary binary intensity MCID,30% decrease,4-item BPI-SF intensity subscale | timeframe column primary baseline-to3, secondary6/12; measured-by cell literally baseline,6,12 |
| SAP-N008; SAP-S009 | p11 section3.2 | Secondary binary interference MCID,30% decrease,7-item BPI-SF interference subscale; definition cell literally begins `difference (MCID) in pain intensity` | timeframe column primary baseline-to3, secondary6/12; measured-by cell literally baseline,6,12 |
| SAP-N009; SAP-S010 | p11 section3.2 | Secondary continuous severity, BPI-SF11item composite; intensity4 items; interference7items | baseline,3,6,12; primary3 secondary6/12. Intensity timeframe cell is visually empty; other rows explicitly show3/6/12 |
| SAP-N010; SAP-S011 | p12 section3.2 | Secondary social role PROMIS Ability to Participate Social Roles4A,4items continuous; physical PROMIS Physical Functioning Short Form6b,6items continuous | baseline,3,6,12; primary3 secondary6/12 |
| SAP-N011; SAP-S012 | p12 section3.2 | Secondary PGIC Guy/Farrar,1item each pain status and overall status | collected3,6,12; primary baseline-to3 secondary6/12 |
| SAP-N012; SAP-S013 | p12 section3.3 | Exploratory/tertiary long-term opioid use binary; opioid orders/fills continuous ≥60day supply during prior90days, incorporating earlier prescriptions carried into window | baseline day−90 to−1;3mo day1–90;6mo91–180;9mo181–270;12mo271–360; baseline survey day1; quarterlyEHR |
| SAP-N013; SAP-S014 | p12 section3.3 | Exploratory depression PHQ-8,8items continuous; anxiety GAD-7,7items continuous; sleep PROMIS Sleep Disturbance6a,6items continuous | baseline to3,6,12 |
| SAP-N014; SAP-S015 | p13 section3.3 | Exploratory high-impact chronic pain and Graded Chronic Pain Scale–Revised; self-report intensity,duration,disability | baseline to3,6,12 |
| SAP-N015; SAP-S016 | p13 section3.4 | Economic cost and incremental cost per additional severity MCID30% responder at12months; QALY utilities EQ-5D-5L; EHR utilization standard algorithms/Medicare fee schedules; process intervention resources | costs baseline–12mo; EQ-5D baseline,3,6,12 |

No literal `key secondary` designation was identified in the assigned SAP. Secondary and exploratory statuses above are retained exactly; no status is inferred from a main paper.

## Moderators, mediators, sample and randomization

- SAP-N016 / SAP-S017, pp14–15,20: moderators for primary outcome: self-reported sex at birth male vs female/other; age<65 vs≥65 EHR; self-reported white/non-Hispanic, Black or African American/non-Hispanic, Hispanic, Other; urban vs rural/medically underserved. Rural RUCA4,5,6,7,8,9,10 using2010census tract; underserved HRSA primary-care/mental-health geographic/high-needs shortage areas. Multiple nonmalignant pain:1cluster vs>1cluster; EHR diagnoses in previous360days, >1pain-related diagnosis across>1cluster. Printed cluster listing labels1,3,4,5,6,7,8,9 and names back, neck,limb/extremity/joint/arthritic,fibromyalgia,headache,orofacial/ear/TMJ,musculoskeletal chest,general/other pain. Mood disorder depression and/or anxiety ICD-10 in prior360days. Negative SDOH ≥1 need financial1item, food2, transportation2,housing3; baseline self-report.
- SAP-N017 / SAP-S018, p15: mediators continuous catastrophizing PCS-SF6 items baseline/3months; pain self-efficacy Chronic Pain Self-Efficacy pain-management5item subscale baseline/3months; perceived support2items notification/3months. Section16 p22 describes mediator changes baseline-to3; preserve both source timing descriptions.
- SAP-N018 / SAP-S019, p16: primary sample size independent-proportion comparison two-sided,90% power, Fisher LSD3-way comparison; omnibus Wald at0.05 before pairwise. UC15% responder, active22.5%; absolute difference7.5percentage points; displayed relative change150%. Required1,863=621/arm; retention80%; randomize2,331=777/arm. Semantic join: sample/power; omnibus/alpha; responder proportion.

| SAP-N019 / SAP-S020 subgroup power p16 | UC rate | Intervention rate | Detectable difference | Printed relative change | Power |
|---|---:|---:|---:|---:|---:|
|372 (20% of1,863)|15.0%|31.0%|16.0%|206.7%|80%|
|558 (30%)|15.0%|27.7%|12.7%|184.7%|80%|
|744 (40%)|15.0%|25.8%|10.8%|172.0%|80%|

p16: same two-sided independent-proportions Fisher LSD assumptions. Sex and mental-health subgroups expected≥40%; aim≥20% rural/underserved; negative SDOH exploratory subgroup due unknown prevalence.

- SAP-N020, pp17–18, section6.1: EHR enrolled at query and previous360days; age≥18; English/no interpreter; Essentia≥1 encounter or KP≥2 encounters >60days apart, within360days; no musculoskeletal surgery past60days; no≥2 malignant cancer encounters (except nonmelanoma skin) past60days; no hospice/palliative past360days; no severe cognitive impairment; KPWA-only OUD exclusion. Screening high-impact pain most/every day in past3months plus limits life/work most/every day past3months; PEG≥12 (visually confirmed); internet/phone access. Exclude CBT/pain psychoeducation in previous6months, current or next-month CBT, current/next-month intensive SUD services, planned pain-condition surgery next12months.
- SAP-S021, p18 section6.2: `each eligible subject is analyzed according to the treatment group to which they were assigned at the time of randomization.` `Modified intent-to-treat will not be employed in this protocol.` p21: all randomized regardless engagement/exposure. Safety primary all randomized; secondary excludes intervention participants deemed ineligible postrandomization. Per-protocol/as-treated sample may be constructed if UC CBT crossover>10%; treatment as received.
- SAP-N021, p18 section7: adherence≥6 of8 sessions in either active arm.
- SAP-N022 / SAP-S022, p18 section8: individual equal ratio1:1:1 after baseline; strata sex EHR male vs female/other; baselineBPI<7 vs≥7;4sites; rural/underserved EHR geocode. Variable permuted blocks3,6,9 per stratum.
- SAP-S023, p19 section9:2masking levels assignment and outcome-data access. Participants unmasked assignment; administrative/intervention staff unmasked assignment but masked outcome data; assessors masked assignment but access individual outcome data.

## Analysis models, missing data and decision rules

- SAP-S024, p19 section10: exact decision rule `first an omnibus Wald test ... at the 0.05 alpha level` and pairwise `two-sided alpha=0.05, only if the omnibus test is statistically significant.` Similar rule for secondary3-group comparisons; safety no multiplicity because not powered for safety. No noninferiority/equivalence margin is specified.
- SAP-S025, p19 section11: primary analyzes patients with follow-up; MAR given baseline covariates. Missing mechanisms tracked. Sensitivity as required if>15% missing3month follow-up or differential arm missingness. Pattern-mixture imputation relaxes MAR by conditioning on missingness patterns among those with≥1follow-up; IPW for missing all follow-up. Worst/best case sensitivity: every missing active-arm outcome assigned nonresponder at each missing timepoint; every missing UC outcome responder. SAP p4 adds IPW for all-randomized interpretation. Number of imputations, specific IPW prediction covariates, and combining formula are not stated in this assigned SAP text.
- SAP-S026, p19 section12: survey scales such as11point Likert no outlier correction; economic sensitivity winsorizes to99th percentile (source spelling `Windsorize`).
- SAP-S027, p20 section13: baseline and follow-up by arm descriptive means,medians,SD,min,max; categorical frequencies/percent/tabulations. Baseline predictors include age,sex,race,ethnicity,rural/underserved,multiple pain,mood,SDOH. Grouped subgroups dictated by size and balance.
- SAP-S028, pp20–21 section14: modified PoissonGEE for binary severity MCID30% at3(primary),6,12(secondary); Poisson family log link, robust standard errors; explicit relative risk as effect of interest, not logistic because response not rare. Independence working correlation; robust sandwich for within-person and within-health-coach correlation and Poisson-binary mean–variance structure. Arm×time effects; UC and3months references. Covariates baseline pain severity; other stratification variables sex,clinical site,rural/underserved; a priori multisite pain and co-occurring mental health condition. No sex-data-source qualifier in this model paragraph beyond the linked randomization specification.
- SAP-S029, p21 printed primary mean model, visually confirmed: `log(E(Y_ij)) = beta_0 + beta_1 Int1_i + beta_2 Int2_i + beta_3 T6_ij + beta_4 T12_ij + beta_5 Int1_i T6_ij + beta_6 Int2_i T6_ij + beta_7 Int1_i T12_ij + beta_8 Int2_i T12_ij + bold_beta_Z Z_i`. Participants i=1,...,n; time j=1,2,3; Int1/2binary randomized arm indicators; T6 j2,T12 j3; Z baseline covariates. Primary3month intervention coefficients; later effects include their interactions.
- SAP-S030, p21 sensitivity: motivational-interviewing onboarding language added painTRAINER8/9/2021 after approximately140patients; repeat primary analysis among randomized after8/9/2021 to examine enhanced engagement.
- SAP-S031, p21 section15: secondary3month primary timepoint and6/12secondary. Continuous linear regression; binary/countPoisson; GEEindependence, sandwich within-person/coach and variance; arm×time. Covariates `baseline levels of pain severity and all stratification variables.` Outcome list severity continuous,intensityMCID/continuous,interferenceMCID/continuous,social role,physicalfunction,PGIC.
- SAP-S032, pp21–22 section16 Aim1b: expected livecoach benefit over painTRAINER among mood/anxiety,multisite,rural/underserved,unmetneeds. Separate moderator analyses each of sex,age,race/ethnicity,rural/underserved,multiplepain,mood,SDOH. Add moderator main effect and moderator×arm×follow-up; primary interaction terms3months. Qualitative pattern assessment across later timepoints.
- SAP-S033, pp22–23 Aim1c:3month mediator changes for6month outcomes; mediation conducted only interventions significant for outcome6months. Primary mediation severityMCID6months; secondary mediation other6month outcomes; separate each active vs UC. Step1 association `log(E(Y_i))=beta_0+beta_1 Int_i+bold_beta_Z Z_i`,6month binary MCID. Step2 linear `E(M_i)=beta_M0+beta_M1 Int_i+bold_beta_MZ Z_i`, change baseline–3months; retain mediators associated with either arm atP<0.10. Step3 multi-mediatorIPW estimates direct intervention effect; prose states logistic model of assignment given selected mediator changes adjusting baseline confounders. Printed step3a formula (visually confirmed): `logit(E(Int_i))=beta_W0+bold_beta_WM Msub_i` (no Z term printed). Let eta=estimated beta_W0+estimated bold_beta_WM Msub_i; exact printed weights algebra: forInt1, `{exp(eta)/(1+exp(eta))}^-1`; forInt0, `{1-exp(eta)/(1+exp(eta))}^-1`. Weighted Step1 mean model then compared with unweighted to quantify total and individual mediated contributions. These IPW mediator weights are distinct from missing-data IPW.
- SAP-S034, p23 section17: exploratory outcomes use section15 secondary-model approach.
- SAP-S035, pp23–24 section18: economic evaluation KPsites complete utilization; Essentia conditional on EHR comprehensiveness exploration. Health-plan perspective implementation+maintenance+delivery; total and pain-relatedmedical pharmacy,outpatient,inpatient,referrals. Incremental12month severityMCID30% responder andQALY(EQ-5D-5L). Net-benefit regression dependent variable `nb_i = lambda * effect_i - cost_i`; lambda WTP varied forCEAC; examples $30,000–$100,000/QALY. GEEwith appropriate links for healthcarecost comparisons; sensitivities cost transportability,replication,economiesofscale;99thpercentile winsorization perp19.
- SAP-N023, pp24–25 cost categories: prescription; ambulatory primarycare,PT/OT/physiatry,painclinic,mental/behavioral/addiction,ER/urgent,other specialty;inpatient. Pain meds by class(e.g.opioids); pain visits diagnosticICD-10-CM; PT includesOT/physiatry; other specialty excludes already listed/primarycare; pain hospitalization principal painICD-10-CM.
- SAP-S036, pp25–26 sections19.1–19.5: AE identification spontaneous participant report or intervention/study staff regular contact; no uniform solicitation; explicit unequal opportunities by arm, hence group AE comparison not meaningfully interpretable. AE frequency bysite reviewed quarterly and DSMBsemiannually. Safety outcomes death and inpatient hospitalization during activeparticipation; pre-enrollment plannedhospitalization excluded. All active EHR queried every6months; death physicianchartreview; hospitalization diagnoses/admission reason/lengthofstay extracted; no routine hospitalizationchartreview unless relatedness suggested and DSMB recommends. Selfreported death/hospitalization documented for semiannualreview, not atreporttime. Summarize events and persons bytype,arm,timefromrandomization,related/possiblyrelated/notrelated. No formal SAEtests; not powered for safety noninferiority. MedDRA pharmaceutical/biologic/devicecode grouping notapplicable. Twiceyearly DSMBmonitoring; expectation occasional deaths/hospitalizations withplannedN2,331 is explanatory, not an observed count.
- SAP-S037, p27 sections19.6–20: DCCnotifies DSMBchair; chair recommends temporarysuspension of enrollment/procedures/interventions and convenes adhocDSMB; detailed DSMP governs. Exact interim statement: `There are no planned interim analyses of primary or secondary outcome data before the study is completed.` DSMBmay request interim effectiveness estimates while evaluating safety. `No formal futility or effectiveness interim analyses will be conducted.` No printed numerical stoppingboundary.

## Complete physical-page coverage

Each row means the complete page text/image content was inspected and mapped; references and administrative pages have explicit no-applicable-result records. The single artifact covers every row. Numerical thresholds and mathematical glyphs shown above were visually resolved where OCR substituted characters. Fresh OCR text retains the unnormalized engine output, allowing later recheck against image/PDF. Footers and repeated version labels were inspected but do not create duplicated statistical relationships.

| PDF page | Source location | Contents inspected | Mapped relationships / no-applicable reason | Status |
|---|---|---|---|---|
|1|[p1](../../../joi250046supp2_prod_1755300121.15087.pdf#page=1)|Title, registry, investigators, version and protocol date|SAP-N001; administrative identity|COMPLETE|
|2|[p2](../../../joi250046supp2_prod_1755300121.15087.pdf#page=2)|Change history2020|SAP-N002|COMPLETE|
|3|[p3](../../../joi250046supp2_prod_1755300121.15087.pdf#page=3)|Change history2020–2024|SAP-N003|COMPLETE|
|4|[p4](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4)|July2024outcomes,IPW,masking amendments|SAP-S001,SAP-S002|COMPLETE|
|5|[p5](../../../joi250046supp2_prod_1755300121.15087.pdf#page=5)|Approval signatures|No applicable result; administrative signature page|COMPLETE|
|6|[p6](../../../joi250046supp2_prod_1755300121.15087.pdf#page=6)|Complete contents sections1–21|No applicable result; navigation only|COMPLETE|
|7|[p7](../../../joi250046supp2_prod_1755300121.15087.pdf#page=7)|Abbreviations ITT,MCID,GEE-related terminology,SDOH,LSMEANS,SAS|No additional quantified relationship; dictionary only|COMPLETE|
|8|[p8](../../../joi250046supp2_prod_1755300121.15087.pdf#page=8)|Trialdesign,visit schedule,aims|SAP-N004,SAP-S004,SAP-S005|COMPLETE|
|9|[p9](../../../joi250046supp2_prod_1755300121.15087.pdf#page=9)|Aim3scope,plannedN,interventions,duration|SAP-N004,SAP-S004,SAP-S005|COMPLETE|
|10|[p10](../../../joi250046supp2_prod_1755300121.15087.pdf#page=10)|Introduction,EDA,blinding,approval/amendment precedence|SAP-S003,SAP-S027|COMPLETE|
|11|[p11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=11)|Primary andsecondary outcome tables,allcells|SAP-N005–SAP-N009;SAP-S006–SAP-S010|COMPLETE|
|12|[p12](../../../joi250046supp2_prod_1755300121.15087.pdf#page=12)|SecondaryQOL/PGIC andexploratorytable,allcells|SAP-N010–SAP-N013;SAP-S011–SAP-S014|COMPLETE|
|13|[p13](../../../joi250046supp2_prod_1755300121.15087.pdf#page=13)|Exploratorypain andeconomictables|SAP-N014,SAP-N015;SAP-S015,SAP-S016|COMPLETE|
|14|[p14](../../../joi250046supp2_prod_1755300121.15087.pdf#page=14)|Moderator definitions,cutoffs,data sources|SAP-N016,SAP-S017|COMPLETE|
|15|[p15](../../../joi250046supp2_prod_1755300121.15087.pdf#page=15)|SDOH andmediators table|SAP-N016,SAP-N017;SAP-S017,SAP-S018|COMPLETE|
|16|[p16](../../../joi250046supp2_prod_1755300121.15087.pdf#page=16)|Primary andsubgroup sample/power,narrative+alltablecells|SAP-N018,SAP-N019;SAP-S019,SAP-S020|COMPLETE|
|17|[p17](../../../joi250046supp2_prod_1755300121.15087.pdf#page=17)|AllEHR andscreeningeligibility criteria|SAP-N020|COMPLETE|
|18|[p18](../../../joi250046supp2_prod_1755300121.15087.pdf#page=18)|Remaining exclusions,ITT,safety,as-treated,adherence,strata/blocks|SAP-N020,SAP-N021,SAP-N022;SAP-S021,SAP-S022|COMPLETE|
|19|[p19](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19)|Masking,multiplicity,missingness,outliers|SAP-S023,SAP-S024,SAP-S025,SAP-S026|COMPLETE|
|20|[p20](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20)|Baseline summaries,primary/laterhypotheses,primaryGEE|SAP-S027,SAP-S028|COMPLETE|
|21|[p21](../../../joi250046supp2_prod_1755300121.15087.pdf#page=21)|Primaryformula,onboardingsensitivity,ITT,secondarymodels,moderatorhypothesis|SAP-S029,SAP-S030,SAP-S031,SAP-S032|COMPLETE|
|22|[p22](../../../joi250046supp2_prod_1755300121.15087.pdf#page=22)|Moderatorinteraction andmediationsteps1–2|SAP-S032,SAP-S033|COMPLETE|
|23|[p23](../../../joi250046supp2_prod_1755300121.15087.pdf#page=23)|Mediatorstep2/3formulas,IPW,tertiaryapproach,economicscope|SAP-S033,SAP-S034,SAP-S035|COMPLETE|
|24|[p24](../../../joi250046supp2_prod_1755300121.15087.pdf#page=24)|Cost/netbenefit/CEAC,GEE,costcategoriestable|SAP-S035,SAP-N023|COMPLETE|
|25|[p25](../../../joi250046supp2_prod_1755300121.15087.pdf#page=25)|Costfootnotes,AE/SAE ascertainment anddefinitions|SAP-N023,SAP-S036|COMPLETE|
|26|[p26](../../../joi250046supp2_prod_1755300121.15087.pdf#page=26)|AllSAEmonitoring/descriptives/no-tests|SAP-S036|COMPLETE|
|27|[p27](../../../joi250046supp2_prod_1755300121.15087.pdf#page=27)|Safety suspension andinterimrules|SAP-S037|COMPLETE|
|28|[p28](../../../joi250046supp2_prod_1755300121.15087.pdf#page=28)|References1–18|No applicable new planned result/relationship; citations only,notopened|COMPLETE|
|29|[p29](../../../joi250046supp2_prod_1755300121.15087.pdf#page=29)|References19–31|No applicable new planned result/relationship; citations only,notopened|COMPLETE|

## Handoff and limitations

29/29 assigned PDFpages freshly mapped; 23 localnumeric definition groups and37 localstatistical relationship groups; 5pages contain no independent result-relevant quantitative relationship (5,6,7,28,29). No scientific coverage gap. Every outcome table,model,multiplicity/missing-data/interim rule,moderator/mediator,sensitivity,intervention andamendment unit was retained. Rendering/OCR derivatives total29images and29pageOCRtexts; sourcePDF andalloldassets unchanged. OCR glyph substitutions in inequalities andformula notation were resolved onsourceimages rather than silently accepted; rawtext remainsunaltered. A specific unreported method input is recorded as absent within thisdocument,without inferring details fromexternal references. Semantic joinkeys permit matching against reportmaps only after outcome,time,population,contrast andmodel are aligned. The artifact makes no diagnostic or inclusion decisions.
