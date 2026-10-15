# Statistical relationship inventory — report-supplement pass-1 shard

Fresh runtime agent: /root/stat1_reports; configured run model gpt-6.1-sol; reasoning effort high; stage statistics_pass_1; fresh spawn. Exact assigned scope: DOC-005 PDF pages1–16 and19,eTables1–10,eFigures1–2; DOC-004 PDFpages1–7 andDOC-006 eTable 3 A1:J115 for any inferential/method relationships. DOC-005 PDF17–18/eTable11 is excluded from this shard and belongs to the raw-score statistical peer. MAIN inference rows and PLAN-internal relationships belong to separate peers. Every location in this artifact is REPORT; matching main methods were read only for shared definitions (all tests2-sidedα=.05,95%CIs,GEEclustering), not assigned MAIN results.

Scientific inputs: exact sources, current fresh map extraction/parts/reports_restart.md, selective current main-method definitions. No prior Workflow1.6.2 artifact or old finding/report was a scientific input. Quantitative source authority: fresh PyMuPDF1.26.4 CPU renders in preprocessing/stat1_reports, current mapper's source-confirmed complete transcriptions; direct permitted Office helper extract_office_source.py for all 525 populated workbook cells. No web or external literature. No other Python used.

This shard contains 63 stable relationship records, S201–S263. Families carry every printed row/tuple explicitly, not a selected subset. Findings: F-ST1-201–F-ST1-206. Each record is PASS_1_COMPLETE; a fresh separate pass-2 agent must revisit every record. Missing definitions are named as limitations, not filled from convention. Counts/descriptive values without inferential content remain mapped by the numeric peer; they are retained here when needed to identify a statistical population.

## S201 — Outcome definitions, thresholds and directions

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.2](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=2)
- **Finding links:** None

**Printed values and method:**

```text
### SUP-RESULTS-P02 — DOC-005 PDF p2

[Exact source page](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=2)


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

**Pass-1 checks and result:** Means of 11/4/7 BPI items span0–10, higher worse; MCID≥30% decrease,3-month primary. PHQ8sum0–24; GAD7sum0–21; PROMIS T-score references50/10, sleep higher worse/social and physical higher better. Ranges, item counts, thresholds and direction definitions were read; no internal inferential conflict. These definitions anchor all outcome rows below.

## S202 — Primary response completeness and missingness decision

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.4](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.7](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** None

**Printed values and method:**

```text
### SUP-RESULTS-P07 — DOC-005 PDF p7

[Exact source page](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)


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
```

**Pass-1 checks and result:** 3M missingness100−77.1=22.9%>15%: branch triggered; arm completeness79.9/69.8/81.6 differs. Counts and percentages agree within display precision. Pattern counts188+283+1568=2039 versus2036; PT644vs643 andHC692vs690; implied observed visits5458vs5449. All remaining relative gaps<.05, one exclusion. Base complete visits1798+1790+1861=5449.

## S203 — Additional predictor selection and analysis attribution

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.4](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.5](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [DOC-005 PDF p.7](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** F-ST1-203, F-ST1-204

**Printed values and method:**

```text
P<.10 in both adjusted3M-MCID modified Poisson and3M-missingness logistic models selects additional imputation/estimation predictors. Weight model selects variables associated with3M-MCID and any follow-up in corresponding separate adjustedmodels. Base set: arm, baseline severity, age, sex, site, rural, multisite pain,mentalhealth. eTable2 final imputation/estimation adds education(anycollege vsHSorless),unemployment; weight addsPEG,PHQ8,GAD7,anynegativeSDOH,education.
```

**Pass-1 checks and result:** The stated dual-selection rule is coherent. Applied covariate identity/coding is not fully aligned with model coefficient displays; seeS261/S262. No preference for a different selection method is proposed.

## S204 — Pattern-mixture imputation design and response construction

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.4](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.5](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5)
- **Finding links:** None

**Printed values and method:**

```text
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


