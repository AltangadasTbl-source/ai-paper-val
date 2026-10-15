# Complete checker excluded-observation packet

Literal sections from all canonical current checker outputs. Every original exclusion must be revisited independently during statistical pass2 and the final audit. This is a locator packet, not a new screening decision.


Source: checkers/numeric_consistency.md

## Excluded observations

Only apparent issues not emitted are listed. Reconciled arithmetic checks remain in the N inventory.

| Location | Observation | Reason code |
|---|---|---|
| Results supplement p.7 eTable 1; p.8 eTable 3; workbook D3 | Pattern counts 188+283+1568=2039 versus 2036 any follow-up; PT644 vs 643,HC692 vs 690; weighted pattern visits 5458 versus observed 5449; corresponding 650 versus 659 missing. Even nonoverlapping input/output precision leaves relative gaps below 0.05. Example 5458 sum interval[5455,5461] versus observed[5447.5,5450.5], gap 4.5/5449=.000826. Workbook D3=468 also differs from 188+283=471 by a relative gap below 0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Main baseline/narrative versus workbook baseline copies | Female 1712 versus 1713; current-depression 47.8%versus 47.9%; numerous differences in copied descriptives remain below 0.05 after precision and/or refer to subgroup-qualified summaries. These are distinct from the within-cell E82 finding. | ROUNDING_OR_DISPLAY_PRECISION |
| Main Table 2/eTables 7–8 other reciprocal NNT point rows | Small integer NNT deviations remaining after half-units have relative gaps at most 0.05. Example main intensity 3 mo PT−UC rates 24.3−17.7 gives[14.925373,15.384615], printed 16 interval[15.5,16.5], gap.115385/16=.007212. Four SMD additive rows also meet the precision rule and are retained in the inventory. | ROUNDING_OR_DISPLAY_PRECISION |
| Results supplement pp.16–18 eTables 10/11 | Subtracting printed group medians/IQR to reproduce model-based mean differences assumes medians are model means; no such equality is stated. Statistical questions about source headings are reviewed separately. | CONDITIONAL_OR_UNREPORTED |
| Intervention supplement p.6 fidelity denominators |1791+2350=4141 versus total 4626. Training reviewed count 193 is supplied, but total training-session denominator is not supplied; an unreported 485-session component could explain the partition. Reviewed counts 193+89+17 do sum 299. | CONDITIONAL_OR_UNREPORTED |
| Main methods/Table 2/Table 3 and results supplement pp.5/7–10 |2331 randomized target population versus 2036 any-follow-up contributors, weight sum 2036 persons/6108 visits, and observed-at-time counts are explicitly different quantities under the reported nonresponse weighting/imputation. | CONTEXT_RESOLVES |
| Main p.8/p.12 Discussion residence description |Roughly 40% rural/underserved versus 44% elsewhere is an explicitly approximate narrative description, not a replacement numeric extraction for the baseline 44% result. | CONTEXT_RESOLVES |




Source: checkers/cross_source_consistency.md

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




Source: checkers/statistical_pass_1.md

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.10, Table 3 severity 6 months, SMDs −0.26/−0.36/−0.12 | Shared-SD additivity predicts HC–PT [−0.110,−0.090], printed half-unit [−0.125,−0.115]; gap .005/.12=.0417. MD/SMD shared-denominator rounding discrepancy is likewise below .05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.7 secondary narrative vs p.10 severity 3-month SMD row | Narrative −0.26/−0.36 vs table −0.25/−0.34: half-unit gaps0/.010, relative0/.0294. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.10 physical functioning 6-month omnibus P=.05 and footnote p.11 pairwise gate P<.05 | The printed P rounding interval[.045,.055] includes values that satisfy the stated gate; exact unrounded gate result cannot be determined. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.4 Sample Size | Exact 90% simulated power cannot be rebuilt without the complete simulation specification; 2331=777×3,7.5 percentage points andRR1.5 reconcile, with no contradicted sample size. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p.11 Table 3 PGIC headings/footnotes | Mean change label versus a since-start-of-study global-impression scale: scale coding and outcome meaning are evident from adjacent footnotes. | TERMINOLOGY_OR_WORDING |
| REPORT main p.3 primary scoring and p.7 Table1 footnote g | Requirement of all4 intensity and at least4/7 interference items versus mean of11-item instrument wording does not establish a conflicting reported score. | TERMINOLOGY_OR_WORDING |
| REPORT main pp.1,7 secondary benefit narrative vs physical-function rows p.10 | Overall-pattern statements summarize benefits while individual physical-function contrasts vary in null coverage; whether wording means every contrast is not established. | TERMINOLOGY_OR_WORDING |




