# Cross-source consistency review

Scope: all matched result occurrences in DOC-001 REPORT PDF pp. 1–9 and DOC-003 REPORT PDF pp. 1–16; all planned versus reported statistical design specifications and plan-internal decision elements in DOC-002 PLAN PDF pp. 1–15. The complete main/support maps and the source inventory were read. QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Direct pdftotext -layout reads confirmed exact cited pages, including DOC-002 p. 15 amendments. Native text was used as a locator; no historical findings, old reports, web evidence, source changes, new rendering, or OCR were used. No supplied structured data exist. Results were matched on population, time, contrast, model, measure, analysis set, and precision. Counts below have no target interpretation.

## Findings

### F-XS-001

**Issue:** Prequit intervention duration differs between main article and protocol/results supplement.

**Exact compared locations and document roles:** [DOC-001 p. 3, Vaping Cessation Intervention](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=3), REPORT; [DOC-002 p. 2, program description](../../../joi240078supp1_prod_1739900423.22574.pdf#page=2), PLAN; [DOC-002 p. 4, assigned intervention refers to that description](../../../joi240078supp1_prod_1739900423.22574.pdf#page=4), PLAN; [DOC-003 p. 2, eAppendix A](../../../joi240078supp2_prod_1739900423.24574.pdf#page=2), REPORT. [DOC-002 p. 15](../../../joi240078supp1_prod_1739900423.22574.pdf#page=15), PLAN, contains the disclosed amendments and no duration amendment.

**Printed values:** Main article: participants setting a quit date receive messages “6 weeks before and 8 weeks after their quit date.” Protocol: “a week before and 8 weeks afterward.” Results supplement: “1 week preceding their quit date and 8 weeks afterward.” All refer to This is Quitting participants who set a quit date; all distinguish the 4-week schedule for users without a quit date.

**Comparison logic:** Same arm, quit-date condition, and prequit interval, not a different follow-up or no-quit-date schedule. Six and one prequit weeks give nominal total quit-date schedules of 14 and 9 weeks, respectively. Even applying conservative integer half-unit intervals, the prequit intervals [5.5, 6.5] and [0.5, 1.5] weeks are disjoint by 4 weeks; relative discrepancy against the one-week copy is 4/1 = 4.00 (>0.05). The specified durations are discrete schedules, so this rounding allowance is conservative.

**Focus area:** D (randomized intervention duration). **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R, S_C.

**Qualifying route:** Route B.

**Affected result or extracted value:** Duration of the intervention producing the primary 7-month abstinence result, RR 1.35 (1.17–1.57), and extraction of the intervention schedule.

**Why context does not resolve it:** Both schedules are stated affirmatively for users setting a quit date; the adjacent 4-week no-date schedule and agreed 8-week postquit component do not identify whether the delivered prequit exposure was one or six weeks. This is a quantity-changing duration discrepancy, in focus and relevant to extraction.

**Supported alternatives / missing definition:** Main article could describe an updated six-week schedule, while the supplement/protocol describe a one-week schedule; alternatively the one-week schedule may have been delivered. The package does not document such a duration amendment or identify the operative schedule. These are alternatives, not an inferred production mechanism.

**Human question:** Which prequit message duration was delivered to randomized intervention participants who set a quit date, and which supplied description should be used to extract that intervention?

### F-XS-002

**Issue:** The explicitly planned covariate-adjusted primary estimate is not identified in the supplied results.

**Exact compared locations and document roles:** [DOC-002 p. 5, Data Analysis Plan / Primary Analysis](../../../joi240078supp1_prod_1739900423.22574.pdf#page=5), PLAN; [DOC-001 p. 4, Statistical Methods](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4), REPORT; [DOC-001 p. 5, Vaping Cessation](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=5), REPORT; [DOC-001 p. 6, Table 2](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=6), REPORT; [DOC-003 p. 14, eTable 5](../../../joi240078supp2_prod_1739900423.24574.pdf#page=14), REPORT. [DOC-002 p. 15](../../../joi240078supp1_prod_1739900423.22574.pdf#page=15), PLAN, discloses no primary-model amendment.

**Printed statements and results:** Protocol states that 7-month ppa will be compared using logistic regression and “All estimates will be adjusted for baseline confounders of the intervention-outcome relationship.” Main Methods state ordinary logistic regression and ITT missing=vaping, without identifying baseline-confounder adjustment or an adjusted primary result. Main primary rates are 287/759 and 208/744, RR 1.35 (1.17–1.57), OR 1.57 (1.26–1.95). eTable 5 repeats these under Missing=Vaping; its other rows are labeled CCA and IPRW rather than baseline-confounder-adjusted primary analysis.

**Comparison logic:** The prospective statement commits to adjusted primary estimates. None of the supplied primary result displays identifies that adjustment or the planned adjusted result. The displayed point estimates also reproduce simple marginal counts: (287/759)/(208/744) = 1.35254; (287×536)/(472×208) = 1.56690. This arithmetic corroborates the distinction but does not establish that hidden covariates were absent, and no model-versus-crude discrepancy is asserted. The finding is the planned primary adjusted analysis not being reported as such, grounded in the affirmative plan commitment, rather than an unsupported assumption about an unstated model. Display-precision interval arithmetic is not applicable to this categorical analysis-specification comparison.

**Focus area:** D (primary analysis and covariates). **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Whether the primary 7-month treatment effect RR 1.35 and OR 1.57 represent the planned baseline-adjusted estimate, or a different primary analysis; the adjustment status used in evidence extraction.

**Why context does not resolve it:** Route A category 5 covers a planned primary analysis not reported. Ordinary logistic regression can include covariates, but neither an identifiable adjusted estimate nor a description linking those covariates to the displayed primary result is supplied. IPRW is separately labeled a missing-data secondary analysis and does not identify the protocol's promised primary adjustment.

**Supported alternatives / missing definition:** The reported ordinary logistic model may include undisclosed baseline adjustment; the adjusted planned analysis may have been replaced by a marginal treatment-only analysis; or no baseline factors were selected as confounders. The package identifies neither the covariate set/selection rule nor an amendment resolving the prospective commitment.

**Human question:** Was the protocol's baseline-confounder-adjusted primary logistic analysis performed, and which supplied primary estimate and covariate specification report it, or what documented change led to the displayed primary analysis?

### F-XS-003

**Issue:** The reported moderator testing strategy does not retain the outcome-association selection condition stated in the plan.

**Exact compared locations and document roles:** [DOC-002 p. 5, Primary Analysis](../../../joi240078supp1_prod_1739900423.22574.pdf#page=5) and [DOC-002 p. 6, continuation](../../../joi240078supp1_prod_1739900423.22574.pdf#page=6), PLAN; [DOC-001 p. 4, Statistical Methods](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4) and [DOC-001 p. 5, Moderator Results](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=5), REPORT; [DOC-003 p. 6, eAppendix D](../../../joi240078supp2_prod_1739900423.24574.pdf#page=6) and [DOC-003 p. 15, eTable 6](../../../joi240078supp2_prod_1739900423.24574.pdf#page=15), REPORT. [DOC-002 p. 15](../../../joi240078supp1_prod_1739900423.22574.pdf#page=15), PLAN, contains no moderator-strategy amendment.

**Printed statements:** Protocol p. 5 proposes potential moderators (age, gender, baseline motivation) via treatment interactions; the continuation says “For all moderators found to be associated with the primary outcome, we will examine the effects of treatment/moderator interaction terms on outcomes after entering main effects.” Main paper instead says interactions with variables in Table 1 were examined; eAppendix D explicitly states all baseline characteristics were examined “one moderator at a time,” each model containing treatment, moderator and interaction. eTable 6 supplies 25 variable-level tests, adjusted via Holm, and the reported conclusion is no adjusted-significant moderator.

**Comparison logic:** Item-by-item analysis specification: planned outcome association condition versus reported all-characteristic selection; both retain main effects plus interaction, but the report specifies a 25-variable multiplicity family without the plan's association gate. This is an observable planned-versus-reported analysis specification discrepancy, not a claim that any particular moderator should or should not be tested. Exact outcome-association test results used to implement the gate are unavailable. No numerical rounding comparison applies.

**Focus area:** D (prespecified primary-outcome moderator analysis and selection rule). **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The primary-outcome moderator conclusion repeated in abstract, Key Points, results and discussion, including the treatment-effect interaction P values and their Holm adjustment family.

**Why context does not resolve it:** The selection criterion can alter which interaction analyses are in the multiplicity family underlying the no-moderator conclusion. The report's explicit all-characteristic strategy does not state whether all variables first satisfied the plan criterion or whether that criterion was changed; the supplied amendments do not address it. The discrepancy therefore affects interpretation of a specifically reported primary-outcome analysis.

**Supported alternatives / missing definition:** All reported variables may have met the plan's outcome-association criterion, making the practical model set coincide; the criterion may instead have been replaced by all-characteristic screening. The exact gate definition and implementation are not supplied. The protocol's earlier broad statement about analyzing selected interactions may have been intended to authorize broad exploratory screening, but its subsequent criterion remains unresolved.

**Human question:** Was the protocol's outcome-association condition used to select moderator interaction analyses, and how does that selection correspond to the 25-variable Holm family reported in eTable 6?

## Complete matched-result and design checks

The tables record reconciled checks and scope completion separately from excluded apparent issues. Main mapper N001–N064/S001–S021 and support mapper N201–N214/S201–S214 were covered; their IDs are locators, not findings.

| Matched evidence scope | Explicit comparison and result |
|---|---|
| Abstract, Key Points, main Results and flow, DOC-001 pp. 1, 2, 4, 6 | Primary I/C randomized denominators 759/744 sum to 1503. Flow third arm 178 expands total to 1681; different populations are disclosed. Main-group 7-month responses 521+543=1064 yield 70.8%; adding waitlist 132 yields 1196/1681=71.1%. Both match their population. |
| Abstract demographics versus Table 1 and narrative, DOC-001 pp. 1, 4, 5 | Age16.4(SD0.8), female50.6, male42.1, nonbinary/other7.4, Black10.2, White62.6, multiracial18.5, other-race8.7, Hispanic16.2, LGBQ+42.5 and within30min76.2 match the corresponding pooled available-denominator quantities and printed precision. No reversed arm or outcome assignment. |
| Primary result across DOC-001 pp. 1, 2, 5, 6, 7 and DOC-003 pp. 5, 14 | ITT Missing=Vaping rates37.8(34.4–41.3)/28.0(24.9–31.3), RD9.9(5.1–14.5), RR1.35(1.17–1.57), OR1.57(1.26–1.95), P<.001 match exactly where repeated. Discussion35% greater chance corresponds RR1.35, not OR1.57. |
| Repeated abstinence across DOC-001 pp. 3–7 and DOC-003 pp. 5, 14 | Definition is 30-day abstinence at both1/7mo. Counts131/61 in supplement match rates17.3/8.2 using759/744; all Table2 and eTable5 Missing=Vaping intervals/effects/P match. Discussion more than twice corresponds RR2.10. |
| CCA and IPRW primary/repeated results across DOC-001 p. 5 and DOC-003 pp. 5, 14 | CCA RR1.44(1.26–1.64), repeated2.24(1.70–2.94), IPRW1.42(1.24–1.63), repeated2.21(1.67–2.93), P<.001 identical. Available-case denominators521/543 and517/538 are distinguished from randomized759/744 and normalized weighted cases. |
| MI narrative and grid, DOC-001 pp. 4–5; DOC-003 pp. 4, 11 | Direction, range RR1.26–1.35/OR1.57–1.84, 1/100 and100 endpoints, and positive treatment effects match. Finite sensitivity estimates differ from ITT as different analyses, not copied identical results. |
| Baseline main/supplement constructs, DOC-001 Tables1/footnotes; DOC-003 eTables1,2,4 | Every shared demographic category, dependence scale, GAIN subscale, loneliness scale, PEARLS risk category and substance-use measure aligned by definition, arm and available N. eTable4 responder/nonresponder groups are partitions rather than the treatment groups; contributor Ns are not conflated with analysis denominators. |
| Retention-predictor text versus eTable4, DOC-001 p. 5 and DOC-003 pp. 12–13 | Named variable-level associations correspond to adjusted P<.05; sexuality nominal.028/adjusted.364 and cigarettes.047/.517 are appropriately absent from adjusted-significant list. eTable4 does not report weighted post-IPRW cells, so postweighting balance cannot be numerically compared to an identical display. |
| Moderator claims versus eAppendixD/eTable6, DOC-001 pp. 1,2,4,5,7 and DOC-003 pp. 6,15 | All25 Holm-adjusted family tests nonsignificant; lowest variable-level nominal P .010 becomes .250; individual category contrasts excluded from adjustment as stated. Reference coding remains assessment-only; no cross-location sign or P copy conflict. Planned selection condition separately F-XS-003. |
| CTP narrative, Table3 and abstract, DOC-001 pp. 1,4–7 | Complete-case n1016=501+515, baseline598+418, four states445/326/30/215 agree. Dual abstinence52.9 vs35.0, difference17.9(11.9–23.8); baseline exclusive54.3 vs38.6 and dual50.8 vs30.0 match cells. Baseline CTP41.1 to24.1 reduction17.0 matches categories. Ten exclusive-CTP quitters match3+7; no alternate supplied analysis compares the same contrast. |
| Plan primary endpoint/time/contrast, DOC-002 pp. 3,5 versus DOC-001 pp. 1–4 | Self-reported30-day ppa at7mo, intervention versus assessment-only, individual allocation and main1800 target reconcile. Primary superiority direction intervention more abstinent; no noninferiority/equivalence margin in any supplied source. The report explicitly refers to nicotine-containing devices; plan broad vaping-screening text is considered separately below. |
| Analysis-set and missing-data rules, DOC-002 pp. 3–6 versus DOC-001 pp. 2–4; DOC-003 pp. 4–5 | Original-arm ITT, missing=vaping, supplement NMAR sensitivity, baseline completion/welcome-text enrollment and third-arm exclusion from primary sample-size calculation reconcile. No additional per-protocol set or eligibility-driven analytic exclusion is specified. CCA/IPRW explicitly supplementary analyses. |
| Planned adjustment and moderator analysis, DOC-002 pp. 5–6 versus report methods/results | Logistic model class and moderator main-effects/interaction structure match. Adjustment and selection differences documented separately in F-XS-002 and F-XS-003. |
| Sample-size/power/hypothesis direction, DOC-002 pp. 3,6 versus DOC-001 p. 3 | Plan main1800/900per-arm with ancillary waitlist450; report same target, achieved1503/1800=83.5%, budget stopping disclosed. Plan does not print20%/15%,80% power,.05 alpha assumptions to contradict reported inputs. No plan-internal conflicting sample-size input or margin found. |
| Multiplicity/interim/stopping, DOC-002 p. 10; DOC-001 pp. 2–5; DOC-003 pp. 6,15 | Plan leaves interim frequency/masking and benefit/futility/safety rules to DSMB; no numerical boundary exists to compare. Report budget termination is explicit, not claimed as a statistical boundary crossing. Holm adjustment is disclosed for response-predictor and moderator families; no plan specifies an alternative multiplicity rule. |
| Secondary outcomes/analyses, DOC-002 pp. 3,5,6 versus DOC-001 pp. 3,4,8 | Plan lists motivation, attempts, reduced use,7-day ppa,continuous abstinence,satisfaction/engagement and mediation. No outcome other than7-month30-day ppa is explicitly designated key secondary. Article gives repeated ppa and post hoc CTP; it expressly reserves mediation and cannabis/alcohol changes for further work. The primary endpoint has not been replaced. |
| Plan amendments and internal versions, DOC-002 p. 15 versus pp. 3–8 and DOC-001 pp. 2–5 | Added loneliness/PEARLS, simplified decisional questionnaire and second opportunity, added fraud withdrawal/attention checks each reconciled with report timing/missingness and enrollment statements. No primary-model/duration amendment supplied. Primary endpoint, ITT rule, main target and follow-up schedule consistent throughout bound plan. |

### Item-by-item criterion comparison

| Criterion list | Each item examined and matched result |
|---|---|
| Eligibility | Age13–17; past30-day e-cigarette use; interest quitting next30days; US residence/IP criterion; contact phone/email and text enrollment. Main mobile phone/active text plan operationalizes planned texting requirement. No altered numerical age/use/quit window. Plan nicotine-or-THC screening wording does not provide a separate analysis-set denominator in report. |
| Enrollment / analysis-set entry | Baseline completed; assent; decisional capacity; text enrollment; response to initial welcome within24h; retain original treatment assignment; nonresponse at follow-up coded vaping. Main flow counts pre-enrollment exclusions separately and both main arms analyzed fully. Plan p.15 permits second capacity-question opportunity and fraud withdrawal; main does not assert these were forbidden. |
| Seven decisional-capacity items | Study purpose; participation voluntary; what agreement entails; possible lack of benefit/harm; possible benefit; how to leave; consequences of declining. Main summarizes seven questions without substituting a different criterion list; amendment changes answer format/second opportunity. |
| Primary success criterion | Self-reported absence of vaping in past30days at7mo; ITT missing=vaping. Repeated ppa has separate1/7mo criterion. No main composite adds CTP abstinence to the primary endpoint; CTP dual abstinence is explicitly post hoc. |
| Other planned quitting outcomes | Motivation change; quit attempts; reduced use;7-day ppa;continuous abstinence. Report repeated ppa is not silently equated to continuous abstinence. No category is expressly designated key secondary in plan; absence of other non-key results does not establish replacement of primary endpoint. |
| Satisfaction / mediators | Overall/recommendation0–10;frequency satisfaction;personal relevance;engagement messages/date/keywords/unsubscribe/days;social support/self-efficacy changes. Article has no supplied estimates for these, and identifies mediation outside manuscript scope. |
| Primary model | Logistic; baseline-confounder adjustment;potential-moderator interactions;association gate;main effects before interaction. First and final structure reconcile; adjustment and association gate require human clarification as recorded. |
| Missingness | ITT failures;NMAR MI;OR.miss1–5;reported sensitivity includes those values and additional assumptions;no change in original assigned-group counts. |
| Interim / stopping | Frequency to be determined;masking to be determined;possible benefit/futility/safety guidelines to be discussed;DSMB quorum half+one/three. No asserted numeric decision threshold to contrast with report's budget stopping. |

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-002 pp. 5–6; DOC-001 pp. 3–4 | Repeated ppa is named among “Primary outcome analyses,” while plan primary endpoint is7-month30-day ppa and other abstinence outcomes are secondary. Main abstract/Measures explicitly preserve the single primary endpoint; “primary outcome analyses” alone does not assert repeated ppa is co-primary, and repeated is not described as prespecified continuous abstinence. | TERMINOLOGY_OR_WORDING |
| DOC-002 p. 6; DOC-003 pp. 4,11 | Report expands OR.miss grid beyond planned1–5 while retaining1,1.25,1.5,2,3,5 and the planned NMAR analysis; report calls it broad sensitivity exploration, not an amended primary estimand. | CONTEXT_RESOLVES |
| DOC-001 p. 6 Table2; DOC-003 p. 11 eTable3 | eTable3 +infinity rates37.98/28.06 and RD9.92 versus ITT37.8/28.0/RD9.9. Half-unit gaps .125/.005/0 for intervention/control/RD; relative discrepancies .00331/.00018/0, all ≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p. 5 Table1; DOC-003 p. 9 eTable2 | Control health-concern summary is mean3.4(SD1.2) in main and median3.0(IQR3–4) in supplement. These descriptive baseline copies use different summaries; no primary/key secondary result or analysis-population denominator changes. | PERIPHERAL_COMPARISON |
| DOC-002 p. 5; DOC-001 pp. 1–3 | Plan screening specifies nicotine-or-THC e-cigarette use; report instructs nicotine-device reporting and describes nicotine vaping objective. No supplied explicit THC-only subgroup count, exclusion, or alternative primary endpoint definition demonstrates an analysis-population discrepancy. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 p. 5; DOC-003 pp. 12–13 | Male/Black/multiracial named predictors of nonresponse, while their marginal proportions are larger in responders. “Predictors” does not itself state an increased-risk coefficient; no conditional retention coefficients are printed to establish a reversed model claim. | CONDITIONAL_OR_UNREPORTED |
| DOC-002 pp. 3,5–6; DOC-001 p. 8 | Mediation and other non-primary quitting outcomes are not supplied as results; mediation is expressly outside manuscript scope. No additional outcome is designated key secondary or reported as replaced, so omission alone does not reproduce a route-A category5 primary/key-secondary omission. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 p. 2 versus p. 4 | Waitlist described as excluded from significance tests, but retention paragraph lists all three arm rates beside P=.02/.11. The test scope is not specified; a two-main-arm test could accompany ancillary descriptive third-arm rates. No supplied statement affirmatively identifies the P values as three-arm tests. | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

Cross-source review complete: 40/40 direct pages represented by complete source maps; all matched main numeric/statistical and support relationships compared; three findings emitted, eight apparent observations excluded. No scientific coverage gap. No separate supplied final SAP/DSMB charter, covariate-adjusted model output, or retention-model coefficients exist; their absence is identified where it limits mechanical reconciliation, without treating missing raw evidence as a new finding. No source or reused asset modified. No C IDs or adjudication judgments assigned.
