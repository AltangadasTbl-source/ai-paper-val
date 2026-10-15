# Cross-source consistency review

Scope: all supplied REPORT content in DOC-001 (14 PDF pages), DOC-004 (7 PDF pages), DOC-005 (19 PDF pages), and DOC-006 (worksheet eTable 3, A1:J115), matched against PLAN content in DOC-002 (77 PDF pages) and DOC-003 (29 PDF pages), and qualifying within-report and within-plan relationships. All 147 source units have current fresh maps. This checker used those current maps, supplied sources, source-derived text and source-page images; no earlier scientific conclusions or external sources were used. The complete scope and review contract were read before comparison. No candidate IDs or adjudications are assigned here.

The comparison matched outcome, population, baseline/time point, contrast, model, effect measure, analysis set and precision. Primary binary response is a ≥30% baseline reduction in the modified 11-item BPI-SF at 3 months; later severity responses and the pain/functioning outcomes named in the abstract were retained as key secondary results. Crude/unadjusted, adjusted, complete-case, weighted-imputed, worst/best-case and date-restricted estimates were matched separately. Every listed finding was checked against its exact supplied source page or workbook XML. Findings: 8. Excluded observations: 11.

## Completed comparison coverage

| Comparison scope | Completed comparison |
|---|---|
| Abstract, Key Points, narrative, main Tables 2–3 and Figure 2 | All three primary adjusted percentages and RR contrasts agree with their matching body/table copies; Figure 2 uses the same primary/later severity outcome and direction. Narrative continuous-severity SMD copies were compared by exact time and contrast. Every binary and continuous key-secondary row, direction and omnibus-versus-pairwise qualifier was considered. General narrative pattern statements were distinguished from an explicit test of each individual contrast. |
| Main results versus DOC-005 | All nine severity RR contrasts at 3/6/12 months in eTable 4 match main Table 2, including precision differences. eTables 7–8 are different missing-data or population analyses; eTable 9 is unadjusted; eTables 10–11 are unadjusted continuous results. Their estimates were not treated as copies of the weighted adjusted main analysis. Scoring ranges, scale direction, ≥30% response definitions, source populations and analysis labels were compared. |
| Participant flow, treatment, safety and workbook | Randomized eligibility and analysis sets, any-follow-up versus time-specific follow-up, session thresholds, intervention dose/duration, safety event versus participant counts, and missingness-pattern group definitions were matched. DOC-006 B3:E3 and source eTable 1 represent the same randomized/missingness-pattern population definitions, with a small contributor-count difference screened below. All workbook labels, prespecified flags and H/I/J test purposes were considered; baseline copies are peripheral. |
| Plan endpoint/status/component lists | Primary severity MCID, severity at 6/12 months, intensity and interference MCID, continuous severity/intensity/interference, social and physical functioning, both PGIC items, exploratory opioid/depression/anxiety/sleep/high-impact/graded pain, economic and safety outcomes were compared individually. The amended 11-item composite, four intensity items, seven interference items, two PGIC items and outcome hierarchy reconcile. No supplied report changes a prespecified outcome status. Ancillary moderator/mediator/economic/exploratory outputs absent from this primary trial report were not recast as absent primary/key-secondary outcomes. |
| Plan eligibility lists, item by item | Active health-system enrollment/care in prior year; age ≥18; English/no interpreter; Essentia ≥1 versus KP ≥2 pain encounters >60 days apart in 360 days; surgery in prior 60 days; malignancy threshold; hospice/palliative care in prior 360 days; severe cognitive impairment; KPWA opioid-use-disorder exclusion; high-impact pain frequency and interference in prior 3 months; PEG ≥12; phone/internet access; prior-six-month/current/next-month behavioral pain treatment; current/next-month intensive substance-use services; next-12-month pain surgery were each matched. The malignancy threshold is finding F-XS-001; absent operational details alone are screened below. |
| Primary model and analysis population | Individual equal allocation, four strata, variable blocks 3/6/9; modified Poisson log-link GEE; working independence; robust person/coach clustering; arm-by-time interactions; UC/3-month references; six named baseline adjustment factors; eligible-randomized ITT regardless of engagement; retained pre-withdrawal data; imputation among any-follow-up participants and nonresponse weighting were compared. Covariate and primary-versus-sensitivity specifications are findings below. Exclusion of two UC participants who did not meet EHR eligibility agrees with the SAP eligible-subject effectiveness set. |
| Secondary, sensitivity, subgroup and plan-internal statistical design | Secondary linear versus Poisson GEE, baseline adjustment, seven moderator definitions and three-way interactions, 3-month moderator comparison, 6-month mediator endpoint, mediator measurement times/selection P<.10, conditional crossover >10%, enhanced-onboarding restriction after 8/9/2021, missingness >15% or group differential, extreme active=0/UC=1 sensitivity, mean covariate imputation, and disclosed SAP amendments were compared individually. Plan-internal ancillary details not affecting a reported primary/key-secondary analysis are screened below. |
| Hypothesis, power and decisions | Superiority direction, 3-month primary endpoint, 90% power, UC15% versus active22.5%, 7.5 percentage-point difference/RR1.5, 1863 analyzed/621 per arm, 80% retention, 2331 randomized/777 per arm, subgroup80% assumptions, two-sided .05, omnibus Fisher LSD gate, no formal efficacy/futility interim, safety suspension logic and no SAE between-group tests were checked against report statements. No noninferiority/equivalence margin, prior, alpha-spending boundary or reported efficacy stopping decision applies. The report adds a simulation implementation without contradicting these printed assumptions. |

