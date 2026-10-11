# Statistical pass 1

Runtime ID: 01a128e0-c784-7a33-87ba-81b76f900a82. Fresh gpt-6.1-sol agent, high effort. Scope: every relationship S001–S032 and S050–S094, 77 relationships, including all adjustment and interaction cells in S073–S077. This agent owns this checker artifact only; the coordinator merges the explicit completion records into the canonical statistical inventory. QUALITY_CONTROL_SCOPE.md and the 1.6.1 review contract were read completely. Fresh main and support maps and their source-linked relationship inventories were used; no legacy checker, candidate, screening, classification, or report was read.

All source-page numbers below are physical PDF pages. DOC-001 and DOC-004 are REPORT; DOC-002 and DOC-003 are PLAN, by content. Exact source text was checked using direct Poppler pdftotext layout output for DOC-001 pp.4,6–9, DOC-002 pp.8–9,16–17,28,43–44, DOC-003 pp.2–5, and DOC-004 pp.14–15,18–23. Reusable DOC-004 page_019.png was also visually inspected for the complete moderation table. These commands returned source text to the session and created no derivative. The tooling record states all direct PDF tools available. Commands followed `pdftotext -f N -l M -layout SOURCE.pdf -`; no fallback, OCR, Python scientific orchestration, external literature, or web was used.

## Rules, calculations, and bounded results

All displayed regression and ratio estimates in scope lie inside ordered printed confidence intervals. All confidence intervals exclude or include their appropriate null in agreement with the printed nominal decisions, allowing endpoint rounding. The primary ITT ratios include 1 and their P values exceed .05. The significant secondary coefficients and moderation terms have directions agreeing with the outcome scales and narratives. CACE therapy MDD OR .78 (.64–.95), supplement PHQ B .43 (.08–.77), and therapy GAD B −.31 (−.60–−.02) agree with their significance marks. The remaining CACE intervals include their respective nulls.

Interventions are explicitly effect coded −1/+1, jointly modeled; adjusted and multiply-imputed estimates are not crude ratios. Table 3 explicitly doubles coefficients and endpoints for the adjusted between-condition mean difference. Every narrative contrast matches at display precision: .33/.12/.53 versus .65/.25/1.06, .28/.05/.50 versus .56/.11/1.01, .60/.15/1.05 versus 1.20/.29/2.10, .25/.08/.42 versus .50/.16/.84, and −.24/−.42/−.06 versus −.48/−.84/−.12. For example, a hidden coefficient .326 and lower endpoint .124 can display as .33 and .12 while their doubled values display as .65 and .25. There is no discrepancy beyond the permitted rounding intervals.

Exact reconstruction of a pooled P value from a rounded interval is bounded by absent analysis-specific imputation degrees of freedom and variance components. Normal-Wald calculations were diagnostic only and were not treated as the reported tests. For the no-imputation T12 robust-linear table, printed B and SE allow compatible values after half-unit rounding. For example, PHQ supplement B .28 (SE .11), P .013 admits B .276 and SE .111, and IDS supplement B .28 (SE .28), P .30 admits B .285 and SE .275. No test statistic or finite-sample degrees of freedom is printed there; none was invented. All twelve T12 B/SE/P cells and corresponding overall interval/P cells were reviewed individually.

The report sample-size assumptions give a useful labeled diagnostic: the usual equal-allocation independent two-proportion normal approximation, using control .30, active .20, z(.975)=1.95996 and z(.90)=1.28155, yields approximately 391.95 per marginal comparison group, or 195.97 per factorial cell. This reproduces the report's 392/196 grouping under the factorial interpretation. Its phrase “392 participants (196 in each of the 4 possible intervention combinations)” does not state the marginal grouping clearly, but the same sentence's factorial main-effect context identifies it at once. With rounded 196 per cell, 196/.78≈251.28; 250 per cell is compatible with rounded input percentages and sample-size approximation. This diagnostic does not establish the protocol's additive-interaction power calculation: its contrast specification is not supplied. The protocol's 180/.80=225 is below its sufficient recruitment target 250, so it does not contradict that target. No preferred sample-size calculation is proposed.