Source: checkers/statistical_pass_1.md

## Excluded observations

Only apparent issues decided against emission are listed; checks that reconcile remain in the S records.

| Location | Observation | Reason code |
|---|---|---|
| DOC-005 PDF p.7, eTable 1 completeness patterns; DOC-006 eTable 3 B3:E3 | Pattern counts 188+283+1568=2039 versus any-followup 2036; PT 644 vs 643 and HC 692 vs 690; implied visits 5458 vs 5449; workbook missing 1-or-2 is 468 versus 188+283=471. Half-unit pattern-total interval [2037.5,2040.5] versus [2035.5,2036.5] leaves gap 1/2036=.000491; visit totals [5455,5461] versus [5447.5,5450.5] leave gap 4.5/5449=.000826; the workbook comparison [470,472] versus [467.5,468.5] leaves gap 1.5/468=.003205. All are ≤.05; arm-total intervals overlap. The pattern is listed once. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-005 PDF pp.11/14, eTables7–8, other NNT point estimates | All44 reciprocal NNT comparisons other than F-ST1-206 either overlap under half-unit input/output intervals or have remaining relative gaps≤.05. Largest excluded gap: reminder-letter6M HC/UC NNT6 versus reciprocal[5.154639,5.208333], printed[5.5,6.5], relative.048611. Other apparent NNT differences are one consolidated display-precision pattern. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-005 PDF p.8, eTable3, quantitative CI-width/P diagnostics beyond the seven null conflicts | A normal-Wald diagnostic SE=(upper−lower)/(2×1.96), then two-sided P from estimate/SE, yields differences for additional rows (for example Time6M estimate.13,CI.07–.19 gives diagnostic z4.247 and Pabout.000022 versus.025). Coefficient-test family, degrees of freedom and interval construction are not stated; a specific exact numerical test cannot be established. The seven direct CI-null/P conflicts remain emitted separately as F-ST1-201. | CONDITIONAL_OR_UNREPORTED |
| DOC-005 PDF p.8, eTable3, arm coefficients versus improvement direction | Positive imputation coefficients cannot alone be interpreted as worse clinical response without a supplied sign convention for the imputation change, the missingness-pattern conditioning and the complete covariate context. No direct printed direction statement for these conditional coefficients conflicts. | CONDITIONAL_OR_UNREPORTED |
| DOC-005 PDF pp.5/9/10, weight normalization description and sums | “Scaled to the study sample size” could be read as2331 rather than2036, but eTable6 explicitly sums to2036, eTable4 to3×2036=6108, and imputation is among any-followup participants. These immediate displays identify the analysis sample for the scaling statement. | CONTEXT_RESOLVES |
| DOC-005 PDF p.7, eTable2 all-model list versus pp.4/8/9 | Baseline pain severity is omitted from eTable2's base-variable list, but the adjustment narrative and both complete primary model displays explicitly include it. Its applied inclusion is immediately identifiable and the omission changes no extractable coefficient assignment. | CONTEXT_RESOLVES |
| DOC-005 PDF p.15, eTable9 title | Title says “adjusted relative risk,” but the page explicitly says no adjustment, weighting or imputation, the coefficient heading says Relative Risk, and footnote b says “without adjustment.” The intended unadjusted analysis is immediately identified; point estimates also agree with the unadjusted proportions. | TERMINOLOGY_OR_WORDING |
| DOC-005 PDF p.16, eTable10 descriptive median heading versus mean-effect footnote | Group medians/IQRs do not need to reproduce between-group mean differences. The effect columns explicitly name means and95%CIs, while the descriptive columns name medians/IQRs; this distinction identifies the quantities a reader extracts. No direct numeric contradiction is established. | CONTEXT_RESOLVES |
| DOC-005 PDF p.3, eFigure1 Virtual Coach/VC labels | Virtual Coach names the Health Coach intervention in the surrounding three-arm trial context; no numeric result is attributed to a different intervention. | TERMINOLOGY_OR_WORDING |




