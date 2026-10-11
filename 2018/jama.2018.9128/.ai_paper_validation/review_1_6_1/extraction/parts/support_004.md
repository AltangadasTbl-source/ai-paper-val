# Support quantitative mapping, shard 004

## Scope and evidence method

Exact disjoint scope: DOC-002 `joi180075supp1_prod.pdf` PDF pages 97–113 (17 pages; PLAN), and DOC-003 `joi180075supp2_prod.pdf` PDF pages 1–8 (8 pages; REPORT). All 25 assigned source pages mapped. All 25 are reusable-backed; fresh-required units zero under the curator's verified inventory. Reused whole-document native/layout text was partitioned on form feeds with direct `awk`; no source or reused asset changed. Reusable rendered source pages were visually inspected for DOC-002 pages 108–111, and DOC-003 pages 2–8, including table values, mathematical equations, figure labels and the copyright-only page. Native/layout text is a transcription aid; source PDF remains authority. Legacy derivative engine unrecorded; current read commands use GNU awk and image inspection. No OCR, fallback, Office extraction, workbook formula/cached-value mapping, or external sources needed. Shard keys SUP4-* are mapping keys, not canonical statistical inventory IDs or findings. No candidate diagnosis occurs here.

## Page coverage

| Source | Page | Content opened and mapped | Status |
|---|---:|---|---|
| DOC-002 | 97 | Power table, recruitment sample size, effect modifiers and mediators | COMPLETE |
| DOC-002 | 98 | Secondary analyses related to primary hypothesis | COMPLETE |
| DOC-002 | 99 | Random-effect sensitivity sequence; secondary aims opening | COMPLETE |
| DOC-002 | 100 | Aims 2 and 3 models and hypotheses | COMPLETE |
| DOC-002 | 101 | Aims 4–6, social network/genetic analysis specifications | COMPLETE |
| DOC-002 | 102 | Community-center program counts analysis | COMPLETE |
| DOC-002 | 103 | Bibliographic references 1–20; no applicable trial quantitative result/analysis | COMPLETE |
| DOC-002 | 104 | Bibliographic references 21–41; no applicable trial quantitative result/analysis | COMPLETE |
| DOC-002 | 105 | Bibliographic references 42–48; no applicable trial quantitative result/analysis | COMPLETE |
| DOC-002 | 106 | Chronological amendments, additional 30 dyads and study operations | COMPLETE |
| DOC-002 | 107 | Amendment continuation; additional follow-up year and procedures | COMPLETE |
| DOC-002 | 108 | Original SAP, primary formula/covariates/random effects/hypothesis | COMPLETE |
| DOC-002 | 109 | Original SAP hypothesis continuation, positive quadratic coefficient expectation | COMPLETE |
| DOC-002 | 110 | Final SAP design, primary outcome and ITT/ML model | COMPLETE |
| DOC-002 | 111 | Final SAP hierarchical/combined equations, predictors, covariance | COMPLETE |
| DOC-002 | 112 | Final joint likelihood-ratio decision and missing-data approach | COMPLETE |
| DOC-002 | 113 | Explicit blinded SAP changes, covariates/test/variance/missing-data disclosure | COMPLETE |
| DOC-003 | 1 | Cover and contents; no displayed result, names of all 2 tables/3 figures mapped | COMPLETE |
| DOC-003 | 2 | eTable 1 all 5 rows and all 3 footnotes | COMPLETE |
| DOC-003 | 3 | eTable 2 first 33 estimate rows, moderator labels/units | COMPLETE |
| DOC-003 | 4 | eTable 2 final 5 estimate rows, model and all denominator footnotes | COMPLETE |
| DOC-003 | 5 | eFigure 1 all 6 age-sex panels, axis/legend/CI/reference curves | COMPLETE |
| DOC-003 | 6 | Copyright only, visually confirmed; no applicable quantitative content | COMPLETE |
| DOC-003 | 7 | eFigure 2 obesity risk difference by baseline BMI, axes, intervals and reference lines | COMPLETE |
| DOC-003 | 8 | eFigure 3 all 3 food-security panels, axes/legend/CI/directions | COMPLETE |

## PLAN relationships

