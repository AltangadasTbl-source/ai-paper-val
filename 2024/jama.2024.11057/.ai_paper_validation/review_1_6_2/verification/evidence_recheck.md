# Mechanical Evidence Recheck — Workflow 1.6.2

Runtime agent: /root/evidence_rechecker. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Scope: C001, C002, C003, C004, C005, including every location merged from duplicate checker findings and every cited amendment-context location. All five IDs remain Pending Human Adjudication. This artifact records evidence facts and classifications, not dispositions.

QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. The current-run ledger and independent screen supplied the assigned scope. Exact supplied PDFs were reread using direct `pdftotext -layout -f N -l N SOURCE -`, Poppler 26.01.0, with output streamed rather than stored. Units reread: article PDF pp. 1–6; protocol PDF pp. 2, 4–6, 15; results-supplement PDF pp. 2–6, 14–15. A current direct extraction of the complete article and results supplement was also searched for primary adjustment/covariate attribution. The current-source CPU renderings of article p. 3 and results-supplement p. 14 created by the initial screener were visually inspected, alongside new direct text reads of those supplied PDF pages. Historical reusable OCR, text and tables were not final authority. No new derivative, rendering, OCR, fallback installation, or source/reused-asset modification was needed. Compute device recorded in tooling_record.md: CPU. Arithmetic was independently recomputed using JavaScript; no Python scientific review or external evidence was used.

## Recheck summary

| ID | All affected locations found | Printed source/comparator matched | Evidence state | Primary relationship | All relationships | Review domain | Classification correction |
|---|---|---|---|---|---|---|---|
| C001 | Yes | Yes | reproduced | P_R | P_R | protocol_report | None |
| C002 | Yes | Yes | reproduced | S_W | S_W | statistical_results | None |
| C003 | Yes | Yes | reproduced | P_R | P_R, S_C | protocol_report | None |
| C004 | Yes | Yes | reproduced | P_R | P_R | protocol_report | None |
| C005 | Yes | Yes | reproduced | S_W | S_W | statistical_results | None |

There are no source-location, transcription, or tooling gaps. Missing substantive definitions are recorded separately for each ID. No ID required a transcription correction. No classification was changed.

## C001 — Primary estimate attribution to planned baseline adjustment

**Location found; source value/text matched; comparator matched:** Yes, separately at every listed location:

