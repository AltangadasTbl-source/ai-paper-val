# Candidate Ledger — Workflow 1.6.2

Pending Human Adjudication. Five included issues were registered after the independent screen; no assigned ID is deleted. Source order follows first relevant REPORT passage: main p. 4 Outcomes, then its KM/Cox, logistic and subgroup methods, followed by supplementary eTable 2 p. 4. Duplicate checker findings remain preserved as provenance; Finding IDs lists INCLUDE rows only.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN protocol p. 30 vs REPORT main article pp. 1, 4, 8 | reproduced | CONFIRMED | F-ST1-006 |
| C002 | protocol_report | P_R | P_R | PLAN protocol pp. 33–34 vs REPORT main article pp. 1, 4, 6–8 and results supplement pp. 1–9 | reproduced | CONFIRMED | F-XS-002 |
| C003 | protocol_report | P_R | P_R | PLAN protocol p. 33 vs REPORT main article pp. 4, 7 | reproduced | CONFIRMED | F-XS-001 |
| C004 | protocol_report | P_R | P_R | PLAN protocol p. 34 vs REPORT main article pp. 4, 7–8 and results supplement pp. 1, 3–7 | reproduced | CONFIRMED | F-XS-003 |
| C005 | statistical_results | S_W | S_W | REPORT results supplement p. 4 count and denominator vs percentage in the same display | reproduced | CONFIRMED | F-NUM-001 |

## C001 — Reported respiratory-failure definition omits planned tachypnea duration

**Status:** Pending Human Adjudication

**Finding IDs:** F-ST1-006

**Consolidated duplicate provenance:** None

**Qualifying route:** Route B

**Classification rationale:** The inconsistency compares prospective PLAN specifications with REPORT methods or results; P_R governs, and the domain is protocol_report.

**Classification ambiguity:** No separately supplied SAP or amendment establishes whether a changed or distinct analysis was documented; classification is based on supplied content.

### F-ST1-006

**Title:** The reported respiratory-failure definition omits the planned two-hour tachypnea requirement.