where 𝑌𝑌𝑖𝑖𝑖𝑖 is the change in pain severity for individual i at time point 𝑚𝑚, 𝑋𝑋𝑖𝑖 is the intervention group (UC, PT, and
UC), 𝑚𝑚 is the number of months post randomization, and 𝒁𝒁𝑖𝑖 is the vector of baseline covariates. Further, 𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 is a
variable that indicates the pattern of observed outcomes present. In this case, 𝑂𝑂𝑂𝑂𝑂𝑂𝑖𝑖 takes on the values 1, 2 or 3
depending on whether 1, 2 or 3 of the follow-up measures are observed for a randomized person. The 𝒁𝒁𝑖𝑖 include all
adjustment variables as specified previously. We fit this assuming a modified linear model using GEE with
independent working correlation and robust standard errors, accounting for clustering of participants within health
coaches and multiple observations per person. The fitted imputation model was then used to replace missing
outcomes data with predicted values from the model. The binary MCID outcome variable was then calculated using
the change outcome with imputed data and the baseline value of pain severity.
```

**Pass-1 checks and result:** Linear GEE, independence, robust clustering byperson/coach; arm × time and arm × observed pattern terms printed; referenceOBS3,UC,3M; missing change replaced by predicted values; binary MCID computed from change/baseline. Formula and coefficient structural families align. No unstated covariance, finite-sample test or change-sign convention inferred.

## S205 — Imputation population, observed visits and missing values

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.7](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [DOC-005 PDF p.8](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8)
- **Finding links:** None

**Printed values and method:**

```text
eTable3 observations6108,persons2036,missingvalues659; eTable1 observed visits1798+1790+1861=5449; no follow-up295.
```

**Pass-1 checks and result:** 2036×3=6108;6108−5449=659;2331−295=2036. Participant-level and visit-level sample sizes reconcile. The minute observed-pattern discrepancy isS202's display precision exclusion.

## S206 — Primary estimation functional form, variance and clustering

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.5](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5)
- **Finding links:** None

**Printed values and method:**

```text
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
```

**Pass-1 checks and result:** Log-mean binary MCID Poisson GEE witharm, time,arm × time; robust provider/person sandwich and joint imputation/analysis variance referenced. Form reproduces coefficient/time-contrast families; no individual test statistic, degrees of freedom or numeric standard error supplied.

## S207 — Nonresponse weighting and baseline missing covariates

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.5](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [DOC-005 PDF p.6](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=6), [DOC-005 PDF p.10](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** None

**Printed values and method:**

```text
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


### SUP-RESULTS-P06 — DOC-005 PDF p6

[Exact source page](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=6)


estimation model described in the imputation section (step 2). The fitted weight model is presented in eTable 5, and
eTable 6 and eFigure 1 provide summaries of the predicted probabilities and corresponding weights.




© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.
```

**Pass-1 checks and result:** Entire2331 response-logistic fit;w=1/p scaled for analytic2036 persons, table4 visitweightssum6108=3×2036. Baseline missing means imputed fromavailablebaseline cohort. Conditional response distribution is not an outcome model; no raw/imputed equivalence assumed.

## S208 — Complete linear imputation coefficient/interval/P family

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.8](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8)
- **Finding links:** F-ST1-201

**Printed values and method:**

```text
### SUP-RESULTS-P08 — DOC-005 PDF p8

[Exact source page](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8)


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

**Pass-1 checks and result:** All 28 printed coefficient tuples: point containment and endpoint order hold; seven95%CI-excludes0/P>.05 conflicts consolidated F-ST1-201. Remaining null/significance statuses agree. Numeric Wald reconstruction is diagnostic only because coefficient test/df/interval construction not named. Time6, sex,age,etc diagnostics cannot establish a further contradiction beyond the seven null conflicts.

## S209 — Complete weighted primary RR/interval/P family

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.9](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=9)
- **Finding links:** F-ST1-202, F-ST1-204

**Printed values and method:**

```text
### SUP-RESULTS-P09 — DOC-005 PDF p9

[Exact source page](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=9)


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

**Pass-1 checks and result:** All 23 printed rows including identicalHC/PT3M repetition: containment/order hold; directions and multiplicative contrast closure fit display precision. Age and secondAA education lowerCI1/P.046 conflict consolidated withPEG upperCI1/P.037 inF-ST1-202. Duplicate 3M row reconciles, not an excluded observation. Educationcoding/attribution addressedS261.

## S210 — Complete response-logistic OR/interval/P family

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.10](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** F-ST1-202, F-ST1-203

**Printed values and method:**

```text
### SUP-RESULTS-P10 — DOC-005 PDF p10

[Exact source page](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)


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
```

**Pass-1 checks and result:** All 16 OR95%CI/P tuples and c-statistic. Containment/order and referencegroup direction hold;male upper1,P.053 agrees. PEG upper1,P.037 belongsF-ST1-202. ORlabel is coherent forlogistic response model. Covariate membership discrepancy isS262; no odds-versus-risk relabeling.

## S211 — Response-probability and analytic weight summaries

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.10](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** None

**Printed values and method:**

```text
eTable 6. Summary of estimated weights.
                                                  Sum    Mean      SD   Min.   P25    P50    P75        Max.
  Estimated probability of having at
  least 1 follow-up.                               --    0.88   0.07    0.50   0.85   0.90   0.93       0.98
  Calculated weight used for
  analysis.                                       2036   1.00   0.09    0.89   0.94   0.97   1.03       1.75
