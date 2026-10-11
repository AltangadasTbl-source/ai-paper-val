# Cross-source consistency review

Fresh specialist runtime ID: 01a12959-801d-7763-b4b6-80ba61b5f412. Model: gpt-6.1-sol; reasoning effort: medium. Scope: all matched results and statistical design elements in six supplied sources, 100 mapped PDF pages. Document roles: main article, results supplement and data-sharing statement REPORT; protocol, amendment overview and updated SAP PLAN. All four main and four support map parts were read; no earlier scientific conclusion was used. Checks were divided into three disjoint logical batches, each below 120 relationships: results, criteria/definitions, design/analyses. Every apparent observation was independently self-screened. No C IDs or adjudications are assigned here.

The source-linked comparison records are [results](cross_source_results_checks.md), [criteria and definitions](cross_source_criteria_checks.md), and [design and analyses](cross_source_design_checks.md). Matched population is eligible randomized high PEEP plus recruitment versus low PEEP without routine recruitment; binary outcomes use 989/987 unless a different analysis set is explicit. Five-day primary outcomes, per-protocol outcomes, 90-day hospital-free days, time-to-event HRs, component Bonferroni intervals and repeated-time interactions were kept distinct. No structured participant data were supplied; the data-sharing statement is not a dataset.

Complete comparison count: 130 records, comprising 51 results, 49 itemized criteria/definitions and 30 design/analysis records. Finding count: 9. Excluded-observation count: 17. The log-rank and severity-weighted GEE omissions have separate finding IDs because they are distinct specified analyses without a source-established shared cause.

Evidence: byte-matched layout derivatives and newly produced maps were locators. Exact supplied PDF pages were read directly with Poppler pdftotext 26.01.0 where needed. Source-page image confirmation was used for coma ≤8 and the eFigure 12 effect-measure header; existing images have unrecorded historical rendering engines. No new derivative was produced, no OCR performed, and no source/reused asset modified. Compute device CPU. Nine findings are emitted below. Findings concern reporting and specification; alternatives are questions for human review, not proposed corrections.

## Findings

### F-XS-001

**Title:** Abstract hypoxemia interval has a positive upper bound while its matched table interval has a negative upper bound.

**Locations and roles:** REPORT [main abstract, PDF p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1); REPORT [Table 3, PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9); REPORT [secondary-outcome interpretation, PDF pp.10-11](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).

**Printed values and comparison:** The abstract prints hypoxemia 5.0% versus 13.6%, difference −8.6%, 95% CI −11.1% to **6.1%**, P<.001. Table 3 prints 49/989 versus 134/987, difference −8.6%, 95% CI −11.1% to **−6.1%**, P<.001. Population, outcome, time and contrast match exactly. The abstract interval contains zero while the P value is below .001; the table interval excludes zero. The copies' upper-bound intervals are [6.05,6.15] and [−6.15,−6.05], gap 12.10 percentage points, relative gap 12.10/6.1=1.984. This arithmetic supplements the interval/test conflict; category 1 does not use rounding exclusions.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 1; independently Route A, category 2.

**Affected result or extracted value:** Abstract 95% CI for high-minus-low intraoperative hypoxemia and its significance reading.

**Why context does not resolve it:** Route A requires registration of the printed interval/test conflict even though the table supplies a reconstructable alternative.

**Supported alternatives:** The table supports the negative upper bound; the abstract's positive bound is independently printed. No separate abstract analysis is described.

**Exact human question:** Which upper bound belongs to the abstract hypoxemia difference, and should the interval and P value be treated as outputs from the same analysis?

### F-XS-002

**Title:** The same primary collapsed-composite estimate is labeled risk ratio in the article and odds ratio in the sensitivity figure.