**Relationships:** S206, S007. **Compared locations and roles:** PLAN [protocol p30, acute respiratory failure definition](../../joi190108supp1_prod.pdf#page=30); REPORT [main p4, postextubation respiratory failure definition](../../jama_thille_2019_oi_190108.pdf#page=4) and [Table2 p8](../../jama_thille_2019_oi_190108.pdf#page=8).

**Printed statements:** Protocol ARF requires at least2 criteria, one being respiratory rate>25breaths/min “during at least2hours.” The report defines postextubation respiratory failure by at least2 criteria and lists respiratory rate>25breaths/min, without duration. Its day7 failure result is88/302 versus70/339, difference−8.5 (95% CI−15.2 to−1.8), P=.01.

**Rule and reproduced comparison:** A duration condition is part of the planned threshold/window used to classify a key secondary endpoint, but the reported explicit endpoint definition omits it. A qualifying tachypnea period shorter than2hours can meet the reported criterion and not the printed planned criterion. This is a logical definition comparison; no numeric rounding arithmetic applies.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; all relationships P_R.
**Qualifying route:** Route B.
**Affected result or extracted value:** The day7 postextubation respiratory-failure event counts and endpoint definition highlighted in the abstract.
**Why context does not resolve it:** The report presents a complete explicit criterion list but provides no pointer retaining a minimum tachypnea duration. A reader cannot tell which duration governed the reported counts.
**Alternatives and missing definition:** The2hour rule may have been applied but omitted from the condensed report, or changed by amendment. The source does not identify which.
**Human question:** Did the day7 respiratory-failure counts require tachypnea persisting at least2hours as specified in the protocol?


## C002 — Planned primary and key mortality Cox results are not reported

**Status:** Pending Human Adjudication

**Finding IDs:** F-XS-002

**Consolidated duplicate provenance:** F-ST1-002

**Qualifying route:** Route A, category 5

**Classification rationale:** The inconsistency compares prospective PLAN specifications with REPORT methods or results; P_R governs, and the domain is protocol_report.

**Classification ambiguity:** No separately supplied SAP or amendment establishes whether a changed or distinct analysis was documented; classification is based on supplied content.

### F-XS-002 — Prespecified Cox-analysis results are absent from the supplied report package

- **Compared locations and document roles:** PLAN [protocol p. 33, section 6.2 primary analysis](../../joi190108supp1_prod.pdf#page=33) and PLAN [protocol p. 34, mortality analysis](../../joi190108supp1_prod.pdf#page=34); REPORT [main p. 4 methods](../../jama_thille_2019_oi_190108.pdf#page=4), REPORT [main pp. 6–7 results](../../jama_thille_2019_oi_190108.pdf#page=6), REPORT [main p. 8 Table 2](../../jama_thille_2019_oi_190108.pdf#page=8), and REPORT [supplement pp. 1–9, full results package](../../joi190108supp2_prod.pdf#page=1), particularly [survival p. 9](../../joi190108supp2_prod.pdf#page=9).
- **Printed statements:** Primary protocol section 6.2 explicitly prescribes Cox regression with P<.20 outcome-associated-variable screening and backward selection, reporting adjusted relative risk and HR with 95% CI. Mortality section similarly prescribes univariate Cox screening followed by backward Cox modeling. Main reports primary chi-square, Kaplan–Meier/log-rank and an adjusted logistic OR, and ICU mortality risk difference −2.4 (−6.7 to 1.7), P=.25. The complete report and supplement contain no Cox HR, adjusted relative risk or accompanying Cox-model result.
- **Comparison logic:** Complete main/supplement mapping and source-linked text search for Cox/hazard confirm absence, not a missing table pointer. Kaplan–Meier/log-rank and logistic OR do not supply the specified adjusted time-to-event estimates. One finding consolidates the repeated absence of the planned Cox-model reporting for primary reintubation and mortality, including abstract-key ICU mortality.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationship type / all relationships:** P_R / P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Prespecified primary reintubation time-to-event analysis and key secondary ICU-mortality analysis; their planned adjusted HR/relative-risk estimates are unavailable for extraction.
- **Why context does not resolve it:** Category 5 expressly includes a planned primary or key secondary analysis that is not reported. This is a positively specified planned analysis, not a conjecture about an unreported detail.
- **Supported alternatives / missing definition:** The plan may describe prognostic predictor modeling separate from treatment-effect modeling; no treatment HR is inferred or demanded. Those specified outcome analyses could have been performed but left out, or superseded by an unsupplied amendment/SAP. This finding makes no assertion that analyses were not performed.
- **Display precision:** Logical reporting absence; no rounded estimate comparison or diagnostic estimate is used.
- **Exact human question:** Where are the Cox analyses and adjusted HR/relative-risk results prescribed for primary reintubation and ICU mortality, or the documentation explaining their replacement or nonreporting?


## C003 — Primary logistic covariate-selection specifications differ

**Status:** Pending Human Adjudication

**Finding IDs:** F-XS-001

**Consolidated duplicate provenance:** F-ST1-001

**Qualifying route:** Route A, category 5

**Classification rationale:** The inconsistency compares prospective PLAN specifications with REPORT methods or results; P_R governs, and the domain is protocol_report.

**Classification ambiguity:** No separately supplied SAP or amendment establishes whether a changed or distinct analysis was documented; classification is based on supplied content.

### F-XS-001 — Primary adjusted-model specification differs from the supplied plan

- **Compared locations and document roles:** PLAN [protocol p. 33, section 6.2](../../joi190108supp1_prod.pdf#page=33); REPORT [main p. 4, Statistical Analysis](../../jama_thille_2019_oi_190108.pdf#page=4); REPORT [main p. 7, adjusted primary result](../../jama_thille_2019_oi_190108.pdf#page=7).
- **Printed statements:** The plan specifies multivariate logistic regression after testing interactions, a maximal model containing variables associated with the dependent outcome at P<.20 plus literature-relevant forced variables, then backward elimination retaining outcome-associated P<.05 and forced variables. The report says all analyses followed a predefined SAP, but specifies adjustment on PaCO2 and potential baseline-unbalanced variables, defining imbalance as P<.05; chronic lung disease is the sole added variable. Its adjusted primary OR is 0.60 (95% CI 0.38–0.93), P=.02.
- **Comparison logic:** Association with reintubation and imbalance between treatment groups are different selection conditions. The published selection rule is absent from the supplied plan; the plan's outcome-based selection/backward elimination is not described as producing the printed adjusted OR. The model family alone being logistic does not reconcile the covariate rule.
- **Focus area:** D, planned versus reported statistical design.
- **Proposed review domain:** protocol_report.
- **Proposed relationship type / all relationships:** P_R / P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Adjusted day-7 reintubation OR 0.60 (0.38–0.93) and its designation as a predefined analysis.
- **Why context does not resolve it:** Category 5 applies to an analysis described as predefined whose stated specification is not contained in the supplied plan. The report gives the final covariates but no supplied amendment or alternative SAP reconciles the selection rules.
- **Supported alternatives / missing definition:** A separate predefined SAP or amendment, not supplied here, may have specified the report model. Alternatively the planned predictor-model exercise and the report's treatment-adjustment exercise may have been distinct analyses; the report does not supply the planned exercise or identify that separation. No claim is made about which model should be used.
- **Display precision:** Not a disagreement between rounded copies of one numeric result; the discrepancy is between logical covariate-selection rules. No recomputed estimate is asserted.
- **Exact human question:** Which supplied prespecified specification or documented amendment governs the covariate-selection rule for the adjusted day-7 reintubation OR, and how does it relate to protocol section 6.2?


## C004 — Two planned primary-outcome subgroup families are not reported

**Status:** Pending Human Adjudication

**Finding IDs:** F-XS-003

**Consolidated duplicate provenance:** F-ST1-003

**Qualifying route:** Route A, category 5

**Classification rationale:** The inconsistency compares prospective PLAN specifications with REPORT methods or results; P_R governs, and the domain is protocol_report.

**Classification ambiguity:** No separately supplied SAP or amendment establishes whether a changed or distinct analysis was documented; classification is based on supplied content.

### F-XS-003 — Prespecified non-PaCO2 primary-outcome subgroup analyses are not reported

- **Compared locations and document roles:** PLAN [protocol p. 34, section 6.4](../../joi190108supp1_prod.pdf#page=34); REPORT [main p. 4 subgroup methods](../../jama_thille_2019_oi_190108.pdf#page=4), REPORT [main p. 7 subgroup results](../../jama_thille_2019_oi_190108.pdf#page=7), REPORT [main p. 8 Figure 3](../../jama_thille_2019_oi_190108.pdf#page=8), REPORT [supplement p. 1 index](../../joi190108supp2_prod.pdf#page=1) and REPORT [supplement pp. 3–7 subgroup displays](../../joi190108supp2_prod.pdf#page=3).
- **Printed statements:** Protocol says subgroup analyses will be performed for main and secondary criteria in hypercapnic/nonhypercapnic patients, and additionally in patients with underlying cardiac or respiratory disease and according to the weaning test (T-piece versus minimal pressure support). Main reports a PaCO2 interaction P=.25, primary subgroup contrasts and Figure 3; supplement eTables 2–4 are exclusively PaCO2 subgroup baseline/outcome displays. No primary-outcome contrast by underlying cardiac/respiratory disease or by weaning-test type appears in the full supplied package.
- **Comparison logic:** The three planned subgroup families were compared individually with every report display. The PaCO2 family is present; the other two families' primary-outcome analyses are absent. Overall chronic lung disease adjustment and baseline T-piece/PS counts are different analyses and cannot substitute for these subgroup outcome analyses. Repeated absence across the two subgroup families is consolidated.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationship type / all relationships:** P_R / P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Prespecified day-7 reintubation contrasts within chronic cardiac/respiratory-disease and weaning-test subgroups.
- **Why context does not resolve it:** Category 5 includes a planned primary-outcome analysis not reported; the plan explicitly commits to these analyses. The report neither presents them nor explains an amendment.
- **Supported alternatives / missing definition:** They may have been performed but omitted, or removed through an unsupplied amendment/SAP. The chronic-disease groups may overlap; that does not explain absence of the specified analyses. No preferred subgroup analysis is proposed.
- **Display precision:** Reporting absence, not a comparison of rounded values.
- **Exact human question:** Where are the prespecified primary-outcome analyses by underlying cardiac/respiratory disease and by T-piece versus minimal pressure-support weaning test, or the documented reason for their nonreporting?


## C005 — Four hypercapnic cough and secretion percentages do not reconcile

**Status:** Pending Human Adjudication

**Finding IDs:** F-NUM-001

**Consolidated duplicate provenance:** F-ST1-007

**Qualifying route:** Route A, category 3

**Classification rationale:** All conflicting counts, denominators and percentages are in one REPORT table; corroborating main-table values do not create another relationship. S_W governs, and the domain is statistical_results.

**Classification ambiguity:** None

### F-NUM-001

**Title:** Four hypercapnic cough and secretion percentages do not reconcile with their explicit numerators and denominators.

**Locations and roles:** REPORT [joi190108supp2_prod.pdf, PDF p.4, eTable2](../../joi190108supp2_prod.pdf#page=4), final two rows, the two hypercapnic columns (HFNC alone and HFNC with NIV). All compared quantities occur within this single display. N203 tracks the relationship. REPORT [main Table1 PDF p.6](../../jama_thille_2019_oi_190108.pdf#page=6) corroborates aggregate counts and denominators but does not create the inconsistency or an additional cross-document relationship.

**Printed inputs:** Ineffective cough, No./total No.(%): hypercapnic HFNC alone14/45(69), HFNC with NIV16/59(73). Abundant secretions, No./total No.(%): hypercapnic HFNC alone20/46(57), HFNC with NIV23/61(62). Column participant totals48 and63 are separately printed; row-specific denominators are explicit45,59,46,61.

**Rule and calculation:** A row labeled No./total No.(%) states a percentage100×numerator/denominator. For each integer numerator n and denominator d, recomputed interval is [100(n−.5)/(d+.5),100(n+.5)/(d−.5)]; the whole-percentage printed interval is [p−.5,p+.5]. The intervals remain separated even under these permissive half-unit input bounds.

| Row / group | Printed pair | Direct ratio,% | Recomputed half-unit interval,% | Printed percentage interval,% | Gap,percentage points | Relative discrepancy |
|---|---|---:|---|---|---:|---:|
| Ineffective cough / HFNC alone |14/45(69)|31.1111|[29.6703,32.5843]|[68.5,69.5]|35.9157|0.52052|
| Ineffective cough / HFNC with NIV |16/59(73)|27.1186|[26.0504,28.2051]|[72.5,73.5]|44.2949|0.60678|
| Abundant secretions / HFNC alone |20/46(57)|43.4783|[41.9355,45.0549]|[56.5,57.5]|11.4451|0.20079|
| Abundant secretions / HFNC with NIV |23/61(62)|37.7049|[36.5854,38.8430]|[61.5,62.5]|22.6570|0.36544|

Each relative discrepancy exceeds0.05. The same within-display count/percentage rule fails across the same hypercapnic block in adjacent rows; this is one consolidated reporting pattern with all four locations, not four separate findings.

**Focus area:** A, counts and denominators.

**Proposed review domain:** statistical_results.

**Proposed relationship type / all relationships:** S_W / S_W.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** Baseline prevalence of ineffective cough and abundant secretions in hypercapnic patients in each randomized arm; an extractor could take69%/73% or57%/62%, whereas the explicit ratios are approximately31%/27% or43%/38%.

**Why context does not resolve it:** The reproduced cells meet the always-register category for counts within one display. Even if the intended percentage can be reconstructed, its printed reading changes magnitude beyond the display-precision threshold and remains an extractable number.

**Source-grounded alternatives:** The adjacent previous-page lung-disease row prints33/48(69) and46/63(73), matching the cough percentage pair. This suggests a possible copied pair but does not establish how the four cells arose. The numerators and available denominators recombine with the nonhypercapnic rows to the main table: cough51+14=65 and70+16=86,239+45=284 and263+59=322; secretions101+20=121 and91+23=114,242+46=288 and265+61=326. An alternative population or percentage definition is not identified in the row labels/footnotes. The observed fact is the arithmetic inconsistency; the production mechanism is an inference and is not needed for inclusion.

**Exact human question:** For the hypercapnic cough and secretion cells in eTable2, which values should be used as the counts, available denominators and percentages, and do the displayed percentages refer to the explicitly printed numerator/denominator pairs or to another population?


