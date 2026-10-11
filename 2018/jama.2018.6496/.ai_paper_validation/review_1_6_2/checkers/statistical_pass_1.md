# Statistical consistency review — pass 1

Runtime agent: /root/statistics_one. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Status: COMPLETE.

Exact scope: the complete 49-page package, through both complete extraction maps: all 73 main MS relationships and 33 applicable support relationships, canonical S001–S106. The canonical inventory enumerates every ID and records PASS_1_COMPLETE for each. Every inferential row in Tables 2, 3 and 5 and eTable 1 includes its arm intervals, difference interval, P value and any interaction P. Design, sample-size, missingness, censoring, clustering, superiority, interim and plan/report rules are included. Reference/background and unpopulated form quantities were inspected for applicability, without treating them as trial results.

Authority and tools: exact supplied PDFs, direct Poppler 25.03.0 pdftotext -layout reads and source-linked reusable images for Table 2 and Table 3; CPU, no new rendering/OCR, no source mutation. Both complete maps, QUALITY_CONTROL_SCOPE.md and the complete review contract were read. No prior review conclusions or external evidence were used. Arithmetic diagnostics below are explicitly labeled; no unstated variance, degrees of freedom, interaction model, covariance or estimand was assumed as the reported method.

## Findings

### F-ST1-001

**Title:** Three significant process tests accompany printed 95% intervals reaching zero.

**Relationships:** S019, S020, S027; primary S_W; all relationships S_W. **Focus area:** B. **Proposed review domain:** statistical_results.