**Locations and roles:** REPORT [abstract, PDF p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), REPORT [primary analysis, PDF p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), REPORT [Table 3, PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), REPORT [Figure 2, PDF p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), versus REPORT [eFigure 12, PDF p.42](../../../joi190055supp4_prod_16092.pdf#page=42). PLAN [SAP p.2](../../../joi190055supp3_prod_16092.pdf#page=2) corroborates the article risk-ratio specification and is not an independent conflicting side.

**Printed values and comparison:** Article and Figure 2 print risk ratio 0.93 (95% CI 0.83–1.04) for the first-five-day collapsed PPC composite. eFigure 12 places “Collapsed Composite” 0.93 [0.83,1.04] under “Odds Ratio (95% CI).” The other global rows are proportional-odds and GEE outputs, also under that heading. The exact primary tuple is repeated but the measure changes. Display-copy intervals overlap completely; gap zero. This is a quantity-identity conflict, not a numeric discrepancy. No additional collapsed-composite odds-ratio model is supplied that establishes a different tuple.

**Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_C. **All relationships:** S_C.

**Qualifying route:** Route B.

**Affected result or extracted value:** Whether 0.93 (0.83–1.04) is extracted as RR or OR for the primary outcome.

**Why context does not resolve it:** Both RR and OR are plausible quantities in a figure mixing binomial and GEE analyses; the numbers alone do not identify which measure the collapsed-composite row represents. This changes evidence-synthesis coding, rather than merely naming the same group.

**Supported alternatives:** The row could repeat the article RR under a shared OR header, or refer to a separately calculated OR. The package does not identify the latter analysis.

**Exact human question:** What measure and model produced the eFigure 12 collapsed-composite row, and is its 0.93 (0.83–1.04) the same RR shown in the article?

### F-XS-003

**Title:** Five-day mortality is a post hoc outcome in the article and a secondary outcome in the results supplement.

**Locations and roles:** REPORT [main outcome hierarchy, PDF p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), REPORT [Table 3 post hoc section, PDF p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), versus REPORT [eMethods secondary list, PDF p.21](../../../joi190055supp4_prod_16092.pdf#page=21). PLAN [final SAP outcome list, PDF p.1](../../../joi190055supp3_prod_16092.pdf#page=1) lists in-hospital mortality but not five-day mortality, corroborating the article side.

**Printed values and comparison:** The article explicitly states “Post hoc outcomes included 5-day mortality” and puts deaths 5 versus 3, HR1.67 (0.40–6.97), P=.48 in its post hoc table section. Supplement eMethods explicitly lists “5-day and in-hospital mortality” among “secondary outcomes.” Matching five-day mortality is also reported in REPORT [eFigure 11, p.41](../../../joi190055supp4_prod_16092.pdf#page=41), HR1.67 (0.40–6.97), P=.484, whose rounding overlaps .48. The conflict is outcome status, not the rounded P copy.

**Focus area:** D/outcome-status attribution. **Proposed review domain:** report_internal_inconsistency. **Proposed relationship:** S_C. **All relationships:** S_C.

**Qualifying route:** Route B.

**Affected result or extracted value:** Prespecified-secondary versus post hoc status of the five-day mortality HR.

**Why context does not resolve it:** The two report documents supply different explicit hierarchy assignments for the same reported outcome. Secondary versus post hoc affects interpretation of the result's analysis provenance; a reader cannot make both assignments simultaneously.

**Supported alternatives:** The eMethods list could have grouped a later post hoc endpoint with secondary endpoints, or the article's hierarchy could differ from the operational report definition. The final SAP supports only in-hospital mortality as secondary.

**Exact human question:** Was five-day mortality prespecified as a secondary outcome or added post hoc, and how should the eMethods list be interpreted alongside the article?

### F-XS-004

**Title:** The protocol's secondary outcome hierarchy is changed in the final SAP and report.

**Locations and roles:** PLAN [protocol synopsis, PDF p.5](../../../joi190055supp1_prod_16092.pdf#page=5), PLAN [protocol secondary endpoint list, PDF p.12](../../../joi190055supp1_prod_16092.pdf#page=12), versus PLAN [updated SAP list, PDF p.1](../../../joi190055supp3_prod_16092.pdf#page=1), REPORT [main secondary list, PDF p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), and REPORT [eMethods, PDF p.21](../../../joi190055supp4_prod_16092.pdf#page=21). PLAN [amendment overview, pp.1-3](../../../joi190055supp2_prod_16092.pdf#page=1) supplies changes but no explicit corresponding secondary-endpoint revision.

**Printed statements and comparison:** Protocol secondary endpoints include postoperative invasive/noninvasive ventilatory support, hospital readmission within30 days and mortality at90 days. Updated SAP instead lists severe PPC excluding mild respiratory failure and in-hospital mortality, and omits standalone postoperative ventilatory support,30-day hospital readmission and90-day mortality. Article follows the updated list. Ventilatory support is still a severe respiratory-failure component, which is not the same standalone outcome; in-hospital mortality is not the same time window as90-day mortality. The SAP is explicitly finalized January20,2018 before last inclusion, database locking and analysis, and the article identifies this final SAP. This context is preserved: no assertion of undisclosed timing or noncompliance is made.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R, P_P.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Which secondary endpoints and mortality follow-up window were prespecified, and whether omitted original secondary endpoints retained any prospective status.

**Why context does not resolve it:** Route A requires recording reproduced changes in prespecified outcome status or composite definition. A prospective updated SAP is an alternative explanation to be retained, rather than an automatic screen-out of the change.

**Supported alternatives:** The final SAP may constitute an approved outcome-hierarchy revision superseding the protocol, or the earlier endpoints may have remained prospectively planned but omitted from this report. The supplied overview does not state that specific revision.

**Classification ambiguity:** The direct difference exists both PLAN-to-PLAN and PLAN-to-REPORT; P_R has precedence. The updated SAP's prospective timing is disclosed and may resolve the human assessment of why the lists differ.

**Exact human question:** Did the final SAP formally supersede the protocol's ventilatory-support,30-day readmission and90-day mortality endpoints, and what prospective status and reporting location apply to each original endpoint?

### F-XS-005

**Title:** The planned randomization block and risk-balancing specification differs from the reported allocation specification.

**Locations and roles:** PLAN [protocol randomization, PDF pp.12-13](../../../joi190055supp1_prod_16092.pdf#page=12), REPORT [main randomization, PDF p.2](../../../jama_bluth_2019_oi_190055_16092.pdf#page=2). PLAN [supplied amendment overview, pp.1-3](../../../joi190055supp2_prod_16092.pdf#page=1) and PLAN [updated SAP, pp.1-3](../../../joi190055supp3_prod_16092.pdf#page=1) were checked for an allocation amendment.

**Printed statements and comparison:** Protocol specifies permuted-block randomization “block length6,” balanced per center, and randomization must take account of intermediate/high ARISCAT risk subgroups to assure balance. Article specifies permuted random block sizes4,6,8 and stratification by study site. Both use1:1 allocation of the same intervention and patient population. Fixed6 versus variable4/6/8 is an explicit statistical design difference, not a display-precision comparison. The article does not state ARISCAT balancing; omission alone is an unresolved qualifier rather than proof it was absent.

**Focus area:** D/statistical allocation specification. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** Allocation strata/block specification and the interpretation of site-only adjustment for the primary PPC result.

**Why context does not resolve it:** The supplied statistical design descriptions give different block schemes, with no corresponding amendment identified. Allocation strata are relevant to the specification of the reported stratification sensitivity analysis; this is more than a site-count comparison.

**Supported alternatives:** Allocation may have been prospectively amended to variable block sizes, or the article may summarize the operational scheme differently. ARISCAT balancing may have been retained without being restated.

**Exact human question:** Which allocation block scheme and ARISCAT balancing rule were used, and where is the applicable amendment recorded?

### F-XS-006

**Title:** Reported mild/moderate respiratory-failure criteria introduce an oxygen-flow boundary absent from the supplied protocol.

**Locations and roles:** PLAN [protocol primary-component definitions, PDF p.31](../../../joi190055supp1_prod_16092.pdf#page=31), REPORT [Table 3 note d, PDF p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), REPORT [eMethods component definitions, PDF p.20](../../../joi190055supp4_prod_16092.pdf#page=20). PLAN [updated SAP, PDF p.1](../../../joi190055supp3_prod_16092.pdf#page=1) specifies severe PPC excluding mild respiratory failure and refers to components defined elsewhere.

**Printed statements and comparison:** Protocol mild respiratory failure is PaO2<60 or SpO2<90 after at least10min room air, responding to supplemental oxygen without a flow cutoff; moderate respiratory failure is the same low oxygen thresholds “despite supplemental oxygen.” Report Table3 distinguishes mild responding to2L/min or less and moderate responding only to more than2L/min; report eMethods prints =2L/min for mild and >2L/min for moderate. The report's explicit2L/min boundary can classify a patient who responds to higher-flow oxygen as moderate rather than mild. The protocol's broad “responding” clause and “despite” clause do not specify that boundary. The report-internal =2/≤2 shorthand is not separately emitted.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Component counts135/154 mild and42/58 moderate, and severe PPC composite116/134 that excludes mild respiratory failure.

**Why context does not resolve it:** Route A covers a composite definition change. Mild-versus-moderate allocation changes membership of the severe composite; the term “supplemental oxygen” alone does not establish the report's2L/min decision rule.

**Supported alternatives:** The2L/min criterion could be an operational clarification used throughout the trial, or a revised severity criterion. No supplied amendment explicitly establishes this cutoff.

**Exact human question:** What oxygen-flow rule distinguished mild from moderate respiratory failure during outcome collection, and was the report's2L/min boundary an approved clarification of the protocol definition?

### F-XS-007

**Title:** The coma component threshold is inclusive in the protocol and strict in the results supplement.

**Locations and roles:** PLAN [protocol extrapulmonary definition, PDF p.32](../../../joi190055supp1_prod_16092.pdf#page=32), REPORT [eMethods extrapulmonary definition, PDF p.21](../../../joi190055supp4_prod_16092.pdf#page=21), REPORT [main Table3 coma/composite, PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9).

**Printed statements and comparison:** Direct visual protocol reading gives Glasgow Coma Score **≤8**, absent therapeutic coma/sedation. Report eMethods gives Glasgow Coma Score **<8** under the same exclusions. The reusable protocol text loses the underline and reads <8; that derivative does not supersede the source image. For integer GCS,≤8 includes8 and<8 excludes8; this is an endpoint decision criterion, not rounded copies of a result.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Coma2/2 and extrapulmonary composite167/150, with potential differences for patients scoring8.

**Why context does not resolve it:** Route A covers changes to a prespecified composite component. The two explicit thresholds give different eligibility for GCS8, with no supplied threshold amendment.

**Supported alternatives:** One threshold may be the operational definition, or an amendment/clarification may have been used; the package does not identify it. No assumption is made that any actual patient had GCS8.

**Exact human question:** Did the operational coma definition include GCS8, and which source definition applied to the reported coma and extrapulmonary composite counts?

### F-XS-008

**Title:** The planned primary time-to-event log-rank comparison is not identified among the reported Cox outputs.

**Locations and roles:** PLAN [SAP primary time-to-event plan, PDF p.2](../../../joi190055supp3_prod_16092.pdf#page=2), PLAN [SAP clinical-severity-weighted GEE, PDF p.3](../../../joi190055supp3_prod_16092.pdf#page=3), REPORT [main analysis, PDF p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), REPORT [eFigure8, PDF p.38](../../../joi190055supp4_prod_16092.pdf#page=38), REPORT [eTable9, PDF p.30](../../../joi190055supp4_prod_16092.pdf#page=30), REPORT [eFigure12, PDF p.42](../../../joi190055supp4_prod_16092.pdf#page=42), REPORT [additional-analysis discussion, PDF pp.10-11](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).

**Printed statements and comparison:** SAP p.2 plans Kaplan-Meier time-to-PPC curves compared by log-rank. Main report instead specifies Cox models and eFigure8 reports HR0.88 (0.73–1.06), P=.190, with proportional-hazards diagnostics; no result is identified as log-rank. Full mapped report content was checked, including captions and footnotes; no planned log-rank output is identified under another label. The SAP p.3 and eTable9/eFigure12 locations above were checked for additional primary analyses and are corroborating negative-search context, not an additional weighted-analysis issue within this finding.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The planned primary time-to-PPC log-rank comparison versus the reported Cox HR/P.

**Why context does not resolve it:** Route A always registers an unreported planned primary analysis. A Cox HR/P is not explicitly the planned log-rank test; related methods yielding similar conclusions do not establish the planned test's reporting.

**Supported alternatives:** Log-rank may have been performed but not displayed, Cox may have replaced it, or the displayed P may correspond to another test despite the Cox description. No preferred analysis is proposed.

**Exact human question:** Where is the prespecified primary log-rank output, or what replacement or omission applies to it?

### F-XS-009

**Title:** The planned clinical-severity-weighted primary composite GEE has no identified reported output.

**Locations and roles:** PLAN [SAP clinical severity weight analysis, PDF p.3](../../../joi190055supp3_prod_16092.pdf#page=3), REPORT [eTable9, PDF p.30](../../../joi190055supp4_prod_16092.pdf#page=30), REPORT [eFigure12, PDF p.42](../../../joi190055supp4_prod_16092.pdf#page=42), REPORT [main sensitivity methods, PDF p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), REPORT [additional-analysis discussion, PDF pp.10-11](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).

**Printed statements and comparison:** SAP explicitly plans a posteriori clinical severity weights for each primary component and a multivariate common-effect GEE OR. The report displays count, individual components, common-effect GEE, average relative effect and heterogeneity analyses, but identifies no severity weights or weighted common-effect estimate. eTable9's common-effect footnote describes a single treatment effect across all12 components without identifying clinical severity weighting. Full report maps, captions and footnotes contain no separately identifiable weighted output. This absence is a distinct specified analysis from the log-rank comparison in F-XS-008; no common production cause is inferred.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified severity-weighted sensitivity estimate for the primary composite and the narrative statement that alternative statistical assumptions gave similar results.

**Why context does not resolve it:** Route A always registers an unreported planned primary analysis. A common-effect row lacking a weighting specification does not establish that the planned clinically weighted analysis was reported.

**Supported alternatives:** The weighted analysis may have been performed without display, omitted, or incorporated in a displayed row without identifying weights. The package does not distinguish these alternatives.

**Exact human question:** Where is the planned severity-weighted GEE output, and what component weights or omission applied?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT main abstract p.1 versus Figure1 p.3 | Abstract intervention arm sizes989/987 are analysis counts, whereas randomized sizes are1011/1002. Half-unit copy gaps21/14 divided by1011/1002 are.0208/.0140, below.05; numerical difference is screened under display precision. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main Table1 pp.5-6 versus Figure2 p.10 | BMI categories use35–40/>40 versus<40/≥40, with different at-boundary counts. Descriptive baseline categories and planned subgroup partition are explicitly different; no primary subgroup result is assigned to the baseline partition. | PERIPHERAL_COMPARISON |
| REPORT main Table2 p.8 versus REPORT eTable3 p.24 | Synthetic-colloid P values .50 versus .09 correspond to median conditional volumes versus overall mean volumes; count P .09 versus .10 is also an apparent difference. These perioperative secondary displays do not alter a primary/key-secondary result or analysis-population size. | PERIPHERAL_COMPARISON |
| PLAN protocol p.12 versus PLAN pp.10-11 | Procedure section retains total748 while enrollment/re-estimation state2013. The adjacent original/revised sample-size section explicitly provides the version sequence and operative revised target. | CONTEXT_RESOLVES |
| PLAN protocol p.23 versus PLAN p.22/SAP p.2 | General significance .05 versus final primary threshold.044. Specific sequential primary rule supplies the exception; different general and interim-adjusted levels are identified. | CONTEXT_RESOLVES |
| PLAN protocol p.23 versus PLAN SAP p.2/REPORT main p.4 | Preliminary logistic/SPSS specification versus final RR/χ²/R analysis. Protocol explicitly delegates final a priori SAP, and the supplied prospective updated SAP states the operative analysis. No conflict with that final RR plan was inferred solely from this superseded description. | CONTEXT_RESOLVES |
| PLAN SAP p.2 versus REPORT main pp.4,9 | Planned hospital-free-days mean-ratio zero-inflated beta GAM consistency analysis is not displayed. Hospital-free days is a secondary, not separately designated key-secondary outcome; omission alone is not a reproduced conflicting result. | CONDITIONAL_OR_UNREPORTED |
| REPORT eFigure11 p.41 | Caption says extrapulmonary complications but immediately parenthesizes5-day mortality, matching title,axis,HR and proportions. The death outcome is identifiable at once. | TERMINOLOGY_OR_WORDING |
| REPORT main Table3 note d p.10 versus REPORT eMethods p.20 | Mild respiratory failure oxygen flow≤2 versus=2. Context identifies the conventional low-flow severity boundary and no separately reported<2L subgroup; do not treat this shorthand as an independent candidate. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p.13 versus REPORT main p.3/eMethods p.19 | Target SpO2≥93% versus>92%; these are the same integer pulse-oximetry threshold in immediate rescue context. | TERMINOLOGY_OR_WORDING |
| PLAN SAP p.2 versus REPORT main p.4 | Modified ITT versus ITT nomenclature, despite both excluding consent/canceled/eligible-surgery losses and reporting actual989/987. The flow identifies all exclusions; nomenclature alone does not assign a result to a different actual set. | TERMINOLOGY_OR_WORDING |
| REPORT main p.4/flow p.3 | No primary outcome missing data statement versus8 postoperative losses. Primary complete-case dataset is explicitly1976 after exclusions; the statement concerns that analysis dataset, not all2013 randomized participants. | CONTEXT_RESOLVES |
| REPORT main text p.3 versus Table3 notes p.10/eMethods p.21 | Hypoxemia/hypotension durations and baseline-fall clauses are abbreviated in different locations; added fall clauses remain below the same absolute thresholds and the detailed definition supplies the measurement context. No distinct numeric result is assigned to a different endpoint. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p.10 versus REPORT article p.2/eMethods p.18 | Expected surgery≥2h versus>2h is an at-boundary scheduling description without a distinct printed result assigned to a different eligible population. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p.32 versus REPORT eMethods p.21 | Wound infection plus any other infection versus wound infection or any other infection names the same component types; field wording is resolved without identifying a different event result. | TERMINOLOGY_OR_WORDING |
| PLAN protocol changes p.1 | June2014 versus June2013 date label for prior version2.4.1. Calendar-label difference does not change a statistical decision rule in this package. | PERIPHERAL_COMPARISON |
| PLAN historical ARISCAT appendix p.29 versus REPORT eTable1 p.22 | Historical development-sample coefficients are not current primary/key-secondary trial results; apparent text glyph/score differences would be peripheral unless they change the enrollment rule≥26, which matches. | PERIPHERAL_COMPARISON |

## Limitations

No raw participant data, analytic code or Office sources were supplied; no request was made for external data. Graphically plotted repeated-time means and confidence limits are unlabeled and were compared as graphical patterns rather than exact invented coordinates. Historical reusable rendering-engine provenance is unrecorded. None creates an uncovered source unit or limits reproduction of the nine stated findings. Statistical reconstruction of the estimate formulas remains a separate checker scope. The published-source correction notice is retained as context; no external version was sought.
