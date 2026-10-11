# Cross-source consistency review — Workflow 1.6.2

Runtime ID: 01a12955-9d0e-7423-b6d8-0ca949eeff5c. Fresh cross_source_consistency_reviewer; gpt-6.1-sol/medium. Read complete QUALITY_CONTROL_SCOPE.md and review_contract.md. Scientific inputs are the fresh main/support evidence maps and supplied direct PDFs. No legacy conclusions or external evidence were used.

Scope: all five direct PDFs, 102 source pages, main N001–N071 and S001–S040, support N201–N220 and S201–S242. REPORT: main article, results supplement and data-sharing statement; PLAN: protocol version 7 and five-page SAP. All matched result relationships and supplied plan design elements were checked, with criterion lists compared item by item. This checker emits 9 findings and 10 excluded observations. All findings are proposals for independent inclusion screening; no candidate IDs or adjudications are assigned.

Direct-source locator derivatives: preprocessing/cross_source_review/main-layout.txt (11 pages), protocol-layout.txt (60 pages), sap-layout.txt (5 pages), support-layout.txt (25 pages), all created by direct pdftotext -layout, Poppler 26.01.0, CPU. Source pages, not these derivative files, are evidence authority. The existing main/support maps preserve all pages, table tuples and figure descriptions. All sources and reused assets were preserved.

## Findings

### F-XS-001

**Title:** Printed online-screening BMI threshold differs from the eligibility threshold.

