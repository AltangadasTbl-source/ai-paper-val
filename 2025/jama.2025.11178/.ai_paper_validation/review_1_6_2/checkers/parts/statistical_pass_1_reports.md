# Statistical pass 1 — REPORT supplement shard

Runtime agent: /root/statistics_pass_1_reports. Fresh fixed gpt-6.1-sol/high role. Exact assigned scope: DOC-004 pp1–7; DOC-005 pp1–16 and19, with methods applicable to eTables3,4,5,7,8,9,10; DOC-006 worksheet eTable 3!A1:J115. Entire eTable11 pp17–18 was reassigned before registration and is excluded from this shard's findings, relationship IDs and exclusions.

Completed scope:120 S records(S101–S220),67 coefficient rows,39 outcome/time rows with117 explicit pairwise contrast cells,14 method/selection/numeric families. All525 workbook cells and every nonempty selection-P cell inspected. Full exact row evidence and checks are in statistics/parts/relationship_inventory_reports.md. Six findings and seven excluded-observation families below. No candidate IDs or adjudications assigned.

Evidence uses supplied sources only. New direct images: Poppler pdftoppm26.01.0 CPU,source-07.png through source-11.png andsource-14.png through source-17.png in preprocessing/stat1_reports; page17 was unused after reassignment. Source values for findings on pp7–10 and14 visually confirmed. Workbook source XML and shared strings directly confirm E3,E82,E83 and the selection-P cells. Models and method statements were read from source-linked complete transcription; copied equations were visually mapped by the current mapper. No old scientific conclusions used.

### F-ST1-101

**Title:** Seven imputation coefficients have95% intervals excluding zero alongside P values above.05.

**Locations and document roles:** REPORT [DOC-005 p8,eTable3](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8),each coefficient's estimate,95% CI andP cells. Method context is REPORT [DOC-005 pp4–5](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5): linear GEE imputation model,robust standard errors. Relationship IDs:S106,S107,S112,S114,S119,S120,S126.

| Exact coefficient row | Estimate |95% CI|P|
|---|---:|---|---:|
|Pattern:2 observed follow-ups|−.28|(−.47,−.08)|.150|
|Pattern:1 observed follow-up|−.20|(−.36,−.03)|.226|
|Pattern2 × painTRAINER|−.30|(−.58,−.02)|.280|
|Pattern2 × Health Coach|−.47|(−.74,−.19)|.090|
|Site3|.19|(.08,.29)|.069|
|Site4|.15|(.05,.24)|.124|
|Education:AA degree,second occurrence|.16|(.07,.25)|.077|

**Rule and calculation:** Each printed95% interval lies wholly on one side of zero,while the corresponding P exceeds.05. Each estimate is contained and endpoints are ordered; the discrepancy is the interval-versus-test reading,not containment. Even allowing±.005 to every two-decimal interval limit,the closest-to-null bounds remain−.075,−.025,−.015,−.185,.075,.045,.065 respectively. The P rounding bands do not approach.05. No covariance or reference distribution is needed for this significance comparison. Display-precision screening does not apply to RouteA1; relative discrepancy is not applicable.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W;all compared content is REPORT in one source.
**Qualifying route:** Route A, category 1.
**Affected result or extracted value:** The inferential reading of seven fitted imputation-model coefficients used to construct the primary outcome analysis.
**Why context does not resolve it:** RouteA1 requires registration of the printed interval/test conflict. These are individual coefficient rows,not omnibus versus pairwise tests.

**Alternatives and missing definition:** P values might use another variance calculation,test reference distribution or analysis than the intervals. The report does not identify such a separation. Normal-Wald inverse calculations would be diagnostic only and are not needed for this finding.
**Exact human question:** Which interval and test specifications apply to these seven coefficients,and which printed inferential values should a reader extract?

### F-ST1-102

**Title:** Three printed coefficient intervals touch the null while corresponding P values are below.05.

