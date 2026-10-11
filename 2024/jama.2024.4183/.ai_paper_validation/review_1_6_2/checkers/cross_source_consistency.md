# Cross-source consistency review — Workflow 1.6.2

Status: COMPLETE. Assigned scope: all matched quantitative relationships and prospective statistical-design comparisons across DOC-001 REPORT (10 physical pages), DOC-002 PLAN (45 physical pages), and DOC-003 REPORT (36 physical pages). Eleven findings and twelve excluded observations are recorded. No candidate IDs or AI adjudications are assigned.

## Sources, methods, and complete comparison coverage

Read QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md, settings.toml, source inventory, source coverage, tooling record, and both new canonical extraction maps. The support map includes the complete disjoint protocol map. Reusable source-matched text and new maps were locators; direct Poppler pdftotext 26.01.0 extraction from the cited physical PDF pages confirmed printed findings. Current direct-source renders of DOC-003 p.16 and DOC-002 p.8 were visually inspected for the six-month figure and biochemical/MINI eligibility criteria; mapper visual transcriptions of other figures were checked against their source-page text, captions, and matching records. CPU; no fresh OCR, fallback environment, web, raw data, or old scientific conclusions used. No supplied structured data or Office source exists. All sources and reusable assets were preserved.

The comparison keys were population, initial medication, six-week response, second-stage treatment, outcome definition, time origin/window, contrast direction, model, measure, analysis set, and displayed precision. Bayesian posterior probabilities and credible intervals were distinguished from crude counts and from the explicitly post hoc frequentist GEE pathway estimates. Anticipated simulation results were not matched as observed results.

| Comparison scope | Complete assessment |
|---|---|
| Main abstract, Key Points, narrative, Table, Figures 1–3, captions and footnotes | All 55 main numeric and 28 statistical map records compared with matching locations. The eight week-12 cells, two initial-treatment counts, six rescue cells, responder contrast, primary RDs, and longer-term conclusions were matched individually. Main primary probabilities/counts agree across body and Figure 3; discrepancies are recorded below. |
| Report supplement | All 20 numeric and 36 statistical groups inspected: eAppendices 1–5, eFigures 1–3, eTables 1–12, every displayed row and associated definitions. Each primary eTable 4 contrast was matched with the main body where available; every secondary figure cell was matched with summaries, detailed text and eTables 9–11. Adherence, safety, baseline and post hoc populations were kept distinct. |
| Primary endpoint and response rule | Seven-day abstinence, week 12, expired CO below 6 ppm, six-week response, and six-plus-six-week medication phases reconcile between report and plan. Primary outcome is not a composite of several independent clinical events. Tobacco terminology expands explicitly to little cigars/cigarillos in the plan; this does not itself identify a different printed outcome. |
| Secondary definitions and status | Continuous abstinence at EOT plus 30 days and six months is expressly planned and reported as secondary. Continuous versus prolonged, three-month versus six-month, and EOT versus quit-date origins were checked separately. Planned secondary prolonged abstinence and exploratory symptom/moderator analyses have no printed primary/key-secondary replacement or status reclassification established here; exclusion rows address the apparent omissions. |
| Intervention | Initial 21-mg patch plus 2-mg lozenge versus 2-mg daily varenicline; switch titration; augmentation to 42-mg patch retaining 2-mg lozenge versus 3-mg daily varenicline; treatment start, six-week decision, six additional weeks, double dummy, and permitted adverse-event dose modification compared item by item. The simulation-figure lozenge dose differs below. |
| Eligibility criteria | Individually matched age, smoking minimum and preceding period, biochemical criterion/exception, treatment interest, English ability, consent, reachable address/phone, household restriction, other tobacco, other cessation treatment, hypertension, renal/liver thresholds, unstable disease, recent cardiovascular history, each medication category, MINI modules, suicidality, hospitalization, pregnancy/contraception, hypersensitivity, investigator safety discretion, suitability/follow-up and toxicology prescriptions/retest exceptions. Summarized or unreported details alone were not converted to findings. Two categorical population-definition differences are recorded below. |
| Primary analysis and analysis set | Logistic response model, initial-treatment and rescue indicators/interactions, each Aim 1–3 contrast, IPW, responder versus nonresponder sets, ITT, missing=smoking, retained off-drug follow-up, one excluded randomized person and deterministic continuation assignment compared. Planned conditional confounder adjustment was distinguished from unconditional missingness/prior sensitivity analyses. |
| Statistical design and plan-internal rules | Priors and fitting revision; sample size 500, pilot allowance, K=1000, all ten beta-distribution inputs, eight simulated cells and each power-table contrast/threshold; all Aims 1–7 and exploratory status; inferential threshold; multiplicity, noninferiority/equivalence margins, hypothesis direction, interim and stopping checked. No noninferiority/equivalence margin or current-trial efficacy interim/stopping boundary is supplied, so absence does not establish a conflict. Future adaptive arm dropping is explicitly future-trial context. |
| Criterion lists inside plan | Eligibility and safety exception lists, augmentation tolerability criteria, seven-day/continuous/prolonged abstinence criteria, imputed-smoking/retention rules, responder/nonresponder contrast sets, and posterior-probability advancement rule checked item by item. Conditional future plans were kept distinct from present decision rules. Symbol/heading observations excluded below did not establish a distinct numerical result. |