**Compared locations and roles:** REPORT [main Figure 1, PDF p. 3](../../../jama_bot_2019_oi_190007.pdf#page=3), REPORT [abstract, PDF p. 1](../../../jama_bot_2019_oi_190007.pdf#page=1), REPORT [Methods, PDF p. 2](../../../jama_bot_2019_oi_190007.pdf#page=2), REPORT [eligibility appendix, PDF p. 3](../../../joi190007supp3_prod.pdf#page=3). PLAN [protocol eligibility, PDF p. 16](../../../joi190007supp1_prod.pdf#page=16) corroborates the 25–40 eligibility range and is not a conflicting side.

**Printed values:** Figure 1 assigns 1451 online exclusions to “BMI <15 or >40”; the abstract, Methods and eligibility appendix specify BMI 25–40. Figure 1 separately lists 18 telephone exclusions for BMI <25.

**Comparison logic:** The initial exclusion label prints a lower cutoff 15, whereas the source-defined eligible population has lower cutoff 25. At integer display precision, the copies have intervals [14.5,15.5] and [24.5,25.5]; gap 9/reference 25 = 0.36. The 1451 exclusions therefore appear to describe a different BMI range. The subsequent telephone exclusions permit an actual staged screening rule as an alternative; they do not determine whether 15 was intended.

**Focus area:** A/C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W; all relationships S_C, S_W.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** The BMI criterion represented by 1451 online-screening exclusions and the reported population-selection flow.

**Why context does not resolve it:** This is a printed numeric cutoff changing the reading of a participant-flow category, rather than only a different name for the same criterion. Route A category 2 applies even if 25 is inferred as the likely intended value.

**Supported alternatives:** The initial online screen may intentionally have used 15, with the final eligibility cutoff enforced later; alternatively, Figure 1 may intend 25. No individual screening data are supplied.

**Human question:** Did the 1451 online exclusions use BMI <15 or BMI <25, and what range does that count represent?

### F-XS-002

**Title:** Reported omega-3 dose differs from the protocol dose.

**Compared locations and roles:** PLAN [protocol summary, PDF p. 8](../../../joi190007supp1_prod.pdf#page=8), PLAN [intervention specification, PDF p. 18](../../../joi190007supp1_prod.pdf#page=18), PLAN [explicit EPA+DHA dose, PDF p. 23](../../../joi190007supp1_prod.pdf#page=23), PLAN [manufacturing tolerance, PDF p. 20](../../../joi190007supp1_prod.pdf#page=20), REPORT [abstract, PDF p. 1](../../../jama_bot_2019_oi_190007.pdf#page=1), REPORT [interventions, PDF p. 2](../../../jama_bot_2019_oi_190007.pdf#page=2), REPORT [supplement intervention, PDF p. 4](../../../joi190007supp3_prod.pdf#page=4).

**Printed values:** Protocol 1000 mg omega-3 per capsule, one capsule plus one multivitamin pill daily; explicit “EPA+DHA =1.0g per day.” Report 1412 mg EPA+DHA daily, ratio 3:1, two pills daily for one year. Protocol acceptable manufacturing deviation 90%–125%.

**Comparison logic:** Match daily combined EPA+DHA, rather than capsule mass or fish-oil concentration. Using the coarser printed 1.0 g input gives [950,1050] mg, compared with [1411.5,1412.5] mg; gap 361.5/1000 = 0.3615. Even extending the upper rounded planned dose by the maximum printed manufacturing factor gives 1050×1.25 = 1312.5 mg, below 1411.5 mg. Other reported nutrient doses lie within protocol ranges; one-year exposure and pill/capsule count reconcile.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The randomized omega-3 exposure associated with the MDD prevention estimate, and intervention dose extracted for evidence synthesis.

**Why context does not resolve it:** Both documents explicitly describe combined daily EPA+DHA, so fish-oil versus fatty-acid terminology does not resolve the discrepancy; the printed tolerance does not cover it.

**Supported alternatives:** A product/dose amendment or revised delivered composition may explain the report; the results supplement provides composition testing but no reconciliation with the stated planned daily dose. The supplied protocol is version 7, not a full amendment history.

**Human question:** What amendment or dose definition reconciles planned 1.0 g/day EPA+DHA with reported 1412 mg/day?

### F-XS-003

**Title:** Sample-size assumptions differ between the protocol and report.

**Compared locations and roles:** PLAN [protocol calculation, PDF p. 16](../../../joi190007supp1_prod.pdf#page=16), PLAN [power continuation, PDF p. 17](../../../joi190007supp1_prod.pdf#page=17), REPORT [sample-size calculation, PDF p. 4](../../../jama_bot_2019_oi_190007.pdf#page=4).

**Printed values:** Protocol: difference 25% in cumulative incidence; expected control 30%, intervention 15%; 180 participants per group; 90% power, two-sided .05; dropout 20%; 250 per intervention arm; pure-treatment synergistic comparison 80% power. Report: 33% reduction, control 30%, active 20%; 392 participants, parenthetically 196 in each of four combinations; 90% power, two-sided .05; attrition 22%; 250 per combination; absolute difference 10%.

**Comparison logic:** The same one-year MDD factorial-design calculation is described, but the alternative active incidence is 15% versus 20%, and dropout 20% versus 22%; the final target of 250 per combination does not show which assumptions support it. At percentage-point integer precision the active-rate gap is 4/reference 15 = 0.2667 and the dropout gap 1/reference 20 = 0.05 (the latter individually within the display rule). For 180 versus 196 participants, integer half-unit intervals give gap 15/reference 180 = 0.0833. The report's own 392 versus 4×196 relationship is also preserved for numeric/statistical review; it is not used here to choose a corrected total.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** Planned detectable difference and power underlying interpretation of the reported null primary MDD effects.

**Why context does not resolve it:** The intervention incidence and planned per-group sample do not agree beyond display precision. The supplied SAP contains no replacement power calculation or explanation of these input changes.

**Supported alternatives:** A revised calculation may explain the report, or the documents may use different factor-level versus combination-group sample counts. Those alternatives require the actual calculation and amendment timing; the unchanged target does not establish them.

**Human question:** Which one-year MDD risk assumptions and participant counts generated the operative power calculation, and when were they revised?

### F-XS-004

**Title:** Endpoint hierarchy differs among protocol, SAP and report.

**Compared locations and roles:** PLAN [protocol main endpoints, PDF pp. 8–9](../../../joi190007supp1_prod.pdf#page=9), PLAN [protocol hierarchy, PDF p. 28](../../../joi190007supp1_prod.pdf#page=28), PLAN [primary-parameter analyses, PDF p. 43](../../../joi190007supp1_prod.pdf#page=43), PLAN [SAP outcomes, PDF p. 2](../../../joi190007supp2_prod.pdf#page=2), REPORT [outcome hierarchy, PDF p. 4](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT [Table 3, PDF p. 8](../../../jama_bot_2019_oi_190007.pdf#page=8).

**Printed statements:** Protocol “Main study parameter/endpoint” lists both 12-month MDD incidence and IDS depressive symptomatology; its “Primary study parameter(s)” analysis includes IDS. SAP has primary binary MDD, secondary PHQ-9 and IDS, and “Other” GAD-7 and health utility. Report labels MDD as primary and PHQ-9, IDS, anxiety and health utility as secondary outcomes.

**Comparison logic:** Match the same instruments and 3/6/12-month assessments. IDS moves from the protocol main/primary parameter set to SAP/report secondary. GAD and utility are protocol secondary, SAP “Other,” and report secondary. These are endpoint-status changes, not interchangeable instrument names. The shared pattern is consolidated. Display precision is not applicable to categorical hierarchy.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R, P_P.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified status of the IDS depression-severity effects and anxiety/utility effects, including their interpretation as primary versus secondary versus other endpoints.

**Why context does not resolve it:** Route A category 5 registers changed outcome status. The report's general advice to interpret secondary results as exploratory because of multiple comparisons is not used as a separate status change.

**Supported alternatives:** The SAP may intentionally revise the protocol hierarchy; “Other” may be intended as an organizational label rather than a formal lower tier. Either requires clarification and timing, while the IDS main/primary versus secondary transition remains explicit.

**Human question:** What was the operative prespecified hierarchy for IDS, GAD-7 and health utility, and which amendments explain the supplied differences?

### F-XS-005

**Title:** Protocol primary MDD analysis suite is replaced or absent in the supplied report.

**Compared locations and roles:** PLAN [protocol primary analyses, PDF p. 43](../../../joi190007supp1_prod.pdf#page=43), PLAN [SAP primary endpoint, PDF p. 2](../../../joi190007supp2_prod.pdf#page=2), PLAN [SAP analyses, PDF p. 3](../../../joi190007supp2_prod.pdf#page=3), PLAN [SAP secondary Cox analysis, PDF p. 4](../../../joi190007supp2_prod.pdf#page=4), REPORT [abstract model, PDF p. 1](../../../jama_bot_2019_oi_190007.pdf#page=1), REPORT [methods, PDF p. 4](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT [Table 2, PDF p. 6](../../../jama_bot_2019_oi_190007.pdf#page=6).

**Printed statements:** Protocol primary-parameter section specifies Kaplan–Meier, log-rank, Cox time-to-event analyses and additional repeated mixed-model analyses of MDD and IDS at baseline/3/6/12, accounting for participant repeated measurements and country clustering. SAP primary analysis is effect-coded logistic regression of binary cumulative MDD, with Cox secondary. Report primary analysis is logistic; time-to-onset Cox is post hoc; symptom follow-ups use GEE and separate 12-month robust linear regression.

**Comparison logic:** Match the one-year primary MDD endpoint and all planned primary-analysis components individually: logistic cumulative outcome is reported; Cox is reported under a different status (F-XS-006); Kaplan–Meier/log-rank results and repeated mixed-model MDD results are absent from all REPORT sources. The repeated symptom analysis uses a SAP-permitted alternative, GEE; its mere method choice is not a separate finding. Stratification covariates and ITT reconcile. The primary suite/status changes remain even though SAP supports the reported logistic model. No numerical approximation substitutes for the actual models.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R, P_P.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Which analysis constituted the prespecified primary MDD inference and whether the protocol's planned primary survival/repeated-MDD analyses are available.

**Why context does not resolve it:** Planned primary analyses are replaced or not reported, an always-register category. A later SAP can explain a change but does not establish its date or authorization from its undated contents.

**Supported alternatives:** An operative SAP may have prospectively superseded protocol analyses; the protocol may use “primary study parameters” to describe the endpoint rather than an inferential hierarchy. The missing planned model results cannot be reconstructed from the supplied logistic ORs.

**Human question:** Which plan version governed the primary MDD analysis, and were the planned Kaplan–Meier/log-rank and repeated-MDD analyses superseded or performed but not supplied?

### F-XS-006

**Title:** Planned Cox time-to-MDD analysis is reported as post hoc.

**Compared locations and roles:** PLAN [protocol primary survival specification, PDF p. 43](../../../joi190007supp1_prod.pdf#page=43), PLAN [SAP secondary Cox specification, PDF p. 4](../../../joi190007supp2_prod.pdf#page=4), REPORT [outcomes and methods, PDF p. 4](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT [Table 2 “Post Hoc Outcome”, PDF p. 6](../../../jama_bot_2019_oi_190007.pdf#page=6), REPORT [Cox narrative, PDF p. 7](../../../jama_bot_2019_oi_190007.pdf#page=7).

**Printed statements and values:** SAP “As a secondary analysis” specifies time to onset of MDD, Cox regression, HR/95% CI/P. Report calls time-to-first-MDD analysis “post hoc” and Table 2 labels it “Post Hoc Outcome.” HRs are supplements 1.05 (0.86–1.27), therapy 0.91 (0.75–1.10), interaction 0.91 (0.75–1.11); matched narrative values reconcile.

**Comparison logic:** The same endpoint, model, contrasts and one-year observation window are present in the supplied plan, so this concerns analysis status, not absence of the analysis. It is separate from unreported protocol analysis components in F-XS-005. Precision is not applicable to status.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Whether the reported time-to-MDD HRs are prespecified secondary or post hoc results.

**Why context does not resolve it:** Changed status of a planned outcome/analysis belongs to route A category 5.

**Supported alternatives:** The supplied SAP could have been written after the analysis decision or the report could use post hoc to mean supplementary to the cumulative endpoint. The SAP is undated and does not establish chronology.

**Human question:** Was Cox time-to-MDD analysis prospectively specified, and why does the report label it post hoc?

### F-XS-007

**Title:** Planned site/history effect modification is collectively described as post hoc.

**Compared locations and roles:** PLAN [SAP modification specification, PDF p. 4](../../../joi190007supp2_prod.pdf#page=4), PLAN [SAP interaction testing/reporting, PDF p. 5](../../../joi190007supp2_prod.pdf#page=5), PLAN [protocol country moderators, PDF p. 44](../../../joi190007supp1_prod.pdf#page=44), REPORT [methods, PDF p. 4](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT [results, PDF p. 8](../../../jama_bot_2019_oi_190007.pdf#page=8), REPORT [moderation appendix, PDF pp. 18–20](../../../joi190007supp3_prod.pdf#page=18).

**Printed statements:** SAP secondary effect modification is by history of depression and center; other modifiers are reserved for a separate paper. Report Methods distinguishes site/history interactions from baseline symptom severity “post hoc analyses.” Report Results describes “post hoc effect modification analyses by study site, history of depression, and baseline symptoms scores.” Supplement reports no history moderation of primary/secondary outcomes and significant symptom-severity/site moderation findings.

**Comparison logic:** Compare modifiers item by item: center/site and history are explicitly planned; baseline symptom severity is explicitly post hoc in the report and is not alleged to be prespecified. The collective Results label changes the status of the first two planned modifiers. This pattern is consolidated across site/history, and is not inferred from an absence of numerical interaction P values.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R, S_W.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecification status of site/history moderation of the primary and reported secondary outcomes.

**Why context does not resolve it:** Route A category 5 concerns the prespecified versus post hoc analysis designation. The Methods distinction supports an alternative but does not remove the collective printed Results claim.

**Supported alternatives:** “Post hoc” in Results may have been intended only for baseline severity; or a later plan may have prospectively included site/history after earlier decisions. No supplied dating settles the latter.

**Human question:** Which site/history moderation analyses were prespecified, and does the Results post hoc label apply only to baseline severity?

### F-XS-008

**Title:** Planned additive interaction of the primary MDD outcome is not reported.

**Compared locations and roles:** PLAN [SAP primary-outcome interaction, PDF p. 4](../../../joi190007supp2_prod.pdf#page=4), REPORT [primary analysis description, PDF p. 4](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT [primary interaction results, PDF p. 6](../../../jama_bot_2019_oi_190007.pdf#page=6), REPORT [primary narrative, PDF p. 7](../../../jama_bot_2019_oi_190007.pdf#page=7). Absence check covers the complete main article, 25-page results supplement and one-page data-sharing statement.

**Printed statements:** SAP says “as a sensitivity analysis we will also study” departure from additivity via RERI, with a linear odds-ratio model, likelihood-based 95% CI and preventive-condition recoding. Report gives multiplicative logistic interaction OR 0.93 (0.76–1.14), P .48, and Cox interaction HR 0.91 (0.75–1.11), P .36. No RERI or additive-interaction interval/result is present in the supplied REPORT documents.

**Comparison logic:** Multiplicative A×B, additive RERI, linear OR model, likelihood CI and preventive-reference recoding were matched separately. The reported multiplicative interaction is not the planned additive estimand. This is an explicitly planned sensitivity analysis of the primary MDD outcome, rather than an unreported optional model detail. Numerical display precision is not applicable to absence of an entire planned analysis.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Planned primary-outcome additive interaction of the two randomized strategies, relevant to interpretation of their joint preventive effect.

**Why context does not resolve it:** A planned primary-outcome analysis is not supplied; multiplicative OR/HR interaction results cannot substitute for RERI without changing the quantity.

**Supported alternatives:** The analysis may have been performed elsewhere, superseded, or omitted from this publication. The provided data-sharing statement is administrative and supplies no additive result or amendment.

**Human question:** Was the prespecified RERI analysis performed, and where is its estimate/interval or the amendment superseding it?

### F-XS-009

**Title:** Detailed eligibility exclusion lists differ in temporal and population criteria.

**Compared locations and roles:** PLAN [protocol full criteria, PDF p. 16](../../../joi190007supp1_prod.pdf#page=16), REPORT [full eligibility appendix, PDF p. 3](../../../joi190007supp3_prod.pdf#page=3), REPORT [flow psychiatric exclusion footnote, PDF p. 3](../../../jama_bot_2019_oi_190007.pdf#page=3).

**Printed statements:** Protocol excludes history of eating disorders; anxiety or alcohol/substance/drug addiction in the preceding 6 months; history of bariatric surgery; and current supervised behavioral interventions interfering with the trial. Results appendix excludes current eating disorder; history of substance dependence or other severe psychiatric disorder requiring specialized attention; history of or planned bariatric surgery. It does not separately repeat the protocol's recent anxiety or interfering-supervised-intervention criterion. Figure 1 groups anxiety and addiction among psychiatric exclusions without specifying the temporal window.

**Comparison logic:** The complete itemwise comparison below shows which criteria reconcile and which change the eligible population. The narrow affirmative differences are history versus current eating disorder, recent versus history substance dependence, and addition of planned bariatric surgery. An omitted criterion could be contained within the broad severe-disorder or psychological-intervention language, so those omissions are supporting ambiguities rather than separate claims of nonimplementation. Categorical temporal/population criteria have no rounding interval.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The eligible psychiatric/surgical population represented by the primary MDD prevention estimates.

**Why context does not resolve it:** A history of eating disorder includes resolved episodes, while a current disorder does not; history of substance dependence is not confined to the preceding 6 months. The detailed lists alone do not determine which people were eligible. These temporal contrasts change a population definition rather than merely its name.

**Supported alternatives:** Local screening rules or a prospective eligibility amendment may explain the differences; broad severe-psychiatric-disorder language could have included some resolved disorders. Aggregate exclusion counts do not establish the operative criteria.

**Human question:** Which temporal criteria for eating disorder/substance dependence and which bariatric-surgery exclusions governed enrollment, and what amendment reconciles the supplied lists?

## Completed comparison record

All numeric/statistical relationships in the assigned maps were considered; the grouping below is a complete scope index, not a sample of checks. Reconciled checks are recorded here rather than in the Excluded observations table.

| Relationship scope | Completed cross-location/design comparison |
|---|---|
| N001–N009, N012–N020, N056–N059, N064–N065, N069; S001–S004, S006–S008, S011–S019, S040 | Abstract/body/Key Points/flow primary population, four-arm and marginal events, logistic estimates, follow-up and safety match after factor/combination distinctions. 105 events and n1025 reconcile. 779 completing follow-up is the flow total; 246 missing at month12 and 239 with no prior MDD differ by their explicitly printed definitions. Cox and logistic are distinct estimands. |
| N010–N011, N008, N201, N207 | Eligibility, all online/telephone exclusion categories, and all inclusion/exclusion criteria matched itemwise; F-XS-001/F-XS-009 and criterion table below. |
| N006, N021, N023, N060, N070, N203–N204, N208–N210, N212–N218; S211, S215–S216, S234–S241, S037 | One-year intervention duration, 21 sessions =15 individual+6 group, doses/ranges, adherence thresholds, measurement source, CACE population/model, safety and adherence narrative/table copies checked. F-XS-002 concerns omega dose. CACE therapy MDD OR .78(.64,.95) matches main/supplement. Capsule omega adherence versus generic supplement adherence is expressly reported; multivitamin adherence is separately measured. No raw-data reconstruction of latent compliers was attempted. |
| N024, N202, S005, S202 | Planned/report sample size, rates, power, factor-group terminology and attrition checked; F-XS-003. Protocol own 25% difference alongside 30%/15% is passed to the statistical checker as a plan-internal power-input ambiguity, not resolved through literature. |
| N022, N055, N205, N211; S007, S009–S010, S020–S036, S203–S210, S214, S222–S233 | Outcome definitions/windows/status, instruments/units, adjusted GEE overall versus robust-linear month12, baseline adjustment, effect coding, MI versus available-data and secondary exploratory interpretation checked. Hierarchy F-XS-004; primary analysis suite F-XS-005. Table3 coefficient×2 and narrative mean differences reconcile under displayed precision. Nonimputed appendix is explicitly a different sensitivity analysis. SAP permits mixed or GEE, so no unqualified claim that the reported GEE contradicts that plan. |
| N061–N063, N219 | Main figure factor-marginal distributions versus supplemental four-arm distributions use matching instruments/time points but different grouping; available observations rather than MI-adjusted inference. Graphical directions reconcile with narrative. No exact unlabeled coordinates were invented. |
| S008, S011–S013, S204, S213 | Cox planned/report status checked: F-XS-006; primary-analysis suite differences F-XS-005. |
| S038, S206, S213, S217–S221 | Country/site, history, sex, education, income, BMI, age and baseline-severity modifier lists matched separately. SAP explicitly reserves other potentially modifying variables for a separate paper; no absence finding is made for that reserved set. Site/history status F-XS-007. Reported moderation directions match the appendix tables. |
| S003, S212; protocol p16 | Multiplicative/additive primary-interaction analyses checked itemwise: F-XS-008. No RERI is present. Conditional pure-group synergistic comparison is not asserted to have been triggered. |
| N026–N054, N066–N068, N220, S039, S242 | Baseline summaries, unadjusted available-data secondary scores, concealment counts/percentages and their narrative copies checked. Main concealment percentages 8.2/10.4/25.5/43.7 and unknown-allocation 307/759 =40.448% reconcile. Baseline pooled age46.5 and BMI31.4 reconcile; pooled women772 matches. |
| N071, N206, S205; all no-applicable units in the complete maps; DOC-005 p1 | Administrative, background, reference and safety-plan pages accounted for. No supplied noninferiority/equivalence margin or composite primary outcome exists. Two-sided .05 and95% intervals agree; no separate multiplicity/interim/stopping rule is specified in the supplied plans; protocol says DSMB not applicable. No preferred method or broad clinical/design critique is introduced. Data-sharing statement contributes no result comparison. |

### Itemwise criterion-list comparison

| Criterion | Protocol p16 PLAN | Results appendix p3 REPORT | Check result |
|---|---|---|---|
| Age |18–75|18–75|Reconciles|
| BMI |25–40|25–40|Reconciles; printed flow cutoff handled separately|
| Screening PHQ-9 |≥5|≥5|Reconciles|
| MDD |Past 6 months, MINI/DSM-IV|Past 6 months, MINI 5.0/DSM-IV|Reconciles|
| Antidepressant/psychological treatment |Past 6 months|Past 6 months|Reconciles|
| Psychosis/schizophrenia/bipolar |History|History psychosis/bipolar/other severe psychiatric disorder|Broad grouping terminology alone excluded|
| Eating disorder |History|Current|F-XS-009 temporal population difference|
| Anxiety |Previous 6 months|Not separately stated; broad severe psychiatric disorder|F-XS-009 supporting ambiguity; flow includes anxiety|
| Alcohol/substance/drug dependence |Previous 6 months|History substance dependence|F-XS-009 temporal population difference|
| Bariatric surgery |History|History or planned|F-XS-009 affirmative added exclusion|
| Severe life-threatening physical disease |Current|Current|Reconciles|
| Severe cognitive impairment |Limits conduct, staff instrument feasibility|Limits conduct, staff ability to complete instruments|Reconciles|
| Interfering supervised behavioral intervention |Current|Not separate; past6month psychological intervention broader category|F-XS-009 supporting ambiguity only|
| Competing supplement |Stop, or exclude if GP prescribed|Unable/unwilling to stop relevant-nutrient supplement|Same cessation requirement; prescribed supplements occur in flow|
| Pregnancy/breastfeeding |Current|Current|Reconciles; flow additionally prints planning pregnancy, but no primary-analysis-population count discrepancy established|
| ITT inclusion |All randomized; follow-up encouraged after withdrawal|All randomized regardless receipt/withdrawal,MI|Reconciles|
| Supplement good adherence |SAP ≥70% over 12 months, weighed jars else averaged self-report|≥70% over 12 months, weighed jars/self-report; CACE omega ≥70%|Explicit omega operationalization recorded; no contradictory primary-population count supplied|
| Therapy good adherence |SAP ≥8 of 21 over 12 months|≥8 of 21 over 12 months|Reconciles|
| Primary MDD success classification |SAP positive any T3/T6/T12; negative all|12-month cumulative onset measured T3/T6/T12|Reconciles|
| Composite components |No composite primary endpoint|No composite primary endpoint|Not applicable|
| Hypothesis direction/margin |Prevention superiority;two-sided .05;no NI/equivalence margin|Two-sided.05;no NI/equivalence margin|Reconciles|
| Primary covariates |SAP site/history; protocol country/history|Site/history|Reconciles|
| Missing-data decision |SAP FIML or MI where appropriate; 100 MI, MAR, Rubin|100 MI, MAR, Rubin; non-MI symptom sensitivity|Reconciles with available plan option|
| Interim/stopping/multiplicity |No supplied formal statistical rule;DSMB not applicable|No reported interim/stopping claim;secondary interpretation exploratory|No conflicting printed rule|

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [Table 2 footnote d, p6](../../../jama_bot_2019_oi_190007.pdf#page=6) versus REPORT [abstract, p1](../../../jama_bot_2019_oi_190007.pdf#page=1) | The second group is described “without therapy” again for22/256(8.6%); footnote f and the abstract identify with therapy. No numeric value changes, and the two complementary supplement groups are obvious from immediate context. | TERMINOLOGY_OR_WORDING |
| PLAN [protocol p28](../../../joi190007supp1_prod.pdf#page=28) versus PLAN [summary p8](../../../joi190007supp1_prod.pdf#page=8)/[operational MINI schedule p33](../../../joi190007supp1_prod.pdf#page=33) and REPORT [primary outcome p4](../../../jama_bot_2019_oi_190007.pdf#page=4) | DSM-5 versus DSM-IV wording occurs with the same MINI version 5 instrument and operational schedule. No differing operational episode-component list or extracted event value is supplied; instrument context identifies what was used. | TERMINOLOGY_OR_WORDING |
| REPORT [main Table3/narrative p8](../../../jama_bot_2019_oi_190007.pdf#page=8) | PHQ overall coefficient .33 doubles to .66 versus narrative mean difference .65; respective printed intervals overlap after ×2; gap zero. Similar tiny endpoint differences occur forPHQ/IDS limits. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [main Table3 p8](../../../jama_bot_2019_oi_190007.pdf#page=8) versus REPORT [noMIappendix p21](../../../joi190007supp3_prod.pdf#page=21) | Coefficients differ, e.g.therapy PHQ month 12 −.17 versus−.22, because tables explicitly use MI versus no MI and secondary interactions differ in display. They are not printed copies of the same analysis. | CONTEXT_RESOLVES |
| REPORT [main narrative p8](../../../jama_bot_2019_oi_190007.pdf#page=8) and [Table3 p8](../../../jama_bot_2019_oi_190007.pdf#page=8) | Unadjusted GAD means 3.9/3.2 and PHQ means 4.1/4.9 differ from adjusted model contrasts; available-data versus adjusted MI estimates are identified. | MODEL_VERSUS_CRUDE |
| PLAN [protocol measurement table p35](../../../joi190007supp1_prod.pdf#page=35) versus REPORT [supplement dietary methods p12](../../../joi190007supp3_prod.pdf#page=12) | FFQ item count 264 versus250 and questionnaire table counts do not alter a primary/keysecondary mental-health endpoint or analysis-population size. | PERIPHERAL_COMPARISON |
| REPORT [Figure2 p7](../../../jama_bot_2019_oi_190007.pdf#page=7) | Nine-month axis ticks are present but outcomes and assessment counts are printed for0/3/6/12 months; ticks do not assert an additional measurement. | NOTATION_OR_TYPOGRAPHY |
| PLAN [SAPp3](../../../joi190007supp2_prod.pdf#page=3) versus REPORT [Table3p8](../../../jama_bot_2019_oi_190007.pdf#page=8) | SAP specifies standardized mean differences with 95% CI/P; report suppliesCohen D point values with separate unstandardized CI/P. Missing standardized CI/P alone does not establish an absent entire planned analysis or contradictory printed value. | CONDITIONAL_OR_UNREPORTED |
| REPORT [mainp6](../../../jama_bot_2019_oi_190007.pdf#page=6) versus REPORT [adherenceappendixp16](../../../joi190007supp3_prod.pdf#page=16) | Main says more than 70% for descriptive 77% adherence while definitions/tables consistently use≥70%; no boundary participant count or changed CACE result is supplied. | TERMINOLOGY_OR_WORDING |
| REPORT [moderationappendixp19](../../../joi190007supp3_prod.pdf#page=19) | Baseline GAD P displayed 0 is a display-zero value; no independent interval/null conflict follows from it. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations

All 102 source pages are covered by the complete maps and this assigned comparison scope; no scientific-coverage unit is omitted. No raw participant data, structured results workbook/CSV, or dated complete amendment history is supplied. Thus screening implementation and SAP chronology cannot be established beyond printed statements. Unlabeled figure coordinates were not converted into exact numeric estimates; visual descriptions and printed counts provide the comparison context. Direct text is usable; no OCR or fallback tooling was required. Source-grounded alternatives are retained for independent screening and human review.
