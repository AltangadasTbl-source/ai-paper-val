# Statistical consistency review — pass 1

**Scope:** Independent pass-one review of all 38 frozen inferential/statistical relationships, `S001` through `S038`.  Evidence was limited to the freshly prepared source maps, direct PDFs, fresh native/layout text, and designated rendered pages.  This is a quality-control review; every observation and provisional candidate is **Pending Human Adjudication**.

**Method:** For each assigned relationship, the review checked the printed estimate against interval containment/order, sign and direction, effect-measure/scale/reference labels, duplicate occurrences, outcome/time/population matching, and stated test/model compatibility. Calculations below are diagnostic only where the supplied material does not define all inferential inputs. Planned documents from different versions were kept version-specific and were not treated as contradictions merely because their design changed.

**Display-zero screen:** No assigned result printed a coherent `P = 0`, `p = 0.000`, or equivalent. `DISPLAY_ZERO_NOT_CANDIDATE` count: **0**.

## Complete relationship coverage

| Canonical ID | PASS_1_COMPLETE record |
|---|---|
| S001 | `PASS_1_COMPLETE` — **SC001**: printed sample-size total (779) is incompatible with the simultaneously printed 389 in each group (778 total). |
| S002 | `PASS_1_COMPLETE` — Interim threshold/Bayesian quantities are definitions only; no matched reported test was supplied for compatibility checking. |
| S003 | `PASS_1_COMPLETE` — Mortality-analysis labels distinguish Kaplan-Meier, risk difference, and Cox HR; matched HR 0.98 (0.77-1.24) contains its estimate and has ordered endpoints. |
| S004 | `PASS_1_COMPLETE` — Competing-risk IMV definition is supplied; main-text cause-specific HR 0.85 (0.68-1.06) contains its estimate and has ordered endpoints. Figure-label inconsistency is captured jointly in SC003. |
| S005 | `PASS_1_COMPLETE` — Stated test/effect labels were checked against displayed results; no compatible statistic/SE inputs were supplied. |
| S006 | `PASS_1_COMPLETE` — Day-28 mortality HR 0.98 (0.77-1.24), P=.94, and risk difference -0.5% (-7.3 to 6.3) are internally ordered/contain the estimates. Figure 3 contrast/direction issue is captured in SC003. |
| S007 | `PASS_1_COMPLETE` — IMV cause-specific HR 0.85 (0.68-1.06), P=.17, and risk difference -5.1% (-12.3 to 2.0) are internally ordered/contain the estimates. Figure 3 contrast/direction issue is captured in SC003. |
| S008 | `PASS_1_COMPLETE` — Infection cause-specific HR 1.01 (0.96-1.06), P=.91, and risk difference -0.6% (-4.6 to 4.1) are internally ordered/contain the estimate. |
| S009 | `PASS_1_COMPLETE` — ICU and hospital mortality RRs (1.01 [0.82-1.24] and 0.99 [0.84-1.17]) contain estimates and have ordered intervals; no supplied rule permits a further P/SE reconstruction. |
| S010 | `PASS_1_COMPLETE` — Length-of-stay differences have ordered intervals containing their estimates; medians/IQRs and mean-difference estimands are explicitly distinguished. |
| S011 | `PASS_1_COMPLETE` — Figure 2 log-rank P=.85 is a finite value; it is not required to equal the Cox-model P=.94 because different named tests are printed. |
| S012 | `PASS_1_COMPLETE` — **SC002**: matched abstract and narrative respiratory-rate intervals differ at the upper bound (-0.2 versus -0.3 per minute). |
| S013 | `PASS_1_COMPLETE` — PaO2:FIO2 difference 19.5 (4.4-34.6) contains its estimate, is ordered, and agrees with the reported direction (150 versus 119). |
| S014 | `PASS_1_COMPLETE` — **SC003**: Figure 3A all-patient HR/CI is the reciprocal of the matched Table 2/main-text HR/CI while its displayed direction axis is not reconciled to that opposite contrast. |
| S015 | `PASS_1_COMPLETE` — **SC003**: Figure 3B all-patient HR/CI is the reciprocal of the matched Table 2/main-text cause-specific HR/CI while its displayed direction axis is not reconciled to that opposite contrast. |
| S016 | `PASS_1_COMPLETE` — Post hoc center-effect P values (.33 mortality, .07 intubation) have no supplied test statistic/SE; no cross-location conflict found. |
| S017 | `PASS_1_COMPLETE` — Intubated-patient risk difference +3% (-8.5 to 14.5), P=.65 contains the estimate and has ordered endpoints; compatible test details are absent. |
| S018 | `PASS_1_COMPLETE` — Cancer/noncancer risk difference +1.8% (-10.8 to 14.3), P=.50 contains the estimate and has ordered endpoints; compatible test details are absent. |
| S019 | `PASS_1_COMPLETE` — Time-to-IMV mean difference -0.5 days (-1.2 to 0.1) contains the estimate and supports the printed non-significant direction; no P/test is supplied. |
| S020 | `PASS_1_COMPLETE` — Primary/secondary interpretation repeats agree with the printed non-significant primary outcome and exploratory-secondary qualification. |
| S021 | `PASS_1_COMPLETE` — No applicable statistical result relationship on main PDF p.9. |
| S022 | `PASS_1_COMPLETE` — Initial noninferiority sample/design values are version-specific planning values; not equated to later superiority planning or final results. |
| S023 | `PASS_1_COMPLETE` — **SC004**: the printed noninferiority criterion calls for a lower 95% CI boundary “less than 9%,” whereas its immediately preceding supplied figure depicts the noninferiority margin to the negative/left side of zero on the stated new-minus-active-control efficacy axis. |
| S024 | `PASS_1_COMPLETE` — Initial ITT/PP analysis-set definition is a planned rule; actual two consent withdrawals/388-per-arm analysis are not a direct conflict. |
| S025 | `PASS_1_COMPLETE` — **SC005**: initial-plan primary-hypothesis text names “NIV” although the same plan identifies HFNO as the experimental intervention. |
| S026 | `PASS_1_COMPLETE` — **SC006**: the same initial-plan primary-outcome paragraph says patients are classified alive/dead at day 28 but labels the effect measure “relative risk of hospital death.” |
| S027 | `PASS_1_COMPLETE` — Gail-Simon interaction and conditional subset-analysis rules are planning definitions; no direct inconsistency identified. |
| S028 | `PASS_1_COMPLETE` — Competing-risk, Gray-test, cause-specific-Cox, and longitudinal-model rules are endpoint-specific plan definitions; no compatible result/statistic pair was supplied here. |
| S029 | `PASS_1_COMPLETE` — “No interim analysis” belongs to the initial protocol version; it is not a contradiction solely with the later published protocol/main-paper interim plan. |
| S030 | `PASS_1_COMPLETE` — Published-protocol superiority design/sample plan is version-specific; main sample-size arithmetic issue is separately captured in SC001. |
| S031 | `PASS_1_COMPLETE` — Published-protocol interim/terminal thresholds and Bayesian quantities are plan definitions; no contradictory matched inferential result is present. |
| S032 | `PASS_1_COMPLETE` — **SC005** and **SC006** recur in the published protocol: primary hypothesis names “NIV,” and day-28 alive/dead classification is paired with “relative risk of hospital death.” |
| S033 | `PASS_1_COMPLETE` — Published secondary/PER-protocol/missing-data rules provide definitions, but no contradictory matched inferential result. |
| S034 | `PASS_1_COMPLETE` — Published competing-risk/Gray/cause-specific-Cox/joint-model plan gives endpoint-specific definitions; no direct discrepancy identified. |
| S035 | `PASS_1_COMPLETE` — **SC007**: Supplement eFigure 1 labels the cumulative-incidence P=.17 as a log-rank test, whereas the supplied main methods specify Gray testing for IMV cumulative incidence with death without IMV as competing risk. |
| S036 | `PASS_1_COMPLETE` — eFigure 2 asterisks lack a supplied legend/threshold. This is a precisely recorded missing definition, not a candidate absent an independent mismatch. |
| S037 | `PASS_1_COMPLETE` — eTable medians/IQRs are descriptive with no printed P value/test; no inferential compatibility check is applicable. |
| S038 | `PASS_1_COMPLETE` — External/preliminary-study P values are comparator-only evidence and were not matched to HIGH-trial results. |