```

**Pass-1 checks and result:** Probability[min.50,max.98],quartiles.85/.90/.93,mean.88,SD.07; weight[min.89,max1.75],quartiles.94/.97/1.03,mean1,SD.09,sum2036. Quantiles ordered and means inside extrema; reciprocal scaled range ratios are compatible within display precision. Mean reciprocal is not reciprocal mean; no such inference made.

## S212 — Complete-case sensitivity method and multiplicity rule

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
### SUP-RESULTS-P11 — DOC-005 PDF p11

[Exact source page](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)


SENSITIVITY ANALYSES
Missing Data Analyses: Sensitivity analysis results for different missing data assumptions for the MCID on pain severity primary outcome are presented in
eTable 7 below. eTable 7 provides results for different models assumptions for missing data that were pre-specified in the SAP including: a) complete-case
analysis (missing outcomes removed) adjusting for baseline pain severity, age, sex, clinical site, rural/medically underserved residency, multisite pain, and co-
occurring mental health conditions; b) worst case/best case analysis (missing outcomes for participants randomized to PT or HC are assumed 0 (worst case) and
missing outcomes for participants randomized to UC are 1 (best case)) adjusting for baseline pain severity, age, sex, clinical site, rural/medically underserved
residency, multisite pain, and co-occurring mental health conditions.


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

**Pass-1 checks and result:** No imputation/weighting,seven baseline covariates,1798observed3Mpersons=621+542+635; modified Poisson GEE estimates standardized proportions, RR andNNT. OmnibusWaldacross3arms gates pairwiseinterpretation atP<.05, all 3 rows pass. Test is omnibus, not a pairwise P.

## S213 — Worst/best-case sensitivity method and population

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
Missingactive(PT/HC)outcomes set0;missingUCoutcomes set1;all2331(UC777,PT776,HC778),seven baseline covariates;modified Poisson GEE. Table notes define NNT=100/(percentage difference) and disjoint infinity-containing branches when risk-difference CI crosses0.
```

**Pass-1 checks and result:** 777+776+778=2331; deliberately unfavorable active direction is coherent withmethod. All omnibusP<.001 passgate. NNT branch order is explicitly defined; do not treat positive/negative displayed endpoints as a conventional finite interval.

## S214 — eTable7 complete-case 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 32.2 (28.5, 36.3) 35.5 (32.0, 39.3) 24.0 (20.9, 27.6) 1.34 (1.12, 1.61) 1.48 (1.24, 1.75) 1.10 (0.94, 1.29) <0.001 13 (8, 33)             9 (7, 15)      31 (13, -60)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S215 — eTable7 complete-case 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
6 months 40.1 (36.3, 44.3) 41.1 (37.4, 45.1) 26.6 (23.4, 30.3) 1.51 (1.28, 1.77) 1.54 (1.32, 1.81) 1.02 (0.90, 1.17) <0.001 8 (6, 13) 7 (6, 11) 101 (16, -22)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S216 — eTable7 complete-case 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
12 months 41.0 (37.3, 45.1) 41.5 (37.9, 45.4) 30.5 (27.2, 34.3) 1.34 (1.16, 1.56) 1.36 (1.17, 1.57) 1.01 (0.89, 1.15) <0.001 10 (7, 20) 10 (7, 15) 217 (22, -28)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S217 — eTable7 worst/best-case 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 22.7 (20.0, 25.8) 29.3 (26.3, 32.6) 39.4 (36.1, 43.0) 0.58 (0.49, 0.67) 0.74 (0.65, 0.85) 1.29 (1.09, 1.52) <0.001 -6 (-9, -5) -10 (-18, -7) 16 (10, 40)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S218 — eTable7 worst/best-case 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
6 months 28.6 (25.6, 31.9) 33.1 (30.0, 36.5) 41.3 (38.0, 44.9) 0.69 (0.60, 0.79) 0.80 (0.70, 0.91) 1.16 (1.00, 1.34) <0.001 -8 (-13, -6) -13 (-26, -8) 23 (12, 227)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S219 — eTable7 worst/best-case 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.11](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11)
- **Finding links:** None

**Printed values and method:**

```text
12 months 31.3 (28.2, 34.6) 34.4 (31.2, 37.8) 43.0 (39.6, 46.7) 0.73 (0.64, 0.83) 0.80 (0.70, 0.91) 1.10 (0.96, 1.26) <0.001 -9 (-15, -7) -12 (-21, -8) 33 (15, -194)
```