Source: checkers/statistical_pass_1.md

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC-002 PDF p.55, section15.1 and subgroup power table; PLAN DOC-003 PDF p.16, section5; REPORT DOC-001 PDF p.4, Sample Size, selectively read as context | A simple independent-proportion normal diagnostic yields567.072/arm rather than621; continuity-correction diagnostic593.439/arm. Subgroup diagnostics also depend on routine. Neither normal algorithm is stated; the REPORT explicitly describes10,000 modified-Poisson simulations. The necessary simulation inputs and success definition are absent, and no chosen diagnostic is established as a method reproducing other rows of this display. This is an approximation-dependent observation rather than reproduced stated-method conflict. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 PDF p.55; PLAN DOC-003 PDF p.16, narrative and power table | “Relative change150%” and the subgroup “Relative Change” values206.7/184.7/172.0% are explicitly defined by the table as active/UC ratio. Values and arithmetic reconcile; the label versus percentage-increase terminology does not change the available ratio or response rates. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 PDF p.22 and DOC-003 PDF p.11, binary interference responder row, brief-description cell | The description uses “pain intensity” while the row label and same sentence explicitly specify the7-item interference subscale and30% reduction. The intended scale is evident in that row. No printed number, composite definition or actual outcome status changes. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 PDF p.22 and DOC-003 PDF p.11, both binary subscale rows, measurement and timeframe cells; corroborating PLAN DOC-002 p.57/DOC-003 p.21 | Measurement cells list baseline,6,12-months while the immediately adjacent timeframe cells explicitly include primary baseline-to-3-months. The same displays identify the3-month analysis; subsequent analysis text confirms3-month primary time for secondary outcomes. No outcome is absent from the supplied plan and no numerical result conflicts. | CONTEXT_RESOLVES |
| PLAN DOC-002 PDF p.25, moderator introduction, versus pp.57–58, section15.7; PLAN DOC-003 pp.14,22 | Protocol table relates moderators to6-month severity MCID; analysis paragraph identifies3-month interaction comparison, and SAP says primary outcome/3-months. This is an ancillary plan-internal moderator-time comparison without a reported subgroup result in the current REPORT map. It does not alter the trial's primary3-month severity definition or sample size; planned-versus-reported omission/status screening is separately assigned to the cross-source checker. | PERIPHERAL_COMPARISON |
| PLAN DOC-003 PDF p.23, Step3a narrative, equation and inverse-probability weights | Narrative mentions baseline-confounder adjustment while the displayed logistic equation and weights show selected mediators without a Z term. The difference concerns the ancillary mediation method, for which no fitted mediation result is reported in the current REPORT map. It has no supplied numerical effect on primary/key-secondary results, population size or primary decision rule. Planned-versus-reported mediation omission/status screening is separately assigned. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 PDF pp.27,47,58; PLAN DOC-003 PDF pp.15,22–23 | Mediation prose says baseline-to-3-month changes for all three mediators, but perceived support is explicitly collected at notification of randomization and3-months. Protocol p.47 expressly says the notification survey serves as baseline potential mediator; the intended origin is stated. | CONTEXT_RESOLVES |
| PLAN DOC-002 PDF p.5 amendment history versus p.32 current eligibility; PLAN DOC-003 PDF pp.3,17 | Protocol history says two pain encounters at least30-days apart; current protocol/SAP eligibility says>60 days and SAP amendment specifies60 days. The history/current comparison does not demonstrate a changed actual effectiveness-population size, primary/key-secondary result or decision rule. Actual reported eligibility/population matching remains assigned cross-source scope. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 PDF p.61, qualitative frameworks section16 | RE-AIM/TFA component/domain count descriptions differ from the named list lengths. These framework descriptions do not represent trial participant/event counts, power inputs or statistical result/decision quantities. They fall outside the four quantitative focus areas. | OUT_OF_FOCUS |
| PLAN DOC-002 PDF p.50, systematic SAE review description; PLAN DOC-003 PDF p.3 amendment and p.26 current safety text, with SAP precedence p.10 | Routine hospitalization chart-review differs between protocol and current SAP, but the SAP amendment explicitly removes it and current text preserves death review and conditional hospitalization review. This is a disclosed procedural update; event definitions and the stated descriptive safety analysis remain clear. | CONTEXT_RESOLVES |