## Findings

### F-XS-001

**Observation:** The malignant-cancer eligibility criterion uses a different encounter threshold in the report and plans.

**Exact locations and document roles:** REPORT [main article p.2, Methods, clinical eligibility criterion 5](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=2); PLAN [protocol p.32, section 5.1, EHR criterion 6](../../../joi250046supp1_prod_1755300121.14087.pdf#page=32); PLAN [SAP p.17, section 6.1, EHR criterion 6](../../../joi250046supp2_prod_1755300121.15087.pdf#page=17).

**Printed statements:** The report requires no malignant-cancer diagnosis other than nonmelanoma skin cancer within 60 days. Both plans require that the participant does not have two or more separate encounters carrying such a diagnosis within 60 days.

**Comparison logic and reproduction:** These statements differ for a person with one qualifying cancer-coded encounter. The plans do not exclude that person by criterion 6; the report's literal criterion excludes any diagnosis in that window. The same 60-day window and cancer exception were matched. This is a criterion comparison, not a rounded count; recomputed interval and relative discrepancy are not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** Eligibility/target population for the 2331-participant primary pain-severity response analysis.

**Why context does not resolve it:** The report does not identify whether its diagnosis language summarizes a two-encounter confirmation algorithm or represents a more restrictive rule. This quantitative criterion can change which population the primary effects represent.

**Supported alternatives:** The two-encounter EHR rule may operationalize a confirmed diagnosis and the report may summarize that rule; alternatively, the implemented malignancy exclusion may have differed from the supplied plans. No number of affected participants is supplied.

**Human question:** Was malignant-cancer exclusion implemented for any diagnosis or for at least two separate coded encounters within 60 days, and which rule defines the reported effectiveness population?

### F-XS-002

**Observation:** Expected session lengths differ between the protocol and the reported intervention descriptions.

**Exact locations and document roles:** PLAN [protocol p.43, section 10.1.1 painTRAINER overview](../../../joi250046supp1_prod_1755300121.14087.pdf#page=43); PLAN [protocol p.44, section 10.1.2 coach overview](../../../joi250046supp1_prod_1755300121.14087.pdf#page=44); REPORT [main article p.3, Health Coach Program and Online Program](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=3); REPORT [TIDieR p.3, Procedures row](../../../joi250046supp3_prod_1755300121.15087.pdf#page=3); REPORT [TIDieR p.4, When and How Much row](../../../joi250046supp3_prod_1755300121.15087.pdf#page=4).

**Printed values:** Protocol painTRAINER sessions take 45–60 minutes and coach sessions take 60 minutes. Main and TIDieR reports give painTRAINER 30–45 minutes and coach 45–60 minutes. All locations describe eight sessions, approximately weekly, with a 12-week intended completion period.

**Comparison logic and reproduction:** For painTRAINER, the corresponding stated lower and upper durations each differ by 15 minutes. Half-minute precision intervals are [44.5,45.5] versus [29.5,30.5] for the lower endpoint and [59.5,60.5] versus [44.5,45.5] for the upper endpoint. The gaps are 14 minutes, or 14/45=0.311 and 14/60=0.233 relative to the protocol endpoints, both above .05. Coach 60-minute expectation lies at the reported range's upper endpoint and is corroborating context, not a separately reproduced numeric-copy discrepancy. This single finding concerns the changed session-duration description, primarily the painTRAINER range.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The duration/dose of the online intervention associated with the primary RR1.28 versus UC and HC-versus-PT RR1.20.

**Why context does not resolve it:** The supplied report does not explain whether the shorter online durations reflect a program revision, delivered duration, or a revised expectation. The range changes the intervention dose extracted for replication or synthesis.

**Supported alternatives:** The protocol may provide a conservative completion estimate whereas the reports describe experience during the trial; a revised duration estimate or session-content change is another possibility. The source confirms self-pacing and pause/resume features but does not select between these readings.

**Human question:** Does 30–45 versus 45–60 minutes describe a revised online session dose, actual completion time, or different duration conventions, and which planned and delivered duration should be extracted?

### F-XS-003

**Observation:** Age is described as a prespecified base adjustment factor in report material, although the supplied primary analysis specifications do not include it in that set.

**Exact locations and document roles:** PLAN [protocol p.56, section 15.5 adjustment list](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56); PLAN [SAP p.20, section 14 adjustment list](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20); REPORT [main article p.4, Statistical Analysis adjustment sentence](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT [results supplement p.4, Adjustment, base-set sentence](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); REPORT [results supplement p.7, eTable 2 variables included in all models](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); REPORT [p.8 eTable 3 age coefficient](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); REPORT [p.9 eTable 4 age coefficient](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); REPORT [p.10 eTable 5 age coefficient](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); REPORT [supplied workbook, worksheet eTable 3, G2 and A10/G10](../../../joi250046supp5_prod_1755300121.16087.xlsx).

**Printed statements and values:** Both plans and main p.4 name baseline severity, sex, site, residence, multisite pain and mental-health condition for the primary model. Supplement p.4 first repeats that list, then calls the base set prespecified and inserts age. eTable 2 includes age≥65 versus <65 in all models. Age coefficients are 0.19 (0.12–0.27) in imputation, RR1.15 (1–1.33) in primary estimation, and OR0.97 (0.70–1.35) in weighting. Workbook G2 is “Pre-specified Adjustment Variables”; G10 flags age with X.

**Comparison logic and reproduction:** The six named plan factors were compared item by item; age is an additional seventh baseline factor in the reported base set and fitted models. SAP section 13 mentions age among potential baseline variables, but neither the section 14 primary specification nor the documented amendments states that it is a fixed primary adjustment factor. No numeric-copy arithmetic is required; recomputed interval and relative discrepancy are not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R, S_C, S_W.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified versus added covariate specification for the primary severity MCID adjusted RRs1.28,1.54,1.20 and their intervals.

**Why context does not resolve it:** Category 5 applies to an analysis element described as prespecified that is not contained in the supplied primary specification. A generic potential-variable list does not identify the final fixed base model or the timing of age's addition.

**Supported alternatives:** An additional supplied-plan section or amendment may have been intended to authorize age; it may have been selected after baseline/missingness examination; or the report's prespecified wording may refer only to the six original factors. The fitted tables establish age's use, but not its prespecification.

**Human question:** Which prospective specification made age a fixed primary adjustment covariate, and was age included in the model producing the main primary results as a prespecified or subsequently added factor?

### F-XS-004

**Observation:** The secondary outcome adjustment set is expanded in the report relative to the explicit plan lists.

**Exact locations and document roles:** PLAN [protocol p.57, section 15.6 final analysis sentence](../../../joi250046supp1_prod_1755300121.14087.pdf#page=57); PLAN [SAP p.21, section 15 secondary analysis paragraph](../../../joi250046supp2_prod_1755300121.15087.pdf#page=21); REPORT [main article p.4, secondary modeling paragraph](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT [main Table 3 pp.10–11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10).

**Printed statements:** Both plans explicitly state baseline pain severity and all stratification variables as secondary-analysis covariates. The report says the same modeling structures as the primary analysis were applied, with added adjustment for the given baseline secondary outcome. The primary structure in the preceding paragraph additionally includes multisite pain and mental-health condition.

**Comparison logic and reproduction:** Baseline severity, sex, site and residence match. The report additionally specifies outcome-specific baseline adjustment and imports the primary structure's multisite-pain and mental-health factors. The plan's general “same proposed approach” phrase and its explicit final covariate list are retained separately; neither explicitly names the given baseline secondary outcome. This is an analysis specification comparison; recomputed interval and relative discrepancy are not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** Adjusted intensity, interference, social-role, physical-functioning and global-impression secondary estimates and mean differences in Tables 2–3.

**Why context does not resolve it:** The specific covariate lists differ and the report does not identify an amendment or distinguish which baseline terms apply to each outcome. This determines the adjusted estimand extracted for the abstract's secondary pain/functioning results.

**Supported alternatives:** “Same proposed approach” may have been intended to inherit the entire primary covariate set, while the final plan sentence gives only minimum covariates; outcome-specific baseline adjustment may have been an additional specification. A later amendment may explain the expansion.

**Human question:** What exact covariate set was planned and used for each secondary outcome, including its baseline value, multisite pain and mental-health condition, and where is any expansion documented?

### F-XS-005

**Observation:** The role of the follow-up/MAR and weighted pattern-mixture analyses differs between the SAP primary-analysis paragraph and the report.

**Exact locations and document roles:** PLAN [SAP p.19, section 11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19); PLAN [SAP p.4, July 17, 2024 IPW amendment](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4); REPORT [main article p.4, missing-data paragraph](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT [results supplement p.4, Missing Data opening paragraph](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); REPORT [p.9 eTable 4 primary estimation model](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); REPORT [p.11 eTable 7 sensitivity introduction and complete-case block](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).

**Printed statements and values:** SAP section 11 says the primary analyses analyze patients with follow-up and assume MAR given baseline covariates, then describes sensitivity analyses when >15% missing at 3 months or group differential, including pattern-mixture/IPW and worst/best case. Its amendment says the current approach already imputes by pattern mixture and adds IPW to permit interpretation among all randomized. The report says the threshold caused the primary analysis to use MNAR imputation, nonresponse weighting and adjustment. The report's complete-case analysis is labeled sensitivity: 3-month PT/UC RR1.34 (1.12–1.61), HC/UC1.48 (1.24–1.75), HC/PT1.10 (0.94–1.29). Its primary weighted-imputed RRs are1.28,1.54,1.20.

**Comparison logic and reproduction:** These are explicitly distinct analyses and are not numeric copies. The observable difference is the assigned primary-versus-sensitivity role and associated MAR versus MNAR assumption. The >15% or differential rule is present in both sources; SAP section 11 does not explicitly state that meeting it replaces the primary MAR analysis. Recomputed numeric interval and relative discrepancy are not applicable to this specification comparison.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R, P_P.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Which three-month severity analysis is designated primary and which missing-data assumption accompanies RRs1.28,1.54,1.20.

**Why context does not resolve it:** Category 5 applies to replacement of a planned primary analysis. The amendment corroborates that weighted pattern-mixture estimation was intended, but section 11 retains the contrasting primary MAR statement and sensitivity wording; the supplied plan does not explicitly reconcile their roles.

**Supported alternatives:** The July 2024 amendment may authorize weighted MNAR as primary and section 11 may retain an earlier description; the threshold branch may have been intended to switch the primary analysis; or the report may use “primary” for an analysis that was prospectively sensitivity. The complete-case result is reported, so this finding does not assert its numerical absence.

**Human question:** Under the final approved SAP, was the primary analysis the follow-up/MAR model or the weighted MNAR pattern-mixture model, and what statement or amendment assigned the final primary-versus-sensitivity roles?

### F-XS-006

**Observation:** Education is described as binary in the final selected-variable list but represented by multiple distinct parameters in the fitted primary models.

**Exact locations and document roles:** REPORT [results supplement p.7, eTable 2 final imputation/estimation variable list](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); REPORT [p.8 eTable 3 education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); REPORT [p.9 eTable 4 education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); REPORT [workbook worksheet eTable 3, A12:A16](../../../joi250046supp5_prod_1755300121.16087.xlsx).

**Printed values:** eTable 2 selects education “any college vs. HS degree or less.” The imputation table has two separate AA-degree rows with estimates −0.02 (−0.11–0.08) and0.16 (0.07–0.25), and a graduate-degree row0.39 (0.29–0.49), each relative to high school or less. The estimation table similarly has education RRs0.97 (0.82–1.16),1.16 (1–1.33),1.35 (1.13–1.61). Workbook categories distinguish high school or less, associate/technical, college, doctoral/postgraduate.

**Comparison logic and reproduction:** A single binary college indicator has one coefficient relative to HS or less; three separate level coefficients describe a different design matrix. The issue is not merely the repeated AA name; the number and grouping of coefficients disagree with the binary final list. No arithmetic on rounded estimates is needed; recomputed interval and relative discrepancy are not applicable.

**Focus area:** C. **Proposed review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** Education coding in the imputation and primary estimation models producing adjusted severity MCID results.

**Why context does not resolve it:** The reader cannot identify whether the fitted primary models used a pooled college indicator or three education levels. The workbook establishes available categories but does not identify the final model matrix.

**Supported alternatives:** The selected-variable summary may describe an initial screen rather than final coding; the fitted models may use four-category education; or some displayed parameter labels may not describe the final fit. No replacement coefficient is inferred.

**Human question:** Was education binary or represented by three nonreference levels in each final imputation and estimation model, and what educational level does each printed coefficient represent?

### F-XS-007

**Observation:** The listed selected predictors for nonresponse weights differ from those displayed in the fitted weight model.

**Exact locations and document roles:** REPORT [results supplement p.7, eTable 2 final nonresponse variable list](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); REPORT [p.10, eTable 5 full coefficient display](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); REPORT [p.5, Non-Response Weighting specification](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5); REPORT [workbook worksheet eTable 3, A18 and H18:J18](../../../joi250046supp5_prod_1755300121.16087.xlsx).

**Printed values:** eTable 2 lists additional weighting predictors PEG, PHQ-8, GAD-7, any negative social determinant and education (any college versus HS or less). eTable 5 displays PEG, PHQ-8, GAD-7, negative SDOH and “Not employed” OR1.49 (1.11–2.00), P=.008, but no education term. Employment is listed for imputation/estimation, not weighting, in eTable 2. The workbook gives employment selection tests H18<.001, I18=.0228 and J18=.0591; these are separate outcome/nonresponse/3-month-missingness tests.

**Comparison logic and reproduction:** The base factors match. Four of the five additional weighting factors match; the final list specifies education where the coefficient display has employment. The source excludes health-care-site identification, not education coefficients. This is a model-membership comparison; recomputed interval and relative discrepancy are not applicable.

**Focus area:** C. **Proposed review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The response-weight model used for primary population-average adjusted severity RRs and percentages.

**Why context does not resolve it:** Neither the full fitted table nor the final list explains whether education, employment, or both contributed to the weights. The selection tests support possible employment inclusion but do not resolve education's absence from the displayed final fit.

**Supported alternatives:** The final list may retain an earlier selected model; the coefficient table may omit education; the weights may have used employment instead. The supplied materials do not identify the implemented predictor vector.

**Human question:** Did the final nonresponse model include education, employment, or both, and which specification generated the weights used for the primary results?

### F-XS-008

**Observation:** The raw-score summary label in eTable 11 conflicts with the narrative's mean description and with the possible medians of the reported PGIC scale.

**Exact locations and document roles:** REPORT [results supplement p.15, Additional Unadjusted Data and Analyses introduction](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15); REPORT [p.17, eTable 11 title and raw-score header, every outcome block at 3/6/12 months](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17); REPORT [main p.11, Table 3 PGIC scale footnotes h–i](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11).

**Printed values and labels:** The introduction says eTable 11 provides unadjusted mean secondary outcomes. The title says median/interquartile ranges, and the group header says “Raw Score Median (25%-tile,75%tile).” All 21 rows are affected by this summary label: severity, intensity, interference, social-role functioning, physical functioning, PGIC pain and PGIC general, each at3/6/12 months. PGIC is one item with integer response categories1–7. Printed PT PGIC-pain summaries are2.9 (2.8,2.9),2.8 (2.7,2.9),2.8 (2.7,2.9); PT general summaries are2.7 (2.6,2.7),2.5 (2.4,2.6),2.6 (2.4,2.7). HC3-month PGIC entries instead have2.0 (1.0,3.0) and2.0 (1.0,2.0).

**Comparison logic and reproduction:** A conventional sample median of a one-item integer score is integer or half-integer. The half-unit rounding intervals for2.9,2.8,2.7 and2.6 are respectively [2.85,2.95], [2.75,2.85], [2.65,2.75] and [2.55,2.65], each containing no possible such median. This is a quantity/summary-type comparison; a relative numeric-copy discrepancy is not applicable. No arithmetic comparison of medians with mean differences is asserted.

**Focus area:** C. **Proposed review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** Whether the unadjusted secondary group summaries are means with confidence intervals, medians with quartiles, or mixed summary types, for extraction of all21 eTable11 rows.

**Why context does not resolve it:** The conflicting mean/median descriptions and the different PGIC interval shapes do not establish a single intended quantity. The label changes both the central statistic and meaning of the parentheses.

**Supported alternatives:** Most entries may be means with95% intervals while the HC3-month PGIC entries are medians/quartiles; all entries may have been intended as a different model-based summary; or a mixture of summaries may be intentional. No numerical relabeling or replacement is proposed.

**Human question:** What central statistic and interval type is reported for each group in eTable11, particularly the HC3-month PGIC cells, and which entries should be extracted as means versus medians?

## Excluded observations

Only apparent issues considered and not emitted appear here. Reconciled comparisons are recorded in the scope table above.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.7 Secondary Outcomes versus Table3 p.10 severity3-month SMDs | Narrative PT/UC−0.26 and HC/UC−0.36 versus table−0.25 and−0.34. Their rounding intervals overlap for PT; HC gap=.01/.34=.0294≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main pp.4/9 and Supplement4 eTables7–11 | Primary adjusted versus complete-case, date-restricted or unadjusted estimates differ. They are explicitly different models/populations and not matching result copies. | NOT_REPRODUCED |
| REPORT Supplement4 p.15/eTable9 title and footnote | Title says adjusted RR, but immediately accompanying introduction says no adjustment/weighting/imputation and footnote explicitly says without adjustment; counts and RRs support that reading. | CONTEXT_RESOLVES |
| REPORT Supplement4 p.16/eTable10 versus p.15 introduction | Introduction calls the changes means while the table explicitly labels medians/quartiles. The displayed change distributions and the separately labeled mean-difference columns make the descriptive median reading identifiable. | CONTEXT_RESOLVES |
| PLAN protocol pp.22–23 and SAP p.11, pain-interference row and measurement column | Description says intensity but names the seven-item interference subscale; baseline/6/12 measurement list omits3 months while neighboring time-frame column explicitly states baseline-to3-month primary time. Subscale and intended three-month timing are evident. | TERMINOLOGY_OR_WORDING |
| PLAN SAP p.21 and REPORT TIDieR p.5 versus REPORT results supplement pp.13–14 | Enhanced-onboarding change is associated with approximately140 versus454 enrolled, but every source uses8/9/2021; eTable8 explicitly defines pre/post randomized populations454/1877. The calendar-count discrepancy does not change the stated subset boundary or analysis size. | PERIPHERAL_COMPARISON |
| REPORT workbook eTable3 D3 versus REPORT Supplement4 p.7/eTable1 one/two follow-up counts | Workbook missing1-or2 count468 versus188+283=471. With printed count intervals, recomputation [470,472] versus[467.5,468.5] leaves gap1.5/471=.00318≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN eligibility lists protocol pp.32–33/SAP pp.17–18 versus REPORT main p.2 | Severe-cognitive-impairment and KPWA-only OUD operational criteria are not repeated in the main list; no report statement affirmatively includes these patients or supplies conflicting analysis counts. | CONDITIONAL_OR_UNREPORTED |
| PLAN moderator tables protocol pp.25–26/SAP pp.14–15 versus analytic text protocol pp.57–58/SAP pp.21–23 | Moderator table names6-month MCID while interaction comparison is3 months; support mediator table starts at randomization notification while analytic text says baseline; mediation weight equation omits the narrative's baseline-confounder term. No such ancillary fitted result is reported here and these details do not alter a reported primary/key-secondary analysis or decision rule. | PERIPHERAL_COMPARISON |
| REPORT main Table3 pp.10–11 PGIC heading versus scale footnotes; PLAN names and REPORT names throughout | PGIC “mean change” refers to a change-impression item whose scale is explicitly given; virtual coach/health coach, usual care/usual care plus, and ability-to-participate/social-role-functioning descriptions identify the same outcomes or arms. No numerical assignment changes. | TERMINOLOGY_OR_WORDING |
| PLAN ancillary analyses versus supplied REPORT outcome displays | Moderator, mediation, economic and exploratory outcome analyses are not presented in this primary results package. The plans do not designate these absent outputs as primary or key secondary outcomes of this report, and no report claims to present them. | CONDITIONAL_OR_UNREPORTED |

## Evidence provenance and limitations

Fresh source confirmation for this checker: preprocessing/cross_source_review/main-2.png, main-3.png, main-4.png, tidier-3.png, tidier-4.png and results-4.png, generated from exact supplied sources with allowed pdf_tools.py render, PyMuPDF1.26.4,150dpi, CPU. Current fresh SAP/protocol renders and current report-source renders confirm the additional cited plan and fitted-model locations. Workbook quoted flags, categories and selection tests were confirmed by direct unzip/Perl inspection of supplied worksheet XML and shared strings; no workbook recalculation occurred. No new OCR was required.

Native plan text is glyph encoded; source renders and fresh visual maps supply coverage. Unlabeled histogram bars are not exact numerical copies. No participant-level data, fitted code or additional amendments are supplied, so this checker does not infer the number of people affected by a criterion, reproduce an unreported design matrix, or select a preferred model. These are evidence limits, not scientific coverage gaps. Source and reused assets remain unchanged.