**Pass-1 checks and result:** All three group95%CIs,three RR95%CIs,omnibusP andthree NNT95%limits reviewed. Containment/order/directions hold, treating disjoint NNT limits according tofootnote. RR point estimates consistent with standardized proportion ratios; omnibus differs frompairwise null tests; no implication thatall three pairwise contrasts significant. NNT reciprocals checked with half-unit precision; any remaining gaps≤.05 relative. RD variance absent: NNT limits cannot be derived from marginal group CIs alone.

## S220 — Protocol-change subset definitions, sample populations and adjustment

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.13](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=13), [DOC-005 PDF p.14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14), [DOC-005 PDF p.7](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** F-ST1-205

**Printed values and method:**

```text
### SUP-RESULTS-P13 — DOC-005 PDF p13

[Exact source page](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=13)


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


Before8/9/2021:N454,any follow-up366,3MPT149/HC153/UC152;after:N1877,any1670,3MUC512/PT448/HC527;after3/31/2022:N1038,any935,3MUC296/PT262/HC300. p13 callsresults primaryanalysis restrictedtosubsets; p14 covariate listcontainssevenbase variables.
```

**Pass-1 checks and result:** 454+1877=2331;366+1670=2036;letters858/1038=82.659%=82.7and935/1038=90.077%=90.1. Before3M149+153+152=454 label is randomized arm population rather thanobservedcounts; noadditional claimedresponse rate. Primaryvsbase subset covariates differ F-ST1-205. Prespecifiedenhancement/posthocletters status retained forcross-sourcechecker.

## S221 — eTable8 pre-enhancement 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 20.5 (14.2, 29.6) 28.5 (23.4, 34.8) 21.3 (15.2, 29.8) 0.96 (0.59, 1.57) 1.34 (0.92, 1.95) 1.39 (0.92, 2.10) 0.138 -120 (11, -10) 14 (7, -67) 13 (6, -84)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S222 — eTable8 pre-enhancement 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
6 months 32.9 (25.1, 43.0) 32.4 (27.8, 37.7) 25.2 (18.5, 34.2) 1.31 (0.88, 1.95) 1.29 (0.92, 1.80) 0.98 (0.73, 1.33) 0.313 13 (6, -27) 14 (7, -56) -185 (11, -10)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S223 — eTable8 pre-enhancement 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
12 months 32.6 (25.0, 42.5) 37.7 (32.2, 44.3) 20.5 (14.7, 28.6) 1.59 (1.05, 2.41) 1.84 (1.29, 2.63) 1.16 (0.85, 1.57) 0.003     9 (5, 75)   6 (4, 12)   20 (7, -20)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S224 — eTable8 post-enhancement 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 28.0 (24.4, 32.0) 32.7 (29.5, 36.2) 20.4 (17.4, 23.9) 1.37 (1.11, 1.69) 1.60 (1.33, 1.93) 1.17 (0.99, 1.38) <0.001 14 (8, 39) 9 (6, 14) 22 (11, -327)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S225 — eTable8 post-enhancement 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
6 months 33.8 (30.1, 38.1) 38.2 (34.5, 42.3) 22.2 (19.1, 25.7) 1.53 (1.27, 1.84) 1.72 (1.44, 2.06) 1.13 (0.97, 1.32) <0.001     9 (6, 16)   7 (5, 10)   24 (11, -88)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S226 — eTable8 post-enhancement 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
12 months 36.9 (33.1, 41.2) 38.1 (36.0, 40.3) 28.6 (25.2, 32.5) 1.29 (1.09, 1.52) 1.33 (1.16, 1.52) 1.03 (0.92, 1.16) <0.001   13 (8, 34)   11 (8, 19) 86 (18, -31)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S227 — eTable8 reminder-letter 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa 31.6 (26.7, 37.3) 34.1 (29.5, 39.5) 20.5 (16.6, 25.3) 1.54 (1.18, 2.01) 1.67 (1.30, 2.14) 1.08 (0.87, 1.34) <0.001 9 (6, 23) 8 (5, 14)   40 (11, -23)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S228 — eTable8 reminder-letter 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** F-ST1-206

**Printed values and method:**

```text
6 months 35.6 (30.6, 41.4) 40.6 (35.8, 46.1) 21.3 (17.5, 26.1) 1.67 (1.30, 2.14) 1.90 (1.50, 2.41) 1.14 (0.94, 1.39) <0.001 8 (5, 14)  6 (4, 8)    20 (9, -43)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S229 — eTable8 reminder-letter 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14)
- **Finding links:** None

**Printed values and method:**

```text
12 months 38.2 (33.1, 44.0) 38.9 (35.6, 42.5) 26.1 (21.9, 31.2) 1.46 (1.17, 1.83) 1.49 (1.23, 1.80) 1.02 (0.87, 1.20) <0.001 9 (6, 21) 8 (6, 14) 133 (15, -19)
```

**Pass-1 checks and result:** All group95%CIs,RR95%CIs,omnibusP,NNT95%limits checked. Containment/order/direction coherent; NNT disjoint branches handledby footnote. Pre3M/6M omnibus.138/.313 closespairwise gate despiteprinted estimates; no superiority assertion made. Other omnibus values pass the gate. Half-unit reciprocal NNT checks are withinthreshold except reminder-letter6MPT/UC,seeF-ST1-206. No inferred covariance/df orpairwise P.

## S230 — Unadjusted binary analysis method and effect identity

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
Narrative:no adjustment,weightingorimputation. Footnote:modified Poisson GEE forbinaryoutcome without adjustment. Heading:unadjusted n/N(%),RelativeRisk(95%CI); titlecontains'adjusted relative risk'. PT/HC/UC groups; contrastsPT/UC,HC/UC,HC/PT.
```

**Pass-1 checks and result:** Repeated definitionsmakeunadjustedstatus immediately identifiable; title wording screened once. Unadjusted crudeproportion ratios provide a diagnosticpoint-estimate check supportedbyexplicitmethod; all 27 RRs agree withratioswithinprecision. No crude-SE-based CI orassumedwithinperson/coach covariance imposed.

## S231 — eTable9 pain severity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa     179/542 (33.0) 229/635 (36.1) 151/621 (24.3) 1.36 (1.13, 1.63) 1.48 (1.26, 1.75) 1.09 (0.94, 1.27)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S232 — eTable9 pain severity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
6 months      225/547 (41.1) 259/621 (41.7) 167/622 (26.8) 1.53 (1.30, 1.80) 1.55 (1.32, 1.83) 1.01 (0.88, 1.17)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S233 — eTable9 pain severity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
12 months 246/583 (42.2) 269/639 (42.1) 197/639 (30.8) 1.37 (1.18, 1.59) 1.37 (1.21, 1.54) 1.00 (0.90, 1.10)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S234 — eTable9 pain intensity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa     164/543 (30.2) 192/635 (30.2) 129/621 (20.8) 1.46 (1.19, 1.78) 1.46 (1.18, 1.79) 1.00 (0.83, 1.21)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S235 — eTable9 pain intensity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
6 months      183/548 (33.4) 222/622 (35.7) 153/623 (24.6) 1.36 (1.13, 1.63) 1.45 (1.20, 1.74) 1.06 (0.90, 1.26)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S236 — eTable9 pain intensity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
12 months 218/583 (37.4) 238/641 (37.1) 191/639 (29.9) 1.25 (1.07, 1.47) 1.24 (1.08, 1.42) 0.99 (0.87, 1.12)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S237 — eTable9 pain-related interference 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa     206/543 (37.9) 249/635 (39.2) 169/620 (27.3) 1.39 (1.17, 1.64) 1.44 (1.25, 1.65) 1.03 (0.92, 1.17)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S238 — eTable9 pain-related interference 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
6 months      249/546 (45.6) 277/620 (44.7) 176/621 (28.3) 1.61 (1.38, 1.88) 1.58 (1.35, 1.85) 0.98 (0.86, 1.12)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S239 — eTable9 pain-related interference 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.15](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15)
- **Finding links:** None