Source evidence: [DOC-002 p.55](../../../joi250046supp1_prod_1755300121.14087.pdf#page=55), [DOC-003 p.16](../../../joi250046supp2_prod_1755300121.15087.pdf#page=16), [DOC-001 p.4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [DOC-002 p.22](../../../joi250046supp1_prod_1755300121.14087.pdf#page=22), [DOC-003 p.11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=11), [DOC-002 p.25](../../../joi250046supp1_prod_1755300121.14087.pdf#page=25), [DOC-002 p.58](../../../joi250046supp1_prod_1755300121.14087.pdf#page=58), [DOC-003 p.23](../../../joi250046supp2_prod_1755300121.15087.pdf#page=23), [DOC-002 p.47](../../../joi250046supp1_prod_1755300121.14087.pdf#page=47), [DOC-003 p.15](../../../joi250046supp2_prod_1755300121.15087.pdf#page=15), [DOC-002 p.5](../../../joi250046supp1_prod_1755300121.14087.pdf#page=5), [DOC-002 p.32](../../../joi250046supp1_prod_1755300121.14087.pdf#page=32), [DOC-003 p.3](../../../joi250046supp2_prod_1755300121.15087.pdf#page=3), [DOC-003 p.17](../../../joi250046supp2_prod_1755300121.15087.pdf#page=17), [DOC-002 p.61](../../../joi250046supp1_prod_1755300121.14087.pdf#page=61), [DOC-002 p.50](../../../joi250046supp1_prod_1755300121.14087.pdf#page=50), [DOC-003 p.26](../../../joi250046supp2_prod_1755300121.15087.pdf#page=26), [DOC-003 p.10](../../../joi250046supp2_prod_1755300121.15087.pdf#page=10).




Source: checkers/statistical_pass_1.md

## Excluded observations

Only apparent issues decided not to emit are listed here. Reconciled checks are recorded in the S inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-005p17 PGIC remaining fractional raw centers: Pain PT3=2.9,UC3=1.9,HC6=2.1,UC6=2.1,HC12=2.1; General UC3=1.6,PT12=2.6,HC12=1.9,UC12=1.9 | These centers also fall between eligible ordinary single-item medians, but their half-unit interval gaps to the nearest eligible median are0.05 and relative discrepancies range0.0172–0.0313, at most0.05. These occurrences are outside the five-location finding under the display-precision rule. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-005p17 all21 raw-summary/contrast rows, p15 intro, p18 note b | Subtracting raw centers under printed PT/HC/UC headings differs from many GEE mean contrasts. A diagnostic UC/PT/HC permutation of raw columns makes all21 contrast triples feasible within one-decimal rounding. However the raw centers explicitly represent medians and the contrasts model means; no supplied method establishes equality between the two. This numerical permutation alone does not reproduce an arm-label or mean-difference inconsistency. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-005p17 physical functioning6/12months omnibusP=.005/.001; contextual DOC-001p11 footnote c and DOC-005p15 intro | A diagnostic same-covariance normal-CI, joint two-contrast Wald reconstruction matches social3 and physical3 Ps within rounding but yields physical6 approximateP=.015–.040 and physical12 approximateP=.0036–.020. eTable11 does not specify its exact omnibus reference distribution/degrees of freedom, normal-versus-t CI rule, or whether omnibus and CIs use the same fitted covariance. An exact conflict cannot be asserted by importing these choices from convention or another display; no null/significance contradiction exists at .05. | CONDITIONAL_OR_UNREPORTED |