| Exact supplied location | Content-confirmed role | Direct-source recheck fact |
|---|---|---|
| [Protocol p. 5, Data Analysis Plan, Primary Analysis](../../../joi240078supp1_prod_1739900423.22574.pdf#page=5) | PLAN | Prospectively states that seven-month point-prevalence abstinence will be compared using logistic regression and that all estimates will be adjusted for baseline confounders of the intervention-outcome relationship. |
| [Article p. 1, abstract Main Outcomes/Results](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=1) | REPORT | Primary outcome is seven-month 30-day abstinence under intention-to-treat with missingness coded as vaping; primary rates 37.8% and 28.0%; RR 1.35, 95% CI 1.17–1.57, P<.001. No adjustment identity is attached to that estimate. |
| [Article p. 4, Statistical Methods](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4) | REPORT | Ordinary logistic regression in R glm, original randomized assignment and missing=vaping are stated. MI and IPRW are distinguished as other analyses. No primary baseline-confounder formula, covariate list, or selection rule is supplied here. |
| [Article p. 5, Vaping Cessation](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=5) | REPORT | Primary rates 287/759 and 208/744 and RR 1.35 (1.17–1.57) are confirmed. CCA and IPRW estimates are separately identified. |
| [Article p. 6, Table 2, 30-day row and footnote](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=6) | REPORT | RR 1.35 (1.17–1.57), OR 1.57 (1.26–1.95), P<.001; footnote says missing outcomes were counted as vaping. The display does not identify baseline adjustment. |
| [Results supplement p. 14, eTable 5, 30-day Missing=Vaping row](../../../joi240078supp2_prod_1739900423.24574.pdf#page=14) | REPORT | Same primary RR 1.35 (1.17–1.57) and OR 1.57 (1.26–1.95) are confirmed; CCA and IPRW are separately labeled. |
| [Protocol p. 15, Summary of Changes](../../../joi240078supp1_prod_1739900423.22574.pdf#page=15) | PLAN, context only | Listed changes concern baseline measures, decisional-capacity questions, and fraud prevention. No primary-model or confounder-adjustment amendment is identified. |

**Consistency rule applicable:** Yes, focus areas C/D and Route B. The comparison is the affirmative prospective adjustment commitment versus the report's unresolved attribution of its printed primary effect to that commitment. It is not a comparison that treats a model-based estimate as a crude estimate, and it does not establish that the planned analysis was absent.

**Logical comparison reproduced:** The plan promises adjustment; the report names an ordinary logistic primary analysis and its numeric outputs but does not connect a defined adjustment model to RR 1.35 or OR 1.57. Ordinary logistic regression permits covariates, so the description does not itself contradict adjusted modeling. The registered inconsistency is the unresolved connection between the supplied specification and the specific primary estimate, as qualified by the independent screen. Immediate context supplies no adjustment attribution or operative amendment.

**Calculation and display-precision interval check:** The integer counts give marginal RR=(287/759)/(208/744)=1.3525387656 and marginal OR=(287/472)/(208/536)=1.5669002608. Those are contained in the printed point-estimate half-unit intervals [1.345,1.355] and [1.565,1.575]; diagnostic residual discrepancy is zero. Counts denote exact integer events rather than continuously rounded quantities. The calculation confirms that there is no registered count-to-effect discrepancy and cannot identify the fitted covariates. Half-unit numeric intervals do not resolve the categorical model-attribution comparison.

**Necessary inputs available:** The affirmative plan statement, reported method, primary population, outcome/time point, primary effect labels, counts and amendment summary are available and matched. These reproduce the reporting-attribution question.

**Exact missing inputs or definitions:** The fitted primary model formula, included baseline covariates, confounder-selection rule, any decision that no covariate qualified, the identity of any adjusted versus marginal estimand, and any applicable model amendment are not supplied. Individual data and a fitted-model output sufficient to establish what was actually run are unavailable. Their absence prevents determining the underlying analysis, not observing the supplied reporting comparison.

**Source-grounded alternative interpretation:** Unlisted covariates could be present in the ordinary logistic model; no candidate covariate could have qualified under an undisclosed selection rule; or the analysis specification could have changed. MI/IPRW descriptions do not by themselves establish primary confounder adjustment. Numeric agreement with crude points does not exclude adjustment.

**Direct observation versus inferred explanation:** Direct observations are the plan's affirmative commitment, the report's printed effects and its described method/labels. An omitted adjustment, a treatment-only model, or an undocumented amendment would be an inference and is not established here.

**Classification confirmed:** Every substantive comparator in the prospective protocol is PLAN; every retrospective article/results-supplement location is REPORT. Primary relationship P_R; all relationships P_R; review domain protocol_report. The REPORT locations corroborate the same primary reporting attribution, so no S_C relationship is introduced. The amendment page is contextual and creates neither P_P nor an additional relationship. No classification correction. Classification ambiguity is limited to the operative adjustment/model definition.

**Evidence state:** reproduced. **Decisive recheck fact:** The exact plan's baseline-adjustment commitment remains unconnected to the specific primary estimates in the exact supplied reporting locations. This reproduces the narrowly registered Route B reporting-attribution issue, not proof that covariate adjustment was omitted.

**Exact remaining human question:** Which primary model and baseline covariates generated the printed RR 1.35 and OR 1.57, and how does that model correspond to the protocol's adjustment commitment?

## C002 — Retention test population and waitlist exclusion

**Location found; source value/text matched; comparator matched:** Yes, separately at every listed location:

| Exact supplied location | Content-confirmed role | Direct-source recheck fact |
|---|---|---|
| [Article p. 2, Participants, waitlist discussion](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=2) | REPORT | The sentence's antecedent is the waitlist control group: it was included to estimate assessment reactivity/retention-incentive influence, and was not included in sample-size calculations or tests of statistical significance. The sentence continues at the top of the right column. |
| [Article p. 4, first Results paragraph](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4) | REPORT | At one month, assessment-only 636/744 and waitlist 152/178 are compared with intervention 609/759 beside P=.02. At seven months, the text says no difference between groups and lists intervention 521/759, assessment-only 543/744 and waitlist 132/178 beside P=.11. |
| [Article p. 6, participant-flow figure](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=6) | REPORT, corroboration | Randomized groups 759, 744, 178 and one-/seven-month completed-survey counts 609/521, 636/543, 152/132 agree with the retention paragraph. The figure includes only the two main groups in primary analysis and says the waitlist group provides context. |

**Consistency rule applicable:** Yes, focus area C and Route B. The same REPORT excludes a group from significance testing but places named P values beside retention comparisons that describe that group without identifying a narrower tested contrast. This concerns attribution of P=.02 and P=.11 to a test population, rather than a peripheral cross-location difference in contributor counts.

**Logical comparison reproduced:** The unqualified significance-test exclusion and three-group retention language remain present. No supplied sentence identifies the test used, states that the P values concern only the two principal arms, or provides a retention-only exemption. The test population is therefore unresolved in the printed report. The p. 6 contextual waitlist label does not establish which retention test was performed.

**Calculation and display-precision interval check:** As diagnostics only, a three-arm Pearson 3-by-2 responder/nonresponder test gives chi-square 8.1085841539 with 2 degrees of freedom and P=.0173477567 at one month, and chi-square 4.3270956482 with 2 degrees of freedom and P=.1149166927 at seven months. The observed responder totals are 1397 and 1196, each among 1681 randomized participants. These diagnostic P values lie in the printed half-unit intervals [.015,.025] for .02 and [.105,.115] for .11. Thus residual numeric discrepancy is zero; neither diagnostic is an interval/P-value conflict. This match cannot establish the actual test or tested population. Rounding has no bearing on categorical inclusion of waitlist participants in a test.

**Necessary inputs available:** Group identities, exact integer randomized/respondent counts, printed P values, the exclusion sentence and complete local retention paragraph are available and matched. These reproduce the reporting question and permit the explicitly labeled diagnostics.

**Exact missing inputs or definitions:** The actual test procedure and degrees of freedom, group contrast for each P value, the scope intended for the exclusion statement, and any retention-specific exemption are unavailable. Actual test output and individual data are not supplied.

**Source-grounded alternative interpretation:** The exclusion could have been intended only for cessation-outcome tests; alternatively, a separately defined two-arm retention contrast could have generated each P value while waitlist percentages were provided as context. Neither interpretation is identified next to the named tests. The three-group numerical match is not evidence sufficient to select the first interpretation.

**Direct observation versus inferred explanation:** Direct observations are the exclusion statement and the reporting of each P value alongside all three groups. Actual inclusion of waitlist participants in a Pearson test, or an unstated outcome-specific scope for the exclusion, remains inferred.

**Classification confirmed:** All substantive statements and corroborating flow counts are retrospective results/methods within one REPORT document. Primary relationship S_W; all relationships S_W; review domain statistical_results because the issue concerns statistical-test population/method attribution. No plan is substantively compared and no report-to-plan relationship is added. No classification correction. Classification ambiguity is the scope of the significance-test exclusion and actual contrast.

**Evidence state:** reproduced. **Decisive recheck fact:** The exact REPORT's waitlist test exclusion and its all-three-group retention P-value attribution remain unreconciled by a stated contrast or exception. Reproduction does not identify the underlying test.

**Exact remaining human question:** Which groups and test procedures generated retention P=.02 and P=.11, and what scope was intended for the waitlist exclusion from significance tests?

## C003 — Prequit intervention duration across supplied documents

**Location found; source value/text matched; comparator matched:** Yes, separately at every listed location:

| Exact supplied location | Content-confirmed role | Direct-source recheck fact |
|---|---|---|
| [Article p. 3, continuation of Vaping Cessation Intervention](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=3) | REPORT | Users who set a quit date receive messages six weeks before and eight weeks after their quit date. The adjacent no-date branch is four weeks. Visual inspection confirms a baseline numeral 6 describing weeks, not a superscript reference. |
| [Protocol p. 2, program description](../../../joi240078supp1_prod_1739900423.22574.pdf#page=2) | PLAN | Users who set a quit date receive messages for a week before and eight weeks afterward; the no-date/not-ready branch is four weeks. |
| [Protocol p. 4, Interventions](../../../joi240078supp1_prod_1739900423.22574.pdf#page=4) | PLAN | Trial intervention participants will receive This is Quitting messages as described above, linking the p. 2 schedule to trial intervention assignment. |
| [Results supplement p. 2, eAppendix A, Additional Detail About This is Quitting](../../../joi240078supp2_prod_1739900423.24574.pdf#page=2) | REPORT | One week preceding the quit date and eight weeks afterward; no-date users receive four weeks. Despite describing program procedures, this is retrospective additional detail about the delivered study methods, not a prospective plan. |
| [Protocol p. 15, Summary of Changes](../../../joi240078supp1_prod_1739900423.22574.pdf#page=15) | PLAN, context only | Assessment, decisional-capacity and fraud-prevention amendments are listed; no intervention-duration amendment appears. |

**Consistency rule applicable:** Yes, focus area D and Route B. Randomized intervention duration is an eligible substantive cross-document element. Comparators match the quit-date branch, program and prequit time direction. Neither the postquit period nor the no-date branch resolves which prequit schedule accompanied the primary trial result.

**Calculation and display-precision interval check reproduced:** The printed prequit durations are six versus one week. Conservatively allowing whole-week half-unit intervals gives [5.5,6.5] versus [0.5,1.5]. Their minimum gap is 5.5−1.5=4 weeks; relative discrepancy against the one-week reference is 4/1=4.00, above .05. The result applies separately to article versus protocol and article versus results supplement. Protocol and results supplement agree: interval gap zero. Nominal prequit-plus-postquit windows are 14 versus 9 weeks; these sums are descriptive diagnostics rather than claims about actual accumulated messages for users who reset a date. The mismatch persists even under the conservative display intervals.

**Necessary inputs available:** The exact three schedule descriptions, common eight-week postquit component, common four-week no-date branch, plan-to-intervention linkage, and amendment summary are available and matched. All duplicated finding locations were checked.

**Exact missing inputs or definitions:** The actual delivered message schedule for quit-date users, operative program version/date, treatment of quit-date resets, any distinction between an operational contact window and the stated treatment period, and any duration amendment are unavailable. Message-delivery logs are not supplied.

**Source-grounded alternative interpretation:** The program might have expanded between the planned and delivered versions, or an operational window could have been reported differently from a standardized schedule. The supplied texts name no such version difference or distinction. The no-date branch cannot account for the mismatch because all compared statements explicitly concern users who set a quit date.

**Direct observation versus inferred explanation:** Direct observations are the printed six-versus-one prequit-week descriptions and their linkage to the trial. A duration amendment, a distinct program version, or a particular delivered exposure is inferred and not established. The printed descriptions alone do not establish a change in treatment effect.

**Classification confirmed:** Article and eAppendix A are REPORT by retrospective content; protocol description, prospective intervention assignment and amendment page are PLAN. Article versus protocol is P_R; article versus the separate results REPORT is S_C. Primary relationship P_R by precedence P_R>S_C; all relationships P_R, S_C; review domain protocol_report. The agreement between protocol and supplement is corroboration and not an additional inconsistency. Amendment context does not create P_P. No classification correction. Classification ambiguity is the operative schedule/version.

**Evidence state:** reproduced. **Decisive recheck fact:** Direct source text and visual confirmation retain six prequit weeks in the article versus one in both substantive comparators, with a conservative relative interval gap of 4.00 and no supplied reconciliatory amendment.

**Exact remaining human question:** Which prequit schedule was delivered to participants setting a quit date, and how does it correspond to the prospective protocol and retrospective article/supplement descriptions?

## C004 — Planned moderator selection and reported testing family

**Location found; source value/text matched; comparator matched:** Yes, separately at every listed location:

| Exact supplied location | Content-confirmed role | Direct-source recheck fact |
|---|---|---|
| [Protocol p. 5, Primary Analysis, ending sentence](../../../joi240078supp1_prod_1739900423.22574.pdf#page=5) | PLAN | Potential moderators, including age, gender and motivation to quit, will be identified through treatment interactions with selected variables. The sentence continues on p. 6. |
| [Protocol p. 6, opening continuation](../../../joi240078supp1_prod_1739900423.22574.pdf#page=6) | PLAN | For all moderators found associated with the primary outcome, interaction effects will be examined after entering main effects. Both pages were read together; the qualifier was not detached from its context. |
| [Article p. 4, Statistical Methods](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4) | REPORT | Treatment-assignment interactions with variables reported in Table 1 were examined; eAppendix D is referenced. |
| [Article p. 5, Moderator Results](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=5) | REPORT | Analyses of all Table 1 variables as potential moderators yielded no statistically significant results after Holm adjustment. |
| [Results supplement p. 6, eAppendix D](../../../joi240078supp2_prod_1739900423.24574.pdf#page=6) | REPORT | All baseline characteristics described in Table 1 were examined one at a time; models include treatment and moderator main effects and interaction. Omnibus multi-category moderator P values enter Holm adjustment; individual contrasts are illustrative and excluded from the adjustment family. |
| [Results supplement p. 15, eTable 6](../../../joi240078supp2_prod_1739900423.24574.pdf#page=15) | REPORT | Twenty-five moderator hypotheses have adjusted P values. Lowest nominal P=.010 for GAIN-SS internalizing disorders is adjusted P=.250. The other categorical contrasts are distinguished from omnibus hypotheses. |
| [Protocol p. 15, Summary of Changes](../../../joi240078supp1_prod_1739900423.22574.pdf#page=15) | PLAN, context only | Baseline measure additions, decisional-capacity changes and fraud-prevention changes are disclosed. Added baseline measures do not specify the outcome-association condition or redefine the testing family. No moderator-selection amendment is identified. |

**Consistency rule applicable:** Yes, focus areas C/D and Route B. The plan affirmatively conditions moderator examination on association with the primary outcome, while the retrospective specification uses all baseline characteristics and a defined multiplicity family without connecting that family to the stated condition. This affects interpretation of the named no-adjusted-significant-moderator primary-outcome conclusion; it is not a preferred variable-selection method or a peripheral descriptive comparison.

**Logical comparison reproduced:** The exact plan qualifier and exact report's all-characteristic specification remain present. The report describes fitting and Holm family membership but does not identify an association gate, its definition, or which variables met it. The broad preceding plan language and additions of measures do not demonstrate how the condition produced the reported family. The comparison reproduces this unresolved planned-rule attribution; it does not establish that the condition was bypassed.

**Calculation and display-precision interval check:** The family comprises 6 demographic hypotheses, 5 vaping-related hypotheses, 6 nicotine/dependence hypotheses, 4 psychosocial hypotheses and 4 other-substance-use hypotheses, total 25. The smallest nominal printed P=.010 times 25 gives .250, matching the printed adjusted P=.250. Allowing three-decimal half-unit intervals, [.0095,.0105] times exact 25 gives [.2375,.2625], overlapping adjusted [.2495,.2505]. Residual discrepancy is zero; no Holm arithmetic inconsistency is registered. Numeric display precision does not resolve whether the stated outcome-association condition defined family membership.

**Necessary inputs available:** The complete plan continuation, report selection/fitting statements, multiplicity definition, all adjusted eTable 6 hypothesis rows and amendment page are available and matched. These reproduce the family-attribution question and check the ancillary arithmetic.

**Exact missing inputs or definitions:** The meaning and threshold of “associated with the primary outcome,” whether association means a main effect, an interaction, or prior evidence, association-screen results for each variable, operative family-selection specification, and any updated analysis plan are unavailable. Individual-level data are not supplied. These gaps prevent deciding whether all variables met the planned condition.

**Source-grounded alternative interpretation:** All listed variables could have satisfied the planned association condition; the preceding selected-variable/interactions wording could have intended an exploratory sequence broad enough to include all baseline variables; or an updated specification could have expanded the family. The article's baseline description links variables to e-cigarette-use associations, but this does not define or document the prospective condition's relationship to the primary abstinence outcome. No preferred family or selection approach is proposed.

**Direct observation versus inferred explanation:** Direct observations are the plan's condition, the report's all-variable specification and the 25-hypothesis adjusted table. Skipping the condition, satisfying it for all variables, or replacing it with a different specification are possible inferred explanations, not direct facts.

**Classification confirmed:** The prospective selection statement and amendment page are PLAN; the article and eAppendix D/eTable 6 are REPORT by retrospective analytic/result content. Primary relationship P_R; all relationships P_R; review domain protocol_report. Report sources describe the same family and corroborate each other; no S_C relationship is added. The amendment page creates no P_P inconsistency. No classification correction. Classification ambiguity is the definition and implementation of the selection condition.

**Evidence state:** reproduced. **Decisive recheck fact:** The exact prospective outcome-association qualifier is not connected in the supplied reporting locations to the explicitly reported all-characteristic, 25-hypothesis family. The reporting comparison persists while the Holm arithmetic reconciles.

**Exact remaining human question:** Was the protocol's primary-outcome association condition used, how was it defined, and which specification determined the reported 25-variable moderator testing family?

## C005 — Weighted odds-ratio upper confidence limit in eTable 5

**Location found; source value/text matched; comparator matched:** Yes. [Results supplement p. 14, eTable 5](../../../joi240078supp2_prod_1739900423.24574.pdf#page=14), a retrospective REPORT display, was read directly from the supplied PDF and visually checked. The 30-day IPRW Odds Ratio cell is 1.92 (1.50, 2.24), and its P-value cell is <.001. Column alignment confirms that 2.24 is an OR upper confidence limit. Every same-display comparator row was checked separately below. [Results supplement p. 5, eAppendix C](../../../joi240078supp2_prod_1739900423.24574.pdf#page=5), also REPORT, states that stabilized weights were used for survey-weighted logistic models via the survey package in R 4.0.2. It supplies method context but no distinct confidence-interval construction for this row.

**Consistency rule applicable:** Yes, focus areas B/C, Route A category 4. An upper-bound construction supported by all five other odds-ratio rows of the same display does not reproduce the weighted 30-day upper bound beyond the display-precision threshold. The rule is not an assumption about an unsupported method; the comparator pattern supplies the within-display support. It does not establish that the actual weighted procedure must have been log symmetric.

**Calculation and display-precision interval check reproduced:** For a log-symmetric odds-ratio confidence interval, U=OR squared/L. With each two-decimal OR and lower bound given its half-unit interval, monotonicity gives recomputed U in [(OR−.005) squared/(L+.005), (OR+.005) squared/(L−.005)]. Every printed upper bound also receives ±.005. All source triples and checks are listed here; the table is a recheck of one registered issue, not additional candidates.

| Exact eTable 5 row, OR column | Printed OR, lower, upper | Recomputed upper interval | Printed upper interval | Interval gap |
|---|---|---|---|---|
| 30-day CCA | 1.98, 1.55, 2.52 | [2.508440514,2.550307443] | [2.515,2.525] | 0 |
| 30-day Missing=Vaping | 1.57, 1.26, 1.95 | [1.936146245,1.976593625] | [1.945,1.955] | 0 |
| Repeated CCA | 2.65, 1.90, 3.70 | [3.672454068,3.719802111] | [3.695,3.705] | 0 |
| Repeated IPRW | 2.61, 1.87, 3.65 | [3.619213333,3.666608579] | [3.645,3.655] | 0 |
| Repeated Missing=Vaping | 2.34, 1.69, 3.22 | [3.216651917,3.263516320] | [3.215,3.225] | 0 |
| 30-day IPRW, affected cell | 1.92, 1.50, 2.24 | [2.436694352,2.478678930] | [2.235,2.245] | 0.191694352 |

For the affected cell, OR [1.915,1.925] and lower [1.495,1.505] yield the stated disjoint upper interval. Minimum gap is 2.436694352−2.245=0.191694352; relative discrepancy is 0.191694352/2.24=0.085577836, above .05. Central diagnostic OR squared/L is 2.4576; it is not a suggested final correction. Each comparator's gap and relative discrepancy are zero. In particular, the other IPRW row reproduces the construction within display precision. The printed affected point 1.92 lies within its printed bounds, the bounds exclude 1, and P<.001 is significant; this is not an interval-versus-significance conflict.

**Necessary inputs available:** All six exact OR triples, table/row/column identities, confidence level 95%, P-value cell and reported survey-weighted logistic method context are available and matched. These suffice for the within-display reproducibility comparison and conservative half-unit calculation.

**Exact missing inputs or definitions:** The actual interval algorithm for the weighted 30-day OR, whether it used a symmetric log-scale Wald interval or an asymmetric procedure, fitted coefficient/covariance output, weighting design/degrees of freedom, and any row-specific construction choice are unavailable. Raw data and the survey-model object are not supplied. These gaps prevent identifying the production mechanism or reconstructing an authoritative alternate interval.

**Source-grounded alternative interpretation:** An asymmetric or row-specific interval method for the survey-weighted model could yield the printed limits without matching U=OR squared/L. The source identifies survey-weighted logistic models but does not name such an interval distinction. This alternative remains for human review; Route A category 4 retains the observable within-display discrepancy.

**Direct observation versus inferred explanation:** Direct observations are the exact printed triple, the five exact comparators and their differing interval-arithmetic behavior. A substituted limit, a particular software convention or a particular intended limit is inferred and is not established. There is no demonstrated reversal of significance or direction and no demonstrated downstream propagation.

**Classification confirmed:** All six compared OR cells are retrospective REPORT results in the same document; eAppendix C is REPORT method context. Primary relationship S_W; all relationships S_W; review domain statistical_results. No PLAN or second REPORT document is substantively compared. No classification correction. Classification ambiguity concerns only the interval construction.

**Evidence state:** reproduced. **Decisive recheck fact:** Direct source text and visual table confirmation retain upper limit 2.24, and the independently recomputed minimum relative interval gap remains 0.085577836 while the same construction reproduces every other OR row.

**Exact remaining human question:** Which confidence-interval construction produced the weighted 30-day OR upper limit 2.24, and how does it relate to the construction of the other five OR intervals in eTable 5?

## Covered scope and remaining definitions

Covered stable IDs: C001, C002, C003, C004, C005; covered count 5. Evidence states: reproduced 5, reproduced_after_transcription_correction 0, not_reproduced 0. Classification corrections 0. Every merged duplicate location and cited amendment page was rechecked. Available source evidence supports each narrowly registered comparison; the actual primary adjustment model, retention-test contrasts, delivered prequit schedule, moderator-gate implementation and weighted interval construction remain the five substantive human questions. There is no unresolved source-access or transcription item. All supplied sources and reusable artifacts were preserved.