**Locations and document roles:** REPORT [DOC-005 p9,eTable4](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=9),Age≥65 and second Education:AA degree row; REPORT [DOC-005 p10,eTable5](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10),PEG score. S140,S149,S165.

**Printed values:** Age RR1.15,95% CI(1,1.33),P=.046; second AA education RR1.16,95% CI(1,1.33),P=.046; PEG OR.96,95% CI(.92,1.00),P=.037.

**Rule and calculation:** Null is1 for RR/OR. All three printed closed intervals include1 at an endpoint,while P<.05. Bounds are correctly ordered and estimates contained. This is the reverse interval/test significance conflict. Display-precision screening is inapplicable under RouteA1; no relative discrepancy is assigned.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.
**Qualifying route:** Route A, category 1.
**Affected result or extracted value:** The significance reading of age,education and PEG coefficients in the primary estimation and weighting model summaries.
**Why context does not resolve it:** RouteA1 is always registered for the printed interval-versus-test reading.

**Alternatives and missing definition:** A more precise unrounded lower limit slightly above1 for age/education,or upper limit slightly below1 for PEG,could reconcile the underlying test. The display does not provide that precision. Different test/interval constructions are another possibility. Neither possibility is asserted as the reported analysis.
**Exact human question:** What are the unrounded confidence limits,and do the printed confidence intervals and P values refer to the same inferential specification?

### F-ST1-103

**Title:** Binary education adjustment in the selection summary does not match the fitted primary model parameterization.

**Locations and document roles:** REPORT [DOC-005 p7,eTable2](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7),final variables selected for imputation and estimation; REPORT [DOC-005 p8,eTable3](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8),three education coefficient rows; REPORT [DOC-005 p9,eTable4](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=9),three education coefficient rows. S125,S126,S127,S148,S149,S150,S218.

**Printed values/statements:** eTable2 specifies education“any college vs.HS degree or less.” eTable3 prints education coefficients−.02,.16,.39,each with HS or less as reference; eTable4 prints educationRR.97,1.16,1.35. The first two coefficient rows carry the same AA label,and the third is Graduate degree.

**Rule and calculation:** A binary contrast against HS or less has one education coefficient. The fitted displays contain three separately estimated education coefficients against the same reference,consistent with a multi-level parameterization. Repeated labels alone are not the basis: the numerical coefficient set conflicts with the reported binary coding. Display rounding is not relevant to this discrete model-definition comparison.

**Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.
**Qualifying route:** Route B.
**Affected result or extracted value:** The education adjustment specification in the imputation and primary MCID estimation models.
**Why context does not resolve it:** A reader cannot tell whether the primary model used the reported binary collapse or distinct education categories. This changes which analysis specification accompanies extracted primary effects.

**Alternatives and missing definition:** eTable2 may describe a collapsed selection model and eTables3/4 may describe a separate final parameterization,but that change is not identified. Duplicate AA wording may refer to the college category; that wording observation is separately excluded because it is not the numerical issue.
**Exact human question:** Was education binary or multi-level in the fitted primary imputation and estimation models,and how does the final parameterization relate to the selection model?

### F-ST1-104

**Title:** Selected weighting covariates and the displayed fitted weight model do not match.

**Locations and document roles:** REPORT [DOC-005 p7,eTable2](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7),final nonresponse-weight model covariates; REPORT [DOC-005 p10,eTable5](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10),all fitted covariate rows; REPORT [DOC-005 pp5–6](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5),nonresponse selection/model description. S163,S214,S218,S219. Supporting REPORT workbook: [DOC-006](../../../../joi250046supp5_prod_1755300121.16087.xlsx),eTable 3!H12:J12,H18:J18,H39:I39,H81:I81,H84:I84,H108:I108.

**Printed statements/values:** eTable2 lists PEG,PHQ8,GAD7,any negative social determinant and education as additional weighting covariates. eTable5 displays PEG OR.96,PHQ8 .97,GAD7 .99,no negative social determinant1.34 and not employed1.49(1.11,2.00),P=.008; there is no education row. The printed base covariates in eTable2/pp5–6 do not include employment. Workbook unemployment H18<.001,I18=.0228 andJ18=.0591;education H12=.0156,J12=.05 andI12 blank.