## Findings

### F-XS-001

**Issue:** The abstract gives a different lower credible limit for primary CNRT rescue contrasts.

**Exact locations and roles:** REPORT [main p.1 abstract](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1); REPORT [main p.5, Smoking Cessation End of Phase 2](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5); REPORT [supplement p.21, eTable 4, CNRT increase/switch versus stay](../../../joi240036supp2_prod_1716416466.01349.pdf#page=21).

**Printed values:** Abstract combines switching and dose increase as RD 6%, 95% CrI 6%–11%. Body combines them as RD 6%, 2%–11%. eTable 4 prints increase 6% (2%–11%) and switch 6% (2%–10%). Population is six-week CNRT nonabstainers; endpoint is week-12 seven-day abstinence; reference is continuation.

**Comparison logic:** The lower-limit copies 6 and 2 have half-unit intervals [5.5,6.5] and [1.5,2.5] percentage points. Gap=3; relative discrepancy=3/6=0.50, above 0.05. Upper-limit copies 10 and 11 have touching rounding intervals and are not an additional finding.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_C; **All relationships:** S_C, S_W.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** The lower 95% credible limit of the primary rescue-versus-continuation RD for initial CNRT nonabstainers.

**Why context does not resolve it:** This is a reproduced printed interval-limit difference. Reconstruction from the body does not remove the abstract reading under category 2.

**Supported alternatives:** The common abstract interval may summarize the increase contrast, the switch contrast, or a pooled contrast; no separate pooled model is identified.

**Exact human question:** Which lower credible limit and which contrast should be used for the abstract's 6% CNRT rescue benefit?

### F-XS-002

**Issue:** The primary varenicline switch contrast has conflicting direction and treatment attribution.

**Exact locations and roles:** REPORT [main p.1 abstract](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1); REPORT [main p.5, varenicline nonabstainers](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5); REPORT [main p.7 Figure 3](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7); REPORT [supplement p.21 eTable 4, switch CNRT versus varenicline stay](../../../joi240036supp2_prod_1716416466.01349.pdf#page=21).

**Printed values:** Switch to CNRT has 0/41 and 0% (0%–0%); continuation has 2/77 and 3% (1%–4%); increase has 8/39 and 20% (16%–26%). Body specifies switch relative to continuation RD −3% (−4% to −1%), then says the >99% probability means “continuing was worse than switching.” Abstract associates RD −3% with continuing being worse than switching to a higher dosage, although its next sentence gives the higher-dose contrast RD 18% (13%–24%). eTable 4 instead prints the labeled switch-versus-stay ARD as positive 3% (1%–4%).

**Comparison logic:** In the stated body switch-minus-continuation contrast, a negative RD favors continuation on an abstinence scale. The printed 0% versus 3% cell probabilities support that direction. Higher dose is a distinct 20% cell and an 18% RD. Reversing the contrast explains positive 3%, but the eTable label remains switch versus stay. No rounding can reverse the signs or exchange the switch and increased-dose cells.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_C; **All relationships:** S_C, S_W.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Direction/reference and intervention identity for the primary 3-percentage-point varenicline continuation-versus-CNRT-switch comparison.

**Why context does not resolve it:** Category 2 applies to a direction statement reversing printed values; the abstract also attaches that numerical result to a different rescue strategy.

**Supported alternatives:** The body direction sentence may describe switch-minus-continuation with its favored group reversed; eTable 4 may use unsigned absolute magnitudes; the abstract sentence may intend the separate increased-dose benefit. These alternatives do not identify one consistent contrast throughout.

**Exact human question:** For the −3%/3% primary result, which treatment is the reference, which is favored, and should the abstract describe switching to CNRT or increasing varenicline?

### F-XS-003

**Issue:** Repeated decimal shifts change printed secondary abstinence estimates and credible limits.

**Exact locations and roles:** REPORT [supplement p.10, detailed EOT+30 CNRT/varenicline analysis](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10); REPORT [supplement p.11, varenicline continuation and abstainer analyses](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11); REPORT [supplement p.12, six-month abstainer analysis](../../../joi240036supp2_prod_1716416466.01349.pdf#page=12); REPORT matching [p.15 eFigure 2](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15), [p.33 eTable 9](../../../joi240036supp2_prod_1716416466.01349.pdf#page=33), [p.34 eTable 10](../../../joi240036supp2_prod_1716416466.01349.pdf#page=34), and [p.35 eTable 11](../../../joi240036supp2_prod_1716416466.01349.pdf#page=35).

**Printed values and all affected occurrences:** p.10 CNRT switch probability 1.0% (7.0%–1.3%) versus eFigure 2 10% (7%–13%); p.10 CNRT increase 8.0% (5.0%–1.1%) versus 8% (5%–11%); p.10 CNRT switch RD 6.0% (3.0%–1.0%) versus eTable 9 6% (3%–10%). p.10 varenicline increase probability 8.0% (5.0%–1.1%) versus 8% (5%–11%). p.11 varenicline increase-versus-continuation RD and increase-versus-switch RD each 8.0% (5.0%–1.1%), versus corresponding eTables 9/10 8% (5%–11%). p.11 responder CNRT-versus-varenicline RD 1.1% (−1.0%–22%) versus eTable 11 11% (−1%–22%). p.12 six-month responder RD 1.0% (−1.3%–1.1%) versus eTable 11 1% (−11%–12%).

**Comparison logic:** The p.10 limits 7.0–1.3, 5.0–1.1 and 3.0–1.0 are reversed and exclude their associated point estimates; category 1 applies independently of rounding. For shifted copied values, the respective half-unit gaps and relative discrepancies, using the detailed narrative as reference, are: 1.0 versus 10: [0.95,1.05] versus [9.5,10.5], gap8.45, relative8.45; 1.3 versus13: gap11.15, relative8.58; 1.1 versus11: gap9.35, relative8.50; 1.0 versus10: gap8.45, relative8.45. The six-month negative limits −1.3 versus−11 have gap9.15/1.3=7.04; positive limits1.1 versus12 have gap10.35/1.1=9.41. All exceed0.05.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W; **All relationships:** S_W.

**Qualifying route:** Route A, category 1; the repeated numeric shifts also satisfy Route A, category 2.

**Affected result or extracted value:** Each specified secondary cell probability, RD, and credible limit, including the abstract's key six-month continuous-abstinence outcome.

**Why context does not resolve it:** Point estimates outside their intervals and printed digit/decimal changes are always-register categories. Other displays supplying plausible alternatives do not remove the printed readings.

**Supported alternatives:** The figures/tables supply the larger values listed above; the source does not disclose a different model for the detailed narrative. The six-month responder direction also differs in wording between narrative and table; no additional numerical sign is inferred here.

**Exact human question:** Which estimate and interval should be extracted at every listed detailed-analysis location, and do any represent an analysis different from their cited figure/table counterparts?

### F-XS-004

**Issue:** Six-month CNRT summaries label an RD as a treatment-group abstinence rate and give a different continuation rate.

**Exact locations and roles:** REPORT [main p.7 Secondary Outcomes](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7); REPORT [supplement p.10 summarized analysis](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10); REPORT [supplement p.11 detailed six-month CNRT analysis](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11); REPORT [supplement p.16 eFigure 3](../../../joi240036supp2_prod_1716416466.01349.pdf#page=16); REPORT [supplement p.33 eTable 9](../../../joi240036supp2_prod_1716416466.01349.pdf#page=33).

**Printed values:** Main p.7 and supplement p.10 describe the CNRT patch-increase condition as 3% and continuation as 0%, with96% probability of a nonzero difference. Detailed p.11 and eFigure 3 give increase6% (4%–9%;3/50), continuation3% (2%–5%;3/90), and eTable 9 gives the increase-minus-continuation RD3% (0%–6%) with96% probability. The0% continuation rate belongs to the initial-varenicline branch, not CNRT.

**Comparison logic:** Match six-month post-quit continuous abstinence, initial CNRT, six-week nonresponse, and the same second-stage cells. Rate3 versus6: half-unit intervals[2.5,3.5] and[5.5,6.5], gap2/3=0.667. Continuation0 versus3 has a2-percentage-point interval gap against a printed zero, which qualifies. The RD3% and cell rate6% are distinct quantities.

**Focus area:** B. **Proposed review domain:** report_internal_inconsistency. **Proposed relationship:** S_C; **All relationships:** S_C, S_W.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** The key secondary six-month CNRT-increase and CNRT-continuation abstinence rates and their distinction from the RD.

**Why context does not resolve it:** The same3% reading could be extracted as a cell probability or an RD; the0% reading identifies a different initial-treatment population. Category2 covers the printed magnitude changes.

**Supported alternatives:** The summaries may intend to describe the3% absolute benefit instead of the6% cell probability and may carry forward the varenicline continuation0%. No separate CNRT population/model is specified.

**Exact human question:** Should six-month CNRT increase and continuation be reported as6% and3%, with RD3%, or do the summary3% and0% refer to another analysis?

### F-XS-005

**Issue:** The report describes a posterior-benefit threshold of0.80 as prespecified, while the supplied protocol specifies0.90.

**Exact locations and roles:** PLAN [protocol p.31, advancement criterion](../../../joi240036supp1_prod_1716416466.00349.pdf#page=31); PLAN [protocol p.33–34 power definition/Table3](../../../joi240036supp1_prod_1716416466.00349.pdf#page=33) and [p.34](../../../joi240036supp1_prod_1716416466.00349.pdf#page=34); REPORT [main p.4 sample size and statistical plan](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4); REPORT [supplement p.9 prespecified confirmation criterion](../../../joi240036supp2_prod_1716416466.01349.pdf#page=9).

**Printed values:** Protocol: posterior probability>0.90 that the postulated effect exists constitutes sufficient evidence for further evaluation in a confirmatory phase. Report: >0.80 was prespecified as sufficient for confirmation of hypotheses, clinical decisions and future trials. Both materials evaluate power at0.80,0.85,0.90,0.95, but only the protocol prose selects>0.90 as its advancement rule.

**Comparison logic:** Presence of an0.80 column in a simulation table is not a statement selecting0.80 as the decision criterion. The plan's selected0.90 and report's asserted prespecified0.80 are different rules. With two-decimal half-unit intervals[0.895,0.905] and[0.795,0.805], gap0.09/0.90=0.10; rule identity also differs categorically.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The prespecified threshold used to interpret posterior probabilities as confirming the primary hypotheses and sufficient for future evaluation.

**Why context does not resolve it:** Category5 applies to a reported prespecified analysis criterion not contained in the supplied plan. The report's explicit reference to future trials overlaps the protocol's advancement purpose.

**Supported alternatives:**0.80 may be a separate clinical-information criterion and0.90 an advancement criterion, or a later amendment may have selected0.80. No separate supplied rule/amendment establishes that distinction.

**Exact human question:** Which prospectively specified criterion governed hypothesis confirmation and advancement, and where is the0.80 rule documented if it differed from the supplied0.90 protocol rule?

### F-XS-006

**Issue:** Planned missing-data and prior-sensitivity analyses for the primary/key-secondary analyses are not reported.

**Exact locations and roles:** PLAN [protocol p.28, General Data Analytic Strategy](../../../joi240036supp1_prod_1716416466.00349.pdf#page=28); REPORT [main p.4 statistical analysis and missing=nonabstinent](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4); REPORT [main p.7–8 secondary/post hoc analyses](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7) and [p.8](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8); REPORT [supplement p.5–13 analysis appendices](../../../joi240036supp2_prod_1716416466.01349.pdf#page=5), [p.8](../../../joi240036supp2_prod_1716416466.01349.pdf#page=8), [p.9](../../../joi240036supp2_prod_1716416466.01349.pdf#page=9), [p.12](../../../joi240036supp2_prod_1716416466.01349.pdf#page=12), [p.13](../../../joi240036supp2_prod_1716416466.01349.pdf#page=13).

**Printed statements:** Protocol specifies primary ITT/missing=smoking, secondary joint modeling of observed outcomes and missing data, sensitivity analyses of robustness to missing data, pattern-mixture handling of nonignorable patterns, and sensitivity analyses using optimistic and pessimistic/skeptical priors. Report describes missing=nonabstinent and logistic/IPW analyses; supplement describes a convergence-driven intercept-prior revision and posterior predictive fit, but supplies no joint/pattern-mixture missingness results or optimistic/pessimistic prior-sensitivity results in either complete REPORT document.

**Comparison logic:** Each planned analysis family was checked individually across all main and supplementary methods, result paragraphs and tables. The unconditional sensitivity promises apply to the primary analysis and the reported key six-month abstinence endpoint. A convergence-driven replacement prior is not the planned paired optimistic/pessimistic sensitivity assessment. No claim is made that a particular sensitivity would change a result.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The primary week-12 and key six-month treatment comparisons and the availability of their prospectively planned robustness analyses.

**Why context does not resolve it:** These are named planned analyses for the relevant outcomes, rather than an invented desirable method or an isolated unreported parameter; category5 applies to planned primary/key-secondary analyses not reported.

**Supported alternatives:** Analyses may have been performed but omitted, removed by an amendment, or reported elsewhere outside the supplied package. The covariate rule was conditional on detected confounding and is excluded separately.

**Exact human question:** Were the planned joint/pattern-mixture missing-data and optimistic/pessimistic prior-sensitivity analyses performed for the primary and key-secondary outcomes, and where are their results or documented changes?

### F-XS-007

**Issue:** Two eligibility criteria describe a different potential analysis population in the report and protocol.

**Exact locations and roles:** PLAN [protocol p.8 inclusion and MINI exclusions](../../../joi240036supp1_prod_1716416466.00349.pdf#page=8), with [p.9 tobacco/psychiatric definitions](../../../joi240036supp1_prod_1716416466.00349.pdf#page=9); REPORT [main p.2 Participants](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=2); REPORT [main p.5 Table footnote d](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5); REPORT [supplement p.20 eTable3 footnote b](../../../joi240036supp2_prod_1716416466.01349.pdf#page=20).

**Printed criteria:** Plan includes CO≥6ppm with a positive-cotinine exception when CO≤5ppm; the directly viewed plan-page transcription resolves the native-text comparator glyph. Main says participants were included with CO≥6ppm, and both report-table footnotes say CO6ppm or higher was required. Plan excludes MINI current manic or hypomanic episode only; main excludes current or lifetime mania. These are two criteria in the population-description pattern; all other criteria were compared individually as recorded above.

**Comparison logic:** A positive-cotinine smoker with CO≤5 is permitted by the printed plan exception but excluded by the report's categorical “required” threshold. A participant with past mania without a current episode is not excluded by the plan's current-only MINI criterion but is excluded by the report's current/lifetime criterion, unless a separate safety-discretion condition applies. This compares criterion membership, not rounding or synonymous disease names.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** Eligibility definition of the490-person population underlying the primary and key-secondary treatment effects.

**Why context does not resolve it:** The categorical report rules and explicit plan exceptions cannot both define the same eligible set for the examples above. The package provides no count of affected participants or amendment resolving which criteria were applied.

**Supported alternatives:** The report may summarize criteria more restrictively than implemented, or actual recruitment criteria may have changed. Investigator discretion can exclude particular participants, but does not itself establish a universal lifetime-mania rule or remove the biochemical exception.

**Exact human question:** Were low-CO/positive-cotinine smokers and participants with past but no current mania eligible, and which criterion list describes the population actually analyzed?

### F-XS-008

**Issue:** The anticipated primary-outcome figure labels augmented CNRT with a different lozenge dose.

**Exact locations and roles:** REPORT [supplement p.14 eFigure1 caption](../../../joi240036supp2_prod_1716416466.01349.pdf#page=14); REPORT [supplement p.17 eTable1 dose definitions](../../../joi240036supp2_prod_1716416466.01349.pdf#page=17), [p.15 eFigure2](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15), and [p.16 eFigure3](../../../joi240036supp2_prod_1716416466.01349.pdf#page=16); REPORT [main p.4 medication and p.7 Figure3 caption](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4) and [p.7](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7). PLAN [p.25 regimen](../../../joi240036supp1_prod_1716416466.00349.pdf#page=25) corroborates2mg and does not independently create a plan/report relationship.

**Printed values:** eFigure1 says two21-mg patches plus4-mg lozenge for augmented CNRT. All listed reported intervention definitions and eTable1 simulation definitions retain2-mg lozenges, with patch increase only. The figure attaches the anticipated augmented-CNRT outcome0.20 (0.10–0.34), Beta(8.90,34.6), to its4-mg regimen.

**Comparison logic:** The simulation figure and matching simulation table describe the same primary-design cell but different doses. Allowing integer half-unit intervals gives[3.5,4.5] versus[1.5,2.5]mg, gap1/4=0.25. This is a value in the regimen definition, not a unit/glyph difference.

**Focus area:** C. **Proposed review domain:** report_internal_inconsistency. **Proposed relationship:** S_C; **All relationships:** S_C, S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The randomized regimen attached to the anticipated0.20 augmented-CNRT primary outcome and the corresponding sample-size/power assumption.

**Why context does not resolve it:** It is unclear whether4mg describes the regimen assumed when planning that cell or whether the figure intends the same2-mg regimen as the trial and simulation table. Dose distinctions also matter to extraction of the randomized intervention.

**Supported alternatives:** A historical anticipated regimen may have included4-mg lozenges, or the figure may intend2mg. The source provides no dose-change explanation at the figure.

**Exact human question:** Were augmented-CNRT simulations based on2-mg or4-mg lozenges, and which dose should be attached to the anticipated figure cell?

### F-XS-009

**Issue:** The reported primary continuation analysis includes nonresponders who did not undergo the planned second randomization.

**Exact locations and roles:** PLAN [protocol p.7 trial allocation](../../../joi240036supp1_prod_1716416466.00349.pdf#page=7), [p.24–25 phaseII](../../../joi240036supp1_prod_1716416466.00349.pdf#page=24) and [p.25](../../../joi240036supp1_prod_1716416466.00349.pdf#page=25), [p.28–30 primary models/contrasts](../../../joi240036supp1_prod_1716416466.00349.pdf#page=28), [p.29](../../../joi240036supp1_prod_1716416466.00349.pdf#page=29), [p.30](../../../joi240036supp1_prod_1716416466.00349.pdf#page=30); REPORT [main p.1 abstract](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1), [p.4 Results](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4), [p.6 Figure2 footnote c](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6), and [p.8 limitation](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8); REPORT [supplement p.6 weighting definition](../../../joi240036supp2_prod_1716416466.01349.pdf#page=6).

**Printed statements and values:** Plan says six-week nonresponders will undergo randomization among continuation, augmentation and switch; planned primary contrasts/IPW use those rescue cells, with missing observations imputed smoking. Report assigns40 CNRT and35 varenicline participants who did not return for rerandomization to continuation for phase2 analyses. Thus primary continuation denominators are90=50+40 and77=42+35, while switch/increase remain actual rerandomized cells. Supplement defines the nonresponder phaseII weight1/(0.5×0.33)=6.06 for rerandomized participants; it does not separately describe the75 deterministic assignments.

**Comparison logic:** Imputing an absent smoking outcome and imputing a treatment-strategy assignment are distinct operations. The supplied plan specifies the former but not the latter. The primary continuation-versus-rescue comparison population changes from second-stage randomized continuation to randomized plus deterministically assigned continuation. No assumed weight for the75 is asserted here.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The primary week-12 continuation reference groups and resulting rescue-versus-continuation RDs.

**Why context does not resolve it:** The report discloses the assignment and discusses it as a limitation, but the supplied plan does not contain this replacement of the planned randomized continuation analysis set. Category5 requires registration of a planned primary analysis changed in the report.

**Supported alternatives:** A prospective amendment may have established deterministic treatment assignment for nonreturners; the primary contrasts may have been supplemented by analyses restricted to the50/42 actually rerandomized continuation participants. Neither is supplied as an analysis result or plan rule.

**Exact human question:** Was assignment of the40/35 nonreturners to continuation specified prospectively, and which primary analysis set and weights were used for them relative to the planned rerandomized rescue contrasts?

### F-XS-010

**Issue:** The reported EOT+30 varenicline-continuation denominator differs between narrative and figure.

**Exact locations and roles:** REPORT [main p.7 Secondary Outcomes](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7); REPORT [supplement p.10 summarized analysis](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10); REPORT [supplement p.15 eFigure2 varenicline-nonabstainer continuation row](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15); REPORT [main p.6 Figure2](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6).

**Printed values:** Both narrative copies describe EOT+30 varenicline nonabstainers n157 and continuation0%, n42. eFigure2 supplies the same labeled continuation cell0/77,0%(0%–0%). Figure2 identifies42 rerandomized continuation plus35 assigned continuation. Both result occurrences point to the same outcome figure.

**Comparison logic:** Denominators are exact integer counts;77−42=35. Even permitting half-unit intervals[41.5,42.5] and[76.5,77.5], gap34/42=0.810. This is an analysis-set-size discrepancy, which is an explicit exception to the peripheral per-time-point-count exclusion.

**Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship:** S_C; **All relationships:** S_C, S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The denominator and analysis population for the EOT+30 continuous-abstinence0% continuation reference result.

**Why context does not resolve it:** The42-person and77-person sets are both plausible because one excludes nonreturners; the narratives do not say their secondary analysis changes population while pointing to a77-person figure.

**Supported alternatives:** The narratives may report only rerandomized participants while the figure reports all assigned participants, or the n42 label may be a copied randomization count. Equal printed0% rates do not identify which analysis population generated the result.

**Exact human question:** Does the EOT+30 varenicline-continuation result use42 rerandomized participants or77 including assigned nonreturners, and which denominator should be extracted?

### F-XS-011

**Issue:** Primary rescue-group percentages use different denominators within each abstract population description.

**Exact locations and roles:** REPORT [main p.1 abstract Results](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1); REPORT [main p.6 Figure2 allocations](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6).

**Printed values:** CNRT paragraph identifies191 nonabstainers,151 rerandomized and40 assigned continuation; then describes90(47%),50(33%) and51(34%) for the191. Varenicline paragraph identifies157 nonabstainers,122 rerandomized and35 assigned continuation; then describes39(32%),41(34%) and77(49%) for the157. Continuation percentages use all nonabstainers, whereas increase/switch percentages reproduce with151/122 rerandomized denominators.

**Comparison logic:** For the stated191 population, exact counts yield50/191=26.178% and51/191=26.702%; compared with integer displayed33% and34%, printed intervals[32.5,33.5] and[33.5,34.5] leave gaps6.322/33=0.192 and6.798/34=0.200. For157,39/157=24.841% and41/157=26.115%, compared with[31.5,32.5] and[33.5,34.5], gaps6.659/32=0.208 and7.385/34=0.217. Counts are exact, so no input rounding is needed. All relative discrepancies exceed0.05. The alternate denominators151/122 explain the displayed percentages but are not the stated population for the parallel result list.

**Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W; **All relationships:** S_W.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** Allocation percentages and denominators attached to the primary week-12 rescue results in the abstract.

**Why context does not resolve it:** Category3 applies to count/denominator/percentage inconsistencies within one display. The different denominators can be reconstructed, but the parallel percentage list mixes randomized-only and total analysis-set populations.

**Supported alternatives:** The percentages may intentionally describe continuation among all nonabstainers and rescue arms among rerandomized nonabstainers; an explicit denominator label for each would establish that interpretation.

**Exact human question:** Should each rescue-group percentage use the191/157 analysis populations or151/122 rerandomized populations, and how should the mixed continuation percentages be labeled?

## Excluded observations

Only apparent issues declined as findings are listed. Reconciled checks are in the coverage narrative, not this table.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.4 versus REPORT supplement p.6 | Software versions4.0.3 and4.3 differ, with no source-linked primary/key-secondary result attributed to distinct software calculations. | PERIPHERAL_COMPARISON |
| REPORT main p.5 versus REPORT supplement p.21 | Primary responder RD lower limit−5% versus−4%, and varenicline-increase RD upper limit24% versus23%; whole-percent half-unit intervals touch, gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement p.11 versus p.34 | Six-month CNRT increase-versus-switch posterior probability88% versus89%; integer-percent rounding intervals touch, gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement p.12 versus p.35 | Six-month responder probability55% versus56%; integer-percent rounding intervals touch, gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN p.28 versus REPORT supplement p.8 | The revised intercept prior Normal(0,variance10) differs from the planned variance1,000,000; the appendix expressly discloses the original specification, convergence difficulty and fitted revision, so the planned-versus-used distinction is identifiable. | CONTEXT_RESOLVES |
| PLAN p.7 versus REPORT main p.4 | Plan minimization lists motivation, gender and race; report lists gender and race without stating motivation was excluded. Omission alone does not establish a different implemented minimization rule. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.28 versus complete REPORT materials | Conditional covariate-adjusted/unadjusted analyses are not shown; their stated trigger requires both baseline differences and outcome association, and the package does not establish that trigger. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp.7,19–20,30 versus complete REPORT materials | Planned prolonged/three-month abstinence and exploratory motivation/dependence/NMR/symptom analyses are not shown; these are not identified as primary or key secondary analyses replaced in the report. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.34 Table3 versus p.29 Aim2 and REPORT supplement p.18 eTable2 | The third Aim2 row repeats “VAR vs.NPL,” while its0.195 contrast is distinguished in the report as switch versus increase. The missing plus in the plan label is identifiable from the adjacent three-contrast Aim2 list and0.399−0.204 inputs. | NOTATION_OR_TYPOGRAPHY |
| PLAN pp.28–30 and REPORT supplement pp.6–7 | Cell-equation coefficient subscripts/signs for the varenicline-to-CNRT switch differ from literal substitution into the master equation. This symbol-level observation does not identify a different fitted numerical output, and the coding/master equation makes intended cell substitution immediate. | NOTATION_OR_TYPOGRAPHY |
| PLAN p.20 | Prolonged-abstinence examples include EOT although the stated grace period ends two weeks after EOT; the definition's explicit future post-grace relapse rule supplies the meaning, and no prolonged-abstinence result is reported here. | TERMINOLOGY_OR_WORDING |
| REPORT main abstract versus REPORT main p.4/REPORT supplement p.4 | “Weekly brief counseling” summarizes the detailed eight counseling contacts and brief medication/support calls across12weeks; this difference does not change the randomized dose, duration or a result. | TERMINOLOGY_OR_WORDING |

## Limitations and handoff

No source-unit or assigned comparison-coverage gap remains. The package supplies no participant-level data, amendment history, exact fitted coefficient table, sensitivity-analysis outputs, or separate SAP beyond the45-page protocol. The findings distinguish such source limitations from reproduced printed comparisons; no preferred analysis is proposed. Graphic density curves were not digitized because only their printed estimates, limits, counts and dose/time labels are relevant matched results. Independent inclusion screening and direct evidence recheck remain required.

## Subsequent independent audit clarification

For F-XS-008 / C014, direct visual audit confirms that supplement pp.15–16 captions specify the two-patch plus lozenge pathway without lozenge mg. Those figure captions provide pathway context only. Explicit 2-mg comparators are supplement pp.17–18 and main pp.4,7,8; the focal anticipated 4-mg caption is supplement p.14. Earlier observation prose is preserved as audit history; this source-specific clarification governs the final report and does not create another finding.