## Provisional candidates for coordinator de-duplication

### SC001 — Sample-size total does not equal the printed equal arm counts

- **Linked relationships:** S001, S030.
- **Category:** Numeric or arithmetic inconsistency.
- **Exact source locations:** [DOC-001 PDF p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3); [DOC-002 PDF pp.90-91](../../../joi180109supp1_prod.pdf#page=90) for the separate 778/389-per-arm later protocol plan.
- **Printed evidence:** Main p.3: “779 patients (389 in each group)” were required. The main paper’s Figure 1 and results use 778 randomized, 389 per group; the published protocol plan likewise states 778, 389 per group.
- **Direct observation:** One stated two-arm allocation is 389 + 389, while the same main-paper sentence states a total of 779.
- **Reasoning procedure / calculation:** 389 + 389 = 778, not 779. This is plain displayed arithmetic and does not require a model assumption.
- **Diagnostic inference:** The single-unit discrepancy may be a total-count transcription or an unreported unequal-allocation/sample-size calculation detail; neither is supplied in the main-paper sentence.
- **Alternative source-grounded interpretations:** The calculation target may have been 779 total with a non-even allocation not reflected in the parenthetical, or the total may have been rounded/corrected to 778 in later protocol versions. The supplied source does not state which printed component is intended.
- **Missing definitions / exact human question:** Was the intended sample-size target 779 total with a non-389/389 allocation, or 778 total (389 per group)?
- **Status:** Pending Human Adjudication.

### SC002 — Matched respiratory-rate confidence interval differs between abstract and narrative

- **Linked relationships:** S012.
- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001 PDF p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1); [DOC-001 PDF p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6).
- **Printed evidence:** The abstract reports high-flow versus control respiratory rate at 6 hours as 25 versus 26/min, difference -1.8/min (95% CI -3.2 to -0.2). The results narrative reports the same 25 versus 26/min and mean difference -1.8, but 95% CI -3.2 to -0.3.
- **Direct observation:** The population, time point, contrast, estimate, and lower CI endpoint match, while the printed upper endpoint differs by 0.1/min.
- **Reasoning procedure / calculation:** Exact location-to-location comparison; no reconstruction of a test statistic was used.
- **Diagnostic inference:** The discrepancy could reflect a rounding, transcription, or use of two differently rounded source calculations. The supplied article does not identify distinct models or analysis sets for the two occurrences.
- **Alternative source-grounded interpretations:** A hidden precision/rounding convention could yield different displayed endpoints even if the unrounded interval is shared; alternatively one occurrence may be a copy error.
- **Missing definitions / exact human question:** Which confidence interval, model, analysis set, and rounding rule is authoritative for the stated six-hour respiratory-rate contrast?
- **Status:** Pending Human Adjudication.