**Locations and roles:** REPORT [main PDF p.6, Table 2, senior resident/fellow, junior resident, and screen viewed during passage rows](../../../jama_driver_2018_oi_180054.pdf#page=6); REPORT [p.4 statistical methods](../../../jama_driver_2018_oi_180054.pdf#page=4).

**Printed values:** Senior operator: 318/381 versus 334/376, difference −5 percentage points (95% CI −10 to 0), P=.03. Junior operator: 57/381 versus 37/376, difference 5 (0 to 10), P=.03. Video during passage: 75/377 versus 98/372, difference −6 (−12 to 0), P=.04. Methods specify chi-square binary tests, 95% CIs and two-sided .05.

**Rule and calculation:** Each printed closed interval includes the zero difference while its printed P is below .05. This is the reverse of the interval/test compatibility rule. A diagnostic unpooled normal interval computed from the counts gives respectively [−10.270,−0.461], [0.441,9.799], and [−12.473,−0.427] percentage points. Diagnostic Pearson P values are .03273, .03269 and .03624. These diagnostics explain how rounding nonzero endpoints to whole points could produce the display, but are not asserted to be the reported interval method. Half-unit endpoint intervals around the printed zero are [−0.5,0.5]; the display-precision exemption in route A category 1 applies, so no relative-discrepancy cutoff is used to exclude the printed interval/test conflict.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** Significance and interval endpoints for the three process differences.

**Why context does not resolve it:** Route A category 1 explicitly requires registration of a printed interval/test conflict even when rounding or different inferential constructions might explain it. The repeated zero-endpoint pattern is consolidated into one finding.

**Alternatives and missing definition:** Unrounded limits may exclude zero, as the diagnostic suggests; alternatively the CI and test may use different constructions. Exact interval construction and unrounded limits are absent.

**Human question:** What are the unrounded confidence limits and interval constructions for these three rows, and how should their displayed zero endpoints be read alongside P=.03/.03/.04?

### F-ST1-002

**Title:** Grade-4 success difference interval excludes zero although its test is nonsignificant.

**Relationships:** S049; primary S_W; all relationships S_W. **Focus area:** B. **Proposed review domain:** statistical_results.

**Locations and roles:** REPORT [main PDF p.7, Table 3, Cormack–Lehane Grade 4](../../../jama_driver_2018_oi_180054.pdf#page=7); REPORT [p.4 methods](../../../jama_driver_2018_oi_180054.pdf#page=4).

**Printed values:** Bougie 3/3, 100% (95% CI 29 to 100); tube 2/5, 40% (5 to 85); difference 60 (95% CI 17 to 100), P=.09, interaction P=.78. Confidence level 95%, two-sided test level .05.

**Rule and calculation:** The difference interval [17,100] excludes zero but .09>.05. The estimate lies within its interval and the endpoints are ordered, so this finding concerns CI/test compatibility specifically. Diagnostic independent unpooled normal calculation gives 60±1.96×sqrt(0+(.4×.6)/5)×100=[17.059,102.941], which could be capped at 100; diagnostic Pearson chi-square gives P≈.08969. Those different constructions can explain the display but do not remove a route A category 1 finding. Half-unit lower-limit interval [16.5,17.5] remains strictly positive; P half-unit interval [.085,.095] remains above .05. No relative-discrepancy cutoff applies to category 1.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** Grade-4 first-attempt success contrast, particularly whether its uncertainty supports a nonzero difference.

**Why context does not resolve it:** This is an always-register interval/test conflict; the interaction P concerns a different hypothesis and is not a remedy.

**Alternatives and missing definition:** CI and P may intentionally use different inferential constructions; the actual difference-CI method is not named. The diagnostic is an explanation, not a proposed replacement analysis.

**Human question:** Which confidence-interval method produced 17% to 100%, which test produced P=.09, and how should their divergent zero-difference conclusions be interpreted?

### F-ST1-003

**Title:** All-patient duration interval limits are printed in descending order.

**Relationships:** S040, S097; primary S_W; all relationships S_W, S_C. **Focus area:** B. **Proposed review domain:** statistical_results.

**Locations and roles:** REPORT [main PDF p.7, Table 3, all-patient first-attempt duration](../../../jama_driver_2018_oi_180054.pdf#page=7); REPORT [supplement PDF p.2, eTable 1, corresponding duration](../../../joi180054supp2_prod.pdf#page=2); REPORT [main p.4 methods](../../../jama_driver_2018_oi_180054.pdf#page=4).

**Printed values:** Main medians 38 (IQR29–51) and 36 (25–54) seconds, Hodges–Lehmann difference 1 (95% CI 4 to −1) seconds, P=.24. Clustering display prints corresponding difference 1 (−1 to 4) seconds, P=.95, with adjustment disclosed.

**Rule and calculation:** A lower-to-upper interval requires L≤U; printed L=4>−1=U. Half-unit limits [3.5,4.5] and [−1.5,−0.5] cannot reverse the ordering: the minimum gap is 4 seconds, a relative gap of 4/4=1 against the first printed endpoint. This exceeds .05. Point estimate 1 lies between the unordered endpoints but not in a lower-to-upper reading of the printed interval. The supplement corroborates a possible reordered reading; its changed P is explicitly a clustering analysis and is not a cross-source P conflict.

**Qualifying route:** Route B.

**Affected result or extracted value:** Lower and upper 95% confidence limits for the all-patient first-attempt duration difference.

**Why context does not resolve it:** The printed lower and upper positions determine extracted fields; a reader must choose whether the limits were transposed or another signed result was intended. The intended order may be reconstructed but the numeric endpoint positions remain inconsistent.

**Alternatives and missing definition:** The two limits may have been transposed. A descending interval convention would need explicit definition; other rows use ascending order. No patient-level times are supplied to reconstruct the Hodges–Lehmann result.

**Human question:** Which limit is the lower and which is the upper 95% confidence limit for this duration difference?

### F-ST1-004

**Title:** Planned cuff-inflation time endpoint is replaced by blade-removal duration.

**Relationships:** S037, S040, S065, S067, S070, S071, S076, S094, S097, S099, S100; primary P_R; all relationships P_R. **Focus area:** D. **Proposed review domain:** protocol_report.

**Locations and roles:** PLAN [protocol p.9 §2.2(2), lines315–317](../../../joi180054supp1_prod.pdf#page=9), [p.10 §3.2 lines346–347](../../../joi180054supp1_prod.pdf#page=10), [p.19 §8.1 lines657–659](../../../joi180054supp1_prod.pdf#page=19); REPORT [main p.3 outcome duration definition](../../../jama_driver_2018_oi_180054.pdf#page=3), [p.7 Table3 duration rows and note c](../../../jama_driver_2018_oi_180054.pdf#page=7), [p.8 Figure2](../../../jama_driver_2018_oi_180054.pdf#page=8), [supplement pp.2–4 duration definitions/results](../../../joi180054supp2_prod.pdf#page=3).

**Printed statements:** Protocol defines secondary time to intubation, first attempt only, from attempt beginning to inflation of the ETT cuff with tube in trachea; stopwatch refers to that definition. Report defines first-attempt duration from blade insertion to blade removal and labels these results planned secondary outcomes. Medians include difficult subgroup39 versus40 seconds and overall38 versus36 seconds. Reported KM/Cox analyses also analyze first-attempt duration/success, without a separately identified cuff-inflation endpoint result. Planned KM summaries include 25th/50th/75th percentiles with 95% CIs and percent censored; no separate such cuff-inflation summaries appear.

**Rule and calculation:** Cuff inflation and blade removal are different endpoint events; the supplied text does not state that their timestamps coincide. The planned secondary time endpoint appears in the abstract's secondary scope but no result is explicitly assigned its planned definition. This is a logical endpoint/analysis comparison, not rounding or a recomputation of medians.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Which duration endpoint is represented by the planned-secondary medians, differences and time-to-success analyses.

**Why context does not resolve it:** Route A category 5 applies to a replaced planned analysis/outcome. The result cannot be assigned to the cuff-inflation endpoint solely by treating two distinct events as synonyms.

**Alternatives and missing definition:** A disclosed operational amendment or timing convention could reconcile the definitions, but none is supplied. Blade removal could occur close to cuff inflation, but equality is not documented.

**Human question:** Was the planned cuff-inflation time endpoint amended to blade-removal duration, and which reported result represents the originally specified endpoint?

### F-ST1-005

**Title:** Hypoxemia observation window ends relative to different events in plan and report.

**Relationships:** S036, S039, S054, S075, S078, S079, S099; primary P_R; all relationships P_R. **Focus area:** D. **Proposed review domain:** protocol_report.

**Locations and roles:** PLAN [protocol p.9 §2.2(1)/(4), lines304–325](../../../joi180054supp1_prod.pdf#page=9) and [p.10 §3.2 lines340–354](../../../joi180054supp1_prod.pdf#page=10); REPORT [main p.3 measurement window](../../../jama_driver_2018_oi_180054.pdf#page=3), [p.7 Table3 note b](../../../jama_driver_2018_oi_180054.pdf#page=7), [p.9 Table5 note b](../../../jama_driver_2018_oi_180054.pdf#page=9), [supplement p.3 note](../../../joi180054supp2_prod.pdf#page=3).

**Printed statements:** Plan records hypoxemia from first-attempt beginning until one minute after ETT cuff inflation; report records during or within one minute after completion of the intubation attempt, defined by blade removal. Thresholds <90%, or >10% absolute decrease when starting <90%, otherwise agree. Reported hypoxemia is47/371 versus50/364; success-without-hypoxemia is156/191 versus123/177 in the primary subgroup and317/371 versus282/366 overall.

**Rule and calculation:** The endpoint event anchoring the one-minute window differs. No statement equates cuff inflation to completion/blade removal, and a failed first attempt need not have cuff inflation. This concerns an explicitly defined component of planned secondary outcomes. No numerical rounding calculation applies.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Hypoxemia and first-attempt-success-without-hypoxemia outcome definitions and extracted event counts.

**Why context does not resolve it:** An always-register planned composite/window difference remains despite identical thresholds; a data extractor cannot assume event times coincide.

**Alternatives and missing definition:** An operational amendment may have changed the window or equated the timing anchors. No event-time mapping or amendment is supplied.

**Human question:** Which observation window was applied to hypoxemia and its composite outcome, and how does it map to the cuff-inflation window in the supplied protocol?

### F-ST1-006

**Title:** Interim display uses all enrolled patients although the specified analysis is primary-subgroup only.

**Relationships:** S069, S083, S090, S101; primary P_R; all relationships P_R. **Focus area:** D. **Proposed review domain:** protocol_report.

**Locations and roles:** PLAN [protocol p.20 §8.4.1/8.5, lines693–706](../../../joi180054supp1_prod.pdf#page=20), [p.21 §8.6.2, lines730–741](../../../joi180054supp1_prod.pdf#page=21), quoted PLAN [supplement p.6 interim specification](../../../joi180054supp2_prod.pdf#page=6); REPORT [same supplement p.6 observed interim analysis](../../../joi180054supp2_prod.pdf#page=6), [main p.3 primary population](../../../jama_driver_2018_oi_180054.pdf#page=3).

**Printed values/statements:** Primary analysis is the any-difficult-airway subset. Interim data are to be analyzed for the primary outcome only after500 enrolled. After507 enrolled the appendix displays250/257 (97%) bougie and213/250 (85%) tube;257+250=507, the complete enrolled interim cohort. It reports continuation using the projected1000-patient assumptions.

**Rule and calculation:** Display denominators account for all507 enrolled, rather than an identified difficult-airway subset; the publication explicitly treats all-enrolled first-attempt success as secondary. Both source roles occur on p.6 and are classified by content. Diagnostic projected arm rates using the disclosed rule are (250+243)/500=.986 and .852, yielding an absolute difference .134; this supports a nonfutility direction for the displayed overall cohort but does not establish the decision for the planned primary subgroup. Exact subgroup denominators/results and exact projected test are absent.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Interim primary outcome analysis population and the basis of the futility continuation decision.

**Why context does not resolve it:** The planned primary and secondary populations are explicitly distinct; no primary-subgroup interim result is provided. The all-patient continuation calculation does not substitute for that result.

**Alternatives and missing definition:** The displayed overall rates might supplement an unreported primary-subgroup calculation; an amendment might have revised the interim population. The interim subgroup distribution, exact test and any amendment are absent.

**Human question:** Was the futility decision based on difficult-airway primary-subgroup data or all507 enrolled patients, and what primary-subgroup result or amendment supports that choice?

### F-ST1-007

**Title:** Planned and reported accrual stopping rules differ.

**Relationships:** S063, S086; primary P_R; all relationships P_R. **Focus area:** D. **Proposed review domain:** protocol_report.

**Locations and roles:** PLAN [protocol p.19 §8.2 lines667–674](../../../joi180054supp1_prod.pdf#page=19); REPORT [main p.3 sample-size/stopping paragraph](../../../jama_driver_2018_oi_180054.pdf#page=3) and [p.1 study interval](../../../jama_driver_2018_oi_180054.pdf#page=1).

**Printed statements:** Plan enrolls for1 calendar year or1000 patients, whichever first, discussing extension if fewer than374 difficult-airway patients. Report says difficult-airway count was monitored and trial stopped when more than374 were enrolled. Final population380 difficult/757 overall, September2016–August2017.

**Rule and calculation:** A count-triggered rule >374 is not the same as a calendar-year/1000 maximum rule. Actual accrual can satisfy both, so this finding does not assert that the observed termination date contradicts the plan; it records the explicit statistical stopping-rule descriptions. No rounding applies to categorical rules.

**Qualifying route:** Route B.

**Affected result or extracted value:** The accrual rule governing the primary-subgroup sample size and precision.

**Why context does not resolve it:** Report does not state whether the count threshold supplemented, replaced or happened to coincide with the planned limit. The decision rule, rather than a recruitment-date copy, is in scope.

**Alternatives and missing definition:** The thresholds could have been reached at the same time, or a supplied-plan version may predate an amendment. No amendment or joint stopping-rule statement is supplied.

**Human question:** Did the difficult-airway count threshold replace or supplement the calendar-year/1000-patient rule, or were both termination criteria satisfied concurrently?

### F-ST1-008

**Title:** Facial/neck trauma is present in the planned randomization stratum but absent from the reported stratum.

**Relationships:** S062, S081; primary P_R; all relationships P_R. **Focus area:** D. **Proposed review domain:** protocol_report.

**Locations and roles:** PLAN [protocol p.11 §4.1.1 lines373–378](../../../joi180054supp1_prod.pdf#page=11); REPORT [main p.3 randomization paragraph](../../../jama_driver_2018_oi_180054.pdf#page=3).

**Printed statements:** Plan stratum1 includes any cervical collar, gestalt obesity, or apparent facial/neck trauma; stratum2 none. Report stratum1 includes obesity or cervical immobilization; stratum2 neither. Equal allocation and random block sizes2/4/6/8/10 agree.

**Rule and calculation:** The allocation rule for a patient with facial/neck trauma and neither obesity nor cervical immobilization differs under the two descriptions. This is a planned-versus-reported statistical-design stratification element, not a sites/calendar comparison. No rounding calculation applies.

**Qualifying route:** Route B.

**Affected result or extracted value:** The randomized allocation strata governing the primary and secondary contrasts.

**Why context does not resolve it:** The report does not identify an amendment or state that all trauma patients also met another stratification criterion. The intended rule cannot be determined from the supplied descriptions.

**Alternatives and missing definition:** A pretrial operational amendment could have removed trauma or the report could abbreviate a fuller rule. No such mapping is supplied; no inference about imbalance or treatment effects is made.

**Human question:** Which stratification rule was implemented, and was facial/neck trauma removed by an amendment or merely omitted from the report description?

### F-ST1-009

**Title:** Protocol primary missing-data recovery names the success-without-hypoxemia composite.

**Relationships:** S074, S075, S083, S089; primary P_P; all relationships P_P. **Focus area:** D. **Proposed review domain:** plan_material.

**Locations and roles:** PLAN [protocol pp.8–9 §2.1/2.2](../../../joi180054supp1_prod.pdf#page=9), [p.20 §8.4.1 and §8.6.1 lines719–720](../../../joi180054supp1_prod.pdf#page=20), [p.21 §8.6.1 lines721–722](../../../joi180054supp1_prod.pdf#page=21).

**Printed statements:** Primary outcome is first-pass success in the difficult-airway analysis subgroup. First-pass success without hypoxemia is secondary. Under “For the primary outcome,” missing both forms triggers video review to determine whether first-pass success without hypoxemia was achieved; absent video leads to exclusion.

**Rule and calculation:** The missing-data recovery instruction for the primary endpoint names the separately defined secondary composite, so its written success criterion adds absence of hypoxemia. This is a source-grounded difference in the primary analysis specification, not an assumption about a particular patient's classification. No rounding applies.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The planned primary-outcome ascertainment criterion when both case forms are absent.

**Why context does not resolve it:** Route A category 5 requires a composite-definition/analysis difference to be registered. The surrounding text distinguishes primary success from the secondary composite, but does not explicitly state whether the additional hypoxemia requirement applies only to recovered records.

**Alternatives and missing definition:** The recovery sentence may intend primary success only or recovery of both endpoints. Report has no missing primary outcomes, so this does not assert any reported patient's primary classification changed. The question concerns the written plan's primary-analysis pathway.

**Human question:** In the primary missing-data pathway, was video intended to ascertain first-pass success alone or success without hypoxemia, and how was the primary endpoint to be derived from that review?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Main p.7 Table3 durations; p.4 methods; supplement p.3 note | Median38 minus36 is2 while reported difference is1; a Hodges–Lehmann difference need not equal the difference of the two medians. | MODEL_VERSUS_CRUDE |
| Main p.4 clustering sensitivity; supplement pp.2–3 eTable1 | Recalculating adjusted CIs/P from crude arm ratios lacks the stated cluster procedure, covariance and variance estimator; no independent printed conflict is present. | CONDITIONAL_OR_UNREPORTED |
| Main pp.4–5 interaction tests; Table3; supplement eTable1 | No interaction model/scale, statistic, degrees of freedom or covariance is specified; significance .04 for grade1 is a different hypothesis than its within-grade P=.07. Missing method details alone do not establish a conflict. | CONDITIONAL_OR_UNREPORTED |
| Main pp.5,8–10 Cox/PH discussion; supplement p.4 | PH nonproportionality is disclosed and interpretation limited; proposing another time-to-event method would question an acknowledged, stated analysis choice. | OUT_OF_FOCUS |
| Main p.9 “similar” all-patient duration and complication frequency | Descriptive similarity/nonsignificance does not assert a formal equivalence or noninferiority result; no margin or such test is claimed. | TERMINOLOGY_OR_WORDING |
| Protocol p.11 aim “more than9%”; p.19 sample size; main p.3 | Treating9% planning effect as a formal null margin would impose an unstated hypothesis; the plan specifies a standard two-group test, not a9% superiority-margin decision. | TERMINOLOGY_OR_WORDING |
| Main p.3 esophageal outcome; Table5; protocol p.9 §2.2(3) | The main article does not reprint the ventilation/removal condition; no reported statement explicitly conflicts with the detailed plan definition. | CONDITIONAL_OR_UNREPORTED |
| Prospective form supplement p.13 versus main Table5 | Unpopulated cardiac-arrest/death capture options are not identified as primary/key secondary endpoint analyses; their omission from result rows does not establish a qualifying planned outcome-status change. | CONDITIONAL_OR_UNREPORTED |

## Coverage, missing definitions and limitations

106 relationships completed; 9 findings; 8 excluded observations. The inventory names all inferential fields and every pass-1 result. No scientific coverage gaps. Exact binary difference-CI construction, interaction model/scale/covariance, physician-cluster adjustment formula, patient-level duration ranks/ties, Cox coefficients/standard errors, numeric PH statistic and exact interim futility test are not supplied. These limit exact numerical inversion, are documented in the relevant S records, and are not findings without a conflict. The sample-size diagnostic with continuity correction gives186.997≈187 per arm, matching374 total; the supplied Stata command specifies the actual calculation but Stata is unavailable, so this is a diagnostic consistency check rather than an executed Stata reproduction. No noninferiority, equivalence, adjusted multiplicity boundary or superiority stopping test is claimed. All results remain subject to independent inclusion screening; no C IDs or adjudications are assigned here.

## Explicit per-relationship pass-1 records

Mechanical completion handoff: the records below are copied from the pass-1 fields already authored by root/statistics_one in the canonical inventory. This expands the earlier range-only scope notation; it introduces no new scientific review or finding and preserves the fresh statistical agent's recorded reasoning.

#### S001

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S002

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S003

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S004

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S005

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S006

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S007

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S008

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S009

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S010

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S011

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S012

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S013

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S014

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S015

- **Pass 1:** PASS_1_COMPLETE — Zero estimate lies in [0,0], includes null, P=.60 nonsignificant; no conflict. Exact Hodges–Lehmann/rank-sum inversion lacks ranks/ties.

#### S016

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S017

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S018

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S019

- **Pass 1:** PASS_1_COMPLETE — F-ST1-001: CI−10 to0 contains null but P=.03 significant; diagnostic unpooled95%CI[−10.270,−.461], PearsonP=.03273. Rounded endpoint is an alternative, not an exclusion under route A category1.

#### S020

- **Pass 1:** PASS_1_COMPLETE — F-ST1-001: CI0 to10 contains null but P=.03 significant; diagnostic unpooled95%CI[.441,9.799], PearsonP=.03269. Rounded endpoint alternative retained.

#### S021

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S022

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S023

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S024

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S025

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S026

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S027

- **Pass 1:** PASS_1_COMPLETE — F-ST1-001: CI−12 to0 contains null but P=.04 significant; diagnostic unpooled95%CI[−12.473,−.427], PearsonP=.03624. Rounded endpoint alternative retained.

#### S028

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S029

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S030

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S031

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S032

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S033

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S034

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S035

- **Pass 1:** PASS_1_COMPLETE — Containment/order/direction and positive CI[8,20] versusP<.001 reconcile; interactionP=.36 is a different hypothesis and agrees with narrative/no-difficult row; abstract/body matched. No finding.

#### S036

- **Pass 1:** PASS_1_COMPLETE — Containment/order/direction and CI[3,21] versusP=.006 reconcile; interactionP=.61 separate hypothesis. F-ST1-005 records planned hypoxemia window.

#### S037

- **Pass 1:** PASS_1_COMPLETE — Contained difference−1 in ordered[−6,3], P=.50 agree; interactionP=.17 separate. F-ST1-004 time endpoint; ranks/ties absent.

#### S038

- **Pass 1:** PASS_1_COMPLETE — Contained positive difference11 in ordered[7,14], P<.001 agree; arm intervals contain98/87, abstract/body matched; interactionNA. No finding.

#### S039

- **Pass 1:** PASS_1_COMPLETE — Contained difference8 in ordered[3,14], P=.003 agree; arm intervals contain85/77; interactionNA. F-ST1-005 window definition.

#### S040

- **Pass 1:** PASS_1_COMPLETE — F-ST1-003 descending CI4 to−1 beyond half-unit precision; no corrected interval assigned. P=.24 agrees with nonsignificance if limits reordered; F-ST1-004 endpoint. HL difference need not equal38−36.

#### S041

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed. Printed interaction P is separately inspected; no interaction coefficient/CI/model/link/scale/covariance given, so no exact inversion inferred.

#### S042

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed. Printed interaction P is separately inspected; no interaction coefficient/CI/model/link/scale/covariance given, so no exact inversion inferred.

#### S043

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed. Printed interaction P is separately inspected; no interaction coefficient/CI/model/link/scale/covariance given, so no exact inversion inferred.

#### S044

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed. Printed interaction P is separately inspected; no interaction coefficient/CI/model/link/scale/covariance given, so no exact inversion inferred.

#### S045

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed. Printed interaction P is separately inspected; no interaction coefficient/CI/model/link/scale/covariance given, so no exact inversion inferred.

#### S046

- **Pass 1:** PASS_1_COMPLETE — Contained difference3 in ordered[0,5], P=.07 nonsignificant agree; interactionP=.04 tests a different hypothesis, not a CI/P conflict.

#### S047

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed. Printed interaction P is separately inspected; no interaction coefficient/CI/model/link/scale/covariance given, so no exact inversion inferred.

#### S048

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed. Printed interaction P is separately inspected; no interaction coefficient/CI/model/link/scale/covariance given, so no exact inversion inferred.

#### S049

- **Pass 1:** PASS_1_COMPLETE — F-ST1-002: contained difference60 in ordered[17,100] excludes0 but P=.09 nonsignificant. Diagnostic unpooled95%CI[17.059,102.941], PearsonP=.08969 explain distinct constructions. Interaction.78 separate.

#### S050

- **Pass 1:** PASS_1_COMPLETE — Narrative aggregation101/104=97.115% and54/90=60% agrees with97/60 within half-unit precision. No additional aggregate CI/P printed.

#### S051

- **Pass 1:** PASS_1_COMPLETE — Contained difference10 in ordered[7,14], P<.001 agree. Actual-device402/355 differs explicitly from randomized381/376; no-device assigned randomized device by footnote. No population/measure conflict.

#### S052

- **Pass 1:** PASS_1_COMPLETE — Contained HL difference4 in ordered[2,7], P<.001 agree in direction/significance; interaction.03 separate. Raw ranks/model absent; no exact test inversion inferred. Analysis expressly post hoc and success-selected.

#### S053

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S054

- **Pass 1:** PASS_1_COMPLETE — Contained difference−1 in ordered[−6,4], P=.67 agree; retain waveform denominators371/364 distinctly from composite371/366. F-ST1-005 window, no model inferred from missingness.

#### S055

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S056

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S057

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S058

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S059

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S060

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S061

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained in ordered CIs; B-minus-T direction matches; printed difference-CI zero inclusion agrees with P at .05. No inferential finding. Count contrast/display precision inspected; exact binary CI construction/statistic/SE absent, no unreported method imposed.

#### S062

- **Pass 1:** PASS_1_COMPLETE — Individual1:1/block sizes align; prospective primary difficult subset is not made exploratory by postrandomization capture. F-ST1-008 planned trauma stratum omission. Preobservable strata are not all difficult characteristics.

#### S063

- **Pass 1:** PASS_1_COMPLETE — Diagnostic uncorrected two-proportion n165.435/arm; continuity-corrected n186.997/arm matches187/arm=374total. No sample-size finding; Stata command not executed. F-ST1-007 accrual rule. No9% null margin inferred.

#### S064

- **Pass 1:** PASS_1_COMPLETE — ITT/difficult primary/all-patient secondary align with plan and flow; no missing primary result/no-procedure case supplied. Crossovers do not change randomized primary population. No finding.

#### S065

- **Pass 1:** PASS_1_COMPLETE — Patient-level independent chi-square and continuous HL/rank-sum explicitly stated;95%CI/two-sided.05. Exact binary CI method, statistic/SE and ranks/ties absent. F-ST1-001/002 CI/P and F-ST1-003 order findings; no median subtraction imposed.

#### S066

- **Pass 1:** PASS_1_COMPLETE — Every interaction entry inspected separately from within-subgroup effect: .36,.61,.17,.31,.25,.63,.36,.46,.04,.13,.17,.78 and success-duration.03. NA follows all-patient rule. Model/link/scale/statistic/df/covariance absent; no convention inferred.

#### S067

- **Pass 1:** PASS_1_COMPLETE — KM successful first-attempt event, failed-attempt end ticks, Cox/log-rank and proportionality checks stated. HR direction maps to earlier success, not marginal-median subtraction. PH failure disclosed. F-ST1-004 endpoint; raw times/SE absent.

#### S068

- **Pass 1:** PASS_1_COMPLETE — Exploratory subgroups unplanned, no multiplicity correction claimed; cluster sensitivity post hoc. Significant primary conclusion retained in eTable1, matches narrative. Cluster formula absent, no crude/adjusted conflict asserted.

#### S069

- **Pass 1:** PASS_1_COMPLETE — Missing values/no imputation with endpoint-valid denominators coherent; source recovery before planned exclusion not contradicted. No missing primary result. Futility-only interim/no alpha adjustment stated; F-ST1-006 population. Exact futility test absent.

#### S070

- **Pass 1:** PASS_1_COMPLETE — HR1.29 inside ordered[1.04,1.60], null1 excluded, log-rankP=.02 significant, direction/caption/narrative agree. Cox/log-rank distinct tests, PH failure disclosed. F-ST1-004 time endpoint; raw times/SE absent.

#### S071

- **Pass 1:** PASS_1_COMPLETE — HR1.12 inside ordered[.97,1.30], includes1, log-rankP=.12 nonsignificant, eFigure1 agrees. PH failure disclosed. F-ST1-004 endpoint; no equivalence claim, exactSE/times absent.

#### S072

- **Pass 1:** PASS_1_COMPLETE — Cox-based earlier difficult-subgroup success versus median comparisons concerns distinct estimands; no direction reversal inferred. 'Similar' all-patient wording not formal equivalence. F-ST1-004 timing definition.

#### S073

- **Pass 1:** PASS_1_COMPLETE — Higher-success conclusion agrees with positive/significant primary/overall results; PH limitation disclosed, generalizability provisional. No NI/equivalence margin, adjusted multiplicity or efficacy-stop claim inferred.

#### S074

- **Pass 1:** PASS_1_COMPLETE — Primary first-device success definition agrees; switches during retained blade count primary initial-device failure. F-ST1-009 applies only to written missing-data recovery.

#### S075

- **Pass 1:** PASS_1_COMPLETE — Composite success without hypoxemia/threshold match, timing anchor differs: F-ST1-005. Components/valid denominators not silently equated.

#### S076

- **Pass 1:** PASS_1_COMPLETE — F-ST1-004: planned cuff-inflation timing versus reported blade removal; original endpoint result not separately identifiable; equality/amendment absent.

#### S077

- **Pass 1:** PASS_1_COMPLETE — Esophageal secondary outcome reported. Article does not restate ventilation/removal condition but supplies no opposing definition; absent detail alone excluded.

#### S078

- **Pass 1:** PASS_1_COMPLETE — Abstract retains hypoxemia secondary status; complication table title alone does not downgrade status. F-ST1-005 window difference.

#### S079

- **Pass 1:** PASS_1_COMPLETE — Observer/physician discordance video recovery matches report; source recovery distinct from imputation. Stopwatch refers to planned time endpoint, F-ST1-004/005.

#### S080

- **Pass 1:** PASS_1_COMPLETE — Randomized single-center unblinded superiority design coherent. >9% aim is planning context, not explicit9% superiority-null margin; no NI/equivalence model asserted.

#### S081

- **Pass 1:** PASS_1_COMPLETE — Block sizes/1:1 match; F-ST1-008 facial/neck-trauma stratum absent report. Stratified allocation does not by itself assert an adjusted primary analysis.

#### S082

- **Pass 1:** PASS_1_COMPLETE — Any-difficult primary/all-enrolled secondary match; postprocedure capture permitted. Facial/neck versus facial wording does not independently identify altered patients/results.

#### S083

- **Pass 1:** PASS_1_COMPLETE — ITT/primary difficult/all-patient secondary match; no no-procedure randomized cases reported. Blade insertion without passed device is an attempt, not no-attempt exclusion. F-ST1-006 defines interim population.

#### S084

- **Pass 1:** PASS_1_COMPLETE — Post-stabilization characteristic capture/rescue choice coherent with report. ED safety assessment can extend beyond participation per other sections; no independent safety-stop conflict inferred.

#### S085

- **Pass 1:** PASS_1_COMPLETE — Two-sided.05/95%CI match. Planned KM percentileCIs/percent-censoring not separately given for original cuff-inflation endpoint: F-ST1-004. Software-version change does not itself conflict.

#### S086

- **Pass 1:** PASS_1_COMPLETE — 95/86%,80%power,187/arm=374 match. Continuity-corrected normal diagnostic n186.997/arm reconciles; supplied Stata calculation not executed. F-ST1-007 accrual rule.

#### S087

- **Pass 1:** PASS_1_COMPLETE — Actual-device/deviations reported; exploratory as-treated contrast explicitly differs from ITT. No primary denominator substitution.

#### S088

- **Pass 1:** PASS_1_COMPLETE — Chi-square/difficult primary/overall secondary align. Secondary differences by difficult status reported. Exploratory interactions and cluster sensitivity not claimed prespecified. F-ST1-004 planned time result replaced.

#### S089

- **Pass 1:** PASS_1_COMPLETE — F-ST1-009 primary recovery names secondary composite; no affected observed missing-primary case asserted. Video recovery/relevant exclusion compatible with no imputation.

#### S090

- **Pass 1:** PASS_1_COMPLETE — F-ST1-006 all507 interim versus primary difficult subset. +15pp cap100%,projected1000,futility-only/no superiority alpha adjustment agree; exact 'no difference' test/boundary absent.

#### S091

- **Pass 1:** PASS_1_COMPLETE — DSMB safety halt expressly separate from futility; repeated safety rules coherent. No numeric efficacy/NI/equivalence boundary or actual safety halt reported; locator8.7.2 not a new rule.

#### S092

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained; ordered positive difference CI and significant P agree. Clustering explicitly distinct from unadjusted main; wider CIs/changed P not mismatched copies. Interactions for subgroup rows are separate hypotheses,NA for overall analyses explicit. Exact clustering adjustment/test/CI construction,covariance and raw ranks absent; no Gaussian exact P or crude-ratio conflict inferred.

#### S093

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained; ordered positive difference CI and significant P agree. Clustering explicitly distinct from unadjusted main; wider CIs/changed P not mismatched copies. F-ST1-005 window comparison. Interactions for subgroup rows are separate hypotheses,NA for overall analyses explicit. Exact clustering adjustment/test/CI construction,covariance and raw ranks absent; no Gaussian exact P or crude-ratio conflict inferred.

#### S094

- **Pass 1:** PASS_1_COMPLETE — Duration estimate contained in ordered interval including0 and P=.31 nonsignificant agree; IQRs ordered. F-ST1-004 endpoint comparison. Interaction.17 is separate hypothesis. Exact clustering adjustment/test/CI construction,covariance and raw ranks absent; no Gaussian exact P or crude-ratio conflict inferred.

#### S095

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained; ordered positive difference CI and significant P agree. Clustering explicitly distinct from unadjusted main; wider CIs/changed P not mismatched copies. Interactions for subgroup rows are separate hypotheses,NA for overall analyses explicit. Exact clustering adjustment/test/CI construction,covariance and raw ranks absent; no Gaussian exact P or crude-ratio conflict inferred.

#### S096

- **Pass 1:** PASS_1_COMPLETE — Arm estimates/difference contained; ordered positive difference CI and significant P agree. Clustering explicitly distinct from unadjusted main; wider CIs/changed P not mismatched copies. F-ST1-005 window comparison. Interactions for subgroup rows are separate hypotheses,NA for overall analyses explicit. Exact clustering adjustment/test/CI construction,covariance and raw ranks absent; no Gaussian exact P or crude-ratio conflict inferred.

#### S097

- **Pass 1:** PASS_1_COMPLETE — Duration estimate contained in ordered interval including0 and P=.95 nonsignificant agree; IQRs ordered. F-ST1-004 endpoint comparison. F-ST1-003 main descending interval; disclosed clustering P change not conflicting copy. Exact clustering adjustment/test/CI construction,covariance and raw ranks absent; no Gaussian exact P or crude-ratio conflict inferred.

#### S098

- **Pass 1:** PASS_1_COMPLETE — Point compatible with printed interval; upper bound use explicit. Exact cluster size weighting/formula, covariance, variance estimator, statistic/df and interval/test pairing absent. No value/test decision conflicts, no preferred adjustment proposed.

#### S099

- **Pass 1:** PASS_1_COMPLETE — Matches report threshold/window, F-ST1-004/005 compare plan timing. Keep endpoint-valid denominators distinct. Exact duration n/ranks absent, do not infer from arm headers.

#### S100

- **Pass 1:** PASS_1_COMPLETE — Containment/order/direction and nonsignificant CI/test agree, matches S071. Risk rows start randomized n and decline. Failure ticks/crossing curves explained. F-ST1-004 timing; PH failure disclosed. No exact digital coordinates/CoxSE/numericPH statistic supplied.

#### S101

- **Pass 1:** PASS_1_COMPLETE — 257+250=507 and97.276/85.2% reconcile half-unit display. F-ST1-006 population. Diagnostic final500/arm B(250+243)/500=.986,T.852,difference.134 favors continuation for displayed cohort; exact subgroup/test absent. 'After500' allows507, no independent timing conflict.

#### S102

- **Pass 1:** PASS_1_COMPLETE — Primary-subgroup capture matches report eight features. No populated values. Allocation stratum distinct from capture checklist; F-ST1-008 concerns protocol randomization rule.

#### S103

- **Pass 1:** PASS_1_COMPLETE — Capture supports primary first-device-success/no-device failure definitions; retained-blade switching remains initial-device failure. F-ST1-004 duration endpoint comparison, no additional primary-success conflict inferred.

#### S104

- **Pass 1:** PASS_1_COMPLETE — No populated counts or planned grade inferential model. Illustrated categories compatible with report verbal grade definitions; missing wording is not an opposing definition.

#### S105

- **Pass 1:** PASS_1_COMPLETE — No observed counts or separate statistical hypothesis. Rescue/confirmation capture compatible with discretionary rescue/report process quantities. No new numeric result asserted by blank form.

#### S106

- **Pass 1:** PASS_1_COMPLETE — No populated counts or explicitly primary/key-secondary status for cardiac-arrest/death options. Omitted result row alone does not establish a qualifying status change. Safety windows preserved; no count reconstructed from blank fields.