**Printed values and method:**

```text
12 months 267/583 (45.8) 293/638 (45.9) 221/638 (34.6) 1.32 (1.15, 1.52) 1.33 (1.18, 1.48) 1.00 (0.91, 1.10)
```

**Pass-1 checks and result:** All three n/Npercentages andthree RR95%CIs checked. Count percentages match withinprecision, point containment/order hold, RR direction matchesproportions; displayedRR versusexplicitunadjusted ratio remaining gap≤.05 relative. No P printed, no variance/test reconstruction without GEE covariance. Differentdenominators acrossoutcomes reflectobservedoutcomes, not a shared stated denominator.

## S240 — Unadjusted continuous-change descriptive/inferential method

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
Medians(25%-tile,75%tile) forchanges frombaseline; between-groupMEANdifferences95%CIs fromlinear regression GEE;15outcome/timepointrows;omnibusP acrossarms.
```

**Pass-1 checks and result:** Median differences neednot equalmean model differences. Direction is coherent withhigher worsepainandhigher betterfunction. Footnote'meanchange' andmedianheader do not changeeffect-column meaning; screened context observationonce. P is omnibus;pairwise nonsignificanceHC/PT doesnotconflictwithsignificant overall test.

## S241 — eTable10 pain severity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa    -1.1 (-2.1, -0.1)     -1.1 (-2.3, -0.1)    -0.6 (-1.6, 0.2)   -0.4 (-0.6, -0.3) -0.4 (-0.6, -0.3) 0.0 (-0.2, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S242 — eTable10 pain severity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months     -1.3 (-2.5, -0.1)     -1.4 (-2.5, -0.2)    -0.8 (-1.8, 0.2)   -0.4 (-0.7, -0.2) -0.5 (-0.8, -0.3) -0.1 (-0.3, 0.1)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S243 — eTable10 pain severity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months    -1.3 (-2.5, -0.3)     -1.4 (-2.5, -0.2)    -0.8 (-2.2, 0.1)   -0.4 (-0.7, -0.2) -0.4 (-0.6, -0.2) 0.0 (-0.1, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S244 — eTable10 pain intensity 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa       -0.8 (-1.8, 0.0)   -0.8 (-2.0, 0.0)     -0.5 (-1.5, 0.2)   -0.3 (-0.5, -0.2) -0.3 (-0.5, -0.1) 0.0 (-0.1, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S245 — eTable10 pain intensity 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months        -1.0 (-2.0, 0.0)   -1.0 (-2.2, 0.0)     -0.8 (-1.5, 0.2)   -0.3 (-0.5, -0.1) -0.3 (-0.5, -0.2) -0.1 (-0.3, 0.1)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S246 — eTable10 pain intensity 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months       -1.0 (-2.2, 0.0)   -1.0 (-2.2, 0.0)     -0.8 (-2.0, 0.2)   -0.3 (-0.5, -0.1) -0.2 (-0.4, -0.1) 0.0 (-0.1, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S247 — eTable10 pain-related interference 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa    -1.3 (-2.4, -0.1)     -1.3 (-2.6, 0.0)     -0.7 (-1.9, 0.1)   -0.5 (-0.7, -0.3) -0.5 (-0.7, -0.3) 0.0 (-0.2, 0.2)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S248 — eTable10 pain-related interference 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months        -1.4 (-2.9, 0.0)   -1.6 (-2.9, -0.1)    -0.9 (-2.1, 0.1)   -0.6 (-0.8, -0.3) -0.6 (-0.9, -0.4) -0.1 (-0.4, 0.2)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S249 — eTable10 pain-related interference 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months    -1.6 (-3.0, -0.1)     -1.6 (-3.0, -0.1)    -1.0 (-2.6, 0.1)   -0.5 (-0.8, -0.3) -0.5 (-0.7, -0.3) 0.0 (-0.2, 0.3)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S250 — eTable10 social role functioning 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa        1.8 (-2.0, 5.8)   1.9 (-1.9, 6.0)      0.0 (-2.2, 4.3)     0.9 (0.1, 1.7)    1.5 (0.7, 2.2)   0.5 (-0.2, 1.3)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S251 — eTable10 social role functioning 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months         1.9 (-1.9, 6.5)   1.9 (-1.9, 7.4)      1.5 (-3.2, 5.5)     1.3 (0.4, 2.2)    1.7 (0.9, 2.6)   0.4 (-0.5, 1.4)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S252 — eTable10 social role functioning 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months        1.9 (-1.9, 7.5)   2.0 (-1.7, 7.7)      0.0 (-3.2, 5.8)     1.4 (0.4, 2.3)    1.4 (0.8, 2.1)   0.1 (-0.7, 0.8)     <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S253 — eTable10 physical functioning 3-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
3 monthsa        1.6 (-0.8, 3.6)   1.2 (-0.8, 3.8)      0.9 (-1.4, 3.2)     0.6 (0.1, 1.1)    0.8 (0.3, 1.2)   0.1 (-0.3, 0.6)     0.002
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S254 — eTable10 physical functioning 6-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
6 months         1.7 (-0.8, 4.4)   1.2 (-0.9, 4.4)      1.0 (-1.0, 3.6)     0.8 (0.3, 1.4)    0.5 (0.1, 0.9)   -0.3 (-0.8, 0.2)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S255 — eTable10 physical functioning 12-month complete outcome tuple

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.16](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=16)
- **Finding links:** None

**Printed values and method:**

```text
12 months        1.9 (-0.9, 5.0)   1.3 (-1.2, 4.6)      0.9 (-1.7, 3.6)     1.1 (0.5, 1.7)    0.8 (0.2, 1.5)   -0.3 (-0.9, 0.4)    <0.001
```

**Pass-1 checks and result:** All three median/IQRtriples,three mean-difference95%CIs andomnibusP reviewed. Medians inside ordered IQRs; every effect estimate inside an ordered CI; three contrast differences obey additive closure within half-unit precision. PairwiseCI excludes0 foractive/UC,includes0 forHC/PT; omnibus.002(physical3M)or<.001elsewhere consistentwithactive/UC evidence. No covariance supplied foromnibus reconstruction. Mean contrast is notdifference of medians.

## S256 — Complete workbook model-selection P-value family

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-006 worksheet eTable 3](../../../../joi250046supp5_prod_1755300121.16087.xlsx), H2:J108; A114
- **Finding links:** None

**Printed values and method:**

```text
Outcome/MissingAll/Missing3M selection headers H/I/J. FootnoteA114 boldmeansP<.10inbothprimary3M-MCIDandatleastonemissingnessmodelafterbase adjustment. All32 populated P cells:

| Cell | Stored value | Formula |
|---|---|---|
| H12 | 1.5599999999999999E-2 |  |
| J12 | 0.05 |  |
| H18 | <0.001 |  |
| I18 | 2.2800000000000001E-2 |  |
| J18 | 5.91E-2 |  |
| H20 | 1.8599999999999998E-2 |  |
| H39 | 6.3600000000000004E-2 |  |
| I39 | 1.9599999999999999E-2 |  |
| H41 | 5.2499999999999998E-2 |  |
| H43 | 5.7599999999999998E-2 |  |
| H45 | 3.0800000000000001E-2 |  |
| I47 | 2.0000000000000001E-4 |  |
| I51 | 1E-3 |  |
| H52 | 7.4099999999999999E-2 |  |
| H54 | 5.1000000000000004E-3 |  |
| H58 | 6.1499999999999999E-2 |  |
| H60 | 1.6999999999999999E-3 |  |
| H66 | 3.2300000000000002E-2 |  |
| H68 | 0.01 |  |
| H72 | <0.001 |  |
| H74 | <0.001 |  |
| H81 | <0.001 |  |
| I81 | 9.4999999999999998E-3 |  |
| H84 | 3.27E-2 |  |
| I84 | 3.3099999999999997E-2 |  |
| H87 | 1.0800000000000001E-2 |  |
| H100 | 4.9200000000000001E-2 |  |
| H101 | 4.9200000000000001E-2 |  |
| H102 | <.0001 |  |
| H105 | <.0001 |  |
| H108 | 2.4500000000000001E-2 |  |
| I108 | 4.0500000000000001E-2 |  |
```

**Pass-1 checks and result:** All populated Pvalues lie0–1or are valid upper bounds; H/I/J aredistinctselection tests, nottreatmentcomparisons. EmploymentH18<.001,I18=.0228,J18=.0591,PHQ8H81<.001/I81=.0095,GAD7H84=.0327/I84=.0331,SDOHH39=.0636/I39=.0196,PEGH108=.0245/I108=.0405meetdual weight selector. EducationH12=.0156,J12=.05 butI12blank; no numeric P asserted for a blank. Selectedweightmembership examinedS262. No estimate, SE, CI,test statisticprinted for these selection tests; no testreconstruction possible.

## S257 — Workbook completeness groups and sample implications

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-006 worksheet eTable 3](../../../../joi250046supp5_prod_1755300121.16087.xlsx), B3:E3; A110; DOC-005 eTable1 [DOC-005 PDF p.7](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** None

**Printed values and method:**

```text
Overall2331;MissingAll295;Missing1or2 468;AllObserved1568. FootnoteA110 excludesmissing from percentdenominator. Complete workbook descriptives mapped inreports_restart.
```

**Pass-1 checks and result:** 295+468+1568=2331;468+1568=2036. This agreesanalyticcohortandvisitrows; eTable1 correspondingone+two471differs3,screenedonceasdisplay precision withS202. Baselinecount-percentage checks are assigned to the numeric checker,not duplicated here. Prespecified adjustment flags G4,G10,G11,G38,G54,G80 anchorsbase variables.

## S258 — Adherence histogram method and direction

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.3](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=3)
- **Finding links:** None

**Printed values and method:**

```text
PT/VirtualCoach8-sessionhistograms;xticks0,2,4,6,8; proportions0,.2,.4,.6,.8,1.0. Unlabeledbars; visuallyapproximatePTfirst/last .38/.38,VC .18/.63.
```

**Pass-1 checks and result:** No P,CI ormodelclaim. Histogram definition and arms match the intervention dose; exact counts not recoverable without labels. Visualapproximationscannotbeusedasprinted valuesforquantitativediscrepancy. VC/HC terminology is resolved by context, one exclusion.

## S259 — Probability/weight diagnostic figure

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.10](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** None

**Printed values and method:**

```text
eFigure2 observed≥1followupgreenversusnoobservedfollowupsorange;leftestimatedresponseprobability,rightweight;unlabeled barsandfittedsmoothcurves.
```

**Pass-1 checks and result:** Observedresponsegroup higher predicted probability andlower weight coherently matchesinverseprobability weighting. Figureincludesnonsampledresponsegroup fordiagnostics; onlyany follow-upanalysiscontributesfinalweightsum2036. No exact bar counts or bin probabilitiesprinted; no inferential comparison claimed.

## S260 — TIDieR sampling, fidelity and intervention definitions

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-004 PDF pp.2–6](../../../../joi250046supp3_prod_1755300121.15087.pdf#page=2)
- **Finding links:** None

**Printed values and method:**

```text
HC12providers;8sessions45–60min/12weeks;PT8sessions30–45min/12weeks;fidelityplannedrandom5%first12months,onepercoach/6monthslater,thresholds100%content/80%CBT. Reviewed299=193training+89first12months+17later;8/2992.7%,11/2993.7%. Outreach356/77645.9%;extensionn14.
```

**Pass-1 checks and result:** All DOC-004 pages1–7read in the assigned fresh map. No inferential P, CI,statistical model,power calculationorstatistical stopping ruleinTIDieR. The fidelity sampling rule is descriptive protocol administration, not a trial decision rule; percentages reconcile. Intervention definitions support histogram identity; broadclinical or procedure auditnot performed.

## S261 — Education coding and coefficient attribution

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.7](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [DOC-005 PDF p.8](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), [DOC-005 PDF p.9](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=9)
- **Finding links:** F-ST1-204

**Printed values and method:**

```text
eTable2 selectededucation'anycollegevsHSdegreeorless';eTable3 printsAA−.02(−.11,.08),P.866;secondAA .16(.07,.25),P.077;graduate .39(.29,.49),P<.001;eTable4printsAA .97(.82,1.16),P.770;secondAA1.16(1,1.33),P.046;graduate1.35(1.13,1.61),P<.001.
```

**Pass-1 checks and result:** Onebinaryeducationfactorversusthreecategorycontrastsdoesnotidentifytheapplied model. Duplicated AA labels preventmatchingthetwo differentprinted estimates toonecategory, eventhoughworkbookdistinguishesassociate/college/graduate. Source-groundedRouteBobservationconsolidatedwithcoding discrepancy.

## S262 — Weight-model applied covariates versus final selected list

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.4](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.5](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [DOC-005 PDF p.7](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [DOC-005 PDF p.10](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10)
- **Finding links:** F-ST1-203

**Printed values and method:**

```text
eTable2 finalweightadditionPEG,PHQ8,GAD7,SDOH,education;allmodelbase variableslistdoesnotcontainemployment; eTable5weightcoefficientsincludeNotemployed1.49(1.11,2.00),P.008 andnoeducationrow.
```

**Pass-1 checks and result:** Explicitlistandcompletefitdisplaydisagreeonwhichadditional predictorsgeneratedtheweights. Different reference armUC/HCversusPTcan reparameterize the logistic model and is not a finding;the membership difference cannot be resolved by reference choice.

## S263 — Subset analysis model attribution

- **Status:** PASS_1_COMPLETE
- **Document role:** REPORT at every cited location.
- **Exact locations:** [DOC-005 PDF p.13](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=13), [DOC-005 PDF p.14](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14), [DOC-005 PDF p.4](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [DOC-005 PDF p.7](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7)
- **Finding links:** F-ST1-205

**Printed values and method:**

```text
Subsetnarrative'results oftheprimaryanalysisrestrictingtosubsets';primaryselectionstateseducationandemploymentaddedtoimputation/estimation;subsetfootnotelistsexclusivelysex,age,site, rural,morethan1condition,mentalhealth,baselineseverity.
```

**Pass-1 checks and result:** Subset point estimates are explicitly reported, but method mapping is unclear because the primary restricted fit and printed base set are different adjustments. This doesnot inferanythingfromabsenceofweightorimputationterms;onlytheexplicitcovariate lists compared.

## Scope limitations and no-applicable checks

No superiority decision based on an individual pairwise P outside the gated omnibus rule is reported in these assigned units. No noninferiority/equivalence margin, statistical interim/stopping boundary, power calculation, numeric standard error or numeric test statistic appears in the assigned supplement results. The source states two-sided tests and 95% CIs, but the coefficient-test family, degrees of freedom, coefficient-CI construction and full variance-covariance matrix are not provided: exact numeric P/statistic/SE reconstruction is not asserted. This does not limit CI-null/P-level or point-containment checks. Figures have unlabeled bars; no exact bin counts were extracted. Office conversion is unavailable, but direct cell structure provided exact stable locations. Scientific source-unit coverage gap: none; assigned source pages and workbook were completely mapped by the current fresh mapper and all result-relevant relationships were reviewed here.