### SUP4-P01 — power and enrollment, page 97

Source: [DOC-002 page 97](../../../../joi180075supp1_prod.pdf#page=97). Table columns are standardized effect size 0.3, 0.4 (OD program default), 0.5; cells are total sample size:

| Power | Effect 0.3 | Effect 0.4 | Effect 0.5 |
|---|---:|---:|---:|
| 70.00% | 500 | 285 | 186 |
| 80.00% | 640 | 360 | 232 |
| 90.00% | 860 | 480 | 308 |

Pilot considerations: inclusion range considered extends from baseline BMI 50th–95th to 50th–99th percentile. In Salud estimation, adding 95th–99th percentile increased variance and group difference, leaving standardized effect size nearly unchanged; desired sample sizes under various conditions changed by no more than two persons. Planned recruitment 600 children to allow attrition; may stop smaller if recruitment problematic, ideally at least 480 (Table 5 reference). Matching main-paper keys: randomized enrollment count, sample-size rationale and 90% power/effect assumptions; table/model inputs beginning before p97 belong to another shard.

### SUP4-P02 — modifiers and mediators, page 97

Source: [DOC-002 page 97](../../../../joi180075supp1_prod.pdf#page=97). Previously listed moderators, e.g. race/ethnicity and genetic risk score, entered as interactions for child BMI trajectory; relevant three-way interactions, e.g. gender × age × group, also tested. Mediators/covariates entered as time-varying covariates with effects assessed controlling all else. Matching keys: main-paper exploratory moderation and covariate methods.

### SUP4-P03 — secondary primary-related analyses, page 98

Source: [DOC-002 page 98](../../../../joi180075supp1_prod.pdf#page=98). Entry at age at least 3 and under 6 years; occasion six at least 3 years after enrollment. Adiposity rebound mean age/nadir derived from main-model coefficients: control `−β2/(2β3)`; intervention `−β4/(2β5)`. Parent baseline BMI predictor and subsequent parent BMI as time-varying covariates for child trajectory. Group mean BMI at 36 months to be tested. Acceptable versus unacceptable child BMI trajectory binary outcome compared first unadjusted 2×2 (group × outcome), then logistic regression adjusted for demographics (e.g. gender), baseline variables and baseline normal/overweight category. Matching keys: main BMI trajectory model, 36-month BMI, adult BMI moderation and exploratory binary outcomes.

### SUP4-P04 — random-effect sensitivity sequence, page 99

Source: [DOC-002 page 99](../../../../joi180075supp1_prod.pdf#page=99). Original fitted model changed to independent covariance, reducing stated random-effect count 7→5; add two condition-specific age-squared random effects under independence, count 5→7; then unstructured covariance with age-squared retained, count 13. At each step assess effects of added terms and convergence. Thirteen-component model considered to have reduced power and is secondary rather than primary. If within-condition session ICC variability sufficiently wide, consider cluster-adjusted standard errors for fixed and random effects, described as generalized sandwich estimator. Matching keys: primary covariance/random effects, session clustering, sensitivity analyses; p113 later disclosure is required version context.

### SUP4-P05 — Aim 2 diet/activity, pages 99–100

Sources: [DOC-002 page 99](../../../../joi180075supp1_prod.pdf#page=99), [page 100](../../../../joi180075supp1_prod.pdf#page=100). Treatment versus control anticipated lower actigraphy sedentary activity after intensive phase T2 and study completion; better age-specific USDA nutrition adherence via diet recall (age-appropriate calories, more fruits/vegetables, less sugar-sweetened beverages). Sedentary level multiple regression on group with baseline sedentary level and covariates e.g. child gender at T2/completion. Binary adherence unadjusted 2×2 then adjusted logistic regression with group, gender, baseline BMI. Matching keys: main-paper dietary energy intake and physical activity secondary outcomes, their time points/models.

### SUP4-P06 — Aim 3 parent-child diet/activity, page 100

Source: [DOC-002 page 100](../../../../joi180075supp1_prod.pdf#page=100). Parents categorized by significant sedentary reduction from baseline (yes/no), and appropriate dietary adherence (yes/no). Child sedentary multiple regression at T2/completion: group, baseline child sedentary level, both parent binary variables, each parent-variable × group interaction, covariates e.g. gender. Child binary nutrition adherence logistic model at T2/completion with same parent variables/interactions and group/covariates. Matching keys: parent behavior moderation of child diet/activity; these are secondary aim definitions, not reported numeric results here.

### SUP4-P07 — Aim 4 social networks, page 101

Source: [DOC-002 page 101](../../../../joi180075supp1_prod.pdf#page=101). UCINET and In-Flow used for network strength/cohesion and graphical/network measures, combined individual network and attribute variables. Regression/logistic analyses of changing networks on child BMI growth, child/adult body composition, feeding practices, child/adult activity and energy intake. Hypothesized within-network similarity and stronger new networks linked to reduced sedentary/improved diet. No numerical network effect reported here.

### SUP4-P08 — Aim 5 genetic risk, page 101

Source: [DOC-002 page 101](../../../../joi180075supp1_prod.pdf#page=101). Higher genetic risk score associated with heavier-for-age baseline BMI and moderation of growth; stated model regresses heavier-for-age baseline BMI on score and score × time with covariates e.g. gender. No genetic result reported here. Matching keys: genetic risk moderator specification.

### SUP4-P09 — Aim 6 center program counts, pages 101–102

Sources: [DOC-002 page 101](../../../../joi180075supp1_prod.pdf#page=101), [page 102](../../../../joi180075supp1_prod.pdf#page=102). Two participating centers East/Coleman: counts of activity/nutrition programs baseline and end; compare within-center increases and count comparisons with nonparticipating centers at both occasions. No actual counts or inferential model supplied. Matching key: community programming secondary aim, peripheral administrative comparisons unless tied to specified statistical result.

### SUP4-P10 — amendment register, pages 106–107

Sources: [DOC-002 page 106](../../../../joi180075supp1_prod.pdf#page=106), [page 107](../../../../joi180075supp1_prod.pdf#page=107). Critical amendments chronological; implemented after written IRB approval. Quantitatively relevant entries: 12/18/12 recruitment changed from three waves to rolling cohorts; intervention phone makeup and all six data-collection sessions permit makeup/home collection. 5/14/13 prescreen child height/weight can be baseline data. 8/20/13 cognitive-assessment timing changed, random quality-control participants compensated $10. 4/22/14 add 30 parent-child dyads. 6/5/14 ancillary ACTIVATE subcohort family survey at T5/T6 and GROW Baby pregnant-family medical-record comparison (partially garbled native text; ancillary content, no primary quantitative value lost). 3/24/15 add six maternal pregnancy diet/activity questions. 7/14/15 second saliva collection at T6. 10/1/15 compensation up to $100 at T5/T6 and additional follow-up year T7. Other entries are survey addition 6/12/12; group renaming/retention tool 7/12/12; recruitment sites 7/31/12; GIS/informed-consent clarification 9/19/12; convenient baseline sites 1/18/13; consent visuals/prescreen scripts/incentives 2/15/13; referral recruitment 3/8/13; reminder texts 3/19/13; re-engagement letter 5/20/14; consent clarification 1/21/15; confidentiality certificate 5/18/17. Matching keys: enrollment target 600 plus amendment dyads; intervention identities; baseline measurements and optional later follow-up. All administrative units opened; no other result estimate present.

### SUP4-P11 — original SAP, pages 108–109

Sources: [DOC-002 page 108](../../../../joi180075supp1_prod.pdf#page=108), [page 109](../../../../joi180075supp1_prod.pdf#page=109). DSMB approval April 2012. Formula visually confirmed:

`BMI = β0 C + β1 I + β2(age−X) C + β3(age−X)^2 C + β4(age−X) I + β5(age−X)^2 I + other predictors + random terms`.

I=1 intervention/0 control; C=1 control/0 intervention. No traditional common intercept; X is age at enrollment. β0 and β1 are respective arm baseline means; linear terms entry growth; quadratic terms acceleration. Planned other predictors gender (female=1/male=0), ethnicity anticipated three groups/two indicators, gender × age. Random subject intercept, subject × age and covariance with heterogeneous variance; no primary random subject × age² because proposed unstructured matrix would have 13 random-effect components/convergence concerns. Baseline BMI not predictor, nor BMI × treatment in primary; baseline BMI × treatment secondary. Primary post-hoc test β3=β5 at 0.05; no linear-term hypothesis. β5 expected positive and smaller than β3. Matching keys: revised model on pp110–113 and main primary method. Explicit final-plan change disclosure must accompany any version comparison.

### SUP4-P12 — final SAP design and estimand, page 110

Source: [DOC-002 page 110](../../../../joi180075supp1_prod.pdf#page=110). Finalized November 2016. Open longitudinal randomized dyads, two sites, children 3–5 years, within-site stratification by parent language English/Spanish, three-year prevention versus control. Says six occasions; printed list baseline, 12 weeks/3 months, 9, 12, 36 months (24 months not in this printed list). Primary BMI trajectories slower in treatment; shape ages 3–8 curvilinear. ITT multilevel mixed-effects linear model; maximum likelihood handles missingness. Matching keys: main randomization/assessment schedule/primary population and model.

### SUP4-P13 — final SAP hierarchical formula, page 111

Source: [DOC-002 page 111](../../../../joi180075supp1_prod.pdf#page=111). Visually confirmed equations; native text has encoded mathematical glyphs, normalized below from rendered page. Repeated BMI Level 1 nested in children Level 2. Time years since baseline, actual individual measurement dates. Baseline centered age and assignment predict intercept/linear/quadratic growth; gender predicts intercept only.

`BMI_ti = π0i + π1i Time_ti + π2i Time_ti² + e_ti`

`π0i = β00 + β01(age−C)_i + β02 I_i + β03 F_i + r0i`

`π1i = β10 + β11(age−C)_i + β12 I_i + r1i`

`π2i = β20 + β21(age−C)_i + β22 I_i + r2i`.

Combined equation sums these intercept, Time-multiplied linear and Time²-multiplied quadratic brackets plus `r0i + r1i Time_ti + r2i Time_ti² + e_ti`. C here denotes centering value, not the original SAP's control indicator. I intervention=1/control=0; F female=1/male=0. β00 control male initial mean adjusted for centered baseline age; β01 baseline age effect; β02 initial assignment effect expected 0; β03 female initial effect; text describes r0i as random error variance. β10 control linear baseline growth, β11 baseline age effect on linear growth; β12 intervention linear growth effect; β22 intervention acceleration effect adjusted baseline age. Unstructured variance-covariance matrix. Matching keys: primary mixed model parameters, units BMI/year and BMI/year², report adjusted trajectories and test.

### SUP4-P14 — final joint test/missingness, page 112

Source: [DOC-002 page 112](../../../../joi180075supp1_prod.pdf#page=112). Likelihood-ratio test two df jointly β12=β22=0. If joint P<0.05, intervention effect significant; otherwise effectiveness not demonstrated. Six repeated measurements, mixed model uses all available observations without dropping subjects for missed occasions (comparison with older repeated-measures ANOVA). Matching keys: main joint trajectory P, ML/available data approach.

### SUP4-P15 — disclosed changes and version context, page 113

Source: [DOC-002 page 113](../../../../joi180075supp1_prod.pdf#page=113). All study personnel including site statisticians still blinded to group-aggregated non-baseline data when changes made. Final predictors baseline age and gender; ethnicity dropped for sample homogeneity. Gender intercept predictor, gender × age removed based on comparable curve shapes. Clarifies baseline age versus longitudinal time exposed. Primary maximum likelihood missing-data treatment explicit; secondary post-hoc MI with/without auxiliary variables remains planned. Original quadratic-only 0.05 hypothesis changed to two-df likelihood-ratio joint linear/quadratic intervention test at P<0.05; rationale both terms govern curve shape. Original heterogeneous session ICC structure, estimated separately in intervention because control had no group sessions, changed to homogeneous variance primary; heterogeneous explored secondary. These disclosures directly contextualize original-versus-final primary covariate, test and variance differences; they must not be omitted from matched comparisons. Matching keys: report declared November 2016 revisions, primary joint test and sensitivity analyses.

## REPORT eTable 1: child BMI by occasion

Source for every row: [DOC-003 page 2](../../../../joi180075supp2_prod.pdf#page=2). Intervention/control are mean (SD), counts are available observations; adjusted differences and CIs from longitudinal mixed-effects regression, not differences recomputed from displayed means. Corrected P values use Benjamini–Hochberg for five comparisons. BMI quantity kg/m² (the table calls it child BMI; standard unit confirmed graphical axes). Main matching keys: child BMI primary outcome by occasion, Table 2/primary narrative and 36-month result.

| Key | Month | Intervention n | Intervention mean (SD) | Control n | Control mean (SD) | Adjusted difference (95% CI) | P | BH P |
|---|---:|---:|---|---:|---|---|---:|---:|
| SUP4-R01 | 3 | 279 | 16.7 (0.9) | 271 | 16.6 (1.0) | −0.01 (−0.12, 0.13) | 0.83 | 0.83 |
| SUP4-R02 | 9 | 280 | 16.7 (1.0) | 280 | 16.7 (1.2) | −0.04 (−0.20, 0.12) | 0.63 | 0.83 |
| SUP4-R03 | 12 | 274 | 16.7 (1.2) | 275 | 16.8 (1.3) | −0.05 (−0.23, 0.13) | 0.62 | 0.83 |
| SUP4-R04 | 24 | 278 | 17.2 (1.5) | 266 | 17.2 (1.7) | −0.03 (−0.28, 0.22) | 0.80 | 0.83 |
| SUP4-R05 | 36 | 276 | 17.8 (2.2) | 272 | 17.8 (2.1) | 0.05 (−0.29, 0.38) | 0.79 | 0.83 |

## REPORT eTable 2: every moderation estimate

Sources: [DOC-003 page 3](../../../../joi180075supp2_prod.pdf#page=3), [page 4](../../../../joi180075supp2_prod.pdf#page=4). Every linear quantity is BMI difference/year; every quadratic quantity BMI difference/year². Continuous moderators represented by interaction terms, categorical moderators by within-category intervention effects. These are estimates from longitudinal mixed-effects regression adjusted baseline age and gender with additional moderator interaction terms for growth parameters. This is separate from a global joint moderation test; table P values are individual terms. Main matching keys: exploratory moderator narrative/global interaction P results; age-sex and food-security graphical trajectories below. Contrast intervention versus control.

| Key | Page | Moderator (scale/category) | Growth term | Estimate (95% CI) | P |
|---|---:|---|---|---|---:|
| SUP4-R06 | 3 | Baseline child age, continuous years | Linear | 0.105 (−0.081, 0.292) | 0.27 |
| SUP4-R07 | 3 | Baseline child age, continuous years | Quadratic | −0.024 (−0.076, 0.028) | 0.37 |
| SUP4-R08 | 3 | Child gender, male | Linear | −0.143 (−0.379, 0.093) | 0.24 |
| SUP4-R09 | 3 | Child gender, male | Quadratic | 0.076 (0.010, 0.143) | 0.02 |
| SUP4-R10 | 3 | Child gender, female | Linear | −0.025 (−0.253, 0.203) | 0.83 |
| SUP4-R11 | 3 | Child gender, female | Quadratic | −0.009 (−0.072, 0.055) | 0.79 |
| SUP4-R12 | 3 | Baseline adult BMI, continuous kg/m² | Linear | −0.013 (−0.043, 0.017) | 0.40 |
| SUP4-R13 | 3 | Baseline adult BMI, continuous kg/m² | Quadratic | 0.001 (−0.007, 0.009) | 0.81 |
| SUP4-R14 | 3 | Parent ethnicity, Hispanic | Linear | −0.062 (−0.234, 0.110) | 0.48 |
| SUP4-R15 | 3 | Parent ethnicity, Hispanic | Quadratic | 0.024 (−0.024, 0.073) | 0.33 |
| SUP4-R16 | 3 | Parent ethnicity, non-Hispanic | Linear | −0.279 (−0.827, 0.269) | 0.32 |
| SUP4-R17 | 3 | Parent ethnicity, non-Hispanic | Quadratic | 0.106 (−0.046, 0.258) | 0.17 |
| SUP4-R18 | 3 | Baseline child energy intake, continuous calories | Linear | −0.207 (−0.649, 0.235) | 0.36 |
| SUP4-R19 | 3 | Baseline child energy intake, continuous calories | Quadratic | 0.163 (0.039, 0.286) | 0.01 |
| SUP4-R20 | 3 | Baseline child energy from fat, continuous % | Linear | −0.012 (−0.044, 0.019) | 0.45 |
| SUP4-R21 | 3 | Baseline child energy from fat, continuous % | Quadratic | 0.004 (−0.005, 0.013) | 0.40 |
| SUP4-R22 | 3 | Baseline child energy from carbohydrate, continuous % | Linear | 0.003 (−0.023, 0.029) | 0.81 |
| SUP4-R23 | 3 | Baseline child energy from carbohydrate, continuous % | Quadratic | −0.002 (−0.009, 0.005) | 0.57 |
| SUP4-R24 | 3 | Baseline child energy from protein, continuous % | Linear | 0.018 (−0.033, 0.068) | 0.49 |
| SUP4-R25 | 3 | Baseline child energy from protein, continuous % | Quadratic | −0.002 (−0.016, 0.013) | 0.82 |
| SUP4-R26 | 3 | Baseline child wear time sedentary, continuous % | Linear | −0.015 (−0.041, 0.012) | 0.28 |
| SUP4-R27 | 3 | Baseline child wear time sedentary, continuous % | Quadratic | 0.003 (−0.004, 0.010) | 0.45 |
| SUP4-R28 | 3 | Baseline child wear time moderate/vigorous activity, continuous % | Linear | 0.019 (−0.035, 0.073) | 0.48 |
| SUP4-R29 | 3 | Baseline child wear time moderate/vigorous activity, continuous % | Quadratic | −0.006 (−0.021, 0.009) | 0.48 |
| SUP4-R30 | 3 | Baseline child BMI percentile, continuous percentile | Linear | −0.001 (−0.018, 0.016) | 0.88 |
| SUP4-R31 | 3 | Baseline child BMI percentile, continuous percentile | Quadratic | −0.0005 (−0.0051, 0.0042) | 0.85 |
| SUP4-R32 | 3 | Child birthweight, continuous kg | Linear | −0.167 (−0.600, 0.266) | 0.45 |
| SUP4-R33 | 3 | Child birthweight, continuous kg | Quadratic | 0.078 (−0.045, 0.201) | 0.21 |
| SUP4-R34 | 3 | Baseline food security, secure | Linear | −0.092 (−0.308, 0.124) | 0.41 |
| SUP4-R35 | 3 | Baseline food security, secure | Quadratic | 0.026 (−0.034, 0.087) | 0.39 |
| SUP4-R36 | 3 | Baseline food security, insecure without hunger | Linear | 0.106 (−0.203, 0.415) | 0.50 |
| SUP4-R37 | 3 | Baseline food security, insecure without hunger | Quadratic | −0.017 (−0.104, 0.069) | 0.70 |
| SUP4-R38 | 3 | Baseline food security, insecure with hunger | Linear | −0.499 (−0.954, −0.044) | 0.03 |
| SUP4-R39 | 4 | Baseline food security, insecure with hunger | Quadratic | 0.149 (0.023, 0.275) | 0.02 |
| SUP4-R40 | 4 | Community center A | Linear | −0.054 (−0.231, 0.124) | 0.55 |
| SUP4-R41 | 4 | Community center A | Quadratic | 0.025 (−0.025, 0.074) | 0.33 |
| SUP4-R42 | 4 | Community center B | Linear | −0.240 (−0.672, 0.192) | 0.28 |
| SUP4-R43 | 4 | Community center B | Quadratic | 0.069 (−0.052, 0.190) | 0.26 |

SUP4-R44 — denominator footnotes on page 4: b valid baseline adult BMI, e.g. not pregnant/unreliable, n=563; c valid baseline diet recall n=609 (energy intake/fat/carbohydrate superscripts explicitly printed; protein heading has no c superscript); d valid baseline accelerometry n=604; e valid child baseline BMI percentile and ≥1 valid nonbaseline child BMI n=589; f valid child birthweight n=405; g valid baseline food-security status n=606. Age/gender/parent ethnicity/center headings have no denominator superscript. Preserve these source distinctions; no unprinted n inferred.

## REPORT figures

### SUP4-R45 — eFigure 1, six age-sex panels

Source: [DOC-003 page 5](../../../../joi180075supp2_prod.pdf#page=5). Longitudinal mixed-model estimated BMI trajectories for baseline ages 3, 4, 5 years separately male/female, arranged male left/female right by age rows. X Months ticks 0,12,24,36. Y Fitted Mean (95% CI), Child BMI (kg/m²), ticks 15–20. Blue control, black intervention. Shaded 95% CIs around each curve; reference CDC standardized 50th green, 85th orange and 95th red percentile growth curves specific to age/sex. Age 3 fitted curves fall modestly then rise; age 4 near-flat early then increase; age 5 increase more strongly. Treatment/control nearly coincide in all six panels, overlapping shaded regions. Exact curve coordinates and CI endpoints not printed; graphical locations cannot supply precise tabular estimates. All six panels included, no omitted p6 continuation. Matching keys: primary adjusted child BMI trajectory, baseline-age/gender models and eTable2 individual categorical intervention effects (distinct moderation models must be matched before comparison).

### SUP4-R46 — eFigure 2, obesity risk at three months

Source: [DOC-003 page 7](../../../../joi180075supp2_prod.pdf#page=7). Title Model-Estimated Intervention Effect on Child Obesity Risk at 3 Months by Child Baseline BMI. X child baseline BMI kg/m², ticks 15,15.5,16,16.5,17,17.5,18. Y Fitted Mean (95% CI), Child Obesity Risk Difference, ticks 0,−0.1,−0.2,−0.3,−0.4,−0.5. Dotted/connected estimate is intervention minus control obesity risk; capped intervals are 95% CIs. Horizontal reference at zero; vertical mean baseline child BMI reference located between 16.5 and 17 (approximately 16.6, graph reading only). Plotted point at each x tick; risk difference near zero at 15–16, increasingly negative with greater BMI, approximately −0.02 at16.5, −0.04 at17, −0.095 at17.5, −0.23 at18, with much wider CI at18 (roughly −0.45 to slightly below0). These are approximate graphical readings, not source-printed numeric results; exact points not labeled. Matching keys: main three-month obesity exploratory analysis and baseline-BMI moderation; risk difference is not OR/RR and not a BMI difference.

### SUP4-R47 — eFigure 3, all food-security categories

Source: [DOC-003 page 8](../../../../joi180075supp2_prod.pdf#page=8). Longitudinal mixed-model child BMI trajectories moderated by baseline food security: secure, insecure without hunger, insecure with hunger. X Months in Study ticks0,12,24,36; Y Fitted Mean (95% CI), Child BMI (kg/m²), ticks16,17,18,19. Blue control, black intervention; each shaded95% CI. Secure trajectories begin about16.6 and reach about17.6, intervention slightly below control. Insecure without hunger begin about16.5 and reach about18.1 intervention versus17.9 control, intervention above after baseline. Insecure with hunger begin about16.7; intervention falls initially then increases and lies below control during follow-up, at36 months about18.1 intervention versus18.3 control. These coordinates are approximate graphical readings; no exact curve estimates/endpoints printed. Matching keys: food-security moderation narrative and eTable2 category-specific linear/quadratic estimates SUP4-R34–R39; plotted effects have quadratic time dependence and must not be treated as a single fixed subgroup risk difference.

## Completeness and limitations

Mapped 25/25 pages; 15 plan mapping groups, 5 time-point inferential/count rows, 38 individual moderation coefficient/CI/P rows, one denominator group and three graphical relationship groups. Bibliographic pages103–105, cover page1 and copyright-only page6 explicitly no-applicable for numerical result extraction. No quantitative scientific coverage gap. The partial native encoding of one ancillary amendment on plan p106 does not conceal a primary analysis or displayed result; its study context is described above. Exact graphical point/CI coordinates are not printed in source, and approximations are labeled; no raw data/workbook or formula caches supplied in this scope. All p113 revision disclosures preserved as version context. Sources and reused artifacts unchanged.
