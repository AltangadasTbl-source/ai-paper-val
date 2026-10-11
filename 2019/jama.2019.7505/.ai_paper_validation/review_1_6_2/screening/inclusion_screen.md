# Initial independent inclusion screen

Fresh runtime: 01a12968-bd54-7e42-add6-25f56ec40245. Model: gpt-6.1-sol. Reasoning effort: high. Scope: every finding in the finalized numeric, cross-source and statistical-pass-1 checker artifacts: 3 + 9 + 10 = 22 findings. The complete scope and review contract were read. Decisions use the supplied sources alone, without earlier audit conclusions, external evidence or an expected count. Candidate IDs were assigned by the coordinator after completion of this independent screen.

The independent screen yields 13 included issues, 6 duplicate findings and 3 other screened-out findings: TERMINOLOGY_OR_WORDING 1, OUT_OF_FOCUS 1, CONTEXT_RESOLVES 1. The DIC and per-protocol cardiopulmonary-edema interval/test conflicts remain separate: no source establishes one production cause, and the combined F-NUM-003 is preserved as provenance for both.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-NUM-003 | numeric_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C009 |
| F-XS-001 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C002 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-003 | cross_source_consistency_reviewer | initial | SCREENED_OUT | TERMINOLOGY_OR_WORDING | — |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-005 | cross_source_consistency_reviewer | initial | SCREENED_OUT | OUT_OF_FOCUS | — |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-XS-007 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C012 |
| F-XS-008 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-009 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-ST1-001 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C002 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-ST1-003 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-ST1-004 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-ST1-005 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-ST1-006 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-ST1-007 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-ST1-008 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C006 |
| F-ST1-009 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |
| F-ST1-010 | statistics_pass_1 | initial | SCREENED_OUT | CONTEXT_RESOLVES | — |

## One-sentence decision justifications