The stated analyses are superiority analyses. No noninferiority/equivalence margin or numerical efficacy stopping/interim boundary is supplied. Secondary analyses are explicitly exploratory because of multiple comparisons; no multiplicity-adjusted claim or threshold was inferred. The primary absence of statistically significant reduction follows from the printed ITT intervals and P values. The report explicitly distinguishes CACE from ITT; their differing conclusions are not a contradiction.

## Findings

### F-ST1-001

**Title:** Primary-outcome power assumptions differ between the protocol and report.

**Relationships:** S001, S051. **Locations and roles:** [DOC-002 protocol p.16](../../../joi190007supp1_prod.pdf#page=16) and [p.17](../../../joi190007supp1_prod.pdf#page=17), PLAN, section 4.4; [DOC-001 article p.4](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT, Sample Size; [article p.9](../../../jama_bot_2019_oi_190007.pdf#page=9), REPORT, power discussion/limitations. **Proposed relationship:** P_R. **Focus area:** D. **Proposed review domain:** protocol_report.

**Printed statements:** Protocol control 30%, intervention 15%, two-sided α=.05, power .90, 180 per group, dropout 20%, recruitment 250 per intervention arm; interest in additive interaction and 80% power under a synergistic pure-treatment comparison. Report control 30%, active 20%, relative reduction 33%, absolute difference 10%, α=.05, power .90, 196 per factorial combination/392 marginal group, attrition 22%, recruitment 250 per combination. Both concern one-year MDD prevention.

**Rule and calculation:** Match the prospective and reported power inputs for the same primary one-year MDD outcome, retaining their distinct factorial contrasts. The intervention incidences are .15 versus .20, a 5 percentage-point difference; corresponding control-to-active differences are .15 versus .10. Protocol dropout .20 differs from report .22. Even allowing each integer percentage ±.5 percentage point, the intervention-rate ranges [14.5%,15.5%) and [19.5%,20.5%) do not overlap. Recruitment totals matching at 1000 do not make these assumptions identical. The labeled normal approximation above illustrates the report's grouping; it is not a reconstruction of protocol interaction power.

**Affected result or extracted value:** The design effect and power assumptions accompanying the primary null MDD result, especially downstream extraction of the assumed intervention incidence and absolute effect, and the report's interpretation that unexpectedly low incidence reduced power.

**Why context does not resolve it:** The supplied protocol and report give different numerical assumptions and different power contrasts without a reconciled revision statement identifying whether the report replaces the protocol calculation. The common final target does not identify which primary design assumptions governed it. This finding does not rely on the readily resolved report grouping wording or the protocol's introductory “25%” phrase.

**Alternatives and missing definitions:** The report may describe a later calculation for factorial main effects, whereas the protocol describes an interaction-oriented calculation, or the protocol input may have been revised. The supplied locations do not establish a dated amendment or a mapping between those calculations. No timing or adherence inference is made.

**Exact human question:** Which primary MDD power calculation and assumptions governed the trial's recruitment target, and how do the supplied protocol's 30%/15%, 20% dropout assumptions relate to the report's 30%/20%, 22% attrition assumptions?

### F-ST1-002

**Title:** Primary statistical analysis and time-to-onset priority differ across the protocol, SAP, and report.

**Relationships:** S005–S007, S054, S055, S064, S068. **Locations and roles:** [DOC-002 protocol p.43](../../../joi190007supp1_prod.pdf#page=43), PLAN, section 10.1; [DOC-003 SAP p.3](../../../joi190007supp2_prod.pdf#page=3), PLAN, fourth analysis; [SAP p.4](../../../joi190007supp2_prod.pdf#page=4), PLAN, Secondary analysis; [DOC-001 article p.4](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT, Statistical Methods; [article p.6](../../../jama_bot_2019_oi_190007.pdf#page=6), REPORT, Table 2; [article p.7](../../../jama_bot_2019_oi_190007.pdf#page=7), REPORT, onset narrative. **Proposed primary relationship:** P_R. **All relationships:** P_R, P_P. **Focus area:** D. **Proposed review domain:** protocol_report.

**Printed statements:** Protocol section 10.1 Primary study parameter(s) specifies Kaplan–Meier, log-rank, Cox analysis of MDD time-to-event and additionally mixed regression incorporating baseline,3,6,12 months for MDD onset and IDS. SAP specifies primary logistic regression for new MDD episode and Cox time-to-onset as a secondary analysis. Article specifies logistic regression for primary 12-month cumulative MDD and labels Cox time-to-first-MDD as post hoc; Table 2 repeats Primary Outcome versus Post Hoc Outcome. Article Table 2 prints supplement/therapy/interaction primary ORs 1.06/.93/.93 and Cox HRs 1.05/.91/.91.

**Rule and calculation:** Compare the explicitly assigned primary models and analysis priorities, rather than numeric OR versus HR values or a preference between methods. Logistic regression of a binary cumulative endpoint and Cox regression of time-to-onset are distinct analyses. The report's primary ORs match the SAP specification; this does not reconcile the protocol primary time-to-event specification or the report's post hoc designation for a Cox analysis explicitly planned in the SAP. Protocol-to-SAP is P_P; the protocol/report model and SAP/report priority comparisons are P_R. These linked changes of primary/time-to-onset analysis specification are consolidated into one finding.

**Affected result or extracted value:** Identification of the prespecified primary MDD effect measure and analysis, and whether the reported HR 1.05 (.86–1.27), HR .91 (.75–1.10), and HR .91 (.75–1.11) belong to a planned secondary analysis or an unplanned analysis.

**Why context does not resolve it:** The report clearly identifies which model produced each reported number, but the supplied documents assign different analysis priorities and the report calls the SAP-prespecified Cox analysis post hoc. A reader cannot identify the intended prospective analysis status merely from the differing labels. No located statement explains which protocol provisions were replaced or why the Cox analysis is described as post hoc.

**Alternatives and missing definitions:** The SAP may have superseded the protocol's primary models and the report may use “post hoc” to refer to a narrower implementation; alternatively, the analysis hierarchy may have changed. The supplied locations do not define such a narrower post hoc element or an explicit amendment mapping. The coherence of the reported logistic model is not questioned.

**Exact human question:** Which supplied specification defines the prespecified primary MDD model, and why is the Cox time-to-onset analysis labeled post hoc in the report when it appears prospectively as primary in the protocol and secondary in the SAP?

### F-ST1-003

**Title:** IDS changes from a main endpoint in the protocol to an exploratory secondary endpoint in the report.

**Relationships:** S013–S016, S050, S055, S062, S031. **Locations and roles:** [DOC-002 protocol p.9](../../../joi190007supp1_prod.pdf#page=9), PLAN, continuation of Main study parameters/endpoints; [protocol p.28](../../../joi190007supp1_prod.pdf#page=28), PLAN, section 8.1.1; [protocol p.43](../../../joi190007supp1_prod.pdf#page=43), PLAN, section 10.1; [DOC-003 SAP p.2](../../../joi190007supp2_prod.pdf#page=2), PLAN, outcomes; [DOC-001 article p.4](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT, Secondary Outcomes and exploratory interpretation; [article p.8](../../../jama_bot_2019_oi_190007.pdf#page=8), REPORT, Table 3 and narrative. **Proposed primary relationship:** P_R. **All relationships:** P_R, P_P. **Focus area:** D. **Proposed review domain:** protocol_report.

**Printed statements:** Protocol lists IDS depressive symptomatology at baseline,3,6,12 months as a main study endpoint and places its analysis under Primary study parameter(s). SAP lists IDS30-SR under Secondary continuous depressive symptoms. Article lists IDS under Secondary Outcomes and states secondary-endpoint findings should be interpreted as exploratory because of multiple comparisons. Article IDS supplement overall coefficient .60 (95% CI .15–1.05), P=.01; narrative adjusted difference 1.20 (.29–2.10), P=.01.

**Rule and calculation:** Compare the hierarchy for the same IDS scale and time points, while respecting that coefficient .60 and full contrast 1.20 reconcile by explicit effect coding. “Main study parameter/endpoint” and inclusion in Primary study parameter(s) are contrasted with the explicitly secondary/exploratory status; this is an endpoint-hierarchy comparison, not a calculation discrepancy or terminology-only comparison. Protocol/SAP gives P_P and protocol/report gives P_R, with P_R precedence.

**Affected result or extracted value:** Whether the reported IDS supplement overall effect .60 (.15–1.05), or full adjusted mean difference 1.20 (.29–2.10), P=.01 is extracted and interpreted as a prospectively main endpoint result or a secondary exploratory result.

**Why context does not resolve it:** The same IDS measure is consistently identified, but its planned hierarchy is explicitly different. The SAP and report corroborate the secondary status without identifying a revision of the protocol's two separate main-endpoint/primary-analysis statements. This is relevant to interpretation of the supplied IDS result even though no unprinted multiplicity procedure is assumed.

**Alternatives and missing definitions:** The protocol may use “main” more broadly than the SAP's primary/secondary hierarchy, or the hierarchy may have been revised. Its separate primary-analysis subsection includes IDS, so a reader cannot determine that broader usage at once. No explicit supplied amendment reconciles the hierarchy. The finding does not assert that a particular multiplicity adjustment was required.

**Exact human question:** Was IDS prospectively a main endpoint or a secondary endpoint for the reported analyses, and what reconciles its placement under the supplied protocol's main-endpoint and primary-analysis sections with the SAP/report's secondary exploratory status?

## Excluded observations

Each observation is listed once with exactly one normative reason code; repeated occurrences are consolidated. Reconciled routine cell checks are summarized in the per-relationship completion table rather than represented as findings.

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 p.4, S001 | Literal total 392 versus four cells of 196 is resolved by the explicit factorial main-effect context and reproduced marginal n≈392/cell n≈196; the final 250 per cell also identifies recruitment grouping. | CONTEXT_RESOLVES |
| DOC-001 p.4, S001 | Rounded attrition 22%, cell size196, and target250 need not reproduce an exact integer from rounded percentages or an unnamed sample-size algorithm. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-002 pp.16–17, S051 | “Difference25%” is followed immediately by explicit control30%/intervention15%; the assumed incidences are identifiable despite the generic introductory wording. | CONTEXT_RESOLVES |
| DOC-002 pp.16–17, S051 | A simple two-proportion approximation does not reconstruct180 per cell because the source describes additive interaction and a different synergy contrast without all four incidence inputs or the power algorithm. | CONDITIONAL_OR_UNREPORTED |
| DOC-002 pp.16–17, S051 | 180/.80=225 is below250, and the protocol calls250 sufficient rather than asserting exact equality. | CONTEXT_RESOLVES |
| DOC-001 pp.1,4,6–7, S002–S007 | Effect-coded adjusted imputed OR/HR values differ from crude printed-count contrasts; explicit coding identifies the coefficient scale and model. | MODEL_VERSUS_CRUDE |
| DOC-001 pp.4,8, S008 | General GEE methods versus robust-linear T12 footnote are resolved by the table's explicit overall/T12 model definitions. | CONTEXT_RESOLVES |
| DOC-001 p.8, S009,S010,S013,S017 | Doubling rounded coefficients/endpoints differs by .01 from some full narrative contrasts but overlapping rounding intervals reproduce every matching value. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p.8, S021; DOC-004 p.21, S087 | Utility intervals end at display-zero .000 while P=.052/.055; a small negative hidden upper endpoint rounds to .000. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 pp.4,6–8, S002–S024; DOC-004 pp.18–22, S073–S093 | Reconstructing exact pooled or robust P values from rounded intervals or SEs without analysis-specific degrees of freedom, variance components, and CI/test procedure is conditional; no such definitions were inferred. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 pp.4,8, S032 | Cohen D, including IDS therapy .006 versus adjusted B−.28, uses baseline/follow-up means and pooled SDs, not adjusted B divided by SD; exact imputed input summaries are absent. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 pp.4,8; DOC-004 pp.14–15,22, S026,S072,S090–S093 | A scalar CACE division of the printed OR or log-OR by observed compliance cannot reconstruct an explicitly SEM-based imputed estimate without its latent-class model and inputs. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 pp.4,8, S028; DOC-004 p.21, S078–S089 | MI and no-MI sensitivity estimates arise from separately specified analyses; comparable does not assert identical coefficients, interaction specification, or P values. | CONTEXT_RESOLVES |
| DOC-001 p.6, S029 | Exact reproduction of attrition P=.47/.62/.91 needs the unnamed test and its tested table; missingness counts are separately mapped and no contradictory decision is printed. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 p.8; DOC-004 p.23, S030,S094 | Concealment test is not named; the printed directional differences and P<.001 are compatible, while exact test reconstruction would assume its statistic. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 pp.4,8–9, S031 | Nominal secondary significance is explicitly exploratory under multiplicity caution; there is no asserted adjusted threshold or noninferiority/equivalence conclusion. | CONTEXT_RESOLVES |
| DOC-002 pp.8,28,33–34; DOC-003 p.2; DOC-001 p.4, S050,S061 | DSM-5 versus DSM-IV wording is resolved by the explicit MINI5.01/5.0 instrument and repeated DSM-IV definition; no supplied outcome mapping establishes a changed reported number. | TERMINOLOGY_OR_WORDING |
| DOC-002 pp.39,43; DOC-003 p.4; DOC-001 pp.4,6, S053,S066 | Protocol supplementary per-protocol wording is made precise by SAP/report's CACE description; the report clearly retains ITT as primary. | TERMINOLOGY_OR_WORDING |
| DOC-002 pp.43–44; DOC-003 pp.4–5, S056–S059,S069 | Broader nonmental, mediation, 24-month, and modifier outputs are outside this expressly 12-month mental-health article; SAP explicitly reserves other modifiers for another paper. | CONTEXT_RESOLVES |
| DOC-002 pp.40–42,49, S060 | No numerical efficacy interim/stopping rule is supplied; absence of one does not establish a contradictory decision. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p.3, S065 | Printed “p0.05” has an evident significance-threshold reading from the sentence and report's matching two-sided .05 statement. | NOTATION_OR_TYPOGRAPHY |
| DOC-003 p.3; DOC-001 p.8, S064,S032 | Standardized differences are supplied as Cohen D but without their own CI/P; absence of precision alone is not a reproduced inconsistency. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p.4; DOC-001 pp.4,6–7, S067 | Planned additive-interaction RERI sensitivity output is not located; the displayed interaction is explicitly logistic/multiplicative. No conflicting additive result or claim is supplied, and an unreported sensitivity detail alone cannot change an extracted printed RERI. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p.5; DOC-001 p.4, S070,S071 | MAR/MI100/Rubin are specified coherently; unreported imputation predictors, outlier diagnostics, transformations, and assumption-dependent sensitivity inputs are not contradictions. | CONDITIONAL_OR_UNREPORTED |
| DOC-004 p.19, S074 | Country adjustment intervals are not centered exactly on B (Spain midpoint .048 versus .107; UK .1335 versus .117; Germany .1025 versus .058), but point estimates are contained and interval computation/pooling is not defined for this table. Symmetric-Wald reconstruction would assume an unreported definition; these ancillary country coefficients are not intervention effects. | CONDITIONAL_OR_UNREPORTED |
| DOC-004 p.19, S074 | Baseline GAD P=0 is a permitted display-zero representation of a very small P value. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-004 p.20, S075–S077 | Two C2 headings and subgroup covariate coefficients need not equal the pooled model main effect because the populations and model contrasts differ; each table names its population. | CONTEXT_RESOLVES |
| DOC-004 p.22, S090–S093 | Integer-like compliance shorthand8/21 versus≥8 and supplement omega≥70% is immediately read with the SAP and report's explicit adherence definitions; no distinct fitted compliance population is established. | CONTEXT_RESOLVES |

## Explicit relationship completion records

| S ID | Pass status | Outcome and bounded check |
|---|---|---|
| S001 | PASS_1_COMPLETE | Report factorial sample-size diagnostic reproduces392 marginal/196 cell; contextual grouping resolved; protocol input comparison F-ST1-001. |
| S002 | PASS_1_COMPLETE | Primary supplement OR1.06(.87–1.29),P.57 contains estimate/null; source occurrences match; coding/imputation explicit. |
| S003 | PASS_1_COMPLETE | Primary therapy OR.93(.76–1.13),P.47 contains estimate/null; source occurrences match. |
| S004 | PASS_1_COMPLETE | Interaction OR.93(.76–1.14),P.48 contains estimate/null; explicit multiplicative model; additive detail excluded. |
| S005 | PASS_1_COMPLETE | Supplement HR1.05(.86–1.27),P.65 direction/containment match; primary/time-to-onset priority F-ST1-002. |
| S006 | PASS_1_COMPLETE | Therapy HR.91(.75–1.10),P.32 direction/containment match; analysis priority F-ST1-002. |
| S007 | PASS_1_COMPLETE | Interaction HR.91(.75–1.11),P.36 direction/containment match; analysis priority F-ST1-002. |
| S008 | PASS_1_COMPLETE | OverallGEE versus T12 robust-linear distinctions and coefficient doubling explicitly resolve method/scale. |
| S009 | PASS_1_COMPLETE | PHQ supplement overall.33(.12–.53),P.002; positive direction; narrative doubled contrast matches rounding. |
| S010 | PASS_1_COMPLETE | PHQ supplementT12.28(.05–.50),P.02; narrative full contrast matches rounding. |
| S011 | PASS_1_COMPLETE | PHQ therapy overall−.13(−.33–.07),P.19; null inclusion agrees. |
| S012 | PASS_1_COMPLETE | PHQ therapyT12−.17(−.39–.06),P.14; null inclusion agrees; D separately defined. |
| S013 | PASS_1_COMPLETE | IDS supplement overall.60(.15–1.05),P.01; full contrast1.20 matches; endpoint hierarchy F-ST1-003. |
| S014 | PASS_1_COMPLETE | IDS supplementT12.36(−.19–.90),P.20; null inclusion agrees; hierarchy F-ST1-003. |
| S015 | PASS_1_COMPLETE | IDS therapy overall−.23(−.67–.22),P.32; null inclusion agrees; hierarchy F-ST1-003. |
| S016 | PASS_1_COMPLETE | IDS therapyT12−.28(−.83–.27),P.31; adjusted coefficient versus D distinct; hierarchy F-ST1-003. |
| S017 | PASS_1_COMPLETE | GAD supplement overall.25(.08–.42),P.004; doubled narrative.50 matches. |
| S018 | PASS_1_COMPLETE | GAD supplementT12.14(−.04–.33),P.13; null inclusion agrees. |
| S019 | PASS_1_COMPLETE | GAD therapy overall−.16(−.32–.01),P.06; null inclusion agrees. |
| S020 | PASS_1_COMPLETE | GAD therapyT12−.24(−.42–−.06),P.01; narrative−.48 matches; lower anxiety direction agrees. |
| S021 | PASS_1_COMPLETE | Utility supplement overall−.006(−.012–.000),P.052; roundedzero endpoint reconciles nominal decision. |
| S022 | PASS_1_COMPLETE | Utility supplementT12−.002(−.008–.005),P.61; null inclusion agrees. |
| S023 | PASS_1_COMPLETE | Utility therapy overall.002(−.003–.008),P.44; null inclusion agrees. |
| S024 | PASS_1_COMPLETE | Utility therapyT12.004(−.002–.009),P.23; null inclusion agrees. |
| S025 | PASS_1_COMPLETE | Secondary interactionP.41–.98 implies no nominal significance; table omission explicit and coherent. |
| S026 | PASS_1_COMPLETE | CACE therapyOR.78(.64–.95) agrees with significance narrative and supplement; SEM inputs prevent scalar reconstruction. |
| S027 | PASS_1_COMPLETE | Moderation narrative directions match all corresponding supplement coefficients and populations; no missing interactions inferred. |
| S028 | PASS_1_COMPLETE | No-MI sensitivity model explicitly separate; comparable results checked against all supplied sensitivity cells. |
| S029 | PASS_1_COMPLETE | AttritionP.47/.62/.91 are nonsignificant; exact unnamed test reconstruction bounded. |
| S030 | PASS_1_COMPLETE | Concealment8.2/10.4/25.5/43.7% direction matches supplement; test method absent but no contradiction. |
| S031 | PASS_1_COMPLETE | ITT null and exploratory secondary conclusions follow stated two-sided.05 rule; IDS hierarchy F-ST1-003. |
| S032 | PASS_1_COMPLETE | All eight D values reviewed as imputed baseline-follow-up standardized contrasts, distinct from adjusted coefficients; underlying inputs absent. |
| S050 | PASS_1_COMPLETE | Instrument terminology context resolves DSM wording; IDS main-endpoint hierarchy F-ST1-003. |
| S051 | PASS_1_COMPLETE | Protocol power inputs differ from report F-ST1-001; interaction-power reconstruction bounded; conservative250 target coherent. |
| S052 | PASS_1_COMPLETE | Individual factorial randomization, site/history strata, four250 arms coherent with report analysis-unit adjustment. |
| S053 | PASS_1_COMPLETE | ITT and supplementary adherence analysis explained by SAP CACE; baseline test detail does not alter reported inference. |
| S054 | PASS_1_COMPLETE | Protocol primary time-to-event/Cox priorities differ from SAP/report F-ST1-002. |
| S055 | PASS_1_COMPLETE | Protocol primary mixed MDD/IDS analysis compared with SAP/report F-ST1-002 and IDS hierarchy F-ST1-003. |
| S056 | PASS_1_COMPLETE | Secondary repeated-outcome methods reviewed; SAP permits mixed/GEE; country adjustment present, no preferred model inferred. |
| S057 | PASS_1_COMPLETE | Nonmental mediation/blood analyses are outside article's expressly mental-health scope; no conflicting reported number. |
| S058 | PASS_1_COMPLETE | Broad protocol modifiers versus SAP separate-paper provision contextualized; report site/history/baseline moderation explicit. |
| S059 | PASS_1_COMPLETE | Prospective24month online outcomes distinguished from expressly12month article; no misattributed time point. |
| S060 | PASS_1_COMPLETE | Safety suspension qualitative; no numerical efficacy stopping/interim rule or conflicting decision supplied. |
| S061 | PASS_1_COMPLETE | Binary cumulative positive-any/negative-all definition coherent with logistic primary and MI; no unreported missingness mapping inferred. |
| S062 | PASS_1_COMPLETE | SAP IDS secondary matches report but differs from protocol hierarchy F-ST1-003. |
| S063 | PASS_1_COMPLETE | Site/history and corresponding baseline covariates match report/table descriptions; no missing mandatory adjustment. |
| S064 | PASS_1_COMPLETE | SAP logistic primary and mixed/GEEsecondary coherent with report; protocol primary difference F-ST1-002; missing D precision bounded. |
| S065 | PASS_1_COMPLETE | Two-sided.05 threshold matches report; notation slip resolves; no multiplicity correction invented. |
| S066 | PASS_1_COMPLETE | ITT/CACE and≥70%/≥8of21 compliance thresholds match report; source fallback selfreport clear. |
| S067 | PASS_1_COMPLETE | Multiplicative interaction maps to displayed logistic interaction; unreported RERI sensitivity lacks a contradictory value or additive claim. |
| S068 | PASS_1_COMPLETE | SAP explicitly secondary Cox versus report post hoc priority F-ST1-002. |
| S069 | PASS_1_COMPLETE | Site/history modifiers and.05 interaction rule match report; other modifiers reserved for separatepaper, baseline analysis labeledposthoc. |
| S070 | PASS_1_COMPLETE | MAR100MI/Rubin pooling coherent with report; sensitivity and missing predictors bounded by supplied definitions. |
| S071 | PASS_1_COMPLETE | Conditional outlier/transformation steps do not establish an unmet condition or a conflicting fitted method. |
| S072 | PASS_1_COMPLETE | CACE latentclass/exclusionrestriction/SEM assumptions explicitly stated; exact nonlinear fitted estimate not reconstructed by scalar OR division. |
| S073 | PASS_1_COMPLETE | All9 nonreference tableA cells checked for order/containment/null decisions; FBA×PHQ−.064 andP.020 support larger reduction at higher baseline. |
| S074 | PASS_1_COMPLETE | All9 nonreference tableB cells checked; supplement×GAD.062(.009–.115),P.022 direction agrees; country asymmetry conditional; P0 excluded. |
| S075 | PASS_1_COMPLETE | All13 nonreference C1 cells checked; FBA×UK.017(.001–.033),P.041 supports stated site moderation; other interaction null decisions agree. |
| S076 | PASS_1_COMPLETE | All4 UK subgroup coefficients checked; FBA.013(.001–.024),P.033 direction/nominal decision agree; pooling definitions absent. |
| S077 | PASS_1_COMPLETE | All4 Netherlands subgroup coefficients checked; FBA−.007(−.019–.005),P.267 null inclusion agrees. |
| S078 | PASS_1_COMPLETE | NoMI PHQ supplement overall.30(.11–.49),P.002 andT12.28(SE.11),P.013 compatible within precision. |
| S079 | PASS_1_COMPLETE | NoMI PHQFBA overall−.14(−.34–.05),P.14 andT12−.22(SE.11),P.052 compatible within precision. |
| S080 | PASS_1_COMPLETE | NoMI PHQinteraction overall−.01(−.20–.18),P.94 andT12.02(SE.11),P.84 compatible within precision. |
| S081 | PASS_1_COMPLETE | NoMI IDS supplement overall.55(.11–.99),P.01 andT12.28(SE.28),P.30 compatible within precision. |
| S082 | PASS_1_COMPLETE | NoMI IDSFBA overall−.26(−.70–.18),P.25 andT12−.36(SE.28),P.20 compatible within precision. |
| S083 | PASS_1_COMPLETE | NoMI IDSinteraction overall−.01(−.45–.43),P.96 andT12.12(SE.28),P.66 compatible within precision. |
| S084 | PASS_1_COMPLETE | NoMI GADsupplement overall.24(.08–.40),P.004 andT12.17(SE.09),P.07 compatible within precision. |
| S085 | PASS_1_COMPLETE | NoMI GADFBA overall−.16(−.32–.00),P.06 andT12−.26(SE.09),P.005 compatible with rounded endpoint/SE. |
| S086 | PASS_1_COMPLETE | NoMI GADinteraction overall.04(−.13–.20),P.66 andT12.03(SE.09),P.74 compatible within precision. |
| S087 | PASS_1_COMPLETE | NoMI utilitysupplement overall−.006(−.011–.000),P.055 andT12−.001(SE.003),P.66 compatible with roundedzero/SE. |
| S088 | PASS_1_COMPLETE | NoMI utilityFBA overall.002(−.004–.007),P.51 andT12.004(SE.003),P.23 compatible within precision. |
| S089 | PASS_1_COMPLETE | NoMI utilityinteraction overall−.002(−.008–.003),P.42 andT12.001(SE.003),P.65 compatible within precision; interaction model explicit. |
| S090 | PASS_1_COMPLETE | CACE MDDtherapy.78(.64–.95)* andsupplement.84(.67–1.07) agree with nominal marks; main matching result identical. |
| S091 | PASS_1_COMPLETE | CACE PHQtherapy−.22(−.59–.15),supplement.43(.08–.77)* have contained estimates and matching decisions. |
| S092 | PASS_1_COMPLETE | CACE IDStherapy−.42(−1.24–.40),supplement.47(−.33–1.27) null inclusion agrees; model adjustedbaseline/site/history explicit. |
| S093 | PASS_1_COMPLETE | CACE GADtherapy−.31(−.60–−.02)*,supplement.18(−.11–.47) decisions/directions agree; compliance footnotes contextualized. |
| S094 | PASS_1_COMPLETE | Threecategory concealmentcounts sum759 and match main percentages; P<.001 plausible, exact unnamed test not inferred. |

## Limits and handoff

No assigned relationship or displayed adjustment row remains uncovered. Exact mechanical reproduction is unavailable where the source omits analysis-specific imputation variance/df, CI construction, robust test statistic/df, CACE latent-model inputs, factorial interaction power inputs, raw imputed mean/SD summaries, or named attrition/concealment tests. These missing definitions do not establish a contradictory analysis. S-ID completion is explicit for all 77 IDs; stable IDs were preserved, not reassigned. Three findings require independent inclusion screening; no C ID, adjudication, severity, disposition, or correction is assigned here. Excluded-observation count: 28.