**Rule and calculation:** The named final weighting model changes membership: education is selected in eTable2 but absent in its fitted model summary,while employment appears in the fit without appearing in that selected list or stated base set. This comparison requires no raw data. The blankI12 is not interpreted as a P value or proof of a failed selection test. Display rounding is not relevant.

**Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W. The workbook corroborates the unemployment selection criteria; it does not add a conflict relationship.
**Qualifying route:** Route B.
**Affected result or extracted value:** The nonresponse weights incorporated into the primary weighted MCID analysis,and the covariate list extracted as its model specification.
**Why context does not resolve it:** The printed selected list and fitted table are both presented as final model information. A reader cannot identify the actual weighting specification from their different membership.

**Alternatives and missing definition:** Education might be omitted from an otherwise incomplete coefficient summary,or eTable2 may describe another model stage. Employment might be carried into the weight model by an unstated additional rule. Neither is disclosed in the named final-list/fitted-model mapping.
**Exact human question:** Which exact covariates produced the nonresponse weights used in the primary analysis,and how should the eTable2 list be matched to eTable5?

### F-ST1-105

**Title:** One sensitivity NNT does not reproduce under the printed reciprocal definition and half-unit display rule.

**Locations and document roles:** REPORT [DOC-005 p14,eTable8](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14),Reminder Letters Added,6 months,PTvsUC;footnote d. S181,S216.

**Printed values:** PT35.6%,UC21.3%,NNT8(5,14). Footnote d defines NNT as one over the difference in adjusted improvement percentages.

**Rule and calculation:** Point reciprocal100/(35.6−21.3)=6.99300699. Percentage rounding bands[35.55,35.65] and[21.25,21.35] yield RD[14.20,14.40] percentage points and reciprocal[6.94444444,7.04225352]. Printed integer8 gives[7.5,8.5]. Interval gap=.45774648;relative gap=.45774648/8=.05721831>.05. The same reciprocal/display method reconciles the other44 sensitivity NNT cells under the zero-gap or≤.05 rule,as explicitly recorded in eachS row. For example,eTable8 Letters3 PT/UC100/(31.6−20.5)=9.0090 with printed9;Letters6 HC/PT100/(40.6−35.6)=20 with printed20.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.
**Qualifying route:** Route A, category 4.
**Affected result or extracted value:** PTvsUC6-month sensitivity NNT after reminder letters.
**Why context does not resolve it:** Under the required half-unit display rule,the displayed reciprocal result differs by more than.05 relative discrepancy. RouteA4 registers a row not reproduced by a method that reproduces the rest of the same display.

**Alternatives and missing definition:** A deliberate upward integer rounding convention could reconcile8 when the unrounded reciprocal lies just above7. This convention is supported by several other NNT cells;for example,eTable7 Complete3 PT/UC reciprocal12.195 is displayed13,and eTable8 Letters3 HC/UC reciprocal7.353 is displayed8. The supplied footnote does not state a ceiling convention. The independent inclusion screener must consider that source-supported alternative under the normative display rule; no correction is proposed.
**Exact human question:** Which NNT integer-rounding convention was used,and what unrounded adjusted risks and NNT underlie the printed8?

### F-ST1-106

**Title:** The workbook current-depression count and percentage do not reconcile with its stated missingness-adjusted denominator.

**Locations and document roles:** REPORT [DOC-006 workbook](../../../../joi250046supp5_prod_1755300121.16087.xlsx),worksheet eTable 3!E82,current depression in All Observed;comparator E3 population,E83 missing,andA110 denominator rule. S220.

**Printed values:** E82“711(73.2)”;E3“N=1568”;E83 missing2. A110 says missing observations are excluded from the percentage denominator.