- **F-NUM-001:** Route B qualifies because source-described intervention risk ratios repeatedly reconstruct a different conditional-allocation contrast, with several half-unit discrepancies above .05 and no stated model or denominator mapping resolving the extracted outcome-risk estimand.
- **F-NUM-002:** Route A categories 1 and 2 qualify because the abstract hypoxemia upper limit is printed +6.1 rather than the matching table's −6.1, making the abstract interval contain zero despite P < .001, with a half-unit copy gap of 12.10 percentage points and relative discrepancy 1.98361.
- **F-NUM-003:** The DIC portion duplicates included F-ST1-005 and supplies its primary candidate target, while its separately preserved per-protocol edema portion duplicates included F-ST1-007 and must also be cross-referenced in that candidate's provenance.
- **F-XS-001:** This duplicates the included F-NUM-002 abstract hypoxemia sign/interval issue, and its additional main pp.10–11 interpretation locations are retained with that issue.
- **F-XS-002:** Route B qualifies because the exact primary collapsed-composite tuple is called RR in the main report and OR in eFigure 12, leaving the effect measure to extract unresolved despite identical numeric copies.
- **F-XS-003:** The results supplement's broad secondary heading does not say prespecified, so a nonprimary outcome can also be the explicitly post hoc five-day mortality outcome identified by the main report without establishing changed prespecification.
- **F-XS-004:** Route A category 5 qualifies because the original protocol secondary hierarchy and mortality window differ from the prospectively finalized SAP and report hierarchy, with the disclosed SAP revision retained as context rather than erasing the reproduced endpoint changes.
- **F-XS-005:** Fixed versus variable randomization blocks and an omitted restatement of ARISCAT balancing do not establish a change to any named quantitative result, analysis-population size, primary analysis, outcome or statistical decision rule in this package, and absence of ARISCAT analysis adjustment cannot be inferred from them.
- **F-XS-006:** Route A category 5 qualifies because the supplied protocol's mild/moderate primary-component definitions lack the report's explicit 2 L/min split, which changes component membership and the severe composite that excludes mild failure.
- **F-XS-007:** Route A category 5 qualifies because the protocol source image prints GCS ≤8 while the results supplement prints GCS <8 for the same coma component, changing its inclusion rule at score 8.
- **F-XS-008:** Route A category 5 qualifies because a primary time-to-PPC log-rank comparison is explicitly planned, whereas the complete supplied report identifies Cox outputs but no result identifiable as that planned comparison.
- **F-XS-009:** Route A category 5 qualifies because the SAP specifies a distinct clinical-severity-weighted primary-composite GEE and the supplied report identifies no weights or weighted result among its separately listed sensitivity models.
- **F-ST1-001:** This duplicates included F-NUM-002 and retains both the interval/P incompatibility and signed-limit comparison.
- **F-ST1-002:** Route A category 1 qualifies because three printed Table 2 intervals include zero while their accompanying two-sided P values are significant, irrespective of possible unrounded endpoints or distinct procedures.
- **F-ST1-003:** Route A category 2 and independently Route B qualify because monitoring/reversal percentages imply contrasts that differ beyond half-unit precision from their displayed absolute differences, including a reversed reversal direction, while the printed fractions support a different reading.
- **F-ST1-004:** This duplicates included F-NUM-001's repeated conditional-allocation versus outcome-risk estimand issue and adds its complete subgroup and component correspondence records.
- **F-ST1-005:** Route A category 1 qualifies because DIC RR 2.00 (1.91–2.09) excludes one while its accompanying P > .99 is nonsignificant, with the named interval/test distinction retained as an alternative rather than a screen-out.
- **F-ST1-006:** Route A category 4 qualifies because mortality RR 1.41 (.95–1.81) does not reproduce the same-display log-interval relation that reproduces neighboring ratio rows, leaving a relative lower-limit discrepancy .13960 after half-unit precision.
- **F-ST1-007:** Route A category 1 qualifies because per-protocol cardiopulmonary edema effect 1.36 (1.02–1.82) excludes the ratio null one while P = .09 is nonsignificant, preserving the generic effect heading and interval/test definition question.
- **F-ST1-008:** This duplicates included F-XS-009's distinct planned clinical-severity-weighted primary analysis without an identifiable reported counterpart.
- **F-ST1-009:** This duplicates included F-XS-002's primary collapsed-composite RR/OR identity issue and does not merge it with the conditional-allocation arithmetic issue.
- **F-ST1-010:** The main outcome paragraph supplies duration conditions and the detailed table notes supply the baseline-dependent deterioration clauses, while the supplement abbreviates these same outcomes without asserting a competing duration or analyzed population, so the descriptions can be read cumulatively at once.

## Source rereading and reproduction

Fresh direct-source Poppler pdftotext 26.01.0 layout extractions were made on the CPU in `preprocessing/inclusion_initial/`; commands and every derivative are recorded in [the extraction engine manifest](../preprocessing/inclusion_initial/engine_manifest.md). Exact supplied main source pp.1–4,7–11; protocol pp.5,12,13,19,31,32; all amendment and SAP pages; results pp.20,21,29,30,38,41,42 were reread for decisions. Complete main and results native/layout extraction searches independently checked reported counterparts for log-rank, clinical weighting and the original endpoint list. Source-page images were also inspected for main pp.1,7,8,9, protocol p.32 and results pp.29,42; the protocol's ≤8 underline and the figure's OR header require that visual authority. The reused PNG rendering engines are historically unrecorded, and all images are immutable supplied-source derivatives.

No direct-source unit is omitted from the assigned finding scope. Image-only forest text was read visually rather than assumed absent from extraction. No raw participant data or analysis code are available, so response/model provenance and actual patient recategorization are human questions, not demonstrated mechanisms. All three screened-out findings were independently reread, including the main randomization paragraph, protocol randomization statements, SAP timing and original duration/baseline-dependent definitions.

## Registration handoff: one issue per group

These groups are descriptive handoff labels, not candidate IDs. The coordinator assigns stable IDs in source order. Every group remains **Pending Human Adjudication**. Each classification below is provisional for the required source recheck. Protocol/SAP locations that only corroborate an internal report issue do not add P_R.

### Repeated outcome-risk estimand identity