### SC003 — Figure 3 hazard-ratio contrast/direction is not reconciled with Table 2 and narrative

- **Linked relationships:** S004, S006, S007, S014, S015.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-001 PDF p.5, Table 2](../../../jama_azoulay_2018_oi_180109.pdf#page=5); [DOC-001 PDF p.6, secondary-outcome narrative](../../../jama_azoulay_2018_oi_180109.pdf#page=6); [DOC-001 PDF p.7, Figure 3A-B](../../../jama_azoulay_2018_oi_180109.pdf#page=7).
- **Printed evidence:** Table 2/main narrative report high-flow versus standard day-28 mortality HR 0.98 (95% CI 0.77-1.24) and IMV cause-specific HR 0.85 (0.68-1.06). Figure 3’s all-patient rows, using the same high-flow and standard event totals (138/388 versus 140/388; 150/388 versus 170/388), report mortality HR 1.02 (0.81-1.29) and IMV HR 1.17 (0.94-1.46). Figure 3’s axis labels values below 1 as “Favors High-Flow Nasal Oxygen Therapy” and values above 1 as “Favors Standard Oxygen Therapy.”
- **Direct observation:** The Figure 3 all-patient mortality estimate/interval are the rounded reciprocal of the Table 2 estimate/interval: 1/0.98 = 1.020; reciprocal endpoints are 1/1.24 = 0.806 and 1/0.77 = 1.299. Its IMV estimate/interval are likewise the rounded reciprocal: 1/0.85 = 1.176; reciprocal endpoints are 1/1.06 = 0.943 and 1/0.68 = 1.471. The supplied figure does not print a contrast definition for its HR column.
- **Reasoning procedure / calculation:** Reciprocal check only, based on the printed HRs/CIs. It establishes an opposite effect-ratio orientation but does not identify which figure component was intended to be changed.
- **Diagnostic inference:** Figure 3 may intentionally use standard-versus-high-flow HRs while Table 2/narrative use high-flow-versus-standard HRs. If so, the figure’s directional “favors” axis requires reconciliation to that opposite contrast; if not, the figure’s HR values/labels are inconsistent with the matched results. No pooled-model equivalence was assumed.
- **Alternative source-grounded interpretations:** A figure-specific reciprocal contrast could be valid if explicitly defined and direction labels correspond to it; the exact reciprocal values support that possibility. The figure lacks that definition, leaving readers unable to reconcile the displayed HR direction with the labelled favours axis and Table 2 narrative.
- **Missing definitions / exact human question:** What numerator/reference group defines Figure 3 HRs, and are its “Favors High-Flow”/“Favors Standard” labels oriented to that same contrast? Should Figure 3 be relabelled or should its HR values be reciprocated to match Table 2/narrative?
- **Status:** Pending Human Adjudication.

### SC004 — Initial noninferiority criterion’s printed bound/sign conflicts with its supplied explanatory axis

- **Linked relationships:** S023.
- **Category:** Statistical reporting inconsistency.
- **Exact source locations:** [DOC-002 PDF p.40, Figure 4](../../../joi180109supp1_prod.pdf#page=40); [DOC-002 PDF p.42](../../../joi180109supp1_prod.pdf#page=42).
- **Printed evidence:** Figure 4 labels its horizontal measure “Difference in Efficacy (New Treatment Minus Active Control),” marks zero, and places the noninferiority margin on the left/negative side. Page 42 states: “Non-inferiority of HFNO will thus be demonstrated if the lower boundary of the 95% CI is less than 9%.”
- **Direct observation:** The graphical margin is on the negative side of the labelled difference scale, but the accompanying sentence supplies a positive `9%` criterion for the lower CI boundary without a negative sign or effect-scale definition.
- **Reasoning procedure / calculation:** Direction/axis comparison only. No P value, CI, or threshold was recomputed.
- **Diagnostic inference:** The written rule may have omitted a minus sign, used a differently oriented risk/efficacy scale, or been translated imprecisely. The source does not define an alternative scale in that sentence.
- **Alternative source-grounded interpretations:** The intended rule may be a lower-bound criterion of greater than -9% on the Figure 4 efficacy-difference axis; a differently defined mortality-risk difference might require another orientation. Neither interpretation is explicitly linked to the printed “less than 9%” wording.
- **Missing definitions / exact human question:** What exact signed effect measure and inequality were prespecified for the 9% noninferiority margin, and does the p.42 text contain a sign or inequality error?
- **Status:** Pending Human Adjudication.

### SC005 — Primary-hypothesis intervention is labelled NIV while the plans identify HFNO as the intervention

- **Linked relationships:** S025, S032.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-002 PDF p.52](../../../joi180109supp1_prod.pdf#page=52); [DOC-002 PDF p.104](../../../joi180109supp1_prod.pdf#page=104); related HFNO-superiority wording on those same pages.
- **Printed evidence:** Initial-plan p.52 states, “The primary hypothesis is non inferiority of the NIV in terms of 28-day mortality,” then states that “HFNO is superior over standard oxygen or NIV” for secondary outcomes. Published-protocol p.104 states, “The primary hypothesis is superiority of the NIV in terms of 28-day mortality,” then states that “HFNO is superior over standard oxygen” for secondary outcomes. Both documents elsewhere identify HFNO as the experimental intervention.
- **Direct observation:** The primary-hypothesis sentence uses `NIV`, whereas the immediately associated intervention/comparator wording names HFNO as the experimental therapy and standard oxygen as control.
- **Reasoning procedure / calculation:** Exact label comparison; no inference about trial validity or a treatment effect is made.
- **Diagnostic inference:** `NIV` may be a carried-forward label, may refer to an unrecorded comparator definition, or may be a textual error. The documents do not define NIV as the intervention in these passages.
- **Alternative source-grounded interpretations:** The writers may have intended “HFNO” and retained `NIV` from an earlier template; alternatively `NIV` could refer to a generic oxygenation strategy but that meaning is not supplied for the primary hypothesis.
- **Missing definitions / exact human question:** Does `NIV` in each primary-hypothesis sentence intentionally denote HFNO, or should it be replaced with HFNO/another explicitly defined intervention?
- **Status:** Pending Human Adjudication.

### SC006 — Planned primary outcome alternates between day-28 vital status and “hospital death”

- **Linked relationships:** S026, S032.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-002 PDF p.54](../../../joi180109supp1_prod.pdf#page=54); [DOC-002 PDF p.82](../../../joi180109supp1_prod.pdf#page=82); [DOC-002 PDF p.104](../../../joi180109supp1_prod.pdf#page=104).
- **Printed evidence:** Each statistical-plan passage says all patients will be followed until day 28 and classified “alive or dead,” then says “The relative risk of hospital death in the experimental versus the control arm will be estimated.”
- **Direct observation:** A fixed day-28 vital-status endpoint and `hospital death` are different printed outcome labels. No statement limits hospital death to day 28 or equates the two labels.
- **Reasoning procedure / calculation:** Outcome/time-label comparison only; no patient-level data or effect calculation was inferred.
- **Diagnostic inference:** “Hospital death” may have been intended as shorthand for death by day 28 during the index hospitalization, or it may be a carried-forward endpoint label. The supplied plans do not resolve the time horizon.
- **Alternative source-grounded interpretations:** Because patients were followed to day 28, every observed death in the primary analysis may have occurred in hospital; alternatively deaths after discharge/before day 28 could make the labels non-equivalent. The source gives no defining rule.
- **Missing definitions / exact human question:** Is the planned relative-risk estimand day-28 all-cause mortality, hospital mortality without a fixed time point, or hospital death censored/limited at day 28?
- **Status:** Pending Human Adjudication.

### SC007 — eFigure 1 labels the IMV cumulative-incidence comparison as log-rank despite the supplied competing-risk/Gray-test definition

- **Linked relationships:** S004, S028, S034, S035.
- **Category:** Statistical reporting inconsistency.
- **Exact source locations:** [DOC-001 PDF pp.3-4](../../../jama_azoulay_2018_oi_180109.pdf#page=3); [DOC-002 PDF p.82](../../../joi180109supp1_prod.pdf#page=82); [DOC-003 PDF p.3, eFigure 1](../../../joi180109supp2_prod.pdf#page=3).
- **Printed evidence:** Main methods specify death without IMV as a competing risk, nonparametric cumulative incidence, and Gray testing for the IMV endpoint. The original plan likewise specifies competing-risk cumulative incidence and the Gray test. eFigure 1 is titled “Cumulative Incidence of Mechanical Ventilation” and prints `P (log Rank test) = 0.17`; the main Table 2/narrative gives the matched IMV P=.17.
- **Direct observation:** The supplied endpoint/test definitions call for Gray testing for competing-risk cumulative incidence, whereas the matched supplementary cumulative-incidence figure labels its P=.17 as a log-rank test.
- **Reasoning procedure / calculation:** Test-label comparison only. The matching P values were not assumed to prove identical test calculations, and no statistic/SE reconstruction was attempted.
- **Diagnostic inference:** The eFigure label may be an inaccurate test name, the figure may have used a separate log-rank calculation, or the figure may represent a differently defined time-to-IMV analysis. The supplied materials do not say which.
- **Alternative source-grounded interpretations:** A log-rank test can be applied to a different time-to-event representation, but the figure’s title and treatment groups match the stated competing-risk endpoint; a distinct estimand/censoring rule is not printed.
- **Missing definitions / exact human question:** Was eFigure 1’s P=.17 generated by Gray’s test, a log-rank test, or an analysis with a different competing-risk/censoring definition from the main IMV endpoint?
- **Status:** Pending Human Adjudication.

## Pass-one limitations

- No raw data, model coefficients, standard errors, degrees of freedom, covariance structures, sidedness-specific calculations, variance estimators, multiplicity adjustments, or exact rounding specifications were supplied for most displayed results. Compatibility checks beyond the explicit printed rules were therefore not inferred from convention.
- The direct evidence establishes printed-label, arithmetic, and cross-location observations. It does not establish a correction, root cause, statistical validity, or effect on conclusions.
- No DISPLAY_ZERO_NOT_CANDIDATE entries were needed because no display-zero P value occurred in the assigned relationships.

**Pass-one completion:** 38/38 canonical S IDs explicitly completed; 7 distinct provisional candidates (`SC001`–`SC007`); 0 display-zero records; all provisional candidates remain Pending Human Adjudication.