**Rule and calculation:** Count denominator1568−2=1566.100×711/1566=45.40229885%,not73.2%. Conservative half-unit intervals on all displayed inputs: count[710.5,711.5],population[1567.5,1568.5],missing[1.5,2.5],denominator[1565,1567],recomputed percentage[45.34141672,45.46325879]. Printed percentage interval[73.15,73.25]. Gap27.68674121 percentage points;relative gap27.68674121/73.2=.37823417>.05. Integer counts taken as exact would make the discrepancy stronger.

**Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.
**Qualifying route:** Route A, category 3.
**Affected result or extracted value:** The prevalence of current depression among participants with all primary-outcome follow-ups observed.
**Why context does not resolve it:** RouteA3 applies to the count/percentage/denominator discrepancy in a single display.

**Alternatives and missing definition:** An unstated denominator around971 would yield73.2% for711,but the displayed All Observed population and missingness row provide1566. No separate analysis subset is identified.
**Exact human question:** Which denominator and percentage correspond to the printed711 current-depression participants in the All Observed group?

## Excluded observations

Each row is one apparent issue family; checks that reconcile are recorded only in the S inventory.

|Location|Observation|Reason code|
|---|---|---|
|REPORT DOC-005 p7 eTable1 observed-pattern counts|188+283+1568=2039 versus2036; implied observations5458 versus5449. Conservative half-unit gaps1/2036=.00049 and4.5/5449=.00083,within.05 scope rule.|ROUNDING_OR_DISPLAY_PRECISION|
|REPORT DOC-005 p8 eTable3 Time6M,SexMale,Age≥65,1+musculoskeletal conditions and interaction rows without a null/test conflict|Normal-Wald back-calculated P values can differ from exact printedP—for example Time6M diagnosticSE(.19−.07)/3.92=.03061,Z4.247 versusP.025. Exact test distribution,sidedness and variance mapping are not supplied; an exact-test mismatch is not established. The seven observable null/test conflicts are emitted asF-ST1-101.|CONDITIONAL_OR_UNREPORTED|
|REPORT DOC-005 pp8–9 eTables3–4 repeated AA education wording|Two education rows carry AA labels. Level ordering and other categories suggest a college label;wording alone is not registered. The conflicting binary versus multi-level model specification is separatelyF-ST1-103.|TERMINOLOGY_OR_WORDING|
|REPORT DOC-005 p11 eTable7 andp14 eTable8 NNT cells other thanF-ST1-105|Small reciprocal-versus-integer differences all have zero interval gap or relative gap≤.05;each of44 individual computations is retained in itsS record.|ROUNDING_OR_DISPLAY_PRECISION|
|REPORT DOC-005 p14 eTable8,before8/9/2021,listed3-month arm counts|149+153+152=454 randomized,while only366 have any follow-up. This comparison concerns a per-time-point contributor label and does not change the randomized analysis-population size or decision rule.|PERIPHERAL_COMPARISON|
|REPORT DOC-005 p15 eTable9 caption“adjusted relative risk” versus prose/footnote|Surrounding heading,paragraph and explicit footnote all identify GEE without adjustment,weighting or imputation. Analysis identity is immediately recoverable.|CONTEXT_RESOLVES|
|REPORT DOC-005 p16 eTable10 social/physical median differences versus mean contrasts|The group statistics are explicitly medians/IQRs,while the contrasts are GEE mean differences. Subtraction of medians is not a test of the stated mean-analysis identity.|CONDITIONAL_OR_UNREPORTED|

## Limitations and completion

All assigned relationship families are PASS_1_COMPLETE;pass2 is pending for a different fresh agent. No exact coefficient reference distribution,covariance matrix,degrees of freedom or sidedness is inferred. Diagnostic normal approximations cannot replace the reported analysis. Histograms have no exact printed bin heights. eTable11 is outside the amended shard and is assigned separately. No scientific gap remains in this shard. Inclusion screening remains independent;all emitted findings retain their source-grounded alternatives.