**Included anchor:** F-NUM-001. **Duplicate provenance:** F-ST1-004. **Route:** B. **Domain:** statistical_results. **Primary/all relationships:** S_W / S_W; the same within-display pattern recurs in more than one REPORT, rather than two reports printing opposing versions of one matched result. **Roles:** all conflicting labels, counts and estimates REPORT; PLAN SAP only corroborates the intended event-incidence terminology.

**Complete source locations:** [main abstract p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), [main binary methods p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), [primary/mild/pleural narrative p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), [all Table 3 binary rows p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), [continued Table 3, notes and complete Figure 2 p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), [per-protocol eTable 8 p.29](../../../joi190055supp4_prod_16092.pdf#page=29), [all component rows eFigure 12 p.42](../../../joi190055supp4_prod_16092.pdf#page=42). Preserve all row occurrences in [the complete numeric diagnostic table](../checkers/numeric_consistency.md) and [the complete 57-row statistical diagnostic](../statistics/effect_measure_diagnostics.md), rather than reducing this issue to three examples.

**Affected rows:** S054,S055,S056,S057,S058,S059,S060,S061,S062,S063,S064,S065,S066,S067,S068,S069,S070,S071,S072,S073,S075,S077,S078,S079,S080,S082,S083,S085,S086,S087,S088,S089,S090; all subgroups S092,S093,S094,S095,S096,S097,S098,S099,both S100 rows,S101; per-protocol S344,S345,S346,S347,S348,S349,S350,S351,S352,S353,S354,S355,S356; component repeats S373,S374,S375,S376,S377,S378,S379,S380,S381,S382,S383,S384. Rows with relative discrepancies at most .05 are supporting occurrences, never independent qualifying numeric discrepancies. The zero-control DIC crude ratio is undefined and is not assigned a fabricated finite value. The collapsed-composite OR heading is a separate issue below.

**Reproduction:** For high/low counts a,b and totals H,L, outcome-risk contrast is (a/H)/(b/L); the diagnostic [a/(a+b)]/[(H−a)/(H+L−a−b)] conditions on event status and reconstructs many printed effects. Independently recomputed pleural outcome-risk interval [1.97075,2.11980] versus printed [1.345,1.355] leaves relative gap .45611; hypoxemia [.35950,.37041] versus [.505,.515] leaves .26390; hypotension [1.82729,1.84769] versus [1.425,1.435] leaves .27433. The conditional diagnostics are 1.35795, .51074, 1.43123 respectively. Both formulas condition on different variables. No computational provenance is attributed.

**Alternatives/context:** A source-unidentified marginal/adjusted estimator, transformation or denominator orientation could differ from crude risks; explicitly modeled subgroup/component and GEE quantities are not forced to equal crude estimates. The issue is the systematic source-supported identity pattern and the absent mapping of the stated outcome-risk quantity to those displayed values. **Human question:** Which response variable, model, arm/reference orientation, conditioning variable and denominator define each displayed binary effect and interval?

### Abstract hypoxemia signed confidence limit

**Included anchor:** F-NUM-002. **Duplicate provenance:** F-XS-001,F-ST1-001. **Route:** A1 and A2. **Domain:** statistical_results. **Primary/all relationships:** S_W / S_W. **Roles:** REPORT main abstract [p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1) versus REPORT Table 3 [p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), with REPORT interpretation [p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) and [p.11](../../../jama_bluth_2019_oi_190055_16092.pdf#page=11) retained. **Relationship:** S085.

The matched −8.6% hypoxemia difference prints abstract 95% CI −11.1 to +6.1 with P < .001, while the table prints −11.1 to −6.1 with the same P and outcome proportions 5.0%/13.6%. Printed upper-limit intervals [6.05,6.15] versus [−6.15,−6.05] leave gap 12.10 percentage points, relative 1.98361; the abstract interval/test conflict has no rounding screen-out. The body supports the negative upper limit as an alternative, but does not erase the abstract's extraction reading. **Human question:** Which signed upper confidence limit and corresponding analysis belong to the abstract hypoxemia result?

### Primary collapsed-composite RR/OR identity

**Included anchor:** F-XS-002. **Duplicate provenance:** F-ST1-009. **Route:** B. **Domain:** statistical_results. **Primary/all relationships:** S_C / S_C. **Roles:** REPORT main [abstract p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), [analysis p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), [Table 3 p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), [Figure 2 p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) versus REPORT [eFigure 12 p.42](../../../joi190055supp4_prod_16092.pdf#page=42); PLAN [SAP p.2](../../../joi190055supp3_prod_16092.pdf#page=2) merely corroborates RR. **Relationships:** S054,S101,S108,S385.

The exact .93 (.83–1.04) tuple is an RR in the article and is under the OR global heading in the figure. Copy intervals overlap (gap zero), so the issue concerns quantity identity rather than rounding. Other OR-based models make both readings plausible, and no separate collapsed OR model or row-specific heading exception identifies the correct extraction measure. **Human question:** Is the eFigure 12 collapsed row the article's RR, or a separately defined OR analysis?

### Original secondary hierarchy and mortality follow-up

**Included anchor:** F-XS-004. **Route:** A5. **Domain:** protocol_report. **Primary/all relationships:** P_R / P_R, P_P. **Roles/locations:** PLAN [protocol synopsis p.5](../../../joi190055supp1_prod_16092.pdf#page=5) and [secondary endpoints p.12](../../../joi190055supp1_prod_16092.pdf#page=12) versus PLAN [updated SAP p.1](../../../joi190055supp3_prod_16092.pdf#page=1) and REPORT [main secondary list p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), [results definitions p.21](../../../joi190055supp4_prod_16092.pdf#page=21); retain PLAN amendment [p.1](../../../joi190055supp2_prod_16092.pdf#page=1), [p.2](../../../joi190055supp2_prod_16092.pdf#page=2), [p.3](../../../joi190055supp2_prod_16092.pdf#page=3).

The protocol lists standalone postoperative invasive/noninvasive ventilation, 30-day hospital readmission and 90-day mortality; the final SAP/report list severe PPC and in-hospital mortality instead and do not identify those original standalone endpoints. Severe respiratory failure includes ventilation but is not that same standalone outcome; in-hospital death is not 90-day death. Preserve the SAP's explicit January 20, 2018 finalization and endorsement before last inclusion/database lock/analysis, and the main article's identification of this final SAP. This may document prospective supersession; the finding does not assert an undisclosed revision or noncompliance. **Human question:** What status, supersession and reporting location apply to each original endpoint and mortality window?

### Mild/moderate respiratory-failure flow boundary

**Included anchor:** F-XS-006. **Route:** A5. **Domain:** protocol_report. **Primary/all relationships:** P_R / P_R. **Roles/locations:** PLAN [protocol pulmonary components p.31](../../../joi190055supp1_prod_16092.pdf#page=31) versus REPORT [Table 3 note d p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), REPORT [component definitions p.20](../../../joi190055supp4_prod_16092.pdf#page=20); PLAN [SAP severe composite p.1](../../../joi190055supp3_prod_16092.pdf#page=1) gives context.

Protocol mild failure responds to supplemental oxygen without a flow boundary and moderate persists despite it; main mild responds to ≤2 L/min and moderate responds only to >2 L/min. Results eMethods prints =2 L/min for mild and >2 for moderate. Keep the report's =2/≤2 shorthand as documentary context, not a second issue. The 2 L boundary changes mild/moderate membership and the severe PPC composite that excludes mild; relevant counts are 135/154 mild, 42/58 moderate and 116/134 severe composite. No claim is made that any individual was recategorized. **Human question:** Which operational oxygen-flow classification was used, and was the stated boundary an approved clarification or revision?

### Coma score inclusion threshold

**Included anchor:** F-XS-007. **Route:** A5. **Domain:** protocol_report. **Primary/all relationships:** P_R / P_R. **Roles/locations:** PLAN [protocol extrapulmonary definition p.32](../../../joi190055supp1_prod_16092.pdf#page=32) versus REPORT [results extrapulmonary definition p.21](../../../joi190055supp4_prod_16092.pdf#page=21), with REPORT [Table 3 coma/composite p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9).

The protocol visual source prints GCS ≤8, whereas results definitions print <8 under the same sedation/therapeutic-coma exclusions. Native extraction drops the underline, and that derivative does not override the visual source. Score 8 therefore falls on different sides of the printed eligibility rule; affected readings concern coma 2/2 and extrapulmonary composite 167/150. Whether any participant actually had score 8 is unavailable and not assumed. **Human question:** Was GCS 8 included in the operational coma component used for the reported counts?

### Planned primary log-rank output

**Included anchor:** F-XS-008. **Route:** A5. **Domain:** protocol_report. **Primary/all relationships:** P_R / P_R. **Roles/locations:** PLAN [SAP primary time-to-event analysis p.2](../../../joi190055supp3_prod_16092.pdf#page=2) versus REPORT [main analysis p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), [eFigure 8 p.38](../../../joi190055supp4_prod_16092.pdf#page=38); additional inspected REPORT [eTable 9 p.30](../../../joi190055supp4_prod_16092.pdf#page=30), [eFigure 12 p.42](../../../joi190055supp4_prod_16092.pdf#page=42), [main p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), [main p.11](../../../jama_bluth_2019_oi_190055_16092.pdf#page=11) and PLAN [SAP p.3](../../../joi190055supp3_prod_16092.pdf#page=3) remain negative-search context rather than another issue.

SAP explicitly plans Kaplan–Meier curves compared by log-rank; the article identifies Cox models and the figure prints HR .88 (.73–1.06), P = .190 without identifying the planned test. Complete supplied report extraction and image-only sensitivity displays identify no log-rank counterpart. This records an unidentifiable reported planned primary output, without asserting that the test was not performed. The displayed P could be log-rank despite the Cox discussion, or the comparison may have been replaced or omitted; preserve all alternatives. **Human question:** Which displayed output, if any, is the planned log-rank test, and what replacement or omission applies?

### Planned primary clinical-severity-weighted GEE

**Included anchor:** F-XS-009. **Duplicate provenance:** F-ST1-008. **Route:** A5. **Domain:** protocol_report. **Primary/all relationships:** P_R / P_R. **Roles/locations:** PLAN [SAP clinical severity weight p.3](../../../joi190055supp3_prod_16092.pdf#page=3) versus REPORT [main sensitivity methods p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), [discussion p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), [additional analysis p.11](../../../jama_bluth_2019_oi_190055_16092.pdf#page=11), [eTable 9 p.30](../../../joi190055supp4_prod_16092.pdf#page=30), [eFigure 12 p.42](../../../joi190055supp4_prod_16092.pdf#page=42). **Relationships:** S110,S123,S318 with all reported sensitivity comparators S357,S358,S359,S360,S361,S373,S374,S375,S376,S377,S378,S379,S380,S381,S382,S383,S384,S385,S386,S387,S388 retained.

SAP separately specifies a posteriori clinical component weights and a common-effect GEE applying them; the report gives site-random, count, common-effect, heterogeneity and average-effect outputs but identifies no clinical weights or weighted counterpart. The common-effect footnote says one effect across 12 components without identifying weights. A reported unlabelled row might contain the weighted result, or the analysis may have been performed without display or omitted; no such explanation is assumed. The weighted GEE and log-rank analyses are independent specifications and remain separate. **Human question:** Where is the planned weighted result, and what component weights or omission apply?

### Table 2 null-endpoint/significant-P pattern

**Included anchor:** F-ST1-002. **Route:** A1. **Domain:** statistical_results. **Primary/all relationships:** S_W / S_W. **Roles/locations:** REPORT [Table 2 p.7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7) and REPORT [two-sided significance p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4). **Relationships:** S002,S003,S016.

All three occurrences are retained: tidal volume first hour .1 (0–.2), P = .007; tidal volume last hour .1 (0–.2), P = .008; respiratory rate last hour −.4 (−.7–0), P = .02. Each printed 95% interval includes zero and the printed test is significant at .05. This is one shared zero-endpoint display pattern, distinct from the binary sparse-event intervals. Unrounded endpoints could exclude zero or different methods could generate interval/test results; category A1 specifically prevents removing the issue through either explanation. **Human question:** What unrounded endpoints and interval/test procedures apply to each of the three comparisons?

### Monitoring/reversal displayed percentage contrasts

**Included anchor:** F-ST1-003. **Route:** A2 and B. **Domain:** statistical_results. **Primary/all relationships:** S_W / S_W. **Roles/location:** REPORT [Table 2 p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8). **Relationships:** S038,S039.

Monitoring prints 632/982 (64.9%) versus 651/984 (67.7%), difference −1.8%; reversal 724/982 (74.3%) versus 723/984 (75.2%), difference +.2%. Percentage half-unit intervals imply monitoring contrast [−2.90,−2.70] versus printed [−1.85,−1.75], gap .85/1.8 = .47222; reversal [−1.00,−.80] versus [.15,.25], gap .95/.2 = 4.75 with reversed direction. Exact fractions imply −1.80008% and +.25148%, respectively, supporting the displayed-difference reading. Individual fraction/percentage differences are below .05 and are not registered separately; it is the explicit contrast conflict that qualifies. The percentages resemble preceding blockade denominators 974/961 but that is a diagnostic alternative, not an assigned denominator. **Human question:** Which denominator applies to each percentage, and what exact population contrast does the difference column represent?

### DIC interval/test compatibility

**Included anchor:** F-ST1-005. **Duplicate provenance:** primary portion of F-NUM-003. **Route:** A1. **Domain:** statistical_results. **Primary/all relationships:** S_W / S_W. **Roles/locations:** REPORT [Table 3 DIC p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), [notes b/c p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10). **Relationship:** S080.

DIC counts 1/989 versus 0/987 accompany RR 2.00 (95% CI 1.91–2.09), P > .99; its RD .1 (−.1–.3) contains zero. The RR interval excludes one and the P is nonsignificant at .05. Lower-limit rounding interval [1.905,1.915] remains above one, but A1 does not use rounding exclusions. Preserve named Wald interval versus χ² test, sparse cells and unspecified zero-cell interval handling. This compatibility rule is independent of the repeated point-estimand identity issue. **Human question:** What ratio interval and zero-cell procedure generated 1.91–2.09, and how should its null exclusion be interpreted alongside P > .99?

### Mortality same-display interval relation

**Included anchor:** F-ST1-006. **Route:** A4. **Domain:** statistical_results. **Primary/all relationships:** S_W / S_W. **Roles/locations:** REPORT [Table 3 mortality and comparator rows p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), REPORT [interval note and vasoactive comparator p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10). **Relationship:** S088.

Mortality 12/989 versus 5/987 prints RR 1.41 (.95–1.81), P = .09. Neighboring pleural 1.35 (1.14–1.62), hypoxemia .51 (.40–.65), bradycardia 1.27 (1.11–1.45) and vasoactive 1.10 (1.01–1.21) reproduce log symmetry within the scope's precision tolerance. For a log-symmetric ratio interval, point² = lower × upper; mortality point [1.405,1.415] and upper [1.805,1.815] imply lower [1.08762,1.10927], whereas its printed lower is [.945,.955], gap .13262/.95 = .13960. This reproduction uses the same-display algebra, not assumed variance or crude event risks. A mortality-specific asymmetric procedure could explain the tuple, but the common footnote does not identify such an exception. **Human question:** What mortality-specific interval construction accounts for .95–1.81 around 1.41?

### Per-protocol cardiopulmonary-edema interval/test compatibility

**Included anchor:** F-ST1-007. **Duplicate provenance:** secondary portion of F-NUM-003, whose table row names the DIC candidate as its scalar primary target. **Route:** A1. **Domain:** statistical_results. **Primary/all relationships:** S_W / S_W. **Roles/locations:** REPORT [eTable 8 p.29](../../../joi190055supp4_prod_16092.pdf#page=29); REPORT [main binary/PP methods p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4) supplies ratio-analysis context rather than an opposing result. **Relationship:** S355.

Per-protocol 15/917 (1.6%) versus 7/912 (.8%) accompanies effect 1.36 (95% CI 1.02–1.82), P = .09. The table's literal heading is Effect Estimate, not an inserted RR label; the matching binary analysis context supplies the ratio null one. Lower-limit interval [1.015,1.025] remains above one, whereas the test is nonsignificant at .05; A1 independently qualifies. Different interval/test procedures and the missing row-specific effect definition remain alternatives. This sparse-event result is not merged with DIC merely because both violate interval/test compatibility. **Human question:** What measure and interval/test methods generated the PP edema tuple, and how should the opposed null-inclusion readings be interpreted?

## Screened-out source context retained

For **F-XS-003**, [main p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3) and [Table 3 p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) explicitly call five-day mortality post hoc; [results p.21](../../../joi190055supp4_prod_16092.pdf#page=21) includes it in a secondary list but never calls it prespecified; [SAP p.1](../../../joi190055supp3_prod_16092.pdf#page=1) lists only in-hospital mortality. [eFigure 11 p.41](../../../joi190055supp4_prod_16092.pdf#page=41) repeats HR 1.67 (.40–6.97), P .484, whose precision overlaps main .48. The heading does not reproduce a changed planned endpoint status.

For **F-XS-005**, [protocol pp.12](../../../joi190055supp1_prod_16092.pdf#page=12) and [13](../../../joi190055supp1_prod_16092.pdf#page=13) give site balance, ARISCAT risk accounting and block length 6; [main p.2](../../../jama_bluth_2019_oi_190055_16092.pdf#page=2) gives blocks 4,6,8 and site stratification. These descriptions differ, but both keep individual 1:1 randomization; the [amendment overview](../../../joi190055supp2_prod_16092.pdf#page=1) and [final SAP](../../../joi190055supp3_prod_16092.pdf#page=1) supply no result that requires a different block rule. Treating risk accounting as a required omitted covariate or changing site-only adjustment would add an unstated analytic premise. No primary/key-secondary extraction value, analysis-population size or statistical decision rule is changed by the reproduced block-size description alone.

For **F-ST1-010**, [main p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1) and [p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3) supply >1-minute hypoxemia and >2-minute hypotension duration; [table notes p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) add >5% SpO2 and >10 mm Hg systolic declines conditional on previously low values; [results p.21](../../../joi190055supp4_prod_16092.pdf#page=21) summarizes the same low-value thresholds. [Protocol p.12](../../../joi190055supp1_prod_16092.pdf#page=12) preserves durations and [p.19](../../../joi190055supp1_prod_16092.pdf#page=19) identifies the conditional rules as new complications in patients already below the threshold before recruitment. The cumulative reading supplies duration plus baseline-dependent detail; no location states that duration was discarded, or assigns the printed 49/134 or 313/170 results to a differently defined analysis. An absence of a single repeated combined sentence alone is not a conflicting result.

## Limitations

No raw data or analytic code were supplied. Exact model, link, variance and sparse-cell constructions remain unavailable where named in the handoff; none is silently inferred. Unlabelled figure endpoints cannot establish precise extra values. Historical reused-PNG engine provenance is unrecorded. Every assigned finding and every cited decisive source location was screened; there is no coverage limitation for these 22 findings. No supplied source or reusable asset was changed.

## Coordinator registration cross-reference

Included issue IDs in source order: C001 RR/OR identity; C002 abstract interval sign; C003 original secondary hierarchy; C004 outcome-risk estimand identity; C005 log-rank output; C006 weighted GEE; C007 Table 2 zero endpoints; C008 percentage contrasts; C009 DIC interval/test; C010 mortality interval relation; C011 oxygen-flow boundary; C012 coma threshold; C013 PP edema interval/test. F-NUM-003 has primary duplicate target C009 and separately retained secondary provenance for C013. Neither portion is suppressed or merged with the other. Complete source-linked handoff above remains unchanged.
